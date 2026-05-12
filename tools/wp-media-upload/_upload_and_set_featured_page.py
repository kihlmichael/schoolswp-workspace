"""One-shot: upload a single image to WP media library and set it as the
featured image of a Page (not Post). Reads credentials in-memory from
.claude/settings.local.json (no .env, no shell export — see
feedback_never_read_env.md and the auto-classifier policy).

Pipeline mimicks tools/wp-media-upload/cli.py but routes the featured-media
call to /wp/v2/pages/{id} instead of /wp/v2/posts/{id}.

Steps:
  1. Backup the source image into backup/<slug>/
  2. Bake EXIF via ExifTool (whitelisted XP* + Copyright + ImageDescription)
  3. POST multipart to /wp/v2/media (strip leading "NN-" prefix from filename)
  4. POST /wp/v2/media/{id} with title/alt/caption/description
  5. POST /wp/v2/pages/{page_id} with {"featured_media": media_id}
  6. Move source to processed/<slug>/

Usage:
  .venv/Scripts/python tools/wp-media-upload/_upload_and_set_featured_page.py \
      --article template-welcome-fluentcrm --file 01-hero-template-welcome-fluentcrm.png
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp")
SETTINGS = ROOT / ".claude" / "settings.local.json"
TOOL = ROOT / "tools" / "wp-media-upload"
INBOX = TOOL / "inbox"
PROCESSED = TOOL / "processed"
BACKUP = TOOL / "backup"
CONFIG_PATH = TOOL / "config.yaml"

ORDERING_PREFIX_RE = re.compile(r"^\d+[-_]")


def strip_ordering_prefix(filename: str) -> str:
    return ORDERING_PREFIX_RE.sub("", filename, count=1)


def _ensure_exiftool_on_path() -> None:
    """ExifTool installed via winget user scope sits outside PATH on Windows
    (cf. reference_exiftool_path.md). Inject the canonical install dir if
    present and exiftool is not already callable."""
    try:
        subprocess.run(["exiftool", "-ver"], capture_output=True, timeout=5, check=False)
        return
    except FileNotFoundError:
        pass
    user = Path.home() / "AppData" / "Local" / "Programs" / "ExifTool"
    if user.exists():
        os.environ["PATH"] = f"{user};{os.environ.get('PATH', '')}"


def load_wp_config() -> tuple[str, str, str]:
    raw = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = raw.get("env", {}) or {}
    url = env["WP_API_URL"].rstrip("/")
    user = env["WP_API_USERNAME"]
    pwd = env["WP_API_PASSWORD"]
    if url.endswith("/wp-json"):
        base = url
    elif "/wp-json" in url:
        base = url.split("/wp-json")[0] + "/wp-json"
    else:
        base = f"{url}/wp-json"
    return base, user, pwd


def load_global_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return {}
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}


def bake_exif(image_path: Path, exif_fields: dict[str, str], whitelist: list[str]) -> bool:
    if not exif_fields:
        return True
    args = ["exiftool", "-overwrite_original", "-charset", "filename=utf8", "-codedcharacterset=utf8"]
    for key, value in exif_fields.items():
        if key not in whitelist:
            print(f"  WARN: EXIF field not whitelisted, skipping: {key}")
            continue
        args.append(f"-{key}={value}")
    args.append(str(image_path))
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=30, check=False, encoding="utf-8")
        if result.returncode != 0:
            print(f"  EXIF FAIL: {result.stderr.strip()[:300]}")
            return False
        print(f"  EXIF baked into {image_path.name}")
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        print(f"  EXIF FAIL: {exc}")
        return False


def upload_media(base: str, auth: tuple[str, str], image_path: Path, timeout: int) -> dict[str, Any]:
    wp_filename = strip_ordering_prefix(image_path.name)
    mime = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
    with image_path.open("rb") as fp:
        files = {"file": (wp_filename, fp, mime)}
        r = requests.post(f"{base}/wp/v2/media", files=files, auth=auth, timeout=timeout)
    if r.status_code not in (200, 201):
        raise RuntimeError(f"Upload failed HTTP {r.status_code}: {r.text[:300]}")
    return r.json()


def patch_media_fields(base: str, auth: tuple[str, str], media_id: int, entry: dict[str, Any], timeout: int) -> None:
    payload = {
        "title": entry.get("title", ""),
        "alt_text": entry.get("alt_text", ""),
        "caption": entry.get("caption", ""),
        "description": entry.get("description", ""),
    }
    r = requests.post(f"{base}/wp/v2/media/{media_id}", json=payload, auth=auth, timeout=timeout)
    if r.status_code not in (200, 201):
        raise RuntimeError(f"Patch fields failed HTTP {r.status_code}: {r.text[:300]}")


def set_featured_page(base: str, auth: tuple[str, str], page_id: int, media_id: int, timeout: int) -> dict[str, Any]:
    r = requests.post(
        f"{base}/wp/v2/pages/{page_id}",
        json={"featured_media": media_id},
        auth=auth,
        timeout=timeout,
    )
    if r.status_code not in (200, 201):
        raise RuntimeError(f"Set featured (page) failed HTTP {r.status_code}: {r.text[:300]}")
    return r.json()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article", required=True, help="Article/page slug (folder name in inbox/)")
    parser.add_argument("--file", required=True, help="Image filename inside the inbox folder")
    parser.add_argument("--no-exif", action="store_true")
    args = parser.parse_args()

    _ensure_exiftool_on_path()
    manifest_path = INBOX / args.article / "manifest.yaml"
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 1
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    entry = next((e for e in manifest.get("images", []) if e.get("file") == args.file), None)
    if entry is None:
        print(f"File entry not found in manifest: {args.file}", file=sys.stderr)
        return 1

    page_id = int(manifest.get("article", {}).get("id", 0))
    if not page_id:
        print("article.id missing in manifest", file=sys.stderr)
        return 1

    source = INBOX / args.article / args.file
    if not source.exists():
        print(f"Source not found: {source}", file=sys.stderr)
        return 1

    base, user, pwd = load_wp_config()
    auth = (user, pwd)
    global_cfg = load_global_config()
    timeout = int(global_cfg.get("request_timeout_seconds", 60))
    exif_whitelist = list(global_cfg.get("exif_fields_whitelist", []))

    backup_dir = BACKUP / args.article
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_target = backup_dir / args.file
    if not backup_target.exists():
        shutil.copy2(source, backup_target)
        print(f"Backup -> {backup_target}")

    if not args.no_exif:
        ok = bake_exif(source, entry.get("exif", {}) or {}, exif_whitelist)
        if not ok:
            print("EXIF bake failed, aborting before upload.", file=sys.stderr)
            return 2

    print(f"Uploading {source.name} to {base}/wp/v2/media ...")
    media = upload_media(base, auth, source, timeout)
    media_id = media["id"]
    media_url = media.get("source_url")
    print(f"  media_id={media_id}  url={media_url}")

    patch_media_fields(base, auth, media_id, entry, timeout)
    print(f"  fields patched (title/alt/caption/description)")

    print(f"Setting featured_media={media_id} on page {page_id} ...")
    page = set_featured_page(base, auth, page_id, media_id, timeout)
    print(f"  page status={page.get('status')} featured_media={page.get('featured_media')}")

    processed_dir = PROCESSED / args.article
    processed_dir.mkdir(parents=True, exist_ok=True)
    dest = processed_dir / args.file
    if not dest.exists():
        shutil.move(str(source), str(dest))
        print(f"Moved -> {dest}")
    time.sleep(0.5)

    print()
    print("DONE")
    print(f"  WP edit page : {base.rsplit('/wp-json',1)[0]}/wp-admin/post.php?post={page_id}&action=edit")
    print(f"  Media URL    : {media_url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""wp-media-upload - Upload images to WordPress with SEO metadata.

Usage:
    python cli.py env-check
    python cli.py list --article <slug>
    python cli.py upload --article <slug> [--dry-run] [--no-exif]
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests
import yaml

ORDERING_PREFIX_RE = re.compile(r"^\d+[-_]")


def strip_ordering_prefix(filename: str) -> str:
    """Remove leading N- or N_ prefix from filename for clean WP URLs.
    Local files keep the prefix for sorting, WP gets clean names.
    """
    return ORDERING_PREFIX_RE.sub("", filename, count=1)


ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "inbox"
PROCESSED = ROOT / "processed"
BACKUP = ROOT / "backup"
LOGS = ROOT / "logs"
CONFIG_PATH = ROOT / "config.yaml"

# Ensure base dirs exist so fresh installs work
for _dir in (INBOX, PROCESSED, BACKUP, LOGS):
    _dir.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOGS / "uploads.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("wp-media-upload")


@dataclass
class WPConfig:
    base_url: str
    username: str
    password: str

    @classmethod
    def from_env(cls) -> "WPConfig":
        url = os.environ.get("WP_API_URL", "").rstrip("/")
        user = os.environ.get("WP_API_USERNAME", "")
        pwd = os.environ.get("WP_API_PASSWORD", "")
        missing = [k for k, v in [("WP_API_URL", url), ("WP_API_USERNAME", user), ("WP_API_PASSWORD", pwd)] if not v]
        if missing:
            raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")
        # Normalize base: we want https://domain.tld/wp-json
        if url.endswith("/wp-json"):
            base = url
        elif "/wp-json" in url:
            base = url.split("/wp-json")[0] + "/wp-json"
        else:
            base = url + "/wp-json"
        return cls(base_url=base, username=user, password=pwd)


def load_global_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return {}
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def exiftool_available() -> bool:
    try:
        result = subprocess.run(
            ["exiftool", "-ver"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def bake_exif(image_path: Path, exif_fields: dict[str, str], whitelist: list[str]) -> bool:
    """Run ExifTool to embed XP/Copyright metadata into the JPEG."""
    if not exif_fields:
        return True
    args = ["exiftool", "-overwrite_original", "-charset", "utf8"]
    for key, value in exif_fields.items():
        if key not in whitelist:
            log.warning("EXIF field not whitelisted, skipping: %s", key)
            continue
        args.append(f"-{key}={value}")
    args.append(str(image_path))
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=30, check=False)
        if result.returncode != 0:
            log.error("ExifTool failed on %s: %s", image_path.name, result.stderr.strip())
            return False
        log.info("ExifTool baked metadata into %s", image_path.name)
        return True
    except subprocess.TimeoutExpired:
        log.error("ExifTool timeout on %s", image_path.name)
        return False


def wp_request(
    config: WPConfig,
    method: str,
    endpoint: str,
    *,
    files: dict | None = None,
    data: dict | None = None,
    json_body: dict | None = None,
    timeout: int = 60,
) -> requests.Response:
    url = f"{config.base_url}{endpoint}"
    auth = (config.username, config.password)
    kwargs: dict[str, Any] = {"auth": auth, "timeout": timeout}
    if files is not None:
        kwargs["files"] = files
    if data is not None:
        kwargs["data"] = data
    if json_body is not None:
        kwargs["json"] = json_body
    return requests.request(method, url, **kwargs)


def cmd_env_check(_args: argparse.Namespace) -> int:
    try:
        config = WPConfig.from_env()
    except RuntimeError as exc:
        print(f"FAIL: {exc}")
        return 1
    print(f"WP_API_URL resolved to: {config.base_url}")
    print(f"WP_API_USERNAME: {config.username}")
    print(f"WP_API_PASSWORD: {'*' * 8} ({len(config.password)} chars)")
    try:
        resp = wp_request(config, "GET", "/wp/v2/users/me", timeout=10)
    except requests.RequestException as exc:
        print(f"FAIL: connection error: {exc}")
        return 1
    if resp.status_code == 200:
        data = resp.json()
        print(f"OK: authenticated as {data.get('name')} (id={data.get('id')})")
    else:
        print(f"FAIL: HTTP {resp.status_code} - {resp.text[:200]}")
        return 1
    if exiftool_available():
        print("ExifTool: found")
    else:
        print("ExifTool: NOT FOUND (install via: winget install OliverBetz.ExifTool)")
    return 0


MANIFEST_TEMPLATE = """# Manifest pour l'article {slug}
# Depose tes JPEG dans ce dossier avec des noms descriptifs (prefixe 01-, 02- optionnel
# pour le tri local - le tool le strippe automatiquement a l'upload).
#
# Commandes utiles :
#   python cli.py list --article {slug}
#   python cli.py upload --article {slug} --dry-run
#   python cli.py upload --article {slug}

article:
  id: 0                # id numerique du post WordPress (0 = pas de featured auto)
  slug: {slug}

images:
  - file: exemple-capture.jpg      # remplace par le nom de ton JPEG
    title: "Titre image 55-60 car - schoolsWP"
    alt_text: "Alt text 120-125 car decrivant l'image, avec mot-cle principal et schoolsWP"
    caption: "Legende 1-2 phrases apparaissant sous l'image dans l'article."
    description: "Description longue 3-4 phrases pour la mediatheque WordPress, contexte editorial et role SEO de l'image."
    featured: true                 # une seule image peut avoir featured: true
    exif:
      XPTitle: "XP Title 50-60 car"
      XPSubject: "Sujet XP - branding schoolsWP"
      XPKeywords: "mot-cle 1, mot-cle 2, schoolsWP, WordPress, ..."
      XPComment: "Commentaire XP sur le role de l'image"
      XPAuthor: "Michael KIHL - schoolsWP"
      Copyright: "(c) ANNEE Michael KIHL - Tous droits reserves"
      ImageDescription: "Description EXIF courte"
"""


def cmd_init(args: argparse.Namespace) -> int:
    slug = args.article
    folder = INBOX / slug
    manifest_path = folder / "manifest.yaml"
    folder.mkdir(parents=True, exist_ok=True)
    if manifest_path.exists() and not args.force:
        print(f"Manifest already exists: {manifest_path}")
        print("Use --force to overwrite.")
        return 1
    manifest_path.write_text(MANIFEST_TEMPLATE.format(slug=slug), encoding="utf-8")
    print(f"Scaffolded: {folder}")
    print("  - manifest.yaml created (template)")
    print()
    print("Next steps:")
    print(f"  1. Drop your JPEGs into: {folder}")
    print("  2. Edit manifest.yaml with real metadata")
    print(f"  3. Run: python cli.py upload --article {slug} --dry-run")
    print(f"  4. Run: python cli.py upload --article {slug}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    folder = INBOX / args.article
    if not folder.exists():
        print(f"No inbox folder for article: {args.article}")
        return 1
    files = sorted(p for p in folder.iterdir() if p.suffix.lower() in ALLOWED_EXTENSIONS)
    manifest = folder / "manifest.yaml"
    print(f"Article: {args.article}")
    print(f"Folder: {folder}")
    print(f"Manifest: {'present' if manifest.exists() else 'MISSING'}")
    print(f"Images ({len(files)}):")
    for p in files:
        size_kb = p.stat().st_size / 1024
        print(f"  - {p.name} ({size_kb:.1f} KB)")
    return 0


def load_manifest(slug: str) -> dict[str, Any]:
    path = INBOX / slug / "manifest.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Manifest not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a YAML mapping")
    if "images" not in data or not isinstance(data["images"], list):
        raise ValueError("Manifest must contain an 'images' list")
    return data


def upload_image_multipart(config: WPConfig, image_path: Path, timeout: int) -> dict[str, Any]:
    # Strip ordering prefix (01-, 02-) from uploaded filename so WP URL is clean
    wp_filename = strip_ordering_prefix(image_path.name)
    mime = "image/jpeg" if image_path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
    with image_path.open("rb") as fp:
        files = {"file": (wp_filename, fp, mime)}
        resp = wp_request(config, "POST", "/wp/v2/media", files=files, timeout=timeout)
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"Upload failed HTTP {resp.status_code}: {resp.text[:300]}")
    return resp.json()


def patch_media_fields(config: WPConfig, media_id: int, entry: dict[str, Any], timeout: int) -> dict[str, Any]:
    payload = {
        "title": entry.get("title", ""),
        "alt_text": entry.get("alt_text", ""),
        "caption": entry.get("caption", ""),
        "description": entry.get("description", ""),
    }
    resp = wp_request(config, "POST", f"/wp/v2/media/{media_id}", json_body=payload, timeout=timeout)
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"Patch media fields failed HTTP {resp.status_code}: {resp.text[:300]}")
    return resp.json()


def set_featured_media(config: WPConfig, post_id: int, media_id: int, timeout: int) -> None:
    resp = wp_request(
        config,
        "POST",
        f"/wp/v2/posts/{post_id}",
        json_body={"featured_media": media_id},
        timeout=timeout,
    )
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"Set featured_media failed HTTP {resp.status_code}: {resp.text[:300]}")


def cmd_upload(args: argparse.Namespace) -> int:
    slug = args.article
    inbox_folder = INBOX / slug
    if not inbox_folder.exists():
        print(f"No inbox folder for article: {slug}")
        return 1

    try:
        manifest = load_manifest(slug)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Manifest error: {exc}")
        return 1

    try:
        config = WPConfig.from_env()
    except RuntimeError as exc:
        print(f"Env error: {exc}")
        return 1

    global_cfg = load_global_config()
    timeout = int(global_cfg.get("request_timeout_seconds", 60))
    sleep_between = float(global_cfg.get("sleep_between_uploads_seconds", 0.5))
    exif_whitelist = list(global_cfg.get("exif_fields_whitelist", []))

    article_info = manifest.get("article", {}) or {}
    article_id = article_info.get("id")

    use_exif = (not args.no_exif) and exiftool_available()
    if args.no_exif:
        log.info("ExifTool disabled by flag")
    elif not exiftool_available():
        log.warning("ExifTool not found, skipping EXIF baking (install: winget install OliverBetz.ExifTool)")

    processed_folder = PROCESSED / slug
    processed_folder.mkdir(parents=True, exist_ok=True)
    backup_folder = BACKUP / slug
    backup_folder.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    featured_media_id: int | None = None

    for entry in manifest["images"]:
        file_name = entry.get("file", "")
        if not file_name:
            log.error("Entry missing 'file' key, skipping")
            continue
        source = inbox_folder / file_name
        dest_processed = processed_folder / file_name
        result = {"file": file_name, "status": "pending", "media_id": None, "url": None, "error": None}

        if dest_processed.exists():
            log.info("Already processed, skipping: %s", file_name)
            result["status"] = "skipped (already processed)"
            results.append(result)
            continue
        if not source.exists():
            log.error("File not found: %s", source)
            result["status"] = "failed"
            result["error"] = "file not found in inbox"
            results.append(result)
            continue

        log.info("Processing: %s", file_name)

        # Auto-backup: copy source to backup/<slug>/ BEFORE any EXIF mutation or move
        backup_target = backup_folder / file_name
        if not backup_target.exists():
            try:
                shutil.copy2(str(source), str(backup_target))
                log.info("Backed up to: %s", backup_target)
            except OSError as exc:
                log.warning("Backup failed (non-blocking): %s", exc)
        else:
            log.info("Backup already exists, skipping: %s", backup_target.name)

        if args.dry_run:
            log.info("DRY-RUN: would bake EXIF=%s, upload to WP, set fields", use_exif)
            result["status"] = "dry-run OK"
            results.append(result)
            continue

        # 1. EXIF bake
        if use_exif:
            exif_fields = entry.get("exif", {}) or {}
            if exif_fields:
                ok = bake_exif(source, exif_fields, exif_whitelist)
                if not ok:
                    result["status"] = "failed"
                    result["error"] = "ExifTool failure"
                    results.append(result)
                    continue

        # 2. Upload multipart
        try:
            media = upload_image_multipart(config, source, timeout)
        except (RuntimeError, requests.RequestException) as exc:
            log.error("Upload failed: %s", exc)
            result["status"] = "failed"
            result["error"] = str(exc)[:300]
            results.append(result)
            continue
        media_id = media.get("id")
        media_url = media.get("source_url")
        log.info("Uploaded: %s -> media_id=%s url=%s", file_name, media_id, media_url)

        # 3. Patch fields
        try:
            patch_media_fields(config, media_id, entry, timeout)
            log.info("Fields patched for media_id=%s", media_id)
        except (RuntimeError, requests.RequestException) as exc:
            log.error("Patch fields failed: %s", exc)
            result["status"] = "uploaded but patch failed"
            result["error"] = str(exc)[:300]
            result["media_id"] = media_id
            result["url"] = media_url
            results.append(result)
            continue

        # 4. Featured flag
        if entry.get("featured") and article_id and featured_media_id is None:
            try:
                set_featured_media(config, int(article_id), int(media_id), timeout)
                featured_media_id = media_id
                log.info("Featured media set: %s on post %s", media_id, article_id)
            except (RuntimeError, requests.RequestException) as exc:
                log.error("Set featured failed: %s", exc)

        # 5. Move to processed
        try:
            shutil.move(str(source), str(dest_processed))
            log.info("Moved to processed: %s", dest_processed)
        except OSError as exc:
            log.error("Move failed (upload was OK): %s", exc)

        result["status"] = "OK"
        result["media_id"] = media_id
        result["url"] = media_url
        results.append(result)

        time.sleep(sleep_between)

    print()
    print(f"Article: {slug}" + (f" (post id={article_id})" if article_id else ""))
    ok_count = sum(1 for r in results if r["status"] == "OK" or r["status"].startswith("dry-run"))
    print(f"Processed {ok_count}/{len(results)} images.")
    print()
    print(f"{'File':<45} | {'Status':<28} | {'Media ID':>8} | URL")
    print("-" * 140)
    for r in results:
        url = r.get("url") or ""
        mid = r.get("media_id") or ""
        print(f"{r['file']:<45} | {r['status']:<28} | {str(mid):>8} | {url}")
    if featured_media_id:
        print()
        print(f"Featured image set: media_id={featured_media_id} on post {article_id}")
    return 0 if all(r["status"] in {"OK", "dry-run OK", "skipped (already processed)"} for r in results) else 2


def main() -> int:
    parser = argparse.ArgumentParser(prog="wp-media-upload")
    sub = parser.add_subparsers(dest="command", required=True)

    p_env = sub.add_parser("env-check", help="Verify env vars and WP connectivity")
    p_env.set_defaults(func=cmd_env_check)

    p_init = sub.add_parser("init", help="Scaffold inbox/<slug>/ with a manifest template")
    p_init.add_argument("--article", required=True, help="Article slug (new folder to create)")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing manifest")
    p_init.set_defaults(func=cmd_init)

    p_list = sub.add_parser("list", help="List images in inbox/<slug>/")
    p_list.add_argument("--article", required=True, help="Article slug (folder name in inbox/)")
    p_list.set_defaults(func=cmd_list)

    p_up = sub.add_parser("upload", help="Upload images for an article")
    p_up.add_argument("--article", required=True, help="Article slug (folder name in inbox/)")
    p_up.add_argument("--dry-run", action="store_true", help="Simulate without calling WP")
    p_up.add_argument("--no-exif", action="store_true", help="Skip ExifTool bake")
    p_up.set_defaults(func=cmd_upload)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

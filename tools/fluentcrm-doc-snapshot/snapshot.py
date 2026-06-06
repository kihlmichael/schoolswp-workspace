"""
FluentCRM doc snapshot to Google Drive.

Scrape https://docs.fluentcrm.com/ pages and upload each as <slug>.md to a
Google Drive folder. Idempotent by default: skips slugs already present.

Usage:
    python snapshot.py --folder-id <drive_folder_id>
    python snapshot.py --folder-id <id> --mode full
    python snapshot.py --folder-id <id> --only mcp-for-ai-agents,sms-automation
    python snapshot.py --folder-id <id> --urls-file custom_urls.json --limit 10

Modes:
    missing  default. Upload only slugs absent from the Drive folder.
    full     re-scrape and replace every slug (deletes existing then creates).
    delta    re-scrape every slug; replace only if content hash differs.

Auth:
    Google Drive: OAuth desktop client. Place secrets at
    ./drive_credentials.json (or set GDRIVE_CREDENTIALS_PATH). First run opens
    a browser to authorize, then saves drive_token.json.
    Firecrawl: API key from FIRECRAWL_API_KEY env var (or .env at project root).

Outputs:
    manifest.json updated each run with per-slug status, file_id, hash, dates.
    snapshot.log human-readable log of the run.

Exit codes:
    0 success (every targeted slug is uploaded or up to date).
    1 partial failure (one or more slugs failed; details in manifest + log).
    2 setup error (missing creds, missing API key, urls file unreadable).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaInMemoryUpload
except ImportError:
    sys.stderr.write(
        "Missing Google API libs. Run: pip install -r requirements.txt\n"
    )
    sys.exit(2)


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_URLS = SCRIPT_DIR / "urls.json"
DEFAULT_MANIFEST = SCRIPT_DIR / "manifest.json"
DEFAULT_LOG = SCRIPT_DIR / "snapshot.log"
DEFAULT_TOKEN = SCRIPT_DIR / "drive_token.json"
DEFAULT_CREDS = SCRIPT_DIR / "drive_credentials.json"

DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive.file"]
FIRECRAWL_ENDPOINT = "https://api.firecrawl.dev/v2/scrape"


def setup_logging(log_path: Path) -> logging.Logger:
    logger = logging.getLogger("fluentcrm-doc-snapshot")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.handlers.clear()
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


def load_env() -> None:
    candidates = [
        SCRIPT_DIR / ".env",
        SCRIPT_DIR.parent.parent / ".env",
    ]
    for path in candidates:
        if path.exists():
            load_dotenv(path)
            return
    load_dotenv()


def get_drive_service(creds_path: Path, token_path: Path) -> Any:
    creds: Credentials | None = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), DRIVE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not creds_path.exists():
                raise FileNotFoundError(
                    f"Drive OAuth client secrets missing at {creds_path}. "
                    "Create an OAuth Desktop client in Google Cloud Console "
                    "and download the JSON to that path, OR set "
                    "GDRIVE_CREDENTIALS_PATH env var to point to it."
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(creds_path), DRIVE_SCOPES
            )
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def list_folder_files(service: Any, folder_id: str) -> dict[str, dict[str, Any]]:
    files: dict[str, dict[str, Any]] = {}
    page_token: str | None = None
    while True:
        resp = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed=false",
                fields="nextPageToken, files(id, name, size, modifiedTime, md5Checksum)",
                pageSize=200,
                pageToken=page_token,
            )
            .execute()
        )
        for f in resp.get("files", []):
            files[f["name"]] = f
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return files


def scrape_page(api_key: str, url: str, logger: logging.Logger) -> str | None:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "waitFor": 2000,
    }
    for attempt in (1, 2):
        try:
            resp = requests.post(
                FIRECRAWL_ENDPOINT, headers=headers, json=payload, timeout=60
            )
            resp.raise_for_status()
            data = resp.json().get("data") or {}
            md = data.get("markdown") or ""
            if md.strip():
                return md
            logger.warning("Empty markdown from %s (attempt %d)", url, attempt)
            payload["waitFor"] = 6000
        except requests.RequestException as exc:
            logger.warning("Scrape error %s (attempt %d): %s", url, attempt, exc)
            time.sleep(2)
    return None


def build_markdown(url: str, slug: str, scraped_at: str, body: str) -> str:
    return (
        "---\n"
        f"source_url: {url}\n"
        f"slug: {slug}\n"
        f"scraped_at: {scraped_at}\n"
        "source: docs.fluentcrm.com\n"
        "---\n\n"
        f"{body}\n"
    )


def md5_hex(content: str) -> str:
    return hashlib.md5(content.encode("utf-8")).hexdigest()


def upload_file(
    service: Any, folder_id: str, name: str, content: str, replace_id: str | None
) -> str:
    media = MediaInMemoryUpload(
        content.encode("utf-8"), mimetype="text/markdown", resumable=False
    )
    if replace_id:
        updated = (
            service.files()
            .update(fileId=replace_id, media_body=media, fields="id")
            .execute()
        )
        return updated["id"]
    metadata = {"name": name, "parents": [folder_id], "mimeType": "text/markdown"}
    created = (
        service.files()
        .create(body=metadata, media_body=media, fields="id")
        .execute()
    )
    return created["id"]


def slug_from_url(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def load_manifest(path: Path) -> dict[str, Any]:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"runs": [], "slugs": {}}
    return {"runs": [], "slugs": {}}


def save_manifest(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--folder-id", required=True, help="Drive folder ID")
    parser.add_argument(
        "--mode",
        choices=("missing", "full", "delta"),
        default="missing",
        help="missing=skip present, delta=replace if hash diff, full=replace all",
    )
    parser.add_argument("--urls-file", default=str(DEFAULT_URLS))
    parser.add_argument(
        "--only", help="Comma-separated slugs to limit the run (intersect with urls)"
    )
    parser.add_argument("--limit", type=int, default=0, help="Cap number of urls")
    parser.add_argument(
        "--target-date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="Used in scraped_at frontmatter",
    )
    parser.add_argument(
        "--credentials",
        default=os.environ.get("GDRIVE_CREDENTIALS_PATH", str(DEFAULT_CREDS)),
    )
    parser.add_argument("--token", default=str(DEFAULT_TOKEN))
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--log", default=str(DEFAULT_LOG))
    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=200,
        help="Pause between Firecrawl calls (rate limit cushion)",
    )
    args = parser.parse_args()

    logger = setup_logging(Path(args.log))
    load_env()

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        logger.error("FIRECRAWL_API_KEY env var missing.")
        return 2

    urls_path = Path(args.urls_file)
    if not urls_path.exists():
        logger.error("urls file not found: %s", urls_path)
        return 2
    urls: list[str] = json.loads(urls_path.read_text(encoding="utf-8"))

    if args.only:
        wanted = {s.strip() for s in args.only.split(",") if s.strip()}
        urls = [u for u in urls if slug_from_url(u) in wanted]
    if args.limit:
        urls = urls[: args.limit]

    logger.info("Run start: %d urls, mode=%s, folder=%s", len(urls), args.mode, args.folder_id)

    try:
        service = get_drive_service(Path(args.credentials), Path(args.token))
    except FileNotFoundError as exc:
        logger.error(str(exc))
        return 2

    existing = list_folder_files(service, args.folder_id)
    logger.info("Folder has %d existing files", len(existing))

    manifest = load_manifest(Path(args.manifest))
    run_started = datetime.now(timezone.utc).isoformat()
    slugs_state: dict[str, Any] = manifest.setdefault("slugs", {})

    counts = {"uploaded": 0, "replaced": 0, "skipped": 0, "failed": 0, "unchanged": 0}
    failures: list[dict[str, str]] = []

    for idx, url in enumerate(urls, 1):
        slug = slug_from_url(url)
        name = f"{slug}.md"
        present = existing.get(name)

        if args.mode == "missing" and present:
            counts["skipped"] += 1
            logger.info("[%3d/%d] skip (present): %s", idx, len(urls), slug)
            continue

        time.sleep(args.sleep_ms / 1000.0)
        body = scrape_page(api_key, url, logger)
        if not body:
            counts["failed"] += 1
            failures.append({"slug": slug, "reason": "empty_or_error"})
            logger.error("[%3d/%d] FAIL scrape: %s", idx, len(urls), slug)
            continue

        content = build_markdown(url, slug, args.target_date, body)
        new_hash = md5_hex(content)

        if args.mode == "delta" and present:
            prev = slugs_state.get(slug, {})
            if prev.get("hash") == new_hash:
                counts["unchanged"] += 1
                logger.info("[%3d/%d] unchanged: %s", idx, len(urls), slug)
                continue

        try:
            replace_id = present["id"] if present and args.mode in ("full", "delta") else None
            file_id = upload_file(service, args.folder_id, name, content, replace_id)
            if replace_id:
                counts["replaced"] += 1
                logger.info("[%3d/%d] replaced: %s (%d bytes)", idx, len(urls), slug, len(content))
            else:
                counts["uploaded"] += 1
                logger.info("[%3d/%d] uploaded: %s (%d bytes)", idx, len(urls), slug, len(content))
            slugs_state[slug] = {
                "url": url,
                "file_id": file_id,
                "bytes": len(content),
                "hash": new_hash,
                "scraped_at": args.target_date,
                "uploaded_at": datetime.now(timezone.utc).isoformat(),
            }
        except HttpError as exc:
            counts["failed"] += 1
            failures.append({"slug": slug, "reason": f"drive_http: {exc}"})
            logger.error("[%3d/%d] FAIL upload %s: %s", idx, len(urls), slug, exc)

    manifest.setdefault("runs", []).append(
        {
            "started_at": run_started,
            "ended_at": datetime.now(timezone.utc).isoformat(),
            "folder_id": args.folder_id,
            "mode": args.mode,
            "target_date": args.target_date,
            "counts": counts,
            "failures": failures,
        }
    )
    save_manifest(Path(args.manifest), manifest)

    logger.info(
        "Done. uploaded=%d replaced=%d unchanged=%d skipped=%d failed=%d",
        counts["uploaded"],
        counts["replaced"],
        counts["unchanged"],
        counts["skipped"],
        counts["failed"],
    )
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Finalize FluentCart uploads to Google Drive (3 buckets unified).

Uses `gws` CLI (Google Workspace CLI, authenticated via keyring) for both
listing existing Drive files and creating new ones. No direct OAuth needed.

Idempotent: lists existing titles per parent and skips matches.
"""
import json
import subprocess
import sys
from pathlib import Path

BUCKETS = [
    {
        "name": "Transcripts",
        "parent_id": "1lJ3OqzAL1SlxIwMeuu_zKzNzYfxI-5or",
        "src_dir": r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-transcripts",
        "title_map": None,  # title = stem
    },
    {
        "name": "Doc Customer",
        "parent_id": "1kRnfMRmMEVWBXPVb3Jq_tO_y6EX2HaOU",
        "src_dir": r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer",
        "title_map": {
            "00-INDEX-doc-customer": "00 - INDEX Doc Customer",
            "01-getting-started": "01 - Getting Started",
            "02-product-types-creation": "02 - Product Types Creation",
            "03-store-management": "03 - Store Management",
            "04-payments-checkout": "04 - Payments Checkout",
            "05-shipping": "05 - Shipping",
            "06-tax-duties": "06 - Tax Duties",
            "07-customer-dashboard": "07 - Customer Dashboard",
            "08-marketing-sales-tools": "08 - Marketing Sales Tools",
            "09-settings-configuration": "09 - Settings Configuration",
            "10-customization-themes": "10 - Customization Themes",
            "11-integrations": "11 - Integrations",
            "12-migration-edd": "12 - Migration EDD",
            "13-reporting-analytics": "13 - Reporting Analytics",
            "14-storage": "14 - Storage",
            "15-troubleshooting-support": "15 - Troubleshooting Support",
            "16-changelog-misc": "16 - Changelog Misc",
        },
    },
    {
        "name": "Doc Developer",
        "parent_id": "1U8VJ3btmHhdex9-YlktlN-Xxk-w-BLTy",
        "src_dir": r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-dev",
        # Pretty title from stem (e.g. "05a-database-models-part1" → "05a - Database Models Part1")
        "title_map": None,
    },
]


def prettify_title(stem: str) -> str:
    """Convert stem 'NN-...' into 'NN - ... Title Case'."""
    parts = stem.split("-", 1)
    if len(parts) == 2:
        prefix = parts[0]
        if prefix[0].isdigit():
            rest = parts[1].replace("-", " ").title()
            return f"{prefix} - {rest}"
    return stem


GWS_BIN = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"


def run_gws(args: list) -> dict:
    """Run gws CLI command and return parsed JSON output. Raises on non-zero exit."""
    proc = subprocess.run(
        [GWS_BIN] + args,
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gws failed (exit {proc.returncode}): {proc.stderr.strip()}")
    # gws prepends a "Using keyring backend: ..." line on stdout — strip it
    out = proc.stdout
    json_start = out.find("{")
    if json_start == -1:
        return {}
    return json.loads(out[json_start:])


def list_existing_titles(parent_id: str) -> set:
    """Return set of titles already in parent (paginated)."""
    titles = set()
    page_token = None
    while True:
        params = {
            "q": f"'{parent_id}' in parents and trashed=false",
            "pageSize": 200,
            "fields": "nextPageToken,files(id,name)",
        }
        if page_token:
            params["pageToken"] = page_token
        result = run_gws(["drive", "files", "list", "--params", json.dumps(params)])
        for f in result.get("files", []):
            titles.add(f["name"])
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    return titles


def upload_file(file_path: Path, title: str, parent_id: str) -> str:
    """Upload via gws drive files create. Returns file_id."""
    metadata = {
        "name": title,
        "parents": [parent_id],
        "mimeType": "text/markdown",
    }
    result = run_gws([
        "drive", "files", "create",
        "--upload", str(file_path),
        "--upload-content-type", "text/markdown",
        "--json", json.dumps(metadata),
    ])
    return result["id"]


def process_bucket(bucket: dict):
    src = Path(bucket["src_dir"])
    if not src.is_dir():
        print(f"[{bucket['name']}] Source dir missing: {src}")
        return 0, 0, 0
    print(f"\n=== {bucket['name']} ===")
    print(f"  Source : {src}")
    print(f"  Parent : {bucket['parent_id']}")
    print(f"  Listing existing Drive titles...")
    existing = list_existing_titles(bucket["parent_id"])
    print(f"  -> {len(existing)} files already on Drive")

    md_files = sorted(src.glob("*.md"))
    print(f"  -> {len(md_files)} .md files locally")

    uploaded = skipped = failed = 0
    for f in md_files:
        stem = f.stem
        if bucket["title_map"]:
            title = bucket["title_map"].get(stem, prettify_title(stem))
        else:
            title = prettify_title(stem) if bucket["name"] == "Doc Developer" else stem
        if title in existing:
            skipped += 1
            print(f"  SKIP  {title}")
            continue
        try:
            fid = upload_file(f, title, bucket["parent_id"])
            uploaded += 1
            size_kb = f.stat().st_size / 1024
            print(f"  OK    {title}  ({size_kb:.0f} KB)  -> id={fid}")
        except Exception as e:
            failed += 1
            print(f"  FAIL  {title}: {e}")
    return uploaded, skipped, failed


def main():
    print("=== FluentCart Finalize Uploads (via gws CLI) ===")
    totals = [0, 0, 0]
    for bucket in BUCKETS:
        u, s, fai = process_bucket(bucket)
        totals[0] += u
        totals[1] += s
        totals[2] += fai

    print("\n=== TOTALS ===")
    print(f"  Uploaded : {totals[0]}")
    print(f"  Skipped  : {totals[1]} (already on Drive)")
    print(f"  Failed   : {totals[2]}")


if __name__ == "__main__":
    main()

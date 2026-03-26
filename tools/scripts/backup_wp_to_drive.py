"""
Backup WordPress FR articles to Google Drive.
Fetches all published FR articles from schoolswp.com,
compares with existing Drive files, and creates Google Docs
for missing articles in the correct category subfolder.
"""

import html
import json
import os
import re
import subprocess
import sys
import time

import requests

# Force UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Config
WP_API = "https://schoolswp.com/wp-json/wp/v2"
DRIVE_PARENT_ID = "1oFMl1i2no8uSyl9sHNjqPxmXj7W4uFCe"

# Category slug -> Drive folder ID mapping
DRIVE_FOLDERS = {
    "guides-wordpress": "1UO2lSGAWDEIX0jbdhJ9AVIAshyJSo2kT",
    "design-wordpress": "19aKXHHUhwx7UHeUq5rBw0Xf7yFW9-ENL",
    "ecommerce-wordpress": "1q7KYdx5KCS7vngEgIami0SW812jn71HK",
    "monetisation-wordpress": "1Yk_INm-S_KpPFHxKwan9L7FZPraOYDhW",
    "formulaires-crm": "1go2fZE228r66FPtUjKi5tSfxTq8Vn_-H",
    "seo-wordpress": "1gz3PfsIo6RuXw6hJpQ7_OCtztbbxvWQ9",
    "hebergement-wordpress": "1WUOg45Rn5x2I0Cw24PVBHG8DUJ_CqHQu",
    "espaces-membres-wordpress": "1fQZqXJ3QONX8XLXrrErHrQ3mZy9j4TKs",
    "performance-wordpress": "1NAP3clSxUPAYg8Mb3vRux9UQCkM_dT1t",
    "reservations-wordpress": "1UfMfugM1gL01cNtoQqa2gLWoDO2YaXMT",
    "ia-wordpress": "1UP0VYEEs_E6tMS2hlSm-8qq-c0nC97nF",
    "maintenance-securite-wordpress": "1IP6Sx5Naw9dBvS8AekYiqepO7BepmJnp",
    "formation-en-ligne-lms": "1y7uCMOBu1b0cxpiyFASZRA3t99LOeJ_r",
    "automatisations-wordpress": "1Fd0CuzJjaJHLFAMfADIxaHOe-vQK4_zP",
    "autres": "18pidgU-o1MakWSnYdkMd4kli1pQp85to",
}

# Parent category slug -> Drive folder slug mapping
PARENT_CAT_SLUG_MAP = {}


def gws_cmd(service, resource, action, params=None, json_body=None):
    """Run a gws CLI command and return parsed JSON."""
    gws_path = os.path.expandvars(r"%APPDATA%\npm\gws.cmd")
    if not os.path.exists(gws_path):
        gws_path = "gws"
    cmd = [gws_path, service, resource, action]
    if params:
        cmd += ["--params", json.dumps(params)]
    if json_body:
        cmd += ["--json", json.dumps(json_body)]
    result = subprocess.run(
        cmd, capture_output=True, timeout=30, encoding="utf-8", errors="replace"
    )
    stdout = result.stdout or ""
    if result.returncode != 0:
        return None
    try:
        output = stdout.strip()
        json_start = output.find("{")
        if json_start >= 0:
            return json.loads(output[json_start:])
    except json.JSONDecodeError:
        pass
    return None


def get_fr_categories():
    """Fetch all FR categories and build ID->slug mapping."""
    cats = {}
    page = 1
    while True:
        r = requests.get(
            f"{WP_API}/categories",
            params={"per_page": 100, "page": page},
            timeout=30,
        )
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        for c in data:
            cats[c["id"]] = {
                "slug": c["slug"],
                "name": c["name"],
                "parent": c["parent"],
            }
        page += 1
    return cats


def get_parent_slug(cat_id, all_cats):
    """Get the parent category slug for a given category ID."""
    cat = all_cats.get(cat_id)
    if not cat:
        return "autres"
    if cat["parent"] == 0:
        return cat["slug"]
    parent = all_cats.get(cat["parent"])
    if parent:
        return parent["slug"]
    return cat["slug"]


def get_all_fr_posts(all_cats):
    """Fetch all published FR posts."""
    fr_cat_ids = set(all_cats.keys())
    # FR parent category IDs (parent=0 and slug matches our Drive folders)
    fr_parent_slugs = set(DRIVE_FOLDERS.keys())
    fr_parent_ids = {
        cid
        for cid, c in all_cats.items()
        if c["parent"] == 0 and c["slug"] in fr_parent_slugs
    }
    # Also include children of FR parent categories
    fr_family_ids = set(fr_parent_ids)
    for cid, c in all_cats.items():
        if c["parent"] in fr_parent_ids:
            fr_family_ids.add(cid)

    posts = []
    page = 1
    while True:
        r = requests.get(
            f"{WP_API}/posts",
            params={
                "per_page": 100,
                "page": page,
                "status": "publish",
                "_fields": "id,title,slug,categories,date,link",
            },
            timeout=30,
        )
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        for p in data:
            post_cats = set(p.get("categories", []))
            if post_cats & fr_family_ids:
                posts.append(p)
        page += 1
    return posts


def get_existing_drive_files():
    """Get all existing file names in Drive article subfolders."""
    existing = set()
    for slug, folder_id in DRIVE_FOLDERS.items():
        result = gws_cmd(
            "drive",
            "files",
            "list",
            params={
                "q": f"'{folder_id}' in parents and trashed = false",
                "fields": "files(name)",
                "pageSize": 200,
            },
        )
        if result and "files" in result:
            for f in result["files"]:
                # Normalize: extract slug from file name
                name = f["name"].lower().strip()
                existing.add(name)
    return existing


def map_post_to_folder(post, all_cats):
    """Determine which Drive folder a post belongs to."""
    for cat_id in post.get("categories", []):
        parent_slug = get_parent_slug(cat_id, all_cats)
        if parent_slug in DRIVE_FOLDERS:
            return parent_slug
    return "autres"


def create_doc_in_drive(title, folder_id):
    """Create a Google Doc in a specific Drive folder."""
    # Create doc via Docs API
    result = gws_cmd("docs", "documents", "create", json_body={"title": title})
    if not result or "documentId" not in result:
        return None
    doc_id = result["documentId"]

    # Move to correct folder
    gws_cmd(
        "drive",
        "files",
        "update",
        params={
            "fileId": doc_id,
            "addParents": folder_id,
            "removeParents": "root",
        },
        json_body={},
    )
    return doc_id


def main():
    print("=" * 60)
    print("BACKUP WordPress FR -> Google Drive")
    print("=" * 60)

    # Step 1: Get categories
    print("\n[1/4] Fetching WordPress categories...")
    all_cats = get_fr_categories()
    print(f"  {len(all_cats)} categories loaded")

    # Step 2: Get FR posts
    print("\n[2/4] Fetching FR published posts...")
    fr_posts = get_all_fr_posts(all_cats)
    print(f"  {len(fr_posts)} FR posts found")

    # Step 3: Get existing Drive files
    print("\n[3/4] Scanning existing Drive files...")
    existing = get_existing_drive_files()
    print(f"  {len(existing)} files already in Drive")

    # Step 4: Find missing posts and create docs
    print("\n[4/4] Creating missing articles in Drive...")
    created = 0
    skipped = 0
    errors = 0

    for post in fr_posts:
        title_raw = post["title"]["rendered"]
        # Clean ALL HTML entities in one pass
        title_clean = html.unescape(title_raw)
        # Remove any remaining HTML tags
        title_clean = re.sub(r"<[^>]+>", "", title_clean)
        date = post["date"][:10]
        slug = post["slug"]

        # Build Drive-compatible name
        drive_name = f"{date} - {title_clean} - Article - FR - Contenu - Publies"

        # Check if already exists (match by slug in existing file names)
        already_exists = False
        slug_parts = slug.replace("-", " ").lower()
        for existing_name in existing:
            # Check if slug words appear in the existing file name
            existing_lower = existing_name.lower()
            if slug in existing_lower or slug_parts[:30] in existing_lower:
                already_exists = True
                break

        if already_exists:
            skipped += 1
            continue

        # Determine folder
        folder_slug = map_post_to_folder(post, all_cats)
        folder_id = DRIVE_FOLDERS.get(folder_slug, DRIVE_FOLDERS["autres"])

        # Create doc
        doc_id = create_doc_in_drive(drive_name, folder_id)
        if doc_id:
            created += 1
            print(f"  + [{folder_slug}] {drive_name[:70]}...")
        else:
            errors += 1
            print(f"  ! ERREUR: {drive_name[:70]}...")

        # Rate limiting (Google API quota)
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"DONE: {created} created, {skipped} skipped (already exist), {errors} errors")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

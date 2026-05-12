"""Fetch a WordPress post + featured image. Reads creds from .env without exposing them.

Usage:
    python tools/scripts/fetch_post_image.py <post_id> [--download-to <dir>]

Behaviour:
- Loads .env from project root.
- Tries auth combos in order: (WP_API_USERNAME, WP_API_PASSWORD),
  (WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD), (WP_USER, WP_APP_PASSWORD).
- Logs ONLY: post title, slug, link, featured_media id, featured image URL,
  and downloaded file path. Never logs env var names or values.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

AUTH_PAIRS = [
    ("WP_API_USERNAME", "WP_API_PASSWORD"),
    ("WORDPRESS_USERNAME", "WORDPRESS_APP_PASSWORD"),
    ("WP_USER", "WP_APP_PASSWORD"),
    ("NOVAMIRA_USER", "NOVAMIRA_APP_PASSWORD"),
]

WP_BASE_CANDIDATES = [
    os.environ.get("WP_API_URL", "").rstrip("/"),
    "https://schoolswp.com/wp-json",
]


def pick_auth() -> tuple[str, str] | None:
    for u_key, p_key in AUTH_PAIRS:
        u, p = os.environ.get(u_key), os.environ.get(p_key)
        if u and p:
            return (u, p)
    return None


def pick_base() -> str:
    for b in WP_BASE_CANDIDATES:
        if not b:
            continue
        if b.endswith("/wp-json"):
            return b
        if "/wp-json" in b:
            return b.split("/wp-json")[0] + "/wp-json"
        return b.rstrip("/") + "/wp-json"
    return "https://schoolswp.com/wp-json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("post_ref", help="Post ID (int) or slug")
    ap.add_argument("--download-to", default=str(ROOT / "tools" / "scripts" / "_tmp_images"))
    ap.add_argument("--context", default="edit", help="REST context: view|edit (edit needs auth)")
    ap.add_argument("--skip-download", action="store_true", help="Don't download the featured image")
    args = ap.parse_args()

    auth = pick_auth()
    if not auth:
        print("ERROR: no WP credentials found in .env (expected one of: "
              "WP_API_USERNAME/PASSWORD, WORDPRESS_USERNAME/APP_PASSWORD, "
              "WP_USER/APP_PASSWORD, NOVAMIRA_USER/APP_PASSWORD)", file=sys.stderr)
        return 2

    base = pick_base()

    # Resolve slug -> id if needed
    post_ref = args.post_ref
    try:
        post_id = int(post_ref)
    except ValueError:
        slug = post_ref.strip("/").split("/")[-1] if "/" in post_ref else post_ref.strip("/")
        lookup = requests.get(f"{base}/wp/v2/posts?slug={slug}&context={args.context}", auth=auth, timeout=30)
        if lookup.status_code != 200 or not lookup.json():
            # Try pages
            lookup = requests.get(f"{base}/wp/v2/pages?slug={slug}&context={args.context}", auth=auth, timeout=30)
            if lookup.status_code != 200 or not lookup.json():
                print(f"ERROR: slug '{slug}' not found in posts or pages", file=sys.stderr)
                return 4
        post_id = lookup.json()[0].get("id")

    post_url = f"{base}/wp/v2/posts/{post_id}?context={args.context}&_embed=1"
    r = requests.get(post_url, auth=auth, timeout=30)
    if r.status_code == 401 or r.status_code == 403:
        print(f"ERROR: auth failed ({r.status_code}) on {post_url}", file=sys.stderr)
        return 3
    if r.status_code == 404:
        # Try pages endpoint
        page_url = f"{base}/wp/v2/pages/{post_id}?context={args.context}&_embed=1"
        r = requests.get(page_url, auth=auth, timeout=30)
        if r.status_code != 200:
            print(f"ERROR: post {post_id} not found in posts or pages ({r.status_code})", file=sys.stderr)
            return 4
    r.raise_for_status()
    data = r.json()
    args.post_id = post_id

    title = data.get("title", {}).get("rendered") or data.get("title", {}).get("raw") or "(no title)"
    slug = data.get("slug", "")
    link = data.get("link", "")
    status = data.get("status", "")
    fm_id = data.get("featured_media", 0)
    post_type = data.get("type", "")
    excerpt = (data.get("excerpt") or {}).get("rendered", "")
    lang = data.get("lang", "")
    categories = data.get("categories", [])
    yoast_meta = data.get("yoast_head_json", {})
    meta_desc = yoast_meta.get("description", "") if isinstance(yoast_meta, dict) else ""

    print(f"POST_ID:     {args.post_id}")
    print(f"TYPE:        {post_type}")
    print(f"STATUS:      {status}")
    print(f"TITLE:       {title}")
    print(f"SLUG:        {slug}")
    print(f"LINK:        {link}")
    print(f"LANG:        {lang}")
    print(f"CATEGORIES:  {categories}")
    print(f"META_DESC:   {meta_desc[:200]}")
    print(f"EXCERPT:     {excerpt[:200]}")
    print(f"FEATURED_ID: {fm_id}")

    if not fm_id:
        print("No featured media on this post.")
        return 0

    if args.skip_download:
        return 0

    media_url = f"{base}/wp/v2/media/{fm_id}?context={args.context}"
    rm = requests.get(media_url, auth=auth, timeout=30)
    rm.raise_for_status()
    media = rm.json()

    source_url = media.get("source_url", "")
    alt = media.get("alt_text", "")
    caption = (media.get("caption") or {}).get("rendered", "")
    mime = media.get("mime_type", "")
    sizes = (media.get("media_details") or {}).get("sizes", {})
    full = sizes.get("full", {})

    print(f"IMAGE_URL:   {source_url}")
    print(f"ALT:         {alt}")
    print(f"MIME:        {mime}")
    print(f"DIMENSIONS:  {full.get('width', '?')}x{full.get('height', '?')}")

    # Download
    out_dir = Path(args.download_to)
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = Path(urlparse(source_url).path).name or f"post-{args.post_id}-featured.bin"
    out_path = out_dir / fname
    rd = requests.get(source_url, timeout=60)
    rd.raise_for_status()
    out_path.write_bytes(rd.content)
    print(f"DOWNLOADED:  {out_path}")
    print(f"BYTES:       {len(rd.content)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

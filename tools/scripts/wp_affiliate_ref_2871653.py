#!/usr/bin/env python3
"""
Append ?ref=723 to every fluentcrm.com link in post 2871653 content.
- Re-fetches the LIVE post first (so we patch the latest state, not stale local copy)
- Idempotent: skips URLs that already contain ref=723
- Preserves existing query strings (adds &ref=723) and #anchors (places ?ref=723 before #)
- Dry-run mode by default. Pass --push to actually update.
"""

import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 2871653
SITE = "https://schoolswp.com"
AFFILIATE_PARAM = "ref"
AFFILIATE_VALUE = "723"
SAVE_DIR = ROOT / "content" / "articles" / "_workspace"
SAVE_DIR.mkdir(parents=True, exist_ok=True)


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth():
    u, p = load_creds()
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()


def fetch_post():
    req = urllib.request.Request(
        f"{SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit",
        headers={"Authorization": auth(), "Accept": "application/json",
                 "User-Agent": "schoolswp-fetcher/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def push_content(content):
    payload = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        f"{SITE}/wp-json/wp/v2/posts/{POST_ID}",
        method="POST",
        data=payload,
        headers={"Authorization": auth(), "Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "schoolswp-fetcher/1.0"},
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def add_ref(url):
    """Add ?ref=723 to a fluentcrm.com URL preserving existing query and anchor."""
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.lower() not in ("fluentcrm.com", "www.fluentcrm.com"):
        return url, False
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    # Idempotence: skip if already has our ref
    for k, v in q:
        if k == AFFILIATE_PARAM and v == AFFILIATE_VALUE:
            return url, False
    q.append((AFFILIATE_PARAM, AFFILIATE_VALUE))
    new_query = urllib.parse.urlencode(q)
    new = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment))
    return new, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true", help="actually push the update (default = dry-run)")
    args = ap.parse_args()

    print(f"[fetch] GET {SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit")
    post = fetch_post()
    c = post["content"]["raw"]
    print(f"        current content: {len(c)} chars, modified: {post.get('modified')}")

    # Extract every href on fluentcrm.com (case-insensitive scheme)
    pattern = re.compile(r'href="(https?://(?:www\.)?fluentcrm\.com[^"]*)"', re.IGNORECASE)
    urls = pattern.findall(c)
    unique = sorted(set(urls))
    print(f"\nFound {len(urls)} fluentcrm.com hrefs ({len(unique)} unique).")
    for u in unique:
        new, changed = add_ref(u)
        marker = " (already has ref=723)" if not changed else f"  ->  {new}"
        print(f"  {u}{marker}")

    # Build new content
    def repl(m):
        url = m.group(1)
        new, _ = add_ref(url)
        return f'href="{new}"'

    new_c = pattern.sub(repl, c)
    delta = len(new_c) - len(c)
    print(f"\nDelta chars: {delta:+d}")

    # Save preview
    preview = SAVE_DIR / "post-2871653-ref723-preview.json"
    preview.write_text(json.dumps({"content": new_c}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[preview] saved -> {preview}")

    if not args.push:
        print("\n[dry-run] no push performed. Re-run with --push to apply.")
        return

    print("\n[push] sending update...")
    status, d = push_content(new_c)
    print(f"[push] HTTP {status}")
    print(f"       modified : {d.get('modified')}")
    print(f"       content  : {len(d.get('content', {}).get('raw', ''))} chars")


if __name__ == "__main__":
    main()

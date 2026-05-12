#!/usr/bin/env python3
"""
Push enriched content (post-2871653-enriched.json) back to schoolswp.com draft 2871653.
Preserves status=draft. Does NOT touch Rank Math meta, categories, tags, slug, title.
Only updates `content`.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
ENRICHED = ROOT / "content" / "articles" / "_workspace" / "post-2871653-enriched.json"
POST_ID = 2871653
SITE = "https://schoolswp.com"


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth():
    u, p = load_creds()
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()


def main():
    data = json.loads(ENRICHED.read_text(encoding="utf-8"))
    new_content = data["content"]["raw"]
    print(f"[push] payload : {len(new_content)} chars to POST -> {SITE}/wp-json/wp/v2/posts/{POST_ID}")

    payload = json.dumps({"content": new_content}).encode("utf-8")
    req = urllib.request.Request(
        f"{SITE}/wp-json/wp/v2/posts/{POST_ID}",
        method="POST",
        data=payload,
        headers={
            "Authorization": auth(),
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "schoolswp-fetcher/1.0",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            body = r.read().decode("utf-8")
            d = json.loads(body)
            print(f"[push] HTTP {r.status} OK")
            print(f"       title    : {d.get('title', {}).get('raw', '')[:120]}")
            print(f"       status   : {d.get('status', '')}")
            print(f"       modified : {d.get('modified', '')}")
            print(f"       content  : {len(d.get('content', {}).get('raw', ''))} chars")
            print(f"       link     : {d.get('link', '')}")
    except urllib.error.HTTPError as e:
        print(f"[push] HTTP {e.code}: {e.read().decode('utf-8', errors='replace')[:1000]}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

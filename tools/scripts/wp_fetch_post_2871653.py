#!/usr/bin/env python3
"""
Fetch post 2871653 from schoolswp.com WP REST (raw edit context).
Writes content to content/articles/_workspace/post-2871653-current.json.
Credentials from .claude/settings.local.json (env block). Never echoed.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT_DIR = ROOT / "content" / "articles" / "_workspace"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "post-2871653-current.json"
POST_ID = 2871653
SITE = "https://schoolswp.com"


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, app_pw):
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    return f"Basic {token}"


def main():
    try:
        user, pw = load_creds()
    except KeyError as e:
        print(f"[fetch] Missing key in settings.local.json env: {e}", file=sys.stderr)
        sys.exit(2)

    url = f"{SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit"
    req = urllib.request.Request(url, headers={
        "Authorization": auth_header(user, pw),
        "Accept": "application/json",
        "User-Agent": "schoolswp-fetcher/1.0",
    })

    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"[fetch] HTTP {e.code}: {e.read().decode('utf-8', errors='replace')[:500]}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(body)
    OUT_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[fetch] OK -> {OUT_FILE}")
    print(f"        title    : {data.get('title', {}).get('raw', '')[:120]}")
    print(f"        slug     : {data.get('slug', '')}")
    print(f"        status   : {data.get('status', '')}")
    print(f"        modified : {data.get('modified', '')}")
    print(f"        content  : {len(data.get('content', {}).get('raw', ''))} chars")


if __name__ == "__main__":
    main()

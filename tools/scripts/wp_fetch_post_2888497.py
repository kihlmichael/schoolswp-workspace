#!/usr/bin/env python3
"""
Fetch post 2888497 (DE) from schoolswp.com WP REST (raw edit context) + Rank Math meta.
Writes content to content/articles/_workspace/post-2888497-current.json.
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
OUT_FILE = OUT_DIR / "post-2888497-current.json"
OUT_META = OUT_DIR / "post-2888497-rankmath.json"
POST_ID = 2888497
SITE = "https://schoolswp.com"


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, app_pw):
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    return f"Basic {token}"


def http_get(url, auth):
    req = urllib.request.Request(url, headers={
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-fetcher/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    try:
        user, pw = load_creds()
    except KeyError as e:
        print(f"[fetch] Missing key in settings.local.json env: {e}", file=sys.stderr)
        sys.exit(2)

    auth = auth_header(user, pw)

    # 1) Post raw
    try:
        data = http_get(f"{SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth)
    except urllib.error.HTTPError as e:
        print(f"[fetch] HTTP {e.code}: {e.read().decode('utf-8', errors='replace')[:500]}", file=sys.stderr)
        sys.exit(1)

    OUT_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[fetch] OK -> {OUT_FILE}")
    print(f"        title    : {data.get('title', {}).get('raw', '')[:160]}")
    print(f"        slug     : {data.get('slug', '')}")
    print(f"        status   : {data.get('status', '')}")
    print(f"        modified : {data.get('modified', '')}")
    print(f"        content  : {len(data.get('content', {}).get('raw', ''))} chars")
    print(f"        excerpt  : {len(data.get('excerpt', {}).get('raw', ''))} chars")

    # 2) Rank Math meta (best-effort, may 404)
    try:
        meta = http_get(f"{SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit&_fields=meta,rank_math", auth)
        OUT_META.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[fetch] meta -> {OUT_META}")
    except Exception as e:
        print(f"[fetch] meta fetch skipped: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

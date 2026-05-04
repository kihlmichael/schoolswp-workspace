#!/usr/bin/env python3
"""
Push optimized v4 content to post 52944 (/creer-plateforme-formation-wordpress/).
Reads credentials from .claude/settings.local.json (env block).
Does NOT echo credentials anywhere.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
HTML_FILE = ROOT / "content" / "articles" / "lms-pilier" / "v4-gutenberg.html"
POST_ID = 52944


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, app_pw):
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    return f"Basic {token}"


def read_html_body():
    raw = HTML_FILE.read_text(encoding="utf-8")
    # Strip the leading banner comment (between the first "<!--" and "-->")
    import re

    # Remove the top file-level comment blocks (our instructions),
    # but KEEP section-separator comments so they remain as trail in the editor.
    # Actually, WP will strip HTML comments on render anyway. But for the "Gutenberg
    # code editor" path we want pure content. Let's strip ALL html comments to keep
    # the block cleaner.
    cleaned = re.sub(r"<!--.*?-->", "", raw, flags=re.DOTALL)
    # Collapse triple+ newlines to doubles
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def patch_post(user, pw, payload):
    url = f"https://schoolswp.com/wp-json/wp/v2/posts/{POST_ID}"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": auth_header(user, pw),
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main():
    user, pw = load_creds()
    body = read_html_body()
    print(f"[info] HTML body chars: {len(body)}")
    print(f"[info] Target: post {POST_ID}")
    payload = {"content": body}
    status, resp = patch_post(user, pw, payload)
    if status == 200:
        print("[ok] HTTP 200 — post updated")
        if isinstance(resp, dict):
            print(f"[ok] modified: {resp.get('modified')}")
            print(f"[ok] link: {resp.get('link')}")
            print(f"[ok] content len (rendered): {len(resp.get('content', {}).get('rendered', ''))}")
    else:
        print(f"[error] HTTP {status}")
        print(resp if isinstance(resp, str) else json.dumps(resp, indent=2)[:2000])
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Inspect post 59051 (/en/learndash-review/) raw content.
Locate [CTA_STANDARD] placeholder + duplicated Pinterest iframes.
Print context to plan the patch. No write.
"""

import base64
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 59051
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http_get(url, user, pw):
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Authorization": auth_header(user, pw),
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def main():
    user, pw = load_creds()
    status, post = http_get(f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status != 200:
        print(f"[error] GET {status}")
        sys.exit(1)

    raw = post["content"]["raw"]
    print(f"[info] post {POST_ID} raw len={len(raw)}")

    # Save raw for inspection
    out = ROOT / "tools" / "scripts" / "_tmp_59051_raw.html"
    out.write_text(raw, encoding="utf-8")
    print(f"[info] raw saved to {out}")

    # 1. [CTA_STANDARD] placeholder
    idx = raw.find("[CTA_STANDARD]")
    print(f"\n=== [CTA_STANDARD] @ offset {idx} ===")
    if idx >= 0:
        before = raw[max(0, idx - 300) : idx]
        after = raw[idx : idx + 100]
        print("--- 300 chars before ---")
        print(repr(before))
        print("--- placeholder + 100 chars after ---")
        print(repr(after))

    # 2. Pinterest iframes - find all
    pin_re = re.compile(r'<iframe[^>]+pinterest[^>]+id=(\d+)[^>]*>.*?</iframe>', re.DOTALL)
    pins = list(re.finditer(r'assets\.pinterest\.com/ext/embed\.html\?id=(\d+)', raw))
    print(f"\n=== Pinterest embeds: {len(pins)} found ===")
    for m in pins:
        print(f"  offset {m.start()}: pin id={m.group(1)}")

    # Find the wp-block-columns wrapping them
    col_re = re.compile(r'<!-- wp:columns.*?<!-- /wp:columns -->', re.DOTALL)
    for m in col_re.finditer(raw):
        block = m.group(0)
        if 'pinterest' in block:
            print(f"\n=== wp:columns block @ {m.start()}..{m.end()} ({len(block)} chars) ===")
            print(block[:1200])
            if len(block) > 1200:
                print(f"... [{len(block)-1200} more chars] ...")
                print(block[-400:])


if __name__ == "__main__":
    main()

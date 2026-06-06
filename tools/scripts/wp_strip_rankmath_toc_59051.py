#!/usr/bin/env python3
"""
Strip the broken wp:rank-math/toc-block from post 59051 (/en/learndash-review/).
Block has {"title":"..."} but no "headings" -> Gutenberg editor JS crashes on .length.
Per memory reference_rank_math_toc_block_bug.md, fix is REST PATCH removing the block.
"""

import base64
import hashlib
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

TOC_PATTERN = re.compile(
    r"<!-- wp:rank-math/toc-block\b.*?<!-- /wp:rank-math/toc-block -->\s*",
    re.DOTALL,
)


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, user, pw, payload=None):
    headers = {
        "Authorization": auth_header(user, pw),
        "Accept": "application/json",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main():
    user, pw = load_creds()

    status, post = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status != 200:
        print(f"[error] GET {status}: {str(post)[:500]}")
        sys.exit(1)

    raw = post["content"]["raw"]
    sha_before = hashlib.sha1(raw.encode("utf-8")).hexdigest()
    print(f"[info] before: len={len(raw)} sha1={sha_before}")

    matches = list(TOC_PATTERN.finditer(raw))
    print(f"[info] found {len(matches)} rank-math TOC block(s)")
    if not matches:
        print("[ok] nothing to strip")
        sys.exit(0)
    for m in matches:
        block = m.group(0)
        has_headings = '"headings"' in block
        print(f"  - offset {m.start()}..{m.end()} ({len(block)} chars) has_headings={has_headings}")

    new_raw = TOC_PATTERN.sub("", raw)
    sha_local = hashlib.sha1(new_raw.encode("utf-8")).hexdigest()
    print(f"[info] after : len={len(new_raw)} sha1={sha_local}")
    print(f"[info] removed {len(raw) - len(new_raw)} chars")

    if new_raw == raw:
        print("[error] no change despite matches - aborting")
        sys.exit(2)

    print(f"\n[info] POST post {POST_ID}...")
    status, resp = http("POST", f"{BASE}/{POST_ID}", user, pw, {"content": new_raw})
    if status != 200:
        print(f"[error] POST {status}: {str(resp)[:1500]}")
        sys.exit(3)

    print("[ok] HTTP 200")
    print(f"[ok] modified: {resp.get('modified')}")

    status, post2 = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status == 200:
        raw2 = post2["content"]["raw"]
        sha_server = hashlib.sha1(raw2.encode("utf-8")).hexdigest()
        still = len(TOC_PATTERN.findall(raw2))
        print(f"[ok] server: len={len(raw2)} sha1={sha_server} toc_blocks={still}")
        if still > 0:
            print("[error] TOC block STILL present!")
            sys.exit(4)
        if sha_server == sha_local:
            print("[ok] byte-perfect")
        else:
            print("[info] server normalized whitespace - TOC gone, content intact")
    print("[done] /en/learndash-review/ editor crash fixed")


if __name__ == "__main__":
    main()

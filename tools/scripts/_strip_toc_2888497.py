#!/usr/bin/env python3
"""Strip broken wp:rank-math/toc-block from post 2888497.

Per reference_rank_math_toc_block_bug.md: TOC block injected via REST without a
populated `headings` attribute crashes Gutenberg's save() on .length read.
Fix: strip the block, leave audit recommendation to Michael who'll add it via UI.
"""

import base64
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
WORKSPACE = ROOT / "content" / "articles" / "_workspace"
POST_ID = 2888497
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"

TOC_PATTERN = re.compile(
    r"\n*<!-- wp:rank-math/toc-block\b[\s\S]*?<!-- /wp:rank-math/toc-block -->\n*",
)


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, auth, payload=None):
    headers = {
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-fixer/1.0",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    # 1) Backup current state
    st, post = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    if st != 200:
        print(f"[error] GET {st}", file=sys.stderr)
        sys.exit(1)

    backup = WORKSPACE / "post-2888497-backup-pre-strip-toc.json"
    backup.write_text(json.dumps(post, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[backup] {backup}")

    raw = post["content"]["raw"]
    before_len = len(raw)
    matches = TOC_PATTERN.findall(raw)
    print(f"[scan] TOC blocks found: {len(matches)}")
    if matches:
        print(f"[scan] first match: {matches[0][:200]!r}")

    new_raw = TOC_PATTERN.sub("\n\n", raw)
    new_raw = re.sub(r"\n{3,}", "\n\n", new_raw)
    after_len = len(new_raw)
    print(f"[strip] {before_len} -> {after_len} chars (delta {after_len-before_len:+d})")

    if matches == [] and before_len == after_len:
        print("[strip] nothing to do, exiting")
        return

    # 2) Save patched locally before push
    (WORKSPACE / "post-2888497-no-toc.html").write_text(new_raw, encoding="utf-8")

    # 3) Push
    st, resp = http("POST", f"{BASE}/{POST_ID}", auth, payload={"content": new_raw})
    print(f"[push] HTTP {st}")
    print(f"  status   : {resp.get('status')}")
    print(f"  modified : {resp.get('modified')}")
    print(f"  slug     : {resp.get('slug')}")

    # 4) Re-fetch + verify byte-perfect + zero TOC
    st, after = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    after_raw = after["content"]["raw"]
    (WORKSPACE / "post-2888497-after-strip.json").write_text(
        json.dumps(after, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    if after_raw == new_raw:
        print("  byte-perfect: YES ✓")
    else:
        print(f"  byte-perfect: NO (expected={len(new_raw)} got={len(after_raw)})")

    remaining = TOC_PATTERN.findall(after_raw)
    print(f"  remaining TOC blocks: {len(remaining)} (must=0)")


if __name__ == "__main__":
    main()

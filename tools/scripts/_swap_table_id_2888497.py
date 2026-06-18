#!/usr/bin/env python3
"""Swap Ninja Tables tableId in post 2888497 (DE).

Replaces all occurrences of OLD_ID (2592801, the FR source table) with NEW_ID
in the post content. Touches 3 places per audit:
  - "tableId":"OLD_ID"  (Kadence/Gutenberg block attrs)
  - id="OLD_ID"         (shortcode [ninja_tables id="..."])
  - Any other ref       (safety net)

Usage:  python _swap_table_id_2888497.py NEW_ID

Per reference_ninja_tables_rest.md: do NOT modify table 2592801 directly
(used by FR article /ninja-tables-datatables-seo-guide/, post 2592793).
Michael creates the DE clone via UI ("Duplicate"), gives the new ID here.
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
OLD_TABLE_ID = "2592801"
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8"))["env"]
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, auth, payload=None):
    headers = {
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-swap/1.0",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python _swap_table_id_2888497.py <NEW_TABLE_ID>", file=sys.stderr)
        sys.exit(2)
    new_id = sys.argv[1]
    if new_id == OLD_TABLE_ID:
        print(f"[refuse] NEW_ID == OLD_ID ({OLD_TABLE_ID}). Aborting.", file=sys.stderr)
        sys.exit(3)

    user, pw = load_creds()
    auth = auth_header(user, pw)

    # 1) GET current
    st, post = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    if st != 200:
        print(f"[error] GET {st}")
        sys.exit(1)

    backup = WORKSPACE / "post-2888497-backup-pre-swap-table.json"
    backup.write_text(json.dumps(post, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[backup] {backup}")

    raw = post["content"]["raw"]
    before_count = (
        raw.count(f'"tableId":"{OLD_TABLE_ID}"')
        + raw.count(f'id="{OLD_TABLE_ID}"')
    )
    print(f"[scan] tableId references found for {OLD_TABLE_ID}: {before_count}")
    if before_count == 0:
        print("[scan] nothing to swap, exiting")
        return

    new_raw = raw.replace(f'"tableId":"{OLD_TABLE_ID}"', f'"tableId":"{new_id}"')
    new_raw = new_raw.replace(f'id="{OLD_TABLE_ID}"', f'id="{new_id}"')

    # Safety: refuse if 2592801 still appears anywhere
    leftover = new_raw.count(OLD_TABLE_ID)
    if leftover > 0:
        print(f"[warn] {leftover} stray reference(s) to {OLD_TABLE_ID} remain after swap")
        # Show context
        for m in re.finditer(re.escape(OLD_TABLE_ID), new_raw):
            ctx = new_raw[max(0, m.start()-60):m.end()+60]
            print(f"   ...{ctx}...")

    # 2) Push
    st, resp = http("POST", f"{BASE}/{POST_ID}", auth, payload={"content": new_raw})
    print(f"[push] HTTP {st}  modified={resp.get('modified')}")

    # 3) Verify
    st, after = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    after_raw = after["content"]["raw"]
    after_count = (
        after_raw.count(f'"tableId":"{new_id}"')
        + after_raw.count(f'id="{new_id}"')
    )
    old_after = after_raw.count(OLD_TABLE_ID)
    print(f"  new id refs : {after_count} (expected={before_count})")
    print(f"  old id refs : {old_after} (expected=0)")
    print(f"  byte-perfect: {'YES ✓' if after_raw == new_raw else 'NO'}")

    (WORKSPACE / "post-2888497-after-swap.json").write_text(
        json.dumps(after, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Batch-fix all posts/pages listed in _scan-broken-toc.json by stripping their
broken wp:rank-math/toc-block (no 'headings' attribute -> Gutenberg editor crash).

Reads findings JSON. For each entry: GET context=edit, sub-match TOC blocks
without 'headings', POST back. Verifies byte-perfect or normalized whitespace.
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
SCAN = ROOT / "tools" / "scripts" / "_scan-broken-toc.json"
BASE = "https://schoolswp.com/wp-json/wp/v2"

# Match a full toc-block (open comment, body, close comment), capturing attrs.
TOC_FULL = re.compile(
    r"<!-- wp:rank-math/toc-block(\s+(\{.*?\}))?\s*-->(.*?)<!-- /wp:rank-math/toc-block -->\s*",
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
        "User-Agent": "Mozilla/5.0 schoolsWP-fix",
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


def strip_broken_toc(raw):
    """Remove TOC blocks where attrs lack 'headings'. Keep healthy TOCs intact."""
    removed = 0

    def replacer(m):
        nonlocal removed
        attrs = m.group(2) or ""
        if '"headings"' in attrs:
            return m.group(0)  # keep healthy block
        removed += 1
        return ""

    new_raw = TOC_FULL.sub(replacer, raw)
    return new_raw, removed


def fix_one(entry, user, pw):
    pid = entry["id"]
    ptype = entry["type"]
    url = f"{BASE}/{ptype}/{pid}"
    status, post = http("GET", f"{url}?context=edit", user, pw)
    if status != 200:
        print(f"  [error] GET {ptype}/{pid}: HTTP {status}")
        return False
    raw = post.get("content", {}).get("raw", "")
    sha_before = hashlib.sha1(raw.encode("utf-8")).hexdigest()

    new_raw, removed = strip_broken_toc(raw)
    if removed == 0:
        print(f"  [skip] {ptype}/{pid}: nothing to strip (already fixed?)")
        return True
    sha_local = hashlib.sha1(new_raw.encode("utf-8")).hexdigest()

    print(f"  [fix ] {ptype}/{pid}: -{len(raw)-len(new_raw)} chars, {removed} block(s)")
    print(f"         sha {sha_before[:10]} -> {sha_local[:10]}")

    status, resp = http("POST", url, user, pw, {"content": new_raw})
    if status != 200:
        print(f"  [error] POST {ptype}/{pid}: HTTP {status} {str(resp)[:300]}")
        return False
    print(f"  [ok  ] modified: {resp.get('modified')}")

    # Verify
    status, post2 = http("GET", f"{url}?context=edit", user, pw)
    if status == 200:
        raw2 = post2.get("content", {}).get("raw", "")
        _, still = strip_broken_toc(raw2)
        if still > 0:
            print(f"  [WARN] still {still} broken blocks on server!")
            return False
        sha_server = hashlib.sha1(raw2.encode("utf-8")).hexdigest()
        match = "byte-perfect" if sha_server == sha_local else "normalized"
        print(f"  [ok  ] server clean ({match})")
    return True


def main():
    user, pw = load_creds()
    findings = json.loads(SCAN.read_text(encoding="utf-8"))
    print(f"[info] {len(findings)} entries to fix")
    print()

    success = 0
    fail = 0
    for entry in findings:
        print(f"--- {entry['type']}/{entry['id']} {entry['slug']} -> {entry['link']}")
        ok = fix_one(entry, user, pw)
        if ok:
            success += 1
        else:
            fail += 1
        print()

    print(f"=== {success} fixed, {fail} failed ===")
    sys.exit(0 if fail == 0 else 1)


if __name__ == "__main__":
    main()

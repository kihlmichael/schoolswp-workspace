#!/usr/bin/env python3
"""
Batch-strip all wp:shortcode blocks containing [rank_math_breadcrumb] across all posts/pages.

Reads findings from _scan-rankmath-breadcrumb.json (must run scan first).
For each entry:
  1. GET context=edit
  2. backup pre-state to manifest (id + sha1_before + content_before excerpt + modified)
  3. strip with regex (only if pattern still present - idempotent)
  4. POST update
  5. verify (sha1 server)

Manifest written to _backup-rankmath-breadcrumb-batch-<ts>.json for rollback.
Polite rate-limit: 0.25s sleep between posts.
"""

import base64
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
SCRIPTS = ROOT / "tools" / "scripts"
SCAN = SCRIPTS / "_scan-rankmath-breadcrumb.json"
BASE = "https://schoolswp.com/wp-json/wp/v2"

BREADCRUMB_BLOCK = re.compile(
    r"<!--\s*wp:shortcode(\s+\{.*?\})?\s*-->\s*\[rank_math_breadcrumb([^\]]*)\]\s*<!--\s*/wp:shortcode\s*-->\s*",
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


def strip_block(raw):
    new_raw, n = BREADCRUMB_BLOCK.subn("", raw)
    return new_raw, n


def main():
    user, pw = load_creds()
    findings = json.loads(SCAN.read_text(encoding="utf-8"))
    total = len(findings)
    print(f"[info] {total} entries to process")

    ts = time.strftime("%Y-%m-%d_%H%M%S")
    manifest_path = SCRIPTS / f"_backup-rankmath-breadcrumb-batch-{ts}.json"
    manifest = []

    success = 0
    skipped = 0
    failed = 0
    t_start = time.time()

    for i, entry in enumerate(findings, 1):
        pid = entry["id"]
        ptype = entry["type"]
        slug = entry["slug"]
        url = f"{BASE}/{ptype}/{pid}"

        # 1. GET
        status, post = http("GET", f"{url}?context=edit", user, pw)
        if status != 200:
            print(f"[{i:3}/{total}] [GET-FAIL] {ptype}/{pid} {slug}: HTTP {status}")
            failed += 1
            continue

        raw = post.get("content", {}).get("raw", "")
        sha_before = hashlib.sha1(raw.encode("utf-8")).hexdigest()

        # Idempotency check
        if not BREADCRUMB_BLOCK.search(raw):
            print(f"[{i:3}/{total}] [skip   ] {ptype}/{pid} {slug}: pattern absent (already fixed?)")
            skipped += 1
            continue

        # 2. Strip
        new_raw, n_removed = strip_block(raw)
        sha_local = hashlib.sha1(new_raw.encode("utf-8")).hexdigest()
        delta = len(raw) - len(new_raw)

        # 3. Backup pre-state
        manifest.append({
            "id": pid,
            "type": ptype,
            "slug": slug,
            "modified_before": post.get("modified"),
            "sha1_before": sha_before,
            "sha1_after_local": sha_local,
            "len_before": len(raw),
            "len_after": len(new_raw),
            "delta": delta,
            "blocks_removed": n_removed,
        })

        # 4. POST
        status, resp = http("POST", url, user, pw, {"content": new_raw})
        if status != 200:
            print(f"[{i:3}/{total}] [POST-FAIL] {ptype}/{pid} {slug}: HTTP {status} {str(resp)[:200]}")
            failed += 1
            continue

        # 5. Verify - quick check: pattern absent on server
        status, post2 = http("GET", f"{url}?context=edit", user, pw)
        if status == 200:
            raw2 = post2.get("content", {}).get("raw", "")
            if BREADCRUMB_BLOCK.search(raw2):
                print(f"[{i:3}/{total}] [WARN  ] {ptype}/{pid} {slug}: pattern still present on server!")
                failed += 1
                continue
            sha_server = hashlib.sha1(raw2.encode("utf-8")).hexdigest()
            tag = "byte-perfect" if sha_server == sha_local else "normalized"
            manifest[-1]["sha1_server"] = sha_server
            manifest[-1]["verify"] = tag
        success += 1

        elapsed = time.time() - t_start
        rate = i / elapsed if elapsed > 0 else 0
        eta = (total - i) / rate if rate > 0 else 0
        if i % 10 == 0 or i == total:
            print(f"[{i:3}/{total}] ok {ptype}/{pid:>7} {slug:50.50} -{delta:>4}ch | {rate:.1f}/s ETA {eta:.0f}s")

        time.sleep(0.25)  # polite rate-limit

    manifest_path.write_text(json.dumps({"timestamp": ts, "entries": manifest}, indent=2, ensure_ascii=False), encoding="utf-8")

    elapsed = time.time() - t_start
    print(f"\n=== BATCH DONE in {elapsed:.0f}s ===")
    print(f"success: {success}")
    print(f"skipped: {skipped}")
    print(f"failed : {failed}")
    print(f"manifest (for rollback): {manifest_path}")


if __name__ == "__main__":
    main()

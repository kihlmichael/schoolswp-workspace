#!/usr/bin/env python3
"""
Scan schoolswp.com posts + pages for the wp:shortcode block containing [rank_math_breadcrumb].
Read-only. Reports findings to _scan-rankmath-breadcrumb.json with all variants observed.
"""

import base64
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUTFILE = ROOT / "tools" / "scripts" / "_scan-rankmath-breadcrumb.json"
BASE = "https://schoolswp.com/wp-json/wp/v2"
TYPES = ["posts", "pages"]

# Capture the full block + any attrs on the shortcode comment + any attrs inside the shortcode itself
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


def http(method, url, user, pw):
    headers = {
        "Authorization": auth_header(user, pw),
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolsWP-scan",
    }
    req = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read().decode("utf-8")
            total = resp.headers.get("X-WP-Total")
            total_pages = resp.headers.get("X-WP-TotalPages")
            try:
                parsed = json.loads(body)
            except json.JSONDecodeError:
                # WP Social Reviews CSS injection workaround
                for marker in ("[", "{"):
                    pos = body.find(marker)
                    while pos >= 0:
                        try:
                            parsed = json.loads(body[pos:])
                            return resp.status, parsed, int(total or 0), int(total_pages or 0)
                        except json.JSONDecodeError:
                            pos = body.find(marker, pos + 1)
                return resp.status, None, 0, 0
            return resp.status, parsed, int(total or 0), int(total_pages or 0)
    except urllib.error.HTTPError as e:
        return e.code, None, 0, 0


def iter_post_type(ptype, user, pw):
    per_page = 50
    page = 1
    while True:
        url = f"{BASE}/{ptype}?per_page={per_page}&page={page}&context=edit&status=publish,future,draft,private&_fields=id,slug,link,status,content"
        status, body, total, total_pages = http("GET", url, user, pw)
        if status != 200 or not isinstance(body, list) or not body:
            if status != 200 and page == 1:
                print(f"[warn] {ptype}: HTTP {status}")
            return
        if page == 1:
            print(f"[info] {ptype}: {total} items in {total_pages} pages")
        for item in body:
            raw = item.get("content", {}).get("raw", "")
            yield item["id"], item["slug"], item["link"], item.get("status"), raw
        if page >= total_pages:
            return
        page += 1
        time.sleep(0.1)


def main():
    user, pw = load_creds()
    findings = []
    scanned = 0
    variants = {}

    for ptype in TYPES:
        for pid, slug, link, status, raw in iter_post_type(ptype, user, pw):
            scanned += 1
            matches = list(BREADCRUMB_BLOCK.finditer(raw))
            if not matches:
                continue
            for m in matches:
                wp_attrs = (m.group(1) or "").strip()
                inner_attrs = (m.group(2) or "").strip()
                key = f"wp_attrs={wp_attrs!r}|inner_attrs={inner_attrs!r}"
                variants[key] = variants.get(key, 0) + 1
            findings.append({
                "id": pid,
                "type": ptype,
                "slug": slug,
                "link": link,
                "status": status,
                "occurrences": len(matches),
                "offsets": [m.start() for m in matches],
                "first_match_full": matches[0].group(0),
            })

    OUTFILE.write_text(json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== SCAN SUMMARY ===")
    print(f"items scanned : {scanned}")
    print(f"items with breadcrumb block: {len(findings)}")
    total_blocks = sum(f["occurrences"] for f in findings)
    print(f"total breadcrumb blocks   : {total_blocks}")
    print(f"\n=== Variants observed ===")
    for k, count in variants.items():
        print(f"  {count:4} x {k}")
    print(f"\nreport saved to: {OUTFILE}")

    # Print 2 sample full matches for sanity check
    if findings:
        print(f"\n=== Sample 1: post {findings[0]['id']} ({findings[0]['slug']}) ===")
        print(repr(findings[0]["first_match_full"]))
        if len(findings) > 1:
            print(f"\n=== Sample 2: post {findings[-1]['id']} ({findings[-1]['slug']}) ===")
            print(repr(findings[-1]["first_match_full"]))


if __name__ == "__main__":
    main()

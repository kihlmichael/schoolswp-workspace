#!/usr/bin/env python3
"""
Scan schoolswp.com for broken wp:rank-math/toc-block (no 'headings' attribute).
Such blocks crash Gutenberg editor save() on .length (memory reference_rank_math_toc_block_bug.md).

Iterates all posts + pages across all Polylang languages, context=edit.
Read-only. Reports JSON list to scripts/_scan-broken-toc.json + prints summary.
Never patches anything.
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
OUTFILE = ROOT / "tools" / "scripts" / "_scan-broken-toc.json"
BASE = "https://schoolswp.com/wp-json/wp/v2"

# Post types to scan (single pass each, no lang filter - Polylang REST returns all langs)
TYPES = ["posts", "pages"]

TOC_OPEN = re.compile(r"<!-- wp:rank-math/toc-block(\s+(\{.*?\}))?\s*-->", re.DOTALL)


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
        "User-Agent": "Mozilla/5.0 schoolsWP-scan",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read().decode("utf-8")
            total = resp.headers.get("X-WP-Total")
            total_pages = resp.headers.get("X-WP-TotalPages")
            try:
                parsed = json.loads(body)
            except json.JSONDecodeError:
                # Some plugin (WP Social Reviews) prepends CSS to REST responses.
                # Find JSON start - look for first '[' or '{' that opens a valid doc.
                for marker in ("[", "{"):
                    pos = body.find(marker)
                    while pos >= 0:
                        try:
                            parsed = json.loads(body[pos:])
                            return resp.status, parsed, int(total or 0), int(total_pages or 0)
                        except json.JSONDecodeError:
                            pos = body.find(marker, pos + 1)
                return resp.status, {"_raw_html": body[:300]}, 0, 0
            return resp.status, parsed, int(total or 0), int(total_pages or 0)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace"), 0, 0


def scan_block(raw):
    """Return list of dicts {open_offset, attrs_json, has_headings} for each TOC block."""
    out = []
    for m in TOC_OPEN.finditer(raw):
        attrs = m.group(2) or ""
        has_headings = '"headings"' in attrs
        out.append({
            "offset": m.start(),
            "attrs": attrs,
            "has_headings": has_headings,
        })
    return out


def iter_post_type(ptype, user, pw):
    """Yield (id, slug, link, status, raw) for all items of post type (all langs)."""
    per_page = 50
    page = 1
    while True:
        url = f"{BASE}/{ptype}?per_page={per_page}&page={page}&context=edit&status=publish,future,draft,private&_fields=id,slug,link,status,content"
        status, body, total, total_pages = http("GET", url, user, pw)
        if status != 200:
            print(f"[warn] {ptype} page={page}: HTTP {status} body={str(body)[:200]}")
            if page == 1:
                return
            # End of pagination (page beyond total) returns 400 - exit cleanly
            return
        if isinstance(body, dict):
            print(f"[warn] {ptype} page={page}: dict response {str(body)[:200]}")
            return
        if not isinstance(body, list) or not body:
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
    blocks_total = 0
    broken_total = 0

    for ptype in TYPES:
        for pid, slug, link, status, raw in iter_post_type(ptype, user, pw):
            scanned += 1
            if "rank-math/toc-block" not in raw:
                continue
            blocks = scan_block(raw)
            if not blocks:
                continue
            blocks_total += len(blocks)
            broken = [b for b in blocks if not b["has_headings"]]
            if broken:
                broken_total += len(broken)
                findings.append({
                    "id": pid,
                    "type": ptype,
                    "slug": slug,
                    "link": link,
                    "status": status,
                    "toc_blocks_total": len(blocks),
                    "toc_blocks_broken": len(broken),
                    "broken_offsets": [b["offset"] for b in broken],
                })
                print(f"  [BROKEN] {pid:>7} {ptype:5} {slug:55.55} blocks={len(blocks)} broken={len(broken)} -> {link}")

    OUTFILE.write_text(json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8")
    print()
    print(f"=== SCAN SUMMARY ===")
    print(f"items scanned   : {scanned}")
    print(f"toc blocks total: {blocks_total}")
    print(f"toc blocks broken: {broken_total}")
    print(f"posts/pages with broken TOC: {len(findings)}")
    print(f"report saved to : {OUTFILE}")


if __name__ == "__main__":
    main()

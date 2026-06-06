#!/usr/bin/env python3
"""Diagnose unmatched FR pairs against live content of post 343156.

Helps figure out why 26/59 pairs didn't match in the last push:
- Already translated (EN string present, FR absent)?
- Different apostrophe / typographic quote variant?
- WP-normalized entities (&amp;, &nbsp;)?
- Truncated / paraphrased text inside Gutenberg block?
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
PAIRS = ROOT / "content" / "audits" / "flyingpress-wp-rocket-comparison-en" / "2026-05-12" / "payload-pairs.json"
POST_ID = 343156


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def fetch_raw(user, pw):
    url = f"https://schoolswp.com/wp-json/wp/v2/posts/{POST_ID}?context=edit"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode(),
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))["content"]["raw"]


def variants(s):
    """Yield 3 apostrophe variants + 2 quote variants of a string for fuzzy search."""
    seen = set()
    cands = [
        s,
        s.replace("’", "&rsquo;"),
        s.replace("’", "'"),
        s.replace("« ", "&laquo; ").replace(" »", " &raquo;"),
        s.replace(" ", " "),
        s.replace(" ", "&nbsp;"),
    ]
    for c in cands:
        if c not in seen:
            seen.add(c)
            yield c


def find_partial(content, fr_text):
    """Return up to 60-char prefix found, else None."""
    for cut in (40, 30, 25, 20, 15, 12, 10):
        head = fr_text[:cut].replace("’", "")
        if head and head in content.replace("’", ""):
            idx = content.replace("’", "").find(head)
            sample = content[max(0, idx - 10) : idx + cut + 30]
            return cut, sample
    return None, None


def main():
    user, pw = load_creds()
    raw = fetch_raw(user, pw)
    pairs = json.loads(PAIRS.read_text(encoding="utf-8"))
    print(f"[info] post {POST_ID} raw len={len(raw)}")
    print(f"[info] {len(pairs)} pairs to diagnose\n")

    matched = 0
    en_already = 0
    paraphrased = 0
    unknown = 0
    report = []
    for i, (fr, en) in enumerate(pairs, 1):
        # 1. Does any FR variant exist as-is?
        fr_hit = next((v for v in variants(fr) if v in raw), None)
        if fr_hit is not None:
            matched += 1
            continue
        # 2. Is the EN replacement already there?
        en_hit = next((v for v in variants(en) if v in raw), None)
        if en_hit is not None:
            en_already += 1
            report.append((i, "EN_ALREADY", fr[:60]))
            continue
        # 3. Partial FR match?
        cut, sample = find_partial(raw, fr)
        if cut:
            paraphrased += 1
            report.append((i, f"PARTIAL_{cut}", fr[:60], (sample or "")[:120]))
            continue
        unknown += 1
        report.append((i, "UNKNOWN", fr[:60]))

    print(f"[stats] matched_now: {matched}")
    print(f"[stats] en_already_there: {en_already}")
    print(f"[stats] paraphrased_in_raw: {paraphrased}")
    print(f"[stats] unknown_disappeared: {unknown}")
    print()
    for row in report:
        if len(row) == 3:
            i, tag, fr60 = row
            print(f"  #{i:02d} [{tag:14}] FR='{fr60}'")
        else:
            i, tag, fr60, sample = row
            print(f"  #{i:02d} [{tag:14}] FR='{fr60}'")
            print(f"          live: '{sample}'")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extract targeted sections of post 2871653 for enrichment decisions."""

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2871653-current.json"
data = json.loads(SRC.read_text(encoding="utf-8"))
c = data["content"]["raw"]


def section(label):
    print()
    print("=" * 80)
    print(label)
    print("=" * 80)


# 1. Intro: from start to first H2
m = re.search(r"<!--\s*wp:heading\s+", c)
if m:
    section("INTRO (start → first H2)")
    print(c[: m.start()])

# 2. Ninja Tables block
m = re.search(r"<!--\s*wp:ninja-tables/guten-block[^>]*-->.*?<!--\s*/wp:ninja-tables/guten-block\s*-->", c, re.DOTALL)
if m:
    section("NINJA TABLES BLOCK")
    print(m.group(0))
else:
    print("[no ninja-tables block found via regex]")

# 3. FAQ H2 onwards (just the questions, not full answers)
m = re.search(r"<h2[^>]*>\s*Questions fréquentes[^<]*</h2>", c, re.IGNORECASE)
if m:
    faq_start = m.start()
    # find next H2 or end
    nm = re.search(r"<h2[^>]*>", c[m.end():])
    faq_end = (m.end() + nm.start()) if nm else len(c)
    faq = c[faq_start:faq_end]
    section(f"FAQ - questions only ({len(faq)} chars total)")
    # print all H3 inside FAQ + their first ~120 chars of answer
    for sm in re.finditer(r"<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|$)", faq, re.DOTALL | re.IGNORECASE):
        q = re.sub(r"<[^>]+>", "", sm.group(1)).strip()
        a = re.sub(r"<[^>]+>", " ", sm.group(2)).strip()
        a = re.sub(r"\s+", " ", a)
        print(f"  Q: {q}")
        print(f"     A (start): {a[:160]}...")
        print()

# 4. Look at conclusion CTA (last H2)
m_all = list(re.finditer(r"<h2[^>]*>(.*?)</h2>", c, re.DOTALL | re.IGNORECASE))
if m_all:
    last = m_all[-1]
    section("LAST H2 (CTA conclusion)")
    print(c[last.start():])

# 5. Disclosure affiliate location
section("AFFILIATE DISCLOSURE matches (context)")
for m in re.finditer(r"affili[ée]|affiliate|disclos", c, re.IGNORECASE):
    start = max(0, m.start() - 200)
    end = min(len(c), m.end() + 200)
    snippet = c[start:end]
    snippet = re.sub(r"<[^>]+>", "", snippet)
    snippet = re.sub(r"\s+", " ", snippet)
    print(f"  @{m.start()}: ...{snippet[:380]}...")
    print()

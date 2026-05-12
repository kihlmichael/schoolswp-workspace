#!/usr/bin/env python3
"""
Analyze the structure of post 2871653 draft without dumping content to transcript.
Outputs:
- H1/H2/H3 outline with char counts per section
- Block types used (paragraph, list, table, image, code, quote, etc.)
- Internal links (schoolswp.com) and external links
- Affiliate link presence
- Featured snippet block presence ("Reponse rapide" etc.)
- FAQ presence
- Meta description proxy (excerpt)
- Tags/categories
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2871653-current.json"

data = json.loads(SRC.read_text(encoding="utf-8"))
content_raw = data.get("content", {}).get("raw", "")
title = data.get("title", {}).get("raw", "")
excerpt = data.get("excerpt", {}).get("raw", "")
slug = data.get("slug", "")
tags = data.get("tags", [])
cats = data.get("categories", [])
meta = data.get("meta", {}) or {}

print("=" * 80)
print("POST 2871653 - STRUCTURAL ANALYSIS")
print("=" * 80)
print(f"Title     : {title}")
print(f"Slug      : {slug}")
print(f"Excerpt   : {len(excerpt)} chars - {excerpt[:200]}")
print(f"Tags      : {tags}")
print(f"Categories: {cats}")
print(f"Content   : {len(content_raw)} chars total")
print()

# Outline
print("-" * 80)
print("OUTLINE (H1/H2/H3 with char distance to next)")
print("-" * 80)
heads = []
for m in re.finditer(r"<h([1-3])(?:\s[^>]*)?>(.*?)</h\1>", content_raw, re.DOTALL | re.IGNORECASE):
    level = int(m.group(1))
    text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
    heads.append((m.start(), level, text))

for i, (pos, lvl, txt) in enumerate(heads):
    nxt = heads[i + 1][0] if i + 1 < len(heads) else len(content_raw)
    span = nxt - pos
    indent = "  " * (lvl - 1)
    print(f"  L{lvl} {indent}[{span:>5}c] {txt[:90]}")

# Block types (Gutenberg comments)
print()
print("-" * 80)
print("BLOCK TYPES")
print("-" * 80)
blocks = Counter(re.findall(r"<!--\s*wp:([a-z0-9/_-]+)", content_raw, re.IGNORECASE))
for b, c in blocks.most_common():
    print(f"  {c:>4} x {b}")

# Links
print()
print("-" * 80)
print("LINKS")
print("-" * 80)
all_links = re.findall(r'href="(https?://[^"]+)"', content_raw)
internal = [u for u in all_links if "schoolswp.com" in u]
external = [u for u in all_links if "schoolswp.com" not in u]
print(f"  Internal (schoolswp.com): {len(internal)}")
internal_paths = sorted(set(re.sub(r"https?://schoolswp\.com", "", u).split("?")[0] for u in internal))
for p in internal_paths[:40]:
    print(f"    {p}")
print(f"  External: {len(external)} (unique domains: {len(set(re.findall(r'https?://([^/]+)', '\\n'.join(external))))})")
ext_domains = Counter(re.findall(r"https?://([^/]+)", "\n".join(external)))
for d, c in ext_domains.most_common(15):
    print(f"    {c:>3} x {d}")

# Featured snippet blocks / canon schoolswp
print()
print("-" * 80)
print("CANON BLOCKS (heuristic search)")
print("-" * 80)
for label, patterns in [
    ("Reponse rapide / TL;DR / En bref",  [r"Réponse rapide", r"TL;DR", r"En bref", r"En résumé", r"Points clés", r"En 30 secondes"]),
    ("FAQ",                                [r"<h[23][^>]*>\s*FAQ", r"Foire aux questions", r"Questions fréquentes"]),
    ("Free vs Pro",                        [r"free\s+vs\s+pro", r"gratuit\s+vs\s+pro", r"version\s+pro", r"version\s+free"]),
    ("Ordre / parcours",                   [r"dans quel ordre", r"par où commencer", r"l'ordre dans lequel", r"par quoi commencer"]),
    ("Erreurs / pieges",                   [r"erreurs?\s+à\s+éviter", r"pièges?", r"erreurs?\s+courantes"]),
    ("Disclosure affilie",                 [r"affili[éeé]", r"affiliate", r"disclos"]),
    ("Captures / screenshot",              [r"<figure", r"<img"]),
    ("Tableau",                            [r"<!--\s*wp:table", r"<table"]),
    ("CTA Kadence",                        [r"kadence/advancedbtn", r"kadence/singlebtn"]),
    ("Stack co-occurrence",                [r"FluentSMTP", r"FluentForms", r"FluentCart", r"TutorLMS", r"OttoKit"]),
]:
    found = []
    for p in patterns:
        m = re.search(p, content_raw, re.IGNORECASE)
        if m:
            found.append(p)
    if found:
        print(f"  OK  {label}")
        for f in found:
            print(f"        + matched: {f}")
    else:
        print(f"  MISS {label}")

# Rank Math meta if present in raw
print()
print("-" * 80)
print("META (rank_math etc.)")
print("-" * 80)
for k in sorted(meta.keys()):
    v = meta.get(k)
    sv = str(v)
    print(f"  {k}: {sv[:120]}")

# Approximate word count (HTML-stripped)
plain = re.sub(r"<[^>]+>", " ", content_raw)
plain = re.sub(r"\s+", " ", plain).strip()
words = len(plain.split())
print()
print(f"Approx word count: {words}")

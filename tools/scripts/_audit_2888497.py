#!/usr/bin/env python3
"""Structural audit of post 2888497 (DE Ninja Tables DataTables)."""

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2888497-current.json"

d = json.loads(SRC.read_text(encoding="utf-8"))
content = d.get("content", {}).get("raw", "")
title = d.get("title", {}).get("raw", "")
excerpt = d.get("excerpt", {}).get("raw", "")
slug = d.get("slug", "")

# Strip Gutenberg comments + HTML tags for plain text analysis
text = re.sub(r"<!--[\s\S]*?-->", " ", content)
plain = re.sub(r"<[^>]+>", " ", text)
plain = re.sub(r"\s+", " ", plain).strip()

words = re.findall(r"\b[\wäöüÄÖÜß]+\b", plain, flags=re.UNICODE)

# Headings
h_pattern = re.compile(r"<h([1-6])[^>]*>([\s\S]*?)</h\1>", re.IGNORECASE)
headings = [(int(lvl), re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", txt)).strip())
            for lvl, txt in h_pattern.findall(text)]

# Images + alts
img_pattern = re.compile(r'<img[^>]*?>', re.IGNORECASE)
imgs = img_pattern.findall(text)
imgs_no_alt = [i for i in imgs if not re.search(r'alt="[^"]+"', i)]

# Links
link_pattern = re.compile(r'<a[^>]*?href="([^"]+)"[^>]*>([\s\S]*?)</a>', re.IGNORECASE)
links = link_pattern.findall(text)
internal = [(h, t) for h, t in links if "schoolswp.com" in h or h.startswith("/") or h.startswith("#")]
external = [(h, t) for h, t in links if h not in [x[0] for x in internal] and h.startswith("http")]
# Affiliate / cloak pattern
affiliate_internal = [h for h, _ in internal if re.search(r"schoolswp\.com/(ninja-tables|fluent-|kadence|wp-rocket|flying|tutor|fluentcrm|surecart|sureforms|surepress)", h)]

# CTA detection (Kadence button)
cta_blocks = len(re.findall(r"wp:kadence/(advancedbtn|singlebtn|btn)", content))
# Affiliate CTA wording markers
cta_words_de = ["Jetzt", "Kostenlos", "Ninja Tables", "Pro testen", "Kaufen", "Holen", "Plan wählen"]
cta_hits = sum(1 for w in cta_words_de if w.lower() in plain.lower())

# Schema / JSON-LD
schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', content)

# Em-dashes (forbidden per BRAND_RULES)
em_dash = plain.count("—")
en_dash = plain.count("–")

# Separators (forbidden)
separator_blocks = len(re.findall(r"wp:separator", content))

# Year mentions in slug/title (forbidden)
year_in_title = re.findall(r"20\d{2}", title)
year_in_slug = re.findall(r"20\d{2}", slug)

# Tu form check (German "du" instead of "Sie") — schoolsWP brand uses Sie or tutoiement? Brand FR = tutoiement
# In DE, schoolsWP voice typically uses Sie (formal) or du. Let's count both.
sie_count = len(re.findall(r"\bSie\b", plain))
ihr_count = len(re.findall(r"\bIhr\w*\b", plain))
du_count = len(re.findall(r"\b[Dd]u\b", plain))
dein_count = len(re.findall(r"\b[Dd]ein\w*\b", plain))

# We/our (singular voice rule)
wir_count = len(re.findall(r"\bwir\b", plain, re.IGNORECASE))
unser_count = len(re.findall(r"\bunser\w*\b", plain, re.IGNORECASE))

# Placeholder leak check
placeholder_leak = re.findall(r"\[(CTA_STANDARD|CTA|TEMPLATE|TODO|FIXME|TBD)[^\]]*\]", content)

# Tables
tables = len(re.findall(r"wp:ninja-tables|wp:table", content))

# TOC presence
toc = "wp:rank-math/toc-block" in content

# Featured image
feat = d.get("featured_media", 0)

# Keyword density (target)
target_kw_candidates = ["Ninja Tables", "DataTables", "Ninja Tables Pro", "AJAX"]
kw_count = {k: len(re.findall(re.escape(k), plain, re.IGNORECASE)) for k in target_kw_candidates}

# Title length / SEO
title_len = len(title)
excerpt_len = len(excerpt)

# Print report
print("=" * 70)
print(f"AUDIT post 2888497  |  status={d.get('status')}  modified={d.get('modified')}")
print(f"URL: {d.get('link')}")
print("=" * 70)
print()
print(f"TITLE       : {title}")
print(f"SLUG        : {slug}")
print(f"EXCERPT     : {excerpt}")
print()
print(f"length      : title={title_len}c | excerpt={excerpt_len}c | content={len(content)}c")
print(f"words (plain): {len(words)}")
print(f"featured img: {feat}")
print(f"toc present : {toc}")
print(f"separators  : {separator_blocks} (must=0)")
print(f"em-dashes   : {em_dash} (must=0)  | en-dashes: {en_dash}")
print(f"placeholders: {placeholder_leak}")
print(f"year/title  : {year_in_title} | year/slug: {year_in_slug}")
print()
print(f"HEADINGS    : total={len(headings)}")
lvl_counts = Counter(lvl for lvl, _ in headings)
for lvl in sorted(lvl_counts):
    print(f"   H{lvl}: {lvl_counts[lvl]}")
print()
print(f"IMAGES      : total={len(imgs)} | without alt={len(imgs_no_alt)}")
print(f"LINKS       : internal={len(internal)} | external={len(external)} | affiliate(cloak)={len(affiliate_internal)}")
print(f"TABLES      : {tables}")
print(f"CTA blocks  : {cta_blocks} | CTA word hits: {cta_hits}")
print(f"SCHEMAS @type: {Counter(schemas)}")
print()
print(f"VOICE DE    : Sie={sie_count} Ihr*={ihr_count} | du={du_count} dein*={dein_count}")
print(f"             wir={wir_count} unser*={unser_count}  (singular rule: should be 0/low)")
print()
print("KEYWORD COUNTS:")
for k, v in kw_count.items():
    print(f"   {k:25s}: {v}")
print()

print("=== H1-H3 STRUCTURE ===")
for lvl, txt in headings:
    if lvl <= 3:
        print(f"  H{lvl}: {txt[:120]}")

print()
print("=== AFFILIATE / EXTERNAL LINKS (first 20) ===")
for h, t in (internal[:10] + external[:10]):
    label = re.sub(r"<[^>]+>", "", t).strip()[:60]
    print(f"  -> {h[:110]}  | {label}")

print()
print("=== CALLOUT BLOCKS (first 600c) ===")
callouts = re.findall(r'<div class="wp-block-kadence-column[^>]*>([\s\S]*?)</div>\s*<!--', content)
for i, c in enumerate(callouts[:5], 1):
    plain_c = re.sub(r"<[^>]+>", " ", c)
    plain_c = re.sub(r"\s+", " ", plain_c).strip()
    print(f"  [{i}] {plain_c[:200]}...")

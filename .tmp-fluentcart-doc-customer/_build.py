"""Parse Firecrawl crawl JSON, group pages by section, write consolidated .md files."""
import json
import re
from collections import defaultdict
from pathlib import Path

SRC = r'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\1466eebe-189f-4b3d-9bf9-639459711e26\tool-results\mcp-firecrawl-firecrawl_crawl-1779175844496.txt'
OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer')

SECTIONS = [
    ("01-getting-started", "Getting Started", "getting-started"),
    ("02-product-types-creation", "Product Types & Creation", "product-types-creation"),
    ("03-store-management", "Store Management", "store-management"),
    ("04-payments-checkout", "Payments & Checkout", "payments-checkout"),
    ("05-shipping", "Shipping", "shipping"),
    ("06-tax-duties", "Tax & Duties", "tax-&-duties"),
    ("07-customer-dashboard", "Customer Dashboard", "customer-dashboard"),
    ("08-marketing-sales-tools", "Marketing & Sales Tools", "marketing-sales-tools"),
    ("09-settings-configuration", "Settings & Configuration", "settings-configuration"),
    ("10-customization-themes", "Customization & Themes", "customization-and-themes"),
    ("11-integrations", "Integrations", "integrations"),
    ("12-migration-edd", "Migration", "migration"),
    ("13-reporting-analytics", "Reporting & Analytics", "reporting-analytics"),
    ("14-storage", "Storage", "storage"),
    ("15-troubleshooting-support", "Troubleshooting & Support", "troubleshooting-support"),
]
SECTION_SLUGS = {s[2]: (s[0], s[1]) for s in SECTIONS}

print("Loading JSON...")
with open(SRC, encoding='utf-8') as f:
    raw = json.load(f)
data = raw['data']
print(f"Total entries: {len(data)}")

# Filter and normalize
pages = []
skipped = 0
for entry in data:
    md = entry.get('markdown', '') or ''
    meta = entry.get('metadata', {}) or {}
    url = meta.get('url') or meta.get('sourceURL') or meta.get('canonicalUrl') or ''
    if not url.startswith('https://docs.fluentcart.com'):
        skipped += 1
        continue
    if not md.strip():
        skipped += 1
        continue
    title = meta.get('title') or ''
    title = title.replace(' | FluentCart Docs', '').replace(' - FluentCart Docs', '').strip()
    if not title:
        m = re.search(r'^#\s+(.+)$', md, re.MULTILINE)
        title = m.group(1).strip() if m else url.rstrip('/').split('/')[-1].replace('-', ' ').title()
    pages.append({'url': url, 'title': title, 'markdown': md})

print(f"Pages kept: {len(pages)}, skipped: {skipped}")

# Group by section
groups = defaultdict(list)
misc = []
for p in pages:
    url = p['url']
    # path after https://docs.fluentcart.com/
    path = url.replace('https://docs.fluentcart.com', '').strip('/')
    parts = path.split('/') if path else []
    # Expect "guide/<section>/..."
    section_slug = None
    if len(parts) >= 2 and parts[0] == 'guide':
        section_slug = parts[1]
    if section_slug in SECTION_SLUGS:
        groups[section_slug].append(p)
    else:
        misc.append(p)

# Clean markdown: strip nav/footer if patterns appear. Keep main content.
def clean_md(md: str) -> str:
    # Most Firecrawl outputs of docs sites already extract main content; do light cleanup.
    # Remove very long repeated nav blocks if present (heuristic): nothing aggressive.
    # Trim trailing whitespace / multiple blank lines
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    return md.strip()

def section_sort_key(page):
    url = page['url'].rstrip('/')
    path = url.replace('https://docs.fluentcart.com', '').strip('/')
    parts = path.split('/')
    # index page (e.g. /guide/getting-started/) sorts first (depth 2)
    depth = len(parts)
    return (depth, url.lower())

# Write per-section files
written_files = []
section_stats = []
for slug, (file_stub, display_name) in [(s[2], (s[0], s[1])) for s in SECTIONS]:
    pgs = sorted(groups.get(slug, []), key=section_sort_key)
    section_stats.append((slug, display_name, len(pgs)))
    if not pgs:
        continue
    out_path = OUT_DIR / f"{file_stub}.md"
    parts_out = [f"# Section {display_name}\n", "Source : docs.fluentcart.com", "Date scrape : 2026-05-19\n", "---\n"]
    for p in pgs:
        parts_out.append(f"## {p['title']}")
        parts_out.append(f"URL : {p['url']}\n")
        parts_out.append(clean_md(p['markdown']))
        parts_out.append("\n---\n")
    out_path.write_text("\n".join(parts_out), encoding='utf-8')
    written_files.append(out_path)

# Misc / changelog
misc_sorted = sorted(misc, key=section_sort_key)
if misc_sorted:
    out_path = OUT_DIR / "16-changelog-misc.md"
    parts_out = [f"# Section Changelog & Misc\n", "Source : docs.fluentcart.com", "Date scrape : 2026-05-19\n", "---\n"]
    for p in misc_sorted:
        parts_out.append(f"## {p['title']}")
        parts_out.append(f"URL : {p['url']}\n")
        parts_out.append(clean_md(p['markdown']))
        parts_out.append("\n---\n")
    out_path.write_text("\n".join(parts_out), encoding='utf-8')
    written_files.append(out_path)

# Build INDEX (00)
index_parts = ["# Documentation Customer FluentCart - Index\n",
               "Source : https://docs.fluentcart.com",
               "Date scrape : 2026-05-19",
               f"Pages totales : {len(pages)}\n",
               "---\n"]
for slug, (file_stub, display_name) in [(s[2], (s[0], s[1])) for s in SECTIONS]:
    pgs = sorted(groups.get(slug, []), key=section_sort_key)
    if not pgs:
        continue
    index_parts.append(f"## {display_name}")
    index_parts.append(f"Fichier : `{file_stub}.md`")
    index_parts.append(f"Pages : {len(pgs)}\n")
    for p in pgs:
        index_parts.append(f"- [{p['title']}]({p['url']})")
    index_parts.append("")

if misc_sorted:
    index_parts.append("## Changelog & Misc")
    index_parts.append("Fichier : `16-changelog-misc.md`")
    index_parts.append(f"Pages : {len(misc_sorted)}\n")
    for p in misc_sorted:
        index_parts.append(f"- [{p['title']}]({p['url']})")
    index_parts.append("")

(OUT_DIR / "00-INDEX-doc-customer.md").write_text("\n".join(index_parts), encoding='utf-8')
written_files.insert(0, OUT_DIR / "00-INDEX-doc-customer.md")

# Report
print("\n=== STATS ===")
for slug, name, count in section_stats:
    print(f"  {slug:30s} -> {count} pages")
print(f"  MISC                          -> {len(misc_sorted)} pages")

print("\n=== FILES WRITTEN ===")
for f in written_files:
    sz = f.stat().st_size
    print(f"  {f.name:50s} {sz:>10,} bytes")

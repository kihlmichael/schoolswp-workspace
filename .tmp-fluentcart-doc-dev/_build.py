"""Parse Firecrawl crawl JSON and produce consolidated markdown files for FluentCart dev docs."""
import json
import os
from pathlib import Path
from urllib.parse import urlparse

SRC = r'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\1466eebe-189f-4b3d-9bf9-639459711e26\tool-results\mcp-firecrawl-firecrawl_crawl-1779175979214.txt'
OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-dev')
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open(SRC, encoding='utf-8') as f:
    raw = json.load(f)
data = raw['data']

# Normalize records
pages = []
for p in data:
    md = p.get('metadata') or {}
    url = md.get('url') or md.get('sourceURL') or p.get('url') or ''
    if not url.startswith('https://dev.fluentcart.com/'):
        continue
    title = md.get('title') or md.get('og:title') or md.get('ogTitle') or ''
    if not title:
        # Try to extract first H1 from markdown
        for line in (p.get('markdown') or '').splitlines():
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
    title = (title or url).strip()
    markdown = (p.get('markdown') or '').strip()
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    parts = path.split('/') if path else []
    pages.append({
        'url': url,
        'title': title,
        'markdown': markdown,
        'path': path,
        'parts': parts,
    })

# Build a fast lookup by path
by_path = {p['path']: p for p in pages}

def get(path):
    return by_path.get(path)

def find_prefix(prefix):
    """Return list of pages whose path starts with prefix (exclusive of trailing slash)."""
    prefix = prefix.strip('/')
    out = []
    for p in pages:
        if p['path'] == prefix:
            continue  # index handled separately
        if p['path'].startswith(prefix + '/') or (prefix == '' and p['path']):
            out.append(p)
    return out

def render_page(p):
    return (
        f"## {p['title']}\n\n"
        f"**URL** : {p['url']}\n\n"
        f"{p['markdown']}\n"
    )

def write_section(filename, header, intro, ordered_pages):
    lines = [f"# {header}\n"]
    if intro:
        lines.append(intro.strip() + "\n")
    lines.append("---\n")
    for p in ordered_pages:
        lines.append(render_page(p))
        lines.append("\n---\n")
    content = "\n".join(lines)
    (OUT_DIR / filename).write_text(content, encoding='utf-8')
    return filename, len(content), len(ordered_pages)

results = []
used_paths = set()

def use(p):
    if p is None:
        return None
    used_paths.add(p['path'])
    return p

# ----- 01 Getting Started -----
gs_pages = []
p = use(get('getting-started'))
if p: gs_pages.append(p)
# /guides/* — sub-pages, sorted alpha
guides = sorted(find_prefix('guides'), key=lambda x: x['path'])
for g in guides:
    use(g)
    gs_pages.append(g)
results.append(write_section(
    '01-getting-started-dev.md',
    'FluentCart Developer Docs — Getting Started & Guides',
    'Setup, premiers pas et guides pratiques (frontend, abonnements).',
    gs_pages,
))

# ----- 02 API REST overview -----
api_pages = []
# index /api/
p = use(get('api'))
if p: api_pages.append(p)
api_sub = sorted([x for x in find_prefix('api')], key=lambda x: x['path'])
for x in api_sub:
    use(x)
    api_pages.append(x)
# /restapi overview if present
p = use(get('restapi'))
if p: api_pages.append(p)
results.append(write_section(
    '02-api-rest-overview.md',
    'FluentCart Developer Docs — REST API Overview',
    "Overview de l'API REST FluentCart : authentification, orders, products, customers, subscriptions, licensing, order-bump, roles & permissions.",
    api_pages,
))

# ----- 03 Hooks Actions -----
ha_pages = []
p = use(get('hooks/actions'))
if p: ha_pages.append(p)
ha_sub = sorted(find_prefix('hooks/actions'), key=lambda x: x['path'])
for x in ha_sub:
    use(x)
    ha_pages.append(x)
results.append(write_section(
    '03-hooks-actions.md',
    'FluentCart Developer Docs — Hooks (Actions)',
    "Toutes les actions WordPress exposées par FluentCart, groupées par domaine (orders, subscriptions, cart & checkout, customers & users, products & coupons, licenses, admin & templates, payments & integrations).",
    ha_pages,
))

# ----- 04 Hooks Filters -----
hf_pages = []
p = use(get('hooks/filters'))
if p: hf_pages.append(p)
hf_sub = sorted(find_prefix('hooks/filters'), key=lambda x: x['path'])
for x in hf_sub:
    use(x)
    hf_pages.append(x)
results.append(write_section(
    '04-hooks-filters.md',
    'FluentCart Developer Docs — Hooks (Filters)',
    "Tous les filtres WordPress exposés par FluentCart, groupés par domaine (cart & checkout, orders & payments, customers & subscriptions, products & pricing, settings & configuration, integrations & advanced).",
    hf_pages,
))

# ----- 05 Database Models -----
dm_pages = []
p = use(get('database/models'))
if p: dm_pages.append(p)
dm_sub = sorted(find_prefix('database/models'), key=lambda x: x['path'])
for x in dm_sub:
    use(x)
    dm_pages.append(x)
results.append(write_section(
    '05-database-models.md',
    'FluentCart Developer Docs — Database Models',
    "Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.",
    dm_pages,
))

# ----- 06 Database Schema & Query Builder -----
ds_pages = []
# /database (overview) — there's no exact 'database' page in crawl; check
p = use(get('database'))
if p: ds_pages.append(p)
p = use(get('database/schema'))
if p: ds_pages.append(p)
p = use(get('database/query-builder'))
if p: ds_pages.append(p)
results.append(write_section(
    '06-database-schema-query.md',
    'FluentCart Developer Docs — Database Schema & Query Builder',
    "Schéma de la base de données et patterns du query builder utilisé par FluentCart.",
    ds_pages,
))

# ----- 07 Modules -----
mod_pages = []
mod_sub = sorted(find_prefix('modules'), key=lambda x: x['path'])
for x in mod_sub:
    use(x)
    mod_pages.append(x)
results.append(write_section(
    '07-modules.md',
    'FluentCart Developer Docs — Modules',
    "Modules internes FluentCart : fee system, ghost product selling, licensing, payment methods.",
    mod_pages,
))

# ----- 08 Payment Gateway Integration -----
pmi_pages = []
p = use(get('payment-methods-integration'))
if p: pmi_pages.append(p)
# Ordering: overview, then quick-implementation, payment_setting_fields, paddle-example
ordered_slugs = [
    'payment-methods-integration/quick-implementation',
    'payment-methods-integration/payment_setting_fields',
    'payment-methods-integration/paddle-example',
]
for s in ordered_slugs:
    p = use(get(s))
    if p:
        pmi_pages.append(p)
# add any remaining
remaining = sorted(
    [x for x in find_prefix('payment-methods-integration') if x['path'] not in used_paths],
    key=lambda x: x['path'],
)
for r in remaining:
    use(r)
    pmi_pages.append(r)
results.append(write_section(
    '08-payment-gateway-integration.md',
    'FluentCart Developer Docs — Payment Gateway Integration',
    "Guide complet pour intégrer une nouvelle passerelle de paiement à FluentCart (overview, quick implementation, payment setting fields, exemple Paddle).",
    pmi_pages,
))

# ----- 00 INDEX -----
# Build TOC
toc_lines = [
    "# FluentCart Developer Docs — Index\n",
    "Crawl complet de https://dev.fluentcart.com/ (les 367+ endpoints REST `/restapi/operations/` ont été exclus).\n",
    f"Pages source totales : {len(pages)}.\n",
    "## Sommaire\n",
]
section_info = [
    ('01-getting-started-dev.md', 'Getting Started & Guides', 'getting-started, guides/*'),
    ('02-api-rest-overview.md', 'REST API Overview', 'api/*, restapi/'),
    ('03a-hooks-actions-part1.md + 03b-hooks-actions-part2.md', 'Hooks — Actions (2 parts)', 'hooks/actions/*'),
    ('04a-hooks-filters-part1.md + 04b-hooks-filters-part2.md', 'Hooks — Filters (2 parts)', 'hooks/filters/*'),
    ('05a-database-models-part1.md + 05b-database-models-part2.md + 05c-database-models-part3.md', 'Database — Models (3 parts)', 'database/models/*'),
    ('06-database-schema-query.md', 'Database — Schema & Query Builder', 'database/schema, database/query-builder'),
    ('07-modules.md', 'Modules', 'modules/*'),
    ('08-payment-gateway-integration.md', 'Payment Gateway Integration', 'payment-methods-integration/*'),
]
for fname, label, scope in section_info:
    toc_lines.append(f"- **{label}** — `{fname}` (scope : {scope})")
toc_lines.append("")
toc_lines.append("## Pages incluses (ordre alphabétique des URLs)\n")
# Home page first
home = get('')
if home:
    toc_lines.append(f"- [Home — {home['title']}]({home['url']})")
for p in sorted([x for x in pages if x['path']], key=lambda x: x['path']):
    toc_lines.append(f"- [{p['title']}]({p['url']})")

toc_content = "\n".join(toc_lines) + "\n"

# Also add the home page content into the index (it has no other section)
home_page = get('')
if home_page:
    used_paths.add('')
    toc_content += "\n---\n\n## Home — Page racine\n\n" + render_page(home_page)

(OUT_DIR / '00-INDEX-doc-developer.md').write_text(toc_content, encoding='utf-8')
results.insert(0, ('00-INDEX-doc-developer.md', len(toc_content), len(pages)))

# Report
print("\n=== Files written ===")
total_pages_covered = sum(1 for p in pages if p['path'] in used_paths)
print(f"Pages total kept : {len(pages)}")
print(f"Pages covered    : {total_pages_covered}")
print(f"Pages NOT used   : {len(pages) - total_pages_covered}")
not_used = [p['path'] for p in pages if p['path'] not in used_paths]
if not_used:
    print("Unused paths:")
    for u in not_used:
        print(f"  - {u}")
print()
for fname, size, count in results:
    kb = size / 1024
    print(f"{fname:42}  {kb:7.1f} KB  pages={count}")

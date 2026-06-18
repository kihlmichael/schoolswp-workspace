"""Build a Markdown catalog of FR published articles from a Novamira JSON dump.

One-shot script for the Obsidian bridge outbox. Reads the JSON saved by
novamira execute-php and writes a clean Markdown synthesis.
"""
from __future__ import annotations

import html
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

SRC = Path(sys.argv[1])
DST = Path(sys.argv[2])

raw = json.loads(SRC.read_text(encoding="utf-8"))
posts = raw["data"]["return_value"]["posts"]
count = raw["data"]["return_value"]["count"]


def clean(text: str) -> str:
    return html.unescape(text).strip()


def short_date(iso: str) -> str:
    return datetime.fromisoformat(iso).date().isoformat()


def primary_cat(cats: list[str]) -> str:
    if not cats:
        return "Sans categorie"
    return clean(cats[0])


cat_counter: Counter[str] = Counter()
by_cat: dict[str, list[dict]] = defaultdict(list)

for p in posts:
    cats = [clean(c) for c in p.get("categories", [])]
    cat_counter[primary_cat(cats)] += 1
    by_cat[primary_cat(cats)].append(
        {
            "title": clean(p["title"]),
            "slug": p["slug"],
            "date": short_date(p["date"]),
            "modified": short_date(p["modified"]),
            "permalink": p["permalink"],
            "categories": cats,
        }
    )

dates = [short_date(p["date"]) for p in posts]
date_min = min(dates)
date_max = max(dates)

lines: list[str] = []
lines.append("---")
lines.append("type: synthese")
lines.append("date: 2026-05-24")
lines.append("auteur: Claude Code")
lines.append("sujet: Catalogue des articles FR publies sur schoolswp.com")
lines.append("status: draft")
lines.append("source: Novamira live (WP REST execute-php)")
lines.append("---")
lines.append("")
lines.append("# Catalogue des articles FR publies sur schoolswp.com")
lines.append("")
lines.append("## 1. Perimetre et source")
lines.append("")
lines.append(f"- **Total** : {count} articles")
lines.append("- **Type** : `post` (blog), pas les pages")
lines.append("- **Statut** : `publish`")
lines.append("- **Langue** : `fr` (Polylang)")
lines.append(f"- **Periode couverte** : {date_min} -> {date_max}")
lines.append("- **Source** : Novamira live (execute-php, get_posts + Polylang lang=fr)")
lines.append("- **Date de l'extraction** : 2026-05-24")
lines.append("")
lines.append("Hors perimetre : pages, drafts, traductions DE/EN, contenus prives. Le catalogue est un index, pas une copie. Le contenu reel vit sur schoolswp.com et dans `content/articles/` cote projet.")
lines.append("")
lines.append("## 2. Vue par categorie principale")
lines.append("")
lines.append("La categorie principale est la premiere de la liste WordPress (ordre tel que retourne par `wp_get_post_categories`).")
lines.append("")
lines.append("| Categorie principale | Articles |")
lines.append("|----------------------|---------:|")
for cat, n in cat_counter.most_common():
    lines.append(f"| {cat} | {n} |")
lines.append("")
lines.append("## 3. Index complet par categorie")
lines.append("")
for cat in sorted(by_cat.keys(), key=lambda k: (-cat_counter[k], k)):
    items = by_cat[cat]
    items_sorted = sorted(items, key=lambda x: x["date"], reverse=True)
    lines.append(f"### {cat} ({len(items_sorted)})")
    lines.append("")
    lines.append("| Date | Titre | Slug |")
    lines.append("|------|-------|------|")
    for item in items_sorted:
        title_escaped = item["title"].replace("|", "\\|")
        cats_extra = [c for c in item["categories"] if c != cat]
        extra = ""
        if cats_extra:
            extra = " — autres categories : " + ", ".join(cats_extra)
        lines.append(
            f"| {item['date']} | [{title_escaped}]({item['permalink']}){extra} | `{item['slug']}` |"
        )
    lines.append("")
lines.append("## 4. Index brut (tous articles, par date desc)")
lines.append("")
lines.append("| Date | Titre | Categories |")
lines.append("|------|-------|------------|")
all_posts = []
for cat_items in by_cat.values():
    all_posts.extend(cat_items)
seen = set()
deduped = []
for p in all_posts:
    if p["slug"] in seen:
        continue
    seen.add(p["slug"])
    deduped.append(p)
deduped.sort(key=lambda x: x["date"], reverse=True)
for p in deduped:
    title_escaped = p["title"].replace("|", "\\|")
    cats_str = ", ".join(p["categories"]) if p["categories"] else "—"
    lines.append(f"| {p['date']} | [{title_escaped}]({p['permalink']}) | {cats_str} |")
lines.append("")
lines.append("## 5. Carte de propagation (basee sur `index.md` du vault)")
lines.append("")
lines.append("Le vault n'a actuellement aucune zone dediee aux articles publies de schoolswp.com.")
lines.append("`08_sources/` contient pour le moment uniquement `plugins-wordpress/` (TutorLMS pilote).")
lines.append("`07_projects/schoolswp/` ne contient pas de sous-zone `articles/`.")
lines.append("")
lines.append("Propositions de cible pour la promotion (a arbitrer L0) :")
lines.append("")
lines.append("- **Option A** : `07_projects/schoolswp/articles/index.md` — vue corpus interne, lie au projet maitre. Coherent avec `decisions/`, `offre/`, `identite/`, `strategie/`.")
lines.append("- **Option B** : `08_sources/schoolswp-articles/index.md` — traite le corpus comme une source externe consultable, comme `plugins-wordpress/`. Decouple du projet.")
lines.append("- **Option C** : double — un index leger dans `07_projects/schoolswp/articles/index.md` qui pointe vers `08_sources/schoolswp-articles/` pour le detail.")
lines.append("")
lines.append("Pages du vault potentiellement impactees :")
lines.append("")
lines.append("- `07_projects/schoolswp/identite/piliers.md` — verifier que les 7 piliers (LMS, CRM, SEO, automatisation, ecommerce, freelance, formation) sont coherents avec la distribution des categories ci-dessus.")
lines.append("- `07_projects/schoolswp/strategie/` — la couverture par categorie peut nourrir l'arbitrage editorial.")
lines.append("- `07_projects/schoolswp/decisions/` — verifier qu'aucune decision n'engageait un decoupage editorial different.")
lines.append("- `index.md` racine du vault, section 3 — ajouter la nouvelle sous-zone si l'option A ou B est validee.")
lines.append("")
lines.append("Pages potentiellement contredites : aucune detectee a partir de l'index.md actuel.")
lines.append("")
lines.append("## 6. Notes")
lines.append("")
lines.append("- L'index est une photo a un instant t. Pour rafraichir, relancer l'extraction Novamira (script `tools/scripts/_build_articles_fr_catalog.py`).")
lines.append("- Les permalinks pointent sur le domaine canonique `schoolswp.com`.")
lines.append("- La langue FR est filtree via Polylang (`lang=fr` dans `get_posts`). Aucune traduction DE/EN n'est incluse.")
lines.append("- Pas d'inclusion du contenu HTML des articles. Pour le contenu, voir `content/articles/<slug>/` cote projet ou le permalink.")
lines.append("")

DST.write_text("\n".join(lines), encoding="utf-8")
print(f"OK - {len(lines)} lignes ecrites dans {DST}")
print(f"  - {count} articles")
print(f"  - {len(cat_counter)} categories")

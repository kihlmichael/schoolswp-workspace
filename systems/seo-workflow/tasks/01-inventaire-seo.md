# T1 — Inventaire SEO

## Objectif

Cataloguer toutes les URLs de schoolswp.com avec leur rôle SEO et business.

## Inputs

- sitemap.xml de schoolswp.com
- Export GSC (optionnel pour enrichissement)

## Output

- Onglet `T1_INVENTAIRE` dans Google Sheets
- CSV local : `data/seo-workflow/inventory_urls.csv`

## Prompt orchestrateur

```
Tâche T1 : Inventaire SEO

Analyse le sitemap de schoolswp.com et classe chaque URL selon :
- type_page : article | page | category | tag | home
- cluster : lms | crm | seo | automatisation | ecommerce | freelance | formation
- role_SEO : pillar | satellite | support | orphan
- role_business : money | lead | trust | nav
- priorite : 1-5 (5 = critique)

Output : tableau CSV avec colonnes url, type_page, langue, cluster, role_SEO, role_business, priorite, observations
```

## KPIs

- >= 50 URLs catalogées
- 0 URL manquante vs sitemap
- Tous les clusters représentés

# Google Sheets Schema — SEO Workflow

## Onglet T1_INVENTAIRE

| Colonne | Type | Valeurs acceptées | Formule |
|---------|------|-----------------|--------|
| url | string | URL absolue | — |
| type_page | string | article, page, category, tag, home | — |
| langue | string | fr, en | — |
| cluster | string | lms, crm, seo, automatisation, ecommerce | — |
| role_SEO | string | pillar, satellite, support, orphan | — |
| role_business | string | money, lead, trust, nav | — |
| priorite | int | 1-5 | — |
| observations | string | texte libre | — |

## Onglet T2_OPPORTUNITES

| Colonne | Type | Description |
|---------|------|-------------|
| url | string | URL concernée |
| requete | string | Requête GSC |
| type_opportunite | string | A, B, C, D |
| impressions | int | 90 derniers jours |
| ctr | float | % |
| position | float | Moyenne |
| score | float | Impact/effort |
| action | string | Action recommandée |

## Onglet T3_AUDIT_TECH

| Colonne | Type | Description |
|---------|------|-------------|
| url | string | URL concernée |
| issue_type | string | noindex, h1_missing, duplicate_title, slow, broken_link |
| severity | string | critical, high, medium, low |
| detail | string | Détail de l'issue |
| status | string | open, fixed, wontfix |

## Onglet T10_ROADMAP

| Colonne | Type | Description |
|---------|------|-------------|
| action | string | Description de l'action |
| type | string | create, optimize, technical, link |
| priorite | int | 1-5 |
| impact | int | 1-5 |
| effort | int | 1-5 |
| deadline | date | YYYY-MM-DD |
| statut | string | todo, in_progress, done |

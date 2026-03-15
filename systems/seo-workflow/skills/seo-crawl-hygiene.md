# SEO Crawl Hygiene

## Rôle

Catégorise et nettoie les URLs du site pour optimiser le crawl budget.

## 7 Catégories d'URLs

| Catégorie | Critères | Action |
|-----------|---------|--------|
| A — Indexable | 200, index, canonical self | Garder |
| B — Noindex volontaire | noindex tag | Vérifier intention |
| C — Redirect | 301/302 | Auditer destination |
| D — Erreur | 404/410/5xx | Corriger ou supprimer |
| E — Param URL | `?page=`, `?filter=` | Bloquer dans robots.txt |
| F — Dupliquat | Canonical pointe ailleurs | Vérifier canonical |
| G — Thin content | < 300 mots, pas de valeur | Enrichir ou noindex |

## Action table

| Catégorie | Robots.txt | Sitemap | Canonical | Priorité |
|-----------|-----------|---------|-----------|----------|
| A | Allow | Inclure | Self | — |
| B | Allow | Exclure | Self | Faible |
| C | Allow | Exclure | — | Moyenne |
| D | — | Exclure | — | Haute |
| E | Disallow | Exclure | — | Haute |
| F | Allow | Exclure | Externe | Moyenne |
| G | Allow | Inclure | Self | Haute |

## Output CSV

```
url,status_code,category,action,priority,notes
https://schoolswp.com/article,200,A,keep,—,
https://schoolswp.com/tag/wp,200,G,enrich,haute,300 mots
```

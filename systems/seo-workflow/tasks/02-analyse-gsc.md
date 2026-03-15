# T2 — Analyse GSC

## Objectif

Identifier les opportunités SEO depuis Google Search Console.

## Inputs

- API GSC (scope : lecture seule)
- Période : 90 derniers jours
- Site : schoolswp.com

## Output

- Onglet `T2_OPPORTUNITES`
- Top 20 opportunités triées par score

## Prompt

```
Tâche T2 : Analyse GSC

Depuis les données GSC (90j), identifie les opportunités par type :
- Type A : CTR < 3% avec impressions > 100
- Type B : Position 8-20 avec clics > 0
- Type C : Cannibalization (2+ URLs même requête)
- Type D : 0 impression sur URLs du sitemap

Calcule le score = (impressions/100) * (1/CTR) * (20-position)
Output : tableau trié par score décroissant
```

## KPIs

- >= 5 opportunités identifiées
- Au moins 1 opportunité de chaque type

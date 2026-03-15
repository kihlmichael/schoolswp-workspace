# GSC Opportunity Scanner

## Rôle

Identifie et classe les opportunités SEO depuis les données Google Search Console.

## 4 Types d'opportunités

### A — CTR faible (impressions élevées)
- Critères : impressions > 100, CTR < 3%, position <= 20
- Action : Réécrire title + meta description
- Impact : Trafic sans nouveau contenu

### B — Position 8-20 (page 2)
- Critères : position entre 8 et 20, clics > 0
- Action : Enrichir contenu + maillage entrant
- Impact : Passer en top 5 = x3-x5 clics

### C — Cannibalization
- Critères : 2+ URLs sur la même requête
- Action : Fusionner ou redéfinir le focus keyword
- Impact : Consolider l'autorité sur la requête

### D — 0 impression (contenu non indexé)
- Critères : URL dans sitemap, 0 impression sur 90j
- Action : Audit noindex + qualité contenu + maillage
- Impact : Activer des pages dormantes

## Formule de scoring

```
Score = (impressions / 100) * (1 / CTR) * (20 - position)
```

Plus le score est élevé, plus l'opportunité est prioritaire.

## Output attendu

Tableau trié par score décroissant :

| URL | Requête | Type | Impressions | CTR | Position | Score |
|-----|---------|------|------------|-----|----------|-------|

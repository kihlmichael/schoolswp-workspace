# T4 — Analyse SERP

## Objectif

Analyser les SERP des keywords cibles pour identifier les gaps de contenu.

## Inputs

- Top 20 opportunités T2
- API DataForSEO (SERP Organic)

## Output

- Onglet `T4_SERP`
- Top 3 concurrents par keyword
- Gaps identifiés

## Prompt

```
Tâche T4 : Analyse SERP

Pour chaque keyword de T2_OPPORTUNITES :
1. Analyser les 10 premiers résultats
2. Identifier les formats gagnants (listicle, guide, comparatif, tool)
3. Detecter les angles non couverts par les concurrents
4. Évaluer la difficulté vs notre DA

Output : tableau avec keyword, format_gagnant, angle_gap, difficulte
```

## KPIs

- 100% des keywords T2 analysés
- >= 5 angles de différenciation identifiés

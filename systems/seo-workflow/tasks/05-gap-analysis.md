# T5 — Gap Analysis

## Objectif

Identifier les keywords couverts par les concurrents mais absents de schoolswp.com.

## Inputs

- CSV keywords WPMarmite (DataForSEO)
- T1_INVENTAIRE

## Output

- Onglet `T5_GAP`
- Top 30 keywords à cibler

## Concurrent principal

`wpmarmite.com` — leader FR WordPress

## Prompt

```
Tâche T5 : Gap Analysis

Compare les keywords de wpmarmite.com vs schoolswp.com :
- Keywords où WPMarmite est top 10, schoolsWP absent
- Volume > 100 recherches/mois
- Intent : informationnelle ou décisionnelle
- Cluster : lms | crm | seo | automatisation

Tri par volume décroissant. Output : keyword, volume, diff, cluster, angle_differentiation
```

## KPIs

- >= 30 keywords identifiés
- Répartition sur >= 3 clusters

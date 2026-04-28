# Instructions d'utilisation

## Entrée minimale

Déposer un CSV ou un Excel.

## Entrée recommandée

Fournir en plus :

- la feuille à analyser (si Excel multi-feuilles)
- la métrique principale
- les dimensions prioritaires
- le contexte métier
- la période à comparer

## Exemple d'instruction simple

```
Analyse ce fichier et produis un rapport complet, clair et orienté décision.
```

## Exemple d'instruction enrichie

```
Analyse la feuille `Ventes 2026` de ce fichier Excel.
Utilise `revenue` comme KPI principal.
Regarde surtout les dimensions `product`, `channel` et `country`.
Compare si possible les performances entre janvier et février.
Le rapport doit rester compréhensible pour un non-spécialiste.
```

## Paramètres optionnels reconnus

| Paramètre           | Exemple                                  | Utilité                                   |
| ------------------- | ---------------------------------------- | ----------------------------------------- |
| `sheet_name`        | "Ventes 2026"                            | Feuille Excel à analyser                  |
| `primary_metric`    | "revenue"                                | KPI principal                             |
| `dimensions`        | "product, country"                       | Axes d'analyse prioritaires               |
| `comparison_period` | "janvier vs février"                     | Comparaison temporelle                    |
| `business_context`  | "lancement d'un nouveau produit en mars" | Contexte pour affiner les recommandations |
| `focus_area`        | "anomalies seulement"                    | Recentrer l'analyse                       |

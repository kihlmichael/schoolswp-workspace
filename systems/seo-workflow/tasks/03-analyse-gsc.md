# T3 — Analyse Google Search Console

## Objectif

Identifier les opportunités concrètes de trafic via GSC : pages à fort potentiel, CTR à améliorer, cannibalisation de requêtes.

## Pourquoi cette tâche existe

GSC est la seule source de vérité sur le trafic réel de schoolsWP. Cette tâche transforme les données brutes en actions prioritaires.

## Outils clés

- Google Search Console (exports CSV)
- Skill : `gsc-opportunity-scanner` (voir `skills/gsc-opportunity-scanner.md`)
- Doc `.claude/docs/schoolswp-gsc-radar.md` (référence GSC schoolsWP)
- Google Sheets (onglet `03_GSC`)

## Entrées exactes

- Export GSC "Performance > Pages" : CSV 28j
- Export GSC "Performance > Pages" : CSV 3m
- Export GSC "Performance > Pages" : CSV 12m
- Export GSC "Performance > Requêtes" : CSV 28j
- `01_Inventory` rempli (pour filtrer les pages valides uniquement)

## Comment exporter depuis GSC

1. Ouvrir GSC → schoolswp.com → Performance
2. Onglet "Pages" → Date : 28 derniers jours → Exporter CSV
3. Répéter pour 3 mois et 12 mois
4. Onglet "Requêtes" → Date : 28 derniers jours → Exporter CSV

## Étapes

1. Charger les 4 exports dans Google Sheets onglet `03_GSC`
2. Détecter les pages à fort potentiel non exploité :
   - Beaucoup d'impressions + CTR < 3% → recommandation title/meta
   - Positions 8-20 → pages à pousser en Top 3 via contenu ou maillage
3. Détecter la cannibalisation : requêtes associées à plusieurs URLs différentes
4. Pour chaque cas, proposer une action précise avec KPI cible
5. Identifier le Top 10 quick wins (CTR ou position)
6. Remplir `03_GSC` et rédiger Doc `03_GSC`

## Sorties attendues

**Fichier :** `gsc_opportunities.json`
**Destination :** Onglet `03_GSC`

**Schéma CSV :**

```
url, query, impressions, clics, ctr, position, issue, action, priority
```

**Valeurs issue :** ctr-faible | position-8-20 | cannibalisation | impressions-zero | ctr-ok
**Valeurs action :** optimiser-title | renforcer-contenu | fusionner-pages | ameliorer-maillage | creer-page

**Doc :** `03_GSC.gdoc` — Top 10 quick wins avec CTR cible et gain estimé

**Payload exemple :**

```json
{
  "url": "https://schoolswp.com/seo-wordpress/",
  "query": "meilleur plugin SEO",
  "impressions": 12000,
  "clicks": 300,
  "ctr": 2.5,
  "position": 9.7,
  "issue": "position-8-20",
  "action": "renforcer-contenu + améliorer maillage",
  "priority": "P1"
}
```

## Observables

- Impressions, clics, CTR, positions actuels (données GSC réelles)
- URLs présentes dans GSC (indexées et recevant des impressions)
- Requêtes associées à plusieurs URLs (détectable dans l'export)

## Hypothèses à valider

- Volume de recherche exact par mot-clé (À VALIDER via DataForSEO — T4)
- Impact réel d'un changement de title sur le CTR (À VALIDER après implémentation)
- Cause de la cannibalisation : intention ou contenu (À VALIDER via lecture des pages concernées)

## Dépendances

- **T1 obligatoire** : filtrer uniquement les pages valides de l'inventaire
- **T2 recommandé** : écarter les pages noindexées avant analyse

## KPIs

| KPI                              | Baseline         | Objectif                        |
| -------------------------------- | ---------------- | ------------------------------- |
| CTR moyen pages P1               | CTR actuel (GSC) | +3 à +5 points sur pages cibles |
| Pages en positions 8-20 traitées | 0                | 100% avec action définie        |
| Cannibalisations identifiées     | 0                | Toutes documentées avec action  |

## Effort / Priorité

- Effort : S
- Priorité : **P1** — données directement actionnables

## Risques / Blocages

- GSC non configuré → bloquer T3, noter le blocage, configurer GSC avant de continuer
- Exports GSC vides (site nouveau) → utiliser uniquement les observables du sitemap pour T3, passer en P3
- Cannibalisation non confirmable sans lecture des pages → noter "À VALIDER" et indiquer les URLs suspectes

## Intégration n8n

```
n8n HTTP Request (GSC API ou import CSV)
  → Function Node (calcul opportunités : impressions > X AND ctr < 0.03)
  → Google Sheets (Append Rows → 03_GSC)
```

## Prompt agent IA

```
RÔLE : Tu es un analyste Google Search Console pour schoolsWP.com.

OBJECTIF : Identifier les opportunités concrètes de trafic SEO à partir des données GSC réelles.

INPUTS :
- Exports GSC Pages + Requêtes (CSV pour 28j, 3m, 12m)
- Inventaire URLs valides (01_Inventory)

ACTIONS (dans l'ordre) :
1. Analyse les performances par page : impressions, clics, CTR, position
2. Repère les pages à fort potentiel non exploité :
   - Impressions élevées + CTR < 3% → title/meta à optimiser
   - Positions 8-20 → contenu ou maillage à renforcer
3. Détecte la cannibalisation : une requête associée à plusieurs URLs différentes
4. Pour chaque opportunité : propose une action précise et un KPI cible
5. Classe les 10 meilleures opportunités quick win

RÈGLES DE PREUVE :
- Utiliser uniquement les données GSC fournies — ne pas inventer de trafic
- CTR faible : comparer à la médiane des pages du même cluster, pas à une valeur absolue
- Cannibalisation confirmée uniquement si la même requête génère des impressions sur 2+ URLs différentes

FORMAT DE SORTIE :
- JSON : url, query, impressions, clics, ctr, position, issue, action, priority
- Top 10 quick wins listés avec : page, action, CTR cible estimé, effort (XS/S/M)

CONDITIONS D'ARRÊT :
- Toutes les pages avec >500 impressions ont une classification issue + action
- Toutes les cannibalisations identifiées ont une action proposée
```

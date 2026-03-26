# T5 — Clusters & Cannibalisation

## Objectif

Définir la structure thématique du contenu, identifier les conflits de cannibalisation et corriger l'architecture sémantique.

## Outils clés

- Skill : `cluster-cocon-automatique` (existant dans `.claude/skills/`)
- Skill : `topical-authority-map` (existant dans `.claude/skills/`)
- Agent Python : `agents.cluster_architect.cli`
- Google Sheets (onglet `05_Clusters`)

## Entrées exactes

- `01_Inventory` : URLs et clusters
- `03_GSC` : requêtes vs URLs (cannibalisation)
- `04_Competitors` : gaps concurrentiels par cluster

## Étapes

1. Construire la carte clusters : pour chaque cluster, lister la page pilier + satellites
2. Identifier les requêtes GSC associées à plusieurs URLs (cannibalisation)
3. Pour chaque cannibalisation : proposer l'action (garder+améliorer / fusionner / rediriger)
4. Identifier les gaps de couverture (mots-clés sans page assignée)
5. Prioriser par cluster selon trafic potentiel et valeur business
6. Remplir `05_Clusters` + rédiger Doc `05_Clusters`

## Sorties attendues

**Fichier :** `cluster_map.xlsx`
**Destination :** Onglet `05_Clusters`

**Schéma CSV :**

```
cluster, pilier_url, satellites_urls, complete, cannibal_risk, gaps_keywords, action_recommandee
```

**Valeurs complete :** oui | partiel | non
**Valeurs cannibal_risk :** haut | moyen | faible | aucun
**Valeurs action_recommandee :** renforcer | fusionner | rediriger | creer | archiver

## Observables

- Tags et catégories visibles sur le site (liens de navigation)
- Contenu similaire détectable par lecture des URLs du même cluster
- Requêtes GSC associées à plusieurs pages (données GSC réelles)

## Hypothèses à valider

- Vrai conflit SEO de cannibalisation (À VALIDER via positions GSC simultanées sur la même requête)
- Volume exact des mots-clés manquants par cluster (À VALIDER via DataForSEO)
- Impact de la fusion de pages sur le trafic global (À VALIDER post-implémentation)

## Dépendances

- **T1, T3, T4 obligatoires**

## KPIs

| KPI                                        | Baseline   | Objectif                         |
| ------------------------------------------ | ---------- | -------------------------------- |
| Clusters complets (pilier + ≥3 satellites) | À calculer | ≥80% des clusters P1             |
| Cannibalisations corrigées                 | 0          | 100% avec action définie         |
| Gaps couverts par cluster P1               | inconnu    | ≥3 sujets identifiés par cluster |

## Effort / Priorité

- Effort : M
- Priorité : **P2**

## Risques / Blocages

- Trop de clusters à traiter → commencer par les 3 clusters P1 (SEO, LMS, Automatisation)
- Fusion de pages risquée sans redirection → toujours implémenter une 301 vers la page gagnante

## Intégration n8n

```
n8n Function Node (associer requêtes GSC → clusters depuis 03_GSC + 01_Inventory)
  → Agent IA (classifier cannibalisations)
  → Google Sheets (Append Rows → 05_Clusters)
```

## Prompt agent IA

```
RÔLE : Tu es un architecte de contenu SEO pour schoolsWP.com.

OBJECTIF : Cartographier les clusters sémantiques et identifier les cannibalisations.

INPUTS :
- 01_Inventory : toutes les URLs classifiées par cluster
- 03_GSC : requêtes et pages associées
- 04_Competitors : gaps concurrentiels

ACTIONS (dans l'ordre) :
1. Pour chaque cluster, liste la page pilier et les pages satellites existantes
2. Détecte les requêtes GSC qui génèrent des impressions sur 2+ URLs du même cluster
3. Pour chaque cannibalisation : propose garder+améliorer / fusionner+rediriger / définir canonical
4. Identifie les mots-clés non couverts par cluster (gaps)
5. Distingue ce qui est visible (structure URL, tags) vs à valider (volume, positions réelles)

FORMAT DE SORTIE :
- XLSX : cluster, pilier_url, satellites_urls, complete, cannibal_risk, gaps_keywords, action_recommandee
- Doc 1-page : stratégie cluster (renforcer / fusionner / créer) par cluster P1

CONDITIONS D'ARRÊT :
- Tous les clusters P1 ont une page pilier définie
- Toutes les cannibalisations ont une action assignée
- Tous les gaps P1 sont listés avec format recommandé
```

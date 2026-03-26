# T4 — Benchmark concurrentiel (DataForSEO)

## Objectif

Identifier les gaps de contenu par cluster en comparant schoolsWP aux concurrents qui dominent les SERPs sur les mots-clés cibles.

## Outils clés

- DataForSEO API (SERP Advanced + Keywords Data)
- Skill : `seo-competitor-gap-radar` (existant dans `.claude/skills/`)
- n8n HTTP Request
- Google Sheets (onglet `04_Competitors`)

## Entrées exactes

- Liste de mots-clés cœur par cluster (issue de `03_GSC` + `01_Inventory`)
- Clé API DataForSEO (dans `.env` — ne pas committer)
- Endpoint SERP : `https://api.dataforseo.com/v3/serp/google/organic/live/advanced`
- Endpoint Keywords : `https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live`

## Étapes

1. Pour chaque cluster, sélectionner ~20 mots-clés cœur (depuis T3 GSC + sitemap)
2. Appeler DataForSEO SERP API → extraire top 3 domaines + type de résultat (guide, comparatif, liste, vidéo)
3. Appeler DataForSEO Keywords API → volumes de recherche + requêtes associées
4. Identifier les concurrents dominants par cluster
5. Documenter les gaps : cluster X, mot-clé Y, format manquant chez schoolsWP
6. Remplir `04_Competitors` + rédiger Doc `04_Competitors`

## Sorties attendues

**Fichier :** `serp_data.json` (données brutes API)
**Destination :** Onglet `04_Competitors`

**Schéma CSV :**

```
competiteur, cluster, mot_cle, volume, presence_schoolsWP, gap, opportunite, format_gagnant, priorite
```

**Payload exemple :**

```json
{
  "keyword": "plugin cache WordPress",
  "top_domains": ["wpmarmite.com", "hostinger.fr"],
  "top_format": "comparatif",
  "volume": 1000,
  "difficulty": "medium",
  "schoolsWP_present": false,
  "gap": "aucun comparatif dédié"
}
```

## Observables

- Top 3 domaines pour chaque requête (données SERP réelles)
- Format des pages qui ranken (guide, comparatif, liste, avis)
- Présence ou absence de schoolsWP dans les SERPs

## Hypothèses à valider

- Volume de recherche exact (À VALIDER via DataForSEO — données estimées)
- Difficulté réelle des mots-clés (À VALIDER via KD DataForSEO)
- Intention réelle de chaque requête (À VALIDER via lecture des SERPs)

## Dépendances

- **T3 recommandé** : pour les mots-clés initiaux extraits de GSC

## KPIs

| KPI                         | Baseline | Objectif                         |
| --------------------------- | -------- | -------------------------------- |
| Gaps identifiés par cluster | 0        | ≥3 gaps actionnables par cluster |
| Nouveaux formats à créer    | 0        | Liste complète priorisée         |

## Effort / Priorité

- Effort : M
- Priorité : **P2**

## Risques / Blocages

- Crédits DataForSEO insuffisants → prioriser les clusters P1 (SEO, LMS, Automatisation)
- API rate limit → espacer les appels, utiliser le batch mode

## Intégration n8n

```
n8n HTTP Request (DataForSEO SERP batch)
  → Function Node (parse top_domains + format + gap)
  → Google Sheets (Append Rows → 04_Competitors)
```

## Prompt agent IA

```
RÔLE : Tu es un analyste SEO concurrentiel utilisant DataForSEO.

OBJECTIF : Identifier les gaps de contenu de schoolsWP vs concurrents par cluster.

INPUTS :
- Liste de mots-clés stratégiques par cluster
- Résultats API DataForSEO SERP + Keywords

ACTIONS (dans l'ordre) :
1. Pour chaque mot-clé, identifie les top 3 domaines dans la SERP Google
2. Détermine le format gagnant : guide | comparatif | liste | avis | vidéo
3. Vérifie si schoolsWP est présent dans le top 10
4. Identifie les clusters où schoolsWP est absent ou faiblement présent
5. Pour chaque gap : formule une opportunité concrète (ex : "créer un comparatif sur plugin-cache")
6. Marque clairement : Observable (position SERP visible) vs À VALIDER (volume exact)

FORMAT DE SORTIE :
- CSV : competiteur, cluster, mot_cle, volume, presence_schoolsWP, gap, opportunite, format_gagnant, priorite
- Résumé des 5 gaps prioritaires avec format recommandé

CONDITIONS D'ARRÊT :
- Tous les clusters ont ≥1 gap identifié ou "aucun gap" confirmé
- Tous les gaps ont un format et une opportunité définis
```

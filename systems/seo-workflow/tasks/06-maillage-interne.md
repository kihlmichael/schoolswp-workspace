# T6 — Maillage interne

## Objectif

Redistribuer le link juice vers les pages stratégiques (piliers, money pages) et éliminer les pages orphelines.

## Outils clés

- Export crawl (inlinks/outlinks par page)
- Skill : `m1m3-urls-internal-linking` (existant dans `.claude/skills/`)
- Agent Python : `agents.article_pipeline.internal_link_strategist`
- Google Sheets (onglet `06_Linking`)

## Entrées exactes

- Export crawl CSV : `source_url, target_url, anchor_text, inlinks_count, outlinks_count`
- `cluster_map.xlsx` (T5) : pages importantes par cluster
- `01_Inventory` : pages business, newsletters, pages de conversion

## Étapes

1. Analyser la distribution actuelle des liens internes :
   - Pages orphelines (0 liens entrants depuis les pages du site)
   - Pages sur-maillées (trop de liens vers elles, diluant les autres)
   - Pages stratégiques sous-maillées (piliers avec peu de liens entrants)
   - Profondeur excessive (pages à >3 clics de la homepage)
2. Définir les règles de maillage pour schoolsWP :
   - Chaque article lie vers son hub parent
   - Chaque article lie vers 1-2 articles connexes du même cluster
   - Chaque article lie vers 1 page business associée
3. Générer la liste concrète des liens à ajouter
4. Prioriser par impact (pages piliers en P1, articles en P2)
5. Remplir `06_Linking` + rédiger Doc `06_Linking`

## Sorties attendues

**Fichier :** `internal_links_to_add.csv`
**Destination :** Onglet `06_Linking`

**Schéma CSV :**

```
source_url, cible_url, anchor_recommande, contexte, reason_SEO, reason_CRO, priority
```

**Exemple de ligne :**

```
source: /guide-wordpress/
cible: /liste-plugins-cache/
anchor: "meilleurs plugins cache"
reason_SEO: "renforce cluster Performance"
reason_CRO: "vers page affiliée"
priority: P1
```

## Observables

- Structure de menu (hubs sur-liés depuis navigation)
- Articles anciens sans lien interne depuis autres pages (observables via crawl)
- Pages de conversion sans liens entrants depuis les articles de contenu

## Hypothèses à valider

- Liens existants réels entre pages (À VALIDER via crawl complet)
- Impact sur le trafic des pages cibles après ajout de liens (À VALIDER via GSC post-implémentation)
- Comportement du thème WordPress sur les liens contextuels (À VALIDER via test)

## Dépendances

- **T2 obligatoire** : crawl export avec inlinks/outlinks
- **T5 obligatoire** : cluster_map pour identifier les pages importantes

## KPIs

| KPI                         | Baseline            | Objectif                            |
| --------------------------- | ------------------- | ----------------------------------- |
| Pages orphelines piliers    | À VALIDER via crawl | 0 pages pilier sans lien            |
| Profondeur moyenne pages P1 | À VALIDER via crawl | ≤2 clics depuis homepage            |
| Liens vers money pages      | À VALIDER via crawl | ≥3 liens contextuels par money page |

## Effort / Priorité

- Effort : M
- Priorité : **P2**

## Risques / Blocages

- Pas de crawl disponible → lancer Screaming Frog en mode gratuit (500 URLs)
- Modification des templates WordPress nécessaire → coordonner avec T9 (CTA) pour une seule intervention

## Intégration n8n

```
n8n Function Node (map crawl → identifier liens manquants depuis cluster_map)
  → Google Sheets (Append Rows → 06_Linking)
```

## Prompt agent IA

```
RÔLE : Tu es un spécialiste du maillage interne SEO pour schoolsWP.com.

OBJECTIF : Identifier les liens internes manquants et générer un plan d'ajout priorisé.

INPUTS :
- Export crawl (inlinks/outlinks par page)
- cluster_map.xlsx (pages piliers et satellites)
- 01_Inventory (pages business, conversion, newsletter)

ACTIONS (dans l'ordre) :
1. Identifie les pages orphelines (0 lien entrant depuis le site) ou sous-maillées (<2 liens)
2. Identifie les pages piliers sans liens depuis leurs satellites
3. Identifie les pages business sans lien depuis les articles de contenu associés
4. Pour chaque lien manquant : recommande source, cible, ancre contextuelle
5. Applique les règles : article → hub parent + 1-2 articles connexes + 1 page business
6. Marque "À VALIDER" tout ce qui nécessite vérification terrain

FORMAT DE SORTIE :
- CSV : source_url, cible_url, anchor_recommande, contexte, reason_SEO, reason_CRO, priority
- Doc 1-page : stratégie maillage (exemple : "ajouter module articles liés sur tous les hubs")

CONDITIONS D'ARRÊT :
- Toutes les pages piliers P1 ont ≥3 liens entrants recommandés
- Toutes les pages orphelines P1 ont au moins 1 lien recommandé
- Toutes les money pages ont ≥1 lien depuis articles de contenu
```

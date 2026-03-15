# T1 — Inventaire SEO observable

## Objectif

Lister toutes les pages clés de schoolsWP.com par rôles SEO/business et clusters thématiques, à partir des éléments visibles du site uniquement.

## Pourquoi cette tâche existe

Sans inventaire structuré, toutes les tâches suivantes travaillent sur des données incomplètes. C'est le point d'entrée obligatoire du workflow.

## Outils clés

- Google Sheets (onglet `01_Inventory`)
- n8n HTTP Request (scraping sitemap)
- Agent IA (classification)

## Entrées exactes

- URL plan de site : `https://schoolswp.com/plan-de-site`
- Menu principal du site (Observable : navigation visible)
- Listes d'articles sur la page d'accueil (Observable : visible sans authentification)

## Étapes

1. Scraper `https://schoolswp.com/plan-de-site` → extraire toutes les URLs listées
2. Extraire les URLs du menu principal (hubs, catégories)
3. Lister les articles en page d'accueil
4. Pour chaque URL : classer type_page, cluster, langue, role_SEO, role_business
5. Prioriser (P1/P2/P3) selon importance dans l'architecture
6. Remplir `01_Inventory` dans Google Sheets
7. Rédiger synthèse Doc `01_Inventaire` (5-10 lignes)

## Sorties attendues

**Fichier :** `inventory_urls.csv`
**Destination :** Onglet `01_Inventory`

**Schéma CSV :**

```
url, type_page, langue, cluster, sous_cluster, role_SEO, role_business, priorite, observations, notes
```

**Valeurs type_page :** hub | categorie | article | page-conversion | outil | statique
**Valeurs cluster :** SEO | LMS | Automatisation | Hebergement | Performance | Plugins | Affiliation | Business
**Valeurs langue :** fr | en | de
**Valeurs role_SEO :** pilier | support | money | orpheline
**Valeurs role_business :** lead | affilie | vente | support | newsletter
**Valeurs priorite :** P1 | P2 | P3

**Doc :** `01_Inventaire.gdoc` — synthèse en 5-10 lignes + points d'attention

## Observables

- Catégories visibles dans le menu
- Pages d'auteur présentes ou absentes
- Présence de versions EN et/ou DE dans le menu
- Types de pages listés dans le sitemap HTML
- Listes d'articles visibles en page d'accueil

## Hypothèses à valider (via GSC ou crawl)

- Pages réellement indexées par Google (À VALIDER via GSC Coverage)
- Trafic réel par page (À VALIDER via GSC Performance)
- Profondeur réelle de chaque page (À VALIDER via crawl)
- Présence de pages non listées dans le sitemap (À VALIDER via crawl complet)

## Dépendances

- Aucune (point de départ du workflow)

## KPIs

| KPI                       | Baseline | Objectif                 |
| ------------------------- | -------- | ------------------------ |
| % URLs classifiées        | 0%       | 100% des URLs du sitemap |
| Nombre de hubs identifiés | inconnu  | Tous les hubs du menu    |
| Clusters couverts         | inconnu  | ≥5 clusters identifiés   |

## Effort / Priorité

- Effort : S (petite)
- Priorité : **P1** — bloquant pour toutes les tâches suivantes

## Risques / Blocages

- Sitemap HTML inaccessible → fallback : sitemap.xml (`https://schoolswp.com/sitemap.xml`)
- Scraping bloqué → utiliser n8n avec user-agent standard ou scraper manuellement
- URLs en double dans le sitemap → dédupliquer par URL canonique

## Intégration n8n

```
n8n HTTP Request (scrape plan-de-site)
  → Function Node (parse URLs + classify)
  → Google Sheets (Append Rows → 01_Inventory)
```

**Payload exemple :**

```json
{
  "url": "https://schoolswp.com/seo-wordpress/",
  "type_page": "hub",
  "langue": "fr",
  "cluster": "SEO",
  "role_SEO": "pilier",
  "role_business": "lead",
  "priorite": "P1"
}
```

## Prompt agent IA

```
RÔLE : Tu es un analyste SEO pour un site WordPress (schoolsWP.com).

OBJECTIF : Construire l'inventaire SEO complet du site.

INPUTS :
- Plan de site HTML (liste de toutes les URLs)
- Structure du menu principal
- Listes d'articles visibles en page d'accueil

ACTIONS (dans l'ordre) :
1. Extrais toutes les URLs significatives depuis les inputs fournis
2. Pour chaque URL : détermine type_page, cluster, langue, role_SEO, role_business
3. Priorise chaque URL : P1 (critique), P2 (moyen), P3 (longue traîne)
4. Liste les observations visibles (ex : "page d'auteur présente", "version EN dans le menu")
5. Note séparément les hypothèses à valider (ex : "indexation à confirmer via GSC", "trafic inconnu")

RÈGLES DE PREUVE :
- Ne jamais supposer un trafic sans donnée GSC — noter "À VALIDER"
- Ne jamais supposer une indexation sans crawl ou GSC Coverage — noter "À VALIDER"
- Distinguer explicitement Observable vs Hypothèse à valider

FORMAT DE SORTIE :
- CSV conforme au schéma : url, type_page, langue, cluster, sous_cluster, role_SEO, role_business, priorite, observations, notes
- Bref résumé (5 lignes max) des points clés en tête

CONDITIONS D'ARRÊT :
- Toutes les URLs du sitemap sont classifiées
- Chaque URL a un type_page, un cluster et un role_SEO renseignés
- Les observations et hypothèses sont distinguées explicitement
```

# T2 — Crawl & Indexation

## Objectif

Détecter les pages à exclure de l'index (ou à corriger) pour optimiser le budget crawl et éliminer la duplication.

## Pourquoi cette tâche existe

Les pages utilitaires (login, tags, feeds, archives) gaspillent le budget crawl et diluent l'autorité. Les supprimer ou les noindexer est un gain SEO immédiat sans créer de contenu.

## Outils clés

- Export crawl (Screaming Frog ou n8n HTTP batch)
- Skill : `seo-crawl-hygiene` (voir `skills/seo-crawl-hygiene.md`)
- Google Sheets (onglet `02_Hygiene`)

## Entrées exactes

- Export crawl CSV : `url, statut_http, canonical, meta_robots, inlinks, outlinks, profondeur`
- `01_Inventory` rempli (T1 obligatoire)
- Liste observée des pages utilitaires depuis le plan de site

## Étapes

1. Charger le CSV crawl dans l'agent
2. Identifier les pages utilitaires et inutiles :
   - pages login / portail assistance
   - archives tags et catégories vides
   - older posts / flux RSS
   - pages auteur sans contenu
   - URL avec paramètres (?p=, ?s=, etc.)
3. Identifier les statuts problématiques : 4xx, redirections chaînées, 5xx
4. Détecter les doublons (canonical mal défini ou manquant, même contenu sur plusieurs URLs)
5. Classer chaque URL/pattern : `Keep | Noindex | Canonical→X | Redirect→X`
6. Remplir `02_Hygiene` dans Google Sheets
7. Rédiger Doc `02_Hygiene` : quick wins prioritaires

## Sorties attendues

**Fichier :** `tech_hygiene_actions.csv`
**Destination :** Onglet `02_Hygiene`

**Schéma CSV :**

```
url_or_pattern, issue, action, impact, effort, priority, status
```

**Valeurs action :** Keep | Noindex | Canonical | Redirect | Investigate
**Valeurs impact :** H | M | L
**Valeurs priority :** P1 | P2 | P3
**Valeurs status :** todo | done | blocked

**Doc :** `02_Hygiene.gdoc` — résumé + tableau quick wins (noindex archives, redirects)

## Observables

- Pages support/login listées dans le sitemap HTML
- Présence de pages tags dans la navigation
- Archives catégories visibles dans le menu
- URL avec paramètres apparents dans le sitemap

## Hypothèses à valider

- Indexabilité réelle de chaque page (À VALIDER via GSC Coverage)
- Présence de meta robots noindex/index sur chaque page (À VALIDER via crawl complet)
- Existence de doublons de contenu non détectables sans crawl (À VALIDER via crawl complet)
- Budget crawl actuel gaspillé en % (À VALIDER via GSC logs ou crawl)

## Dépendances

- **T1 obligatoire** : `01_Inventory` pour identifier les pages concernées

## KPIs

| KPI                        | Baseline            | Objectif                         |
| -------------------------- | ------------------- | -------------------------------- |
| Pages non-SEO dans l'index | À VALIDER via GSC   | 0 pages utilitaires indexées     |
| Redirections chaînées      | À VALIDER via crawl | 0 redirections en chaîne         |
| Pages orphelines P1        | À VALIDER via crawl | 0 pages pilier sans lien interne |

## Effort / Priorité

- Effort : M
- Priorité : **P1** — impact direct sur indexation et budget crawl

## Risques / Blocages

- Pas de crawl disponible → noter toutes les entrées comme "À VALIDER", effectuer un crawl avant la T3
- GSC Coverage non accessible → documenter le blocage, continuer avec les observables du sitemap
- robots.txt ne retire pas de l'index → toujours utiliser `noindex` si nécessaire (bonne pratique Google Search Central)

## Intégration n8n

```
n8n HTTP Request (CSV crawl import)
  → Function Node (filter utilitaires + classer actions)
  → Google Sheets (Append Rows → 02_Hygiene)
```

**Payload exemple :**

```json
{
  "url_or_pattern": "/portail-assistance/",
  "issue": "page login publique",
  "action": "Noindex",
  "impact": "H",
  "priority": "P1",
  "status": "todo"
}
```

## Prompt agent IA

```
RÔLE : Tu es un auditeur SEO technique spécialisé en hygièneseo.

OBJECTIF : Identifier les actions d'hygiène SEO (noindex, redirect, canonical) pour schoolsWP.

INPUTS :
- CSV du crawl : url, statut_http, canonical, meta_robots, inlinks, outlinks
- Liste des pages utilitaires observées dans le sitemap

ACTIONS (dans l'ordre) :
1. Repère les pages utilitaires ou archive (login, tags, feeds, older posts, auteur sans contenu)
2. Identifie les statuts HTTP problématiques (4xx, 3xx chaînées, 5xx)
3. Détecte les doublons (canonical absent ou pointant vers mauvaise URL)
4. Pour chaque URL/pattern problématique : diagnostique l'enjeu SEO (duplication, contenu faible, budget crawl)
5. Recommande une action : Keep | Noindex | Canonical (vers URL cible) | Redirect (vers URL cible)
6. Priorise par impact SEO (H/M/L)

RÈGLES DE PREUVE :
- robots.txt ne retire pas de l'index — utiliser noindex si nécessaire (bonne pratique Google)
- Toute indexabilité non vérifiable sans GSC → noter "À VALIDER via GSC Coverage"
- Ne pas supposer un doublon sans preuve de similarité du contenu

FORMAT DE SORTIE :
- CSV : url_or_pattern, issue, action, impact, effort, priority, status
- Résumé des 5 quick wins prioritaires (1 ligne chacun)

CONDITIONS D'ARRÊT :
- Toutes les pages utilitaires détectées ont une action assignée
- Les doublons identifiés ont un canonical ou redirect recommandé
```

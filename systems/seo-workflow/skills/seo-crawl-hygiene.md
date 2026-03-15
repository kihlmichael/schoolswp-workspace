# Skill : seo-crawl-hygiene

## Utilité

Analyser un export crawl pour identifier les pages à noindexer, rediriger ou corriger en vue d'optimiser le budget crawl et l'indexation.

## Tâches concernées

- T2 (Crawl & Indexation) — usage principal
- T7 (SEO Multilingue) — usage secondaire (canonical + hreflang)

## Déclenchement

Utiliser ce skill quand :

- Un CSV de crawl est disponible en input
- On cherche des pages utilitaires, doublons, ou erreurs HTTP
- On veut générer un plan d'hygiène SEO priorisé

## Processus

### Étape 1 — Classification des pages

Classer chaque URL dans l'une des catégories :

- `utilitaire` : login, portail, formulaires internes, admin
- `archive-vide` : tags sans contenu, catégories vides, older posts
- `feed` : RSS, Atom, JSON feed
- `doublon` : même contenu sur plusieurs URLs (paramètres, www/non-www, http/https)
- `erreur` : 4xx (introuvable), 5xx (erreur serveur)
- `redirect` : 3xx (vérifier les chaînes de redirections)
- `ok` : page valide à garder dans l'index

### Étape 2 — Action recommandée

Pour chaque URL classifiée comme problématique :

| Catégorie       | Action par défaut                                                   |
| --------------- | ------------------------------------------------------------------- |
| utilitaire      | Noindex (via Rank Math ou `<meta name="robots" content="noindex">`) |
| archive-vide    | Noindex ou Redirect → page catégorie parente                        |
| feed            | Noindex                                                             |
| doublon         | Canonical → URL canonique principale                                |
| erreur 4xx      | Redirect 301 → page pertinente ou supprimer                         |
| redirect chaîné | Corriger → redirect direct                                          |
| ok              | Keep                                                                |

### Étape 3 — Priorisation

- P1 : pages avec trafic ou impressions GSC (risque de perte)
- P1 : erreurs 4xx sur URLs ayant des backlinks
- P2 : archives et feeds indexés sans trafic
- P3 : doublons mineurs sans impact trafic

## Règles de preuve

- **Bonne pratique Google** : robots.txt empêche le crawl mais N'ENLÈVE PAS de l'index. Utiliser `noindex` pour retirer de l'index.
- **À VALIDER** : indexation réelle → toujours confirmer via GSC Coverage avant d'agir
- **À VALIDER** : impact trafic d'une page avant redirection → vérifier GSC Performance

## Format de sortie

CSV : `url_or_pattern, categorie, issue, action, impact, effort, priority, status`

## Limites

- Ne peut pas détecter le contenu dupliqué sémantique sans lecture du contenu
- Ne remplace pas une analyse GSC pour confirmer l'indexation réelle

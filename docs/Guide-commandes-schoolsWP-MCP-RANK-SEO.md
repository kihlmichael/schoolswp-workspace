# Guide des commandes schoolsWP MCP RANK SEO

Version : 1.0
Mode par défaut : LIGHT
Usage : Claude Code, MCP, Obsidian, documentation interne schoolsWP
Source de référence : SOP schoolsWP MCP RANK SEO

## 1. Objectif du guide

Ce guide sert à utiliser les commandes `@schoolsWP_*` de manière simple, stable et actionnable.

Il permet de savoir :

- quelle commande lancer selon le besoin SEO ;
- quelles informations fournir avant de démarrer ;
- quelles limites respecter en mode LIGHT ;
- quel livrable attendre à la fin ;
- quand demander une validation humaine ;
- comment éviter les analyses trop longues, trop coûteuses ou inutilisables.

Principe central : commencer petit, obtenir une décision claire, puis étendre seulement si le résultat mérite d'aller plus loin.

## 2. Règle principale

Toutes les commandes publiques utilisent le préfixe `@schoolsWP`.

Exemple :

```txt
@schoolsWP_carte
@schoolsWP_plan
@schoolsWP_article
```

Important : ce préfixe concerne les commandes visibles par l'utilisateur. Les noms techniques des outils MCP doivent rester ceux réellement installés dans Claude Code tant qu'ils n'ont pas été renommés côté serveur.

## 3. Modes de travail

### Mode LIGHT

C'est le mode par défaut.

Il limite volontairement les analyses pour produire des résultats utiles sans saturer la conversation ni les outils MCP.

Limites globales :

| Élément | Limite LIGHT |
|---|---:|
| Mots-clés | 50 max |
| URLs | 10 max |
| Domaines | 5 max |
| Concurrents | 3 max |
| Pages cartographiées | 20 max |
| Réponse finale | 2000 mots max |

### Mode FULL

Le mode FULL s'utilise uniquement si l'utilisateur le demande explicitement.

Réponse obligatoire avant de continuer :

```txt
Mode FULL demandé. Je peux étendre l'analyse avec pagination.
Je commence par le premier lot.
Je demande validation avant de continuer.
```

## 4. Routeur rapide

| Besoin | Commande à lancer |
|---|---|
| Créer une architecture SEO globale | `@schoolsWP_carte` |
| Construire un cocon sémantique | `@schoolsWP_cocon` |
| Trouver ou analyser les concurrents SEO | `@schoolsWP_concurrent` |
| Classer des mots-clés par intention | `@schoolsWP_intent` |
| Créer un plan éditorial SEO | `@schoolsWP_plan` |
| Analyser des contenus concurrents | `@schoolsWP_scraping` |
| Travailler le SEO local | `@schoolsWP_local` |
| Transformer des vidéos YouTube en guide | `@schoolsWP_guide` |
| Rédiger un article SEO | `@schoolsWP_article` |
| Traiter une liste en lot | `@schoolsWP_batch` |
| Auditer techniquement un site | `@schoolsWP_audit` |
| Analyser backlinks et netlinking | `@schoolsWP_backlinks` |
| Suivre positions et performance SEO | `@schoolsWP_tracking` |

## 5. Progression recommandée

Ordre conseillé pour un projet SEO complet :

1. `@schoolsWP_carte` : poser les piliers SEO.
2. `@schoolsWP_concurrent` : comprendre les concurrents.
3. `@schoolsWP_plan` : créer le plan éditorial.
4. `@schoolsWP_article` : produire les contenus.
5. `@schoolsWP_audit` : corriger les blocages techniques.
6. `@schoolsWP_tracking` : suivre les résultats.

Commandes complémentaires :

- `@schoolsWP_cocon` après la carte si tu veux une arborescence plus fine.
- `@schoolsWP_intent` si tu as déjà une liste de mots-clés.
- `@schoolsWP_scraping` avant un article stratégique.
- `@schoolsWP_backlinks` si l'autorité externe devient prioritaire.
- `@schoolsWP_local` pour une activité locale.
- `@schoolsWP_batch` pour comparer rapidement des listes.

## 6. Tableau complet des commandes

### Module 1 - Stratégie et architecture

| Commande | Paramètres obligatoires | Paramètres optionnels | Description et limites |
|---|---|---|---|
| `@schoolsWP_carte` | Niche ou secteur, pays ou marché, nombre de pages niveau 1 max 3, nombre de pages niveau 2 max 3 par pilier | Mode FULL | Génère une carte d'autorité SEO en 2 niveaux. Limites : 3 piliers, 15 mots-clés par appel, 1200 mots. |
| `@schoolsWP_cocon` | Niche ou secteur, mot-clé racine, pays, langue, profondeur max 2 niveaux | URL du site, mode FULL | Crée un cocon sémantique simple. Limites : 10 pages, 2 niveaux, 50 mots-clés, 1500 mots. |
| `@schoolsWP_concurrent` | Domaine principal, pays ou marché, langue | Liste de concurrents | Analyse les concurrents SEO. Limites : 3 concurrents, 20 mots-clés par concurrent, 1200 mots. |
| `@schoolsWP_intent` | Liste de mots-clés max 50, langue, pays ou marché | Mode FULL | Analyse les intentions de recherche. Limites : 50 mots-clés, 3 clusters, 1000 mots. |

### Module 2 - Recherche et analyse

| Commande | Paramètres obligatoires | Paramètres optionnels | Description et limites |
|---|---|---|---|
| `@schoolsWP_plan` | Pays, langue, titres ou idées de départ | Mode FULL | Crée un plan éditorial SEO. Limites : 15 articles, 3 piliers, 15 mots-clés, 1500 mots. |
| `@schoolsWP_scraping` | URLs cibles max 3, objectif d'analyse, langue, pays | URLs supplémentaires par lots | Analyse des contenus concurrents sans copie. Limites : 3 URLs, 10 mots-clés détectés, 1000 mots. |
| `@schoolsWP_local` | Ville ou région, secteur, rayon d'action | Coordonnées GPS | Produit une analyse SEO local. Limites : 5 concurrents, 15 mots-clés locaux, 1200 mots. |

### Module 3 - Création de contenu

| Commande | Paramètres obligatoires | Paramètres optionnels | Description et limites |
|---|---|---|---|
| `@schoolsWP_guide` | 1 à 3 URLs YouTube | Langue de sortie, pays SEO cible | Transforme des vidéos en guide clair. Limites : 3 vidéos, 10 mots-clés SEO, 1500 mots. |
| `@schoolsWP_article` | Langue, pays, source, mot-clé principal si connu | URL YouTube, mapping, HTML WordPress, préparation publication | Rédige un article SEO. Limites : 1000 à 1500 mots, 10 mots-clés, optimisation SEO légère. |
| `@schoolsWP_batch` | Type, liste d'éléments, pays, langue, 3 métriques max | Export CSV | Traite des URLs, domaines ou mots-clés en lot. Limites : 10 URLs, 5 domaines ou 50 mots-clés. |

### Module 4 - Audit et technique

| Commande | Paramètres obligatoires | Paramètres optionnels | Description et limites |
|---|---|---|---|
| `@schoolsWP_audit` | URL du site principal | 3 à 5 pages clés, 1 à 2 concurrents | Audit technique SEO. Limites : 5 pages analysées, 30 pages cartographiées, 2000 mots. |
| `@schoolsWP_backlinks` | Domaine principal, objectif audit, récupération ou prospection | 1 à 3 concurrents | Analyse backlinks et netlinking. Limites : 3 concurrents, 20 domaines référents, 10 prospects, 2000 mots. |

### Module 5 - Suivi et performance

| Commande | Paramètres obligatoires | Paramètres optionnels | Description et limites |
|---|---|---|---|
| `@schoolsWP_tracking` | Domaine, 20 mots-clés prioritaires max, fréquence | 1 à 3 concurrents | Suit les positions, alertes et opportunités. Limites : 20 mots-clés, 3 concurrents, 5 requêtes SERP live. |

## 7. Fiches d'usage par commande

### `@schoolsWP_carte`

À utiliser pour structurer un nouveau site, une nouvelle catégorie ou une stratégie d'autorité.

Entrée recommandée :

```txt
@schoolsWP_carte
Niche : [niche]
Pays : [pays]
Pages niveau 1 : 3
Pages niveau 2 : 3 par pilier
Mode : LIGHT
```

Sortie attendue :

- analyse rapide de la niche ;
- 3 pages piliers ;
- mots-clés principaux ;
- URLs recommandées ;
- meta descriptions ;
- validation avant les sous-pages.

Message de contrôle :

```txt
Carte Niveau 1 terminée. Valider avant de générer le niveau 2 ?
```

### `@schoolsWP_cocon`

À utiliser pour organiser un mot-clé racine en pages mères et sous-pages.

Entrée recommandée :

```txt
@schoolsWP_cocon
Niche : [niche]
Mot-clé racine : [mot-clé]
Pays : [pays]
Langue : [langue]
URL du site : [optionnel]
Profondeur : 2 niveaux
```

Sortie attendue :

- cartographie du cocon ;
- pages à conserver ;
- pages à créer ;
- pages à optimiser ;
- top 5 actions ;
- plan de maillage simple.

### `@schoolsWP_concurrent`

À utiliser pour identifier les concurrents organiques et extraire les opportunités.

Entrée recommandée :

```txt
@schoolsWP_concurrent
Domaine : [domaine]
Pays : [pays]
Langue : [langue]
Concurrents connus : [optionnel]
```

Sortie attendue :

- top 3 concurrents ;
- métriques principales ;
- top 10 opportunités mots-clés ;
- 3 quick wins ;
- validation avant concurrent suivant.

### `@schoolsWP_intent`

À utiliser pour transformer une liste de mots-clés en architecture de contenus.

Entrée recommandée :

```txt
@schoolsWP_intent
Mots-clés : [liste max 50]
Langue : [langue]
Pays : [pays]
```

Sortie attendue :

- répartition informationnelle, navigationnelle, commerciale, transactionnelle ;
- 3 clusters principaux ;
- top 10 priorités ;
- types de pages recommandés.

### `@schoolsWP_plan`

À utiliser pour créer un plan éditorial SEO exploitable.

Entrée recommandée :

```txt
@schoolsWP_plan
Pays : [pays]
Langue : [langue]
Sujets ou titres : [liste]
Mode : LIGHT
```

Sortie attendue :

- analyse SEO rapide ;
- 15 mots-clés stratégiques ;
- 3 piliers ;
- 15 articles maximum ;
- maillage conseillé ;
- top 5 opportunités.

### `@schoolsWP_scraping`

À utiliser avant un article important pour comprendre la SERP sans copier les concurrents.

Entrée recommandée :

```txt
@schoolsWP_scraping
URLs : [1 à 3 URLs]
Objectif : gap, structure ou optimisation
Pays : [pays]
Langue : [langue]
```

Sortie attendue :

- analyse de structure ;
- angles concurrents ;
- gaps exploitables ;
- bonnes pratiques ;
- plan d'amélioration.

Règle : inspiration uniquement. Jamais de copie.

### `@schoolsWP_local`

À utiliser pour une entreprise locale ou une page service + ville.

Entrée recommandée :

```txt
@schoolsWP_local
Ville : [ville]
Secteur : [activité]
Rayon : [km]
Coordonnées GPS : [optionnel]
```

Sortie attendue :

- concurrents locaux ;
- mots-clés locaux ;
- audit Google Business Profile ;
- citations prioritaires ;
- checklist 10 actions.

### `@schoolsWP_guide`

À utiliser pour transformer des vidéos YouTube en guide clair.

Entrée recommandée :

```txt
@schoolsWP_guide
URLs YouTube : [1 à 3 liens]
Langue de sortie : [langue]
Pays SEO : [optionnel]
```

Sortie attendue :

- résumé exécutif ;
- 5 concepts clés ;
- 3 thèmes majeurs ;
- 3 enseignements pratiques ;
- mots-clés SEO ;
- références utiles.

### `@schoolsWP_article`

À utiliser pour rédiger un article SEO clair et publiable après validation.

Entrée recommandée :

```txt
@schoolsWP_article
Langue : [langue]
Pays : [pays]
Source : [brief, mapping ou URL YouTube]
Mot-clé principal : [mot-clé]
Format souhaité : article, HTML WordPress ou brouillon
```

Sortie attendue :

- article 1000 à 1500 mots ;
- structure Hn propre ;
- FAQ max 5 questions ;
- 2 meta descriptions ;
- rapport SEO court ;
- checklist publication.

Règle : aucune publication WordPress sans validation explicite.

### `@schoolsWP_batch`

À utiliser pour comparer rapidement des listes.

Entrée recommandée :

```txt
@schoolsWP_batch
Type : URLs, domaines ou mots-clés
Liste : [éléments]
Pays : [pays]
Langue : [langue]
Métriques : [max 3]
```

Sortie attendue :

- tableau comparatif ;
- top 3 ;
- flop 3 ;
- 5 recommandations ;
- export CSV si demandé.

### `@schoolsWP_audit`

À utiliser pour diagnostiquer les blocages techniques d'un site.

Entrée recommandée :

```txt
@schoolsWP_audit
URL : [site]
Pages clés : [optionnel]
Concurrents : [optionnel]
```

Sortie attendue :

- score technique global ;
- top 5 problèmes critiques ;
- 3 quick wins ;
- roadmap 3 mois ;
- limites de l'analyse.

### `@schoolsWP_backlinks`

À utiliser pour comprendre l'autorité externe et préparer un plan de netlinking.

Entrée recommandée :

```txt
@schoolsWP_backlinks
Domaine : [domaine]
Objectif : audit, récupération ou prospection
Concurrents : [optionnel]
```

Sortie attendue :

- health check backlinks ;
- forces et faiblesses ;
- opportunités concurrentielles ;
- prospects prioritaires ;
- plan 90 jours.

### `@schoolsWP_tracking`

À utiliser pour suivre les positions et détecter les alertes SEO.

Entrée recommandée :

```txt
@schoolsWP_tracking
Domaine : [domaine]
Mots-clés prioritaires : [max 20]
Concurrents : [1 à 3]
Fréquence : hebdo ou mensuel
```

Sortie attendue :

- dashboard positions ;
- alertes critiques ;
- opportunités positions 11 à 20 ;
- recommandations mensuelles ;
- prochaine action.

## 8. Règles de validation humaine

Demander validation avant :

- de passer du niveau 1 au niveau 2 ;
- d'analyser un concurrent supplémentaire ;
- de traiter un nouveau lot ;
- de passer en mode FULL ;
- de préparer une publication WordPress ;
- de lancer une analyse coûteuse ou longue.

Phrase type :

```txt
Le premier lot est terminé. Je peux continuer avec le lot suivant après validation.
```

## 9. Règles de sortie schoolsWP

Pour les livrables publics liés à schoolsWP :

- écrire `schoolsWP`, jamais une autre casse ;
- utiliser le tutoiement en français ;
- parler avec une voix solo ;
- éviter le jargon inutile ;
- ne pas promettre de résultats garantis ;
- citer les sources si des données externes sont utilisées ;
- garder les slugs evergreen ;
- ne jamais ajouter de date dans une URL sauf demande explicite ;
- ajouter la disclosure affiliée si lien affilié : `Lien affilié - je recommande uniquement les outils que j'utilise au quotidien.`

## 10. Format standard d'un livrable

Chaque commande doit produire une sortie structurée comme ceci :

```txt
# Résultat [commande]

## 1. Synthèse
## 2. Données principales
## 3. Analyse
## 4. Recommandations prioritaires
## 5. Limites
## 6. Prochaine étape

## Brand QA schoolsWP
- Ton : /5
- Clarté : /5
- Valeurs : /5
- Interdits : /5
- Vocabulaire : /5
- Score global : /5
```

Score minimum attendu : 4/5.

## 11. Réponses types

### Données manquantes

```txt
Je ne lance pas encore l'analyse. Il me manque :
1. [élément]
2. [élément]
3. [élément]

Ajoute ces informations et je lance le mode LIGHT.
```

### Limite dépassée

```txt
Mode LIGHT : la limite est de [X] éléments.
Je traite les [X] premiers éléments prioritaires, puis je te proposerai de continuer avec le lot suivant.
```

### Outil indisponible

```txt
L'outil MCP requis n'est pas disponible ou ne répond pas.
Je peux produire une version sans données live, mais elle devra être vérifiée ensuite avec les données SEO.
```

### Résultat insuffisant

```txt
Les données récupérées sont insuffisantes pour conclure proprement.
Je peux reformuler la requête, élargir le lot ou passer en mode FULL après validation.
```

## 12. Prompts prêts à copier

### Démarrer une stratégie SEO complète

```txt
@schoolsWP_carte
Niche : WordPress pour indépendants et petites entreprises
Pays : France
Langue : français
Pages niveau 1 : 3
Pages niveau 2 : 3 par pilier
Mode : LIGHT
```

### Créer un plan éditorial

```txt
@schoolsWP_plan
Pays : France
Langue : français
Sujets : [liste de sujets]
Objectif : créer un plan éditorial SEO actionnable pour schoolsWP
Mode : LIGHT
```

### Préparer un article stratégique

```txt
@schoolsWP_scraping
URLs : [3 URLs concurrentes]
Objectif : identifier les gaps, la structure dominante et l'angle différenciant
Pays : France
Langue : français
Mode : LIGHT
```

Puis :

```txt
@schoolsWP_article
Langue : français
Pays : France
Source : [brief validé]
Mot-clé principal : [mot-clé]
Format souhaité : article + meta descriptions + checklist publication
Mode : LIGHT
```

### Lancer un audit technique

```txt
@schoolsWP_audit
URL : https://schoolswp.com
Pages clés : [3 à 5 URLs]
Concurrents : [optionnel]
Mode : LIGHT
```

### Mettre en place un suivi SEO

```txt
@schoolsWP_tracking
Domaine : schoolswp.com
Mots-clés prioritaires : [max 20]
Concurrents : [1 à 3 domaines]
Fréquence : mensuel
Mode : LIGHT
```

## 13. Checklist avant lancement

- [ ] La bonne commande `@schoolsWP_*` est choisie.
- [ ] Les paramètres obligatoires sont présents.
- [ ] Le mode LIGHT est appliqué par défaut.
- [ ] Les limites sont respectées.
- [ ] Les outils MCP nécessaires sont disponibles.
- [ ] La sortie attendue est claire.
- [ ] Une validation humaine est prévue si nécessaire.
- [ ] Aucune publication automatique n'est prévue sans accord explicite.

## 14. Checklist après livraison

- [ ] La synthèse est claire.
- [ ] Les données importantes sont visibles.
- [ ] Les recommandations sont priorisées.
- [ ] Les limites sont indiquées.
- [ ] La prochaine étape est explicite.
- [ ] Le ton schoolsWP est respecté.
- [ ] La Brand QA est présente si le livrable est public.

## 15. Phrase de contrôle finale

```txt
Je traite d'abord le lot prioritaire en mode LIGHT.
Ensuite, je te propose de continuer
si le résultat mérite d'être étendu.
```

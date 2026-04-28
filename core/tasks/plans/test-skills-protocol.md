# Protocole de test — Skills contenu schoolsWP

Date de création : 2026-04-16
Contexte : validation terrain des skills existants (voie A — tester l'écosystème actuel au lieu de dupliquer ClaudeClaw V2).

## Objectif

Vérifier deux choses à chaque prompt :

1. **Le bon skill se déclenche-t-il ?** (trigger accuracy)
2. **Le livrable est-il utilisable tel quel ?** (qualité output)

## Mode d'emploi

Lancer les 10 prompts **en une seule session dédiée** (pas dispersés). Pour chaque prompt, consigner dans le tableau de bilan en bas du fichier :

- ✅ skill déclenché / ❌ aucun / ⚠️ mauvais skill
- Note livrable /5
- 1 défaut à corriger (si applicable)

---

## Bloc A — Production éditoriale pure (5 prompts)

### Prompt 1 — Article SEO

Cible : `contenu/schoolswp-content-studio` (format article)

> Rédige un article schoolsWP sur "OttoKit vs SureTriggers en 2026", intention comparative, pilier automatisation.

### Prompt 2 — Newsletter

Cible : `contenu/schoolswp-content-studio` (format newsletter)

> Écris l'édition newsletter schoolsWP News de cette semaine. Anecdote : j'ai audité 20 sites WordPress de freelances, 17 n'avaient aucune sauvegarde automatique.

### Prompt 3 — Short YouTube

Cible : `social/youtube-shorts-schoolswp`

> Script Short YouTube : les 3 erreurs FluentCRM des débutants, persona freelance.

### Prompt 4 — Post LinkedIn

Cible : `social/social-content`

> Post LinkedIn à partir de cette idée : installer Yoast ne suffit pas pour le SEO WordPress. Question ouverte à la fin.

### Prompt 5 — Batch Pinterest (5 pins)

Cible : `social/pinterest-strategy`

> Produis 5 pins Pinterest depuis mon article /fluent-support-avis/ en variant les angles.

---

## Bloc B — Stratégie et conversion (3 prompts)

### Prompt 6 — Cocon sémantique

Cibles possibles (chevauchement à observer) :
- `seo/cocon-map-schoolswp`
- `seo/cluster-cocon-automatique`
- `seo/geo-architect`

> Plan de cocon sémantique complet pour OttoKit — 27 pages visées, intention mixte, pilier automatisation.

**Observation clé** : lequel des 3 skills se déclenche ? Si aléatoire → chantier de ménage à prévoir.

### Prompt 7 — Landing lead magnet

Cible : `contenu/landing-page-factory`

> Landing page schoolsWP pour un PDF d'une page "Le prompt SEO schoolsWP" — inscription FluentCRM.

### Prompt 8 — Recyclage multi-format

Test de chaînage multi-skills.

> J'ai publié l'article /fluentcrm-avis/. Transforme-le en : 1 post LinkedIn + 3 pins Pinterest + 1 Short YouTube.

**Observation clé** : les 3 skills sociaux se déclenchent-ils successivement, ou un seul couvre tout ?

---

## Bloc C — Pièges de déclenchement (2 prompts)

### Prompt 9 — Requête ambiguë

> Fais-moi un truc sur FluentCRM pour cette semaine.

**Ce qu'on observe** : le skill demande-t-il à préciser le format, ou invente-t-il ? Si aucun skill ne se déclenche, c'est un vrai signal.

### Prompt 10 — Requête qui NE doit PAS déclencher de skill contenu

> Audit technique du fichier `core/agents-py/agents/content_factory/cli.py` — cherche les appels API non protégés.

**Ce qu'on observe** : aucun skill contenu ne doit s'activer. Si `schoolswp-content-studio` se déclenche ici, la description est trop large.

---

## Tableau de bilan (à remplir pendant le test)

| # | Skill attendu | Déclenchement | Note /5 | Défaut principal à corriger |
|---|---|---|---|---|
| 1 | schoolswp-content-studio | | | |
| 2 | schoolswp-content-studio | | | |
| 3 | youtube-shorts-schoolswp | | | |
| 4 | social-content | | | |
| 5 | pinterest-strategy | | | |
| 6 | cocon-* (à observer) | | | |
| 7 | landing-page-factory | | | |
| 8 | 3 skills sociaux enchaînés | | | |
| 9 | aucun OU clarification | | | |
| 10 | aucun (skill contenu) | | | |

---

## Actions post-test

Après les 10 prompts :

1. **Identifier les "correcteurs manuels"** — skills où je corrige *toujours la même chose* (ex : rajout systématique du code affilié `schoolsWP20`, oubli récurrent du CTA Kadence, phrases trop longues). C'est la vraie dette technique.
2. **Trancher les chevauchements** — notamment les 3 skills cocon. Garder / durcir / fusionner / archiver.
3. **Corriger les descriptions YAML** — pour chaque skill qui a mal déclenché (prompts 9 et 10 notamment).
4. **Créer les skills vraiment manquants** — si un prompt révèle un trou béant (ex : lead-magnet complet 3-livrables n'est couvert par aucun existant).

## Références

- Conception ClaudeClaw V2 : 7 skills théoriques (article, newsletter, cocon, shorts, social, lead-magnet, pinterest).
- Écosystème réel : architecture modulaire par catégorie (`contenu/`, `social/`, `seo/`, etc.) — plus mature mais à valider sur usage réel.
- Priorité roadmap actuelle : lead magnet prompt SEO avant publication YouTube Shorts.

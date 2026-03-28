# Convention UTM officielle — schoolsWP

**Domaine** : schoolswp.com
**Tracking** : Google Analytics 4 (GA4)
**Gestion liens courts** : ClickWhale
**Email** : FluentCRM
**Réseaux actifs** : LinkedIn, YouTube, Instagram
**Liens affiliés** : ThemeForest, plugins WordPress
**Date de création** : 2026-03-13
**Version** : 1.0

---

## Sommaire

1. [Principes fondamentaux](#1-principes-fondamentaux)
2. [Les 5 paramètres UTM](#2-les-5-paramètres-utm)
3. [Valeurs autorisées par paramètre](#3-valeurs-autorisées-par-paramètre)
4. [Matrice source × medium](#4-matrice-source--medium)
5. [Conventions de nommage](#5-conventions-de-nommage)
6. [Exemples par canal](#6-exemples-par-canal)
7. [Liens affiliés](#7-liens-affiliés)
8. [ClickWhale — gestion des liens courts](#8-clickwhale--gestion-des-liens-courts)
9. [FluentCRM — emails et séquences](#9-fluentcrm--emails-et-séquences)
10. [Tableau de référence rapide](#10-tableau-de-référence-rapide)
11. [Règles de gouvernance](#11-règles-de-gouvernance)

---

## 1. Principes fondamentaux

### Règle absolue : cohérence avant tout

Un UTM mal nommé est pire qu'un UTM absent. GA4 traite chaque variation de casse ou d'orthographe comme une source distincte. `LinkedIn` et `linkedin` apparaissent dans deux lignes séparées dans les rapports.

**Règles de base :**

- Tout en **minuscules** sans exception
- Séparateurs : **tirets** (`-`) uniquement — jamais d'espaces, jamais d'underscores dans les valeurs
- Caractères autorisés : `a-z`, `0-9`, `-`
- Pas d'accents, pas de caractères spéciaux
- Longueur maximale recommandée : 50 caractères par paramètre

### Quand taguer

- Tous les liens publiés en dehors du site schoolswp.com
- Tous les liens dans les emails FluentCRM
- Tous les liens affiliés vers des sites tiers
- Toujours via ClickWhale pour les liens courts (Instagram, YouTube description)

### Quand ne pas taguer

- Liens internes entre pages de schoolswp.com (casse la session GA4)
- Liens vers des ressources PDF hébergées sur le site
- Liens de confirmation / transactionnels automatiques (hors campagne)

---

## 2. Les 5 paramètres UTM

| Paramètre | Balise GA4     | Obligatoire | Définition                                    |
| --------- | -------------- | ----------- | --------------------------------------------- |
| Source    | `utm_source`   | Oui         | D'où vient le trafic (la plateforme)          |
| Medium    | `utm_medium`   | Oui         | Le type de canal marketing                    |
| Campaign  | `utm_campaign` | Oui         | Le nom de la campagne ou du contexte          |
| Content   | `utm_content`  | Recommandé  | L'élément précis cliqué (format, emplacement) |
| Term      | `utm_term`     | Optionnel   | Mot-clé (SEA) ou segment d'audience (email)   |

---

## 3. Valeurs autorisées par paramètre

### `utm_source` — La plateforme d'origine

| Valeur           | Contexte d'utilisation                            |
| ---------------- | ------------------------------------------------- |
| `linkedin`       | Publications organiques LinkedIn                  |
| `linkedin-ads`   | Publicités LinkedIn Ads                           |
| `youtube`        | Descriptions de vidéos YouTube, fiches            |
| `instagram`      | Bio Instagram, stories (via lien ClickWhale)      |
| `newsletter`     | Envois newsletter FluentCRM                       |
| `email-sequence` | Séquences automatisées FluentCRM                  |
| `themefores`     | Liens affiliés ThemeForest                        |
| `plugin-affilié` | Liens affiliés vers plugins WordPress             |
| `direct`         | Réservé GA4 — ne pas utiliser manuellement        |
| `google`         | Réservé trafic organique Google — ne pas utiliser |

### `utm_medium` — Le type de canal

| Valeur     | Contexte d'utilisation                       |
| ---------- | -------------------------------------------- |
| `social`   | Post organique sur un réseau social          |
| `video`    | Lien dans ou sous une vidéo                  |
| `email`    | Tout email FluentCRM (newsletter + séquence) |
| `cpc`      | Publicité payante au clic                    |
| `affilié`  | Lien de recommandation avec commission       |
| `bio`      | Lien dans la bio d'un profil social          |
| `referral` | Partenariat, mention externe sans commission |

### `utm_campaign` — Le nom de campagne

Format : `[sujet]-[type]-[période-optionnelle]`

| Valeur exemple             | Contexte                             |
| -------------------------- | ------------------------------------ |
| `lms-wordpress-comparatif` | Article comparatif sur les LMS       |
| `learndash-avis`           | Article avis LearnDash               |
| `newsletter-mars-2026`     | Newsletter mensuelle de mars 2026    |
| `sequence-bienvenue`       | Séquence email d'onboarding          |
| `promo-black-friday-2026`  | Campagne promotionnelle Black Friday |
| `guide-fluentcrm`          | Contenu autour de FluentCRM          |
| `pilier-lms`               | Contenu du pilier thématique LMS     |
| `pilier-crm`               | Contenu du pilier thématique CRM     |

### `utm_content` — L'élément cliqué

Format : `[format]-[emplacement]` ou `[format]-[numéro]`

| Valeur exemple     | Contexte                                  |
| ------------------ | ----------------------------------------- |
| `bouton-cta-fin`   | Bouton CTA en fin d'article               |
| `lien-description` | Lien dans la description YouTube          |
| `lien-texte-intro` | Lien texte dans l'introduction d'un email |
| `image-banniere`   | Image cliquable / bannière                |
| `carte-produit`    | Carte produit dans un email               |
| `lien-bio`         | Lien unique dans la bio Instagram         |
| `post-carrousel`   | Post LinkedIn format carrousel            |
| `post-texte`       | Post LinkedIn format texte                |
| `commentaire`      | Lien posté en commentaire                 |

### `utm_term` — Segment ou mot-clé

Utilisé uniquement pour :

- SEA : le mot-clé acheté
- Email : le segment d'audience FluentCRM ciblé

| Valeur exemple           | Contexte                         |
| ------------------------ | -------------------------------- |
| `lms-wordpress`          | Mot-clé SEA                      |
| `segment-prospects-lms`  | Segment FluentCRM prospects LMS  |
| `segment-clients-actifs` | Segment FluentCRM clients actifs |
| `segment-inactifs-90j`   | Segment inactifs depuis 90 jours |

---

## 4. Matrice source × medium

Cette matrice définit les combinaisons valides. Ne pas inventer de nouvelles combinaisons sans la mettre à jour.

| Source           | Medium     | Cas d'usage                       |
| ---------------- | ---------- | --------------------------------- |
| `linkedin`       | `social`   | Post organique LinkedIn           |
| `linkedin-ads`   | `cpc`      | Publicité LinkedIn Ads            |
| `youtube`        | `video`    | Description vidéo YouTube         |
| `youtube`        | `social`   | Post communauté YouTube           |
| `instagram`      | `social`   | Story / post Instagram            |
| `instagram`      | `bio`      | Lien unique bio Instagram         |
| `newsletter`     | `email`    | Envoi newsletter FluentCRM        |
| `email-sequence` | `email`    | Séquence automatisée FluentCRM    |
| `themefores`     | `affilié`  | Lien affilié ThemeForest          |
| `plugin-affilié` | `affilié`  | Lien affilié plugin WordPress     |
| `partenaire`     | `referral` | Mention / partenariat non-affilié |

---

## 5. Conventions de nommage

### Format général

```
utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

### Règles de nommage des campagnes

**Pour le contenu éditorial :**

```
[sujet-principal]-[type-contenu]
```

Exemples : `lms-wordpress-guide`, `fluentcrm-avis`, `learndash-vs-tutorlms`

**Pour les newsletters :**

```
newsletter-[mois]-[année]
```

Exemples : `newsletter-mars-2026`, `newsletter-avril-2026`

**Pour les séquences email :**

```
sequence-[nom-sequence]
```

Exemples : `sequence-bienvenue`, `sequence-reactivation`, `sequence-lms-nurture`

**Pour les campagnes promotionnelles :**

```
promo-[evenement]-[année]
```

Exemples : `promo-black-friday-2026`, `promo-lancement-formation`

---

## 6. Exemples par canal

### LinkedIn — Post organique

**Contexte** : partage d'un article de blog sur les LMS WordPress

```
https://schoolswp.com/lms-wordpress-comparatif/?utm_source=linkedin&utm_medium=social&utm_campaign=lms-wordpress-comparatif&utm_content=post-texte
```

**Contexte** : partage d'un guide FluentCRM en format carrousel

```
https://schoolswp.com/guide-fluentcrm/?utm_source=linkedin&utm_medium=social&utm_campaign=guide-fluentcrm&utm_content=post-carrousel
```

**Contexte** : lien posté en premier commentaire (technique LinkedIn)

```
https://schoolswp.com/lms-wordpress-comparatif/?utm_source=linkedin&utm_medium=social&utm_campaign=lms-wordpress-comparatif&utm_content=commentaire
```

---

### YouTube — Description de vidéo

**Contexte** : lien vers l'article associé à la vidéo

```
https://schoolswp.com/learndash-avis/?utm_source=youtube&utm_medium=video&utm_campaign=learndash-avis&utm_content=lien-description
```

**Contexte** : lien vers une ressource mentionnée dans la vidéo (timestamps)

```
https://schoolswp.com/guide-fluentcrm/?utm_source=youtube&utm_medium=video&utm_campaign=guide-fluentcrm&utm_content=lien-description-ressource
```

**Contexte** : lien vers la page d'accueil dans la bannière de chaîne

```
https://schoolswp.com/?utm_source=youtube&utm_medium=social&utm_campaign=brand&utm_content=banniere-chaine
```

---

### Instagram — Via ClickWhale

**Contexte** : lien bio Instagram (lien court ClickWhale pointant vers une page hub ou un article)

L'URL longue taguée (configurée dans ClickWhale) :

```
https://schoolswp.com/ressources/?utm_source=instagram&utm_medium=bio&utm_campaign=bio-instagram&utm_content=lien-bio
```

Le lien court ClickWhale affiché en bio :

```
https://go.schoolswp.com/instagram
```

**Contexte** : story Instagram avec lien swipe-up (si applicable)

```
https://schoolswp.com/lms-wordpress-comparatif/?utm_source=instagram&utm_medium=social&utm_campaign=lms-wordpress-comparatif&utm_content=story-swipe
```

---

### Newsletter FluentCRM

**Contexte** : lien principal (CTA) dans la newsletter mensuelle de mars 2026

```
https://schoolswp.com/lms-wordpress-comparatif/?utm_source=newsletter&utm_medium=email&utm_campaign=newsletter-mars-2026&utm_content=bouton-cta-principal
```

**Contexte** : deuxième lien (lien texte) dans le corps de la newsletter

```
https://schoolswp.com/guide-fluentcrm/?utm_source=newsletter&utm_medium=email&utm_campaign=newsletter-mars-2026&utm_content=lien-texte-corps
```

**Contexte** : lien de signature dans tous les emails

```
https://schoolswp.com/?utm_source=newsletter&utm_medium=email&utm_campaign=signature&utm_content=lien-signature
```

---

### Séquences email FluentCRM

**Contexte** : email de bienvenue (email 1), lien vers le guide de démarrage

```
https://schoolswp.com/guide-demarrage/?utm_source=email-sequence&utm_medium=email&utm_campaign=sequence-bienvenue&utm_content=lien-texte-intro&utm_term=segment-nouveaux-inscrits
```

**Contexte** : email de nurturing LMS (email 3), bouton CTA vers l'article comparatif

```
https://schoolswp.com/lms-wordpress-comparatif/?utm_source=email-sequence&utm_medium=email&utm_campaign=sequence-lms-nurture&utm_content=bouton-cta-fin&utm_term=segment-prospects-lms
```

**Contexte** : email de réactivation (inactifs 90 jours)

```
https://schoolswp.com/nouveautes/?utm_source=email-sequence&utm_medium=email&utm_campaign=sequence-reactivation&utm_content=bouton-cta-principal&utm_term=segment-inactifs-90j
```

---

## 7. Liens affiliés

### Principe spécifique aux liens affiliés

Les liens affiliés pointent vers des **sites tiers** (ThemeForest, sites éditeurs de plugins). L'UTM est donc appliqué côté schoolsWP pour tracker l'origine du clic depuis schoolswp.com, mais le lien de destination est le lien affilié du partenaire.

**La chaîne est :** Article schoolsWP → Lien ClickWhale (tracké UTM) → Lien affilié partenaire

Passer tous les liens affiliés par ClickWhale pour :

- Centraliser le suivi des clics
- Masquer le lien affilié brut
- Pouvoir changer la destination sans modifier les articles

### ThemeForest

**Contexte** : lien affilié ThemeForest depuis un article de blog

URL configurée dans ClickWhale (destination : lien affilié ThemeForest) :

```
utm_source=themefores&utm_medium=affilié&utm_campaign=themeforest-recommandation&utm_content=bouton-cta-fin
```

Lien court ClickWhale inséré dans l'article :

```
https://go.schoolswp.com/themeforest
```

### Plugins WordPress (affiliés)

**Contexte** : lien affilié vers LearnDash depuis l'article comparatif LMS

```
utm_source=plugin-affilié&utm_medium=affilié&utm_campaign=learndash-avis&utm_content=bouton-essai-gratuit
```

**Contexte** : lien affilié vers FluentCRM depuis le guide FluentCRM

```
utm_source=plugin-affilié&utm_medium=affilié&utm_campaign=guide-fluentcrm&utm_content=bouton-cta-tarifs
```

**Contexte** : lien affilié vers TutorLMS

```
utm_source=plugin-affilié&utm_medium=affilié&utm_campaign=tutorlms-avis&utm_content=lien-texte-corps
```

---

## 8. ClickWhale — gestion des liens courts

### Pourquoi utiliser ClickWhale pour tous les liens externes

- Les URLs avec UTM sont longues et illisibles sur Instagram/YouTube
- ClickWhale permet de modifier la destination sans mettre à jour les liens publiés
- ClickWhale fournit ses propres analytics clics (complément à GA4)
- Le domaine `go.schoolswp.com` renforce la marque schoolsWP

### Convention de nommage des slugs ClickWhale

Format : `[canal]-[sujet]` ou `[usage]`

| Slug ClickWhale                      | Destination (URL taguée)                    | Usage                       |
| ------------------------------------ | ------------------------------------------- | --------------------------- |
| `go.schoolswp.com/instagram`         | Page hub / dernière ressource mise en avant | Bio Instagram               |
| `go.schoolswp.com/youtube-lms`       | Article LMS comparatif                      | Description vidéo LMS       |
| `go.schoolswp.com/youtube-fluentcrm` | Guide FluentCRM                             | Description vidéo FluentCRM |
| `go.schoolswp.com/themeforest`       | Lien affilié ThemeForest                    | Articles + emails           |
| `go.schoolswp.com/learndash`         | Lien affilié LearnDash                      | Articles + emails           |
| `go.schoolswp.com/fluentcrm-affilié` | Lien affilié FluentCRM                      | Articles + emails           |
| `go.schoolswp.com/tutorlms`          | Lien affilié TutorLMS                       | Articles + emails           |

### Workflow de création d'un lien ClickWhale

1. Construire l'URL taguée complète avec les 4 paramètres UTM
2. Coller l'URL taguée comme destination dans ClickWhale
3. Définir un slug selon la convention ci-dessus
4. Activer le tracking de clics ClickWhale
5. Utiliser le lien court `go.schoolswp.com/[slug]` dans le contenu publié

---

## 9. FluentCRM — emails et séquences

### Configuration recommandée dans FluentCRM

FluentCRM peut ajouter automatiquement des paramètres UTM à tous les liens d'un email. Configurer :

- `utm_source` : `newsletter` (pour les campagnes) ou `email-sequence` (pour les automatisations)
- `utm_medium` : `email`
- `utm_campaign` : nom de la campagne ou séquence (renseigné manuellement par envoi)

**Important** : si FluentCRM ajoute des UTM automatiquement ET que tu ajoutes des UTM manuels sur certains liens, les UTM manuels priment. Vérifier que FluentCRM n'écrase pas les UTM `utm_content` et `utm_term` configurés manuellement.

### Distinction newsletter vs séquence

| Type                                 | `utm_source`     | `utm_medium` | `utm_campaign`              |
| ------------------------------------ | ---------------- | ------------ | --------------------------- |
| Newsletter ponctuelle                | `newsletter`     | `email`      | `newsletter-[mois]-[année]` |
| Séquence automatisée                 | `email-sequence` | `email`      | `sequence-[nom]`            |
| Email transactionnel (hors campagne) | Ne pas taguer    | —            | —                           |

### Gestion des segments avec `utm_term`

Utiliser `utm_term` pour identifier le segment ciblé dans les séquences segmentées :

```
&utm_term=segment-prospects-lms
&utm_term=segment-clients-formation
&utm_term=segment-inactifs-90j
```

Cela permet dans GA4 de comparer les performances par segment FluentCRM.

---

## 10. Tableau de référence rapide

### Générateur de liens — modèle à copier

```
https://schoolswp.com/[slug-article]/?utm_source=[SOURCE]&utm_medium=[MEDIUM]&utm_campaign=[CAMPAIGN]&utm_content=[CONTENT]
```

### Référence des combinaisons les plus fréquentes

| Canal                     | Source           | Medium    | Campaign                     | Content exemple        |
| ------------------------- | ---------------- | --------- | ---------------------------- | ---------------------- |
| Post LinkedIn (texte)     | `linkedin`       | `social`  | `[sujet]-[type]`             | `post-texte`           |
| Post LinkedIn (carrousel) | `linkedin`       | `social`  | `[sujet]-[type]`             | `post-carrousel`       |
| Description YouTube       | `youtube`        | `video`   | `[sujet]-[type]`             | `lien-description`     |
| Bio Instagram             | `instagram`      | `bio`     | `bio-instagram`              | `lien-bio`             |
| Story Instagram           | `instagram`      | `social`  | `[sujet]`                    | `story-swipe`          |
| Newsletter                | `newsletter`     | `email`   | `newsletter-[mois]-[année]`  | `bouton-cta-principal` |
| Séquence bienvenue        | `email-sequence` | `email`   | `sequence-bienvenue`         | `lien-texte-intro`     |
| Affilié ThemeForest       | `themefores`     | `affilié` | `themeforest-recommandation` | `bouton-cta-fin`       |
| Affilié plugin            | `plugin-affilié` | `affilié` | `[plugin]-avis`              | `bouton-cta-fin`       |

---

## 11. Règles de gouvernance

### Qui peut créer des UTM

Michael KIHL — tout nouveau paramètre non listé dans ce document doit être ajouté ici avant utilisation.

### Mise à jour du document

Ce document est la source de vérité unique. Toute nouvelle campagne, nouveau canal ou nouveau partenaire affilié doit entraîner une mise à jour du tableau de référence correspondant.

### Validation avant publication

Checklist avant de publier un lien externe :

- [ ] L'URL est en minuscules intégral (source, medium, campaign, content)
- [ ] Aucun espace dans les paramètres (remplacé par `-`)
- [ ] La combinaison source × medium est dans la matrice validée
- [ ] Le nom de campagne suit le format défini
- [ ] Le lien a été testé (copier-coller dans le navigateur, vérifier que GA4 reçoit l'événement)
- [ ] Si lien long : passé par ClickWhale avant publication sur Instagram/YouTube

### Tester un lien UTM

1. Ouvrir GA4 → Rapports → En temps réel
2. Cliquer sur le lien depuis un autre navigateur (ou mode navigation privée)
3. Vérifier que la session apparaît avec les bons paramètres source/medium/campaign

### Revue périodique

- Revue mensuelle : vérifier que les rapports GA4 ne contiennent pas de valeurs parasites (fautes de frappe, nouvelles variantes non planifiées)
- Revue trimestrielle : nettoyer les slugs ClickWhale obsolètes, archiver les campagnes terminées

---

_Convention UTM schoolsWP — v1.0 — 2026-03-13_
_Source de vérité : ce document. Ne pas créer de variantes UTM en dehors de cette convention._

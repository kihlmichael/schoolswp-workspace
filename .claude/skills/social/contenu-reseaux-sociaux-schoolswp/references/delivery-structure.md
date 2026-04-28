# Structure de livraison — `/Reseaux/Campagne-[nom]/`

> Arborescence de dépôt des livrables Phase 2 en mode Campagne.

---

## Emplacement racine

Les campagnes se déposent à la racine du projet schoolsWP, dans un dossier `Reseaux/` :

```
D:/VS Code/CLAUDE CODE/projects/schoolswp/Reseaux/
```

> Le dossier `Reseaux/` est créé à la première exécution d'une campagne s'il n'existe pas.

---

## Arborescence obligatoire

```
/Reseaux/
  /Campagne-[nom-kebab-case]/
    ├── 00-tableau-maitre.md
    ├── 01-post-01.md
    ├── 02-post-02.md
    ├── 03-post-03.md
    ├── 04-post-04.md
    ├── 05-post-05.md
    ├── 06-post-06.md
    ├── 07-post-07.md
    ├── 08-post-08.md
    ├── 09-post-09.md
    └── 10-post-10.md
```

**Total : 11 fichiers** (1 tableau maître + 10 posts).

---

## Conventions de nommage

### Dossier campagne

- Format : `Campagne-[nom-kebab-case]`
- Kebab-case strict (pas de camelCase, pas d'espaces, pas d'accents)
- Nom descriptif et court (≤ 50 caractères après préfixe)

**Exemples valides** :
- `Campagne-remplacer-mailchimp-par-fluentcrm`
- `Campagne-guide-rank-math-2026`
- `Campagne-ottokit-automatisation`
- `Campagne-lancement-formation-lms`

**Exemples invalides** :
- `Campagne Mailchimp FluentCRM` (espaces)
- `campagne_fluentcrm` (pas de préfixe majuscule, snake_case)
- `Campagne-Remplacer-Mailchimp-Par-FluentCRM-Pour-Ton-Business-En-Ligne` (trop long)

### Fichiers posts

- Format : `NN-post-NN.md`
- Zéro-padding sur 2 chiffres (`01` à `10`)
- Pas de titre descriptif dans le nom de fichier (le titre est dans le contenu)

---

## Contenu de `00-tableau-maitre.md`

Reprend la sortie de Phase 1 :

```markdown
# Campagne — [Nom de la campagne]

**Date de création** : YYYY-MM-DD
**Angle directeur** : [1 phrase]
**Objectif final** : [trafic / lead / conversion / notoriété]
**Cible** : freelances / créateurs / formateurs / entrepreneurs
**Durée estimée de publication** : [ex : 3 semaines à 3 posts/semaine]

---

## Tableau maître

| # | Rôle post | Post Type | Format | Sujet | Angle | Hook | Promesse | Message clé | CTA | Intention | Objectif business |
|---|-----------|-----------|--------|-------|-------|------|----------|-------------|-----|-----------|-------------------|
| 01 | … | … | … | … | … | … | … | … | … | … | … |
| 02 | … | … | … | … | … | … | … | … | … | … | … |
| … | | | | | | | | | | | |
| 10 | … | … | … | … | … | … | … | … | … | … | … |

---

## Synthèse progression

- Posts 1–2 : Accroche / Découverte
- Posts 3–5 : Éducation
- Posts 6–7 : Problème / Solution
- Post 8 : Comparatif / Preuve
- Post 9 : Crédibilité / Retour d'expérience
- Post 10 : Transition / Pré-conversion

## Checklist qualité Phase 1 (validée)

- [x] 10 posts avec progression logique
- [x] Mix formats (≥ 3 différents)
- [x] Mix niveaux d'intention (≥ 3 différents)
- [x] Mix objectifs business (≥ 4 différents)
- [x] Au moins 1 post erreur OU comparatif
- [x] Au moins 1 post retour d'expérience
- [x] Au moins 1 post transition conversion douce
- [x] Hooks écrits (pas placeholders)
- [x] Zéro mot interdit
```

---

## Contenu de `NN-post-NN.md` (1 fichier par post)

Structure fixe obligatoire :

```markdown
# Post NN — [Titre interne]

---

## A. Fiche éditoriale

- **Numéro** : NN
- **Titre interne** : [titre]
- **Objectif** : [objectif business + contextualisation]
- **Angle** : [angle narratif]
- **Niveau d'intention** : [Découverte / Intérêt / Considération / Pré-conversion]
- **Format** : [carrousel / post simple / mini-checklist / mini-comparatif]
- **Hook final** : [hook finalisé]
- **CTA final** : [CTA finalisé]

---

## B. Contenu du post

### [Structure adaptée au format]

Pour carrousel :
- Slide 1 (hook) : …
- Slide 2–N : …
- Slide finale (CTA) : …

Pour post simple :
- Hook : …
- Corps : …
- CTA : …

Pour mini-checklist :
- Titre : …
- Items : …
- Outro : …

Pour mini-comparatif :
- Intro : …
- Critère 1 + verdict : …
- Critère 2 + verdict : …
- Critère N + verdict : …
- Verdict final tranché : …
- CTA : …

### Caption Instagram

[150–220 mots si carrousel, 50–120 mots si post simple]

### Hashtags

[8–12 hashtags, mix expertise / communauté / niche WordPress schoolsWP]

---

## C. Brief visuel

- **Intention visuelle** : …
- **Type de composition** : …
- **Hiérarchie de texte** : …
- **Ambiance** : …
- **Niveau de contraste** : AA minimum
- **Élément à mettre en avant** : …
- **Recommandation visuelle** : …
- **À éviter visuellement** : …

---

## D. Prompt visuel de production

```
[Prompt structuré — 7 blocs : sujet / composition / style / typographie / palette / ambiance / négatifs]
```

---

## E. Notes de production

- Outil de génération recommandé : [Nano Banana / Canva / Midjourney / DALL-E]
- Temps estimé de production visuelle : [5 min / 15 min / 30 min]
- Dépendances : [capture écran nécessaire ? photo produit ? mockup ?]
```

---

## Création de l'arborescence

Lors de la Phase 2, **avant de produire les fichiers**, l'agent doit :

1. Vérifier l'existence de `/Reseaux/` (créer si absent)
2. Créer le dossier `/Reseaux/Campagne-[nom-kebab-case]/`
3. Créer les 11 fichiers dans l'ordre

**Sur ce Windows, pas de `rm`. Jamais.** Si un dossier existe déjà (nom identique), demander confirmation à l'utilisateur avant d'écraser. Proposer un suffixe `-v2`, `-v3` au besoin.

---

## Règles de qualité de livraison

- Chaque `NN-post-NN.md` doit être **auto-portant** (lisible sans ouvrir le tableau maître)
- Chaque fichier doit respecter la **checklist qualité schoolsWP** (naming, tutoiement, preuve, CTA, phrases courtes, zéro mot interdit)
- Le `00-tableau-maitre.md` doit contenir **exactement** le tableau validé en Phase 1 + la synthèse progression
- Aucun fichier ne doit contenir de placeholder type `[à remplir]` — tout doit être écrit en dur

---

## Après livraison

Une fois les 11 fichiers livrés :

1. Propose à l'utilisateur une **synthèse exécutive** (nombre de fichiers, emplacement, prochaines étapes recommandées)
2. Mentionne les **dépendances externes** (captures à faire, visuels à générer via Nano Banana, éléments à filmer pour les Reels)
3. Suggère l'intégration avec `social-media-manager` pour la planification Blotato si multi-plateformes

**Ne pas** publier automatiquement. Ce skill produit, il ne publie pas. La publication relève de `social-media-manager` ou de l'utilisateur.

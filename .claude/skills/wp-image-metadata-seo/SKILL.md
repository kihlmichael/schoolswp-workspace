---
name: wp-image-metadata-seo
description: |
  Génère un bloc complet de métadonnées SEO pour les images schoolsWP : XPTitle, XPSubject,
  XPKeywords, XPComment, XPAuthor, Copyright, ImageDescription, Slug web, Variante Google Images,
  plus les 4 champs médiathèque WordPress (Alt text, Titre, Légende, Description).

  Utilise ce skill dès que l'utilisateur parle de :
  - optimiser une image WordPress pour Google Images ou Bing
  - générer des métadonnées image (alt text, XPTitle, XMP, EXIF)
  - remplir la médiathèque WordPress pour une image d'article
  - créer un slug image, une variante Google Images, des XPKeywords
  - "métadonnées image", "alt text schoolsWP", "optimisation image WP"
  - tout contexte schoolsWP où une image doit être référencée

  TOUJOURS déclencher ce skill pour toute demande de métadonnées image sur schoolsWP,
  même si l'utilisateur ne mentionne pas explicitement "métadonnées" ou "SEO image".
last_reviewed: 2026-04-23
review_interval_days: 90
---

## Rôle

Tu es un expert SEO WordPress spécialisé dans l'optimisation d'images pour Google Images et
Bing Images. Tu combines rigueur SEO, respect du branding schoolsWP et économie de caractères.

---

## Contexte schoolsWP

schoolsWP est un blog éducatif et comparatif WordPress (avis plugins, tutoriels, guides),
géré par Michaël KIHL. Chaque image publiée doit être optimisée pour :
- Le référencement sur Google Images & Bing Images
- L'identité visuelle schoolsWP
- Le maillage sémantique autour du mot-clé principal de l'article

Orthographe exacte obligatoire : **schoolsWP** (jamais SchoolsWP, schoolswp, Schoolswp).
Mots interdits dans tout contenu : disruptif, game changer, scalable, hack, révolutionnaire,
incroyable, en un clic, sans effort, il suffit de.

---

## Collecte de l'INPUT

Si l'un des champs suivants est absent, demande-les TOUS en une seule fois avant de générer :

| Champ | Exemple |
|-------|---------|
| **Sujet / nom du plugin** | FluentCRM, TutorLMS, Rank Math |
| **Mot-clé principal** | fluentcrm avis, tutor lms vs learndash |
| **Catégorie WordPress** | CRM, LMS, SEO, ecommerce, automatisation |
| **Usage principal** | gérer des contacts email, créer des cours en ligne |
| **Angle éditorial** | avis, comparatif, tutoriel, guide, test |
| **Année** | 2025, 2026 |

Si tous les champs sont présents dans le message de l'utilisateur, génère directement.

---

## Contraintes absolues

- N'invente AUCUNE donnée absente de l'INPUT. Si un champ est vide → indique `[À COMPLÉTER]`
- **XPTitle : strictement entre 50 et 60 caractères** — compte les caractères avant de valider
- **Alt text : strictement entre 120 et 125 caractères** — allonge ou raccourcis jusqu'à entrer dans la plage
- **Titre image : strictement entre 55 et 60 caractères** — idem
- Slug toujours en minuscules, tirets, sans accents, sans espaces
- **Règle evergreen schoolsWP : JAMAIS de date (année, mois, "2025", "2026", etc.) dans le Slug web ni dans le Nom de fichier conseillé.** La date reste autorisée partout ailleurs (XPTitle, Alt text, Titre image, Légende, Description, Variante Google Images, Copyright, ImageDescription). Un slug `/flyingpress-avis/` survit au refresh annuel du contenu, `/flyingpress-avis-2026/` non.
- **Règle hygiène URL schoolsWP : JAMAIS "schoolswp" / "schoolsWP" dans le Slug web ni dans le Nom de fichier conseillé.** Le nom de domaine `schoolswp.com` le contient déjà → doublon dans l'URL finale (`schoolswp.com/flyingpress-avis-schoolswp/` = illisible). La mention **schoolsWP doit rester** dans XPSubject, XPComment, ImageDescription, Copyright (métadonnées) et dans les champs médiathèque visibles (Légende, Description). Elle ne va JAMAIS dans un identifiant d'URL.
- XPKeywords : 8 à 12 entrées, virgule, **sans doublon même en casse différente** (ex: "FluentCRM avis" et "fluentcrm avis" = doublon interdit)
- Tout le contenu doit être en **UTF-8** — les caractères accentués (é, è, à, ç, ê…) sont obligatoires, jamais d'entités HTML ni de caractères corrompus

---

## Gabarits par angle éditorial

La **Variante Google Images** et le **Titre image** varient selon l'angle. Applique le bon gabarit :

| Angle | Variante Google Images | Titre image |
|-------|----------------------|-------------|
| **avis** | `[SUJET] [ANNÉE] – schoolsWP teste le plugin WordPress [CATÉGORIE] pour [USAGE]` | `[SUJET] [ANNÉE] : avis plugin [CATÉGORIE] – schoolsWP` |
| **comparatif** | `[SUJET] [ANNÉE] – schoolsWP compare les plugins WordPress [CATÉGORIE] pour [USAGE]` | `[SUJET] [ANNÉE] : comparatif [CATÉGORIE] sur schoolsWP` |
| **guide** | `[SUJET] [ANNÉE] – Guide schoolsWP pour utiliser le plugin WordPress [CATÉGORIE]` | `[SUJET] [ANNÉE] : guide [CATÉGORIE] WordPress – schoolsWP` |
| **tutoriel** | `[SUJET] [ANNÉE] – Tutoriel schoolsWP : configurer le plugin WordPress [CATÉGORIE]` | `[SUJET] [ANNÉE] : tutoriel [CATÉGORIE] sur schoolsWP` |
| **test** | `[SUJET] [ANNÉE] – schoolsWP met à l'épreuve le plugin WordPress [CATÉGORIE]` | `[SUJET] [ANNÉE] : test plugin [CATÉGORIE] – schoolsWP` |

---

## Bibliothèque de formules (fallback si gabarit inadapté)

Utilise ces formules quand l'angle du gabarit ne colle pas parfaitement au contexte.

**XPTitle — 5 variantes types :**
- `[SUJET] WordPress [ANNÉE] – avis complet`
- `[SUJET] [ANNÉE] – plugin WordPress à tester`
- `[SUJET] WordPress [ANNÉE] – guide pratique`
- `[SUJET] [ANNÉE] – optimisation et performance`
- `[SUJET] WordPress [ANNÉE] – test schoolsWP`

**XPSubject — 2 variantes types :**
- `Visuel d'article schoolsWP présentant [SUJET], [CATÉGORIE / USAGE].`
- `Branding schoolsWP avec titre en avant, fond travaillé et angle éditorial clair.`

**XPComment — 2 variantes types :**
- `Image de couverture optimisée SEO pour l'article "[SUJET]" sur schoolsWP.`
- `Elle soutient le référencement dans Google Images et Bing Images tout en renforçant l'identité visuelle schoolsWP.`

**ImageDescription — 2 variantes types :**
- `Visuel "[SUJET] [ANNÉE]" pour un article schoolsWP testant [USAGE principal].`
- `Illustration schoolsWP dédiée à [SUJET], plugin WordPress conçu pour [BÉNÉFICE].`

---

## Exemples de calibration (longueur)

Ces exemples montrent la longueur cible exacte. Utilise-les comme référence visuelle :

**XPTitle — 55 caractères :**
`FluentCRM avis 2025 – plugin CRM WordPress testé` → 49 car. (trop court)
`FluentCRM avis 2025 – plugin CRM email WordPress` → 49 car. (trop court)
`FluentCRM avis 2025 – le plugin CRM pour WordPress` → 51 car. ✓
`TutorLMS vs LearnDash 2025 – comparatif LMS WordPress` → 53 car. ✓
`Rank Math guide 2026 – plugin SEO WordPress complet` → 51 car. ✓

**Alt text — 122 caractères :**
`fluentcrm avis 2025 – plugin CRM WordPress pour gérer des contacts et automatiser des emails marketing, testé par schoolsWP` → 122 car. ✓

**Titre image — 57 caractères :**
`TutorLMS vs LearnDash 2025 : comparatif LMS sur schoolsWP` → 57 car. ✓

---

## Format de sortie — bloc copier-coller unique

Produis un bloc Markdown structuré, prêt à coller dans ExifTool ou la médiathèque WordPress.
Aucun commentaire autour du bloc.

> Note encodage : tout le texte est en UTF-8. Pour ExifTool, utiliser l'option `-charset utf8`.

````
---
### Métadonnées image — [SUJET] [ANNÉE]

**Nom de fichier conseillé** (sans date, sans "schoolswp")
[slug-principal].jpg

**XPTitle** (50-60 car. — vérifier le compte)
[SUJET] [ANGLE] [ANNÉE] – plugin [CATÉGORIE] WordPress [complément pour atteindre 50-60 car.]

**XPSubject**
Visuel d'article schoolsWP présentant [SUJET], plugin [CATÉGORIE] pour [USAGE].
Branding schoolsWP avec titre mis en avant.

**XPKeywords**
[SUJET] [ANGLE], plugin WordPress [CATÉGORIE], [CATÉGORIE] WordPress [USAGE],
[MOT-CLÉ PRINCIPAL], schoolsWP [CATÉGORIE], WordPress [USAGE], [SUJET] [ANNÉE],
[variation mot-clé 1], [variation mot-clé 2], [variation mot-clé 3]

**XPComment**
Image de couverture optimisée SEO pour l'article "[SUJET]" sur schoolsWP.
Améliore le référencement Google Images et renforce le branding.

**XPAuthor**
Michaël KIHL – schoolsWP

**Copyright**
© [ANNÉE] Michaël KIHL – Tous droits réservés

**ImageDescription**
Visuel "[SUJET] [ANNÉE]" pour un article schoolsWP sur [ANGLE] du plugin [CATÉGORIE] [USAGE].

**Slug web** (sans date — règle evergreen)
[sujet-en-minuscules]-plugin-wordpress-[usage-sans-accents]

**Variante Google Images**
[gabarit selon angle — voir tableau ci-dessus]

---
### Médiathèque WordPress

**Alt text** (120-125 car. — vérifier le compte)
[MOT-CLÉ PRINCIPAL] – [description factuelle : usage + contexte schoolsWP + année, jusqu'à 120-125 car.]

**Titre image** (55-60 car. — gabarit selon angle)
[gabarit selon angle — voir tableau ci-dessus]

**Légende** (1-2 phrases, mots-clés secondaires)
[Phrase 1 : ce que fait le plugin + usage principal]
[Phrase 2 : lien avec le contenu schoolsWP sur le sujet]

**Description** (3-4 phrases, contexte + branding)
[Phrase 1 : contexte de l'article et angle éditorial]
[Phrase 2 : ce que l'image illustre concrètement]
[Phrase 3 : audience cible schoolsWP pour ce contenu]
[Phrase 4 : invitation à explorer l'article]
---
````

---

## Exemple complet travaillé — FluentPlayer 2026

INPUT : Sujet = FluentPlayer, Mot-clé principal = FluentPlayer WordPress, Année = 2026,
Catégorie = plugin vidéo WordPress interactif, Usage = optimisation vidéo, Angle = test

````
---
### Métadonnées image — FluentPlayer 2026

**Nom de fichier conseillé**
fluentplayer-wordpress-video-interactive.jpg

**XPTitle** (54 car.)
FluentPlayer WordPress 2026 – test plugin vidéo schoolsWP

**XPSubject**
Visuel d'article schoolsWP présentant FluentPlayer, plugin vidéo WordPress interactif.
Branding schoolsWP avec titre mis en avant et identité visuelle cohérente.

**XPKeywords**
FluentPlayer avis, FluentPlayer WordPress, plugin vidéo WordPress, lecteur vidéo interactif,
conversion vidéo, marketing vidéo WordPress, FluentCRM, schoolsWP, vidéo e-learning, FluentPlayer 2026

**XPComment**
Image de couverture optimisée SEO pour l'article "FluentPlayer" sur schoolsWP.
Améliore le référencement Google Images et renforce le branding.

**XPAuthor**
Michaël KIHL – schoolsWP

**Copyright**
© 2026 Michaël KIHL – Tous droits réservés

**ImageDescription**
Visuel "FluentPlayer 2026" pour un article schoolsWP sur le test du plugin vidéo WordPress interactif.

**Slug web** (sans date — règle evergreen)
fluentplayer-plugin-wordpress-video-interactive

**Variante Google Images**
FluentPlayer 2026 – schoolsWP met à l'épreuve le plugin WordPress vidéo pour l'optimisation vidéo

---
### Médiathèque WordPress

**Alt text** (124 car.)
FluentPlayer WordPress – plugin vidéo interactif testé par schoolsWP pour l'optimisation vidéo, l'engagement et la conversion en 2026

**Titre image** (58 car.)
FluentPlayer 2026 : test plugin plugin vidéo – schoolsWP

**Légende**
FluentPlayer transforme une vidéo WordPress classique en contenu interactif orienté conversion.
Ce visuel schoolsWP met en avant performance, engagement et capture de leads.

**Description**
Cette image illustre un article schoolsWP consacré à FluentPlayer WordPress. Elle met en avant l'optimisation vidéo, l'interactivité et les usages marketing du plugin. Le visuel renforce le branding schoolsWP avec une présentation directe. Son rôle SEO est d'améliorer la pertinence de la page dans Google Images, Bing Images et la médiathèque WordPress.
---
````

---

## Auto-vérification silencieuse (avant d'afficher)

Compte les caractères et corrige sans le mentionner :
- [ ] XPTitle : compte exact entre 50 et 60 car. — rallonge avec un mot descriptif si < 50
- [ ] Alt text : compte exact entre 120 et 125 car. — ajuste la fin de phrase si hors plage
- [ ] Titre image : compte exact entre 55 et 60 car. — gabarit angle appliqué
- [ ] XPKeywords : 8 à 12 entrées, aucun doublon même en casse différente
- [ ] Variante Google Images : gabarit de l'angle appliqué (pas "testant" pour un comparatif)
- [ ] Slug en minuscules, tirets, sans accents, **aucune date et aucun "schoolswp" (règles evergreen + hygiène URL)**
- [ ] Nom de fichier : `[slug-descriptif].jpg` (minuscules, tirets, **pas d'année, pas de "schoolswp"** — le domaine schoolswp.com le contient déjà)
- [ ] Orthographe : **schoolsWP** partout (jamais SchoolsWP ni schoolswp)
- [ ] Aucune donnée inventée (si champ INPUT vide → `[À COMPLÉTER]`)
- [ ] Caractères accentués présents et corrects (é, è, à, ç — jamais Ã© ou clÃ©)

---

## Checklist finale avant validation (visible côté utilisateur)

Après le bloc, ajoute une mini-checklist pour que l'utilisateur valide d'un coup d'œil :

- [ ] Mot-clé principal présent dans XPTitle, Alt text, Titre image
- [ ] Texte naturel, pas de bourrage
- [ ] **schoolsWP** apparaît dans XPSubject, XPComment, ImageDescription (métadonnées visibles). **Jamais dans le Nom de fichier ni le Slug web** — le domaine schoolswp.com l'inclut déjà
- [ ] Slug et Nom de fichier **sans aucune date** (règle evergreen schoolsWP — strict)
- [ ] Alt text décrit réellement l'image, pas seulement les mots-clés
- [ ] Titre image donne envie de cliquer
- [ ] Description ajoute du contexte utile au-delà du nom du plugin

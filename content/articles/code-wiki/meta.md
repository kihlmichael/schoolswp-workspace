# Meta SEO et hero image

## Slug

```
code-wiki-google-wordpress
```

URL canonique : `https://schoolswp.com/code-wiki-google-wordpress/`

## Title (Rank Math)

**Code Wiki (Google) : auditer un plugin WordPress sans coder**

Longueur : 56 caractères. Mot-clé principal en tête, qualifié, bénéfice utilisateur.

## Meta description (Rank Math)

**Code Wiki est un service Google Labs (nov. 2025) qui transforme un dépôt GitHub en wiki interactif avec chat Gemini. Mode d'emploi pour comprendre tes plugins WordPress en 10 minutes, sans être développeur.**

Longueur : 246 caractères (cible 150-160 sur Rank Math, je laisse Michael trancher entre version courte et longue ci-dessous).

Version courte (157 car.) : **Code Wiki transforme un dépôt GitHub en wiki interactif avec chat Gemini. Comprendre tes plugins WordPress en 10 min, sans être développeur.**

## Catégorie WordPress

À créer si elle n'existe pas : **Outils WordPress** (ou rattacher à la catégorie existante la plus proche, par exemple "Tools" ou "Stack"). Décision Michael.

## Tags Rank Math

Aucun (mémoire : pas de tags WordPress sur schoolsWP).

## Internal links à compléter

L'article contient 2 placeholders `[TODO: lien interne]` à remplacer en publication :

1. **Stack WordPress recommandée** : lien vers la page stack ou un article pilier équivalent
2. **Newsletter** : lien vers la landing newsletter / lead magnet welcome

Lien interne par langue strictement (Polylang) : article FR vers articles FR uniquement.

## Hero image

### Prompt Nano Banana / Gemini 2.5 flash image

```
Hero éditorial 16:9, ratio 1920x1080.
Composition : un écran d'ordinateur portable centré, légèrement en perspective trois-quarts.
À l'écran : un wiki interactif Google avec un diagramme d'architecture stylisé (boîtes connectées par des flèches fines, blanc sur fond très sombre).
Au premier plan, sur le clavier ou à côté du portable : un petit logo WordPress en mug ou objet, discret.
Style : photographie produit éditoriale, lumière douce de studio, fond gris très clair (#F4F5F7) avec un dégradé subtil.
Accent couleur : touches discrètes de vert signature schoolsWP en illumination d'écran ou comme highlight sur le diagramme. Couleur à décrire en mots : un vert vif, lumineux, type vert pomme électrique.
Pas de texte, pas de logo Google visible, pas de logo schoolsWP visible.
Cinematic, premium, propre, espace négatif à droite pour superposition de titre éditorial si besoin.
```

### Filename

`code-wiki-google-wordpress-hero.png`

### Alt text WordPress (médiathèque)

**Écran d'ordinateur portable affichant un wiki interactif avec diagramme d'architecture, illustration de l'outil Code Wiki de Google appliqué à un projet WordPress.**

### Title médiathèque

**Code Wiki Google appliqué à un projet WordPress**

### Légende médiathèque

(vide, pas de légende affichée sous l'image)

### Description médiathèque

**Hero schoolsWP pour l'article Code Wiki Google : auditer un plugin WordPress sans coder. Service Google Labs lancé en novembre 2025.**

### Métadonnées EXIF/XMP

À générer via le pipeline `tools/wp-media-upload/` (skill `wp-image-metadata-seo`).

## Open Graph

**OG title** : Code Wiki (Google) : auditer un plugin WordPress sans coder
**OG description** : Service Google Labs gratuit qui transforme un dépôt GitHub en wiki interactif. Comprendre tes plugins WordPress en 10 min, sans être développeur.
**OG image** : variante OG 1200x630 du hero (à générer en parallèle)

## Twitter Card

**Twitter title** : Code Wiki Google pour comprendre tes plugins WordPress
**Twitter description** : J'ai testé Code Wiki, le nouveau service Google qui transforme n'importe quel dépôt GitHub en wiki interactif. Voici 4 cas d'usage concrets pour ton site WordPress.
**Twitter image** : même que OG

## Schema Rank Math

Type : **Article** (pas Review, pas How-To même si l'article contient une méthode en 5 étapes : la méthode est interne, l'article n'est pas une recette).

Author : Michaël KIHL
Publisher : schoolsWP

## CTA box (à placer en pied d'article si template Kadence dispo)

```
Découvre la stack WordPress que j'utilise au quotidien sur schoolsWP.
[Voir la stack →]
```

## Date de publication suggérée

Dès validation. Article hors calendrier édito principal, pas de dépendance amont.

## Suivi post-publication

- Suivi positions Rank Math + GSC sur "code wiki", "code wiki google", "auditer plugin wordpress"
- Suivi citations LLM (perplexity, chatgpt, claude) sur les requêtes adjacentes
- Snapshot audit dans `content/audits/code-wiki-google-wordpress/<date>/` à 30 jours et 90 jours

## Notes pour la version Gutenberg

- Convertir via le converter habituel (`md_to_gutenberg.py`)
- Vérifier que le converter retire les `---` éventuels (il n'y en a pas dans cet article)
- Le bloc `<!-- verdict-box -->` doit être restitué en bloc HTML personnalisé Kadence ou en bloc HTML brut selon ton template
- Les CTA finaux peuvent être convertis en boutons Kadence (advancedbtn + singlebtn, palette9 / palette1, gradient, flèche, shadow, hover) selon le template CTA validé

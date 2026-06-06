# Leçon 3.7 - Styling des avis, schema étoiles et page builders

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Mettre en forme ses avis avec l'onglet Style (étoiles, en-tête, carte d'avis, responsive), configurer correctement le schema des étoiles avec ses champs obligatoires et ses limites, et savoir où poser ses modèles dans Gutenberg et les autres page builders.
- **Prérequis** : Avoir au moins une plateforme connectée et un Review Template créé (leçons 3.2 à 3.6).

---

## Script narration

**[INTRO - face camera]**

On clôt le module avec la partie finition, celle qui fait qu'un bloc d'avis a l'air pro ou bâclé. Trois sujets dans cette leçon.

D'abord le styling, l'onglet Style du modèle, où tu règles les couleurs, les polices et l'allure de chaque carte d'avis. Ensuite le schema des étoiles, qu'on a survolé en 3.1 et qu'on configure maintenant concrètement, sans fausse promesse. Et enfin l'affichage avec les page builders : Gutenberg et Kadence pour notre stack, mais aussi Elementor et les autres. C'est parti.

---

**[SECTION 1 - L'onglet Style : mettre tes avis à ta marque]**

**[ECRAN - éditeur de Review Template, onglet Style à côté de General]**

Tout le styling se passe dans l'onglet Style, juste à côté de General dans l'éditeur de modèle. Là où General décide quel contenu s'affiche, Style décide à quoi il ressemble.

L'onglet est découpé en sections, chacune pour une partie de ton bloc d'avis. Je te montre les plus utiles.

**[ECRAN - section Star Rating : Filled Star Color et Empty Star Color]**

La section Star Rating règle les étoiles : la couleur des étoiles pleines et celle des étoiles vides. C'est ici que tu peux passer du jaune par défaut à une couleur cohérente avec ta marque.

**[ECRAN - section Header : titre, note moyenne, bouton Write a Review]**

La section Header met en forme le grand encadré du haut : couleur et typographie du titre, du gros chiffre de la note moyenne, du bouton Write a Review, et même des barres de progression qui montrent la répartition des notes.

**[ECRAN - section Review Box : Background Color, Padding, Border]**

Et la section la plus importante pour l'allure générale : Review Box, la carte qui contient chaque avis. Tu y règles la couleur de fond, le padding, c'est-à-dire l'espace intérieur entre le bord et le texte, et la bordure : style, épaisseur, couleur. C'est ce qui donne une grille propre et aérée.

**[ECRAN - icônes responsive Desktop / Tablet / Mobile en haut du panneau]**

Dernier réflexe, en haut du panneau : les icônes Desktop, Tablet et Mobile. Tu peux ajuster ton style par appareil. Par exemple réduire la taille de police sur mobile. Pense à cliquer sur Save Template quand tu as fini.

---

**[SECTION 2 - Le schema des étoiles, en pratique]**

**[ECRAN - éditeur General → section Schema.org Markup → Enable]**

Passons au schema, le code invisible qui aide Google à comprendre que ta page contient des avis. On le configure dans l'onglet General du modèle, section Schema.org Markup. Tu actives Enable Schema.org Markup, à laisser presque toujours sur On.

**[ECRAN - champs Business Name, Business Type, Business Logo, Phone]**

Tu remplis ensuite les champs qui rattachent les avis à ton entreprise : le nom, le type d'entreprise, le logo et le numéro de téléphone. Pour le type, attention, tu dois le choisir exactement dans la liste de schema point org, par exemple LocalBusiness ou Restaurant. Pour la note, tu peux indiquer une note moyenne et un nombre d'avis de secours, le Fallback, utile si la donnée en direct n'est pas disponible.

**[ECRAN - slide "3 conditions du schema" rappel de la 3.1]**

Maintenant, les conditions à respecter, on les avait annoncées en 3.1. Un : le schema ne fonctionne pas si tu affiches uniquement les avis. Il faut au minimum un en-tête, avec logo, nom et nombre d'avis. Pense donc à activer l'en-tête dans ta section Header. Deux : Google n'indexe pas le schema sur la page d'accueil, choisis une autre page, et une seule, pour éviter le schema dupliqué. Trois : teste avant de publier.

**[FACE CAMERA]**

Et je redis la nuance, parce qu'elle est essentielle : même avec un schema parfait, Google ne garantit jamais l'affichage des étoiles dans ses résultats. C'est sa décision. Le schema met les chances de ton côté, point. Pour vérifier que ton balisage est valide, colle l'adresse de ta page dans le Rich Results Test de Google. Valide ne veut pas dire affiché, mais c'est la première étape.

---

**[SECTION 3 - Afficher partout : shortcode et page builders]**

**[ECRAN - liste des templates, colonne ShortCode]**

On passe à l'affichage. Le mécanisme universel, tu le connais depuis Google : le shortcode. Chaque modèle a le sien, dans la colonne ShortCode de la liste des templates, du type wp_social_ninja id égale cent, plateforme reviews. Tu cliques pour le copier.

**[ECRAN - éditeur Gutenberg, bloc Shortcode, collage]**

Pour notre stack schoolsWP, Gutenberg et Kadence : tu ajoutes un bloc Shortcode dans l'éditeur, tu colles ton code, et tu publies. Ton bloc d'avis stylé apparaît. Tu peux le poser dans une page, un article, ou une zone de widget. Et comme tu construis avec des blocs Kadence, tu places ce bloc Shortcode où tu veux dans ta mise en page : dans une colonne, sous un titre, dans une section dédiée témoignages.

**[ECRAN - slide "Page builders : Gutenberg/Kadence, Elementor, Beaver, Oxygen"]**

Le shortcode marche dans tous les page builders. Si tu utilises Elementor, Beaver Builder ou Oxygen, le principe reste le même : un emplacement où coller le shortcode. WP Social Ninja propose en plus des intégrations dédiées pour certains de ces builders, qu'on verra dans le Module 6. Mais retiens l'essentiel : un modèle, un shortcode, n'importe où.

---

**[SECTION 4 - Un dernier réflexe : le modèle multi-plateformes]**

**[ECRAN - éditeur General → Platforms, plusieurs cases cochées : Google, Facebook, Yelp]**

Avant de conclure, un usage qui résume tout le module. Dans un seul modèle, onglet General puis Platforms, tu peux cocher plusieurs sources en même temps : Google, Facebook, Yelp, ta source custom. Tu obtiens un mur d'avis unifié, alimenté par toutes tes plateformes.

Combine ça avec deux filtres vus en chemin : la note minimale, pour ne montrer que tes meilleurs avis, et le filtre Hide Reviews Without Text, pour écarter les notes sans commentaire. Tu actives l'icône de plateforme sur chaque carte, et ton visiteur voit d'un coup d'œil que tes bons avis viennent de partout. C'est l'aboutissement de tout ce qu'on a connecté dans ce module.

---

**[OUTRO - face camera]**

Tu sais maintenant styliser tes avis à ta marque, configurer le schema des étoiles avec ses conditions et ses limites honnêtes, et afficher tes modèles dans Gutenberg, Kadence et tous les page builders. C'est la fin du Module 3 sur les Business Reviews. Dans le module suivant, on change complètement de registre avec le Social Chat : WhatsApp, Messenger et les autres canaux pour discuter avec tes visiteurs. On se retrouve dans le Module 4.

---

## Notes de production

### Captures d'écran suggérées

- Onglet Style à côté de General dans l'éditeur de Review Template (section 1)
- Section Star Rating : Filled Star Color / Empty Star Color (section 1)
- Section Header : titre, note moyenne, bouton Write a Review, barres de progression (section 1)
- Section Review Box : Background Color, Padding, Border (section 1)
- Icônes responsive Desktop / Tablet / Mobile (section 1)
- General → Schema.org Markup : Enable + champs Business Name/Type/Logo/Phone (section 2)
- Slide "3 conditions du schema" : en-tête obligatoire, pas sur la home, tester avant (section 2)
- Rich Results Test de Google avec une URL collée (section 2)
- Colonne ShortCode + bloc Shortcode dans Gutenberg/Kadence (section 3)
- Slide "Page builders" : Gutenberg/Kadence, Elementor, Beaver, Oxygen (section 3)
- General → Platforms avec plusieurs cases cochées (Google, Facebook, Yelp) (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast onglet Style, avant/après sur la couleur d'étoiles et le padding
- Section 2 : screencast schema, ralentir sur Business Type (liste schema.org)
- Section 2 fin : face camera ferme sur "valide ne veut pas dire affiché" - franchise, pas de survente
- Section 3 : screencast Gutenberg/Kadence + slide page builders
- Section 4 : screencast modèle multi-plateformes, montrer le mur d'avis final stylé
- Outro : face camera, CTA visuel vers le Module 4 (Social Chat)

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Onglet Style | 2:15 |
| Section 2 - Schema en pratique | 2:30 |
| Section 3 - Shortcode et page builders | 1:45 |
| Section 4 - Modèle multi-plateformes | 0:40 |
| Outro | 0:15 |
| **Total** | **~8:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__template-style-connection.md`
- Doc : `sources/docs/guide__customization-design__website-styling-for-feeds-and-reviews.md`
- Doc : `sources/docs/guide__business-reviews__configure-schema.md`
- Doc : `sources/docs/guide__business-reviews__create-template.md`
- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Vidéos officielles : #45 (Style All Your Reviews from One Place), #57 (Use Page Builders to Style Your Reviews)

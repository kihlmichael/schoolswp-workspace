# Leçon 2.8 - Plusieurs feeds sur une page et styling avancé

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Combiner plusieurs feeds de plateformes différentes sur une même page via leurs shortcodes, organiser la mise en page avec Kadence, et appliquer un styling cohérent et responsive à tous ses feeds.
- **Prérequis** : Module 2 leçons 2.1 à 2.7 terminées (au moins deux feeds créés).

---

## Script narration

**[INTRO - face camera]**

On clôt le module sur la question qui revient une fois qu'on maîtrise chaque feed pris séparément : comment les faire cohabiter sur une seule page ? Une section YouTube, une section Instagram, un mur X, le tout sur la même page, et qui reste cohérent visuellement.

Dans cette leçon, on voit comment poser plusieurs feeds via leurs shortcodes, comment les organiser proprement avec Kadence, et comment pousser le styling pour garder une vraie cohérence de marque, y compris sur mobile. C'est parti.

---

**[SECTION 1 - Le principe : un shortcode par template]**

**[ECRAN - WP Social Ninja → Templates, plusieurs templates listés avec leurs shortcodes]**

Reprenons la mécanique de la leçon 2.1. Chaque template, quelle que soit sa plateforme, a son propre shortcode unique. C'est la clé de cette leçon.

Pour afficher plusieurs feeds sur une page, tu n'as donc rien de nouveau à apprendre. Tu poses simplement plusieurs shortcodes sur la même page. Un shortcode YouTube, un shortcode Instagram, un shortcode X : chacun affiche son feed, indépendamment des autres.

Va dans WP Social Ninja, Templates. Tu y vois la liste de tous tes templates, toutes plateformes confondues, avec leur shortcode dans la colonne dédiée. Chaque shortcode porte sa plateforme, par exemple platform égale youtube, ou platform égale instagram. Tu cliques pour copier celui dont tu as besoin.

---

**[SECTION 2 - Poser plusieurs feeds avec Kadence]**

**[ECRAN - éditeur Gutenberg, plusieurs blocs Shortcode empilés]**

Passons à la pratique dans une page. La méthode la plus simple : tu ajoutes un bloc Shortcode pour chaque feed, et tu colles le shortcode correspondant. Trois feeds, trois blocs Shortcode, dans l'ordre que tu veux.

Mais pour un rendu pro, on structure avec Kadence. Tu ajoutes un bloc Section ou Row Layout de Kadence pour chaque feed, avec un titre au-dessus, par exemple "Mes dernières vidéos", "Sur Instagram", "Sur X". À l'intérieur de chaque section, tu places ton bloc Shortcode.

L'avantage de Kadence : tu maîtrises la largeur, les marges, les couleurs de fond de chaque section, et tu peux alterner les fonds pour séparer visuellement les feeds. Tu obtiens une page "réseaux sociaux" propre, lisible, et qui respire.

**[ECRAN - aperçu de la page avec trois sections distinctes]**

Petit conseil de cadence : ne mets pas trop de feeds sur une même page. Deux ou trois bien choisis valent mieux qu'un empilement de cinq. Chaque feed charge ses propres données, et trop de feeds alourdissent la page. On reparlera de performance juste après.

---

**[SECTION 3 - Garder la cohérence visuelle]**

**[ECRAN - onglet Style d'un template, sections récurrentes]**

Le piège, quand on pose plusieurs feeds côte à côte, c'est l'incohérence. Un feed avec des cartes grises bordées, à côté d'un feed sans bordure et fond blanc : ça jure. La solution se trouve dans l'onglet Style de chaque template.

Bonne nouvelle, les feeds partagent la même logique de styling. Tu retrouves partout, à quelques noms près, les mêmes sections : le Header en haut du feed, le Content ou texte des posts, et surtout l'Item Box, la carte qui contient chaque élément.

L'Item Box, c'est ton levier principal pour la cohérence. Sur chaque feed, règle le même fond de carte, la même bordure et la même épaisseur, les mêmes marges internes. Si tes cartes YouTube, Instagram et X ont le même habillage, la page paraît unifiée même si le contenu vient de plateformes différentes.

Applique aussi tes couleurs de marque de façon identique : la même couleur d'accent pour les boutons Follow et Subscribe, la même police si tu personnalises la typographie. C'est ce travail de cohérence qui fait la différence entre une page bricolée et une vitrine soignée.

---

**[SECTION 4 - Le styling responsive]**

**[ECRAN - onglet Style, icônes Desktop / Tablet / Mobile en haut du panneau]**

Un feed qui rend bien sur grand écran peut se casser sur mobile. WP Social Ninja gère ça avec le styling responsive.

En haut du panneau de style, tu as trois icônes d'appareil : Desktop, Tablet, Mobile. Tu cliques sur l'une d'elles, et tout réglage que tu fais ensuite ne s'applique qu'à cette vue. Par exemple, tu sélectionnes Mobile, tu réduis la taille de police, et ça ne touche que l'affichage mobile.

Combine ça avec le réglage du nombre de colonnes, vu pour chaque plateforme : trois colonnes sur bureau, deux sur tablette, une sur mobile. C'est le réglage qui sauve le plus de mises en page. Un feed à quatre colonnes serré sur un téléphone est illisible, alors qu'une seule colonne respire.

Et ce styling responsive existe aussi pour les templates d'avis, qu'on verra au Module 3. Le principe sera identique.

---

**[SECTION 5 - Performance : ne pas oublier le cache]**

**[ECRAN - Settings → Feed Platforms, réglages Check New Feeds Every par plateforme]**

Plusieurs feeds sur une page, ça veut dire plusieurs sources de données à charger. La performance devient un sujet réel.

Deux leviers, déjà croisés dans le module. D'abord, le cache. Pour chaque plateforme, dans Settings, Feed Platforms, le réglage Check New Feeds Every fixe la fréquence de récupération. Un intervalle plus long, par exemple une fois par jour plutôt que toutes les six heures, allège nettement le chargement. Pour des réseaux sociaux, une mise à jour quotidienne suffit largement.

Ensuite, l'optimisation des images, le réglage Optimize Image présent sur chaque plateforme. Il stocke les images en local et accélère le chargement. Souviens-toi du compromis vu pour Instagram et Facebook : avec l'optimisation, les vidéos ne se lisent plus directement dans le feed, et pour un carrousel, seule la première image s'affiche. À toi d'arbitrer selon ce que tu privilégies.

**[FACE CAMERA]**

La règle de bon sens : sur une page multi-feeds, allonge le cache et limite-toi à deux ou trois feeds. Ta page restera rapide, et tes visiteurs aussi.

---

**[SECTION 6 - Bilan du module]**

**[ECRAN - slide récap des cinq feeds + la grille Source / Template / Shortcode]**

Faisons le bilan de ce Module 2. Tu as découvert les cinq feeds : YouTube, Facebook, Instagram, X et TikTok. Et surtout, tu as compris qu'ils partagent tous la même grille : Source, Template, Shortcode.

Tu sais connecter chaque plateforme avec sa méthode propre, choisir le bon type de feed, curer ton contenu avec les filtres, styliser chaque template, et maintenant en combiner plusieurs sur une seule page de façon cohérente et performante.

**[FACE CAMERA]**

Tu as maintenant tout le socle des social feeds. Dans le Module 7, le cas pratique, on réutilisera précisément ce que tu viens d'apprendre pour construire une vraie page Vidéos sur un site schoolsWP, avec plusieurs feeds YouTube triés par thème. Tout ce module y converge.

---

**[OUTRO - face camera]**

Tu sais désormais faire vivre plusieurs feeds sur une même page, les styliser avec cohérence, et garder ta page rapide. C'est la fin du Module 2 sur les social feeds. Dans le Module 3, on change de registre avec les Business Reviews : afficher des avis clients, gérer le schema, et bâtir de la preuve sociale qui inspire confiance. On se retrouve au module suivant.

---

## Notes de production

### Captures d'écran suggérées

- Page Templates avec plusieurs templates de plateformes différentes et leurs shortcodes (section 1)
- Éditeur Gutenberg : plusieurs blocs Shortcode dans des sections Kadence distinctes (section 2)
- Aperçu front d'une page avec trois sections de feeds bien séparées (section 2)
- Onglet Style : section Item Box mise en évidence sur deux templates côte à côte pour montrer la cohérence (section 3)
- Icônes Desktop / Tablet / Mobile en haut du panneau de style (section 4)
- Réglages Check New Feeds Every et Optimize Image par plateforme (section 5)
- Slide récap final : cinq feeds + grille Source / Template / Shortcode, vert schoolsWP (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 et 2 : screencast Templates puis éditeur Gutenberg / Kadence
- Section 3 : split-screen de deux feeds pour illustrer cohérence vs incohérence
- Section 5 : retour face camera sur la règle de bon sens performance
- Section 6 : slide bilan + teaser Module 7
- Outro : face camera, CTA visuel vers le Module 3

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Un shortcode par template | 1:00 |
| Section 2 - Poser plusieurs feeds avec Kadence | 1:30 |
| Section 3 - Cohérence visuelle | 1:30 |
| Section 4 - Styling responsive | 1:15 |
| Section 5 - Performance et cache | 1:15 |
| Section 6 - Bilan du module | 0:45 |
| Outro | 0:15 |
| **Total** | **~8:00** |

### Sources

- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Doc : `sources/docs/guide__customization-design__website-styling-for-feeds-and-reviews.md`
- Doc : `sources/docs/guide__social-feeds__style-connection-settings.md`
- Doc (cache et optimisation, par plateforme) : `sources/docs/guide__social-feeds__youtube-settings.md`, `guide__social-feeds__instagram-feed-settings.md`
- Vidéo officielle : #82 (Embed Multiple Social Feeds for FREE)

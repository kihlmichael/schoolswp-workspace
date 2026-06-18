# Leçon 2.1 - Comprendre un feed : source, template, shortcode

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Comprendre la mécanique commune à tous les feeds sociaux de WP Social Ninja (source, template, shortcode) pour aborder chaque plateforme avec la même méthode, et savoir afficher un feed n'importe où sur son site.
- **Prérequis** : Module 1 terminé (plugin installé, interface connue).

---

## Script narration

**[INTRO - face camera]**

Avant d'attaquer YouTube, Facebook, Instagram et les autres une par une, on prend cinq minutes pour comprendre une chose : tous les feeds de WP Social Ninja fonctionnent sur le même principe. Une fois que tu as ce principe en tête, chaque plateforme devient une simple variation du même schéma.

Dans cette leçon, on voit les trois pièces qui composent n'importe quel feed : la source, le template, et le shortcode. C'est la grille de lecture que tu vas réutiliser pour toutes les leçons du module. C'est parti.

---

**[SECTION 1 - Les cinq feeds disponibles]**

**[ECRAN - WP Social Ninja → Platforms → onglet Social Feeds]**

Commençons par situer le terrain. WP Social Ninja propose aujourd'hui cinq feeds sociaux : YouTube, Facebook, Instagram, X (anciennement Twitter), et TikTok.

Un feed, c'est tout simplement un affichage automatique de ton contenu social directement sur ton site WordPress. Tu publies une vidéo sur YouTube, un post sur Instagram, et il apparaît sur ta page sans que tu aies à le recopier. Le feed se met à jour tout seul.

L'intérêt est double : tu montres ton activité sociale à tes visiteurs, et tu gardes ton site vivant sans le maintenir à la main. Maintenant, voyons comment ça marche concrètement.

---

**[SECTION 2 - Pièce 1 : la source (la connexion)]**

**[ECRAN - popup de connexion d'une plateforme, bouton Connect]**

Première pièce : la source. C'est la connexion entre ton compte social et le plugin.

Chaque plateforme a sa propre méthode de connexion. YouTube demande une clé API ou un accès Google. Facebook et Instagram passent par une autorisation Meta. X demande un Bearer Token créé dans le portail développeur. TikTok demande un code d'accès et un plugin compagnon. On verra chacune en détail dans les leçons suivantes.

Le point à retenir : la source répond à la question "d'où vient le contenu ?". Sans connexion valide, le feed reste vide. C'est toujours la première étape, et c'est souvent là que se cachent les blocages quand un feed ne s'affiche pas.

---

**[SECTION 3 - Pièce 2 : le template (quoi afficher et comment)]**

**[ECRAN - éditeur de template, onglets General / Style / Connection]**

Deuxième pièce : le template. Une fois ta source connectée, tu cliques sur Add New Template, et tu arrives dans l'éditeur. C'est ici que tu décides quoi afficher, et à quoi ça ressemble.

L'éditeur est presque toujours organisé en trois onglets. Retiens-les bien, parce que tu les retrouveras sur chaque plateforme.

Onglet General : il contrôle le contenu et le fonctionnement. C'est là que tu choisis le type de feed, le nombre d'éléments, l'ordre, les filtres, et la disposition.

Onglet Style : il contrôle l'apparence. Couleurs, polices, espacements, bordures, pour coller à ta marque.

Onglet Connection : il gère le lien API de ce template. Tu t'en sers surtout pour reconnecter un compte ou en ajouter un nouveau.

**[ECRAN - dropdown Layout Type : Grid, Carousel, Masonry, Timeline]**

Et dans cet onglet General, deux réglages reviennent partout. Le Feed Type, qui dit quel contenu remonter, par exemple les vidéos d'une chaîne ou les posts d'une page. Et le Layout Type, la disposition visuelle. Tu retrouveras quasiment toujours la grille, le carrousel, et selon la plateforme, le mode masonry de type Pinterest ou la timeline en une colonne.

Un template, c'est donc une configuration sauvegardée. Tu peux en créer plusieurs pour une même plateforme, par exemple une grille de tes dernières vidéos pour ta page d'accueil, et un carrousel pour ta barre latérale.

---

**[SECTION 4 - Pièce 3 : le shortcode (l'affichage)]**

**[ECRAN - WP Social Ninja → Templates, colonne ShortCode]**

Troisième pièce : le shortcode. C'est lui qui pose ton feed sur une page.

Chaque fois que tu crées un template, WP Social Ninja lui attribue automatiquement un shortcode unique. Tu le retrouves dans WP Social Ninja, puis Templates : c'est une page qui liste tous tes templates avec leur shortcode dans une colonne dédiée.

Le shortcode ressemble à ça : entre crochets, wp_social_ninja, un identifiant, et la plateforme. Par exemple : id égale 100, platform égale youtube. Tu cliques dessus dans la liste, et il se copie tout seul dans ton presse-papiers.

**[ECRAN - éditeur Gutenberg, ajout d'un bloc Shortcode]**

Ensuite, tu ouvres la page où tu veux l'afficher. Tu ajoutes un bloc Shortcode, tu colles ton code, et tu publies. Quand un visiteur charge la page, WordPress remplace cette ligne par ton feed entièrement stylé.

**[FACE CAMERA]**

Petit réflexe utile : sur cette page Templates, en survolant un template, tu as les options Edit, Duplicate et Delete. Duplicate est précieux, il te permet de créer une variante sans repartir de zéro. On s'en servira dans le Module 7 pour la page Vidéos.

---

**[SECTION 5 - La grille de lecture à garder en tête]**

**[ECRAN - slide "Source → Template → Shortcode"]**

Résumons avec la grille que tu vas réutiliser tout le module.

Source : je connecte mon compte. Template : je configure quoi afficher dans l'onglet General, et l'apparence dans l'onglet Style. Shortcode : je copie le code et je le pose sur ma page.

Trois pièces, toujours dans cet ordre. Les leçons suivantes ne font que détailler la pièce Source, qui change d'une plateforme à l'autre, et les options spécifiques de chaque template. Mais le squelette, lui, ne bouge pas.

---

**[OUTRO - face camera]**

Tu as maintenant la mécanique commune à tous les feeds : source, template, shortcode. C'est ta boussole pour tout le module. Dans la prochaine leçon, on applique ça à YouTube : on connecte une chaîne par clé API ou par OAuth, et on découvre les cinq types de feed. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Onglet Social Feeds dans Platforms, les cinq plateformes visibles (section 1)
- Popup de connexion générique d'une plateforme avec le bouton Connect (section 2)
- Éditeur de template avec les trois onglets General / Style / Connection bien visibles (section 3)
- Dropdown Feed Type et dropdown Layout Type côte à côte (section 3)
- Page Templates avec la colonne ShortCode et un shortcode mis en évidence (section 4)
- Bloc Shortcode dans l'éditeur Gutenberg avec le code collé (section 4)
- Slide récap "Source → Template → Shortcode" en trois blocs, vert schoolsWP (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 4 : alternance screencast (interface réelle) et slides Kadence
- Section 3 : insister visuellement sur les trois onglets, c'est le repère qui revient partout
- Section 4 : zoom sur le clic-pour-copier le shortcode et le teaser Duplicate
- Outro : face camera, CTA visuel vers la leçon 2.2

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Les cinq feeds | 1:00 |
| Section 2 - La source | 1:15 |
| Section 3 - Le template | 1:45 |
| Section 4 - Le shortcode | 1:45 |
| Section 5 - La grille de lecture | 0:30 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds.md`
- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Doc (repères onglets et Layout) : `sources/docs/guide__social-feeds__youtube-feed-template-general-settings.md`

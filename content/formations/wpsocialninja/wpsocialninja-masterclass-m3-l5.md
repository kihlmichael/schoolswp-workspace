# Leçon 3.5 - E-commerce : AliExpress, WooCommerce, FluentCart

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter les trois plateformes e-commerce : AliExpress par simple URL produit (utile en dropshipping), WooCommerce en sélectionnant ses produits et en faisant de WP Social Ninja le hub d'avis, et FluentCart par produit avec le drawer interactif.
- **Prérequis** : Leçon 3.2 vue. Pour WooCommerce, le plugin WooCommerce installé avec au moins un produit doté d'un avis. Pour FluentCart, FluentCart installé.

---

## Script narration

**[INTRO - face camera]**

Si tu vends en ligne, cette leçon est pour toi. Les avis sur une page produit, c'est souvent ce qui fait basculer un visiteur hésitant vers l'achat. On va voir trois sources e-commerce, chacune avec son usage.

AliExpress, parfait pour le dropshipping et l'affiliation : tu récupères les avis d'un produit existant. WooCommerce, pour ta propre boutique : tu reprends la main sur tes avis produits. Et FluentCart, l'e-commerce de l'écosystème Fluent, avec une intégration soignée. On commence par AliExpress.

---

**[SECTION 1 - AliExpress : juste une URL produit]**

**[ECRAN - WP Social Ninja → Platforms → ligne AliExpress → icône Settings]**

AliExpress est l'une des connexions les plus simples. Pas de clé API, pas de compte développeur. Une seule chose : le lien d'une page produit.

Le cas d'usage est clair. Tu as une boutique en dropshipping ou en affiliation, une belle fiche produit, mais aucun avis sur ton site, ce qui fait hésiter les acheteurs. Avec cette fonction, tu vas chercher les avis du produit d'origine sur AliExpress et tu les affiches chez toi.

Tu cliques sur l'icône Settings de la ligne AliExpress. Une fenêtre s'ouvre avec deux champs : un pour l'identifiant produit, un pour le nom du produit.

**[ECRAN - aliexpress.com, page produit, URL dans la barre d'adresse]**

Tu vas sur AliExpress, tu ouvres la page du produit qui t'intéresse, et tu copies son URL complète, du type aliexpress point com slash item slash un long numéro point html. Tu notes aussi le nom du produit.

**[ECRAN - retour WordPress, collage nom + URL, bouton Save]**

Tu reviens dans le plugin, tu colles le nom dans le champ Product Name et l'URL complète dans le champ Product ID, puis Save. La ligne AliExpress passe au vert avec le produit listé. Le plugin peut maintenant récupérer les avis de cette page, y compris les notes et les photos clients.

---

**[SECTION 2 - WooCommerce : reprendre la main sur tes avis]**

**[ECRAN - WP Social Ninja → Platforms → module WooCommerce activé → Settings]**

Passons à WooCommerce, pour ta propre boutique. Petit prérequis : avoir WooCommerce installé, avec au moins un produit qui a déjà un avis.

Dans Platforms, tu actives le module WooCommerce et tu cliques sur l'icône Settings. Une fenêtre te laisse sélectionner les produits dont tu veux afficher les avis. Le bouton Add More Product permet d'en ajouter plusieurs. Tu choisis tes produits dans le menu déroulant, puis Save.

**[ECRAN - WP Social Ninja → Settings → Reviews Platform → WooCommerce Settings]**

Là où WooCommerce devient intéressant, c'est dans les réglages globaux : WP Social Ninja, puis Settings, Reviews Platform, WooCommerce Settings. Ces réglages s'appliquent aux produits reliés à un modèle d'avis WooCommerce.

Deux options clés. La synchronisation auto, qui va chercher les nouveaux avis à une fréquence que tu choisis, par exemple chaque jour, avec un bouton de synchro manuelle si tu ne veux pas attendre. Et surtout l'option Make WP Social Ninja Your Main Review Hub : quand tu l'actives, le plugin prend le contrôle de l'affichage des avis et remplace le style standard de WooCommerce par ton modèle.

**[ECRAN - options Display Location + comportement au clic sur les étoiles]**

Tu règles aussi où les avis s'affichent, dans l'onglet Reviews de WooCommerce ou en dehors, et le comportement au clic sur les étoiles : défilement vers la zone d'avis, ou ouverture d'un panneau coulissant, le drawer, en style Modern ou Default. N'oublie pas de cliquer sur Save Settings.

**[ECRAN - fiche produit WooCommerce → Product Data → WP Social Ninja]**

Et pour un réglage produit par produit, tu peux aller dans la fiche d'un produit, section Product Data, onglet WP Social Ninja, pour choisir un modèle spécifique à cet article.

---

**[SECTION 3 - FluentCart : l'intégration de l'écosystème Fluent]**

**[ECRAN - WP Social Ninja → Platforms → FluentCart → icône Settings]**

Troisième source : FluentCart, la solution e-commerce de l'écosystème Fluent. Ici, WP Social Ninja se positionne comme le hub d'avis principal, en remplaçant le système d'avis standard par une expérience plus riche : modération détaillée, style personnalisé et panneau d'avis interactif.

Tu vas dans Platforms, tu trouves FluentCart sous Business Reviews, et tu cliques sur Settings. Tu peux aussi y accéder par Settings, Reviews Platforms, Fluent Cart Settings, avec le bouton Configure Connection.

**[ECRAN - popup Fluent Cart Configuration, recherche de produits, Save]**

Dans la fenêtre de configuration, tu utilises la barre de recherche pour trouver et sélectionner les produits dont tu veux récupérer les avis, puis Save. Une fois les produits ajoutés, tu peux cliquer sur Add New Template directement depuis la fenêtre pour concevoir ta mise en page.

**[ECRAN - FluentCart Pro → Products → onglet Integrations → Add Integration → WP Social Ninja]**

Tu peux aussi piloter l'intégration depuis FluentCart. Dans FluentCart Pro, Products, tu édites un produit, tu vas dans l'onglet Integrations, tu cliques sur Add Integration et tu choisis WP Social Ninja. Tu renseignes un titre, tu sélectionnes ton modèle, tu actives l'intégration et tu cliques sur Create WP Social Ninja Feed.

**[FACE CAMERA]**

Une note technique de la doc, utile pour la suite : si tu utilises un modèle de type Native pour collecter des avis, pense à bien régler la cible, le Review Target, sur FluentCart. On reparlera des formulaires natifs et des sources custom dans la prochaine leçon, alors garde ce terme en tête.

---

**[SECTION 4 - Le point commun : afficher avec le shortcode]**

**[ECRAN - slide récap "AliExpress / WooCommerce / FluentCart → modèle → shortcode"]**

Comme pour Google, Facebook et les autres, le principe d'affichage reste identique. Tu connectes ta source, tu crées un Review Template en cochant la bonne plateforme dans General puis Platforms, et tu poses le shortcode sur ta page.

Pour le e-commerce, un filtre est particulièrement utile dans le modèle : tu peux filtrer par produit ou par catégorie, pour n'afficher sur une fiche que les avis qui la concernent. Et pour AliExpress comme pour les autres, tu peux combiner plusieurs sources dans un même modèle si tu veux un mur d'avis unifié.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter AliExpress par simple URL produit, faire de WP Social Ninja ton hub d'avis WooCommerce, et brancher FluentCart avec son panneau interactif. Trois sources, un même réflexe d'affichage. Dans la prochaine leçon, on passe aux avis maison : formulaires natifs, sources custom et QR code pour collecter toi-même les retours de tes clients. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- AliExpress : icône Settings + champs Product Name / Product ID (section 1)
- AliExpress : page produit avec l'URL dans la barre d'adresse (section 1)
- WooCommerce : module activé + sélection de produits, bouton Add More Product (section 2)
- WooCommerce Settings : auto-sync + Make WP Social Ninja Your Main Review Hub surligné (section 2)
- WooCommerce : comportement au clic (scroll vs drawer Modern/Default) (section 2)
- Fiche produit WooCommerce : Product Data → onglet WP Social Ninja (section 2)
- FluentCart : popup Fluent Cart Configuration avec recherche de produits (section 3)
- FluentCart Pro : Products → Integrations → Add Integration → WP Social Ninja (section 3)
- Slide récap des trois sources e-commerce vers modèle vers shortcode (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast AliExpress, rythme rapide (cas dropshipping)
- Section 2 : screencast WooCommerce, ralentir sur les réglages globaux (le hub)
- Section 3 : screencast FluentCart, montrer les deux entrées (plugin + FluentCart Pro)
- Section 3 fin : face camera, teaser du terme Review Target / Native pour la leçon 3.6
- Section 4 : slide récap, ancrer le pattern shortcode + filtre par produit
- Outro : face camera, CTA visuel vers la leçon 3.6

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - AliExpress | 1:45 |
| Section 2 - WooCommerce | 2:45 |
| Section 3 - FluentCart | 2:30 |
| Section 4 - Shortcode commun | 1:10 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__aliexpress-configuration.md`
- Doc : `sources/docs/guide__business-reviews__woocommerce-reviews.md`
- Doc : `sources/docs/guide__business-reviews__fluentcart-product-review.md`
- Vidéos officielles : #40 (Quickly Embed AliExpress Reviews), #69 (Show AliExpress Reviews 2024), #65 (Display WooCommerce Reviews)

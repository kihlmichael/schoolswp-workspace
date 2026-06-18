# Leçon 3.3 - Facebook, Trustpilot et Yelp

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter trois plateformes d'avis aux méthodes différentes : Facebook par connexion OAuth (ou par jeton manuel pour les développeurs), Trustpilot par simple URL, et Yelp par clé API et Place ID, en connaissant la limite payante de Yelp.
- **Prérequis** : Leçon 3.2 vue (mécanique connecter / cocher / shortcode acquise).

---

## Script narration

**[INTRO - face camera]**

Maintenant que Google est en place, on enchaîne avec trois plateformes très demandées : Facebook, Trustpilot et Yelp. Et l'intérêt de cette leçon, c'est qu'elles illustrent trois niveaux de difficulté de connexion.

Facebook se connecte par simple login, c'est rapide. Trustpilot, c'est encore plus simple : une seule information à coller. Yelp demande un peu plus de travail, avec une clé technique et une limite payante à connaître. Une fois ces trois-là maîtrisées, tu auras vu l'essentiel des cas de figure. On y va.

---

**[SECTION 1 - Facebook : la connexion recommandée par login]**

**[ECRAN - WP Social Ninja → Platforms → ligne Facebook → icône Settings]**

On commence par Facebook. Direction Platforms, tu trouves la ligne Facebook, et tu cliques sur l'icône Settings à droite.

Une fenêtre te demande de choisir le type d'identifiant. Tu as deux choix : OAuth 2.0, c'est-à-dire la connexion par login Facebook, et Manually Connect a Page, la connexion manuelle. Pour la grande majorité des cas, prends la première option, OAuth 2.0, recommandée. Pas besoin de clé de développeur.

**[ECRAN - fenêtre Facebook de login + "Continue as..."]**

Une fenêtre Facebook sécurisée s'ouvre. Tu te connectes si nécessaire, puis Facebook te demande d'autoriser WP Social Ninja. Tu cliques sur Continue as, suivi de ton nom. C'est une procédure standard et sûre.

**[ECRAN - popup "Select Page(s)" + bouton Connect Pages]**

Ensuite, le plugin affiche la liste de tes pages professionnelles Facebook. Tu coches la ou les pages dont tu veux récupérer les avis, puis tu cliques sur Connect Pages. La ligne Facebook passe au vert avec le statut Connected. C'est fait.

---

**[SECTION 2 - Facebook : la méthode manuelle pour les développeurs]**

**[ECRAN - slide "Cas développeur : Page ID + Access Token"]**

Un mot rapide sur la méthode manuelle, parce qu'elle a un vrai usage. Imagine que tu construis le site d'un client : tu n'as pas envie de lui demander son mot de passe Facebook.

Dans ce cas, tu choisis Manually Connect a Page. Le plugin te demande deux informations : un Page ID et un Access Token. Ton client les génère lui-même, en toute sécurité, depuis le générateur de jeton de WP Social Ninja, en cliquant sur Continue with Facebook et en sélectionnant sa page. Il te transmet les deux codes par e-mail, tu les colles, tu enregistres, et la page est connectée sans jamais avoir eu besoin de ses identifiants. Garde ça en réserve, c'est précieux en agence.

---

**[SECTION 3 - Trustpilot : la connexion la plus simple]**

**[ECRAN - WP Social Ninja → Platforms → ligne Trustpilot → icône Settings]**

Place à Trustpilot, et là tu vas souffler, parce que c'est la connexion la plus simple de tout le module. Contrairement aux autres, pas de clé API ni de compte développeur. Une seule information suffit : l'adresse de ta page Trustpilot.

Tu cliques sur l'icône Settings de la ligne Trustpilot. Une fenêtre s'ouvre avec un seul champ : Enter your business URL to get your reviews. Tu la laisses ouverte.

**[ECRAN - site Trustpilot, barre d'adresse avec l'URL de la page entreprise]**

Tu vas sur le site Trustpilot, tu cherches ton entreprise, tu ouvres sa page d'avis. Puis tu regardes l'adresse dans la barre du navigateur, du type trustpilot point com slash review slash ton-domaine. Tu copies cette URL complète.

**[ECRAN - retour WordPress, collage de l'URL, bouton Save]**

Tu reviens dans WordPress, tu colles l'URL dans le champ, et tu cliques sur Save. La ligne Trustpilot passe au vert. Tes avis vont se synchroniser. C'était presque trop facile.

---

**[SECTION 4 - Yelp : clé API et Place ID]**

**[ECRAN - WP Social Ninja → Platforms → ligne Yelp → icône Settings, champs API Key et Place ID]**

Yelp demande un peu plus d'effort, mais rien d'insurmontable. Tu cliques sur l'icône Settings de la ligne Yelp. La fenêtre attend deux informations : une API Key et un Place ID.

**[ECRAN - Yelp Developers → Manage App → Create App]**

Pour la clé, tu vas sur le portail Yelp Developers, tu te connectes avec le compte de ton entreprise, et dans la section Manage App tu crées une application. Tu remplis le nom, le secteur, ton e-mail et une courte description, puis Create App. Yelp affiche aussitôt ta clé API. Tu la copies.

**[ECRAN - page Yelp de l'entreprise, URL avec le segment après /biz/]**

Pour le Place ID, c'est simplement la partie unique de l'adresse de ta page Yelp. Tu vas sur Yelp point com, tu cherches ton établissement, et dans l'URL, tu prends le texte qui suit slash biz slash. Par exemple, pour yelp point com slash biz slash bocconcino-san-francisco, ton Place ID est bocconcino-san-francisco. Tu le copies.

**[ECRAN - retour WordPress, collage API Key + Place ID, bouton Save]**

Tu reviens dans le plugin, tu colles la clé API et le Place ID dans leurs champs, puis Save. La ligne Yelp passe au vert.

**[FACE CAMERA]**

Et là, un point honnête et important. Depuis quelque temps, l'API de Yelp ne fournit plus les avis gratuitement. Pour récupérer tes avis Yelp dans WP Social Ninja, il te faut un forfait Yelp Pro : la formule Pro Enhanced donne jusqu'à trois extraits d'avis par établissement, la Pro Premium jusqu'à sept. Ces limites sont fixées par Yelp, pas par le plugin. À toi de voir si ça vaut le coût selon ton activité, typiquement un restaurant ou un commerce local.

---

**[OUTRO - face camera]**

Tu viens de voir trois logiques de connexion : login pour Facebook, simple URL pour Trustpilot, clé API et Place ID pour Yelp, avec sa limite payante. Et à chaque fois, la suite est la même : tu coches la plateforme dans un modèle et tu poses le shortcode, exactement comme avec Google. Dans la prochaine leçon, on s'attaque au tourisme et au local : Airbnb, Booking.com et Tripadvisor. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Facebook : icône Settings + popup choix OAuth 2.0 vs Manually Connect a Page (section 1)
- Facebook : fenêtre login + Continue as, puis popup Select Page(s) et bouton Connect Pages (section 1)
- Slide "Cas développeur" : schéma Page ID + Access Token transmis par le client (section 2)
- Trustpilot : champ unique business URL + barre d'adresse Trustpilot à copier (section 3)
- Yelp : fenêtre avec champs API Key et Place ID (section 4)
- Yelp Developers : Manage App → Create App → clé affichée (section 4)
- Yelp : URL de l'établissement, segment après /biz/ surligné (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast Facebook, rythme rapide (c'est la voie simple)
- Section 2 : slide explicative, ton "astuce pro" pour le cas agence
- Section 3 : screencast Trustpilot, insister sur la simplicité (contraste avec Yelp qui suit)
- Section 4 : screencast Yelp, ralentir sur la distinction clé API vs Place ID
- Section 4 fin : retour face camera sur la limite payante Yelp - moment de franchise
- Outro : face camera, CTA visuel vers la leçon 3.4

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Facebook OAuth | 2:00 |
| Section 2 - Facebook manuel | 1:15 |
| Section 3 - Trustpilot | 1:45 |
| Section 4 - Yelp | 3:15 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__facebook-configuration.md`
- Doc : `sources/docs/guide__business-reviews__facebook-reviews-access-token.md`
- Doc : `sources/docs/guide__business-reviews__trustpilot-configuration.md`
- Doc : `sources/docs/guide__business-reviews__yelp-configuration.md`
- Vidéos officielles : #21 (How To Add Facebook Reviews), #42 (How to Show Facebook Reviews), #77 (Embed Facebook Page Reviews), #39 (Integrate Yelp Reviews)

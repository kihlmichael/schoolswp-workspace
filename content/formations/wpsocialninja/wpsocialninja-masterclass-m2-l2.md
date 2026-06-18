# Leçon 2.2 - YouTube : connexion (clé API v3 / OAuth) et 5 types de feed

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 10 min (~1400 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter sa chaîne YouTube à WP Social Ninja par l'une des deux méthodes (clé API ou OAuth), et choisir le bon type de feed parmi les cinq selon ce qu'on veut afficher.
- **Prérequis** : Module 1 terminé (plugin installé, interface connue).

---

## Script narration

**[INTRO - face camera]**

Dans cette leçon, on attaque le feed le plus utile pour un créateur de contenu : le feed YouTube. L'idée est simple : afficher tes vidéos directement sur ton site WordPress, et les laisser se mettre à jour toutes seules quand tu publies.

Mais avant d'afficher quoi que ce soit, il faut deux choses : connecter ton compte YouTube au plugin, puis choisir ce que tu veux montrer. On va voir les deux méthodes de connexion, puis les cinq types de feed disponibles. À la fin, tu sauras exactement lequel choisir selon ton besoin. C'est parti.

---

**[SECTION 1 - Les deux méthodes de connexion]**

**[ECRAN - WP Social Ninja → Platforms → onglet Social Feeds → YouTube → Connect]**

On commence par la connexion. Depuis ton tableau de bord WordPress, tu vas dans WP Social Ninja, puis Platforms. Tu cliques sur l'onglet Social Feeds, tu trouves YouTube dans la liste, et tu cliques sur Connect.

Une fenêtre s'ouvre avec deux options. La première : clé API, recommandée. La seconde : OAuth 2.0, c'est-à-dire connexion via Google.

La différence en une phrase : la clé API est plus stable dans le temps, c'est celle que je te conseille pour un site de production. L'OAuth est plus rapide à mettre en place mais repose sur un code d'accès, pratique pour un test rapide. On va voir les deux, en commençant par la clé API.

---

**[SECTION 2 - Méthode 1 : créer la clé API dans Google Cloud]**

**[ECRAN - console.cloud.google.com]**

La clé API se crée gratuitement dans la Google Cloud Console. Tu te connectes avec ton compte Google.

En haut, tu cliques sur le menu déroulant Select a Project, puis sur New Project. Tu donnes un nom au projet, par exemple WP Social Ninja, et tu valides avec Create.

Une fois le projet créé, tu vas dans le menu APIs and Services, puis Credentials. Tu cliques sur le bouton Create Credentials en haut, et tu choisis API key. Une fenêtre affiche ta nouvelle clé : tu cliques sur l'icône de copie pour la récupérer.

**[ECRAN - APIs and Services → API Library → YouTube Data API v3]**

Et là, attention, c'est l'étape que tout le monde oublie. Une clé seule ne suffit pas. Tu dois activer l'API YouTube Data v3, sinon la clé ne fonctionnera pas.

Tu retournes dans APIs and Services, tu ouvres l'API Library, tu cherches YouTube Data API v3, et tu l'actives. Sans cette activation, ton feed restera vide et tu chercheras le problème pendant une heure. Donc on le fait tout de suite.

**[ECRAN - retour WordPress, champ YouTube API Key, Save]**

Tu reviens ensuite dans WordPress, tu rouvres la fenêtre de configuration YouTube, tu choisis l'option clé API, tu colles ta clé dans le champ YouTube API Key, et tu cliques sur Save. Un message de succès confirme que ton compte est connecté. C'est fait.

---

**[SECTION 3 - Méthode 2 : OAuth via Google]**

**[ECRAN - option OAuth 2.0, bouton Sign In and Get Google Access Code]**

La deuxième méthode est plus directe. Dans la fenêtre de connexion, tu choisis OAuth 2.0, puis tu cliques sur Sign In and Get Google Access Code.

Une fenêtre Google s'ouvre. Tu choisis le compte qui gère ta chaîne YouTube, tu cliques sur Continue pour autoriser WP Social Ninja. Google te renvoie un code d'accès : tu le copies, tu reviens dans le plugin, tu le colles dans le champ Access Code, et tu enregistres.

Mon conseil : pour ton vrai site, reste sur la clé API. L'OAuth dépend d'un code qui peut expirer, alors que la clé API tient dans la durée. Maintenant que la connexion est faite, passons au cœur du sujet.

---

**[SECTION 4 - Les cinq types de feed]**

**[ECRAN - éditeur de template, dropdown Feed Type]**

Quand tu crées un template YouTube, le réglage le plus important s'appelle le Feed Type. C'est lui qui décide quel contenu va s'afficher. Il existe cinq types. On les passe en revue.

**[ECRAN - slide "5 Feed Types", apparition une par une]**

Type 1 : Channel. Il affiche les dernières vidéos d'une chaîne entière. Tu lui donnes l'identifiant de la chaîne, sous trois formes possibles : le handle (par exemple @michaelkihl), l'identifiant long qui commence par UC, ou l'ancien nom d'utilisateur. C'est le choix par défaut pour afficher tout le flux d'une chaîne, toujours à jour.

Type 2 : Playlist. Il affiche toutes les vidéos d'une seule playlist. Tu colles l'identifiant de la playlist, celui qui suit list= dans l'URL, et tu peux fixer le nombre de vidéos à récupérer. Parfait quand tu as déjà organisé tes vidéos par thème en playlists sur YouTube.

Type 3 : Search, le terme de recherche. Il affiche les vidéos qui correspondent à un mot-clé. Tu tapes par exemple WordPress Plugins, et le feed remonte les meilleurs résultats. Utile pour une veille ou un mur de vidéos thématiques, mais tu ne contrôles pas exactement quelles vidéos sortent.

Type 4 : Specific Videos, les vidéos choisies. Et celui-là, retiens-le bien, c'est le plus puissant pour nous. Il te laisse sélectionner tes vidéos une par une, par leur identifiant. Tu peux en mettre plusieurs, séparées par une virgule. C'est la curation totale : tu décides exactement quelles vidéos apparaissent, dans quel ordre.

Type 5 : Live Streams, les directs. Il affiche les lives d'une chaîne : terminés, à venir, ou en cours. Pratique si tu fais des directs réguliers.

---

**[SECTION 5 - Quel type choisir selon ton besoin]**

**[ECRAN - slide tableau "Besoin → Type de feed"]**

Résumons par cas d'usage, parce que c'est ça qui compte.

Tu veux afficher tout ton flux, toujours frais : Channel. Tu as déjà rangé tes vidéos en playlists thématiques : Playlist. Tu veux un mur de vidéos sur un sujet, sans trier : Search. Tu veux choisir précisément quelles vidéos montrer, par exemple une sélection de tes meilleurs tutos : Specific Videos. Tu diffuses des directs : Live Streams.

**[FACE CAMERA]**

Garde en tête le type Specific Videos. Dans le Module 7, on construira une page Vidéos qui affiche des tutos triés par thème sur un site schoolsWP, et c'est exactement ce type de feed qu'on utilisera pour garder la main sur la sélection. Tu verras, le lien entre cette leçon et le cas pratique sera direct.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter ta chaîne par clé API ou par OAuth, et tu connais les cinq types de feed avec le bon réflexe pour chacun. Dans la prochaine leçon, on passe à l'apparence : les layouts grille et carrousel, les skins prêts à l'emploi, et les filtres pour affiner ta sélection. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Parcours de connexion : WP Social Ninja → Platforms → Social Feeds → YouTube → Connect (section 1)
- Google Cloud Console : création de projet, Create Credentials, API key (section 2)
- Activation de YouTube Data API v3 dans l'API Library - insister visuellement, c'est le piège (section 2)
- Champ YouTube API Key dans WP Social Ninja + message de succès (section 2)
- Parcours OAuth : bouton Sign In, sélection du compte Google, copie du code (section 3)
- Slide animée "5 Feed Types" : apparition une par une, icône par type (section 4)
- Slide tableau "Besoin → Type de feed" avec la ligne Specific Videos surlignée en vert schoolsWP (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 4 : alternance screencast (clics réels dans l'interface) et slides Kadence
- Section 2 : ralentir sur l'activation de l'API v3, c'est le point de friction numéro un
- Section 5 : retour face camera sur le teaser Module 7 - ton direct, pas de slide
- Outro : face camera, CTA visuel vers la leçon 2.3

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Deux méthodes | 1:15 |
| Section 2 - Clé API Google | 2:45 |
| Section 3 - OAuth | 1:30 |
| Section 4 - Cinq types de feed | 2:45 |
| Section 5 - Quel type choisir | 1:00 |
| Outro | 0:15 |
| **Total** | **~10:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__youtube-configuration.md`
- Doc : `sources/docs/guide__social-feeds__youtube-feed-types.md`
- Vidéos officielles : #3 (Getting Started YouTube Feed), #23 (Add YouTube Feeds), #72 (Embed YouTube Channel)

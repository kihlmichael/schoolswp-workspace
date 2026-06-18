# Leçon 2.4 - Facebook feed : intégration, token, layouts, albums et events

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter une Page Facebook à WP Social Ninja (connexion directe ou par token), choisir le bon type de contenu (timeline, photos, vidéos, albums, events) et configurer les layouts et filtres du feed.
- **Prérequis** : Leçon 2.1 terminée (mécanique source / template / shortcode). Une Page Facebook (pas un profil personnel).

---

## Script narration

**[INTRO - face camera]**

On passe à Facebook. Et tout de suite une précision importante : le feed Facebook fonctionne avec une Page, pas avec ton profil personnel. Si tu as une page pour ton activité, tu es bon.

Dans cette leçon, on voit les deux façons de connecter ta Page : la connexion directe, simple, et la connexion par token, utile quand tu gères la page d'un client. Ensuite, on explore les types de contenu, parce que Facebook va bien plus loin que la simple timeline : photos, vidéos, albums, et même les events. C'est parti.

---

**[SECTION 1 - Connexion directe à ta Page]**

**[ECRAN - WP Social Ninja → Platforms → Facebook → icône Settings]**

On commence par la méthode la plus simple. Depuis ton tableau de bord, va dans WP Social Ninja, puis Platforms. Repère Facebook et clique sur l'icône Settings à côté.

Une fenêtre s'ouvre. Tu cliques sur Continue with Facebook, tu te connectes à ton compte Facebook, et tu autorises WP Social Ninja. Google te renvoie ensuite sur la page des Platforms, où une popup te demande de sélectionner une ou plusieurs Pages à afficher. Tu choisis tes pages, tu cliques sur Connect Pages, et c'est fait.

Tu verras alors ta Page connectée. Tu peux en retirer une avec le bouton Remove, ou en ajouter d'autres avec Add More Account. Pour passer à l'affichage, clique sur Add New Template.

**[ECRAN - encart troubleshooting "Pages not appearing"]**

Un point de dépannage utile : si tu as bien connecté ton compte mais que tes Pages n'apparaissent pas dans la liste, c'est souvent une ancienne app WP Social Ninja restée dans tes intégrations Facebook. Tu vas dans les Business Integrations de Facebook, tu supprimes l'ancienne app, et tu refais la connexion. Garde en tête une règle Meta : supprimer une app déconnecte le token de tous les sites qui l'utilisent. Tu devras donc réautoriser partout.

---

**[SECTION 2 - Connexion par token (cas client)]**

**[ECRAN - popup Facebook → dropdown Credential Type → Account Manually]**

Deuxième méthode : la connexion par token. Elle sert surtout quand tu gères la Page d'un client et que tu ne veux pas lui demander ses identifiants Facebook.

Dans la popup de configuration, tu choisis Account Manually dans le type de credentials. Puis tu vas sur le générateur de token officiel de WP Social Ninja, une page dédiée sur leur site. Tu cliques sur Continue with Facebook, tu autorises, et la page te donne deux choses : un Page ID et un Access Token. Tu copies l'Access Token, tu reviens dans le plugin, tu le colles dans le champ prévu, et tu cliques sur Connect.

L'intérêt : tu peux envoyer cette page de génération à ton client. Il te transmet son token et son ID, et tu connectes sa Page sans jamais toucher à son mot de passe. WP Social Ninja ne stocke rien sur cette page, c'est une app approuvée par Facebook qui utilise l'API officielle.

---

**[SECTION 3 - Les types de contenu (Feed Type)]**

**[ECRAN - éditeur de template Facebook → onglet General → section Source → Feed Type]**

Maintenant le cœur du sujet. Dans l'éditeur de template, onglet General, section Source, le réglage Feed Type décide quel type de contenu remonter. Et Facebook est riche.

Timeline : les posts classiques de ta Page, comme un visiteur les verrait. C'est l'option la plus courante. All Videos : uniquement les vidéos, parfait pour une galerie vidéo. Photos : uniquement les posts photo. Events : un feed de tes événements, avec date, heure et titre. Album et Single Album : pour mettre en avant un album photo précis. Et Specific Video Playlist : une playlist vidéo précise.

Tu choisis aussi le Total Feed, le nombre maximum de posts à récupérer, et si tu as connecté plusieurs Pages, tu sélectionnes laquelle afficher dans ce template.

---

**[SECTION 4 - Layouts et filtres Facebook]**

**[ECRAN - section Template → Layout Type]**

Pour la disposition, Facebook offre plus d'options que YouTube. Timeline, une seule colonne façon mur Facebook. Grid, une grille nette à hauteurs égales. Masonry, une grille de type Pinterest aux hauteurs variables. Et Carousel, le slider horizontal. Comme partout, tu règles les colonnes pour bureau, tablette et mobile, et l'espacement.

**[ECRAN - section Filters → Date Range]**

Côté filtres, en plus des classiques Show et Hide par mots-clés, Facebook a une fonction puissante : le Date Range. Tu as trois choix. Aucun filtre de date. Specific Date Range, une plage fixe entre deux dates, idéale pour un feed d'archive comme "nos posts de juin 2025". Et Relative Date Range, dynamique : "les posts des 30 derniers jours". Celui-là se met à jour tout seul, parfait pour un feed "Actu récente" qui reste toujours frais sans que tu y touches.

Tu peux aussi filtrer par type de contenu avec Display Post With, et masquer des posts précis par leur identifiant.

---

**[SECTION 5 - Les events Facebook]**

**[ECRAN - Feed Type → Events]**

Les events méritent un arrêt, parce qu'ils demandent une connexion particulière. Afficher tes événements Facebook sur ton site, c'est excellent pour un formateur ou un commerce qui organise des dates régulières.

Pour ça, le Feed Type Events a besoin d'un Event Access Token dédié, distinct du token de feed classique. Sa création passe par une app Facebook Developer avec des permissions spécifiques sur les events de la page, puis par la conversion en token longue durée pour que la connexion tienne dans le temps. C'est un peu plus technique : la procédure pas à pas est documentée, je te renvoie à la doc officielle pour la suivre sans te tromper.

Un point important à connaître : un événement créé par un simple co-organisateur n'apparaîtra pas dans ton feed. L'API de Facebook ne partage que les events créés directement par la Page principale. Si un event ne remonte pas, vérifie d'abord qui l'a créé.

---

**[SECTION 6 - Albums, playlists vidéo et réglages globaux]**

**[ECRAN - Feed Type → Single Album / Specific Video Playlist]**

Deux feeds spécifiques rapides à poser. Pour un Single Album : tu choisis Single Album dans le Feed Type, tu colles l'URL ou l'ID de l'album, tu choisis la Page à laquelle il appartient, et tu cliques sur Fetch Feeds. Pour une playlist vidéo : même logique avec Specific Video Playlist, l'URL ou l'ID de la playlist, et la Page concernée.

**[ECRAN - WP Social Ninja → Settings → Feed Platforms → Facebook Settings]**

Et comme pour YouTube, pense aux réglages globaux dans Settings, Feed Platforms, Facebook Settings. Check New Feeds Every pour la fréquence de vérification, Clear Cache si tes nouveaux posts n'apparaissent pas, et Optimize Image pour accélérer le chargement. Attention au même compromis : avec l'optimisation, les vidéos ne se lisent plus directement dans le feed, et pour un carrousel de post, seule la première image s'affiche.

**[FACE CAMERA]**

Le réflexe Facebook : Page et pas profil, et token séparé pour les events. Garde ces deux points en tête, ils évitent 90 % des blocages.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter ta Page Facebook par les deux méthodes, choisir le bon type de contenu, et même afficher tes albums et tes events. Dans la prochaine leçon, on attaque Instagram, avec ses comptes Business Basic et Advanced, le feed shoppable, et la conformité RGPD. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Platforms → Facebook → Continue with Facebook → sélection des Pages → Connect Pages (section 1)
- Encart troubleshooting Business Integrations (section 1)
- Générateur de token officiel : Page ID et Access Token (section 2)
- Dropdown Feed Type Facebook déployé (Timeline, Photos, Videos, Events, Album, etc.) (section 3)
- Section Filters avec le Date Range (Specific / Relative) mis en évidence (section 4)
- Procédure Event Access Token : permissions dans l'API Explorer + token longue durée (section 5)
- Settings → Feed Platforms → Facebook Settings, bouton Clear Cache en vert schoolsWP (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP, insister sur "Page, pas profil"
- Sections 1 à 4 : alternance screencast et slides Kadence
- Section 5 : ralentir, signaler clairement que la procédure token est dans la doc officielle, ne pas filmer chaque clic du portail développeur
- Section 6 : retour face camera sur les deux réflexes clés
- Outro : face camera, CTA visuel vers la leçon 2.5

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Connexion directe | 1:30 |
| Section 2 - Connexion par token | 1:30 |
| Section 3 - Types de contenu | 1:15 |
| Section 4 - Layouts et filtres | 1:30 |
| Section 5 - Events | 1:30 |
| Section 6 - Albums et réglages globaux | 1:00 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__facebook-integration.md`
- Doc : `sources/docs/guide__social-feeds__facebook-feed-access-token.md`
- Doc : `sources/docs/guide__social-feeds__facebook-customization.md`
- Doc : `sources/docs/guide__social-feeds__facebook-layout-styling.md`
- Doc : `sources/docs/guide__social-feeds__facebook-single-album-feed.md`
- Doc : `sources/docs/guide__social-feeds__facebook-specific-video-playlist-feed.md`
- Doc : `sources/docs/guide__social-feeds__display-facebook-events.md`
- Doc : `sources/docs/guide__social-feeds__facebook-events-access-token.md`
- Doc : `sources/docs/guide__social-feeds__facebook-feed-settings.md`
- Vidéos officielles : #26 (Facebook Feed), #35 (Integrating Facebook Feed), #36 (Facebook Feed Settings), #78 (Embed Facebook Timeline Feed)

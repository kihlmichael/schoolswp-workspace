# Leçon 2.6 - X (Twitter) feed : connexion, réglages, styling

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter un compte X (Twitter) à WP Social Ninja via l'API V2 (Bearer Token), configurer les types de feed et les filtres, puis styliser le feed pour coller à sa marque.
- **Prérequis** : Leçon 2.1 terminée. Un compte développeur X (Twitter) pour générer les clés.

---

## Script narration

**[INTRO - face camera]**

On enchaîne avec X, l'ex-Twitter. Sa particularité : la connexion passe par le portail développeur, et tu dois récupérer une clé toi-même. Ça paraît technique, mais la méthode recommandée ne demande au final qu'une seule clé.

Dans cette leçon, on voit les deux méthodes de connexion, on récupère le Bearer Token étape par étape, on configure les types de feed et les filtres, et on termine par le styling pour que ton feed colle à ton site. C'est parti.

---

**[SECTION 1 - Deux méthodes : API V2 ou API V1]**

**[ECRAN - WP Social Ninja → Platforms → X (Twitter) → Connect]**

On commence dans le plugin pour voir ce qu'on doit aller chercher. Va dans WP Social Ninja, Platforms, repère la ligne X (Twitter), et clique sur Connect ou sur l'icône Settings.

Une fenêtre s'ouvre avec deux méthodes. API V2, recommandée : moderne et simple, elle demande seulement deux choses, ton nom d'utilisateur et un Bearer Token. API V1, avancée : plus ancienne et plus complexe, elle réclame quatre clés différentes.

Mon conseil sans détour : reste sur l'API V2. Une seule clé à gérer, c'est largement suffisant pour afficher tes posts. On va la récupérer. Laisse cet onglet ouvert.

---

**[SECTION 2 - Créer ton app et récupérer le Bearer Token]**

**[ECRAN - developer.x.com → Projects & Apps]**

Dans un nouvel onglet, va sur ton compte développeur X. La clé se génère depuis une app, et une app doit vivre dans un projet.

Première étape obligatoire : créer un projet. Dans Projects & Apps, si tu n'en as pas, clique sur Add Project et suis les écrans : un nom, un objectif. Ce projet est requis pour que le Bearer Token de l'API V2 fonctionne correctement.

**[ECRAN - bouton + Create App, nommage de l'app]**

Ensuite, à l'intérieur du projet, clique sur Create App. Donne-lui un nom que tu reconnaîtras, par exemple "WP Social Ninja Connection", et clique sur Next.

**[ECRAN - écran des credentials, champ Bearer Token]**

Et là, bonne nouvelle, l'écran suivant t'affiche directement tes credentials. Tu repères le champ Bearer Token, tu cliques pour copier cette longue chaîne de caractères, et tu la sauvegardes dans un endroit sûr, par exemple un fichier texte. C'est la seule clé dont tu as besoin pour la méthode V2.

Si jamais tu devais utiliser l'API V1, les quatre clés se trouvent dans l'onglet Keys and Tokens de ton app, mais on ne s'attarde pas dessus, l'API V2 couvre le besoin.

---

**[SECTION 3 - Connecter dans WP Social Ninja]**

**[ECRAN - retour popup → onglet API V2 → champs Username + Bearer Token]**

Retour dans WordPress, la popup est restée ouverte. Tu cliques sur l'onglet API V2, tu colles ton Bearer Token et ton nom d'utilisateur, puis Connect.

La fenêtre se ferme, et la ligne X (Twitter) affiche maintenant le statut Connected. Tu peux ajouter un autre compte avec Connect New Account, ou passer à l'affichage avec Add New Template.

---

**[SECTION 4 - Types de feed et filtres]**

**[ECRAN - éditeur de template X → onglet General → section Source → Feed Type]**

Dans l'éditeur, onglet General, section Source, le Feed Type décide quel contenu remonter. X en propose plusieurs.

User Timeline : les posts de ton propre compte, le choix le plus courant. Hashtag : les posts publics portant un hashtag, parfait pour un mur de campagne comme un hashtag d'événement. Home Timeline : ton fil principal. Mention : uniquement les mentions. Et Username : les comptes que tu as connectés.

Tu règles aussi le Total Feed, le nombre maximum de posts récupérés, et le bouton Fetch Feeds rafraîchit l'aperçu à la demande.

**[ECRAN - section Filters]**

Côté Filters, tu retrouves la logique du module : nombre de posts affichés, ordre croissant, décroissant ou aléatoire, filtres Show et Hide par mots-clés, et masquage de posts précis par leur identifiant. Une astuce de la doc : pour masquer toutes les réponses de ton feed, tu peux ajouter le symbole arobase dans le champ Hide.

---

**[SECTION 5 - Affichage du tweet]**

**[ECRAN - section Feed]**

Section Feed, tu contrôles chaque carte. Open Post In décide du clic : None pour une galerie non cliquable, X (Twitter) pour ouvrir le post sur X, ou Popup pour l'ouvrir dans une fenêtre sur ton propre site, la meilleure option pour garder le visiteur chez toi.

Ensuite, une série d'interrupteurs : photo de profil, nom de l'auteur, date, texte du post, icône de la plateforme, et les compteurs de likes, de réponses et de retweets. Tu peux limiter le nombre de mots du texte avec Trim Description Words pour garder un feed net, et activer Equal Height pour aligner les hauteurs en mode grille.

---

**[SECTION 6 - Le styling]**

**[ECRAN - onglet Style → sections Heading, Name, Meta, Content, Action, Item Box]**

On passe à l'onglet Style, qui contrôle l'apparence. Il est découpé en sections logiques que tu retrouveras, à quelques noms près, sur les autres feeds.

Heading : tout le header en haut du feed. Nom complet, nom d'utilisateur, bio, localisation, libellés et chiffres des statistiques, bouton Follow, et la boîte du header avec son fond, ses marges internes et sa bordure.

Name et Meta : le nom de l'auteur, l'arobase et la date sur chaque post. Content : le texte du post, avec un réglage dédié à la couleur des hashtags pour les faire ressortir. Action : la barre du bas avec les icônes de réponse, retweet et like, et leur couleur.

Et la section essentielle, Item Box : c'est la carte qui contient chaque tweet. Tu y règles le fond, les marges internes, la bordure et son épaisseur. C'est ce qui donne le rendu "carte" propre.

**[FACE CAMERA]**

Une chose à savoir : sur les social feeds, le styling complet est une fonction Pro. Sur la version gratuite, tu choisis déjà un skin et ta disposition, ce qui te donne un rendu propre. Le contrôle fin couleur par couleur, lui, demande la version Pro.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter X par Bearer Token, choisir ton type de feed, filtrer tes posts et styliser ta vitrine. Dans la prochaine leçon, on attaque TikTok, qui a la particularité de demander un plugin compagnon et impose une règle de reconnexion à connaître. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Popup de connexion X avec les deux méthodes API V2 / API V1 (section 1)
- Portail développeur : création de projet puis Create App (section 2)
- Écran credentials avec le Bearer Token mis en évidence (section 2)
- Onglet API V2 dans le plugin avec Username + Bearer Token + statut Connected (section 3)
- Dropdown Feed Type X (User Timeline, Hashtag, Mention, etc.) (section 4)
- Section Feed avec Open Post In et les interrupteurs d'affichage (section 5)
- Onglet Style avec les sections Heading / Item Box mises en évidence (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP, dédramatiser le portail développeur
- Section 2 : screencast du portail développeur, rester synthétique, ne pas filmer chaque sous-écran
- Sections 4 et 5 : screencast dans l'éditeur de template
- Section 6 : retour face camera pour signaler honnêtement que le styling fin est Pro
- Outro : face camera, CTA visuel vers la leçon 2.7

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Deux méthodes | 1:00 |
| Section 2 - Créer l'app et le token | 2:00 |
| Section 3 - Connecter | 0:45 |
| Section 4 - Types de feed et filtres | 1:15 |
| Section 5 - Affichage du tweet | 1:00 |
| Section 6 - Styling | 1:15 |
| Outro | 0:15 |
| **Total** | **~8:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__twitter-configuration.md`
- Doc : `sources/docs/guide__social-feeds__twitter-template-settings.md`
- Doc : `sources/docs/guide__social-feeds__twitter-feed-template-styling-connection.md`
- Doc : `sources/docs/guide__social-feeds__twitter-feed-settings.md`
- Vidéos officielles : #5 (Make Your Twitter Feed Super Stylish), #6 (Twitter Feed Settings), #7 (Configure your Twitter Account)

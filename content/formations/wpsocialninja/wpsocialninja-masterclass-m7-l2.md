# Leçon 7.2 - Créer la clé API YouTube Data v3 (Google Cloud), pas à pas

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 7 - Cas pratique schoolsWP : la page Vidéos
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Créer un projet Google Cloud, générer une clé API YouTube Data v3, activer l'API, puis brancher la clé dans WP Social Ninja, sans rien oublier.
- **Prérequis** : Leçon 7.1 vue, un compte Google, WP Social Ninja installé (Module 1).

---

## Script narration

**[INTRO - face camera]**

C'est l'étape qui débloque tout le reste. Sans clé API, aucun feed YouTube ne s'affiche. Bonne nouvelle : cette clé est gratuite, et on l'a déjà créée ensemble au Module 2. Mais comme c'est le prérequis du cas pratique et le point où la majorité des gens se trompent, je te refais le parcours complet, écran par écran, en m'attardant sur le piège qui fait perdre une heure.

On va passer dans la Google Cloud Console, créer un projet, générer la clé, activer l'API YouTube Data v3, puis revenir dans WordPress pour coller la clé. On suit l'ordre exact de la doc officielle. C'est parti.

---

**[SECTION 1 - Ouvrir la fenêtre de connexion dans WP Social Ninja]**

**[ECRAN - WP Social Ninja → Platforms → onglet Social Feeds → YouTube → Connect]**

On commence côté WordPress, juste pour voir où on devra revenir. Depuis ton tableau de bord, tu vas dans WP Social Ninja, puis Platforms. Tu cliques sur l'onglet Social Feeds, tu trouves YouTube dans la liste, et tu cliques sur Connect.

Une fenêtre s'ouvre avec deux options : clé API recommandée, et OAuth deux point zéro. On reste sur la clé API, c'est la méthode stable pour un site de production. Laisse cette fenêtre de côté, on y reviendra à la fin. Direction Google.

---

**[SECTION 2 - Créer un projet dans Google Cloud Console]**

**[ECRAN - console.cloud.google.com]**

Tu ouvres un nouvel onglet et tu vas sur console point cloud point google point com. Tu te connectes avec ton compte Google, celui qui gère ta chaîne YouTube de préférence.

En haut de la page, tu cliques sur le menu déroulant Select a Project, le sélecteur de projet. Une fenêtre s'ouvre, tu cliques sur New Project, nouveau projet.

**[ECRAN - écran New Project, champ Project name]**

Tu donnes un nom au projet. Mets quelque chose de clair, par exemple WP Social Ninja, comme ça tu le retrouves facilement plus tard. Tu cliques sur Create. Google prend quelques secondes pour créer le projet. Une fois fait, vérifie en haut que c'est bien ce projet qui est sélectionné, et pas un autre projet de ton compte.

---

**[SECTION 3 - Générer la clé API]**

**[ECRAN - APIs and Services → Credentials]**

Maintenant, dans le menu principal à gauche, tu vas dans APIs and Services, puis Credentials, c'est-à-dire les identifiants.

En haut de la page Credentials, tu cliques sur le bouton Create Credentials, créer des identifiants. Un menu apparaît, et tu choisis API key, clé API.

**[ECRAN - pop-up de nommage de la clé, puis pop-up "API key created"]**

Selon ta version de l'interface, Google peut te demander de nommer la clé : mets un nom et clique sur Create. Une fenêtre affiche alors ta nouvelle clé : une longue suite de lettres et de chiffres. Tu cliques sur l'icône de copie pour la récupérer. Garde cette clé sous la main, on va la coller dans WordPress dans un instant. Mais avant ça, il reste l'étape que tout le monde oublie.

---

**[SECTION 4 - Activer YouTube Data API v3, le piège numéro un]**

**[ECRAN - APIs and Services → API Library]**

Attention, on arrive sur le point critique. Une clé toute seule ne suffit pas. Tant que tu n'as pas activé l'API YouTube Data v3, ta clé ne renvoie rien et ton feed reste vide. C'est là que les gens cherchent le problème pendant une heure. On le fait tout de suite.

Tu retournes dans APIs and Services, et tu ouvres l'API Library, la bibliothèque d'API.

**[ECRAN - recherche "YouTube Data API v3" dans la bibliothèque, puis bouton Enable]**

Dans la barre de recherche, tu tapes YouTube Data API v3. Tu cliques sur le résultat, et sur la page de l'API tu cliques sur le bouton Enable, activer. Tu attends la confirmation. Voilà, ta clé est maintenant reliée à l'API YouTube. Retiens bien la règle : pas d'activation, pas de vidéos. Si plus tard ton feed est vide, c'est la première chose à revérifier ici.

---

**[SECTION 5 - Coller la clé dans WP Social Ninja]**

**[ECRAN - retour WordPress, fenêtre YouTube, champ YouTube API Key, Save]**

On revient dans WordPress, dans la fenêtre de connexion YouTube qu'on avait laissée ouverte. Tu sélectionnes l'option clé API recommandée. Tu colles ta clé dans le champ YouTube API Key, et tu cliques sur Save.

**[ECRAN - message de succès de connexion]**

Un message de succès confirme que ta chaîne est connectée. Si tu vois ce message, tout est en place. Si à l'inverse tu as une erreur, retourne dans Google Cloud vérifier deux choses : que la clé est bien copiée en entier, et que l'API YouTube Data v3 est bien activée sur le bon projet.

---

**[SECTION 6 - Un mot sur la sécurité de la clé]**

**[FACE CAMERA]**

Deux conseils rapides avant de clore. Premièrement, ta clé API, c'est comme un mot de passe : tu ne la partages pas en public, tu ne la colles pas dans une vidéo ou un screenshot non flouté. Deuxièmement, si tu veux la sécuriser davantage, Google te permet de restreindre une clé à l'API YouTube Data v3 uniquement, dans les réglages de la clé. Ce n'est pas obligatoire pour que ça marche, mais c'est une bonne habitude pour un site de production.

Pour l'alternative OAuth, on l'a déjà détaillée au Module 2 : elle est plus rapide mais repose sur un code qui peut expirer, donc pour ce cas pratique on garde la clé API.

---

**[OUTRO - face camera]**

Ta chaîne YouTube est connectée à WP Social Ninja, et l'API est activée. Le moteur tourne. Dans la prochaine leçon, on passe à la curation : on crée les quatre templates Specific Videos, un par thème, et on y colle les identifiants des vidéos un par un. C'est là que ta page commence à prendre forme. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Parcours WP Social Ninja → Platforms → Social Feeds → YouTube → Connect, fenêtre à deux options (section 1)
- Google Cloud Console : sélecteur de projet → New Project → champ Project name → Create (section 2)
- APIs and Services → Credentials → Create Credentials → API key, puis pop-up affichant la clé avec icône de copie (section 3)
- API Library : recherche "YouTube Data API v3" + bouton Enable - INSISTER, c'est le piège numéro un (section 4)
- Retour WordPress : champ YouTube API Key rempli + bouton Save + message de succès (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 5 : screencast réel (clics dans l'interface), pas de slide
- Section 4 : ralentir nettement, encart rouge ou pictogramme alerte sur l'activation de l'API
- Section 6 : retour face camera pour le rappel sécurité
- Outro : face camera, CTA visuel vers la leçon 7.3

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Ouvrir la fenêtre WPSN | 0:45 |
| Section 2 - Créer le projet Google | 1:45 |
| Section 3 - Générer la clé | 1:45 |
| Section 4 - Activer l'API v3 | 1:45 |
| Section 5 - Coller la clé | 1:15 |
| Section 6 - Sécurité de la clé | 1:00 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__youtube-configuration.md` (méthode 1 : API Key)
- Renvoi formation : leçon 2.2 (connexion clé API / OAuth, déjà rédigée)
- Vidéos officielles : #3 (Getting Started YouTube Feed)

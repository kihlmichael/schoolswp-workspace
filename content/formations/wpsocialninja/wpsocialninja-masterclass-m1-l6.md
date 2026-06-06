# Leçon 1.6 - La logique des connexions : clés API et tokens d'accès

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 1 - Fondations et prise en main
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Comprendre les trois grandes méthodes de connexion d'une plateforme (clé API, OAuth, token manuel), pourquoi WP Social Ninja les propose, et comment il stocke ces clés de façon sécurisée, pour ne plus être perdu face à n'importe quelle plateforme du plugin.
- **Prérequis** : Module 1 jusqu'à la leçon 1.5 (interface et réglages globaux connus).

---

## Script narration

**[INTRO - face camera]**

Dans le module suivant, on va connecter des plateformes : YouTube, Facebook, Instagram, Google, et bien d'autres. Et à chaque fois, le plugin va te demander quelque chose : une clé API, un code d'accès, parfois un token. Si tu ne comprends pas la logique derrière, tu vas avoir l'impression de refaire un parcours différent à chaque plateforme.

Bonne nouvelle : il n'y a en réalité que trois grandes méthodes de connexion. Une fois que tu les comprends, tu reconnais le bon parcours sur n'importe quelle plateforme. Cette leçon est volontairement transversale : pas de plateforme précise, mais la mécanique commune. On y va.

---

**[SECTION 1 - Pourquoi une connexion est nécessaire]**

**[ECRAN - slide schéma : ton site et serveur de la plateforme]**

D'abord, pourquoi connecter quoi que ce soit. WP Social Ninja n'invente pas tes contenus : il va les chercher chez la plateforme. Tes vidéos chez YouTube, tes avis chez Google, tes publications chez Instagram.

Pour aller chercher ces données, la plateforme exige une autorisation. C'est normal : elle veut s'assurer que c'est bien toi, et que tu as le droit d'accéder à ce contenu. Cette autorisation prend la forme d'une clé ou d'un code que tu fournis au plugin. Sans elle, le feed reste vide.

C'est tout le rôle de la section Platforms, qu'on a vue : c'est le hub où tu déposes ces autorisations, une par plateforme.

---

**[SECTION 2 - Méthode 1 : la clé API]**

**[ECRAN - slide "Méthode 1 : clé API"]**

Première méthode : la clé API. C'est une chaîne de caractères que tu génères toi-même chez le fournisseur, par exemple dans la console Google Cloud pour YouTube.

Le principe : tu crées un projet gratuit chez le fournisseur, tu génères une clé, et tu actives le service correspondant, par exemple l'API YouTube Data v3. Ensuite, tu copies cette clé et tu la colles dans le champ prévu du plugin.

L'avantage de la clé API, c'est la stabilité dans le temps. Elle ne dépend pas d'une session de connexion qui pourrait expirer. C'est pour ça que la doc la recommande pour un site de production. Le petit coût : la mise en place est un peu plus longue, parce que tu passes par la console du fournisseur. On détaillera le parcours complet de la clé API YouTube dans le module 2 et dans le cas pratique.

---

**[SECTION 3 - Méthode 2 : OAuth, le code d'accès]**

**[ECRAN - slide "Méthode 2 : OAuth (Sign In)"]**

Deuxième méthode : OAuth, la connexion directe via le compte. C'est la plus rapide à mettre en place.

Le principe : tu cliques sur un bouton du type Sign In and Get Access Code, une fenêtre du fournisseur s'ouvre, tu choisis ton compte, tu autorises WP Social Ninja, et le fournisseur te renvoie un code d'accès. Tu copies ce code, tu reviens dans le plugin, tu le colles dans le champ Access Code, et tu valides.

C'est exactement le parcours que suit Google pour les avis : Sign In, choisir le compte, autoriser, copier le code, le coller, vérifier. C'est rapide et sans console externe.

Le revers : OAuth repose sur un code lié à une session, qui peut expirer ou se rompre dans certaines situations. Pratique pour un test ou pour démarrer vite, mais pour un site de production durable, la clé API reste plus solide quand les deux options existent.

---

**[SECTION 4 - Méthode 3 : le token manuel]**

**[ECRAN - slide "Méthode 3 : token manuel (Page ID + Access Token)"]**

Troisième méthode : la connexion manuelle par token. On la rencontre par exemple pour les avis Facebook.

Le principe : au lieu de te connecter directement, tu génères les clés via un outil dédié, le générateur de tokens de WP Social Ninja. Tu obtiens alors deux informations, par exemple un Page ID et un Access Token. Tu les copies, et tu les colles dans les champs correspondants du plugin.

**[FACE CAMERA]**

À quoi ça sert. C'est très utile quand tu construis un site pour un client. Plutôt que de demander à ton client son mot de passe Facebook, tu lui envoies le lien du générateur. Il génère les deux clés de son côté, en sécurité, et il te les transmet. Tu connectes sa page sans jamais avoir eu ses identifiants. C'est la méthode la plus respectueuse pour une relation prestataire-client.

---

**[SECTION 5 - Comment le plugin garde tes clés en sécurité]**

**[ECRAN - slide "Stockage chiffré des tokens"]**

Dernier point, et il évite un bug qui surprend beaucoup de monde. Une fois que tu as connecté une plateforme, où vont ces clés et tokens.

WP Social Ninja les enregistre dans la base de données de WordPress, et il les chiffre pour les protéger. Pour ce chiffrement, par défaut, il s'appuie sur les clés et sels d'authentification de WordPress, ceux définis dans le fichier de configuration wp-config.

Le piège est là. Si ces sels changent, par exemple après une migration de site, ou parce qu'un plugin de sécurité les régénère, les anciens tokens ne peuvent plus être déchiffrés. Le plugin affiche alors une erreur du type "Access token decryption failed", et tes connexions se rompent.

La parade documentée : définir des clés de chiffrement dédiées à WP Social Ninja dans le fichier de configuration wp-config, deux constantes spécifiques au plugin. Ainsi, ton chiffrement ne dépend plus des sels WordPress et résiste aux migrations. Tu génères ces valeurs une fois, et la règle absolue : tu ne les modifies plus ensuite, sinon il faudrait reconnecter tous tes comptes. Et si tu travailles avec un environnement de staging, tu utilises les mêmes clés sur tous tes environnements.

---

**[OUTRO - face camera]**

Tu connais maintenant les trois méthodes de connexion (clé API, OAuth, token manuel), tu sais reconnaître laquelle s'applique, et tu comprends comment le plugin protège tes clés. C'est la fin du module fondations. Dans le module 2, on entre dans le vif du sujet : les feeds sociaux, en commençant par le plus utile pour un créateur, le feed YouTube. On se retrouve dans le prochain module.

---

## Notes de production

### Captures d'écran suggérées

- Slide schéma "ton site va chercher les données chez la plateforme" avec flèche d'autorisation (section 1)
- Slide "Méthode 1 : clé API" + aperçu console Google Cloud (génération de clé) (section 2) - assets doc api-keys, create-api-key
- Slide "Méthode 2 : OAuth" + bouton Sign In and Get Access Code (section 3) - asset doc google-business-review-2
- Slide "Méthode 3 : token manuel" avec champs Page ID et Access Token (section 4) - asset doc fb-business-review-manual-3
- Slide "Stockage chiffré des tokens" + extrait du fichier de configuration wp-config avec les deux constantes WPSR (section 5)
- Encadré rouge sur l'erreur "Access token decryption failed" (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 5 : slides conceptuelles, screencasts courts en illustration (pas de parcours complet, c'est une leçon transversale)
- Section 4 : retour face camera sur le cas client (prestataire), ton concret
- Section 5 : ralentir sur l'extrait du fichier de configuration et l'erreur, c'est le point de friction à retenir
- Outro : face camera, CTA visuel vers le module 2

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:40 |
| Section 1 - Pourquoi une connexion | 1:05 |
| Section 2 - Méthode clé API | 1:30 |
| Section 3 - Méthode OAuth | 1:30 |
| Section 4 - Méthode token manuel | 1:30 |
| Section 5 - Stockage sécurisé des clés | 1:35 |
| Outro | 0:25 |
| **Total** | **~8:00** |

### Sources

- Doc : sources/docs/guide__social-feeds__style-connection-settings.md
- Doc : sources/docs/guide__social-feeds__youtube-configuration.md (exemple clé API + OAuth)
- Doc : sources/docs/guide__business-reviews__google-configuration.md (exemple OAuth code d'accès)
- Doc : sources/docs/guide__business-reviews__facebook-reviews-access-token.md (exemple token manuel)
- Doc : sources/docs/guide__troubleshooting-support__fixing-access-token-decryption.md (stockage chiffré, clés dédiées)

> Note de précision : leçon transversale par conception. Les parcours plateforme-par-plateforme (clic à clic) sont détaillés dans les modules dédiés (module 2 pour les feeds, module 3 pour les avis). Ici, on ne donne que la mécanique commune, sans figer un parcours UI complet d'une plateforme précise.

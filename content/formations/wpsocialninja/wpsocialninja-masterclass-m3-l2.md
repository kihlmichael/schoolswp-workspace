# Leçon 3.2 - Google Reviews et Google My Business

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter sa fiche Google Business Profile à WP Social Ninja via le code d'accès, gérer plusieurs comptes Google, et créer un premier modèle pour afficher ses avis Google sur son site.
- **Prérequis** : Module 1 terminé, leçon 3.1 vue (rôle du tableau Reviews compris). Avoir une fiche Google Business Profile active.

---

## Script narration

**[INTRO - face camera]**

On attaque la plateforme d'avis la plus utilisée au monde : Google. Si tu as une fiche d'établissement, ce qu'on appelait Google My Business et qui s'appelle aujourd'hui Google Business Profile, tu as probablement déjà des avis qui dorment là-bas.

Dans cette leçon, on va les ramener sur ton site. Bonne nouvelle : c'est l'une des connexions les plus simples du plugin. Pas de clé API à fabriquer, pas de console technique. Tu vas juste te connecter avec ton compte Google et récupérer un code d'accès. On voit la connexion, la gestion de plusieurs comptes, puis le premier modèle d'affichage. C'est parti.

---

**[SECTION 1 - Le point de départ : la plateforme Google]**

**[ECRAN - WP Social Ninja → Platforms → section Business Reviews → Google]**

Tout commence dans la section Platforms du plugin. Depuis ton tableau de bord WordPress, tu vas dans WP Social Ninja, puis Platforms. C'est ton centre de connexion, aussi bien pour les feeds sociaux que pour les avis.

Dans la liste, tu cherches Google. Tu cliques dessus pour ouvrir la configuration. Une chose à savoir avant tout : pour récupérer tes avis Google, le plugin doit dialoguer avec les serveurs de Google. C'est pour ça qu'on passe par une autorisation. Rien de compliqué, je te montre.

---

**[SECTION 2 - Obtenir le code d'accès Google]**

**[ECRAN - bouton "Sign In And Get Google Access Code"]**

La première chose à faire est d'obtenir ton code d'accès Google. Tu cliques sur le bouton Sign In And Get Google Access Code. Une nouvelle fenêtre Google s'ouvre.

**[ECRAN - écran Google "Choisir un compte"]**

Étape une : tu choisis le compte e-mail associé à ta fiche Google Business Profile. C'est important, prends bien le bon compte, celui qui gère ton établissement.

**[ECRAN - écran Google "Continuer" pour autoriser]**

Étape deux : Google te demande d'accorder la permission à WP Social Ninja. Tu cliques sur Continue pour autoriser l'accès.

**[ECRAN - écran avec le code d'accès à copier]**

Étape trois : Google affiche un code d'accès. Tu le copies. C'est cette chaîne de caractères qui va faire le lien entre ton site et tes avis.

---

**[SECTION 3 - Coller le code et vérifier]**

**[ECRAN - retour WordPress, champ de configuration Google, bouton Verify Code]**

Étape quatre : tu reviens sur la page de configuration Google dans WordPress. Tu colles le code d'accès que tu viens de copier dans le champ prévu. Puis tu cliques sur Verify Code, le bouton qui vérifie le code.

Et voilà, le plugin se connecte aux serveurs de Google et commence à récupérer tes avis. Tu as réussi à connecter ta fiche Google Business Profile.

**[ECRAN - bouton "Connect New Account"]**

Petit bonus utile : si tu gères plusieurs établissements sur des comptes Google différents, tu peux cliquer sur Connect New Account pour ajouter d'autres comptes professionnels. Pratique pour une agence ou pour quelqu'un qui pilote plusieurs fiches. Tous les avis se retrouveront ensuite dans le même tableau Reviews qu'on a vu dans la leçon précédente.

---

**[SECTION 4 - Créer le premier modèle d'affichage]**

**[ECRAN - WP Social Ninja → Templates → Add New Template → Review Template]**

Connecter le compte ne suffit pas à afficher quoi que ce soit. Il faut maintenant créer un modèle, ce qu'on appelle un Template, qui décide à quoi ressembleront tes avis.

Tu vas dans WP Social Ninja, puis Templates, et tu cliques sur Add New Template. Dans le menu déroulant Template Type, tu choisis Review Template. Tu lui donnes un nom que tu retrouveras facilement, par exemple Avis Google accueil. Puis Create Template.

**[ECRAN - éditeur de template, onglet General → Platforms, case Google cochée]**

L'éditeur s'ouvre. Le réglage le plus important se trouve dans l'onglet General, section Platforms. C'est là que tu choisis quelles sources afficher. Tu coches Google.

Petit aperçu de ce qui t'attend dans cet éditeur, et qu'on détaillera dans la leçon 3.7 : tu pourras choisir une mise en page, grille ou carrousel par exemple, filtrer par note minimale pour ne montrer que tes meilleurs avis, et régler ce qui s'affiche sur chaque carte. Pour l'instant, retiens juste l'enchaînement : connecter, cocher la plateforme, créer le modèle.

---

**[SECTION 5 - Afficher le modèle avec le shortcode]**

**[ECRAN - colonne ShortCode dans la liste des templates]**

Dernière étape pour rendre tes avis visibles : le shortcode. Chaque modèle que tu crées génère automatiquement un petit code, une ligne unique du genre wp_social_ninja id égale cent, plateforme reviews.

Tu le trouves dans la liste de tes templates, dans la colonne ShortCode. Tu cliques dessus pour le copier.

**[ECRAN - éditeur de page WordPress, bloc Shortcode]**

Ensuite, tu vas sur la page où tu veux montrer tes avis. Tu ajoutes un bloc Shortcode dans l'éditeur WordPress, tu y colles ton code, et tu publies. WordPress remplace cette ligne par ton bloc d'avis Google, mis en forme. C'est le même mécanisme de shortcode que pour les feeds du Module 2 : un code, n'importe quelle page.

**[FACE CAMERA]**

Garde bien cette logique en tête, parce qu'elle est identique pour toutes les plateformes d'avis qu'on va voir ensuite. Connecter la plateforme, cocher la source dans un modèle, poser le shortcode. Une fois que tu maîtrises ça avec Google, le reste s'enchaîne vite.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter ta fiche Google par code d'accès, gérer plusieurs comptes, et afficher tes avis avec un premier modèle et son shortcode. Dans la prochaine leçon, on continue avec trois autres grands noms : Facebook, Trustpilot et Yelp, chacun avec sa propre méthode de connexion. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Parcours : WP Social Ninja → Platforms → Google dans la section Business Reviews (section 1)
- Bouton Sign In And Get Google Access Code (section 2)
- Les trois écrans Google : choix du compte, autorisation Continue, copie du code (section 2)
- Champ de collage du code + bouton Verify Code dans WordPress (section 3)
- Bouton Connect New Account pour les comptes multiples (section 3)
- Création du Review Template + case Google cochée dans General → Platforms (section 4)
- Colonne ShortCode + bloc Shortcode dans l'éditeur de page (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 3 : screencast réel, suivre le parcours de connexion clic par clic
- Section 2 : ralentir sur le choix du bon compte Google, c'est l'erreur fréquente
- Section 4 : screencast éditeur de template, rester léger (le détail viendra en 3.7)
- Section 5 : retour face camera pour ancrer le pattern "connecter / cocher / shortcode"
- Outro : face camera, CTA visuel vers la leçon 3.3

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Plateforme Google | 1:00 |
| Section 2 - Code d'accès | 2:15 |
| Section 3 - Coller et vérifier | 1:30 |
| Section 4 - Premier modèle | 2:00 |
| Section 5 - Shortcode | 1:25 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__google-configuration.md`
- Doc : `sources/docs/guide__business-reviews__create-template.md`
- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Vidéos officielles : #22 (How To Add Google Reviews), #37 (How to Set Up Google My Business), #68 (Add Google Reviews No Coding 2024)

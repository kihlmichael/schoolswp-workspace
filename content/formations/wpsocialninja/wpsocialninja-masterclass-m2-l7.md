# Leçon 2.7 - TikTok feed : activation, configuration, template

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Activer le feed TikTok (qui demande un plugin compagnon), connecter son compte par code d'accès, comprendre la règle de reconnexion sous 7 jours, et configurer le template.
- **Prérequis** : Leçon 2.1 terminée. Un compte TikTok.

---

## Script narration

**[INTRO - face camera]**

Dernier feed du module : TikTok. Et il a deux particularités à connaître dès le départ. La première : pour l'activer, il te faut un plugin compagnon en plus de WP Social Ninja. La seconde : TikTok impose une règle de reconnexion stricte, et si tu l'ignores, tes données disparaissent.

Dans cette leçon, on active le feed, on connecte le compte par code d'accès, on voit cette fameuse règle des 7 jours, puis on configure le template. C'est parti.

---

**[SECTION 1 - Activer le feed : le plugin compagnon]**

**[ECRAN - WP Social Ninja → Platforms → TikTok → icône Settings]**

Commençons par l'activation. Va dans WP Social Ninja, Platforms, et repère TikTok. Clique sur l'icône Settings de la ligne TikTok.

Si ton site n'a pas encore le plugin compagnon, une popup apparaît avec un message et un bouton d'installation. Ce plugin s'appelle Custom Feed for TikTok, et tu peux l'installer directement depuis WP Social Ninja sans aller chercher ailleurs. Tu cliques, et il s'installe.

Pourquoi ce plugin séparé ? C'est l'architecture choisie par l'éditeur pour TikTok, contrairement aux autres feeds qui sont intégrés d'office. Une fois Custom Feed for TikTok installé, ta plateforme TikTok dans WP Social Ninja s'active, et une nouvelle popup te propose de connecter ton compte.

---

**[SECTION 2 - Connecter par code d'accès]**

**[ECRAN - popup TikTok → bouton Continue with TikTok]**

La connexion se fait par un code d'accès. Dans la popup de configuration, tu cliques sur Continue with TikTok.

Tu es redirigé vers la page de connexion TikTok. Tu te connectes à ton compte. TikTok te demande ensuite d'accorder les permissions à l'app WP Social Ninja : tu sélectionnes les permissions et tu cliques sur Continue.

**[ECRAN - page affichant l'Access Code]**

La page suivante t'affiche un Access Code. Tu le copies, tu reviens dans la configuration TikTok du plugin, et tu le colles dans le champ Access Code. Ton compte TikTok est connecté. Tu peux alors créer ton template avec Add New Template.

---

**[SECTION 3 - La règle des 7 jours]**

**[ECRAN - slide "Reconnexion sous 7 jours" + capture de la notification d'erreur]**

Voici le point le plus important de cette leçon, et celui qu'on oublie le plus souvent. TikTok impose une reconnexion régulière de la source.

Si tu ne reconnectes pas ta source dans les 7 jours, deux choses se produisent. D'abord, tu reçois une notification d'erreur TikTok Feed Error. Ensuite, et c'est le vrai problème, toutes les données de ton feed TikTok sont automatiquement supprimées de ton site. C'est une règle de confidentialité imposée par TikTok, pas un bug du plugin.

Concrètement : surveille la notification, et reconnecte ton compte dans la fenêtre des 7 jours pour éviter la suppression automatique. Note-le quelque part, parce que c'est le piège classique du feed TikTok.

**[FACE CAMERA]**

Si ton feed TikTok disparaît un matin, ne cherche pas un bug ailleurs. Vérifie d'abord la date de ta dernière reconnexion. C'est presque toujours ça.

---

**[SECTION 4 - Configurer le template]**

**[ECRAN - éditeur de template TikTok → onglet General → section Source]**

Passons au template. Dans l'éditeur, onglet General, section Source, le Feed Type pour TikTok est le User Account Feed : il affiche les vidéos les plus récentes de ton profil. Si tu as connecté plusieurs comptes, tu choisis lequel afficher, et Fetch Feeds rafraîchit l'aperçu.

**[ECRAN - section Template → Layout Type]**

Côté disposition, tu retrouves les trois layouts du module : Grid pour une grille nette, Carousel pour un slider horizontal idéal en page d'accueil, et Masonry pour une grille de type Pinterest aux hauteurs variables. Comme partout, tu règles les colonnes pour bureau, tablette et mobile, et l'espacement entre les vidéos.

---

**[SECTION 5 - Filtres, affichage et social proof]**

**[ECRAN - sections Filters et Feed]**

Dans Filters, en plus du nombre de vidéos et des filtres par mots-clés, TikTok ajoute des options d'ordre intéressantes : Most Viewed pour les plus vues, et Most Likes pour les plus aimées, en plus de Newest, Oldest et Random. Pratique pour mettre en avant tes meilleures vidéos automatiquement.

Dans la section Feed, tu règles le clic avec Open Post In : None, TikTok, ou Popup, qui lit la vidéo dans une fenêtre sur ton site. Tu affiches ou masques la photo de profil, le nom, la description, l'icône de la plateforme et la date.

**[ECRAN - sous-section Views & Likes]**

Et une sous-section dédiée, Views & Likes, gère la preuve sociale : afficher le nombre de vues, le nombre de likes, et le nombre de commentaires par vidéo. Pour une marque, des compteurs élevés rassurent. Pour un portfolio plus sobre, tu peux les masquer.

Le Header te permet aussi d'afficher un mini-profil : photo, nom de compte, description, abonnés, et le total de likes de ton profil, une métrique forte sur TikTok. Et tu peux ajouter un bouton Follow en haut ou en bas du feed.

---

**[SECTION 6 - Réglages globaux]**

**[ECRAN - WP Social Ninja → Settings → Feed Platforms → TikTok Settings]**

Comme pour les autres plateformes, les réglages globaux sont dans Settings, Feed Platforms, TikTok Settings. Check New Feeds Every fixe la durée du cache, Clear Cache force le rafraîchissement si une vidéo récente n'apparaît pas, Optimize Images stocke les vignettes en local pour accélérer le chargement, et Reset Local Images les recharge.

À noter : pour le RGPD et le format d'image, ces réglages se trouvent dans l'onglet Advanced Settings, exactement comme on l'a vu pour Instagram. Si ton site est français, le réflexe d'optimisation et de conformité reste le même.

---

**[OUTRO - face camera]**

Tu as fait le tour des cinq feeds : YouTube, Facebook, Instagram, X et TikTok. Tu sais activer TikTok avec son plugin compagnon, le connecter par code, éviter le piège des 7 jours, et configurer le template. Dans la dernière leçon du module, on apprend à poser plusieurs feeds différents sur une même page et à pousser le styling un cran plus loin. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Platforms → TikTok → popup d'installation de Custom Feed for TikTok (section 1)
- Bouton Continue with TikTok puis page d'autorisation des permissions (section 2)
- Page affichant l'Access Code à copier (section 2)
- Slide "Reconnexion sous 7 jours" + capture de la notification TikTok Feed Error (section 3)
- Section Source TikTok avec User Account Feed (section 4)
- Sous-section Views & Likes dans la section Feed (section 5)
- Settings → Feed Platforms → TikTok Settings, Clear Cache en vert schoolsWP (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP, annoncer les deux particularités
- Section 1 : insister visuellement sur le plugin compagnon, c'est ce qui surprend
- Section 3 : moment fort, slide claire + face camera pour la règle des 7 jours
- Sections 4 et 5 : screencast dans l'éditeur de template
- Outro : face camera, bilan des cinq feeds + CTA vers la leçon 2.8

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Plugin compagnon | 1:00 |
| Section 2 - Connexion par code | 1:00 |
| Section 3 - Règle des 7 jours | 1:15 |
| Section 4 - Configurer le template | 1:00 |
| Section 5 - Filtres et social proof | 1:15 |
| Section 6 - Réglages globaux | 0:45 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__tiktok-feed-activation.md`
- Doc : `sources/docs/guide__social-feeds__tiktok-feed-configuration.md`
- Doc : `sources/docs/guide__social-feeds__tiktok-feed-template.md`
- Doc : `sources/docs/guide__social-feeds__tiktok-feed-settings.md`
- Vidéos officielles : #67 (Brand New TikTok Feed Plugin 2025), #83 (Embed TikTok Feed FOR FREE)

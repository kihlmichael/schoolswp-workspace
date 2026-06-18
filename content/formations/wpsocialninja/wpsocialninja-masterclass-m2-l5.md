# Leçon 2.5 - Instagram feed : setup, business/basic, shoppable, RGPD

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter un compte Instagram professionnel à WP Social Ninja en choisissant entre Business Basic et Business Advanced, configurer le feed (layout, filtres, hashtags), activer un feed shoppable, et mettre le tout en conformité RGPD.
- **Prérequis** : Leçon 2.1 terminée. Un compte Instagram professionnel (Business ou Creator), pas un compte personnel.

---

## Script narration

**[INTRO - face camera]**

Instagram, c'est le feed visuel par excellence. Mais c'est aussi celui qui a changé récemment, alors commençons par le point qui bloque le plus de monde : depuis fin 2024, Instagram ne supporte plus les comptes personnels pour les feeds. Il te faut un compte professionnel, Business ou Creator.

Dans cette leçon, on voit comment convertir ton compte si besoin, le choix entre Business Basic et Business Advanced, le setup, puis deux fonctions fortes : le feed shoppable pour vendre, et la conformité RGPD pour rester carré côté données. C'est parti.

---

**[SECTION 1 - Le prérequis : un compte professionnel]**

**[ECRAN - slide "Compte personnel → Business / Creator"]**

D'abord le prérequis incontournable. Depuis le 4 décembre 2024, l'ancienne API pour comptes personnels est arrêtée. Pour afficher un feed Instagram, ton compte doit être professionnel : soit Business, soit Creator. Les deux fonctionnent avec le plugin.

Si tu es encore en compte personnel, la conversion se fait dans Instagram : Settings and Privacy, puis Account Type and Tools, puis Switch to Professional Account. Tu choisis Business ou Creator, une catégorie qui correspond à ton activité, et tu complètes les infos demandées.

Et garde ce réflexe : après conversion, tu devras reconnecter ton compte au plugin, parce que l'accès API a changé.

---

**[SECTION 2 - Business Basic ou Business Advanced]**

**[ECRAN - popup Instagram → dropdown Account Type]**

Au moment de connecter, WP Social Ninja te propose trois options : Business Basic, Business Advanced, et Account Manually. Le vrai choix se joue entre Basic et Advanced. Voyons les trois différences qui comptent.

Première différence, la méthode de connexion. Business Basic se connecte directement via Instagram, avec ton identifiant. Business Advanced passe par Facebook et demande donc une page Facebook liée.

Deuxième différence, le contenu. Business Basic affiche tes posts, ton profil, tes avatars. Mais il ne gère pas les feeds de hashtags ni les mentions. Business Advanced, lui, débloque les hashtags et les mentions.

Troisième différence, le nombre de comptes. Business Basic gère un seul compte Instagram. Business Advanced en gère plusieurs.

La règle simple : si tu veux juste afficher les posts d'un compte, Business Basic suffit. Si tu veux des feeds de hashtags ou plusieurs comptes, prends Business Advanced.

---

**[SECTION 3 - Connecter le compte]**

**[ECRAN - bouton Connect with Instagram / Connect with Facebook]**

Passons à la connexion. Pour Business Basic : tu sélectionnes l'option, tu cliques sur Connect with Instagram, tu te connectes à ton compte Business, tu cliques sur Allow pour accorder les permissions. Ton compte est ajouté.

Pour Business Advanced : même départ, mais tu cliques sur Connect with Facebook. Tu te connectes à Facebook, tu accordes les permissions avec Continue as, et ton compte Advanced est ajouté.

Il existe aussi l'option Account Manually : tu génères un Access Token et un User ID depuis le générateur officiel, et tu les colles dans le plugin. C'est l'équivalent du token Facebook qu'on a vu en leçon 2.4.

Petit dépannage, identique à Facebook : si ton compte n'apparaît pas après une connexion Advanced, supprime l'ancienne app WP Social Ninja dans tes Business Integrations Facebook, puis reconnecte. Et souviens-toi de la règle Meta : supprimer une app déconnecte le token sur tous les sites.

---

**[SECTION 4 - Configurer le feed]**

**[ECRAN - éditeur de template Instagram → onglet General → section Accounts]**

Une fois connecté, Add New Template, et on configure. Section Accounts, le Feed Type. User Account Feed affiche les posts de ton profil, c'est le choix courant. Hashtag Feed affiche les posts publics portant un hashtag donné, par exemple celui d'un concours. Rappel : le Hashtag Feed exige Business Advanced.

**[ECRAN - sections Layout, Filters, Post]**

Côté Layout, tu retrouves Grid, Carousel et Masonry, avec les colonnes par appareil. Côté Filters, le nombre de posts affichés, l'ordre, les filtres Show et Hide par mots-clés, et le masquage de posts précis.

Et dans la section Post, un réglage propre à Instagram : l'Image Aspect Ratio. Tu choisis la forme de tes images : Original, carré, paysage, ou portrait. Très utile pour garder une grille homogène. Tu règles aussi l'ouverture au clic, popup ou Instagram, et l'affichage de la légende, des likes et des commentaires.

---

**[SECTION 5 - Le feed shoppable]**

**[ECRAN - section Shoppable Feed Settings → Enable Shoppable Feed]**

Voici une fonction qui transforme ta vitrine en canal de vente : le feed shoppable. L'idée : rendre tes posts cliquables vers tes pages produit.

Tu actives Enable Shoppable Feed. Dès lors, un bouton Add apparaît sur chaque post dans l'aperçu. Tu as deux méthodes pour ajouter les liens.

Méthode manuelle : tu cliques sur Add sur un post, une popup s'ouvre, tu choisis la source du lien : un article, une page, un produit, ou une URL personnalisée, par exemple un lien d'affiliation. Tu écris le texte du bouton, comme "Voir le produit", et tu valides. Contrôle total, post par post.

Méthode automatique : tu actives Include Shoppable by Hashtags, puis tu configures des règles qui associent un hashtag à un lien. Par exemple, le hashtag bluehat25 pointe automatiquement vers la page produit du chapeau bleu. Dès que tu publies un post avec ce hashtag, le lien se crée tout seul sur ton site.

Dernier réglage, Display Shoppable Icon : ajoute une petite icône de panier sur les posts cliquables, pour que le visiteur comprenne qu'il peut acheter. À noter : un lien manuel l'emporte toujours sur un lien automatique par hashtag pour le même post.

---

**[SECTION 6 - La conformité RGPD]**

**[ECRAN - WP Social Ninja → Settings → Advanced Settings → GDPR Compliance]**

Terminons par un point qu'on néglige trop souvent, surtout en France : le RGPD. Par défaut, un feed Instagram charge les images depuis les serveurs d'Instagram, ce qui transfère des données vers un tiers.

Pour être conforme, deux réglages. D'abord, dans Settings, Advanced Settings, tu actives la GDPR Compliance en choisissant Yes. Ensuite, dans Settings, Feed Platforms, Instagram Settings, tu actives Optimize Images. Cette option stocke les images en local sur ton serveur WordPress, ce qui est compatible RGPD.

Sois conscient des limites une fois le RGPD activé. Les images ne viennent plus du CDN d'Instagram, seules les images locales s'affichent. Les vidéos renvoient vers le post Instagram d'origine, aucune donnée vidéo n'est traitée par le plugin. Et dans la lightbox, seule la première image d'un post carrousel s'affiche.

**[FACE CAMERA]**

Pour un site français, ce n'est pas optionnel. Active le RGPD et l'optimisation des images dès le départ. Tu acceptes une petite limite d'affichage, tu gagnes la tranquillité côté conformité.

---

**[OUTRO - face camera]**

Tu sais maintenant connecter Instagram en compte professionnel, choisir entre Basic et Advanced, configurer ton feed, le rendre shoppable, et le mettre en conformité RGPD. Dans la prochaine leçon, on passe à X, anciennement Twitter, avec sa connexion par Bearer Token et ses réglages de styling. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Slide "Compte personnel → Business / Creator" + parcours de conversion dans Instagram (section 1)
- Dropdown Account Type avec Basic / Advanced / Manually (section 2)
- Slide comparatif Basic vs Advanced : connexion, contenu, nombre de comptes (section 2)
- Boutons Connect with Instagram et Connect with Facebook (section 3)
- Section Post avec Image Aspect Ratio déployé (section 4)
- Feed shoppable : bouton Add sur un post + popup Add Promotional URL (section 5)
- Settings → Advanced Settings → GDPR Compliance (Yes) + Optimize Images dans Instagram Settings (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP, insister sur "compte professionnel obligatoire"
- Sections 1 à 5 : alternance screencast et slides Kadence
- Section 2 : slide comparatif clair, c'est la décision structurante de la leçon
- Section 6 : retour face camera sur l'enjeu RGPD français
- Outro : face camera, CTA visuel vers la leçon 2.6

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Compte professionnel | 1:15 |
| Section 2 - Basic vs Advanced | 1:30 |
| Section 3 - Connecter le compte | 1:15 |
| Section 4 - Configurer le feed | 1:15 |
| Section 5 - Feed shoppable | 1:45 |
| Section 6 - RGPD | 1:15 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__instagram-configuration.md`
- Doc : `sources/docs/guide__social-feeds__instagram-business-basic.md`
- Doc : `sources/docs/guide__social-feeds__convert-your-instagram-personal-account-into-professional-account.md`
- Doc : `sources/docs/guide__social-feeds__instagram-setup.md`
- Doc : `sources/docs/guide__social-feeds__instagram-shoppable-feed.md`
- Doc : `sources/docs/guide__social-feeds__instagram-gdpr-compliance.md`
- Doc : `sources/docs/guide__social-feeds__instagram-feed-settings.md`
- Vidéos officielles : #25 (How to fetch Instagram Feeds), #33 (Make Your Instagram Feed Cool), #79 (Embed Instagram Posts)

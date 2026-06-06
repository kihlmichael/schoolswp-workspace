# Leçon 3.6 - Avis maison : formulaires natifs, sources custom, QR code

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Collecter et gérer ses propres avis sans dépendre d'une plateforme tierce : créer un formulaire natif, monter une source custom (ajout manuel ou import CSV), et générer un QR code qui mène à la page d'avis pour récolter des retours sur le terrain.
- **Prérequis** : Leçon 3.1 vue (tableau Reviews et modération). Pour la source custom et le QR code Pro, WP Social Ninja Pro.

---

## Script narration

**[INTRO - face camera]**

Jusqu'ici, on a ramené sur ton site des avis qui existaient ailleurs. Dans cette leçon, on change de logique : tu vas collecter tes propres avis, directement chez toi, sans dépendre de Google ou de Facebook.

Trois outils pour ça. Le formulaire natif, intégré au plugin, pour que tes visiteurs laissent un avis directement sur ton site. Les sources custom, pour entrer manuellement ou importer en masse des avis que tu as déjà. Et le QR code, pour récolter des retours sur le terrain, à la caisse ou sur une table de restaurant. On commence par le formulaire natif.

---

**[SECTION 1 - Le formulaire natif : collecter sans plugin tiers]**

**[ECRAN - WP Social Ninja → Review Forms → + Create Form]**

Le formulaire natif est un outil intégré : pas besoin d'un plugin de formulaire externe. Tes clients soumettent une note, un texte, et même des photos, et tout arrive directement dans ton tableau de modération.

Tu vas dans WP Social Ninja, puis Review Forms, et tu cliques sur Create Form.

**[ECRAN - éditeur, onglet Form Display : titre, sous-titre, style de note]**

L'éditeur s'ouvre. Dans l'onglet Form Display, tu règles l'apparence : un titre comme Laissez un avis, un sous-titre, et le style de la note. Tu as le choix entre étoiles, cœur, emoji ou nombre.

**[ECRAN - onglet Form Fields : nom, e-mail, note, titre, texte, photos, RGPD]**

Dans l'onglet Form Fields, tu choisis les informations à demander : le nom, l'e-mail, la note, un titre d'avis, le texte de l'avis, et l'upload de photos pour une vraie preuve visuelle. Tu peux aussi ajouter une case de consentement à ta politique de confidentialité, ce qui est précieux côté RGPD. Pour chaque champ : afficher ou masquer, modifier le libellé, rendre obligatoire.

**[ECRAN - onglet General Settings : Review Target + Submission Rules]**

L'onglet General Settings contient un réglage important : le Review Target, qui indique à quoi se rattachent ces avis. Tu peux choisir un formulaire natif générique pour des témoignages, un produit FluentCart, ou un produit WooCommerce. Tu y gères aussi des règles comme exiger une connexion ou un seul avis par e-mail.

**[ECRAN - onglet Spam Protection : Turnstile]**

Pense à l'onglet Spam Protection : pour une protection renforcée, tu peux activer Turnstile, en renseignant ta clé de site et ta clé secrète.

**[ECRAN - barre du haut, shortcode du formulaire, bouton Copy]**

Une fois Save cliqué, le formulaire est prêt. Tu récupères son shortcode en haut de l'éditeur, du type wpsr_review_form id égale deux, tu le copies, et tu le colles sur la page où tu veux ton formulaire. Tous les avis reçus arriveront dans ton tableau Reviews, en Approved ou en Pending selon tes réglages globaux.

---

**[SECTION 2 - Les sources custom : tes avis existants]**

**[ECRAN - WP Social Ninja → Custom Sources → + Add Source]**

Deuxième outil : les sources custom. Elles te laissent créer tes propres plateformes d'avis à l'intérieur du plugin. Idéal pour des avis que tu as déjà : un client t'a écrit un e-mail élogieux, ou tu as des retours collectés hors ligne.

Tu vas dans Custom Sources, puis Add Source. Une fenêtre te demande le type de source. Pour des avis existants, tu choisis Custom, tu donnes un nom parlant, par exemple Témoignages site, puis Create Source.

**[ECRAN - dashboard de la source, bouton + Add Custom Review]**

Tu as deux façons d'ajouter tes avis. La première, manuellement, un par un, avec le bouton Add Custom Review. Un formulaire détaillé apparaît : nom du client, lien éventuel, photo, titre, texte, date et note. Tu enregistres, et l'avis rejoint ta liste.

**[ECRAN - bouton Import, Download Sample CSV]**

La seconde, par import CSV, parfaite pour ajouter des dizaines d'avis d'un coup. Tu cliques sur Import, tu choisis le type Custom Sources Reviews, et surtout tu télécharges le modèle avec Download Sample CSV. Tu remplis le fichier en gardant bien les en-têtes de colonnes comme reviewer_name, rating et review_text, tu l'enregistres et tu l'importes.

**[ECRAN - General Settings de la source : logo, label, lien]**

Petit plus marque : dans les réglages de la source, tu peux ajouter un logo, un libellé et un lien, pour que ta source custom ait une vraie identité dans tes modèles. Et bien sûr, ta source custom devient une plateforme cochable dans l'éditeur de modèle, comme Google ou Facebook.

---

**[SECTION 3 - Le QR code : récolter des avis sur le terrain]**

**[ECRAN - WP Social Ninja → Settings → Get Reviews via QR Code]**

Troisième outil, et il est malin : le QR code. Il génère un code unique qui mène directement à ta page d'avis sur une plateforme connectée, par exemple ta fiche Google ou Booking.com. Ton client scanne, et il laisse un avis sans avoir à chercher ta page.

Prérequis : avoir déjà connecté tes plateformes, puisque tu vas choisir une de leurs URL. Tu vas dans WP Social Ninja, Settings, puis le sous-menu Get Reviews via QR Code.

**[ECRAN - + Add New QR Code, nom + Business URL + Generate]**

Tu cliques sur Add New QR Code. Tu donnes un nom pour le retrouver, tu sélectionnes sous Business URL la plateforme cible, et tu cliques sur Generate.

**[ECRAN - QR code affiché, boutons PNG et SVG]**

Le QR code s'affiche. Tu le télécharges en PNG ou en SVG. Tu peux ensuite le poser partout : cartes de visite, flyers, tables de restaurant, comptoir de caisse, signature d'e-mail.

**[FACE CAMERA]**

Et un détail que j'aime bien : le plugin compte le nombre de scans, dans la colonne Total Scans du tableau. Ça te dit concrètement si ton QR code, à cet emplacement, donne envie aux clients de laisser un avis. C'est une vraie mesure, pas une promesse.

---

**[SECTION 4 - L'alternative Fluent Forms, en un mot]**

**[ECRAN - slide "3 façons de collecter : Custom / Native Form / Fluent Forms"]**

Pour être complet, sache qu'il existe une troisième façon de collecter des avis : connecter un Fluent Form. Quand tu crées une source custom, le plugin te propose justement trois types : Custom pour tes avis existants, Native Review Form pour le formulaire intégré qu'on vient de voir, et Fluent Forms pour collecter via un formulaire Fluent Forms.

Cette voie Fluent Forms, plus avancée et en version Pro, permet des champs sur mesure et de collecter des avis au-delà des produits, par exemple pour une formation ou un service. On la détaillera dans le Module 6, consacré aux intégrations. Pour aujourd'hui, retiens les trois outils maison : formulaire natif, source custom, QR code.

---

**[OUTRO - face camera]**

Tu sais maintenant collecter tes propres avis de trois façons : le formulaire natif intégré, les sources custom par ajout manuel ou import CSV, et le QR code pour le terrain avec son compteur de scans. Dans la dernière leçon du module, on rassemble tout : le styling des avis, le schema des étoiles en pratique, et l'usage avec les page builders. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Review Forms : bouton Create Form (section 1)
- Éditeur formulaire : onglets Form Display (style de note) et Form Fields (champs + photos) (section 1)
- General Settings : menu déroulant Review Target (Native / FluentCart / WooCommerce) (section 1)
- Spam Protection : Turnstile (section 1)
- Shortcode du formulaire dans la barre du haut (section 1)
- Custom Sources : Add Source → choix Custom → nommage (section 2)
- Add Custom Review (formulaire détaillé) + Import → Download Sample CSV (section 2)
- General Settings de la source : logo, label, lien (section 2)
- QR Code : Settings → Get Reviews via QR Code → Add New QR Code → Generate (section 3)
- QR code affiché + boutons PNG/SVG + colonne Total Scans (section 3)
- Slide "3 façons de collecter" : Custom / Native Form / Fluent Forms (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast Review Forms, suivre les onglets dans l'ordre
- Section 2 : screencast Custom Sources, montrer les deux méthodes manuel / CSV
- Section 3 : screencast QR code, montrer un QR scanné par un smartphone en surimpression
- Section 3 fin : face camera sur le compteur Total Scans (mesure réelle)
- Section 4 : slide récap des 3 types de source, teaser Module 6 pour Fluent Forms
- Outro : face camera, CTA visuel vers la leçon 3.7

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Formulaire natif | 2:45 |
| Section 2 - Sources custom | 2:30 |
| Section 3 - QR code | 2:00 |
| Section 4 - Alternative Fluent Forms | 0:55 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__native-review-forms.md`
- Doc : `sources/docs/guide__custom-source__custom-source-overview.md`
- Doc : `sources/docs/guide__custom-source__manually-add-or-import-custom-reviews.md`
- Doc : `sources/docs/guide__business-reviews__generate-qr-code-for-reviews.md`
- Doc : `sources/docs/guide__business-reviews__collect-woocommerce-custom-reviews-with-fluent-forms.md`
- Vidéos officielles : #18 (Add Custom Reviews from Website Visitors), #46 (Add Custom Reviews on WordPress), #85 (Collect Reviews from Custom Sources)

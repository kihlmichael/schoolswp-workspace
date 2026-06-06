# Leçon 4.5 - Multi-chat, bouton custom et cohérence de marque

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 4 - Social Chat
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Réunir plusieurs canaux dans un même widget, déclencher la chat box depuis un bouton custom posé n'importe où sur une page, et verrouiller la cohérence de marque du widget de bout en bout.
- **Prérequis** : Leçons 4.2 à 4.4 vues (un ou plusieurs canaux configurés, onglets General et Style connus).

---

## Script narration

**[INTRO - face camera]**

On clôt le module Social Chat en assemblant les pièces. Jusqu'ici, on a branché les canaux un par un. Maintenant, on va les réunir dans un seul widget multi-chat, apprendre à ouvrir la fenêtre depuis un bouton placé dans ta page, et faire le point sur la cohérence de marque.

Trois objectifs, donc : le multi-chat, le bouton custom, et la touche finale qui rend le widget vraiment tien. On y va.

---

**[SECTION 1 - Réunir plusieurs canaux dans un widget]**

**[FACE CAMERA]**

C'est tout l'intérêt de WP Social Ninja : un seul bouton flottant, plusieurs portes d'entrée derrière. Plutôt que de te limiter à un chat unique, tu regroupes plusieurs messageries dans un même bouton, et le visiteur choisit la sienne.

**[ECRAN - éditeur du chat, onglet Channels, ajout successif de WhatsApp, Messenger, Telegram]**

Concrètement, dans l'onglet Channels de ton widget, tu cliques sur "+Add New Channel" autant de fois que de canaux à ajouter. Par exemple WhatsApp, puis Messenger, puis Telegram. Chaque canal s'empile dans la liste, et chacun garde ses propres icônes Edit et Delete pour le modifier ou le retirer.

**[ECRAN - onglet General, section Template, choix du Layout Type]**

Un réglage compte pour le rendu : le Layout Type, dans la section Template de l'onglet General. Le défaut, c'est Chat Box, une interface de chat complète où le visiteur voit tes canaux listés. L'autre option, c'est Only Icon, qui n'affiche que l'icône de chat. À côté, tu peux choisir un Template prêt à l'emploi : General, Support ou Feedback, chacun avec son jeu de couleurs et sa mise en page de départ.

**[FACE CAMERA]**

Mon conseil sur le multi-chat : ne mets pas tous les canaux possibles. Deux ou trois portes claires valent mieux qu'une grille de dix icônes qui noie le visiteur. Choisis celles que tu surveilles vraiment.

---

**[SECTION 2 - Ouvrir le chat depuis un bouton custom]**

**[FACE CAMERA]**

Passons à une fonction pratique. La bulle flottante est utile, mais parfois tu veux ouvrir le chat depuis un bouton placé dans ton contenu, par exemple un bouton "Nous contacter" au milieu d'une page d'offre. C'est possible, et ça reste simple.

**[ECRAN - note "Prérequis : widget et canaux déjà configurés"]**

Une condition d'abord : ton widget et ses canaux doivent déjà être configurés. Ce bouton custom ne crée rien, il déclenche le widget existant et actif.

**[ECRAN - WordPress → Pages → édition d'une page, ajout d'un bloc Buttons]**

La marche à suivre tient en quatre étapes. Étape une, tu ouvres la page concernée dans WordPress, ou tu en crées une nouvelle. Étape deux, dans l'éditeur, tu cliques sur le plus pour ajouter un bloc, tu tapes "Button" et tu choisis le bloc Buttons. Tu personnalises le texte du bouton, par exemple "Nous contacter".

**[ECRAN - panneau Block → Advanced → champ "Additional CSS class(es)" avec wpsn_chat_opener]**

Étape trois, la plus importante. Tu cliques sur le bouton pour le sélectionner, tu vas dans l'onglet Block du panneau de droite, tu ouvres la section Advanced, et tu trouves le champ "Additional CSS class(es)". Dans ce champ, tu écris exactement cette classe : wpsn underscore chat underscore opener. C'est elle qui relie ton bouton au widget de chat.

**[ECRAN - clic Update, test sur la page live, ouverture de la chat box]**

Étape quatre, tu cliques sur Update ou Publish pour enregistrer. Tu visites ensuite la page en ligne et tu cliques sur ton bouton : la fenêtre de chat s'ouvre, prête à accueillir le visiteur.

**[FACE CAMERA]**

C'est une astuce que j'aime bien : tu gardes ta bulle flottante pour le contact général, et tu poses un bouton custom au bon endroit dans une page clé, là où le visiteur est le plus chaud.

---

**[SECTION 3 - Verrouiller la cohérence de marque]**

**[ECRAN - onglet Style, color pickers]**

On finit par la cohérence visuelle, parce que c'est ce qui fait la différence entre un outil tiers et une vraie partie de ton site. Tu connais déjà l'onglet Style vu en 4.2 : tu y règles le fond de l'en-tête, la couleur du titre, celle de la légende, le fond des icônes de canaux, le fond du bouton flottant et la couleur de la croix de fermeture. Reprends tes couleurs de marque exactes, pas une teinte approchante.

**[ECRAN - onglet General, section Chat Bubble Button : icône et upload custom]**

Pousse la marque jusqu'au bouton flottant lui-même, dans la section Chat Bubble Button de l'onglet General. Tu choisis une icône dans la galerie, ou mieux, tu téléverses ta propre icône avec "Upload Custom Icon" pour un rendu unique. Tu peux aussi ajouter un Bubble Text à côté de l'icône, du type "Une question ?".

**[ECRAN - slide checklist cohérence de marque]**

Faisons une petite checklist de cohérence avant publication. Les couleurs du widget reprennent celles du site. L'en-tête affiche ton nom et ton logo. Le message d'accueil sonne juste, dans ton ton. La position de la bulle ne gêne aucun élément important. Et les canaux affichés sont ceux que tu surveilles vraiment.

**[FACE CAMERA]**

Quand ces cinq points sont cochés, le widget ne ressemble plus à un module ajouté : il fait partie de ton site. C'est exactement l'objectif. Pour schoolsWP, ça veut dire le vert de marque sur le bouton flottant et un accueil au tutoiement, fidèle à la voix du site.

---

**[OUTRO - face camera]**

Tu sais maintenant réunir plusieurs canaux dans un widget multi-chat, déclencher la fenêtre depuis un bouton custom avec la classe wpsn underscore chat underscore opener, et verrouiller la cohérence de marque jusqu'à l'icône de la bulle. Ce module Social Chat est bouclé. Dans le module suivant, on passe aux Notifications popup, ces petites preuves d'activité qui rassurent le visiteur. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Onglet Channels avec plusieurs canaux empilés : WhatsApp, Messenger, Telegram, chacun avec Edit/Delete (section 1)
- Onglet General → section Template → dropdown Layout Type (Chat Box / Only Icon) + templates General/Support/Feedback (section 1)
- Note "Prérequis : widget et canaux déjà configurés" (section 2)
- WordPress → Pages → ajout du bloc Buttons et personnalisation du texte (section 2)
- Panneau Block → Advanced → champ "Additional CSS class(es)" avec wpsn_chat_opener saisi - point clé (section 2)
- Test sur page live : clic sur le bouton custom, ouverture de la chat box (section 2)
- Onglet Style avec les color pickers (section 3)
- Onglet General → section Chat Bubble Button : galerie d'icônes + Upload Custom Icon + Bubble Text (section 3)
- Slide checklist cohérence de marque, 5 points, accents schoolsWP en vert (section 3)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast de l'empilement des canaux + slide rapide Layout Type
- Section 2 : ralentir sur la saisie de la classe CSS wpsn_chat_opener, c'est le point de friction de la leçon ; courte démo front du clic sur le bouton custom
- Section 3 : alternance screencast (Style et Bubble Button) et slide checklist finale
- Outro : face camera, CTA visuel vers le Module 5 (Notifications)

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Multi-chat | 2:00 |
| Section 2 - Bouton custom | 2:30 |
| Section 3 - Cohérence de marque | 1:45 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__social-chat__chat-widget-configuration.md` (ajout de plusieurs canaux)
- Doc : `sources/docs/guide__social-chat__chat-settings.md` (Template / Layout Type, Chat Bubble Button)
- Doc : `sources/docs/guide__social-chat__chat-styling.md` (couleurs et cohérence de marque)
- Doc : `sources/docs/guide__social-chat__add-custom-button-chat-widget.md` (bouton custom, classe wpsn_chat_opener)
- Vidéos officielles : #54 (Integrate Multiple Chat Widget), #27 (Style your Chat Widget to match your brand)

# Leçon 4.4 - Telegram et Viber

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 4 - Social Chat
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Ajouter les canaux Telegram et Viber à un widget WP Social Ninja, comprendre la différence d'identifiant entre les deux, et régler les boutons de canaux ainsi que les règles d'affichage du widget.
- **Prérequis** : Leçons 4.2 et 4.3 vues (création d'un widget, ajout de canaux, onglet General).

---

## Script narration

**[INTRO - face camera]**

On continue le tour des messageries avec deux canaux qui comptent selon ton audience : Telegram et Viber. Telegram est apprécié des communautés tech et des créateurs, Viber est très présent dans certains pays d'Europe de l'Est et d'Asie.

La bonne nouvelle, c'est que tu connais déjà le geste : on ajoute un canal, on renseigne un identifiant, on enregistre. Dans cette leçon, on configure les deux, on note la petite différence entre un nom d'utilisateur et un numéro, et on termine par les réglages des boutons et les règles d'affichage du widget. On y va.

---

**[SECTION 1 - Configurer Telegram]**

**[ECRAN - éditeur du chat, "+Add New Channel", clic sur l'icône Telegram]**

On commence par Telegram. Dans l'onglet Channels de ton widget, tu cliques sur "+Add New Channel", puis tu sélectionnes l'icône Telegram.

**[ECRAN - champ "Telegram User ID or Profile Link", champ Label, Save]**

Un champ apparaît : "Telegram User ID or Profile Link". Tu y mets ton identifiant utilisateur Telegram, ou bien le lien vers ton profil. Comme pour les autres canaux, le champ Label te laisse personnaliser le nom affiché du bouton. Tu cliques sur Save.

**[ECRAN - canal Telegram ajouté]**

Après l'enregistrement, ton bouton Telegram apparaît sur le site. Le visiteur peut te contacter directement via l'application Telegram. Et comme partout, tu peux modifier ou supprimer le canal avec les icônes Edit et Delete.

**[FACE CAMERA]**

Retiens que Telegram fonctionne avec un nom d'utilisateur, pas un numéro de téléphone. C'est la différence à garder en tête avec Viber, qu'on voit tout de suite.

---

**[SECTION 2 - Configurer Viber]**

**[ECRAN - éditeur du chat, "+Add New Channel", clic sur l'icône Viber]**

Passons à Viber. Même point de départ : tu cliques sur "+Add New Channel" et tu sélectionnes l'icône Viber.

**[ECRAN - champ numéro mobile Viber avec indicatif pays, champ Label, Save]**

Là, le champ change de logique. Viber te demande ton numéro de mobile, avec l'indicatif pays inclus. C'est donc comme WhatsApp, et pas comme Telegram : ici, c'est bien un numéro, pas un nom d'utilisateur. N'oublie pas l'indicatif, sinon la redirection échoue. Tu personnalises le Label si tu veux, et tu cliques sur Save.

**[ECRAN - canal Viber ajouté, redirection front vers une conversation Viber]**

Une fois connecté, une icône Viber apparaît sur ton site. Quand un visiteur clique dessus, il est redirigé directement vers une conversation Viber avec toi. Modification et suppression toujours possibles via Edit et Delete.

**[ECRAN - slide récap "Telegram : nom d'utilisateur / Viber : numéro + indicatif"]**

Récapitulons la différence, parce que c'est ça qui se confond. Telegram : un nom d'utilisateur ou un lien de profil. Viber : un numéro de mobile avec l'indicatif pays. Garde ce repère, il t'évitera un canal qui ne pointe nulle part.

---

**[SECTION 3 - Boutons de canaux et règles d'affichage]**

**[ECRAN - onglet General, section Channel Buttons]**

Maintenant qu'on empile plusieurs canaux, voyons deux réglages qui s'appliquent à l'ensemble. Direction l'onglet General.

D'abord, la section Channel Buttons, qui pilote les boutons à l'intérieur de la fenêtre de chat. Tu peux y régler quatre choses : afficher ou non la petite icône de chat avec Display Chat Icon, personnaliser le texte du bouton d'action principal avec Chat Button Text, activer un message pré-rempli avec Prefilled Message pour que le visiteur n'ait qu'à l'envoyer, et définir le texte d'invite du champ de saisie avec Prefilled Input Placeholder Text.

**[ECRAN - onglet General, section affichage : Include Pages, Exclude Pages, position]**

Ensuite, le réglage le plus important : où et comment ton widget apparaît. Quelques options à connaître.

Chat Bubble Position : le coin de l'écran où se place la bulle, par exemple en bas à droite ou en bas à gauche.

Include Pages to Display Chat : tu choisis "Everywhere" pour l'afficher partout, c'est le réglage par défaut, ou "Specific Pages/Posts" pour cibler des pages précises.

Exclude Pages to Hide Chat : à l'inverse, tu masques le widget sur certaines pages, même s'il s'affiche partout ailleurs.

Et deux interrupteurs pratiques : Hide Chat on Desktop et Hide Chat on Mobile, pour cacher le widget sur ordinateur ou sur mobile selon ton besoin.

**[FACE CAMERA]**

Un mot sur la langue, parce que c'est une source de bugs. Le widget reprend la langue de ton site WordPress. Donc il fonctionne correctement quand la langue du widget correspond à celle du site. Si ton site est multilingue, tu dois passer par un plugin comme Polylang, WPML ou TranslatePress pour que le widget s'adapte à chaque langue. Sur un site multilingue, c'est le réflexe à ne pas zapper.

---

**[OUTRO - face camera]**

Tu sais maintenant ajouter Telegram et Viber, avec le bon repère : nom d'utilisateur pour l'un, numéro avec indicatif pour l'autre. Et tu maîtrises les boutons de canaux et les règles d'affichage, qui valent pour tous tes canaux. Dans la dernière leçon du module, on assemble tout : plusieurs canaux dans un même widget, un bouton custom déclenché depuis ta page, et la cohérence de marque d'un bout à l'autre. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Onglet Channels → "+Add New Channel" → icône Telegram (section 1)
- Champ "Telegram User ID or Profile Link" + champ Label (section 1)
- Onglet Channels → "+Add New Channel" → icône Viber (section 2)
- Champ numéro mobile Viber avec indicatif pays - insister visuellement sur l'indicatif (section 2)
- Slide récap "Telegram = nom d'utilisateur / Viber = numéro + indicatif" (section 2)
- Onglet General → section Channel Buttons avec ses 4 réglages (section 3)
- Onglet General → réglages d'affichage : Include Pages, Exclude Pages, position, Hide on Desktop/Mobile (section 3)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 et 2 : screencast, clics réels, ralentir sur la saisie de l'indicatif pays pour Viber
- Section 2 : slide récap de la différence d'identifiant Telegram vs Viber - point à marquer
- Section 3 : alternance screencast (onglet General) et incrustation des libellés
- Section 3 : retour face camera sur la note langue / multilingue, ton direct
- Outro : face camera, CTA visuel vers la leçon 4.5

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Telegram | 1:30 |
| Section 2 - Viber | 1:45 |
| Section 3 - Boutons et affichage | 2:50 |
| Outro | 0:20 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__social-chat__chat-widget-configuration.md` (Telegram Configuration, Viber Configuration)
- Doc : `sources/docs/guide__social-chat__chat-settings.md` (Channel Buttons, règles d'affichage, Chat Language / multilingue)
- Vidéos officielles : #75 (Connect Telegram Chat Plugin), #84 (Add Viber Chat Widget in 5 Minutes)

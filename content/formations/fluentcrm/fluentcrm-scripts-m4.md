# Scripts video — Module 4 : Fluent Forms — generer des leads

**Formation** : Maitriser FluentCRM
**Module** : M4 — Fluent Forms : generer des leads (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~50 min
**Date** : 2026-03-23

---

### Lecon 4.1 — Installe et decouvre Fluent Forms

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de l'installation et de l'interface

---

**[INTRO — face camera]**

FluentCRM gere tes contacts et tes automations. Mais pour alimenter ta base, tu as besoin de formulaires. Et le meilleur partenaire de FluentCRM pour ca, c'est Fluent Forms. Meme editeur, meme ecosysteme, integration native. Dans cette lecon, on installe Fluent Forms et on fait le tour de l'interface.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

Pour installer Fluent Forms, va dans Extensions, puis Ajouter. Tape "Fluent Forms" dans la barre de recherche. Tu verras "Fluent Forms — Contact Form Builder" par WPManageNinja. C'est le meme editeur que FluentCRM. Clique sur Installer, puis Activer.

[Montre le plugin dans la liste avec le bouton Activer]

La version gratuite suffit pour creer des formulaires basiques et les connecter a FluentCRM. Mais pour les fonctionnalites qu'on va utiliser dans ce module — logique conditionnelle avancee, champs personnalises, integration complete — tu auras besoin de Fluent Forms Pro.

**[ECRAN — screencast menu Fluent Forms]**

[Montre le nouveau menu "Fluent Forms" dans la barre laterale WordPress]

Une fois active, un nouveau menu apparait dans la barre laterale : "Fluent Forms". Clique dessus. Tu arrives sur le tableau de bord principal.

[Vue du dashboard Fluent Forms]

L'interface est organisee en plusieurs sections. "All Forms" — la liste de tous tes formulaires. C'est ton point de depart. "New Form" — le bouton pour creer un nouveau formulaire. "Entries" — toutes les soumissions recues, triees par formulaire. Et "Settings" — les reglages globaux.

**[ECRAN — screencast galerie de templates]**

[Clique sur "New Form" pour voir les templates]

Clique sur "New Form". Fluent Forms te propose une galerie de templates preconstruits. Formulaire de contact, inscription newsletter, demande de devis, inscription evenement — il y en a des dizaines. Tu peux aussi partir d'un formulaire vierge.

Pour l'instant, on ne cree rien. On explore.

**[ECRAN — screencast editeur de formulaire]**

[Ouvre un template pour montrer l'editeur]

Ouvre un template pour voir l'editeur. C'est un constructeur drag-and-drop. A gauche, les champs disponibles — texte, email, menu deroulant, cases a cocher, champs caches. Au centre, ton formulaire en construction. Tu glisses un champ, tu le deposes, tu le configures.

[Montre le glisser-deposer d'un champ]

Chaque champ a ses propres reglages : libelle, placeholder, champ obligatoire ou non, validation. On verra tout ca en detail dans la lecon suivante.

**[ECRAN — screencast onglet Settings du formulaire]**

[Montre les onglets du formulaire : Editor, Settings, Integration]

En haut du formulaire, trois onglets importants. "Editor" — la ou tu construis. "Settings" — les reglages du formulaire (confirmation, notifications, restrictions). Et "Integration" — c'est la qu'on connectera FluentCRM. On y reviendra dans la lecon 4.3.

**[TRANSITION — face camera]**

Fluent Forms est installe, tu connais l'interface. Dans la prochaine lecon, on cree ton premier formulaire de capture d'email — le formulaire qui va alimenter ta base FluentCRM.

---

**Points cles** :
- Fluent Forms = meme editeur que FluentCRM (WPManageNinja), integration native
- Version gratuite pour les bases, Pro pour logique conditionnelle et integration complete
- Interface : All Forms, Entries, Settings + editeur drag-and-drop
- 3 onglets par formulaire : Editor, Settings, Integration
- Galerie de templates pour demarrer rapidement

**Mots cles SEO** : installer Fluent Forms WordPress, Fluent Forms FluentCRM, formulaire WordPress capture email, Fluent Forms tutoriel

---

### Lecon 4.2 — Cree ton formulaire de capture d'email

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast creation formulaire complet

---

**[INTRO — face camera]**

Un formulaire de capture d'email, c'est la porte d'entree de ton tunnel. Quelqu'un arrive sur ton site, remplit le formulaire, et devient un contact dans FluentCRM. Simple en theorie. En pratique, chaque champ compte. Dans cette lecon, on cree ensemble un formulaire de capture optimise pour generer des leads.

**[ECRAN — screencast Fluent Forms > New Form]**

[Clique sur "New Form" puis "Blank Form"]

Va dans Fluent Forms, clique sur "New Form". Cette fois, on part d'un formulaire vierge. Clique sur "Blank Form".

[Montre le formulaire vierge dans l'editeur]

Tu arrives dans l'editeur avec un formulaire vide. Premiere chose : donne-lui un nom. En haut a gauche, clique sur le titre par defaut et renomme-le. Par exemple : "Lead Magnet — Guide LMS".

Ce nom est interne — tes visiteurs ne le verront pas. Mais toi, quand tu auras 15 formulaires, tu seras content de les retrouver.

**[ECRAN — screencast ajout champ Email]**

[Glisse le champ "Email" dans le formulaire]

Premier champ a ajouter : l'email. C'est le seul champ vraiment obligatoire pour un formulaire de capture. Dans la colonne de gauche, cherche "Email Address" et glisse-le dans le formulaire.

[Configure le champ Email]

Clique sur le champ pour le configurer. "Label" — c'est le libelle visible. Change-le en "Ton adresse email" pour rester dans le ton schoolsWP. "Placeholder" — le texte grise dans le champ. Mets quelque chose de concret : "prenom@exemple.fr". Active "Required" — ce champ est obligatoire, evidemment.

**[ECRAN — screencast ajout champ Prenom]**

[Glisse le champ "Name" dans le formulaire]

Deuxieme champ : le prenom. Pas le nom complet — le prenom. Ca te permettra de personnaliser tes emails dans FluentCRM.

Glisse le champ "Name Fields" dans le formulaire. Par defaut, il inclut prenom, nom et parfois le titre. On ne veut que le prenom. Clique sur le champ, puis desactive "Last Name" et tout le reste. Garde uniquement "First Name".

[Montre la configuration avec seulement First Name actif]

Renomme le libelle en "Ton prenom". Marque-le comme obligatoire.

**[ECRAN — screencast bouton de soumission]**

[Montre le bouton Submit en bas du formulaire]

Le bouton de soumission est ajoute automatiquement. Mais le texte par defaut — "Submit" — est trop generique. Clique dessus et change le texte en quelque chose de specifique a ton offre. Par exemple : "Telecharge le guide gratuit" ou "Recois la formation". Le texte du bouton doit dire ce que le visiteur obtient, pas ce qu'il fait.

**[ECRAN — screencast onglet Settings > Confirmation]**

[Clique sur l'onglet Settings du formulaire]

Va dans l'onglet "Settings" du formulaire. Section "Form Settings". Ici tu configures ce qui se passe apres la soumission.

[Montre les options de confirmation]

Trois options. "Same Page" — un message de confirmation s'affiche sur la meme page. "To a Page" — redirige vers une page de remerciement. "To a Custom URL" — redirige vers une URL specifique.

Mon conseil : redirige vers une page de remerciement dediee. Ca te permet de tracker les conversions dans Google Analytics, de proposer une offre complementaire, et de donner les instructions de telechargement.

Pour le message ou la page, sois clair : "Ton guide est en route. Verifie ta boite mail (et tes spams)."

**[ECRAN — screencast onglet Settings > Email Notifications]**

[Montre la section Email Notifications]

Section "Email Notifications". Par defaut, Fluent Forms t'envoie un email a chaque soumission. Utile au debut pour verifier que tout fonctionne. Tu pourras le desactiver plus tard quand le volume augmente.

Tu peux aussi configurer un email de confirmation envoye au visiteur. Mais attention : si tu connectes FluentCRM dans la lecon suivante, c'est FluentCRM qui gerera les emails de bienvenue. Evite les doublons.

**[ECRAN — screencast preview du formulaire]**

[Clique sur "Preview" pour voir le formulaire]

Clique sur "Preview" en haut a droite pour voir le rendu. Deux champs — prenom et email — un bouton clair. Rien de plus. Un formulaire de capture efficace est un formulaire court. Chaque champ supplementaire reduit le taux de conversion.

**[TRANSITION — face camera]**

Ton formulaire est cree. Deux champs, un bouton, un message de confirmation. Propre et efficace. Dans la prochaine lecon, on connecte ce formulaire a FluentCRM pour que chaque inscription cree automatiquement un contact avec le bon tag.

---

**Points cles** :
- Formulaire de capture = minimum de champs (email + prenom)
- Nommer les formulaires clairement (tu en auras plusieurs)
- Bouton de soumission : texte oriente benefice, pas "Submit"
- Confirmation : rediriger vers une page de remerciement (tracking + upsell)
- Eviter les doublons : email de confirmation via FluentCRM, pas Fluent Forms
- Moins de champs = meilleur taux de conversion

**Mots cles SEO** : creer formulaire capture email WordPress, Fluent Forms formulaire inscription, formulaire lead magnet WordPress, optimiser formulaire conversion

---

### Lecon 4.3 — Connecte Fluent Forms a FluentCRM (Integration Feed)

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast integration complete

---

**[INTRO — face camera]**

Tu as un formulaire. Tu as FluentCRM. Maintenant il faut que les deux se parlent. Quand quelqu'un remplit ton formulaire, son email et son prenom doivent arriver directement dans FluentCRM avec le bon tag et la bonne liste. C'est le role de l'Integration Feed. On le configure ensemble.

**[ECRAN — screencast Fluent Forms > formulaire > Integration]**

[Ouvre le formulaire cree dans la lecon precedente, onglet "Integration"]

Ouvre le formulaire qu'on a cree. Clique sur l'onglet "Integration" en haut. C'est ici que tu connectes Fluent Forms a des services externes — et FluentCRM en fait partie nativement.

[Montre la liste des integrations disponibles]

Tu vois une liste d'integrations disponibles. Cherche "FluentCRM". Clique dessus. Un nouveau "feed" d'integration se cree.

**[ECRAN — screencast configuration du feed FluentCRM]**

[Montre le formulaire de configuration du feed]

Le feed, c'est la regle de transfert entre ton formulaire et FluentCRM. Premiere chose : donne-lui un nom explicite. Par exemple : "Feed — Lead LMS vers FluentCRM". Ce nom est interne, mais quand tu auras plusieurs feeds sur plusieurs formulaires, tu seras content de t'y retrouver.

**[ECRAN — screencast mapping des champs]**

[Montre la section "Map Fields"]

Section "Map Fields" — c'est le coeur de la configuration. Tu fais correspondre chaque champ de ton formulaire a un champ contact dans FluentCRM.

[Montre le mapping Email → Email]

"Email" du formulaire → "Email" dans FluentCRM. C'est le seul mapping obligatoire. Sans ca, FluentCRM ne peut pas creer le contact.

[Montre le mapping Prenom → First Name]

"Prenom" du formulaire → "First Name" dans FluentCRM. Ca te permet d'utiliser la variable {first_name} dans tes emails pour personnaliser.

[Montre la liste deroulante des champs FluentCRM disponibles]

Si tu as des champs personnalises dans FluentCRM — par exemple "Source du lead" ou "Niveau" — tu peux les mapper ici aussi. Tout champ que tu as cree dans FluentCRM > Contacts > Custom Fields apparait dans cette liste.

**[ECRAN — screencast assignation de liste]**

[Montre la section "Lists"]

Section "Lists". Selectionne la liste dans laquelle le contact sera ajoute. Par exemple, ta liste "Newsletter" ou "Leads formation LMS". Si tu n'as pas encore de liste adaptee, retourne dans FluentCRM > Contacts > Lists et cree-en une d'abord.

Un contact peut appartenir a plusieurs listes. Mais pour un formulaire de capture, une seule liste suffit.

**[ECRAN — screencast assignation de tags]**

[Montre la section "Tags"]

Section "Tags". C'est la partie la plus strategique. Le tag que tu assignes ici determine comment FluentCRM va traiter ce contact. Selectionne un tag existant ou cree-en un.

Pour notre exemple lead magnet LMS, on va assigner le tag "lead-lms". Pourquoi ? Parce que dans le Module 5, quand on creera les automations FluentCRM, c'est ce tag qui declenchera la sequence email de bienvenue.

[Selectionne le tag "lead-lms"]

La convention de nommage schoolsWP pour les tags : prefixe + tiret + sujet. "lead-lms", "lead-crm", "client-formation". Ca te permet de filtrer et segmenter proprement.

**[ECRAN — screencast statut du contact]**

[Montre l'option "Contact Status"]

Option "Contact Status". Deux choix principaux : "Subscribed" ou "Pending". Si tu choisis "Subscribed", le contact est ajoute directement avec le statut actif. Si tu choisis "Pending", il recevra un email de double opt-in avant d'etre active.

Pour un lead magnet ou le visiteur donne son email en echange d'un contenu, "Subscribed" est le choix courant. Le consentement est implicite dans l'action. Si tu veux du double opt-in — recommande pour la conformite RGPD stricte — choisis "Pending".

**[ECRAN — screencast activation et test]**

[Montre le toggle "Status" du feed en haut]

Verifie que le feed est bien actif — le toggle "Status" doit etre sur "Enabled". Sauvegarde.

[Ouvre le formulaire en preview et fait une soumission test]

Maintenant, on teste. Ouvre le formulaire en preview. Remplis un prenom et un email de test. Soumets.

[Passe dans FluentCRM > Contacts pour verifier]

Va dans FluentCRM > Contacts. Tu devrais voir ton contact de test avec le bon prenom, le bon email, le tag "lead-lms" et la liste assignee. Si tout est la, ton feed fonctionne.

[Montre la fiche contact avec le tag et la liste]

Voila. Chaque personne qui remplira ce formulaire sera automatiquement ajoutee dans FluentCRM, avec le bon tag et la bonne liste. Zero action manuelle.

**[TRANSITION — face camera]**

Ton formulaire est connecte a FluentCRM. Le mapping des champs est en place, le tag est assigne. Dans la prochaine lecon, on va aller plus loin avec les tags dynamiques — un tag different selon les reponses du visiteur dans le formulaire.

---

**Points cles** :
- Integration Feed = regle de transfert formulaire → FluentCRM
- Mapping obligatoire : Email du formulaire → Email FluentCRM
- Mapper aussi le prenom pour personnaliser les emails ({first_name})
- Assigner une liste et un tag a chaque feed
- Convention tags schoolsWP : prefixe-sujet (lead-lms, lead-crm, client-formation)
- Contact Status : "Subscribed" (direct) ou "Pending" (double opt-in)
- Toujours tester avec un email reel apres configuration

**Mots cles SEO** : connecter Fluent Forms FluentCRM, integration feed FluentCRM, mapping champs formulaire CRM, tag automatique inscription WordPress

---

### Lecon 4.4 — Tag dynamique : segmente des l'inscription

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast configuration tags dynamiques

---

**[INTRO — face camera]**

Dans la lecon precedente, on a assigne un tag fixe a tous les contacts qui remplissent le formulaire. Tout le monde recoit le meme tag. Mais dans certains cas, tu veux segmenter plus finement. Un visiteur interesse par les LMS ne recoit pas le meme tag qu'un visiteur interesse par le CRM. C'est le role des tags dynamiques — un tag different selon ce que le visiteur repond dans le formulaire.

**[ECRAN — screencast Fluent Forms > editeur du formulaire]**

[Ouvre le formulaire dans l'editeur]

Pour mettre en place un tag dynamique, il faut d'abord ajouter un champ de choix dans le formulaire. Un champ qui permet au visiteur de se qualifier lui-meme.

[Glisse un champ "Radio Button" ou "Dropdown" dans le formulaire]

Ajoute un champ de type "Radio" ou "Dropdown". Par exemple, un champ "Quel sujet t'interesse le plus ?" avec trois options : "Creer une formation en ligne (LMS)", "Gerer mes contacts et emails (CRM)", "Automatiser mon business (n8n)".

[Configure les options du champ]

Chaque option a une valeur et un libelle. Le libelle, c'est ce que le visiteur voit. La valeur, c'est ce que le formulaire envoie. Garde des valeurs propres : "lms", "crm", "automation".

**[ECRAN — screencast Integration > feed FluentCRM > Conditional Tags]**

[Va dans l'onglet Integration du formulaire]

Maintenant, va dans l'onglet "Integration". On va creer plusieurs feeds — un par tag. C'est la methode la plus propre.

[Cree un premier feed]

Premier feed : "Feed — Tag lead-lms". Dans le mapping, configure les memes champs que dans la lecon precedente — email, prenom, liste. Pour le tag, selectionne "lead-lms".

[Montre la section "Conditional Logic" en bas du feed]

Et voici la partie importante. En bas du feed, tu vois "Conditional Logic". Active-la. Ca ajoute un bloc de conditions.

[Configure la condition]

Configure la condition : "Si le champ [Quel sujet t'interesse] est egal a [lms]". Ca veut dire : ce feed ne s'execute que si le visiteur a choisi "LMS". Sauvegarde.

**[ECRAN — screencast creation des feeds suivants]**

[Cree un deuxieme feed]

Deuxieme feed : "Feed — Tag lead-crm". Meme mapping, meme liste. Tag : "lead-crm". Condition : le champ sujet est egal a "crm".

[Cree un troisieme feed]

Troisieme feed : "Feed — Tag lead-automation". Tag : "lead-automation". Condition : le champ sujet est egal a "automation".

[Montre la vue d'ensemble des 3 feeds]

Tu as maintenant 3 feeds sur le meme formulaire, chacun avec une condition differente. Un seul s'executera a chaque soumission — celui dont la condition correspond au choix du visiteur.

**[ECRAN — screencast test du systeme]**

[Ouvre le formulaire en preview]

On teste. Ouvre le formulaire en preview. Remplis le prenom et l'email. Selectionne "CRM" comme sujet. Soumets.

[Va dans FluentCRM > Contacts pour verifier]

Dans FluentCRM, le contact apparait avec le tag "lead-crm". Pas "lead-lms", pas "lead-automation". Le tag correspond au choix du visiteur.

[Montre la fiche contact avec le bon tag]

Fais un deuxieme test avec un autre email et le choix "LMS". Verifie que le tag "lead-lms" est bien assigne. Si les deux tests passent, tes tags dynamiques fonctionnent.

**[ECRAN — slide "Quand utiliser les tags dynamiques"]**

Quelques cas d'usage concrets pour les tags dynamiques :

- Segmenter par centre d'interet — LMS, CRM, SEO, automatisation
- Segmenter par niveau — debutant, intermediaire, expert
- Segmenter par objectif — vendre une formation, lancer un SaaS, trouver des clients
- Segmenter par source — si tu as un champ cache avec la source du trafic

Le principe est toujours le meme : un champ de choix dans le formulaire, un feed conditionnel par option dans l'integration.

**[ECRAN — slide "Alternative : opt-in forms natifs FluentCRM"]**

Un mot sur l'alternative. FluentCRM a ses propres formulaires d'opt-in — tu les trouves dans FluentCRM > Forms. Ils sont plus simples : email, prenom, liste, tag. Pas de drag-and-drop, pas de logique conditionnelle.

Pour un formulaire basique d'inscription newsletter, les opt-in forms natifs suffisent. Pour tout ce qui demande de la segmentation, des champs personnalises ou de la logique conditionnelle, Fluent Forms est la solution.

**[TRANSITION — face camera]**

Tu sais maintenant assigner des tags differents selon les reponses du visiteur. La segmentation commence des l'inscription — pas apres. Dans la prochaine lecon, on pousse la logique conditionnelle plus loin pour adapter le formulaire lui-meme au visiteur.

---

**Points cles** :
- Tag dynamique = un tag different selon la reponse du visiteur
- Methode : un champ de choix (radio/dropdown) + un feed conditionnel par option
- Conditional Logic en bas de chaque feed : "si champ X = valeur Y"
- Un seul feed s'execute par soumission
- Cas d'usage : interet, niveau, objectif, source du trafic
- Opt-in forms natifs FluentCRM = basique. Fluent Forms = segmentation avancee
- Toujours tester chaque condition avec un email different

**Mots cles SEO** : tag dynamique FluentCRM, segmenter leads WordPress, formulaire conditionnel FluentCRM, Fluent Forms conditional logic tags

---

### Lecon 4.5 — Conditional logic : adapte le formulaire au visiteur

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast logique conditionnelle

---

**[INTRO — face camera]**

Dans la lecon precedente, on a utilise la logique conditionnelle sur les feeds d'integration — cote back-end. Maintenant, on l'applique au formulaire lui-meme — cote visiteur. Afficher ou masquer des champs, changer les options, adapter le formulaire en temps reel selon les reponses. C'est la logique conditionnelle de Fluent Forms.

**[ECRAN — screencast editeur de formulaire]**

[Ouvre un formulaire dans l'editeur]

Prenons un cas concret. Tu as un formulaire d'inscription ou tu demandes "Quel est ton role ?". Les options : "Formateur", "Freelance", "Chef de projet". Selon la reponse, tu veux afficher une question differente.

[Montre le formulaire avec un champ Radio "Quel est ton role ?"]

Le champ "Quel est ton role ?" est deja dans le formulaire avec les trois options. Maintenant, on ajoute des champs conditionnels.

**[ECRAN — screencast ajout de champs conditionnels]**

[Ajoute un champ texte "Combien d'eleves as-tu ?"]

Ajoute un champ texte : "Combien d'eleves as-tu actuellement ?". Ce champ ne doit apparaitre que si le visiteur choisit "Formateur".

[Clique sur le champ > onglet "Advanced"]

Clique sur ce champ. Va dans l'onglet "Advanced" du champ — pas celui du formulaire, celui du champ lui-meme. Tu vois une section "Conditional Logic".

[Active la logique conditionnelle du champ]

Active-la. Configure la condition : "Show this field when — Quel est ton role — equals — Formateur".

[Montre la condition configuree]

Ca veut dire : ce champ est masque par defaut et n'apparait que si le visiteur selectionne "Formateur". Pour les autres choix, il reste invisible.

**[ECRAN — screencast ajout d'un deuxieme champ conditionnel]**

[Ajoute un champ "Quel CMS utilises-tu ?"]

Ajoute un deuxieme champ conditionnel : "Quel CMS utilises-tu ?" — un dropdown avec WordPress, Shopify, Autre. Ce champ n'apparait que si le visiteur choisit "Freelance".

[Configure la condition : Show when role = Freelance]

Meme methode. Onglet Advanced, Conditional Logic, condition : "Show this field when — Quel est ton role — equals — Freelance".

**[ECRAN — screencast preview avec test en temps reel]**

[Ouvre la preview du formulaire]

On teste en preview. Selectionne "Formateur" — le champ "Combien d'eleves" apparait. Le champ "Quel CMS" reste masque. Change pour "Freelance" — le champ "Quel CMS" apparait, le champ eleves disparait. Change pour "Chef de projet" — aucun des deux n'apparait.

[Montre les transitions entre les choix]

Fluide, instantane, sans rechargement de page. Le visiteur ne voit que ce qui le concerne.

**[ECRAN — screencast conditions avancees]**

[Montre les operateurs disponibles]

Les conditions ne se limitent pas a "equals". Tu as aussi : "not equals", "contains", "starts with", "ends with", "greater than", "less than". Et tu peux combiner plusieurs conditions avec "AND" ou "OR".

[Exemple de condition combinee]

Exemple : "Show this field when — role equals Formateur — AND — pays equals France". Le champ n'apparait que pour les formateurs francais.

**[ECRAN — screencast conditional logic sur les pages/sections]**

[Montre un formulaire multi-pages]

La logique conditionnelle fonctionne aussi a plus grande echelle. Tu peux conditionner des sections entieres, pas seulement des champs individuels. Si ton formulaire est long, tu peux le decouper en pages avec le champ "Form Step" et conditionner l'affichage de certaines pages.

**[ECRAN — slide "Integration avec les tags dynamiques"]**

Et voila ou ca devient puissant : combine la logique conditionnelle du formulaire avec les tags dynamiques de la lecon precedente. Le visiteur voit un formulaire adapte a son profil, et les donnees arrivent dans FluentCRM avec le bon tag, la bonne liste, les bons champs personnalises.

Exemple complet :
1. Le visiteur choisit "Formateur" → un champ supplementaire apparait
2. Le feed conditionnel assigne le tag "lead-formateur"
3. FluentCRM declenche une automation specifique aux formateurs

Formulaire personnalise, segmentation automatique, automation ciblee. Tout ca sans une ligne de code.

**[TRANSITION — face camera]**

Tu sais adapter ton formulaire au visiteur en temps reel. Dans la prochaine lecon, on voit comment placer ce formulaire sur ton site — shortcode, widget, popup. Parce qu'un bon formulaire qui n'est visible nulle part ne genere aucun lead.

---

**Points cles** :
- Conditional Logic = afficher/masquer des champs selon les reponses
- Configuration : onglet "Advanced" de chaque champ > Conditional Logic
- Operateurs : equals, not equals, contains, starts with, greater/less than
- Combiner conditions avec AND / OR
- Fonctionne sur les champs individuels et les sections entieres
- Combiner avec les tags dynamiques pour un parcours complet : formulaire adapte → tag cible → automation specifique
- Version Pro requise pour la logique conditionnelle avancee

**Mots cles SEO** : Fluent Forms logique conditionnelle, formulaire conditionnel WordPress, afficher masquer champ formulaire, Fluent Forms conditional logic tutoriel

---

### Lecon 4.6 — Place ton formulaire : shortcode, widget, popup

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des 3 methodes de placement

---

**[INTRO — face camera]**

Ton formulaire est cree, connecte a FluentCRM, avec des tags dynamiques et de la logique conditionnelle. Maintenant, il faut le rendre visible. Un formulaire qui n'est pas sur ton site ne capture rien. Trois methodes pour l'afficher : shortcode, widget et popup. On voit les trois.

**[ECRAN — screencast methode 1 — Shortcode]**

[Va dans Fluent Forms > All Forms]

Premiere methode : le shortcode. Va dans Fluent Forms > All Forms. A cote de chaque formulaire, tu vois un shortcode. C'est un code court entre crochets qui ressemble a ceci : [fluentform id="3"]. Le chiffre correspond a l'identifiant de ton formulaire.

[Copie le shortcode]

Copie ce shortcode. Tu peux le coller dans n'importe quel editeur WordPress — une page, un article, un texte de widget.

[Ouvre une page dans l'editeur WordPress (Gutenberg)]

Ouvre la page ou tu veux placer le formulaire. Ajoute un bloc "Shortcode" ou un bloc "Code court" dans Gutenberg. Colle le shortcode. Publie ou mets a jour la page.

[Montre le rendu cote visiteur]

Cote visiteur, le formulaire s'affiche a l'emplacement exact du bloc. C'est la methode la plus universelle — ca fonctionne partout ou WordPress accepte des shortcodes.

**[ECRAN — screencast methode 2 — Widget / Bloc Gutenberg]**

[Va dans Apparence > Widgets ou dans l'editeur Gutenberg]

Deuxieme methode : le widget ou le bloc Gutenberg. Si tu utilises un theme avec des zones de widgets — sidebar, footer — tu peux ajouter un widget "Fluent Forms" directement.

[Ajoute un widget Fluent Forms dans la sidebar]

Va dans Apparence > Widgets. Cherche le widget "Fluent Forms Widget". Glisse-le dans la sidebar ou le footer. Selectionne ton formulaire dans la liste deroulante. Sauvegarde.

[Montre le rendu dans la sidebar]

Le formulaire apparait dans la sidebar de toutes les pages qui utilisent cette zone de widget. Pratique pour un formulaire d'inscription newsletter toujours visible.

Dans Gutenberg, tu peux aussi utiliser le bloc "Fluent Forms" — meme principe, mais directement dans le contenu d'une page.

**[ECRAN — screencast methode 3 — Popup]**

[Va dans Fluent Forms Pro > Conversational Form ou montre l'integration avec un plugin popup]

Troisieme methode : le popup. Fluent Forms Pro inclut un mode "Conversational Form" qui affiche le formulaire en plein ecran, question par question. Mais pour un vrai popup — qui apparait apres un delai, au scroll ou a l'intention de sortie — tu as deux options.

[Option A : shortcode dans un plugin popup]

Option A : utilise ton shortcode dans un plugin de popup. Si tu utilises un page builder comme Elementor, Bricks ou un plugin popup dedie, cree un popup et colle le shortcode du formulaire a l'interieur. Configure le declencheur : delai, scroll, exit intent.

[Option B : FluentCRM Forms en popup]

Option B : les formulaires natifs FluentCRM ont une option d'affichage en popup integree. Va dans FluentCRM > Forms, cree un formulaire d'opt-in, et dans les reglages d'affichage, choisis "Popup". Configure le delai et les pages cibles. C'est plus simple mais moins personnalisable qu'un formulaire Fluent Forms complet.

**[ECRAN — slide "Ou placer tes formulaires — checklist"]**

Ou placer tes formulaires pour maximiser les inscriptions :

- Page d'accueil — au-dessus de la ligne de flottaison
- Sidebar du blog — visible sur tous les articles
- Fin d'article — le visiteur vient de lire ton contenu, il est engage
- Page dediee — landing page du lead magnet
- Popup — apres 30 secondes ou a l'exit intent (pas au chargement)
- Footer — en dernier recours, toujours present

Regle : un meme formulaire peut etre place a plusieurs endroits. Les soumissions arrivent au meme endroit dans FluentCRM quel que soit l'emplacement.

**[TRANSITION — face camera]**

Ton formulaire est visible, place aux bons endroits. Tu as maintenant un systeme complet : formulaire optimise, connecte a FluentCRM, avec segmentation automatique. Dans la prochaine lecon, c'est a toi de jouer — tu crees un formulaire lead magnet de A a Z pour ta formation.

---

**Points cles** :
- 3 methodes : shortcode (universel), widget/bloc (sidebar/footer), popup (conversion)
- Shortcode : [fluentform id="X"] — fonctionne partout dans WordPress
- Widget : Apparence > Widgets > "Fluent Forms Widget" pour sidebar/footer
- Popup : via plugin tiers avec shortcode ou FluentCRM Forms natif
- Placements strategiques : accueil, sidebar blog, fin d'article, landing page, popup
- Un formulaire = un identifiant — meme feed FluentCRM quel que soit l'emplacement

**Mots cles SEO** : afficher formulaire WordPress, shortcode Fluent Forms, formulaire popup WordPress, placer formulaire capture email site

---

### Lecon 4.7 — Exercice : Cree un formulaire lead magnet pour ta formation

**Type** : Exercice pratique (consignes ecrites)
**Duree estimee** : 30-40 min

---

## Objectif

Creer un formulaire lead magnet complet, connecte a FluentCRM avec segmentation automatique. A la fin de cet exercice, tu auras un formulaire fonctionnel qui capture des leads, les tague dans FluentCRM et les ajoute a la bonne liste — pret a declencher des automations.

## Prerequis

- Fluent Forms installe et actif (Pro recommande pour la logique conditionnelle)
- FluentCRM installe et actif
- Au moins 1 liste et 2 tags crees dans FluentCRM
- Acces admin a ton site WordPress
- Un lead magnet en tete (guide PDF, checklist, mini-formation, template)

> **Pas d'idee de lead magnet ?** Utilise l'un de ces exemples :
> - "Guide gratuit : Choisir son LMS WordPress en 2026" → tag "lead-lms"
> - "Checklist : 15 points pour configurer FluentCRM" → tag "lead-crm"
> - "Template : Sequence email de bienvenue" → tag "lead-automation"
> Choisis celui qui correspond a ta thematique.

## Etapes

### 1. Cree le formulaire dans Fluent Forms

- Va dans Fluent Forms > New Form > Blank Form
- Nomme-le clairement : "Lead Magnet — [nom du guide]"
- Ajoute les champs :
  - [ ] **Email** (obligatoire, libelle personnalise)
  - [ ] **Prenom** (obligatoire, First Name uniquement)
  - [ ] **Champ de choix** : un radio ou dropdown pour segmenter (ex: "Quel sujet t'interesse ?")
- Configure le bouton de soumission :
  - [ ] Texte oriente benefice (pas "Submit" ou "Envoyer")

### 2. Configure les reglages du formulaire

- Onglet Settings > Form Settings :
  - [ ] Confirmation : redirection vers une page de remerciement (cree la page si besoin)
  - [ ] Ou message de confirmation clair si pas de page dediee
- Email Notifications :
  - [ ] Desactive la notification admin (FluentCRM gerera les emails)

### 3. Connecte a FluentCRM avec Integration Feed

- Onglet Integration > FluentCRM :
  - [ ] **Feed principal** : mapping email + prenom, liste, tag par defaut
  - [ ] **Test** : soumets le formulaire avec un email de test, verifie dans FluentCRM

### 4. Ajoute des tags dynamiques (si champ de choix present)

- Cree un feed conditionnel par option :
  - [ ] Feed 1 : condition = choix A → tag A
  - [ ] Feed 2 : condition = choix B → tag B
  - [ ] Feed 3 : condition = choix C → tag C
- Teste chaque condition avec un email different :
  - [ ] Choix A → verifie tag A dans FluentCRM
  - [ ] Choix B → verifie tag B dans FluentCRM

### 5. Ajoute de la logique conditionnelle au formulaire (optionnel, Pro)

- [ ] Ajoute un champ conditionnel qui n'apparait que pour un choix specifique
- [ ] Verifie en preview que l'affichage est correct

### 6. Place le formulaire sur ton site

- [ ] Place le formulaire avec au moins 2 methodes differentes (shortcode + widget, ou shortcode + popup)
- [ ] Verifie le rendu cote visiteur sur desktop et mobile

### 7. Test final end-to-end

- [ ] Remplis le formulaire depuis une page de ton site (pas depuis la preview)
- [ ] Verifie dans FluentCRM : contact cree, bon tag, bonne liste, bons champs
- [ ] Verifie la page de remerciement (ou le message de confirmation)

## Criteres de validation

- [ ] Le formulaire a au minimum 2 champs (email + prenom) et un bouton personnalise
- [ ] L'Integration Feed FluentCRM est active et fonctionnelle
- [ ] Le contact de test apparait dans FluentCRM avec le bon tag et la bonne liste
- [ ] Le formulaire est place sur au moins une page du site
- [ ] Le rendu est propre sur desktop et mobile
- [ ] Le message/page de confirmation s'affiche apres soumission

## Bonus (optionnel)

- [ ] Ajoute un champ cache "Source" avec la valeur de la page (pour tracker l'origine du lead)
- [ ] Configure un champ conditionnel qui affiche une question differente selon le choix
- [ ] Place le formulaire dans un popup avec declencheur exit-intent
- [ ] Mappe un champ personnalise FluentCRM (ex: "Niveau" ou "Objectif")

---

### Lecon 4.8 — Quiz : Valide tes acquis M4

**Type** : Quiz TutorLMS (8 questions)
**Seuil de reussite** : 80%

---

**Question 1** : Quel est l'editeur commun entre Fluent Forms et FluentCRM ?

- A) Developer Express
- B) WPManageNinja *(bonne reponse)*
- C) Awesome Motive
- D) Starter Templates

---

**Question 2** : Combien de champs minimum recommande-t-on pour un formulaire de capture email ?

- A) 1 (email uniquement)
- B) 2 (email + prenom) *(bonne reponse)*
- C) 3 (email + prenom + nom)
- D) 4 (email + prenom + nom + telephone)

---

**Question 3** : Dans l'Integration Feed, quel mapping est obligatoire pour creer un contact FluentCRM ?

- A) Prenom → First Name
- B) Nom → Last Name
- C) Email → Email *(bonne reponse)*
- D) Telephone → Phone

---

**Question 4** : Comment mettre en place un tag dynamique dans Fluent Forms ?

- A) En creant un seul feed avec plusieurs tags selectionnes
- B) En creant un feed conditionnel par tag, chacun avec sa propre condition *(bonne reponse)*
- C) En utilisant un champ cache qui calcule le tag automatiquement
- D) En activant le mode "Auto-Tag" dans les reglages de Fluent Forms

---

**Question 5** : Ou se configure la logique conditionnelle d'un champ dans Fluent Forms ?

- A) Dans les reglages globaux du formulaire
- B) Dans l'onglet Integration du formulaire
- C) Dans l'onglet Advanced du champ lui-meme *(bonne reponse)*
- D) Dans FluentCRM > Settings > Forms

---

**Question 6** : Quel shortcode permet d'afficher un formulaire Fluent Forms ?

- A) [contact-form id="3"]
- B) [fluentform id="3"] *(bonne reponse)*
- C) [form name="lead-magnet"]
- D) [fluent-crm form="3"]

---

**Question 7** : Quelle est la difference principale entre les opt-in forms natifs FluentCRM et Fluent Forms ?

- A) FluentCRM est payant, Fluent Forms est gratuit
- B) Fluent Forms offre la logique conditionnelle et les champs personnalises, pas les opt-in natifs *(bonne reponse)*
- C) Les opt-in natifs supportent plus de champs que Fluent Forms
- D) Fluent Forms ne peut pas se connecter a FluentCRM

---

**Question 8** : Quel statut de contact choisir dans le feed pour activer le double opt-in ?

- A) Subscribed
- B) Pending *(bonne reponse)*
- C) Unsubscribed
- D) Active

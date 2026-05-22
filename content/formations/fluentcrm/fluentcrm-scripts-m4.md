# Scripts vidéo — Module 4 : Fluent Forms — générer des leads

**Formation** : Maîtriser FluentCRM
**Module** : M4 — Fluent Forms : générer des leads (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~50 min
**Date** : 2026-03-23

---

### Leçon 4.1 — Installe et découvre Fluent Forms

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast de l'installation et de l'interface

---

**[INTRO — face caméra]**

FluentCRM gère tes contacts et tes automations. Mais pour alimenter ta base, tu as besoin de formulaires. Et le meilleur partenaire de FluentCRM pour ça, c'est Fluent Forms. Même éditeur, même écosystème, intégration native. Dans cette leçon, on installe Fluent Forms et on fait le tour de l'interface.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

Pour installer Fluent Forms, va dans Extensions, puis Ajouter. Tape "Fluent Forms" dans la barre de recherche. Tu verras "Fluent Forms — Contact Form Builder" par WPManageNinja. C'est le même éditeur que FluentCRM. Clique sur Installer, puis Activer.

[Montre le plugin dans la liste avec le bouton Activer]

La version gratuite suffit pour créer des formulaires basiques et les connecter à FluentCRM. Mais pour les fonctionnalités qu'on va utiliser dans ce module — logique conditionnelle avancée, champs personnalisés, intégration complète — tu auras besoin de Fluent Forms Pro.

**[ÉCRAN — screencast menu Fluent Forms]**

[Montre le nouveau menu "Fluent Forms" dans la barre latérale WordPress]

Une fois activé, un nouveau menu apparaît dans la barre latérale : "Fluent Forms". Clique dessus. Tu arrives sur le tableau de bord principal.

[Vue du dashboard Fluent Forms]

L'interface est organisée en plusieurs sections. "All Forms" — la liste de tous tes formulaires. C'est ton point de départ. "New Form" — le bouton pour créer un nouveau formulaire. "Entries" — toutes les soumissions reçues, triées par formulaire. Et "Settings" — les réglages globaux.

**[ÉCRAN — screencast galerie de templates]**

[Clique sur "New Form" pour voir les templates]

Clique sur "New Form". Fluent Forms te propose une galerie de templates préconstruits. Formulaire de contact, inscription newsletter, demande de devis, inscription événement — il y en a des dizaines. Tu peux aussi partir d'un formulaire vierge.

Pour l'instant, on ne crée rien. On explore.

**[ÉCRAN — screencast éditeur de formulaire]**

[Ouvre un template pour montrer l'éditeur]

Ouvre un template pour voir l'éditeur. C'est un constructeur drag-and-drop. À gauche, les champs disponibles — texte, email, menu déroulant, cases à cocher, champs cachés. Au centre, ton formulaire en construction. Tu glisses un champ, tu le déposes, tu le configures.

[Montre le glisser-déposer d'un champ]

Chaque champ a ses propres réglages : libellé, placeholder, champ obligatoire ou non, validation. On verra tout ça en détail dans la leçon suivante.

**[ÉCRAN — screencast onglet Settings du formulaire]**

[Montre les onglets du formulaire : Editor, Settings, Integration]

En haut du formulaire, trois onglets importants. "Editor" — là où tu construis. "Settings" — les réglages du formulaire (confirmation, notifications, restrictions). Et "Integration" — c'est là qu'on connectera FluentCRM. On y reviendra dans la leçon 4.3.

**[TRANSITION — face caméra]**

Fluent Forms est installé, tu connais l'interface. Dans la prochaine leçon, on crée ton premier formulaire de capture d'email — le formulaire qui va alimenter ta base FluentCRM.

---

**Points clés** :
- Fluent Forms = même éditeur que FluentCRM (WPManageNinja), intégration native
- Version gratuite pour les bases, Pro pour logique conditionnelle et intégration complète
- Interface : All Forms, Entries, Settings + éditeur drag-and-drop
- 3 onglets par formulaire : Editor, Settings, Integration
- Galerie de templates pour démarrer rapidement

**Mots clés SEO** : installer Fluent Forms WordPress, Fluent Forms FluentCRM, formulaire WordPress capture email, Fluent Forms tutoriel

---

### Leçon 4.2 — Crée ton formulaire de capture d'email

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast création formulaire complet

---

**[INTRO — face caméra]**

Un formulaire de capture d'email, c'est la porte d'entrée de ton tunnel. Quelqu'un arrive sur ton site, remplit le formulaire, et devient un contact dans FluentCRM. Simple en théorie. En pratique, chaque champ compte. Dans cette leçon, on crée ensemble un formulaire de capture optimisé pour générer des leads.

**[ÉCRAN — screencast Fluent Forms > New Form]**

[Clique sur "New Form" puis "Blank Form"]

Va dans Fluent Forms, clique sur "New Form". Cette fois, on part d'un formulaire vierge. Clique sur "Blank Form".

[Montre le formulaire vierge dans l'éditeur]

Tu arrives dans l'éditeur avec un formulaire vide. Première chose : donne-lui un nom. En haut à gauche, clique sur le titre par défaut et renomme-le. Par exemple : "Lead Magnet — Guide LMS".

Ce nom est interne — tes visiteurs ne le verront pas. Mais toi, quand tu auras 15 formulaires, tu seras content de les retrouver.

**[ÉCRAN — screencast ajout champ Email]**

[Glisse le champ "Email" dans le formulaire]

Premier champ à ajouter : l'email. C'est le seul champ vraiment obligatoire pour un formulaire de capture. Dans la colonne de gauche, cherche "Email Address" et glisse-le dans le formulaire.

[Configure le champ Email]

Clique sur le champ pour le configurer. "Label" — c'est le libellé visible. Change-le en "Ton adresse email" pour rester dans le ton schoolsWP. "Placeholder" — le texte grisé dans le champ. Mets quelque chose de concret : "prenom@exemple.fr". Active "Required" — ce champ est obligatoire, évidemment.

**[ÉCRAN — screencast ajout champ Prénom]**

[Glisse le champ "Name" dans le formulaire]

Deuxième champ : le prénom. Pas le nom complet — le prénom. Ça te permettra de personnaliser tes emails dans FluentCRM.

Glisse le champ "Name Fields" dans le formulaire. Par défaut, il inclut prénom, nom et parfois le titre. On ne veut que le prénom. Clique sur le champ, puis désactive "Last Name" et tout le reste. Garde uniquement "First Name".

[Montre la configuration avec seulement First Name actif]

Renomme le libellé en "Ton prénom". Marque-le comme obligatoire.

**[ÉCRAN — screencast bouton de soumission]**

[Montre le bouton Submit en bas du formulaire]

Le bouton de soumission est ajouté automatiquement. Mais le texte par défaut — "Submit" — est trop générique. Clique dessus et change le texte en quelque chose de spécifique à ton offre. Par exemple : "Télécharge le guide gratuit" ou "Reçois la formation". Le texte du bouton doit dire ce que le visiteur obtient, pas ce qu'il fait.

**[ÉCRAN — screencast onglet Settings > Confirmation]**

[Clique sur l'onglet Settings du formulaire]

Va dans l'onglet "Settings" du formulaire. Section "Form Settings". Ici tu configures ce qui se passe après la soumission.

[Montre les options de confirmation]

Trois options. "Same Page" — un message de confirmation s'affiche sur la même page. "To a Page" — redirige vers une page de remerciement. "To a Custom URL" — redirige vers une URL spécifique.

Mon conseil : redirige vers une page de remerciement dédiée. Ça te permet de tracker les conversions dans Google Analytics, de proposer une offre complémentaire, et de donner les instructions de téléchargement.

Pour le message ou la page, sois clair : "Ton guide est en route. Vérifie ta boîte mail (et tes spams)."

**[ÉCRAN — screencast onglet Settings > Email Notifications]**

[Montre la section Email Notifications]

Section "Email Notifications". Par défaut, Fluent Forms t'envoie un email à chaque soumission. Utile au début pour vérifier que tout fonctionne. Tu pourras le désactiver plus tard quand le volume augmente.

Tu peux aussi configurer un email de confirmation envoyé au visiteur. Mais attention : si tu connectes FluentCRM dans la leçon suivante, c'est FluentCRM qui gérera les emails de bienvenue. Évite les doublons.

**[ÉCRAN — screencast preview du formulaire]**

[Clique sur "Preview" pour voir le formulaire]

Clique sur "Preview" en haut à droite pour voir le rendu. Deux champs — prénom et email — un bouton clair. Rien de plus. Un formulaire de capture efficace est un formulaire court. Chaque champ supplémentaire réduit le taux de conversion.

**[TRANSITION — face caméra]**

Ton formulaire est créé. Deux champs, un bouton, un message de confirmation. Propre et efficace. Dans la prochaine leçon, on connecte ce formulaire à FluentCRM pour que chaque inscription crée automatiquement un contact avec le bon tag.

---

**Points clés** :
- Formulaire de capture = minimum de champs (email + prénom)
- Nommer les formulaires clairement (tu en auras plusieurs)
- Bouton de soumission : texte orienté bénéfice, pas "Submit"
- Confirmation : rediriger vers une page de remerciement (tracking + upsell)
- Éviter les doublons : email de confirmation via FluentCRM, pas Fluent Forms
- Moins de champs = meilleur taux de conversion

**Mots clés SEO** : créer formulaire capture email WordPress, Fluent Forms formulaire inscription, formulaire lead magnet WordPress, optimiser formulaire conversion

---

### Leçon 4.3 — Connecte Fluent Forms à FluentCRM (Integration Feed)

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast intégration complète

---

**[INTRO — face caméra]**

Tu as un formulaire. Tu as FluentCRM. Maintenant il faut que les deux se parlent. Quand quelqu'un remplit ton formulaire, son email et son prénom doivent arriver directement dans FluentCRM avec le bon tag et la bonne liste. C'est le rôle de l'Integration Feed. On le configure ensemble.

**[ÉCRAN — screencast Fluent Forms > formulaire > Integration]**

[Ouvre le formulaire créé dans la leçon précédente, onglet "Integration"]

Ouvre le formulaire qu'on a créé. Clique sur l'onglet "Integration" en haut. C'est ici que tu connectes Fluent Forms à des services externes — et FluentCRM en fait partie nativement.

[Montre la liste des intégrations disponibles]

Tu vois une liste d'intégrations disponibles. Cherche "FluentCRM". Clique dessus. Un nouveau "feed" d'intégration se crée.

**[ÉCRAN — screencast configuration du feed FluentCRM]**

[Montre le formulaire de configuration du feed]

Le feed, c'est la règle de transfert entre ton formulaire et FluentCRM. Première chose : donne-lui un nom explicite. Par exemple : "Feed — Lead LMS vers FluentCRM". Ce nom est interne, mais quand tu auras plusieurs feeds sur plusieurs formulaires, tu seras content de t'y retrouver.

**[ÉCRAN — screencast mapping des champs]**

[Montre la section "Map Fields"]

Section "Map Fields" — c'est le cœur de la configuration. Tu fais correspondre chaque champ de ton formulaire à un champ contact dans FluentCRM.

[Montre le mapping Email → Email]

"Email" du formulaire → "Email" dans FluentCRM. C'est le seul mapping obligatoire. Sans ça, FluentCRM ne peut pas créer le contact.

[Montre le mapping Prénom → First Name]

"Prénom" du formulaire → "First Name" dans FluentCRM. Ça te permet d'utiliser la variable {first_name} dans tes emails pour personnaliser.

[Montre la liste déroulante des champs FluentCRM disponibles]

Si tu as des champs personnalisés dans FluentCRM — par exemple "Source du lead" ou "Niveau" — tu peux les mapper ici aussi. Tout champ que tu as créé dans FluentCRM > Contacts > Custom Fields apparaît dans cette liste.

**[ÉCRAN — screencast assignation de liste]**

[Montre la section "Lists"]

Section "Lists". Sélectionne la liste dans laquelle le contact sera ajouté. Par exemple, ta liste "Newsletter" ou "Leads formation LMS". Si tu n'as pas encore de liste adaptée, retourne dans FluentCRM > Contacts > Lists et crée-en une d'abord.

Un contact peut appartenir à plusieurs listes. Mais pour un formulaire de capture, une seule liste suffit.

**[ÉCRAN — screencast assignation de tags]**

[Montre la section "Tags"]

Section "Tags". C'est la partie la plus stratégique. Le tag que tu assignes ici détermine comment FluentCRM va traiter ce contact. Sélectionne un tag existant ou crée-en un.

Pour notre exemple lead magnet LMS, on va assigner le tag "lead-lms". Pourquoi ? Parce que dans le Module 5, quand on créera les automations FluentCRM, c'est ce tag qui déclenchera la séquence email de bienvenue.

[Sélectionne le tag "lead-lms"]

La convention de nommage schoolsWP pour les tags : préfixe + tiret + sujet. "lead-lms", "lead-crm", "client-formation". Ça te permet de filtrer et segmenter proprement.

**[ÉCRAN — screencast statut du contact]**

[Montre l'option "Contact Status"]

Option "Contact Status". Deux choix principaux : "Subscribed" ou "Pending". Si tu choisis "Subscribed", le contact est ajouté directement avec le statut actif. Si tu choisis "Pending", il recevra un email de double opt-in avant d'être activé.

Pour un lead magnet où le visiteur donne son email en échange d'un contenu, "Subscribed" est le choix courant. Le consentement est implicite dans l'action. Si tu veux du double opt-in — recommandé pour la conformité RGPD stricte — choisis "Pending".

**[ÉCRAN — screencast activation et test]**

[Montre le toggle "Status" du feed en haut]

Vérifie que le feed est bien actif — le toggle "Status" doit être sur "Enabled". Sauvegarde.

[Ouvre le formulaire en preview et fait une soumission test]

Maintenant, on teste. Ouvre le formulaire en preview. Remplis un prénom et un email de test. Soumets.

[Passe dans FluentCRM > Contacts pour vérifier]

Va dans FluentCRM > Contacts. Tu devrais voir ton contact de test avec le bon prénom, le bon email, le tag "lead-lms" et la liste assignée. Si tout est là, ton feed fonctionne.

[Montre la fiche contact avec le tag et la liste]

Voilà. Chaque personne qui remplira ce formulaire sera automatiquement ajoutée dans FluentCRM, avec le bon tag et la bonne liste. Zéro action manuelle.

**[TRANSITION — face caméra]**

Ton formulaire est connecté à FluentCRM. Le mapping des champs est en place, le tag est assigné. Dans la prochaine leçon, on va aller plus loin avec les tags dynamiques — un tag différent selon les réponses du visiteur dans le formulaire.

---

**Points clés** :
- Integration Feed = règle de transfert formulaire → FluentCRM
- Mapping obligatoire : Email du formulaire → Email FluentCRM
- Mapper aussi le prénom pour personnaliser les emails ({first_name})
- Assigner une liste et un tag à chaque feed
- Convention tags schoolsWP : préfixe-sujet (lead-lms, lead-crm, client-formation)
- Contact Status : "Subscribed" (direct) ou "Pending" (double opt-in)
- Toujours tester avec un email réel après configuration

**Mots clés SEO** : connecter Fluent Forms FluentCRM, integration feed FluentCRM, mapping champs formulaire CRM, tag automatique inscription WordPress

---

### Leçon 4.4 — Tag dynamique : segmente dès l'inscription

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast configuration tags dynamiques

---

**[INTRO — face caméra]**

Dans la leçon précédente, on a assigné un tag fixe à tous les contacts qui remplissent le formulaire. Tout le monde reçoit le même tag. Mais dans certains cas, tu veux segmenter plus finement. Un visiteur intéressé par les LMS ne reçoit pas le même tag qu'un visiteur intéressé par le CRM. C'est le rôle des tags dynamiques — un tag différent selon ce que le visiteur répond dans le formulaire.

**[ÉCRAN — screencast Fluent Forms > éditeur du formulaire]**

[Ouvre le formulaire dans l'éditeur]

Pour mettre en place un tag dynamique, il faut d'abord ajouter un champ de choix dans le formulaire. Un champ qui permet au visiteur de se qualifier lui-même.

[Glisse un champ "Radio Button" ou "Dropdown" dans le formulaire]

Ajoute un champ de type "Radio" ou "Dropdown". Par exemple, un champ "Quel sujet t'intéresse le plus ?" avec trois options : "Créer une formation en ligne (LMS)", "Gérer mes contacts et emails (CRM)", "Automatiser mon business (n8n)".

[Configure les options du champ]

Chaque option a une valeur et un libellé. Le libellé, c'est ce que le visiteur voit. La valeur, c'est ce que le formulaire envoie. Garde des valeurs propres : "lms", "crm", "automation".

**[ÉCRAN — screencast Integration > feed FluentCRM > Conditional Tags]**

[Va dans l'onglet Integration du formulaire]

Maintenant, va dans l'onglet "Integration". On va créer plusieurs feeds — un par tag. C'est la méthode la plus propre.

[Crée un premier feed]

Premier feed : "Feed — Tag lead-lms". Dans le mapping, configure les mêmes champs que dans la leçon précédente — email, prénom, liste. Pour le tag, sélectionne "lead-lms".

[Montre la section "Conditional Logic" en bas du feed]

Et voici la partie importante. En bas du feed, tu vois "Conditional Logic". Active-la. Ça ajoute un bloc de conditions.

[Configure la condition]

Configure la condition : "Si le champ [Quel sujet t'intéresse] est égal à [lms]". Ça veut dire : ce feed ne s'exécute que si le visiteur a choisi "LMS". Sauvegarde.

**[ÉCRAN — screencast création des feeds suivants]**

[Crée un deuxième feed]

Deuxième feed : "Feed — Tag lead-crm". Même mapping, même liste. Tag : "lead-crm". Condition : le champ sujet est égal à "crm".

[Crée un troisième feed]

Troisième feed : "Feed — Tag lead-automation". Tag : "lead-automation". Condition : le champ sujet est égal à "automation".

[Montre la vue d'ensemble des 3 feeds]

Tu as maintenant 3 feeds sur le même formulaire, chacun avec une condition différente. Un seul s'exécutera à chaque soumission — celui dont la condition correspond au choix du visiteur.

**[ÉCRAN — screencast test du système]**

[Ouvre le formulaire en preview]

On teste. Ouvre le formulaire en preview. Remplis le prénom et l'email. Sélectionne "CRM" comme sujet. Soumets.

[Va dans FluentCRM > Contacts pour vérifier]

Dans FluentCRM, le contact apparaît avec le tag "lead-crm". Pas "lead-lms", pas "lead-automation". Le tag correspond au choix du visiteur.

[Montre la fiche contact avec le bon tag]

Fais un deuxième test avec un autre email et le choix "LMS". Vérifie que le tag "lead-lms" est bien assigné. Si les deux tests passent, tes tags dynamiques fonctionnent.

**[ÉCRAN — slide "Quand utiliser les tags dynamiques"]**

Quelques cas d'usage concrets pour les tags dynamiques :

- Segmenter par centre d'intérêt — LMS, CRM, SEO, automatisation
- Segmenter par niveau — débutant, intermédiaire, expert
- Segmenter par objectif — vendre une formation, lancer un SaaS, trouver des clients
- Segmenter par source — si tu as un champ caché avec la source du trafic

Le principe est toujours le même : un champ de choix dans le formulaire, un feed conditionnel par option dans l'intégration.

**[ÉCRAN — slide "Alternative : opt-in forms natifs FluentCRM"]**

Un mot sur l'alternative. FluentCRM a ses propres formulaires d'opt-in — tu les trouves dans FluentCRM > Forms. Ils sont plus simples : email, prénom, liste, tag. Pas de drag-and-drop, pas de logique conditionnelle.

Pour un formulaire basique d'inscription newsletter, les opt-in forms natifs suffisent. Pour tout ce qui demande de la segmentation, des champs personnalisés ou de la logique conditionnelle, Fluent Forms est la solution.

**[TRANSITION — face caméra]**

Tu sais maintenant assigner des tags différents selon les réponses du visiteur. La segmentation commence dès l'inscription — pas après. Dans la prochaine leçon, on pousse la logique conditionnelle plus loin pour adapter le formulaire lui-même au visiteur.

---

**Points clés** :
- Tag dynamique = un tag différent selon la réponse du visiteur
- Méthode : un champ de choix (radio/dropdown) + un feed conditionnel par option
- Conditional Logic en bas de chaque feed : "si champ X = valeur Y"
- Un seul feed s'exécute par soumission
- Cas d'usage : intérêt, niveau, objectif, source du trafic
- Opt-in forms natifs FluentCRM = basique. Fluent Forms = segmentation avancée
- Toujours tester chaque condition avec un email différent

**Mots clés SEO** : tag dynamique FluentCRM, segmenter leads WordPress, formulaire conditionnel FluentCRM, Fluent Forms conditional logic tags

---

### Leçon 4.5 — Conditional logic : adapte le formulaire au visiteur

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast logique conditionnelle

---

**[INTRO — face caméra]**

Dans la leçon précédente, on a utilisé la logique conditionnelle sur les feeds d'intégration — côté back-end. Maintenant, on l'applique au formulaire lui-même — côté visiteur. Afficher ou masquer des champs, changer les options, adapter le formulaire en temps réel selon les réponses. C'est la logique conditionnelle de Fluent Forms.

**[ÉCRAN — screencast éditeur de formulaire]**

[Ouvre un formulaire dans l'éditeur]

Prenons un cas concret. Tu as un formulaire d'inscription où tu demandes "Quel est ton rôle ?". Les options : "Formateur", "Freelance", "Chef de projet". Selon la réponse, tu veux afficher une question différente.

[Montre le formulaire avec un champ Radio "Quel est ton rôle ?"]

Le champ "Quel est ton rôle ?" est déjà dans le formulaire avec les trois options. Maintenant, on ajoute des champs conditionnels.

**[ÉCRAN — screencast ajout de champs conditionnels]**

[Ajoute un champ texte "Combien d'élèves as-tu ?"]

Ajoute un champ texte : "Combien d'élèves as-tu actuellement ?". Ce champ ne doit apparaître que si le visiteur choisit "Formateur".

[Clique sur le champ > onglet "Advanced"]

Clique sur ce champ. Va dans l'onglet "Advanced" du champ — pas celui du formulaire, celui du champ lui-même. Tu vois une section "Conditional Logic".

[Active la logique conditionnelle du champ]

Active-la. Configure la condition : "Show this field when — Quel est ton rôle — equals — Formateur".

[Montre la condition configurée]

Ça veut dire : ce champ est masqué par défaut et n'apparaît que si le visiteur sélectionne "Formateur". Pour les autres choix, il reste invisible.

**[ÉCRAN — screencast ajout d'un deuxième champ conditionnel]**

[Ajoute un champ "Quel CMS utilises-tu ?"]

Ajoute un deuxième champ conditionnel : "Quel CMS utilises-tu ?" — un dropdown avec WordPress, Shopify, Autre. Ce champ n'apparaît que si le visiteur choisit "Freelance".

[Configure la condition : Show when role = Freelance]

Même méthode. Onglet Advanced, Conditional Logic, condition : "Show this field when — Quel est ton rôle — equals — Freelance".

**[ÉCRAN — screencast preview avec test en temps réel]**

[Ouvre la preview du formulaire]

On teste en preview. Sélectionne "Formateur" — le champ "Combien d'élèves" apparaît. Le champ "Quel CMS" reste masqué. Change pour "Freelance" — le champ "Quel CMS" apparaît, le champ élèves disparaît. Change pour "Chef de projet" — aucun des deux n'apparaît.

[Montre les transitions entre les choix]

Fluide, instantané, sans rechargement de page. Le visiteur ne voit que ce qui le concerne.

**[ÉCRAN — screencast conditions avancées]**

[Montre les opérateurs disponibles]

Les conditions ne se limitent pas à "equals". Tu as aussi : "not equals", "contains", "starts with", "ends with", "greater than", "less than". Et tu peux combiner plusieurs conditions avec "AND" ou "OR".

[Exemple de condition combinée]

Exemple : "Show this field when — role equals Formateur — AND — pays equals France". Le champ n'apparaît que pour les formateurs français.

**[ÉCRAN — screencast conditional logic sur les pages/sections]**

[Montre un formulaire multi-pages]

La logique conditionnelle fonctionne aussi à plus grande échelle. Tu peux conditionner des sections entières, pas seulement des champs individuels. Si ton formulaire est long, tu peux le découper en pages avec le champ "Form Step" et conditionner l'affichage de certaines pages.

**[ÉCRAN — slide "Intégration avec les tags dynamiques"]**

Et voilà où ça devient puissant : combine la logique conditionnelle du formulaire avec les tags dynamiques de la leçon précédente. Le visiteur voit un formulaire adapté à son profil, et les données arrivent dans FluentCRM avec le bon tag, la bonne liste, les bons champs personnalisés.

Exemple complet :
1. Le visiteur choisit "Formateur" → un champ supplémentaire apparaît
2. Le feed conditionnel assigne le tag "lead-formateur"
3. FluentCRM déclenche une automation spécifique aux formateurs

Formulaire personnalisé, segmentation automatique, automation ciblée. Tout ça sans une ligne de code.

**[TRANSITION — face caméra]**

Tu sais adapter ton formulaire au visiteur en temps réel. Dans la prochaine leçon, on voit comment placer ce formulaire sur ton site — shortcode, widget, popup. Parce qu'un bon formulaire qui n'est visible nulle part ne génère aucun lead.

---

**Points clés** :
- Conditional Logic = afficher/masquer des champs selon les réponses
- Configuration : onglet "Advanced" de chaque champ > Conditional Logic
- Opérateurs : equals, not equals, contains, starts with, greater/less than
- Combiner conditions avec AND / OR
- Fonctionne sur les champs individuels et les sections entières
- Combiner avec les tags dynamiques pour un parcours complet : formulaire adapté → tag ciblé → automation spécifique
- Version Pro requise pour la logique conditionnelle avancée

**Mots clés SEO** : Fluent Forms logique conditionnelle, formulaire conditionnel WordPress, afficher masquer champ formulaire, Fluent Forms conditional logic tutoriel

---

### Leçon 4.6 — Place ton formulaire : shortcode, widget, popup

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast des 3 méthodes de placement

---

**[INTRO — face caméra]**

Ton formulaire est créé, connecté à FluentCRM, avec des tags dynamiques et de la logique conditionnelle. Maintenant, il faut le rendre visible. Un formulaire qui n'est pas sur ton site ne capture rien. Trois méthodes pour l'afficher : shortcode, widget et popup. On voit les trois.

**[ÉCRAN — screencast méthode 1 — Shortcode]**

[Va dans Fluent Forms > All Forms]

Première méthode : le shortcode. Va dans Fluent Forms > All Forms. À côté de chaque formulaire, tu vois un shortcode. C'est un code court entre crochets qui ressemble à ceci : [fluentform id="3"]. Le chiffre correspond à l'identifiant de ton formulaire.

[Copie le shortcode]

Copie ce shortcode. Tu peux le coller dans n'importe quel éditeur WordPress — une page, un article, un texte de widget.

[Ouvre une page dans l'éditeur WordPress (Gutenberg)]

Ouvre la page où tu veux placer le formulaire. Ajoute un bloc "Shortcode" ou un bloc "Code court" dans Gutenberg. Colle le shortcode. Publie ou mets à jour la page.

[Montre le rendu côté visiteur]

Côté visiteur, le formulaire s'affiche à l'emplacement exact du bloc. C'est la méthode la plus universelle — ça fonctionne partout où WordPress accepte des shortcodes.

**[ÉCRAN — screencast méthode 2 — Widget / Bloc Gutenberg]**

[Va dans Apparence > Widgets ou dans l'éditeur Gutenberg]

Deuxième méthode : le widget ou le bloc Gutenberg. Si tu utilises un thème avec des zones de widgets — sidebar, footer — tu peux ajouter un widget "Fluent Forms" directement.

[Ajoute un widget Fluent Forms dans la sidebar]

Va dans Apparence > Widgets. Cherche le widget "Fluent Forms Widget". Glisse-le dans la sidebar ou le footer. Sélectionne ton formulaire dans la liste déroulante. Sauvegarde.

[Montre le rendu dans la sidebar]

Le formulaire apparaît dans la sidebar de toutes les pages qui utilisent cette zone de widget. Pratique pour un formulaire d'inscription newsletter toujours visible.

Dans Gutenberg, tu peux aussi utiliser le bloc "Fluent Forms" — même principe, mais directement dans le contenu d'une page.

**[ÉCRAN — screencast méthode 3 — Popup]**

[Va dans Fluent Forms Pro > Conversational Form ou montre l'intégration avec un plugin popup]

Troisième méthode : le popup. Fluent Forms Pro inclut un mode "Conversational Form" qui affiche le formulaire en plein écran, question par question. Mais pour un vrai popup — qui apparaît après un délai, au scroll ou à l'intention de sortie — tu as deux options.

[Option A : shortcode dans un plugin popup]

Option A : utilise ton shortcode dans un plugin de popup. Si tu utilises un page builder comme Elementor, Bricks ou un plugin popup dédié, crée un popup et colle le shortcode du formulaire à l'intérieur. Configure le déclencheur : délai, scroll, exit intent.

[Option B : FluentCRM Forms en popup]

Option B : les formulaires natifs FluentCRM ont une option d'affichage en popup intégrée. Va dans FluentCRM > Forms, crée un formulaire d'opt-in, et dans les réglages d'affichage, choisis "Popup". Configure le délai et les pages cibles. C'est plus simple mais moins personnalisable qu'un formulaire Fluent Forms complet.

**[ÉCRAN — slide "Où placer tes formulaires — checklist"]**

Où placer tes formulaires pour maximiser les inscriptions :

- Page d'accueil — au-dessus de la ligne de flottaison
- Sidebar du blog — visible sur tous les articles
- Fin d'article — le visiteur vient de lire ton contenu, il est engagé
- Page dédiée — landing page du lead magnet
- Popup — après 30 secondes ou à l'exit intent (pas au chargement)
- Footer — en dernier recours, toujours présent

Règle : un même formulaire peut être placé à plusieurs endroits. Les soumissions arrivent au même endroit dans FluentCRM quel que soit l'emplacement.

**[TRANSITION — face caméra]**

Ton formulaire est visible, placé aux bons endroits. Tu as maintenant un système complet : formulaire optimisé, connecté à FluentCRM, avec segmentation automatique. Dans la prochaine leçon, c'est à toi de jouer — tu crées un formulaire lead magnet de A à Z pour ta formation.

---

**Points clés** :
- 3 méthodes : shortcode (universel), widget/bloc (sidebar/footer), popup (conversion)
- Shortcode : [fluentform id="X"] — fonctionne partout dans WordPress
- Widget : Apparence > Widgets > "Fluent Forms Widget" pour sidebar/footer
- Popup : via plugin tiers avec shortcode ou FluentCRM Forms natif
- Placements stratégiques : accueil, sidebar blog, fin d'article, landing page, popup
- Un formulaire = un identifiant — même feed FluentCRM quel que soit l'emplacement

**Mots clés SEO** : afficher formulaire WordPress, shortcode Fluent Forms, formulaire popup WordPress, placer formulaire capture email site

---

### Leçon 4.7 — Exercice : Crée un formulaire lead magnet pour ta formation

**Type** : Exercice pratique (consignes écrites)
**Durée estimée** : 30-40 min

---

## Objectif

Créer un formulaire lead magnet complet, connecté à FluentCRM avec segmentation automatique. À la fin de cet exercice, tu auras un formulaire fonctionnel qui capture des leads, les tague dans FluentCRM et les ajoute à la bonne liste — prêt à déclencher des automations.

## Prérequis

- Fluent Forms installé et actif (Pro recommandé pour la logique conditionnelle)
- FluentCRM installé et actif
- Au moins 1 liste et 2 tags créés dans FluentCRM
- Accès admin à ton site WordPress
- Un lead magnet en tête (guide PDF, checklist, mini-formation, template)

> **Pas d'idée de lead magnet ?** Utilise l'un de ces exemples :
> - "Guide gratuit : Choisir son LMS WordPress en 2026" → tag "lead-lms"
> - "Checklist : 15 points pour configurer FluentCRM" → tag "lead-crm"
> - "Template : Séquence email de bienvenue" → tag "lead-automation"
> Choisis celui qui correspond à ta thématique.

## Étapes

### 1. Crée le formulaire dans Fluent Forms

- Va dans Fluent Forms > New Form > Blank Form
- Nomme-le clairement : "Lead Magnet — [nom du guide]"
- Ajoute les champs :
  - [ ] **Email** (obligatoire, libellé personnalisé)
  - [ ] **Prénom** (obligatoire, First Name uniquement)
  - [ ] **Champ de choix** : un radio ou dropdown pour segmenter (ex: "Quel sujet t'intéresse ?")
- Configure le bouton de soumission :
  - [ ] Texte orienté bénéfice (pas "Submit" ou "Envoyer")

### 2. Configure les réglages du formulaire

- Onglet Settings > Form Settings :
  - [ ] Confirmation : redirection vers une page de remerciement (crée la page si besoin)
  - [ ] Ou message de confirmation clair si pas de page dédiée
- Email Notifications :
  - [ ] Désactive la notification admin (FluentCRM gérera les emails)

### 3. Connecte à FluentCRM avec Integration Feed

- Onglet Integration > FluentCRM :
  - [ ] **Feed principal** : mapping email + prénom, liste, tag par défaut
  - [ ] **Test** : soumets le formulaire avec un email de test, vérifie dans FluentCRM

### 4. Ajoute des tags dynamiques (si champ de choix présent)

- Crée un feed conditionnel par option :
  - [ ] Feed 1 : condition = choix A → tag A
  - [ ] Feed 2 : condition = choix B → tag B
  - [ ] Feed 3 : condition = choix C → tag C
- Teste chaque condition avec un email différent :
  - [ ] Choix A → vérifie tag A dans FluentCRM
  - [ ] Choix B → vérifie tag B dans FluentCRM

### 5. Ajoute de la logique conditionnelle au formulaire (optionnel, Pro)

- [ ] Ajoute un champ conditionnel qui n'apparaît que pour un choix spécifique
- [ ] Vérifie en preview que l'affichage est correct

### 6. Place le formulaire sur ton site

- [ ] Place le formulaire avec au moins 2 méthodes différentes (shortcode + widget, ou shortcode + popup)
- [ ] Vérifie le rendu côté visiteur sur desktop et mobile

### 7. Test final end-to-end

- [ ] Remplis le formulaire depuis une page de ton site (pas depuis la preview)
- [ ] Vérifie dans FluentCRM : contact créé, bon tag, bonne liste, bons champs
- [ ] Vérifie la page de remerciement (ou le message de confirmation)

## Critères de validation

- [ ] Le formulaire a au minimum 2 champs (email + prénom) et un bouton personnalisé
- [ ] L'Integration Feed FluentCRM est active et fonctionnelle
- [ ] Le contact de test apparaît dans FluentCRM avec le bon tag et la bonne liste
- [ ] Le formulaire est placé sur au moins une page du site
- [ ] Le rendu est propre sur desktop et mobile
- [ ] Le message/page de confirmation s'affiche après soumission

## Bonus (optionnel)

- [ ] Ajoute un champ caché "Source" avec la valeur de la page (pour tracker l'origine du lead)
- [ ] Configure un champ conditionnel qui affiche une question différente selon le choix
- [ ] Place le formulaire dans un popup avec déclencheur exit-intent
- [ ] Mappe un champ personnalisé FluentCRM (ex: "Niveau" ou "Objectif")

---

### Leçon 4.8 — Quiz : Valide tes acquis M4

**Type** : Quiz TutorLMS (8 questions)
**Seuil de réussite** : 80%

---

**Question 1** : Quel est l'éditeur commun entre Fluent Forms et FluentCRM ?

- A) Developer Express
- B) WPManageNinja *(bonne réponse)*
- C) Awesome Motive
- D) Starter Templates

---

**Question 2** : Combien de champs minimum recommande-t-on pour un formulaire de capture email ?

- A) 1 (email uniquement)
- B) 2 (email + prénom) *(bonne réponse)*
- C) 3 (email + prénom + nom)
- D) 4 (email + prénom + nom + téléphone)

---

**Question 3** : Dans l'Integration Feed, quel mapping est obligatoire pour créer un contact FluentCRM ?

- A) Prénom → First Name
- B) Nom → Last Name
- C) Email → Email *(bonne réponse)*
- D) Téléphone → Phone

---

**Question 4** : Comment mettre en place un tag dynamique dans Fluent Forms ?

- A) En créant un seul feed avec plusieurs tags sélectionnés
- B) En créant un feed conditionnel par tag, chacun avec sa propre condition *(bonne réponse)*
- C) En utilisant un champ caché qui calcule le tag automatiquement
- D) En activant le mode "Auto-Tag" dans les réglages de Fluent Forms

---

**Question 5** : Où se configure la logique conditionnelle d'un champ dans Fluent Forms ?

- A) Dans les réglages globaux du formulaire
- B) Dans l'onglet Integration du formulaire
- C) Dans l'onglet Advanced du champ lui-même *(bonne réponse)*
- D) Dans FluentCRM > Settings > Forms

---

**Question 6** : Quel shortcode permet d'afficher un formulaire Fluent Forms ?

- A) [contact-form id="3"]
- B) [fluentform id="3"] *(bonne réponse)*
- C) [form name="lead-magnet"]
- D) [fluent-crm form="3"]

---

**Question 7** : Quelle est la différence principale entre les opt-in forms natifs FluentCRM et Fluent Forms ?

- A) FluentCRM est payant, Fluent Forms est gratuit
- B) Fluent Forms offre la logique conditionnelle et les champs personnalisés, pas les opt-in natifs *(bonne réponse)*
- C) Les opt-in natifs supportent plus de champs que Fluent Forms
- D) Fluent Forms ne peut pas se connecter à FluentCRM

---

**Question 8** : Quel statut de contact choisir dans le feed pour activer le double opt-in ?

- A) Subscribed
- B) Pending *(bonne réponse)*
- C) Unsubscribed
- D) Active

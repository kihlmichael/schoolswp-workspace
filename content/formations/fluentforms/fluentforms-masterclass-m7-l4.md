# Script video — Module 7, Lecon 4 : FluentForms + FluentSupport

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 — Ecosysteme et integrations
**Lecon** : 4/9 — FluentForms + FluentSupport
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config integration, slide schema flux
**Objectif** : Transformer les soumissions de formulaire en tickets de support automatiquement

---

**[INTRO — face camera]**

Tes clients ont un probleme. Ils remplissent un formulaire sur ton site. Toi, tu recois un email. Tu le lis, tu reponds. Si le probleme est complexe, ca part en aller-retour d'emails. Un mois plus tard, tu ne retrouves plus l'historique.

FluentSupport transforme chaque soumission de formulaire en ticket de support structure. Numero de ticket, historique, statut, priorite. Le support professionnel sans la complexite d'un Zendesk.

**[SECTION 1 — slide "FluentSupport en bref"]**

FluentSupport, c'est un helpdesk natif WordPress.

Chaque demande cree un ticket avec un numero unique. Le client recoit ce numero et peut suivre l'avancement. Toi, tu as un tableau de bord avec tous les tickets ouverts, en cours, et resolus.

L'historique de la conversation est lie au ticket. Plus de recherche dans Gmail pour retrouver un email. Tout est centralise.

Et comme c'est natif WordPress, les contacts FluentCRM sont lies aux tickets FluentSupport. Tu vois l'historique complet du client — ses achats, ses formulaires remplis, ses tickets.

**[SECTION 2 — screencast "Configurer l'integration"]**

Prerequis : FluentSupport installe et actif. Un "mailbox" (boite de support) cree dans FluentSupport.

Ouvre ton formulaire dans FluentForms. On va prendre un formulaire "Demande de support".

Champs : Nom, Email, Select "Categorie" (Bug, Question, Demande de fonctionnalite), Textarea "Decris ton probleme".

Va dans Settings, Marketing & CRM Integrations. Tu vois FluentSupport dans la liste. Clique pour ajouter un feed.

**[SECTION 3 — screencast "Mapper les champs"]**

Le feed FluentSupport te demande de mapper les champs.

Email du client : mappe vers le champ Email du formulaire. C'est l'identifiant du ticket.

Titre du ticket : tu peux mapper vers un champ du formulaire (par exemple un champ "Objet") ou utiliser un texte fixe combine avec une valeur dynamique. Exemple : "Support — {inputs.categorie}".

Contenu du ticket : mappe vers le Textarea "Decris ton probleme".

Priorite : tu peux la definir de facon fixe ("Normal") ou la mapper vers un champ du formulaire. Si tu ajoutes un champ Select "Urgence" avec les options Normal / Haute / Critique, mappe-le a la priorite du ticket.

Mailbox : selectionne la boite de support dans laquelle le ticket sera cree.

**[SECTION 4 — screencast "L'experience client"]**

Le client remplit le formulaire et soumet. Voici ce qui se passe.

FluentForms enregistre la soumission. Le feed FluentSupport cree un ticket. Le client recoit un email : "Ton ticket #1234 a ete cree. Notre equipe va te repondre sous 24h."

Le client peut repondre directement a cet email — la reponse est ajoutee au ticket dans FluentSupport. Ou il peut se connecter a son espace client WordPress pour voir le ticket et ajouter des messages.

De ton cote, tu vois le ticket dans FluentSupport. Tu reponds. Le client recoit ta reponse par email. Tout l'historique est dans le ticket.

Quand le probleme est resolu, tu changes le statut en "Resolved". Le client recoit une notification. Le ticket est archive.

**[SECTION 5 — screencast "Feed conditionnel"]**

Tu peux creer des tickets differents selon les reponses.

Si la categorie est "Bug" → priorite Haute, assign to "Support technique".
Si la categorie est "Question" → priorite Normal, assign to "Support general".
Si la categorie est "Demande de fonctionnalite" → priorite Basse, assign to "Produit".

Configure ca avec des feeds conditionnels — un feed par categorie, chacun avec ses parametres.

Le bon ticket arrive a la bonne personne avec la bonne priorite. Pas de tri manuel.

**[SECTION 6 — slide "Flux complet"]**

Le client remplit le formulaire de support. FluentForms cree le ticket dans FluentSupport. FluentCRM est notifie — le contact recoit le tag "has-support-ticket". L'equipe recoit une notification. Le client recoit un email avec son numero de ticket. L'echange se fait via ticket. Resolution. Tag "ticket-resolved" dans FluentCRM.

Tout est trace. Tout est centralise. Et FluentCRM sait qui a eu des problemes et qui n'en a pas — utile pour le scoring et la segmentation.

**[OUTRO — face camera]**

FluentForms et FluentSupport sont connectes. Tes soumissions deviennent des tickets structures. Dans la prochaine lecon, on sort de l'ecosysteme WPManageNinja pour connecter FluentForms a Brevo — le service d'email marketing populaire en France.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- FluentSupport : helpdesk natif WordPress (tickets, historique, statuts)
- Feed FluentSupport : soumission formulaire → creation automatique de ticket
- Mapping : email, titre, contenu, priorite, mailbox
- Feeds conditionnels : priorite et assignation selon la categorie
- Le client suit son ticket par email ou depuis son espace WordPress
- Tags FluentCRM : "has-support-ticket" et "ticket-resolved" pour le suivi

**Mots cles SEO** : FluentSupport FluentForms, ticket support WordPress, helpdesk WordPress, formulaire support WordPress

---

**Notes de production** :
- Face camera : intro (le probleme des emails support) + outro (transition Brevo)
- Screencast : config feed FluentSupport + demo ticket (~5 min)
- Slides : 2 slides (FluentSupport en bref + flux complet)
- Ton : oriente professionnalisme — montrer la difference entre email et ticket

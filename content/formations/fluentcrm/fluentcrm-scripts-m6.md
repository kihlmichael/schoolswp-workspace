# Scripts video -- Module 6 : Automation funnels -- fondamentaux

**Formation** : Maitriser FluentCRM
**Module** : M6 -- Automation funnels : fondamentaux (Premium)
**Lecons** : 7 videos + 1 exercice + 1 quiz
**Duree totale** : ~55 min de video
**Date** : 2026-03-23

---

## Lecon 6.1 -- Comprends le vocabulaire : triggers, actions, goals, conditionals

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera + slides vocabulaire + screencast editeur automation FluentCRM

---

**[INTRO -- face camera]**

Tu vas construire tes premiers funnels d'automation. Mais avant de toucher a l'editeur, tu dois maitriser quatre mots. Quatre concepts qui reviennent partout. Si tu les comprends bien, tout le reste devient logique.

**[ECRAN -- slide "Les 4 piliers d'une automation"]**

Une automation FluentCRM, c'est un enchainement de quatre types d'elements.

Premier element : le trigger. C'est l'evenement declencheur. Le point de depart. "Un contact soumet un formulaire", "Un tag est applique", "Un contact est ajoute a une liste". Sans trigger, pas d'automation. C'est le "quand".

Deuxieme element : l'action. C'est ce que tu fais une fois le trigger declenche. Envoyer un email. Appliquer un tag. Creer un utilisateur WordPress. Attendre 3 jours. C'est le "quoi".

Troisieme element : le goal. C'est ton objectif. Le point d'arrivee souhaite. Par exemple : "le contact a achete la formation". Si le goal est atteint, le contact saute directement a cette etape, meme s'il n'a pas parcouru toutes les actions intermediaires. C'est le "ou tu veux l'amener".

Quatrieme element : le conditional. C'est un embranchement. Tu poses une question a laquelle la reponse est oui ou non. "Le contact a-t-il le tag premium ?" Oui : chemin A. Non : chemin B. C'est le "si".

**[ECRAN -- screencast : editeur automation FluentCRM]**

Voyons ces quatre elements dans l'editeur.

[Ouverture d'une automation existante dans FluentCRM]

Le trigger est toujours en haut. C'est le premier bloc. Tu ne peux pas ajouter d'element avant.

En dessous, tu enchaines les actions. Chaque action est un bloc que tu ajoutes avec le bouton "+".

Le goal se reconnait a son icone cible. Il peut etre place n'importe ou dans la sequence.

Et le conditional cree deux branches visuelles : une branche "oui" a gauche, une branche "non" a droite.

[Survol de chaque type de bloc dans l'editeur]

**[ECRAN -- slide "Analogie : le GPS"]**

Pour retenir : pense a un GPS.

Le trigger, c'est ton point de depart. Tu montes dans la voiture.

Les actions, ce sont les instructions. Tourne a gauche, continue tout droit, prends la sortie.

Les conditionals, ce sont les embranchements. Autoroute ou nationale ?

Et le goal, c'est ta destination. Si tu trouves un raccourci, le GPS te fait sauter les etapes intermediaires.

**[FACE CAMERA]**

Quatre mots. Trigger, action, goal, conditional. Tu les retrouveras dans chaque lecon de ce module. Grave-les.

**[TRANSITION]**

Maintenant que tu as le vocabulaire, on va decouvrir l'editeur visuel ou tout ca prend forme.

---

**Points cles** :
- Trigger = evenement declencheur (le "quand")
- Action = ce que l'automation execute (le "quoi")
- Goal = objectif que le contact doit atteindre (peut court-circuiter des etapes)
- Conditional = embranchement oui/non (le "si")
- Analogie GPS : depart, instructions, embranchements, destination

**Mots cles SEO** : automation FluentCRM, trigger action goal, vocabulaire automation email, funnel email WordPress

---

## Lecon 6.2 -- Decouvre l'editeur d'automation visuel

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automations > Editeur visuel

---

**[INTRO -- face camera]**

L'editeur d'automation de FluentCRM est visuel. Tu construis ton funnel en glissant des blocs les uns apres les autres, comme un organigramme. On va faire le tour complet de l'interface.

**[ECRAN -- screencast : FluentCRM > Automations]**

Va dans FluentCRM, puis Automations dans le menu lateral.

[Clic sur Automations]

Tu arrives sur la liste de tes automations. Pour l'instant, elle est peut-etre vide. Clique sur "Create a New Automation".

[Clic sur Create a New Automation]

FluentCRM te propose des templates pre-faits. Tu en as pour le onboarding, la relance, le tagging automatique. C'est pratique pour demarrer, mais pour bien comprendre, on va partir de zero.

Selectionne "Start from Scratch".

[Clic sur Start from Scratch]

**[ECRAN -- screencast : nommage et organisation]**

Premiere chose : donne un nom a ton automation. Ce nom est interne, tes contacts ne le verront pas.

Mon conseil : utilise un prefixe par categorie. Par exemple : "ONBOARD -- Bienvenue formation gratuite" ou "VENTE -- Upsell premium J+7". Ca te permet de retrouver tes automations quand tu en auras 20 ou 30.

[Saisie du nom de l'automation]

Tu peux aussi ajouter un label. Les labels sont des etiquettes colorees pour organiser visuellement ta liste d'automations. Clique sur le champ "Labels" et cree un nouveau label ou selectionne un existant.

[Selection d'un label]

**[ECRAN -- screencast : choix du trigger]**

Maintenant, tu choisis ton trigger. FluentCRM te propose une liste.

[Affichage de la liste des triggers]

On va prendre un trigger simple : "Tag Applied". Ca signifie : quand un tag est applique a un contact, l'automation demarre.

[Selection de Tag Applied]

Configure le tag. Par exemple : "inscrit-gratuit".

[Configuration du trigger]

Clique sur "Save Settings". Ton trigger est en place.

**[ECRAN -- screencast : ajout d'actions]**

En dessous du trigger, tu vois un bouton "+". C'est par la que tu ajoutes des actions.

[Clic sur le "+"]

Le panneau lateral s'ouvre avec toutes les actions disponibles. Tu vois les categories : Actions, Conditionals, Goals.

[Affichage du panneau lateral]

Ajoute une action "Send Custom Email". C'est l'action la plus courante.

[Selection de Send Custom Email]

Tu arrives sur l'editeur d'email integre. Tu rediges ton email directement dans l'automation, avec les memes blocs que pour une campagne. Le sujet, le pre-header, le contenu. Tout est la.

[Vue rapide de l'editeur d'email]

Sauvegarde et ferme. Ton premier bloc action apparait dans le funnel.

**[ECRAN -- screencast : navigation dans l'editeur]**

Quelques raccourcis pour naviguer.

Tu peux zoomer et dezoomer avec la molette ou les boutons +/- en bas a droite.

Tu peux deplacer la vue en cliquant-glissant sur le fond.

Le bouton "Fit to Screen" recentre tout le funnel dans ton ecran.

Et chaque bloc est cliquable. Un clic ouvre ses parametres dans le panneau lateral.

[Demonstration zoom, deplacement, clic sur un bloc]

**[ECRAN -- screencast : statut Draft vs Published]**

Dernier point important. Une automation nouvellement creee est en mode "Draft". Elle ne fait rien.

Pour l'activer, tu dois la passer en "Published" avec le bouton en haut a droite.

[Clic sur le toggle Draft/Published]

Tant qu'elle est en Draft, tu peux modifier tout ce que tu veux sans risque. C'est ton bac a sable.

Une fois en Published, chaque nouveau contact qui remplit la condition du trigger entrera dans le funnel.

**[FACE CAMERA]**

L'editeur est intuitif une fois que tu as compris le principe du "+" pour ajouter des blocs. Dans les prochaines lecons, on va detailler chaque categorie : les triggers, les actions, puis les conditionals.

**[TRANSITION]**

On commence par les triggers. C'est le point de depart de toute automation.

---

**Points cles** :
- Creer une automation : Automations > Create > Start from Scratch
- Nommer avec un prefixe par categorie (ONBOARD, VENTE, RELANCE...)
- Les labels permettent d'organiser visuellement la liste
- Le trigger est toujours le premier element
- Draft = inactive, Published = active (les contacts entrent des que le trigger est rempli)
- Naviguer : molette pour zoomer, clic-glisse pour deplacer, Fit to Screen pour recentrer

**Mots cles SEO** : editeur automation FluentCRM, creer automation WordPress, funnel visuel FluentCRM, editeur email automation

---

## Lecon 6.3 -- Les triggers CRM : form submitted, tag applied, list added

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automation Editor > Triggers

---

**[INTRO -- face camera]**

Le trigger, c'est la porte d'entree de ton automation. FluentCRM en propose une vingtaine, repartis en trois categories. On va les voir une par une pour que tu saches exactement quand utiliser lequel.

**[ECRAN -- slide "3 categories de triggers"]**

Premiere categorie : les triggers CRM. Ce sont les plus utilises. Ils se declenchent sur des actions liees a tes contacts dans FluentCRM.

Deuxieme categorie : les triggers WordPress. Ils se declenchent sur des evenements WordPress : connexion, inscription, changement de role.

Troisieme categorie : les triggers d'integration. Ils se declenchent quand un evenement se produit dans un plugin tiers : WooCommerce, TutorLMS, LearnDash, MemberPress.

**[ECRAN -- screencast : triggers CRM dans l'editeur]**

Commencons par les triggers CRM. Ouvre l'editeur d'automation et clique sur le bloc trigger.

[Affichage de la liste des triggers CRM]

**Tag Applied.** L'automation demarre quand un tag specifique est applique a un contact. C'est le trigger le plus polyvalent. Tu peux l'utiliser pour tout : onboarding, segmentation, relance.

Par exemple : tu appliques le tag "lead-chaud" manuellement ou via un formulaire, et l'automation se declenche.

[Configuration du trigger Tag Applied avec le tag "lead-chaud"]

**Tag Removed.** L'inverse. L'automation demarre quand un tag est retire. Utile pour detecter un changement de statut. Par exemple : quand le tag "abonne-actif" est retire, tu declenches une sequence de reactivation.

**List Applied.** L'automation demarre quand un contact est ajoute a une liste specifique. Par exemple : le contact est ajoute a la liste "Formation gratuite" via un formulaire d'inscription.

[Configuration du trigger List Applied]

**List Removed.** L'automation demarre quand un contact est retire d'une liste. Moins courant, mais utile pour les scenarios de desabonnement.

**Contact Created.** L'automation demarre des qu'un nouveau contact est cree dans FluentCRM, quelle que soit la source : import, formulaire, API.

**[ECRAN -- slide "Triggers WordPress"]**

Maintenant, les triggers WordPress. Ceux-la sont disponibles avec FluentCRM Pro.

**New User Sign Up.** L'automation demarre quand un utilisateur WordPress est cree. Pas un contact FluentCRM, un utilisateur WordPress. La difference est importante. Tu peux filtrer par role : subscriber, student, customer.

**User Login.** L'automation demarre quand un utilisateur se connecte a WordPress. Utile pour declencher un message de bienvenue apres la premiere connexion.

**[ECRAN -- slide "Triggers d'integration"]**

Enfin, les triggers d'integration. Ils dependent des plugins installes.

Avec **TutorLMS** : "Student Enrolled in a Course", "Student Completed a Course", "Student Completed a Lesson".

Avec **WooCommerce** : "New Order (Specific Product)", "Order Status Changed", "Order Completed".

Avec **Fluent Forms** : "Form Submitted". C'est le trigger que tu utiliseras le plus souvent pour capturer des leads.

[Affichage de quelques triggers d'integration]

**[ECRAN -- screencast : configuration avancee d'un trigger]**

Un point important sur la configuration. Chaque trigger a une option "Run For" :

"All" : l'automation se declenche pour tous les contacts, y compris ceux qui sont deja dans l'automation.

"New" : l'automation ne se declenche que pour les contacts qui n'ont jamais ete dans cette automation.

[Affichage de l'option Run For]

En general, choisis "New" pour eviter qu'un contact boucle indefiniment dans le meme funnel.

**[FACE CAMERA]**

Mon conseil : commence par trois triggers. "Form Submitted" pour capturer les leads. "Tag Applied" pour declencher des sequences manuellement. "List Applied" pour les automations liees a une segmentation. Ces trois-la couvrent 80% des cas.

**[TRANSITION]**

Tu sais comment demarrer une automation. Maintenant, on va voir ce que tu peux faire une fois que le contact est entre : les actions.

---

**Points cles** :
- 3 categories de triggers : CRM (tag, list, contact), WordPress (user signup, login), Integration (WooCommerce, TutorLMS, Fluent Forms)
- Tag Applied est le trigger le plus polyvalent
- Form Submitted (Fluent Forms) est le plus courant pour la capture de leads
- Option "Run For" : choisir "New" pour eviter les boucles
- 3 triggers a maitriser en priorite : Form Submitted, Tag Applied, List Applied

**Mots cles SEO** : triggers FluentCRM, declencheur automation, tag applied FluentCRM, form submitted automation WordPress

---

## Lecon 6.4 -- Les actions : send email, apply tag, wait, create WP user

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automation Editor > Actions

---

**[INTRO -- face camera]**

Le trigger fait entrer le contact dans l'automation. Les actions definissent ce qui lui arrive ensuite. FluentCRM en propose une quinzaine. On va voir les plus importantes et celles que tu utiliseras au quotidien.

**[ECRAN -- screencast : panneau des actions dans l'editeur]**

Dans l'editeur d'automation, clique sur le "+" pour voir les actions disponibles.

[Affichage du panneau lateral avec les actions]

On va les parcourir par ordre de frequence d'utilisation.

**[ECRAN -- screencast : Send Custom Email]**

**Send Custom Email.** C'est l'action numero un. Tu crees un email directement dans l'automation. Tu as le meme editeur que pour les campagnes : sujet, pre-header, contenu avec blocs Gutenberg, smart codes.

[Ouverture de l'editeur d'email dans l'automation]

La difference avec une campagne : cet email est envoye automatiquement, au moment ou le contact atteint cette etape du funnel.

Tu peux aussi utiliser "Send Sequence Email" si tu veux envoyer un email qui fait partie d'une sequence existante. Mais pour les automations, le Custom Email offre plus de flexibilite.

**[ECRAN -- screencast : Wait]**

**Wait.** C'est l'action de temporisation. Tu definis un delai avant l'action suivante.

[Configuration d'un delai de 3 jours]

Les options : minutes, heures, jours. Tu peux aussi programmer a un jour et une heure precis. Par exemple : "attendre jusqu'a lundi prochain a 9h".

La question que tout le monde pose : quel delai mettre entre deux emails ? Il n'y a pas de regle absolue. Mais voici un repere : pour une sequence de bienvenue, 1 a 2 jours entre chaque email. Pour une sequence de vente, 2 a 3 jours. Si tu espaces trop, ton contact t'oublie. Si tu enchaines trop vite, tu passes pour du spam.

**[ECRAN -- screencast : Apply Tag / Remove Tag]**

**Apply Tag.** Ajoute un tag au contact. C'est la pour la segmentation automatique. Par exemple : apres avoir ouvert l'email 3, tu appliques le tag "engage-sequence-welcome".

[Configuration Apply Tag avec le tag "engage-sequence-welcome"]

**Remove Tag.** Retire un tag. Utile pour nettoyer les segments. Par exemple : une fois que le contact a termine la sequence, tu retires le tag "en-onboarding".

**[ECRAN -- screencast : Apply List / Remove List]**

**Apply to List / Remove from List.** Meme principe, mais pour les listes. Tu ajoutes ou retires le contact d'une liste specifique.

Combine avec les tags, ca te donne un systeme de segmentation puissant. Le tag pour le comportement ("a-clique-upsell"), la liste pour le statut ("Clients premium").

**[ECRAN -- screencast : Create WordPress User]**

**Create WordPress User.** C'est une action specifique a FluentCRM Pro.

[Configuration de l'action Create WordPress User]

Elle cree un compte utilisateur WordPress pour le contact. Tu definis le role : subscriber, student, customer. FluentCRM genere automatiquement un mot de passe et peut envoyer un email de notification.

Cas d'usage concret dans le contexte schoolsWP : un visiteur s'inscrit a ta formation gratuite via Fluent Forms. FluentCRM cree automatiquement son compte WordPress avec le role "Student". Le contact recoit un email avec ses identifiants. Il peut se connecter et acceder a la formation sur TutorLMS. Zero intervention manuelle.

[Affichage de la configuration complete]

**[ECRAN -- screencast : autres actions utiles]**

Quelques actions supplementaires a connaitre.

**End This Funnel.** Force la sortie du contact. Utile apres un conditional : si le contact a deja achete, tu le sors du funnel de vente.

**Cancel Automations.** Annule d'autres automations en cours pour ce contact. Par exemple : le contact achete, tu annules la sequence de relance.

**Update Contact Property.** Modifie un champ du profil contact. Tu peux changer le statut, le prenom, un champ personnalise.

**Send Notification to Admin.** Envoie un email de notification a l'administrateur ou a une adresse specifique. Pratique pour etre alerte quand un contact atteint une etape importante.

**[FACE CAMERA]**

Les actions que tu utiliseras dans 90% de tes automations : Send Custom Email, Wait, Apply Tag, et Remove Tag. Si tu fais du e-learning, ajoute Create WordPress User. C'est ton kit de base.

**[TRANSITION]**

Tu as les triggers et les actions. Il manque une piece : comment creer des chemins differents selon le comportement du contact. C'est le role des conditionals.

---

**Points cles** :
- Send Custom Email : action la plus utilisee, email directement dans l'automation
- Wait : delai entre les actions (1-2 jours pour bienvenue, 2-3 jours pour vente)
- Apply Tag / Remove Tag : segmentation automatique par comportement
- Create WordPress User : cree un compte WP depuis l'automation (Pro)
- End This Funnel et Cancel Automations pour gerer les sorties et les conflits entre automations
- Kit de base : Send Email + Wait + Apply Tag + Remove Tag

**Mots cles SEO** : actions automation FluentCRM, send email automation, wait delai FluentCRM, creer utilisateur WordPress FluentCRM

---

## Lecon 6.5 -- Les conditionnels : cree des chemins oui/non

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automation Editor > Conditionals

---

**[INTRO -- face camera]**

Jusqu'ici, tes automations suivent un chemin lineaire. Le contact entre, il recoit les actions les unes apres les autres. Mais dans la vraie vie, tous tes contacts ne se comportent pas pareil. Les conditionals te permettent de creer des embranchements : un chemin pour ceux qui font X, un autre pour ceux qui ne le font pas.

**[ECRAN -- screencast : ajout d'un conditional dans l'editeur]**

Dans l'editeur d'automation, clique sur "+" et selectionne "If/Else (Has Tag)".

[Selection du bloc If/Else dans le panneau]

Tu vois deux branches apparaitre. A gauche, la branche "Yes". A droite, la branche "No".

[Affichage visuel des deux branches]

C'est aussi simple que ca. Tu poses une condition, et le contact suit le chemin correspondant.

**[ECRAN -- screencast : types de conditionals]**

FluentCRM propose plusieurs types de conditions.

**Has Tag.** Le contact a-t-il un tag specifique ? C'est la condition la plus courante. Exemple : "Le contact a-t-il le tag client-premium ?"

[Configuration Has Tag avec "client-premium"]

**In List.** Le contact est-il dans une liste specifique ? Exemple : "Le contact est-il dans la liste Formation Payante ?"

**Has User Role.** Le contact a-t-il un role WordPress specifique ? Exemple : "Le contact est-il un Student ?"

**Email Activity.** Le contact a-t-il ouvert ou clique dans un email precedent de cette meme automation ? C'est extremement puissant. Tu peux adapter la suite du funnel en fonction de l'engagement.

[Configuration Email Activity : "Has opened email step 2"]

**[ECRAN -- slide "Exemple concret : conditional apres un email"]**

Voici un cas reel. Tu envoies un email avec un lien vers ton offre premium.

Tu ajoutes un "Wait" de 2 jours.

Puis un conditional "Email Activity" : le contact a-t-il clique sur le lien ?

Branche Oui : tu envoies un email de confirmation avec les details de l'offre et un lien direct vers le paiement.

Branche Non : tu envoies un email de relance avec un angle different. Peut-etre un temoignage, ou un rappel des benefices.

[Affichage du funnel complet avec les deux branches]

**[ECRAN -- screencast : imbrication de conditionals]**

Tu peux imbriquer des conditionals. Un conditional dans une branche d'un autre conditional.

[Demonstration d'un conditional imbrique]

Mais attention : ne surcharge pas. Deux niveaux d'imbrication, c'est le maximum raisonnable. Au-dela, ton funnel devient illisible et difficile a maintenir. Si tu as besoin de plus de branches, decoupe en plusieurs automations separees.

**[ECRAN -- screencast : convergence des branches]**

Apres un conditional, tu peux faire converger les deux branches vers la meme suite d'actions. Pour ca, tu ajoutes les memes actions a la fin de chaque branche.

Ou tu utilises l'action "End This Funnel" dans une branche si tu veux sortir certains contacts.

[Demonstration de la convergence]

**[FACE CAMERA]**

Les conditionals transforment une automation basique en funnel intelligent. Le contact ne recoit que les messages pertinents pour lui. Commence simple : un seul conditional par automation. Tu complexifieras quand tu maitriseras les bases.

**[TRANSITION]**

Tu as les triggers, les actions, les conditionals. Tu as tous les ingredients. Dans la prochaine lecon, on assemble tout ca pour construire ton premier vrai funnel.

---

**Points cles** :
- Conditional = embranchement Oui/Non dans l'automation
- 4 types principaux : Has Tag, In List, Has User Role, Email Activity
- Email Activity permet d'adapter le funnel selon l'engagement (ouverture, clic)
- Maximum 2 niveaux d'imbrication pour garder le funnel lisible
- Commence avec un seul conditional par automation, puis complexifie progressivement

**Mots cles SEO** : conditional FluentCRM, if else automation email, embranchement funnel, segmentation comportementale FluentCRM

---

## Lecon 6.6 -- Construis ton premier funnel : inscription → bienvenue → upsell

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automation Editor (construction pas a pas)

---

**[INTRO -- face camera]**

On passe a la pratique. Tu vas construire un funnel complet de A a Z. Le scenario : un visiteur s'inscrit a ta formation gratuite. Il recoit une sequence de bienvenue. Puis, au bout de quelques jours, une proposition pour passer en premium. C'est le funnel freemium classique de schoolsWP.

**[ECRAN -- slide "Architecture du funnel"]**

Voici le plan du funnel avant de le construire.

Trigger : formulaire d'inscription soumis.

Etape 1 : appliquer le tag "inscrit-gratuit" + ajouter a la liste "Formation Gratuite".

Etape 2 : envoyer l'email de bienvenue avec les identifiants.

Etape 3 : attendre 2 jours.

Etape 4 : envoyer un email de valeur (conseil, ressource, astuce).

Etape 5 : attendre 3 jours.

Etape 6 : envoyer l'email d'upsell vers la formation premium.

Etape 7 : attendre 2 jours.

Etape 8 : conditional -- le contact a-t-il clique sur le lien de l'offre ?

Branche Oui : envoyer un email de rappel avec un lien direct.

Branche Non : envoyer un email de relance avec un temoignage.

Fin du funnel.

**[ECRAN -- screencast : creation de l'automation]**

Allons-y. Va dans Automations > Create a New Automation > Start from Scratch.

[Clic Create > Start from Scratch]

Nomme-la : "ONBOARD -- Inscription formation gratuite → upsell premium".

[Saisie du nom]

Ajoute le label "Onboarding".

[Selection du label]

**[ECRAN -- screencast : trigger]**

Pour le trigger, selectionne "Form Submitted" (si tu utilises Fluent Forms). Choisis ton formulaire d'inscription a la formation gratuite.

[Configuration du trigger : Form Submitted > Formulaire inscription formation gratuite]

Option "Run For" : selectionne "New" pour eviter les doublons.

Sauvegarde.

**[ECRAN -- screencast : etape 1 -- tag + liste]**

Clique sur "+". Selectionne "Apply Tag". Choisis le tag "inscrit-gratuit".

[Configuration Apply Tag]

Clique encore sur "+". Selectionne "Apply to List". Choisis la liste "Formation Gratuite".

[Configuration Apply to List]

Ces deux actions se declenchent instantanement, l'une apres l'autre. Pas besoin de delai entre elles.

**[ECRAN -- screencast : etape 2 -- email de bienvenue]**

Clique sur "+". Selectionne "Send Custom Email".

[Ouverture de l'editeur d'email]

Sujet : "Bienvenue dans la formation -- tes acces sont prets"

Pre-header : "Tout est en place. Connecte-toi et commence maintenant."

Corps de l'email : un message court. Le lien de connexion. Les instructions pour acceder a la formation. Et un rappel de ce qu'ils vont apprendre.

[Redaction rapide du contenu]

Sauvegarde.

**[ECRAN -- screencast : etape 3 -- delai + email de valeur]**

Clique sur "+". Selectionne "Wait". Configure : 2 jours.

[Configuration Wait 2 jours]

Clique sur "+". Selectionne "Send Custom Email".

Sujet : "3 erreurs que font 90% des debutants avec WordPress"

C'est ton email de valeur. Tu ne vends rien. Tu donnes un conseil utile. Tu crees de la confiance.

[Configuration rapide de l'email]

Sauvegarde.

**[ECRAN -- screencast : etape 4 -- delai + email upsell]**

Clique sur "+". Selectionne "Wait". Configure : 3 jours.

[Configuration Wait 3 jours]

Clique sur "+". Selectionne "Send Custom Email".

Sujet : "Pret a passer au niveau suivant ?"

C'est ton email d'upsell. Tu presentes la formation premium. Les benefices concrets. Un lien vers la page de vente.

[Configuration rapide de l'email]

Sauvegarde.

**[ECRAN -- screencast : etape 5 -- conditional + branches]**

Clique sur "+". Selectionne "Wait". Configure : 2 jours.

Clique sur "+". Selectionne "If/Else (Email Activity)". Configure : "Has clicked in step" -- et selectionne l'email d'upsell.

[Configuration du conditional Email Activity]

Branche Oui : clique sur le "+" sous la branche Yes. Ajoute "Send Custom Email". Sujet : "Une question sur la formation premium ?" -- un email de relance douce avec un lien direct vers le paiement.

Branche Non : clique sur le "+" sous la branche No. Ajoute "Send Custom Email". Sujet : "Ce qu'en dit Thomas, formateur WordPress depuis 5 ans" -- un email avec un temoignage ou un cas concret.

[Construction des deux branches]

**[ECRAN -- screencast : finalisation]**

A la fin de chaque branche, ajoute "End This Funnel" si tu ne veux pas continuer apres.

Et ajoute "Apply Tag" avec "onboarding-termine" dans chaque branche pour marquer que le contact a parcouru le funnel.

[Ajout des actions finales]

**[ECRAN -- screencast : verification et publication]**

Avant de publier, verifie chaque etape en cliquant dessus. Relis les emails. Verifie les delais. Verifie les tags.

Quand tout est bon, passe l'automation en "Published".

[Clic sur Published]

**[FACE CAMERA]**

Ton premier funnel est en place. Chaque nouveau inscrit va recevoir automatiquement ta sequence de bienvenue et ton upsell. Tu n'as plus rien a faire manuellement.

Ce funnel est un modele que tu peux dupliquer et adapter. Change les emails, change les delais, change le conditional. La structure reste la meme.

**[TRANSITION]**

Ton funnel tourne. Mais comment savoir s'il fonctionne ? Dans la prochaine lecon, on va lire les rapports d'automation.

---

**Points cles** :
- Funnel freemium : inscription gratuit → sequence valeur → offre premium → relance
- Nommage : prefixe + description (ONBOARD -- Inscription formation gratuite → upsell premium)
- Delais recommandes : 2 jours (bienvenue → valeur), 3 jours (valeur → upsell), 2 jours (upsell → relance)
- Conditional Email Activity pour adapter la relance selon le comportement
- Toujours ajouter un tag de fin pour marquer le parcours complet
- Verifier chaque etape avant de publier

**Mots cles SEO** : funnel FluentCRM, automation bienvenue, upsell email WordPress, onboarding automation, sequence email FluentCRM

---

## Lecon 6.7 -- Lis les rapports d'automation

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Automations > Report

---

**[INTRO -- face camera]**

Ton funnel tourne depuis quelques jours. Des contacts entrent, recoivent des emails. Mais est-ce que ca marche ? FluentCRM te donne des rapports detailles pour chaque automation. On va apprendre a les lire.

**[ECRAN -- screencast : FluentCRM > Automations > liste]**

Retourne dans Automations. Sur la liste, tu vois deja des chiffres a cote de chaque automation.

[Affichage de la liste des automations avec les compteurs]

Le nombre de contacts "In Progress" : ceux qui sont actuellement dans le funnel, entre deux etapes.

Le nombre de contacts "Completed" : ceux qui ont atteint la fin du funnel.

Ces deux chiffres te donnent un apercu rapide sans meme ouvrir l'automation.

**[ECRAN -- screencast : vue interne du funnel]**

Ouvre ton automation. Sur chaque bloc, tu vois le nombre de contacts qui ont passe cette etape.

[Affichage des compteurs sur chaque bloc du funnel]

C'est la que tu detectes les problemes. Si 100 contacts entrent par le trigger et que seulement 60 passent l'etape "Email de bienvenue", il y a un souci. Peut-etre que 40 contacts avaient un email invalide. Peut-etre que le delai est trop long et ils se desabonnent avant.

**[ECRAN -- screencast : stats d'un email dans l'automation]**

Clique sur un bloc "Send Custom Email". Dans les parametres, tu trouves un onglet "Stats" ou "Report".

[Ouverture des stats d'un email]

Tu retrouves les memes metriques que pour une campagne : emails envoyes, taux d'ouverture, taux de clic, desabonnements.

Compare les taux entre les differents emails de ton funnel. Si le premier email a 45% d'ouverture et le troisieme seulement 15%, c'est normal : l'engagement diminue au fil de la sequence. Mais si la chute est brutale entre deux emails consecutifs, revois le contenu ou le delai.

**[ECRAN -- screencast : vue des contacts dans le funnel]**

En haut de l'automation, clique sur "Subscribers" ou "Contacts".

[Affichage de la liste des contacts dans l'automation]

Tu vois chaque contact avec son statut : "Active" (en cours), "Completed" (termine), "Cancelled" (arrete).

Tu peux filtrer par statut. Les contacts "Cancelled" meritent une attention particuliere. Pourquoi sont-ils sortis ? Desabonnement ? Erreur d'envoi ? Regarde leur fiche individuelle pour comprendre.

[Clic sur un contact pour voir son parcours]

Sur la fiche du contact, tu vois exactement a quelle etape il se trouve et quand il est passe par chaque bloc.

**[ECRAN -- slide "Les 4 metriques a surveiller"]**

Recapitulons les quatre metriques a surveiller.

Un : le taux d'entree. Combien de contacts entrent par jour ? Si c'est zero, verifie ton trigger et ton formulaire.

Deux : le taux de completion. Quel pourcentage de contacts atteint la fin ? En dessous de 50%, investigue.

Trois : le taux d'ouverture par email. Compare-les entre eux pour reperer les emails faibles.

Quatre : le taux de conversion au conditional. Quel pourcentage prend la branche "Oui" ? C'est ton indicateur de performance pour l'upsell.

**[FACE CAMERA]**

Les rapports ne sont pas la pour decorer. Consulte-les une fois par semaine au minimum. Repere les points de friction. Ajuste les emails, les delais, les conditions. C'est comme ca que tu transformes un funnel correct en funnel performant.

**[TRANSITION]**

Tu maitrises les fondamentaux des automations. Dans la prochaine lecon, tu passes a la pratique avec un exercice guide.

---

**Points cles** :
- Liste des automations : voir In Progress et Completed en un coup d'oeil
- Chaque bloc affiche le nombre de contacts qui l'ont traverse
- Stats par email : ouverture, clic, desabonnement (comme une campagne)
- Contacts : filtrer par Active / Completed / Cancelled
- 4 metriques a surveiller : taux d'entree, taux de completion, ouverture par email, conversion au conditional
- Consulter les rapports une fois par semaine minimum

**Mots cles SEO** : rapports automation FluentCRM, statistiques funnel email, mesurer performance automation, analytics email WordPress

---

## Lecon 6.8 -- Exercice : cree un funnel de bienvenue pour ta formation gratuite

**Duree** : 6 min
**Type** : Exercice guide
**Ecran** : Slide consigne + screencast rapide de la solution

---

**[INTRO -- face camera]**

C'est l'heure de pratiquer. Tu vas creer un funnel de bienvenue complet par toi-meme. Je te donne le cahier des charges, tu construis. Puis je te montre la solution.

**[ECRAN -- slide "Cahier des charges"]**

Voici ton exercice.

**Objectif** : creer une automation qui accueille les nouveaux inscrits a ta formation gratuite et les oriente vers ta formation premium.

**Contraintes** :

1. Trigger : un contact recoit le tag "inscrit-gratuit" (utilise Tag Applied pour simplifier).

2. Actions immediates : appliquer le tag "en-onboarding" et ajouter a la liste "Formation Gratuite".

3. Email 1 : email de bienvenue. Sujet libre. Contenu : remerciement, lien d'acces, ce qu'ils vont apprendre.

4. Delai : 2 jours.

5. Email 2 : email de valeur. Partage un conseil ou une ressource utile. Pas de vente.

6. Delai : 3 jours.

7. Email 3 : email d'upsell. Presente ta formation premium avec un lien vers la page de vente.

8. Delai : 2 jours.

9. Conditional : le contact a-t-il clique dans l'email d'upsell ?

10. Branche Oui : envoyer un email de confirmation/rappel.

11. Branche Non : envoyer un email avec un angle different (temoignage, benefice cle).

12. Actions finales (les deux branches) : retirer le tag "en-onboarding", appliquer le tag "onboarding-termine", fin du funnel.

**Temps estime** : 15-20 minutes.

**[ECRAN -- slide "Checklist avant de verifier"]**

Avant de regarder la solution, coche cette liste.

- Le nom de l'automation suit la convention de nommage (prefixe + description).
- Le trigger est configure avec "Run For" = "New".
- Les delais sont coherents (pas deux emails le meme jour).
- Les tags de debut ("en-onboarding") et de fin ("onboarding-termine") sont en place.
- Chaque email a un sujet et un pre-header.
- Le conditional cible le bon email (l'email d'upsell, pas un autre).
- L'automation est en mode Draft (ne pas publier avant verification).

**[FACE CAMERA]**

Mets la video en pause et construis ton funnel. Prends ton temps. Reviens quand tu as termine.

[Pause de 3 secondes]

**[ECRAN -- screencast : solution commentee]**

Voici la solution. Je vais parcourir chaque etape rapidement.

[Ouverture d'une automation pre-construite correspondant au cahier des charges]

Le trigger : Tag Applied, tag "inscrit-gratuit", Run For "New". Correct.

Les actions immediates : Apply Tag "en-onboarding", Apply to List "Formation Gratuite". Deux blocs enchaines sans delai.

Email 1 : sujet "Bienvenue -- tes acces sont prets". Pre-header rempli. Contenu avec un lien d'acces bien visible.

Wait 2 jours.

Email 2 : sujet axe conseil ou ressource. Pas de lien de vente dans cet email.

Wait 3 jours.

Email 3 : sujet d'upsell. Lien vers la page de vente.

Wait 2 jours.

Conditional : Email Activity, has clicked, step = email 3.

Branche Oui : email de rappel avec lien direct.

Branche Non : email avec temoignage.

Les deux branches : Remove Tag "en-onboarding", Apply Tag "onboarding-termine", End This Funnel.

[Parcours rapide de chaque bloc]

**[FACE CAMERA]**

Si ton funnel ressemble a ca, bravo. Si tu as oublie un tag ou un delai, corrige-le maintenant. C'est en construisant que tu apprends. Et ce funnel, tu pourras le reutiliser tel quel pour tes propres formations.

**[TRANSITION]**

Dernier arret pour ce module : un quiz pour valider tes acquis.

---

**Points cles** :
- Le funnel complet comporte 13 etapes (trigger + 12 blocs)
- Tags de lifecycle : "en-onboarding" pendant, "onboarding-termine" apres
- Chaque branche du conditional doit avoir ses propres actions finales
- Toujours verifier avec la checklist avant de publier
- Ce funnel est un modele reutilisable pour tout produit freemium

**Mots cles SEO** : exercice automation FluentCRM, creer funnel bienvenue, pratique email marketing WordPress, onboarding email exercice

---

## Quiz M6 -- Automation funnels : fondamentaux

**Type** : Quiz TutorLMS (8 questions)
**Seuil de reussite** : 80%

**Question 1** : Quel element d'une automation FluentCRM permet de creer un embranchement oui/non ?
- A) Le trigger
- B) L'action
- C) Le conditional *(bonne reponse)*
- D) Le goal

**Question 2** : Quel trigger se declenche quand un visiteur soumet un formulaire Fluent Forms ?
- A) Contact Created
- B) Tag Applied
- C) New User Sign Up
- D) Form Submitted *(bonne reponse)*

**Question 3** : Quelle est la difference entre le mode "Draft" et "Published" d'une automation ?
- A) Draft envoie les emails en version test, Published en version finale
- B) Draft est inactive et n'accepte aucun contact, Published est active et declenche le funnel *(bonne reponse)*
- C) Draft est gratuit, Published est payant
- D) Il n'y a pas de difference, ce sont deux noms pour la meme chose

**Question 4** : Quel delai est recommande entre deux emails dans une sequence de bienvenue ?
- A) 6 heures
- B) 1 a 2 jours *(bonne reponse)*
- C) 1 semaine
- D) 30 minutes

**Question 5** : Que fait l'option "Run For: New" sur un trigger ?
- A) L'automation ne se declenche que pour les contacts crees aujourd'hui
- B) L'automation ne se declenche que pour les contacts qui n'ont jamais ete dans cette automation *(bonne reponse)*
- C) L'automation se declenche uniquement une fois puis se desactive
- D) L'automation ne se declenche que pour les nouveaux contacts de moins de 24h

**Question 6** : Quelle action permet de creer un compte utilisateur WordPress depuis une automation FluentCRM ?
- A) Apply Tag
- B) Send Custom Email
- C) Create WordPress User *(bonne reponse)*
- D) Update Contact Property

**Question 7** : Dans un funnel freemium, quel conditional est le plus pertinent apres un email d'upsell ?
- A) Has Tag
- B) In List
- C) Has User Role
- D) Email Activity (has clicked) *(bonne reponse)*

**Question 8** : Combien de niveaux d'imbrication de conditionals sont recommandes au maximum pour garder un funnel lisible ?
- A) 1
- B) 2 *(bonne reponse)*
- C) 4
- D) Il n'y a pas de limite recommandee

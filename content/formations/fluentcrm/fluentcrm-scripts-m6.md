# Scripts vidéo - Module 6 : Automation funnels - fondamentaux

**Formation** : Maîtriser FluentCRM
**Module** : M6 - Automation funnels : fondamentaux (Premium)
**Leçons** : 7 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~55 min de vidéo
**Date** : 2026-03-23

---

## Leçon 6.1 : Comprends le vocabulaire : triggers, actions, goals, conditionals

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra + slides vocabulaire + screencast éditeur automation FluentCRM

---

**[INTRO - face caméra]**

Tu vas construire tes premiers funnels d'automation. Mais avant de toucher à l'éditeur, tu dois maîtriser quatre mots. Quatre concepts qui reviennent partout. Si tu les comprends bien, tout le reste devient logique.

**[ÉCRAN - slide "Les 4 piliers d'une automation"]**

Une automation FluentCRM, c'est un enchaînement de quatre types d'éléments.

Premier élément : le trigger. C'est l'événement déclencheur. Le point de départ. "Un contact soumet un formulaire", "Un tag est appliqué", "Un contact est ajouté à une liste". Sans trigger, pas d'automation. C'est le "quand".

Deuxième élément : l'action. C'est ce que tu fais une fois le trigger déclenché. Envoyer un email. Appliquer un tag. Créer un utilisateur WordPress. Attendre 3 jours. C'est le "quoi".

Troisième élément : le goal. C'est ton objectif. Le point d'arrivée souhaité. Par exemple : "le contact a acheté la formation". Si le goal est atteint, le contact saute directement à cette étape, même s'il n'a pas parcouru toutes les actions intermédiaires. C'est le "où tu veux l'amener".

Quatrième élément : le conditional. C'est un embranchement. Tu poses une question à laquelle la réponse est oui ou non. "Le contact a-t-il le tag premium ?" Oui : chemin A. Non : chemin B. C'est le "si".

**[ÉCRAN - screencast : éditeur automation FluentCRM]**

Voyons ces quatre éléments dans l'éditeur.

[Ouverture d'une automation existante dans FluentCRM]

Le trigger est toujours en haut. C'est le premier bloc. Tu ne peux pas ajouter d'élément avant.

En dessous, tu enchaînes les actions. Chaque action est un bloc que tu ajoutes avec le bouton "+".

Le goal se reconnaît à son icône cible. Il peut être placé n'importe où dans la séquence.

Et le conditional crée deux branches visuelles : une branche "oui" à gauche, une branche "non" à droite.

[Survol de chaque type de bloc dans l'éditeur]

**[ÉCRAN - slide "Analogie : le GPS"]**

Pour retenir : pense à un GPS.

Le trigger, c'est ton point de départ. Tu montes dans la voiture.

Les actions, ce sont les instructions. Tourne à gauche, continue tout droit, prends la sortie.

Les conditionals, ce sont les embranchements. Autoroute ou nationale ?

Et le goal, c'est ta destination. Si tu trouves un raccourci, le GPS te fait sauter les étapes intermédiaires.

**[FACE CAMÉRA]**

Quatre mots. Trigger, action, goal, conditional. Tu les retrouveras dans chaque leçon de ce module. Grave-les.

**[TRANSITION]**

Maintenant que tu as le vocabulaire, on va découvrir l'éditeur visuel où tout ça prend forme.

---

**Points clés** :
- Trigger = événement déclencheur (le "quand")
- Action = ce que l'automation exécute (le "quoi")
- Goal = objectif que le contact doit atteindre (peut court-circuiter des étapes)
- Conditional = embranchement oui/non (le "si")
- Analogie GPS : départ, instructions, embranchements, destination

**Mots clés SEO** : automation FluentCRM, trigger action goal, vocabulaire automation email, funnel email WordPress

---

## Leçon 6.2 : Découvre l'éditeur d'automation visuel

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automations > Éditeur visuel

---

**[INTRO - face caméra]**

L'éditeur d'automation de FluentCRM est visuel. Tu construis ton funnel en glissant des blocs les uns après les autres, comme un organigramme. On va faire le tour complet de l'interface.

**[ÉCRAN - screencast : FluentCRM > Automations]**

Va dans FluentCRM, puis Automations dans le menu latéral.

[Clic sur Automations]

Tu arrives sur la liste de tes automations. Pour l'instant, elle est peut-être vide. Clique sur "Create a New Automation".

[Clic sur Create a New Automation]

FluentCRM te propose des templates pré-faits. Tu en as pour le onboarding, la relance, le tagging automatique. C'est pratique pour démarrer, mais pour bien comprendre, on va partir de zéro.

Sélectionne "Start from Scratch".

[Clic sur Start from Scratch]

**[ÉCRAN - screencast : nommage et organisation]**

Première chose : donne un nom à ton automation. Ce nom est interne, tes contacts ne le verront pas.

Mon conseil : utilise un préfixe par catégorie. Par exemple : "ONBOARD - Bienvenue formation gratuite" ou "VENTE - Upsell premium J+7". Ça te permet de retrouver tes automations quand tu en auras 20 ou 30.

[Saisie du nom de l'automation]

Tu peux aussi ajouter un label. Les labels sont des étiquettes colorées pour organiser visuellement ta liste d'automations. Clique sur le champ "Labels" et crée un nouveau label ou sélectionne un existant.

[Sélection d'un label]

**[ÉCRAN - screencast : choix du trigger]**

Maintenant, tu choisis ton trigger. FluentCRM te propose une liste.

[Affichage de la liste des triggers]

On va prendre un trigger simple : "Tag Applied". Ça signifie : quand un tag est appliqué à un contact, l'automation démarre.

[Sélection de Tag Applied]

Configure le tag. Par exemple : "inscrit-gratuit".

[Configuration du trigger]

Clique sur "Save Settings". Ton trigger est en place.

**[ÉCRAN - screencast : ajout d'actions]**

En dessous du trigger, tu vois un bouton "+". C'est par là que tu ajoutes des actions.

[Clic sur le "+"]

Le panneau latéral s'ouvre avec toutes les actions disponibles. Tu vois les catégories : Actions, Conditionals, Goals.

[Affichage du panneau latéral]

Ajoute une action "Send Custom Email". C'est l'action la plus courante.

[Sélection de Send Custom Email]

Tu arrives sur l'éditeur d'email intégré. Tu rédiges ton email directement dans l'automation, avec les mêmes blocs que pour une campagne. Le sujet, le pré-header, le contenu. Tout est là.

[Vue rapide de l'éditeur d'email]

Sauvegarde et ferme. Ton premier bloc action apparaît dans le funnel.

**[ÉCRAN - screencast : navigation dans l'éditeur]**

Quelques raccourcis pour naviguer.

Tu peux zoomer et dézoomer avec la molette ou les boutons +/- en bas à droite.

Tu peux déplacer la vue en cliquant-glissant sur le fond.

Le bouton "Fit to Screen" recentre tout le funnel dans ton écran.

Et chaque bloc est cliquable. Un clic ouvre ses paramètres dans le panneau latéral.

[Démonstration zoom, déplacement, clic sur un bloc]

**[ÉCRAN - screencast : statut Draft vs Published]**

Dernier point important. Une automation nouvellement créée est en mode "Draft". Elle ne fait rien.

Pour l'activer, tu dois la passer en "Published" avec le bouton en haut à droite.

[Clic sur le toggle Draft/Published]

Tant qu'elle est en Draft, tu peux modifier tout ce que tu veux sans risque. C'est ton bac à sable.

Une fois en Published, chaque nouveau contact qui remplit la condition du trigger entrera dans le funnel.

**[FACE CAMÉRA]**

L'éditeur est intuitif une fois que tu as compris le principe du "+" pour ajouter des blocs. Dans les prochaines leçons, on va détailler chaque catégorie : les triggers, les actions, puis les conditionals.

**[TRANSITION]**

On commence par les triggers. C'est le point de départ de toute automation.

---

**Points clés** :
- Créer une automation : Automations > Create > Start from Scratch
- Nommer avec un préfixe par catégorie (ONBOARD, VENTE, RELANCE...)
- Les labels permettent d'organiser visuellement la liste
- Le trigger est toujours le premier élément
- Draft = inactive, Published = active (les contacts entrent dès que le trigger est rempli)
- Naviguer : molette pour zoomer, clic-glisse pour déplacer, Fit to Screen pour recentrer

**Mots clés SEO** : éditeur automation FluentCRM, créer automation WordPress, funnel visuel FluentCRM, éditeur email automation

---

## Leçon 6.3 : Les triggers CRM : form submitted, tag applied, list added

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automation Editor > Triggers

---

**[INTRO - face caméra]**

Le trigger, c'est la porte d'entrée de ton automation. FluentCRM en propose une vingtaine, répartis en trois catégories. On va les voir une par une pour que tu saches exactement quand utiliser lequel.

**[ÉCRAN - slide "3 catégories de triggers"]**

Première catégorie : les triggers CRM. Ce sont les plus utilisés. Ils se déclenchent sur des actions liées à tes contacts dans FluentCRM.

Deuxième catégorie : les triggers WordPress. Ils se déclenchent sur des événements WordPress : connexion, inscription, changement de rôle.

Troisième catégorie : les triggers d'intégration. Ils se déclenchent quand un événement se produit dans un plugin tiers : WooCommerce, TutorLMS, LearnDash, MemberPress.

**[ÉCRAN - screencast : triggers CRM dans l'éditeur]**

Commençons par les triggers CRM. Ouvre l'éditeur d'automation et clique sur le bloc trigger.

[Affichage de la liste des triggers CRM]

**Tag Applied.** L'automation démarre quand un tag spécifique est appliqué à un contact. C'est le trigger le plus polyvalent. Tu peux l'utiliser pour tout : onboarding, segmentation, relance.

Par exemple : tu appliques le tag "lead-chaud" manuellement ou via un formulaire, et l'automation se déclenche.

[Configuration du trigger Tag Applied avec le tag "lead-chaud"]

**Tag Removed.** L'inverse. L'automation démarre quand un tag est retiré. Utile pour détecter un changement de statut. Par exemple : quand le tag "abonné-actif" est retiré, tu déclenches une séquence de réactivation.

**List Applied.** L'automation démarre quand un contact est ajouté à une liste spécifique. Par exemple : le contact est ajouté à la liste "Formation gratuite" via un formulaire d'inscription.

[Configuration du trigger List Applied]

**List Removed.** L'automation démarre quand un contact est retiré d'une liste. Moins courant, mais utile pour les scénarios de désabonnement.

**Contact Created.** L'automation démarre dès qu'un nouveau contact est créé dans FluentCRM, quelle que soit la source : import, formulaire, API.

**[ÉCRAN - slide "Triggers WordPress"]**

Maintenant, les triggers WordPress. Ceux-là sont disponibles avec FluentCRM Pro.

**New User Sign Up.** L'automation démarre quand un utilisateur WordPress est créé. Pas un contact FluentCRM, un utilisateur WordPress. La différence est importante. Tu peux filtrer par rôle : subscriber, student, customer.

**User Login.** L'automation démarre quand un utilisateur se connecte à WordPress. Utile pour déclencher un message de bienvenue après la première connexion.

**[ÉCRAN - slide "Triggers d'intégration"]**

Enfin, les triggers d'intégration. Ils dépendent des plugins installés.

Avec **TutorLMS** : "Student Enrolled in a Course", "Student Completed a Course", "Student Completed a Lesson".

Avec **WooCommerce** : "New Order (Specific Product)", "Order Status Changed", "Order Completed".

Avec **Fluent Forms** : "Form Submitted". C'est le trigger que tu utiliseras le plus souvent pour capturer des leads.

[Affichage de quelques triggers d'intégration]

**[ÉCRAN - screencast : configuration avancée d'un trigger]**

Un point important sur la configuration. Chaque trigger a une option "Run For" :

"All" : l'automation se déclenche pour tous les contacts, y compris ceux qui sont déjà dans l'automation.

"New" : l'automation ne se déclenche que pour les contacts qui n'ont jamais été dans cette automation.

[Affichage de l'option Run For]

En général, choisis "New" pour éviter qu'un contact boucle indéfiniment dans le même funnel.

**[FACE CAMÉRA]**

Mon conseil : commence par trois triggers. "Form Submitted" pour capturer les leads. "Tag Applied" pour déclencher des séquences manuellement. "List Applied" pour les automations liées à une segmentation. Ces trois-là couvrent 80% des cas.

**[TRANSITION]**

Tu sais comment démarrer une automation. Maintenant, on va voir ce que tu peux faire une fois que le contact est entré : les actions.

---

**Points clés** :
- 3 catégories de triggers : CRM (tag, list, contact), WordPress (user signup, login), Intégration (WooCommerce, TutorLMS, Fluent Forms)
- Tag Applied est le trigger le plus polyvalent
- Form Submitted (Fluent Forms) est le plus courant pour la capture de leads
- Option "Run For" : choisir "New" pour éviter les boucles
- 3 triggers à maîtriser en priorité : Form Submitted, Tag Applied, List Applied

**Mots clés SEO** : triggers FluentCRM, déclencheur automation, tag applied FluentCRM, form submitted automation WordPress

---

## Leçon 6.4 : Les actions : send email, apply tag, wait, create WP user

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automation Editor > Actions

---

**[INTRO - face caméra]**

Le trigger fait entrer le contact dans l'automation. Les actions définissent ce qui lui arrive ensuite. FluentCRM en propose une quinzaine. On va voir les plus importantes et celles que tu utiliseras au quotidien.

**[ÉCRAN - screencast : panneau des actions dans l'éditeur]**

Dans l'éditeur d'automation, clique sur le "+" pour voir les actions disponibles.

[Affichage du panneau latéral avec les actions]

On va les parcourir par ordre de fréquence d'utilisation.

**[ÉCRAN - screencast : Send Custom Email]**

**Send Custom Email.** C'est l'action numéro un. Tu crées un email directement dans l'automation. Tu as le même éditeur que pour les campagnes : sujet, pré-header, contenu avec blocs Gutenberg, smart codes.

[Ouverture de l'éditeur d'email dans l'automation]

La différence avec une campagne : cet email est envoyé automatiquement, au moment où le contact atteint cette étape du funnel.

Tu peux aussi utiliser "Send Sequence Email" si tu veux envoyer un email qui fait partie d'une séquence existante. Mais pour les automations, le Custom Email offre plus de flexibilité.

**[ÉCRAN - screencast : Wait]**

**Wait.** C'est l'action de temporisation. Tu définis un délai avant l'action suivante.

[Configuration d'un délai de 3 jours]

Les options : minutes, heures, jours. Tu peux aussi programmer à un jour et une heure précis. Par exemple : "attendre jusqu'à lundi prochain à 9h".

La question que tout le monde pose : quel délai mettre entre deux emails ? Il n'y a pas de règle absolue. Mais voici un repère : pour une séquence de bienvenue, 1 à 2 jours entre chaque email. Pour une séquence de vente, 2 à 3 jours. Si tu espaces trop, ton contact t'oublie. Si tu enchaînes trop vite, tu passes pour du spam.

**[ÉCRAN - screencast : Apply Tag / Remove Tag]**

**Apply Tag.** Ajoute un tag au contact. C'est là pour la segmentation automatique. Par exemple : après avoir ouvert l'email 3, tu appliques le tag "engagé-séquence-welcome".

[Configuration Apply Tag avec le tag "engagé-séquence-welcome"]

**Remove Tag.** Retire un tag. Utile pour nettoyer les segments. Par exemple : une fois que le contact a terminé la séquence, tu retires le tag "en-onboarding".

**[ÉCRAN - screencast : Apply List / Remove List]**

**Apply to List / Remove from List.** Même principe, mais pour les listes. Tu ajoutes ou retires le contact d'une liste spécifique.

Combine avec les tags, ça te donne un système de segmentation puissant. Le tag pour le comportement ("a-cliqué-upsell"), la liste pour le statut ("Clients premium").

**[ÉCRAN - screencast : Create WordPress User]**

**Create WordPress User.** C'est une action spécifique à FluentCRM Pro.

[Configuration de l'action Create WordPress User]

Elle crée un compte utilisateur WordPress pour le contact. Tu définis le rôle : subscriber, student, customer. FluentCRM génère automatiquement un mot de passe et peut envoyer un email de notification.

Cas d'usage concret dans le contexte schoolsWP : un visiteur s'inscrit à ta formation gratuite via Fluent Forms. FluentCRM crée automatiquement son compte WordPress avec le rôle "Student". Le contact reçoit un email avec ses identifiants. Il peut se connecter et accéder à la formation sur TutorLMS. Zéro intervention manuelle.

[Affichage de la configuration complète]

**[ÉCRAN - screencast : autres actions utiles]**

Quelques actions supplémentaires à connaître.

**End This Funnel.** Force la sortie du contact. Utile après un conditional : si le contact a déjà acheté, tu le sors du funnel de vente.

**Cancel Automations.** Annule d'autres automations en cours pour ce contact. Par exemple : le contact achète, tu annules la séquence de relance.

**Update Contact Property.** Modifie un champ du profil contact. Tu peux changer le statut, le prénom, un champ personnalisé.

**Send Notification to Admin.** Envoie un email de notification à l'administrateur ou à une adresse spécifique. Pratique pour être alerté quand un contact atteint une étape importante.

**[FACE CAMÉRA]**

Les actions que tu utiliseras dans 90% de tes automations : Send Custom Email, Wait, Apply Tag, et Remove Tag. Si tu fais du e-learning, ajoute Create WordPress User. C'est ton kit de base.

**[TRANSITION]**

Tu as les triggers et les actions. Il manque une pièce : comment créer des chemins différents selon le comportement du contact. C'est le rôle des conditionals.

---

**Points clés** :
- Send Custom Email : action la plus utilisée, email directement dans l'automation
- Wait : délai entre les actions (1-2 jours pour bienvenue, 2-3 jours pour vente)
- Apply Tag / Remove Tag : segmentation automatique par comportement
- Create WordPress User : crée un compte WP depuis l'automation (Pro)
- End This Funnel et Cancel Automations pour gérer les sorties et les conflits entre automations
- Kit de base : Send Email + Wait + Apply Tag + Remove Tag

**Mots clés SEO** : actions automation FluentCRM, send email automation, wait délai FluentCRM, créer utilisateur WordPress FluentCRM

---

## Leçon 6.5 : Les conditionnels : crée des chemins oui/non

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automation Editor > Conditionals

---

**[INTRO - face caméra]**

Jusqu'ici, tes automations suivent un chemin linéaire. Le contact entre, il reçoit les actions les unes après les autres. Mais dans la vraie vie, tous tes contacts ne se comportent pas pareil. Les conditionals te permettent de créer des embranchements : un chemin pour ceux qui font X, un autre pour ceux qui ne le font pas.

**[ÉCRAN - screencast : ajout d'un conditional dans l'éditeur]**

Dans l'éditeur d'automation, clique sur "+" et sélectionne "If/Else (Has Tag)".

[Sélection du bloc If/Else dans le panneau]

Tu vois deux branches apparaître. À gauche, la branche "Yes". À droite, la branche "No".

[Affichage visuel des deux branches]

C'est aussi simple que ça. Tu poses une condition, et le contact suit le chemin correspondant.

**[ÉCRAN - screencast : types de conditionals]**

FluentCRM propose plusieurs types de conditions.

**Has Tag.** Le contact a-t-il un tag spécifique ? C'est la condition la plus courante. Exemple : "Le contact a-t-il le tag client-premium ?"

[Configuration Has Tag avec "client-premium"]

**In List.** Le contact est-il dans une liste spécifique ? Exemple : "Le contact est-il dans la liste Formation Payante ?"

**Has User Role.** Le contact a-t-il un rôle WordPress spécifique ? Exemple : "Le contact est-il un Student ?"

**Email Activity.** Le contact a-t-il ouvert ou cliqué dans un email précédent de cette même automation ? C'est extrêmement puissant. Tu peux adapter la suite du funnel en fonction de l'engagement.

[Configuration Email Activity : "Has opened email step 2"]

**[ÉCRAN - slide "Exemple concret : conditional après un email"]**

Voici un cas réel. Tu envoies un email avec un lien vers ton offre premium.

Tu ajoutes un "Wait" de 2 jours.

Puis un conditional "Email Activity" : le contact a-t-il cliqué sur le lien ?

Branche Oui : tu envoies un email de confirmation avec les détails de l'offre et un lien direct vers le paiement.

Branche Non : tu envoies un email de relance avec un angle différent. Peut-être un témoignage, ou un rappel des bénéfices.

[Affichage du funnel complet avec les deux branches]

**[ÉCRAN - screencast : imbrication de conditionals]**

Tu peux imbriquer des conditionals. Un conditional dans une branche d'un autre conditional.

[Démonstration d'un conditional imbriqué]

Mais attention : ne surcharge pas. Deux niveaux d'imbrication, c'est le maximum raisonnable. Au-delà, ton funnel devient illisible et difficile à maintenir. Si tu as besoin de plus de branches, découpe en plusieurs automations séparées.

**[ÉCRAN - screencast : convergence des branches]**

Après un conditional, tu peux faire converger les deux branches vers la même suite d'actions. Pour ça, tu ajoutes les mêmes actions à la fin de chaque branche.

Ou tu utilises l'action "End This Funnel" dans une branche si tu veux sortir certains contacts.

[Démonstration de la convergence]

**[FACE CAMÉRA]**

Les conditionals transforment une automation basique en funnel intelligent. Le contact ne reçoit que les messages pertinents pour lui. Commence simple : un seul conditional par automation. Tu complexifieras quand tu maîtriseras les bases.

**[TRANSITION]**

Tu as les triggers, les actions, les conditionals. Tu as tous les ingrédients. Dans la prochaine leçon, on assemble tout ça pour construire ton premier vrai funnel.

---

**Points clés** :
- Conditional = embranchement Oui/Non dans l'automation
- 4 types principaux : Has Tag, In List, Has User Role, Email Activity
- Email Activity permet d'adapter le funnel selon l'engagement (ouverture, clic)
- Maximum 2 niveaux d'imbrication pour garder le funnel lisible
- Commence avec un seul conditional par automation, puis complexifie progressivement

**Mots clés SEO** : conditional FluentCRM, if else automation email, embranchement funnel, segmentation comportementale FluentCRM

---

## Leçon 6.6 : Construis ton premier funnel : inscription → bienvenue → upsell

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automation Editor (construction pas à pas)

---

**[INTRO - face caméra]**

On passe à la pratique. Tu vas construire un funnel complet de A à Z. Le scénario : un visiteur s'inscrit à ta formation gratuite. Il reçoit une séquence de bienvenue. Puis, au bout de quelques jours, une proposition pour passer en premium. C'est le funnel freemium classique de schoolsWP.

**[ÉCRAN - slide "Architecture du funnel"]**

Voici le plan du funnel avant de le construire.

Trigger : formulaire d'inscription soumis.

Étape 1 : appliquer le tag "inscrit-gratuit" + ajouter à la liste "Formation Gratuite".

Étape 2 : envoyer l'email de bienvenue avec les identifiants.

Étape 3 : attendre 2 jours.

Étape 4 : envoyer un email de valeur (conseil, ressource, astuce).

Étape 5 : attendre 3 jours.

Étape 6 : envoyer l'email d'upsell vers la formation premium.

Étape 7 : attendre 2 jours.

Étape 8 : conditional - le contact a-t-il cliqué sur le lien de l'offre ?

Branche Oui : envoyer un email de rappel avec un lien direct.

Branche Non : envoyer un email de relance avec un témoignage.

Fin du funnel.

**[ÉCRAN - screencast : création de l'automation]**

Allons-y. Va dans Automations > Create a New Automation > Start from Scratch.

[Clic Create > Start from Scratch]

Nomme-la : "ONBOARD - Inscription formation gratuite → upsell premium".

[Saisie du nom]

Ajoute le label "Onboarding".

[Sélection du label]

**[ÉCRAN - screencast : trigger]**

Pour le trigger, sélectionne "Form Submitted" (si tu utilises Fluent Forms). Choisis ton formulaire d'inscription à la formation gratuite.

[Configuration du trigger : Form Submitted > Formulaire inscription formation gratuite]

Option "Run For" : sélectionne "New" pour éviter les doublons.

Sauvegarde.

**[ÉCRAN - screencast : étape 1 - tag + liste]**

Clique sur "+". Sélectionne "Apply Tag". Choisis le tag "inscrit-gratuit".

[Configuration Apply Tag]

Clique encore sur "+". Sélectionne "Apply to List". Choisis la liste "Formation Gratuite".

[Configuration Apply to List]

Ces deux actions se déclenchent instantanément, l'une après l'autre. Pas besoin de délai entre elles.

**[ÉCRAN - screencast : étape 2 - email de bienvenue]**

Clique sur "+". Sélectionne "Send Custom Email".

[Ouverture de l'éditeur d'email]

Sujet : "Bienvenue dans la formation - tes accès sont prêts"

Pré-header : "Tout est en place. Connecte-toi et commence maintenant."

Corps de l'email : un message court. Le lien de connexion. Les instructions pour accéder à la formation. Et un rappel de ce qu'ils vont apprendre.

[Rédaction rapide du contenu]

Sauvegarde.

**[ÉCRAN - screencast : étape 3 - délai + email de valeur]**

Clique sur "+". Sélectionne "Wait". Configure : 2 jours.

[Configuration Wait 2 jours]

Clique sur "+". Sélectionne "Send Custom Email".

Sujet : "3 erreurs que font 90% des débutants avec WordPress"

C'est ton email de valeur. Tu ne vends rien. Tu donnes un conseil utile. Tu crées de la confiance.

[Configuration rapide de l'email]

Sauvegarde.

**[ÉCRAN - screencast : étape 4 - délai + email upsell]**

Clique sur "+". Sélectionne "Wait". Configure : 3 jours.

[Configuration Wait 3 jours]

Clique sur "+". Sélectionne "Send Custom Email".

Sujet : "Prêt à passer au niveau suivant ?"

C'est ton email d'upsell. Tu présentes la formation premium. Les bénéfices concrets. Un lien vers la page de vente.

[Configuration rapide de l'email]

Sauvegarde.

**[ÉCRAN - screencast : étape 5 - conditional + branches]**

Clique sur "+". Sélectionne "Wait". Configure : 2 jours.

Clique sur "+". Sélectionne "If/Else (Email Activity)". Configure : "Has clicked in step" - et sélectionne l'email d'upsell.

[Configuration du conditional Email Activity]

Branche Oui : clique sur le "+" sous la branche Yes. Ajoute "Send Custom Email". Sujet : "Une question sur la formation premium ?" - un email de relance douce avec un lien direct vers le paiement.

Branche Non : clique sur le "+" sous la branche No. Ajoute "Send Custom Email". Sujet : "Ce qu'en dit Thomas, formateur WordPress depuis 5 ans" - un email avec un témoignage ou un cas concret.

[Construction des deux branches]

**[ÉCRAN - screencast : finalisation]**

À la fin de chaque branche, ajoute "End This Funnel" si tu ne veux pas continuer après.

Et ajoute "Apply Tag" avec "onboarding-terminé" dans chaque branche pour marquer que le contact a parcouru le funnel.

[Ajout des actions finales]

**[ÉCRAN - screencast : vérification et publication]**

Avant de publier, vérifie chaque étape en cliquant dessus. Relis les emails. Vérifie les délais. Vérifie les tags.

Quand tout est bon, passe l'automation en "Published".

[Clic sur Published]

**[FACE CAMÉRA]**

Ton premier funnel est en place. Chaque nouveau inscrit va recevoir automatiquement ta séquence de bienvenue et ton upsell. Tu n'as plus rien à faire manuellement.

Ce funnel est un modèle que tu peux dupliquer et adapter. Change les emails, change les délais, change le conditional. La structure reste la même.

**[TRANSITION]**

Ton funnel tourne. Mais comment savoir s'il fonctionne ? Dans la prochaine leçon, on va lire les rapports d'automation.

---

**Points clés** :
- Funnel freemium : inscription gratuit → séquence valeur → offre premium → relance
- Nommage : préfixe + description (ONBOARD - Inscription formation gratuite → upsell premium)
- Délais recommandés : 2 jours (bienvenue → valeur), 3 jours (valeur → upsell), 2 jours (upsell → relance)
- Conditional Email Activity pour adapter la relance selon le comportement
- Toujours ajouter un tag de fin pour marquer le parcours complet
- Vérifier chaque étape avant de publier

**Mots clés SEO** : funnel FluentCRM, automation bienvenue, upsell email WordPress, onboarding automation, séquence email FluentCRM

---

## Leçon 6.7 : Lis les rapports d'automation

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Automations > Report

---

**[INTRO - face caméra]**

Ton funnel tourne depuis quelques jours. Des contacts entrent, reçoivent des emails. Mais est-ce que ça marche ? FluentCRM te donne des rapports détaillés pour chaque automation. On va apprendre à les lire.

**[ÉCRAN - screencast : FluentCRM > Automations > liste]**

Retourne dans Automations. Sur la liste, tu vois déjà des chiffres à côté de chaque automation.

[Affichage de la liste des automations avec les compteurs]

Le nombre de contacts "In Progress" : ceux qui sont actuellement dans le funnel, entre deux étapes.

Le nombre de contacts "Completed" : ceux qui ont atteint la fin du funnel.

Ces deux chiffres te donnent un aperçu rapide sans même ouvrir l'automation.

**[ÉCRAN - screencast : vue interne du funnel]**

Ouvre ton automation. Sur chaque bloc, tu vois le nombre de contacts qui ont passé cette étape.

[Affichage des compteurs sur chaque bloc du funnel]

C'est là que tu détectes les problèmes. Si 100 contacts entrent par le trigger et que seulement 60 passent l'étape "Email de bienvenue", il y a un souci. Peut-être que 40 contacts avaient un email invalide. Peut-être que le délai est trop long et ils se désabonnent avant.

**[ÉCRAN - screencast : stats d'un email dans l'automation]**

Clique sur un bloc "Send Custom Email". Dans les paramètres, tu trouves un onglet "Stats" ou "Report".

[Ouverture des stats d'un email]

Tu retrouves les mêmes métriques que pour une campagne : emails envoyés, taux d'ouverture, taux de clic, désabonnements.

Compare les taux entre les différents emails de ton funnel. Si le premier email a 45% d'ouverture et le troisième seulement 15%, c'est normal : l'engagement diminue au fil de la séquence. Mais si la chute est brutale entre deux emails consécutifs, revois le contenu ou le délai.

**[ÉCRAN - screencast : vue des contacts dans le funnel]**

En haut de l'automation, clique sur "Subscribers" ou "Contacts".

[Affichage de la liste des contacts dans l'automation]

Tu vois chaque contact avec son statut : "Active" (en cours), "Completed" (terminé), "Cancelled" (arrêté).

Tu peux filtrer par statut. Les contacts "Cancelled" méritent une attention particulière. Pourquoi sont-ils sortis ? Désabonnement ? Erreur d'envoi ? Regarde leur fiche individuelle pour comprendre.

[Clic sur un contact pour voir son parcours]

Sur la fiche du contact, tu vois exactement à quelle étape il se trouve et quand il est passé par chaque bloc.

**[ÉCRAN - slide "Les 4 métriques à surveiller"]**

Récapitulons les quatre métriques à surveiller.

Un : le taux d'entrée. Combien de contacts entrent par jour ? Si c'est zéro, vérifie ton trigger et ton formulaire.

Deux : le taux de complétion. Quel pourcentage de contacts atteint la fin ? En dessous de 50%, investigue.

Trois : le taux d'ouverture par email. Compare-les entre eux pour repérer les emails faibles.

Quatre : le taux de conversion au conditional. Quel pourcentage prend la branche "Oui" ? C'est ton indicateur de performance pour l'upsell.

**[FACE CAMÉRA]**

Les rapports ne sont pas là pour décorer. Consulte-les une fois par semaine au minimum. Repère les points de friction. Ajuste les emails, les délais, les conditions. C'est comme ça que tu transformes un funnel correct en funnel performant.

**[TRANSITION]**

Tu maîtrises les fondamentaux des automations. Dans la prochaine leçon, tu passes à la pratique avec un exercice guidé.

---

**Points clés** :
- Liste des automations : voir In Progress et Completed en un coup d'œil
- Chaque bloc affiche le nombre de contacts qui l'ont traversé
- Stats par email : ouverture, clic, désabonnement (comme une campagne)
- Contacts : filtrer par Active / Completed / Cancelled
- 4 métriques à surveiller : taux d'entrée, taux de complétion, ouverture par email, conversion au conditional
- Consulter les rapports une fois par semaine minimum

**Mots clés SEO** : rapports automation FluentCRM, statistiques funnel email, mesurer performance automation, analytics email WordPress

---

## Leçon 6.8 : Exercice : crée un funnel de bienvenue pour ta formation gratuite

**Durée** : 6 min
**Type** : Exercice guidé
**Écran** : Slide consigne + screencast rapide de la solution

---

**[INTRO - face caméra]**

C'est l'heure de pratiquer. Tu vas créer un funnel de bienvenue complet par toi-même. Je te donne le cahier des charges, tu construis. Puis je te montre la solution.

**[ÉCRAN - slide "Cahier des charges"]**

Voici ton exercice.

**Objectif** : créer une automation qui accueille les nouveaux inscrits à ta formation gratuite et les oriente vers ta formation premium.

**Contraintes** :

1. Trigger : un contact reçoit le tag "inscrit-gratuit" (utilise Tag Applied pour simplifier).

2. Actions immédiates : appliquer le tag "en-onboarding" et ajouter à la liste "Formation Gratuite".

3. Email 1 : email de bienvenue. Sujet libre. Contenu : remerciement, lien d'accès, ce qu'ils vont apprendre.

4. Délai : 2 jours.

5. Email 2 : email de valeur. Partage un conseil ou une ressource utile. Pas de vente.

6. Délai : 3 jours.

7. Email 3 : email d'upsell. Présente ta formation premium avec un lien vers la page de vente.

8. Délai : 2 jours.

9. Conditional : le contact a-t-il cliqué dans l'email d'upsell ?

10. Branche Oui : envoyer un email de confirmation/rappel.

11. Branche Non : envoyer un email avec un angle différent (témoignage, bénéfice clé).

12. Actions finales (les deux branches) : retirer le tag "en-onboarding", appliquer le tag "onboarding-terminé", fin du funnel.

**Temps estimé** : 15-20 minutes.

**[ÉCRAN - slide "Checklist avant de vérifier"]**

Avant de regarder la solution, coche cette liste.

- Le nom de l'automation suit la convention de nommage (préfixe + description).
- Le trigger est configuré avec "Run For" = "New".
- Les délais sont cohérents (pas deux emails le même jour).
- Les tags de début ("en-onboarding") et de fin ("onboarding-terminé") sont en place.
- Chaque email a un sujet et un pré-header.
- Le conditional cible le bon email (l'email d'upsell, pas un autre).
- L'automation est en mode Draft (ne pas publier avant vérification).

**[FACE CAMÉRA]**

Mets la vidéo en pause et construis ton funnel. Prends ton temps. Reviens quand tu as terminé.

[Pause de 3 secondes]

**[ÉCRAN - screencast : solution commentée]**

Voici la solution. Je vais parcourir chaque étape rapidement.

[Ouverture d'une automation pré-construite correspondant au cahier des charges]

Le trigger : Tag Applied, tag "inscrit-gratuit", Run For "New". Correct.

Les actions immédiates : Apply Tag "en-onboarding", Apply to List "Formation Gratuite". Deux blocs enchaînés sans délai.

Email 1 : sujet "Bienvenue - tes accès sont prêts". Pré-header rempli. Contenu avec un lien d'accès bien visible.

Wait 2 jours.

Email 2 : sujet axé conseil ou ressource. Pas de lien de vente dans cet email.

Wait 3 jours.

Email 3 : sujet d'upsell. Lien vers la page de vente.

Wait 2 jours.

Conditional : Email Activity, has clicked, step = email 3.

Branche Oui : email de rappel avec lien direct.

Branche Non : email avec témoignage.

Les deux branches : Remove Tag "en-onboarding", Apply Tag "onboarding-terminé", End This Funnel.

[Parcours rapide de chaque bloc]

**[FACE CAMÉRA]**

Si ton funnel ressemble à ça, bravo. Si tu as oublié un tag ou un délai, corrige-le maintenant. C'est en construisant que tu apprends. Et ce funnel, tu pourras le réutiliser tel quel pour tes propres formations.

**[TRANSITION]**

Dernier arrêt pour ce module : un quiz pour valider tes acquis.

---

**Points clés** :
- Le funnel complet comporte 13 étapes (trigger + 12 blocs)
- Tags de lifecycle : "en-onboarding" pendant, "onboarding-terminé" après
- Chaque branche du conditional doit avoir ses propres actions finales
- Toujours vérifier avec la checklist avant de publier
- Ce funnel est un modèle réutilisable pour tout produit freemium

**Mots clés SEO** : exercice automation FluentCRM, créer funnel bienvenue, pratique email marketing WordPress, onboarding email exercice

---

## Quiz M6 - Automation funnels : fondamentaux

**Type** : Quiz TutorLMS (8 questions)
**Seuil de réussite** : 80%

**Question 1** : Quel élément d'une automation FluentCRM permet de créer un embranchement oui/non ?
- A) Le trigger
- B) L'action
- C) Le conditional *(bonne réponse)*
- D) Le goal

**Question 2** : Quel trigger se déclenche quand un visiteur soumet un formulaire Fluent Forms ?
- A) Contact Created
- B) Tag Applied
- C) New User Sign Up
- D) Form Submitted *(bonne réponse)*

**Question 3** : Quelle est la différence entre le mode "Draft" et "Published" d'une automation ?
- A) Draft envoie les emails en version test, Published en version finale
- B) Draft est inactive et n'accepte aucun contact, Published est active et déclenche le funnel *(bonne réponse)*
- C) Draft est gratuit, Published est payant
- D) Il n'y a pas de différence, ce sont deux noms pour la même chose

**Question 4** : Quel délai est recommandé entre deux emails dans une séquence de bienvenue ?
- A) 6 heures
- B) 1 à 2 jours *(bonne réponse)*
- C) 1 semaine
- D) 30 minutes

**Question 5** : Que fait l'option "Run For: New" sur un trigger ?
- A) L'automation ne se déclenche que pour les contacts créés aujourd'hui
- B) L'automation ne se déclenche que pour les contacts qui n'ont jamais été dans cette automation *(bonne réponse)*
- C) L'automation se déclenche uniquement une fois puis se désactive
- D) L'automation ne se déclenche que pour les nouveaux contacts de moins de 24h

**Question 6** : Quelle action permet de créer un compte utilisateur WordPress depuis une automation FluentCRM ?
- A) Apply Tag
- B) Send Custom Email
- C) Create WordPress User *(bonne réponse)*
- D) Update Contact Property

**Question 7** : Dans un funnel freemium, quel conditional est le plus pertinent après un email d'upsell ?
- A) Has Tag
- B) In List
- C) Has User Role
- D) Email Activity (has clicked) *(bonne réponse)*

**Question 8** : Combien de niveaux d'imbrication de conditionals sont recommandés au maximum pour garder un funnel lisible ?
- A) 1
- B) 2 *(bonne réponse)*
- C) 4
- D) Il n'y a pas de limite recommandée

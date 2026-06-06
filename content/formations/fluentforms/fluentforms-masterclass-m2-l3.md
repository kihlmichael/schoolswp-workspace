# Script video - Module 2, Lecon 3 : Notifications conditionnelles

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 - Logique conditionnelle
**Lecon** : 3/7 - Notifications conditionnelles
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration notifications conditionnelles
**Objectif** : Router automatiquement les emails selon les reponses du formulaire

---

**[INTRO - face camera]**

Dans la lecon precedente, on a appris a afficher et masquer des champs. Maintenant, on applique la meme logique aux notifications email.

L'objectif : envoyer automatiquement le bon email a la bonne personne selon ce que le visiteur a repondu. Plus de tri manuel, plus de transferts d'emails. Le routage est automatique.

**[ECRAN - screencast "Le cas pratique"]**

Prenons un cas concret. Tu as un formulaire de contact avec un champ Select "Service" qui propose trois options : Commercial, Support technique, Comptabilite.

Ton equipe a trois adresses :
- commercial@tonsite.fr
- support@tonsite.fr
- compta@tonsite.fr

Quand quelqu'un choisit "Commercial", l'email doit partir a l'equipe commerciale. Quand il choisit "Support technique", l'email va au support. Et ainsi de suite.

On va configurer ca.

**[ECRAN - screencast "Creer la premiere notification conditionnelle"]**

Dans le builder, va dans Form Settings → Notifications & Confirmations → Email Notifications.

Tu as peut-etre deja une notification admin par defaut. On va la garder comme notification generale et en creer de nouvelles pour chaque service.

Clique sur "Add Notification".

Name : "Notification Commercial" - ce nom est interne, le visiteur ne le voit pas.

Send To : commercial@tonsite.fr.

Subject : "Nouvelle demande commerciale - {inputs.name}".

Body : le contenu de l'email avec les merge tags habituels.

Maintenant, la partie cle : en bas de la notification, tu trouves "Conditional Logic". Active le toggle.

Choisis : "Send this notification if" → "Service" → "Equal" → "Commercial".

Sauvegarde. Cette notification ne partira QUE si le visiteur a selectionne "Commercial".

**[ECRAN - screencast "Creer les notifications suivantes"]**

Meme processus pour les deux autres services.

Deuxieme notification : "Notification Support". Send To = support@tonsite.fr. Condition : "Service" Equal "Support technique".

Troisieme notification : "Notification Comptabilite". Send To = compta@tonsite.fr. Condition : "Service" Equal "Comptabilite".

Trois notifications, trois conditions, trois destinataires. Chaque service recoit uniquement les messages qui le concernent.

**[ECRAN - screencast "Notification generale en complement"]**

Tu peux garder une notification admin generale sans condition. Elle part a chaque soumission, quel que soit le service choisi. C'est ton filet de securite - si une notification conditionnelle echoue pour une raison technique, l'admin recoit quand meme le message.

Ca donne quatre notifications au total sur le meme formulaire :
1. Admin generale (pas de condition) → admin@tonsite.fr
2. Commercial (condition : Service = Commercial) → commercial@tonsite.fr
3. Support (condition : Service = Support technique) → support@tonsite.fr
4. Comptabilite (condition : Service = Comptabilite) → compta@tonsite.fr

Plus la notification de confirmation au visiteur, ca fait cinq notifications. Chacune independante, chacune avec sa propre logique.

**[ECRAN - screencast "Notifications avec conditions multiples"]**

Tu peux aller plus loin. Les notifications supportent les memes conditions multiples que les champs : ALL et ANY.

Exemple : envoyer une notification au directeur commercial seulement si le service est "Commercial" ET le budget indique est superieur a 10 000 euros.

Condition 1 : "Service" Equal "Commercial".
Condition 2 : "Budget" Greater Than "10000".
Mode : ALL.

Le directeur ne recoit que les demandes commerciales a fort potentiel. Les petites demandes vont au commercial standard. C'est du routage intelligent.

**[ECRAN - screencast "Personnaliser le contenu selon la condition"]**

Autre possibilite : changer le contenu de l'email selon le service.

Au lieu d'un email generique, tu personnalises le body de chaque notification.

Pour la notification commerciale, tu ajoutes : "Cette demande concerne un projet commercial. Budget indique : {inputs.budget}. Delai souhaite : {inputs.delai}."

Pour la notification support, tu ajoutes : "Probleme signale : {inputs.description_probleme}. Urgence : {inputs.niveau_urgence}."

Chaque equipe recoit un email adapte a son contexte. Le support n'a pas besoin de voir le budget. Le commercial n'a pas besoin de voir le niveau d'urgence.

**[ECRAN - slide "Ce que ca remplace"]**

Pour mettre les choses en perspective : les notifications conditionnelles remplacent un systeme de tickets basique.

Sans FluentForms : le visiteur envoie un email, l'admin le lit, determine le bon service, le transfère manuellement. Si l'admin est absent, le message attend.

Avec FluentForms : le visiteur choisit le service, l'email part directement au bon destinataire. Zero intervention humaine, zero delai.

Pour une petite equipe, ca suffit. Tu n'as pas besoin de Zendesk ou Freshdesk pour router 5 a 20 demandes par jour. FluentForms fait le travail.

**[ECRAN - slide "Erreurs courantes"]**

Deux erreurs a eviter.

Premiere erreur : oublier de couvrir tous les cas. Si ton select a 4 options et tu crees 3 notifications conditionnelles, la 4eme option n'envoie rien. Verifie que chaque valeur possible est couverte.

Deuxieme erreur : ne pas tester chaque branche. Soumets le formulaire une fois pour chaque option du select. Verifie que chaque notification arrive au bon endroit avec le bon contenu.

**[OUTRO - face camera]**

Les notifications conditionnelles, c'est du routage automatique. Le bon email, a la bonne personne, avec le bon contenu. Configuration une fois, execution automatique a chaque soumission.

Prochaine lecon : on applique la logique aux messages de confirmation. Apres la soumission, chaque visiteur voit un message adapte a ce qu'il a repondu. On se retrouve tout de suite.

---

**Points cles** :
- Form Settings → Notifications → Conditional Logic
- Une notification par destinataire avec sa propre condition
- Conditions multiples : ALL/ANY sur les notifications aussi
- Personnaliser le contenu de chaque notification selon le contexte
- Remplace un systeme de tickets basique pour les petites equipes
- Toujours tester chaque branche de condition

**Mots cles SEO** : FluentForms notification conditionnelle, email conditionnel formulaire WordPress, routage email FluentForms, FluentForms conditional notification

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : configuration complete des 3 notifications + test
- Montrer le panneau Conditional Logic de chaque notification
- Ton : pratique, insister sur le test de chaque branche

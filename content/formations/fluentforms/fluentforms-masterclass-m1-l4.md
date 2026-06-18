# Script video - Module 1, Lecon 4 : Notifications email

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 1 - Fondations
**Lecon** : 4/6 - Notifications email
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration notifications
**Objectif** : Configurer des notifications email fiables pour chaque soumission

---

**[INTRO - face camera]**

Un formulaire qui ne notifie personne, c'est un formulaire inutile. Le visiteur remplit tout, clique sur envoyer - et rien ne se passe. Pas de confirmation pour lui, pas d'alerte pour toi. Le lead est la, dans ta base, mais personne ne le sait.

Dans cette lecon, on configure les notifications email. Admin, utilisateur, et conditionnelles.

**[ECRAN - screencast "Notification admin"]**

On commence par la notification admin - celle que toi ou ton equipe recevez.

Dans le builder, va dans l'onglet Form Settings, puis Notifications & Confirmations, puis Email Notifications.

Tu as deja une notification par defaut. Ouvrons-la.

Send To : l'adresse email qui recoit la notification. Par defaut, c'est l'email admin de WordPress. Tu peux en mettre plusieurs, separees par des virgules. Si tu veux que ton commercial recoive aussi le message : ajoute son adresse ici.

Subject : le sujet de l'email. Par defaut "New Form Submission". Change-le en quelque chose d'utile : "Nouveau contact depuis le site - {inputs.name}". Le merge tag {inputs.name} insere automatiquement le nom du visiteur.

Email Body : le contenu de l'email. C'est ici que les merge tags sont essentiels. Tu cliques sur le bouton "Merge Tags" et tu inseres les champs du formulaire.

Un exemple de body efficace :

Nouveau message de {inputs.name}.

Email : {inputs.email}.

Sujet : {inputs.sujet}.

Message : {inputs.message}.

Soumis le {submission.date} depuis {submission.source_url}.

Les merge tags suivent le format {inputs.nom_du_champ}. Pour les donnees systeme, c'est {submission.date}, {submission.source_url}, {submission.browser}.

Reply-To : mets {inputs.email}. Comme ca, quand tu reponds a la notification, ca part directement au visiteur. Pas besoin de copier-coller son adresse.

**[ECRAN - screencast "Notification utilisateur"]**

Deuxieme notification : la confirmation pour le visiteur.

Clique sur "Add Notification" pour en creer une nouvelle.

Send To : ici tu mets {inputs.email}. C'est l'email du visiteur - il recevra la confirmation automatiquement.

Subject : "Merci pour ton message - schoolsWP" ou "Confirmation de ta demande".

Email Body : personnalise le message. Confirme ce qu'il a envoye, indique le delai de reponse, ajoute un lien utile.

Exemple :

Salut {inputs.name},

On a bien recu ton message. Notre equipe te repondra sous 48h.

Pour rappel, voici ce que tu nous as ecrit :

{inputs.message}

A bientot,
L'equipe schoolsWP

Cette confirmation fait deux choses : elle rassure le visiteur (son message est bien parti) et elle met ton email dans sa boite de reception (utile pour la deliverabilite future).

**[ECRAN - screencast "Notifications conditionnelles"]**

Troisieme niveau : les notifications conditionnelles. C'est la que ca devient puissant.

Imaginons un formulaire de contact avec un champ Select "Service" : Commercial, Support, Comptabilite.

Tu crees trois notifications.

Notification 1 : Send To = commercial@tonsite.fr. Conditional Logic activee : si "Service" = "Commercial".

Notification 2 : Send To = support@tonsite.fr. Conditional Logic : si "Service" = "Support".

Notification 3 : Send To = compta@tonsite.fr. Conditional Logic : si "Service" = "Comptabilite".

Chaque departement recoit uniquement les messages qui le concernent. Pas de tri manuel, pas de transferts d'emails. Le routage est automatique.

Pour activer la condition : dans la notification, active "Conditional Logic", choisis le champ "Service", l'operateur "Equal", et la valeur "Commercial" (ou Support, ou Comptabilite).

**[ECRAN - screencast "Plusieurs notifications sur un meme formulaire"]**

Tu peux empiler autant de notifications que tu veux sur un seul formulaire.

Un cas courant : notification admin + confirmation visiteur + notification conditionnelle au departement + notification au manager si le budget est superieur a un seuil.

Chaque notification est independante. Tu peux activer ou desactiver chacune sans toucher aux autres.

Le seul point d'attention : plus tu as de notifications, plus tu generes d'emails. Assure-toi que ton serveur SMTP est fiable. FluentSMTP, du meme editeur, est un bon choix pour ca.

**[ECRAN - slide "Les erreurs a eviter"]**

Quelques erreurs classiques.

Ne pas mettre de notification utilisateur. Le visiteur ne sait pas si son message est parti. Il le renvoie, ou pire, il part et ne revient jamais.

Oublier le Reply-To. Sans Reply-To correctement configure, ta reponse part dans le vide au lieu d'arriver chez le visiteur.

Ne pas tester. Configurer trois notifications et ne jamais envoyer un test. Va dans Form Settings, utilise la preview, soumets le formulaire toi-meme, et verifie chaque email.

Mettre trop d'informations dans le sujet. Le sujet doit etre lisible dans une boite de reception mobile. "Nouveau contact - {inputs.name}" suffit. Pas besoin de coller toute la soumission dans le subject.

**[OUTRO - face camera]**

Les notifications sont le systeme nerveux de ton formulaire. Sans elles, les soumissions restent invisibles. Avec elles, chaque lead est traite, chaque visiteur est confirme, chaque departement est notifie.

Dans la prochaine lecon, on protege le formulaire contre le spam. Parce que recevoir 200 notifications de bots, ca annule tout le travail qu'on vient de faire. A tout de suite.

---

**Points cles** :
- Notification admin : adresse, sujet, body avec merge tags, Reply-To = {inputs.email}
- Notification utilisateur : confirmation automatique a {inputs.email}
- Notifications conditionnelles : routage automatique selon les reponses
- Plusieurs notifications independantes par formulaire
- Toujours tester les notifications avant de publier

**Mots cles SEO** : FluentForms notifications email, FluentForms merge tags, FluentForms email conditionnel, notification formulaire WordPress

---

**Notes de production** :
- Face camera : intro (20 sec) + outro (15 sec)
- Screencast : montrer chaque ecran de configuration step-by-step
- Zoomer sur les merge tags et le champ Reply-To
- Ton : methodique, insister sur l'importance du test

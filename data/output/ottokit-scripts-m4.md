# Scripts video — Module 4 : Actions : ce que tes automations executent

**Formation** : Maitriser OttoKit
**Module** : M4 — Actions : ce que tes automations executent
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~40 min de video
**Date** : 2026-03-30

---

## Lecon 4.1 — Anatomie d'une action : app, evenement, connexion, configuration

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Dans le Module 3, tu as appris ce qui declenche un workflow. Maintenant, on passe a ce qui se passe apres : les actions. Une action, c'est la tache concrete que ton workflow execute dans une app.

**[ECRAN — slide "Qu'est-ce qu'une action ?"]**

Chaque action dans OttoKit est composee de 4 elements :

1. **L'app** — dans quelle application tu veux agir (WordPress, Google Sheets, Gmail, Slack...)
2. **L'evenement** — quelle tache tu veux executer (creer un article, ajouter une ligne, envoyer un email...)
3. **La connexion** — quel compte utiliser (ta connexion WordPress, ton compte Google...)
4. **La configuration** — les details : quel titre pour l'article, quel destinataire pour l'email, quelles donnees dans chaque champ

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow existant avec un trigger et une action deja configures]
[Clique sur le bloc action]
[Pointe chaque element dans le panneau lateral]

Decomposons une action reelle. Ici, on a un workflow qui detecte une nouvelle commande WooCommerce et envoie un email via Gmail.

[Pointe l'app selectionnee : "Gmail"]

L'app, c'est Gmail.

[Pointe l'evenement : "Send Email"]

L'evenement, c'est "Send Email".

[Pointe la connexion : compte Google connecte]

La connexion, c'est ton compte Google.

[Pointe les champs de configuration : destinataire, sujet, corps]

Et la configuration, ce sont les champs : a qui, quel sujet, quel contenu.

**[ECRAN — slide "Action vs Trigger — la difference"]**

| | Trigger | Action |
|---|---|---|
| Role | Demarre le workflow | Execute une tache |
| Position | Toujours en premier | Apres le trigger |
| Quantite | 1 seul par workflow | Autant que tu veux |
| Donnees | Fournit les donnees | Utilise les donnees |

Un workflow a toujours un seul trigger. Mais il peut avoir 1, 2, 5, 10 actions. Chaque action utilise les donnees du trigger ou des actions precedentes.

**[ECRAN — slide "Le processus de configuration"]**

Pour configurer une action, tu suis toujours le meme processus :

1. Choisis l'app
2. Choisis l'evenement
3. Selectionne la connexion
4. Remplis les champs (statiques ou dynamiques)
5. Teste l'action
6. Enregistre

C'est le meme schema que pour les triggers. Si tu maitrises les triggers du Module 3, tu maitrises deja la moitie du travail.

**[TRANSITION — face camera]**

Passons a la pratique. Dans la prochaine lecon, tu configures ta premiere action : creer un article WordPress depuis un workflow OttoKit.

---

**Points cles**
- Une action = app + evenement + connexion + configuration
- Un workflow peut contenir autant d'actions que necessaire
- Les actions utilisent les donnees du trigger ou des actions precedentes
- Le processus de configuration est identique a celui des triggers

**Mots-cles SEO**
- OttoKit action definition
- configurer action OttoKit
- anatomie action automatisation WordPress
- OttoKit workflow action

---

## Lecon 4.2 — Configure une action WordPress (creer un article)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Premiere action concrете. On va configurer un workflow qui cree automatiquement un brouillon d'article WordPress quand un trigger se declenche. C'est une des actions les plus courantes pour les createurs de contenu.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow existant avec un trigger deja configure — par exemple un trigger Google Sheets "New Row Added" avec des colonnes Titre, Contenu, Categorie]
[Clique sur le bouton "+" pour ajouter une action]

On part d'un trigger deja configure. Ici, Google Sheets detecte une nouvelle ligne avec un titre et un contenu d'article. On va ajouter une action pour creer l'article dans WordPress.

**[ECRAN — screencast selection de l'app]**

[Dans le panneau lateral, tape "WordPress" dans la barre de recherche]
[Selectionne "WordPress"]

On selectionne WordPress. OttoKit detecte automatiquement les fonctionnalites disponibles grace au plugin installe sur ton site.

**[ECRAN — screencast selection de l'evenement]**

[Scrolle dans la liste des evenements]
[Montre quelques evenements disponibles : "Create Post", "Create User", "Update Post"...]
[Selectionne "Create Post"]

La liste des evenements WordPress est longue. Creer un article, creer un utilisateur, mettre a jour un article... Ici, on choisit "Create Post".

**[ECRAN — screencast selection de la connexion]**

[Selectionne la connexion WordPress dans le dropdown]

On selectionne la connexion WordPress. C'est celle du Module 2 — ton site schoolsWP.

**[ECRAN — screencast configuration des champs]**

[Montre les champs de configuration : Post Title, Post Content, Post Status, Post Type, Categories, Tags]

Voici les champs a remplir. Et c'est ici que ca devient interessant : tu peux utiliser des donnees dynamiques.

[Clique dans le champ "Post Title"]
[Montre le selecteur de donnees dynamiques — icone ou bouton a cote du champ]
[Selectionne le champ "Titre" venant du trigger Google Sheets]

Pour le titre, on ne tape pas un texte fixe. On clique sur le selecteur de donnees et on choisit le champ "Titre" du trigger. Quand une nouvelle ligne arrive dans le Sheet, le titre de cette ligne devient le titre de l'article.

[Fait la meme chose pour "Post Content" — selectionne "Contenu" du trigger]

Pareil pour le contenu. On mappe la colonne "Contenu" du Sheet vers le corps de l'article.

[Pour "Post Status", selectionne "Draft" dans le dropdown]

Le statut : "Draft". Toujours commencer par un brouillon. Tu pourras relire avant de publier.

[Pour "Post Type", montre "Post" selectionne par defaut]
[Pour "Categories", tape ou selectionne une categorie existante]

**[ECRAN — screencast test de l'action]**

[Clique sur le bouton "Test Action" ou "Test Step"]
[Montre le resultat : "Success" avec l'ID du post cree]

On teste. OttoKit cree un brouillon reel sur ton site. Tu vois le resultat : "Success", avec l'ID du post cree.

[Ouvre un nouvel onglet — va dans wp-admin → Articles → Brouillons]
[Montre l'article cree avec le titre et le contenu du Sheet]

Si tu vas dans ton WordPress, le brouillon est bien la. Titre et contenu correspondent aux donnees du Sheet.

[Reviens dans OttoKit — clique sur "Save"]

**[TRANSITION — face camera]**

Tu viens de creer ta premiere action WordPress. Le processus est toujours le meme : app, evenement, connexion, champs, test. Dans la prochaine lecon, on fait la meme chose avec Google Sheets.

---

**Points cles**
- "Create Post" cree un article WordPress avec titre, contenu, statut et categorie
- Utilise les donnees dynamiques du trigger pour remplir les champs
- Toujours creer un brouillon ("Draft") par defaut — relire avant de publier
- Le test cree un article reel : verifie dans wp-admin

**Mots-cles SEO**
- OttoKit creer article WordPress
- automatiser publication WordPress
- action WordPress OttoKit
- creer post automatiquement OttoKit

---

## Lecon 4.3 — Configure une action SaaS (ajouter une ligne Google Sheets)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Deuxieme type d'action : une action SaaS. On va ajouter automatiquement une ligne dans Google Sheets chaque fois qu'un evenement se produit sur ton site WordPress. C'est l'action la plus utilisee pour le suivi et le reporting.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce "Order Created" deja configure et avec des donnees Fetch Data]
[Clique sur "+" pour ajouter une action]

On part d'un trigger WooCommerce : chaque nouvelle commande declenche le workflow. On va enregistrer les details de la commande dans un Google Sheet.

**[ECRAN — screencast selection de l'app et de l'evenement]**

[Tape "Google Sheets" dans la barre de recherche]
[Selectionne "Google Sheets"]
[Selectionne l'evenement "Add Row" ou "Insert Row"]

App : Google Sheets. Evenement : "Add Row". On veut ajouter une ligne, pas modifier une ligne existante.

**[ECRAN — screencast selection de la connexion]**

[Selectionne la connexion Google dans le dropdown]

On selectionne la connexion Google. Si tu ne l'as pas encore, clique sur "Add Connection" et autorise l'acces OAuth.

**[ECRAN — screencast selection du spreadsheet et de la feuille]**

[Dans le champ "Spreadsheet", clique et selectionne un tableur existant — par exemple "Suivi commandes schoolsWP"]
[Dans le champ "Sheet", selectionne la feuille — par exemple "Sheet1" ou "Commandes"]

Tu choisis d'abord le spreadsheet, puis la feuille. OttoKit liste tous les tableurs de ton Google Drive.

**[ECRAN — screencast mapping des champs]**

[OttoKit affiche les colonnes du Sheet : colonne A (Date), colonne B (Client), colonne C (Email), colonne D (Montant), colonne E (Produit)]
[Pour la colonne "Date", selectionne la donnee dynamique "order_date" du trigger WooCommerce]
[Pour "Client", selectionne "billing_first_name" + texte statique " " + "billing_last_name"]
[Pour "Email", selectionne "billing_email"]
[Pour "Montant", selectionne "total"]
[Pour "Produit", selectionne "line_items" ou le premier element]

C'est le mapping. Pour chaque colonne du Sheet, tu selectionnes la donnee correspondante du trigger. Date de commande, nom du client, email, montant, produit.

Remarque le champ "Client" : on combine prenom + espace + nom. C'est un melange de donnees dynamiques et de texte statique. On verra ca en detail dans le Module 5.

**[ECRAN — screencast test de l'action]**

[Clique sur "Test Action"]
[Montre le resultat : "Success"]
[Ouvre Google Sheets dans un nouvel onglet]
[Montre la nouvelle ligne ajoutee avec les donnees de la commande]

Le test fonctionne. Si tu ouvres ton Google Sheet, la ligne est ajoutee avec toutes les donnees. Chaque nouvelle commande WooCommerce ajoutera une ligne automatiquement.

[Reviens dans OttoKit — clique sur "Save"]

**[TRANSITION — face camera]**

Tu sais maintenant mapper des donnees WordPress vers Google Sheets. Prochaine etape : envoyer un email automatique avec Gmail.

---

**Points cles**
- "Add Row" ajoute une ligne dans Google Sheets avec les donnees du trigger
- Le mapping associe chaque colonne du Sheet a un champ du trigger
- On peut combiner donnees dynamiques et texte statique dans un meme champ
- Toujours verifier dans Google Sheets que la ligne est correctement ajoutee apres le test

**Mots-cles SEO**
- OttoKit Google Sheets action
- ajouter ligne Google Sheets automatiquement
- mapper donnees OttoKit vers Sheets
- automatiser suivi commandes Google Sheets

---

## Lecon 4.4 — Configure une action email (envoyer un Gmail)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Troisieme type d'action : l'email. Tu vas configurer un envoi automatique de Gmail avec un destinataire, un sujet et un contenu qui s'adaptent a chaque situation. C'est l'action la plus utilisee pour communiquer avec tes clients ou tes eleves.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger — par exemple "New User Registration" sur WordPress]
[Clique sur "+" pour ajouter une action]

On part d'un trigger WordPress : un nouvel utilisateur s'inscrit sur ton site. On va lui envoyer un email de bienvenue personnalise.

**[ECRAN — screencast selection app et evenement]**

[Tape "Gmail" dans la barre de recherche]
[Selectionne "Gmail"]
[Selectionne l'evenement "Send Email"]

App : Gmail. Evenement : "Send Email".

**[ECRAN — screencast selection de la connexion]**

[Selectionne la connexion Google/Gmail dans le dropdown]

Tu utilises la meme connexion Google que pour Sheets. Un seul compte Google donne acces a Gmail, Sheets, Drive, Calendar...

**[ECRAN — screencast configuration du destinataire]**

[Dans le champ "To", clique sur le selecteur de donnees dynamiques]
[Selectionne "user_email" depuis les donnees du trigger WordPress]

Le destinataire n'est pas une adresse fixe. On utilise le champ dynamique "user_email" du trigger. Chaque inscrit recevra l'email a sa propre adresse.

**[ECRAN — screencast configuration du sujet]**

[Dans le champ "Subject", tape le texte : "Bienvenue "]
[Clique sur le selecteur dynamique et selectionne "display_name" ou "first_name"]
[Le champ affiche maintenant : "Bienvenue {display_name}"]

Pour le sujet, on combine texte statique et donnee dynamique. "Bienvenue" + le prenom de l'inscrit. Chaque email aura un sujet personnalise.

**[ECRAN — screencast configuration du corps]**

[Dans le champ "Body" ou "Message", tape :]

```
Bonjour {first_name},

Merci de rejoindre schoolsWP. Ton compte est maintenant actif.

Voici tes prochaines etapes :
1. Connecte-toi a ton espace eleve
2. Decouvre le catalogue de formations
3. Commence ta premiere lecon

A bientot,
L'equipe schoolsWP
```

[Montre comment inserer les tokens dynamiques dans le corps du texte]
[Remplace {first_name} par le token reel en cliquant sur le selecteur]

Le corps de l'email melange du texte fixe et des donnees dynamiques. Ici, le prenom s'insere automatiquement. Chaque nouvel inscrit recoit un email personnalise.

**[ECRAN — screencast champs optionnels]**

[Montre les champs CC, BCC, Reply-To si disponibles]
[Montre le champ "From Name" si disponible — taper "schoolsWP"]

Quelques champs optionnels utiles : CC pour mettre quelqu'un en copie, BCC pour une copie invisible, et "From Name" pour que l'email affiche "schoolsWP" au lieu de ton adresse brute.

**[ECRAN — screencast test de l'action]**

[Clique sur "Test Action"]
[Montre le resultat : "Success — Email sent"]

On teste. L'email part immediatement. Verifie ta boite de reception — ou celle de l'adresse de test.

[Ouvre Gmail dans un nouvel onglet — montre l'email recu avec le prenom insere dans le sujet et le corps]

L'email est arrive. Le prenom est bien insere. Le formatage est correct.

[Reviens dans OttoKit — clique sur "Save"]

**[TRANSITION — face camera]**

Tu sais maintenant configurer trois types d'actions : WordPress, Google Sheets et Gmail. Mais un workflow ne se limite pas a une seule action. Dans la prochaine lecon, on enchaine plusieurs actions dans un meme workflow.

---

**Points cles**
- Le destinataire, le sujet et le corps de l'email acceptent des donnees dynamiques
- Combiner texte statique et tokens pour personnaliser chaque email
- Utiliser un email de test pendant le developpement, pas ton email personnel
- Les champs CC, BCC et From Name sont optionnels mais utiles

**Mots-cles SEO**
- OttoKit envoyer email Gmail
- automatiser email WordPress OttoKit
- email personnalise automatique WordPress
- action Gmail OttoKit configuration

---

## Lecon 4.5 — Multi-actions : enchaine plusieurs actions dans un workflow

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Jusqu'ici, chaque workflow avait une seule action. En realite, tu peux en enchainer autant que tu veux. Un trigger, puis action 1, action 2, action 3... C'est la que les workflows deviennent vraiment utiles.

**[ECRAN — slide "Scenario schoolsWP"]**

On va construire un workflow complet :

**Trigger** : un eleve s'inscrit sur schoolsWP (WordPress User Registration)

**Action 1** : creer un contact dans FluentCRM avec son nom et son email

**Action 2** : envoyer un email de bienvenue personnalise via Gmail

**Action 3** : ajouter une ligne dans Google Sheets pour le suivi des inscriptions

Trois actions, un seul trigger. Tout se fait automatiquement.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow avec le trigger WordPress "User Registration" deja configure]

Le trigger est pret. On va ajouter les trois actions une par une.

**[ECRAN — screencast ajout de l'action 1 — FluentCRM]**

[Clique sur "+" apres le trigger]
[Selectionne "FluentCRM" comme app]
[Selectionne "Create/Update Contact" comme evenement]
[Selectionne la connexion WordPress]
[Mappe les champs : Email → user_email, First Name → first_name, Last Name → last_name]
[Selectionne un tag ou une liste : "Nouveaux inscrits"]
[Clique sur "Save"]

Action 1 : creer un contact FluentCRM. On mappe l'email, le prenom, le nom. On ajoute le tag "Nouveaux inscrits" pour segmenter tes contacts.

**[ECRAN — screencast ajout de l'action 2 — Gmail]**

[Clique sur "+" apres l'action 1]
[Selectionne "Gmail" → "Send Email"]
[Selectionne la connexion Google]
[To : user_email du trigger]
[Subject : "Bienvenue sur schoolsWP, {first_name}"]
[Body : message de bienvenue personnalise]
[Clique sur "Save"]

Action 2 : envoyer l'email de bienvenue. On reprend le meme schema que la lecon precedente.

**[ECRAN — screencast ajout de l'action 3 — Google Sheets]**

[Clique sur "+" apres l'action 2]
[Selectionne "Google Sheets" → "Add Row"]
[Selectionne la connexion Google]
[Selectionne le spreadsheet "Inscriptions schoolsWP"]
[Mappe les colonnes : Date → date_registered, Nom → display_name, Email → user_email]
[Clique sur "Save"]

Action 3 : enregistrer dans Sheets. Date, nom, email. Chaque inscription sera tracee.

**[ECRAN — screencast vue d'ensemble du workflow]**

[Dezoom sur le canvas pour voir le workflow complet]
[Pointe la sequence : Trigger → Action 1 → Action 2 → Action 3]

Voici le workflow complet. Un trigger, trois actions. Elles s'executent dans l'ordre, de haut en bas.

**[ECRAN — slide "Ordre d'execution — ce qu'il faut savoir"]**

Trois regles a retenir :

1. **Sequentiel** : les actions s'executent dans l'ordre. Action 1 se termine avant qu'action 2 ne commence.

2. **Dependances** : action 2 peut utiliser les donnees du trigger ET de l'action 1. Action 3 peut utiliser les donnees du trigger, de l'action 1 ET de l'action 2.

3. **Echec** : si une action echoue, les suivantes ne s'executent pas. Si FluentCRM plante, l'email ne part pas et la ligne Sheets n'est pas ajoutee.

**[TRANSITION — face camera]**

Tu as maintenant un workflow multi-actions fonctionnel. Mais avant de le publier, il faut tester chaque action. C'est le sujet de la prochaine lecon.

---

**Points cles**
- Un workflow peut contenir autant d'actions que necessaire
- Les actions s'executent dans l'ordre, de haut en bas
- Chaque action peut utiliser les donnees du trigger et des actions precedentes
- Si une action echoue, les suivantes ne s'executent pas par defaut

**Mots-cles SEO**
- OttoKit multi actions workflow
- enchainer actions OttoKit
- workflow plusieurs etapes OttoKit
- automatiser inscription WordPress FluentCRM

---

## Lecon 4.6 — Test d'action : valide AVANT de publier

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu ne publies jamais un workflow sans l'avoir teste. C'est la regle d'or. Un workflow mal teste, c'est un email qui part a la mauvaise personne, une ligne qui s'ecrit au mauvais endroit, ou un article publie avec un titre vide.

**[ECRAN — slide "Pourquoi tester ?"]**

Tester, c'est verifier trois choses :

1. **La connexion fonctionne** — l'app est bien accessible
2. **Les donnees sont correctes** — les bons champs arrivent aux bons endroits
3. **Le resultat est celui attendu** — l'article, l'email, la ligne sont conformes

**[ECRAN — screencast OttoKit canvas]**

[Ouvre le workflow multi-actions de la lecon 4.5]
[Clique sur l'action 1 — FluentCRM]

On reprend notre workflow a trois actions. On va tester chaque action individuellement.

**[ECRAN — screencast test de l'action 1]**

[Montre le bouton "Test Action" ou "Test Step" en bas du panneau]
[Clique dessus]
[Montre le resultat : "Success" avec les details du contact cree]

Action 1 : FluentCRM. Clique sur "Test Action". OttoKit execute l'action avec les donnees du Fetch Data du trigger. Resultat : "Success". Le contact est cree.

[Montre les details retournes : contact_id, email, status]

OttoKit affiche les details du resultat. L'ID du contact, l'email, le statut. Ces donnees deviennent disponibles pour les actions suivantes.

**[ECRAN — screencast test de l'action 2]**

[Clique sur l'action 2 — Gmail]
[Clique sur "Test Action"]
[Montre le resultat : "Success — Email sent"]

Action 2 : Gmail. Meme processus. "Test Action", resultat "Success". L'email est envoye.

**[ECRAN — screencast test de l'action 3]**

[Clique sur l'action 3 — Google Sheets]
[Clique sur "Test Action"]
[Montre le resultat : "Success — Row added"]

Action 3 : Google Sheets. Teste, reussi, ligne ajoutee.

**[ECRAN — slide "Que faire si un test echoue ?"]**

Si un test echoue, voici la demarche :

1. **Lis le message d'erreur** — OttoKit affiche la raison exacte
2. **Verifie la connexion** — clique sur "Reconnect" si necessaire
3. **Verifie les champs** — un champ obligatoire manquant ? un format incorrect ?
4. **Verifie les donnees source** — le Fetch Data du trigger a-t-il retourne des donnees ?
5. **Re-teste** — corrige et relance le test

Les erreurs les plus courantes :

- **"Connection expired"** — re-autorise l'app dans les connexions
- **"Required field missing"** — un champ obligatoire est vide
- **"Permission denied"** — l'app n'a pas les droits suffisants
- **"Invalid value"** — le format de la donnee ne correspond pas (ex: texte dans un champ nombre)

**[ECRAN — screencast publication du workflow]**

[Apres avoir teste les 3 actions avec succes]
[Clique sur le toggle "Active" ou "Publish" en haut du workflow]
[Le workflow passe de "Draft" a "Active"]

Toutes les actions sont testees avec succes. Maintenant, et seulement maintenant, tu peux publier. Active le workflow. Il est en production.

**[TRANSITION — face camera]**

Tester individuellement, c'est la methode fiable. Mais que se passe-t-il quand un workflow est publie et qu'une action echoue en conditions reelles ? C'est le sujet de la prochaine lecon.

---

**Points cles**
- Tester chaque action individuellement avant de publier le workflow
- Le test utilise les donnees du Fetch Data du trigger
- Lire le message d'erreur : OttoKit explique la raison de l'echec
- Ne jamais publier un workflow sans avoir teste toutes les actions

**Mots-cles SEO**
- OttoKit tester action
- test workflow OttoKit avant publication
- debugger action OttoKit
- OttoKit test step

---

## Lecon 4.7 — Gerer les erreurs : que se passe-t-il si une action echoue ?

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + historique

---

**[INTRO — face camera]**

Ton workflow est publie, il tourne depuis des jours, tout va bien. Et puis un matin, une action echoue. L'API Google est temporairement indisponible, ou un champ arrive vide alors qu'il ne devrait pas. Que se passe-t-il exactement ?

**[ECRAN — slide "Quand une action echoue"]**

Quand une action echoue en production, OttoKit applique un comportement precis :

1. **L'action echoue** — OttoKit detecte l'erreur
2. **Auto-replay** — OttoKit retente automatiquement l'action. 6 tentatives espacees dans le temps.
3. **Si ca fonctionne a la tentative 3** — le workflow reprend normalement a l'action suivante
4. **Si ca echoue 6 fois** — OttoKit abandonne et marque l'execution comme echouee

**[ECRAN — slide "Impact sur les actions suivantes"]**

Regle par defaut : si une action echoue definitivement (apres 6 tentatives), les actions suivantes ne s'executent pas.

Dans notre workflow a 3 actions :
- Si l'action 1 (FluentCRM) echoue → l'action 2 (Gmail) et l'action 3 (Sheets) ne se lancent pas
- Si l'action 2 (Gmail) echoue → l'action 1 est deja terminee avec succes, mais l'action 3 ne se lance pas

C'est un comportement de securite. Mieux vaut ne pas envoyer un email que d'envoyer un email avec des donnees corrompues.

**[ECRAN — screencast OttoKit — historique des executions]**

[Clique sur "History" dans la barre laterale]
[Montre la liste des executions avec des statuts : Success, Failed, In Progress]

L'historique te montre chaque execution. En vert : succes. En rouge : echec. Clique sur une execution echouee pour voir les details.

[Clique sur une execution echouee]
[Montre le detail etape par etape : trigger OK, action 1 OK, action 2 Failed]
[Montre le message d'erreur de l'action 2]

Tu vois exactement ou ca a plante et pourquoi. Ici, l'action 2 a echoue — le message d'erreur t'explique la raison.

**[ECRAN — screencast OttoKit — simuler une erreur]**

[Ouvre un workflow de test]
[Dans une action Google Sheets, modifie le spreadsheet ID pour pointer vers un document supprime ou inaccessible]
[Active le workflow et declenche-le manuellement]
[Montre l'erreur dans l'historique : "Spreadsheet not found" ou equivalent]

Pour comprendre le mecanisme, on simule une erreur. On pointe l'action Sheets vers un document inexistant. Le trigger se declenche, l'action echoue, et on voit le comportement dans l'historique.

[Montre le compteur de tentatives : 1/6, puis 2/6...]

OttoKit retente automatiquement. Tu n'as rien a faire. Si le probleme est temporaire (API indisponible pendant 5 minutes), l'auto-replay corrige la situation tout seul.

**[ECRAN — slide "Bonnes pratiques de gestion d'erreur"]**

1. **Consulte l'historique regulierement** — meme si tout semble fonctionner
2. **Configure les notifications** — OttoKit peut t'envoyer un email quand un workflow echoue (dans Settings)
3. **Utilise des donnees de test robustes** — evite les champs optionnels non geres
4. **Prevois les cas limites** — un email vide, un montant a zero, un nom avec des caracteres speciaux
5. **Dans le Module 5**, tu apprendras a definir des valeurs par defaut pour eviter les champs vides

**[ECRAN — slide "Recapitulatif auto-replay"]**

| Situation | Comportement |
|---|---|
| Erreur temporaire (API down 2 min) | Auto-replay reussit → workflow continue |
| Erreur permanente (mauvais ID spreadsheet) | 6 tentatives echouent → workflow stoppe |
| Action 2 echoue | Actions 3, 4, 5... ne s'executent pas |
| Action 1 reussit puis action 2 echoue | Action 1 n'est pas annulee (pas de rollback) |

Point important : il n'y a pas de rollback. Si l'action 1 a cree un contact FluentCRM et que l'action 2 echoue, le contact reste dans FluentCRM. OttoKit n'annule pas ce qui a deja ete fait.

**[TRANSITION — face camera]**

Tu sais maintenant comment OttoKit gere les erreurs. Le Module 4 est termine. Passe au quiz pour valider tes acquis avant d'attaquer le Module 5 sur le data mapping et les formatters.

---

**Points cles**
- L'auto-replay retente une action echouee 6 fois automatiquement
- Si une action echoue definitivement, les actions suivantes ne s'executent pas
- Il n'y a pas de rollback : les actions deja reussies ne sont pas annulees
- L'historique montre le detail de chaque execution, etape par etape
- Consulter l'historique regulierement pour detecter les echecs silencieux

**Mots-cles SEO**
- OttoKit gestion erreur workflow
- auto-replay OttoKit
- debugger workflow OttoKit
- OttoKit historique execution

---

## Notes de production — Module 4

### Captures a preparer
- Panneau lateral d'une action avec les 4 elements visibles (app, evenement, connexion, champs)
- Configuration action "Create Post" WordPress — champs titre, contenu, statut
- Selecteur de donnees dynamiques dans un champ d'action
- Configuration action "Add Row" Google Sheets — mapping colonnes
- Configuration action "Send Email" Gmail — destinataire dynamique, sujet, corps
- Canvas avec workflow 3 actions (FluentCRM + Gmail + Sheets)
- Bouton "Test Action" et resultat "Success"
- Resultat d'un test echoue avec message d'erreur
- Historique des executions avec statuts succes/echec
- Detail d'une execution echouee — etape par etape
- Toggle publication du workflow (Draft → Active)

### Environnement de demo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec :
  - WooCommerce installe (au moins 1 commande de test)
  - FluentCRM installe (pour l'action "Create Contact")
  - Au moins 1 utilisateur de test inscrit
- Google Sheet "Suivi commandes schoolsWP" avec colonnes : Date, Client, Email, Montant, Produit
- Google Sheet "Inscriptions schoolsWP" avec colonnes : Date, Nom, Email
- Compte Gmail connecte a OttoKit
- Adresse email de test (ne pas utiliser son email personnel pour les demos)

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 4.1 | 5 min |
| 4.2 | 6 min |
| 4.3 | 6 min |
| 4.4 | 6 min |
| 4.5 | 6 min |
| 4.6 | 5 min |
| 4.7 | 6 min |
| **Total M4** | **40 min** |

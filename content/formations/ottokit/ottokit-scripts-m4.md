# Scripts vidéo - Module 4 : Actions : ce que tes automations exécutent

**Formation** : Maîtriser OttoKit
**Module** : M4 - Actions : ce que tes automations exécutent
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~40 min de vidéo
**Date** : 2026-03-30

---

## Leçon 4.1 - Anatomie d'une action : app, événement, connexion, configuration

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Dans le Module 3, tu as appris ce qui déclenche un workflow. Maintenant, on passe à ce qui se passe après : les actions. Une action, c'est la tâche concrète que ton workflow exécute dans une app.

**[ÉCRAN - slide "Qu'est-ce qu'une action ?"]**

Chaque action dans OttoKit est composée de 4 éléments :

1. **L'app** - dans quelle application tu veux agir (WordPress, Google Sheets, Gmail, Slack...)
2. **L'événement** - quelle tâche tu veux exécuter (créer un article, ajouter une ligne, envoyer un email...)
3. **La connexion** - quel compte utiliser (ta connexion WordPress, ton compte Google...)
4. **La configuration** - les détails : quel titre pour l'article, quel destinataire pour l'email, quelles données dans chaque champ

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow existant avec un trigger et une action déjà configurés]
[Clique sur le bloc action]
[Pointe chaque élément dans le panneau latéral]

Décomposons une action réelle. Ici, on a un workflow qui détecte une nouvelle commande WooCommerce et envoie un email via Gmail.

[Pointe l'app sélectionnée : "Gmail"]

L'app, c'est Gmail.

[Pointe l'événement : "Send Email"]

L'événement, c'est "Send Email".

[Pointe la connexion : compte Google connecté]

La connexion, c'est ton compte Google.

[Pointe les champs de configuration : destinataire, sujet, corps]

Et la configuration, ce sont les champs : à qui, quel sujet, quel contenu.

**[ÉCRAN - slide "Action vs Trigger - la différence"]**

| | Trigger | Action |
|---|---|---|
| Rôle | Démarre le workflow | Exécute une tâche |
| Position | Toujours en premier | Après le trigger |
| Quantité | 1 seul par workflow | Autant que tu veux |
| Données | Fournit les données | Utilise les données |

Un workflow a toujours un seul trigger. Mais il peut avoir 1, 2, 5, 10 actions. Chaque action utilise les données du trigger ou des actions précédentes.

**[ÉCRAN - slide "Le processus de configuration"]**

Pour configurer une action, tu suis toujours le même processus :

1. Choisis l'app
2. Choisis l'événement
3. Sélectionne la connexion
4. Remplis les champs (statiques ou dynamiques)
5. Teste l'action
6. Enregistre

C'est le même schéma que pour les triggers. Si tu maîtrises les triggers du Module 3, tu maîtrises déjà la moitié du travail.

**[TRANSITION - face caméra]**

Passons à la pratique. Dans la prochaine leçon, tu configures ta première action : créer un article WordPress depuis un workflow OttoKit.

---

**Points clés**
- Une action = app + événement + connexion + configuration
- Un workflow peut contenir autant d'actions que nécessaire
- Les actions utilisent les données du trigger ou des actions précédentes
- Le processus de configuration est identique à celui des triggers

**Mots-clés SEO**
- OttoKit action definition
- configurer action OttoKit
- anatomie action automatisation WordPress
- OttoKit workflow action

---

## Leçon 4.2 - Configure une action WordPress (créer un article)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Première action concrète. On va configurer un workflow qui crée automatiquement un brouillon d'article WordPress quand un trigger se déclenche. C'est une des actions les plus courantes pour les créateurs de contenu.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow existant avec un trigger déjà configuré - par exemple un trigger Google Sheets "New Row Added" avec des colonnes Titre, Contenu, Catégorie]
[Clique sur le bouton "+" pour ajouter une action]

On part d'un trigger déjà configuré. Ici, Google Sheets détecte une nouvelle ligne avec un titre et un contenu d'article. On va ajouter une action pour créer l'article dans WordPress.

**[ÉCRAN - screencast sélection de l'app]**

[Dans le panneau latéral, tape "WordPress" dans la barre de recherche]
[Sélectionne "WordPress"]

On sélectionne WordPress. OttoKit détecte automatiquement les fonctionnalités disponibles grâce au plugin installé sur ton site.

**[ÉCRAN - screencast sélection de l'événement]**

[Scrolle dans la liste des événements]
[Montre quelques événements disponibles : "Create Post", "Create User", "Update Post"...]
[Sélectionne "Create Post"]

La liste des événements WordPress est longue. Créer un article, créer un utilisateur, mettre à jour un article... Ici, on choisit "Create Post".

**[ÉCRAN - screencast sélection de la connexion]**

[Sélectionne la connexion WordPress dans le dropdown]

On sélectionne la connexion WordPress. C'est celle du Module 2 - ton site schoolsWP.

**[ÉCRAN - screencast configuration des champs]**

[Montre les champs de configuration : Post Title, Post Content, Post Status, Post Type, Categories, Tags]

Voici les champs à remplir. Et c'est ici que ça devient intéressant : tu peux utiliser des données dynamiques.

[Clique dans le champ "Post Title"]
[Montre le sélecteur de données dynamiques - icône ou bouton à côté du champ]
[Sélectionne le champ "Titre" venant du trigger Google Sheets]

Pour le titre, on ne tape pas un texte fixe. On clique sur le sélecteur de données et on choisit le champ "Titre" du trigger. Quand une nouvelle ligne arrive dans le Sheet, le titre de cette ligne devient le titre de l'article.

[Fait la même chose pour "Post Content" - sélectionne "Contenu" du trigger]

Pareil pour le contenu. On mappe la colonne "Contenu" du Sheet vers le corps de l'article.

[Pour "Post Status", sélectionne "Draft" dans le dropdown]

Le statut : "Draft". Toujours commencer par un brouillon. Tu pourras relire avant de publier.

[Pour "Post Type", montre "Post" sélectionné par défaut]
[Pour "Categories", tape ou sélectionne une catégorie existante]

**[ÉCRAN - screencast test de l'action]**

[Clique sur le bouton "Test Action" ou "Test Step"]
[Montre le résultat : "Success" avec l'ID du post créé]

On teste. OttoKit crée un brouillon réel sur ton site. Tu vois le résultat : "Success", avec l'ID du post créé.

[Ouvre un nouvel onglet - va dans wp-admin → Articles → Brouillons]
[Montre l'article créé avec le titre et le contenu du Sheet]

Si tu vas dans ton WordPress, le brouillon est bien là. Titre et contenu correspondent aux données du Sheet.

[Reviens dans OttoKit - clique sur "Save"]

**[TRANSITION - face caméra]**

Tu viens de créer ta première action WordPress. Le processus est toujours le même : app, événement, connexion, champs, test. Dans la prochaine leçon, on fait la même chose avec Google Sheets.

---

**Points clés**
- "Create Post" crée un article WordPress avec titre, contenu, statut et catégorie
- Utilise les données dynamiques du trigger pour remplir les champs
- Toujours créer un brouillon ("Draft") par défaut - relire avant de publier
- Le test crée un article réel : vérifie dans wp-admin

**Mots-clés SEO**
- OttoKit créer article WordPress
- automatiser publication WordPress
- action WordPress OttoKit
- créer post automatiquement OttoKit

---

## Leçon 4.3 - Configure une action SaaS (ajouter une ligne Google Sheets)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Deuxième type d'action : une action SaaS. On va ajouter automatiquement une ligne dans Google Sheets chaque fois qu'un événement se produit sur ton site WordPress. C'est l'action la plus utilisée pour le suivi et le reporting.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce "Order Created" déjà configuré et avec des données Fetch Data]
[Clique sur "+" pour ajouter une action]

On part d'un trigger WooCommerce : chaque nouvelle commande déclenche le workflow. On va enregistrer les détails de la commande dans un Google Sheet.

**[ÉCRAN - screencast sélection de l'app et de l'événement]**

[Tape "Google Sheets" dans la barre de recherche]
[Sélectionne "Google Sheets"]
[Sélectionne l'événement "Add Row" ou "Insert Row"]

App : Google Sheets. Événement : "Add Row". On veut ajouter une ligne, pas modifier une ligne existante.

**[ÉCRAN - screencast sélection de la connexion]**

[Sélectionne la connexion Google dans le dropdown]

On sélectionne la connexion Google. Si tu ne l'as pas encore, clique sur "Add Connection" et autorise l'accès OAuth.

**[ÉCRAN - screencast sélection du spreadsheet et de la feuille]**

[Dans le champ "Spreadsheet", clique et sélectionne un tableur existant - par exemple "Suivi commandes schoolsWP"]
[Dans le champ "Sheet", sélectionne la feuille - par exemple "Sheet1" ou "Commandes"]

Tu choisis d'abord le spreadsheet, puis la feuille. OttoKit liste tous les tableurs de ton Google Drive.

**[ÉCRAN - screencast mapping des champs]**

[OttoKit affiche les colonnes du Sheet : colonne A (Date), colonne B (Client), colonne C (Email), colonne D (Montant), colonne E (Produit)]
[Pour la colonne "Date", sélectionne la donnée dynamique "order_date" du trigger WooCommerce]
[Pour "Client", sélectionne "billing_first_name" + texte statique " " + "billing_last_name"]
[Pour "Email", sélectionne "billing_email"]
[Pour "Montant", sélectionne "total"]
[Pour "Produit", sélectionne "line_items" ou le premier élément]

C'est le mapping. Pour chaque colonne du Sheet, tu sélectionnes la donnée correspondante du trigger. Date de commande, nom du client, email, montant, produit.

Remarque le champ "Client" : on combine prénom + espace + nom. C'est un mélange de données dynamiques et de texte statique. On verra ça en détail dans le Module 5.

**[ÉCRAN - screencast test de l'action]**

[Clique sur "Test Action"]
[Montre le résultat : "Success"]
[Ouvre Google Sheets dans un nouvel onglet]
[Montre la nouvelle ligne ajoutée avec les données de la commande]

Le test fonctionne. Si tu ouvres ton Google Sheet, la ligne est ajoutée avec toutes les données. Chaque nouvelle commande WooCommerce ajoutera une ligne automatiquement.

[Reviens dans OttoKit - clique sur "Save"]

**[TRANSITION - face caméra]**

Tu sais maintenant mapper des données WordPress vers Google Sheets. Prochaine étape : envoyer un email automatique avec Gmail.

---

**Points clés**
- "Add Row" ajoute une ligne dans Google Sheets avec les données du trigger
- Le mapping associe chaque colonne du Sheet à un champ du trigger
- On peut combiner données dynamiques et texte statique dans un même champ
- Toujours vérifier dans Google Sheets que la ligne est correctement ajoutée après le test

**Mots-clés SEO**
- OttoKit Google Sheets action
- ajouter ligne Google Sheets automatiquement
- mapper données OttoKit vers Sheets
- automatiser suivi commandes Google Sheets

---

## Leçon 4.4 - Configure une action email (envoyer un Gmail)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Troisième type d'action : l'email. Tu vas configurer un envoi automatique de Gmail avec un destinataire, un sujet et un contenu qui s'adaptent à chaque situation. C'est l'action la plus utilisée pour communiquer avec tes clients ou tes élèves.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger - par exemple "New User Registration" sur WordPress]
[Clique sur "+" pour ajouter une action]

On part d'un trigger WordPress : un nouvel utilisateur s'inscrit sur ton site. On va lui envoyer un email de bienvenue personnalisé.

**[ÉCRAN - screencast sélection app et événement]**

[Tape "Gmail" dans la barre de recherche]
[Sélectionne "Gmail"]
[Sélectionne l'événement "Send Email"]

App : Gmail. Événement : "Send Email".

**[ÉCRAN - screencast sélection de la connexion]**

[Sélectionne la connexion Google/Gmail dans le dropdown]

Tu utilises la même connexion Google que pour Sheets. Un seul compte Google donne accès à Gmail, Sheets, Drive, Calendar...

**[ÉCRAN - screencast configuration du destinataire]**

[Dans le champ "To", clique sur le sélecteur de données dynamiques]
[Sélectionne "user_email" depuis les données du trigger WordPress]

Le destinataire n'est pas une adresse fixe. On utilise le champ dynamique "user_email" du trigger. Chaque inscrit recevra l'email à sa propre adresse.

**[ÉCRAN - screencast configuration du sujet]**

[Dans le champ "Subject", tape le texte : "Bienvenue "]
[Clique sur le sélecteur dynamique et sélectionne "display_name" ou "first_name"]
[Le champ affiche maintenant : "Bienvenue {display_name}"]

Pour le sujet, on combine texte statique et donnée dynamique. "Bienvenue" + le prénom de l'inscrit. Chaque email aura un sujet personnalisé.

**[ÉCRAN - screencast configuration du corps]**

[Dans le champ "Body" ou "Message", tape :]

```
Bonjour {first_name},

Merci de rejoindre schoolsWP. Ton compte est maintenant actif.

Voici tes prochaines étapes :
1. Connecte-toi à ton espace élève
2. Découvre le catalogue de formations
3. Commence ta première leçon

À bientôt,
L'équipe schoolsWP
```

[Montre comment insérer les tokens dynamiques dans le corps du texte]
[Remplace {first_name} par le token réel en cliquant sur le sélecteur]

Le corps de l'email mélange du texte fixe et des données dynamiques. Ici, le prénom s'insère automatiquement. Chaque nouvel inscrit reçoit un email personnalisé.

**[ÉCRAN - screencast champs optionnels]**

[Montre les champs CC, BCC, Reply-To si disponibles]
[Montre le champ "From Name" si disponible - taper "schoolsWP"]

Quelques champs optionnels utiles : CC pour mettre quelqu'un en copie, BCC pour une copie invisible, et "From Name" pour que l'email affiche "schoolsWP" au lieu de ton adresse brute.

**[ÉCRAN - screencast test de l'action]**

[Clique sur "Test Action"]
[Montre le résultat : "Success - Email sent"]

On teste. L'email part immédiatement. Vérifie ta boîte de réception - ou celle de l'adresse de test.

[Ouvre Gmail dans un nouvel onglet - montre l'email reçu avec le prénom inséré dans le sujet et le corps]

L'email est arrivé. Le prénom est bien inséré. Le formatage est correct.

[Reviens dans OttoKit - clique sur "Save"]

**[TRANSITION - face caméra]**

Tu sais maintenant configurer trois types d'actions : WordPress, Google Sheets et Gmail. Mais un workflow ne se limite pas à une seule action. Dans la prochaine leçon, on enchaîne plusieurs actions dans un même workflow.

---

**Points clés**
- Le destinataire, le sujet et le corps de l'email acceptent des données dynamiques
- Combiner texte statique et tokens pour personnaliser chaque email
- Utiliser un email de test pendant le développement, pas ton email personnel
- Les champs CC, BCC et From Name sont optionnels mais utiles

**Mots-clés SEO**
- OttoKit envoyer email Gmail
- automatiser email WordPress OttoKit
- email personnalisé automatique WordPress
- action Gmail OttoKit configuration

---

## Leçon 4.5 - Multi-actions : enchaîne plusieurs actions dans un workflow

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Jusqu'ici, chaque workflow avait une seule action. En réalité, tu peux en enchaîner autant que tu veux. Un trigger, puis action 1, action 2, action 3... C'est là que les workflows deviennent vraiment utiles.

**[ÉCRAN - slide "Scénario schoolsWP"]**

On va construire un workflow complet :

**Trigger** : un élève s'inscrit sur schoolsWP (WordPress User Registration)

**Action 1** : créer un contact dans FluentCRM avec son nom et son email

**Action 2** : envoyer un email de bienvenue personnalisé via Gmail

**Action 3** : ajouter une ligne dans Google Sheets pour le suivi des inscriptions

Trois actions, un seul trigger. Tout se fait automatiquement.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow avec le trigger WordPress "User Registration" déjà configuré]

Le trigger est prêt. On va ajouter les trois actions une par une.

**[ÉCRAN - screencast ajout de l'action 1 - FluentCRM]**

[Clique sur "+" après le trigger]
[Sélectionne "FluentCRM" comme app]
[Sélectionne "Create/Update Contact" comme événement]
[Sélectionne la connexion WordPress]
[Mappe les champs : Email → user_email, First Name → first_name, Last Name → last_name]
[Sélectionne un tag ou une liste : "Nouveaux inscrits"]
[Clique sur "Save"]

Action 1 : créer un contact FluentCRM. On mappe l'email, le prénom, le nom. On ajoute le tag "Nouveaux inscrits" pour segmenter tes contacts.

**[ÉCRAN - screencast ajout de l'action 2 - Gmail]**

[Clique sur "+" après l'action 1]
[Sélectionne "Gmail" → "Send Email"]
[Sélectionne la connexion Google]
[To : user_email du trigger]
[Subject : "Bienvenue sur schoolsWP, {first_name}"]
[Body : message de bienvenue personnalisé]
[Clique sur "Save"]

Action 2 : envoyer l'email de bienvenue. On reprend le même schéma que la leçon précédente.

**[ÉCRAN - screencast ajout de l'action 3 - Google Sheets]**

[Clique sur "+" après l'action 2]
[Sélectionne "Google Sheets" → "Add Row"]
[Sélectionne la connexion Google]
[Sélectionne le spreadsheet "Inscriptions schoolsWP"]
[Mappe les colonnes : Date → date_registered, Nom → display_name, Email → user_email]
[Clique sur "Save"]

Action 3 : enregistrer dans Sheets. Date, nom, email. Chaque inscription sera tracée.

**[ÉCRAN - screencast vue d'ensemble du workflow]**

[Dézoom sur le canvas pour voir le workflow complet]
[Pointe la séquence : Trigger → Action 1 → Action 2 → Action 3]

Voici le workflow complet. Un trigger, trois actions. Elles s'exécutent dans l'ordre, de haut en bas.

**[ÉCRAN - slide "Ordre d'exécution - ce qu'il faut savoir"]**

Trois règles à retenir :

1. **Séquentiel** : les actions s'exécutent dans l'ordre. Action 1 se termine avant qu'action 2 ne commence.

2. **Dépendances** : action 2 peut utiliser les données du trigger ET de l'action 1. Action 3 peut utiliser les données du trigger, de l'action 1 ET de l'action 2.

3. **Échec** : si une action échoue, les suivantes ne s'exécutent pas. Si FluentCRM plante, l'email ne part pas et la ligne Sheets n'est pas ajoutée.

**[TRANSITION - face caméra]**

Tu as maintenant un workflow multi-actions fonctionnel. Mais avant de le publier, il faut tester chaque action. C'est le sujet de la prochaine leçon.

---

**Points clés**
- Un workflow peut contenir autant d'actions que nécessaire
- Les actions s'exécutent dans l'ordre, de haut en bas
- Chaque action peut utiliser les données du trigger et des actions précédentes
- Si une action échoue, les suivantes ne s'exécutent pas par défaut

**Mots-clés SEO**
- OttoKit multi actions workflow
- enchaîner actions OttoKit
- workflow plusieurs étapes OttoKit
- automatiser inscription WordPress FluentCRM

---

## Leçon 4.6 - Test d'action : valide AVANT de publier

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Tu ne publies jamais un workflow sans l'avoir testé. C'est la règle d'or. Un workflow mal testé, c'est un email qui part à la mauvaise personne, une ligne qui s'écrit au mauvais endroit, ou un article publié avec un titre vide.

**[ÉCRAN - slide "Pourquoi tester ?"]**

Tester, c'est vérifier trois choses :

1. **La connexion fonctionne** - l'app est bien accessible
2. **Les données sont correctes** - les bons champs arrivent aux bons endroits
3. **Le résultat est celui attendu** - l'article, l'email, la ligne sont conformes

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre le workflow multi-actions de la leçon 4.5]
[Clique sur l'action 1 - FluentCRM]

On reprend notre workflow à trois actions. On va tester chaque action individuellement.

**[ÉCRAN - screencast test de l'action 1]**

[Montre le bouton "Test Action" ou "Test Step" en bas du panneau]
[Clique dessus]
[Montre le résultat : "Success" avec les détails du contact créé]

Action 1 : FluentCRM. Clique sur "Test Action". OttoKit exécute l'action avec les données du Fetch Data du trigger. Résultat : "Success". Le contact est créé.

[Montre les détails retournés : contact_id, email, status]

OttoKit affiche les détails du résultat. L'ID du contact, l'email, le statut. Ces données deviennent disponibles pour les actions suivantes.

**[ÉCRAN - screencast test de l'action 2]**

[Clique sur l'action 2 - Gmail]
[Clique sur "Test Action"]
[Montre le résultat : "Success - Email sent"]

Action 2 : Gmail. Même processus. "Test Action", résultat "Success". L'email est envoyé.

**[ÉCRAN - screencast test de l'action 3]**

[Clique sur l'action 3 - Google Sheets]
[Clique sur "Test Action"]
[Montre le résultat : "Success - Row added"]

Action 3 : Google Sheets. Testé, réussi, ligne ajoutée.

**[ÉCRAN - slide "Que faire si un test échoue ?"]**

Si un test échoue, voici la démarche :

1. **Lis le message d'erreur** - OttoKit affiche la raison exacte
2. **Vérifie la connexion** - clique sur "Reconnect" si nécessaire
3. **Vérifie les champs** - un champ obligatoire manquant ? un format incorrect ?
4. **Vérifie les données source** - le Fetch Data du trigger a-t-il retourné des données ?
5. **Re-teste** - corrige et relance le test

Les erreurs les plus courantes :

- **"Connection expired"** - ré-autorise l'app dans les connexions
- **"Required field missing"** - un champ obligatoire est vide
- **"Permission denied"** - l'app n'a pas les droits suffisants
- **"Invalid value"** - le format de la donnée ne correspond pas (ex: texte dans un champ nombre)

**[ÉCRAN - screencast publication du workflow]**

[Après avoir testé les 3 actions avec succès]
[Clique sur le toggle "Active" ou "Publish" en haut du workflow]
[Le workflow passe de "Draft" à "Active"]

Toutes les actions sont testées avec succès. Maintenant, et seulement maintenant, tu peux publier. Active le workflow. Il est en production.

**[TRANSITION - face caméra]**

Tester individuellement, c'est la méthode fiable. Mais que se passe-t-il quand un workflow est publié et qu'une action échoue en conditions réelles ? C'est le sujet de la prochaine leçon.

---

**Points clés**
- Tester chaque action individuellement avant de publier le workflow
- Le test utilise les données du Fetch Data du trigger
- Lire le message d'erreur : OttoKit explique la raison de l'échec
- Ne jamais publier un workflow sans avoir testé toutes les actions

**Mots-clés SEO**
- OttoKit tester action
- test workflow OttoKit avant publication
- debugger action OttoKit
- OttoKit test step

---

## Leçon 4.7 - Gérer les erreurs : que se passe-t-il si une action échoue ?

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + historique

---

**[INTRO - face caméra]**

Ton workflow est publié, il tourne depuis des jours, tout va bien. Et puis un matin, une action échoue. L'API Google est temporairement indisponible, ou un champ arrive vide alors qu'il ne devrait pas. Que se passe-t-il exactement ?

**[ÉCRAN - slide "Quand une action échoue"]**

Quand une action échoue en production, OttoKit applique un comportement précis :

1. **L'action échoue** - OttoKit détecte l'erreur
2. **Auto-replay** - OttoKit retente automatiquement l'action. 6 tentatives espacées dans le temps.
3. **Si ça fonctionne à la tentative 3** - le workflow reprend normalement à l'action suivante
4. **Si ça échoue 6 fois** - OttoKit abandonne et marque l'exécution comme échouée

**[ÉCRAN - slide "Impact sur les actions suivantes"]**

Règle par défaut : si une action échoue définitivement (après 6 tentatives), les actions suivantes ne s'exécutent pas.

Dans notre workflow à 3 actions :
- Si l'action 1 (FluentCRM) échoue → l'action 2 (Gmail) et l'action 3 (Sheets) ne se lancent pas
- Si l'action 2 (Gmail) échoue → l'action 1 est déjà terminée avec succès, mais l'action 3 ne se lance pas

C'est un comportement de sécurité. Mieux vaut ne pas envoyer un email que d'envoyer un email avec des données corrompues.

**[ÉCRAN - screencast OttoKit - historique des exécutions]**

[Clique sur "History" dans la barre latérale]
[Montre la liste des exécutions avec des statuts : Success, Failed, In Progress]

L'historique te montre chaque exécution. En vert : succès. En rouge : échec. Clique sur une exécution échouée pour voir les détails.

[Clique sur une exécution échouée]
[Montre le détail étape par étape : trigger OK, action 1 OK, action 2 Failed]
[Montre le message d'erreur de l'action 2]

Tu vois exactement où ça a planté et pourquoi. Ici, l'action 2 a échoué - le message d'erreur t'explique la raison.

**[ÉCRAN - screencast OttoKit - simuler une erreur]**

[Ouvre un workflow de test]
[Dans une action Google Sheets, modifie le spreadsheet ID pour pointer vers un document supprimé ou inaccessible]
[Active le workflow et déclenche-le manuellement]
[Montre l'erreur dans l'historique : "Spreadsheet not found" ou équivalent]

Pour comprendre le mécanisme, on simule une erreur. On pointe l'action Sheets vers un document inexistant. Le trigger se déclenche, l'action échoue, et on voit le comportement dans l'historique.

[Montre le compteur de tentatives : 1/6, puis 2/6...]

OttoKit retente automatiquement. Tu n'as rien à faire. Si le problème est temporaire (API indisponible pendant 5 minutes), l'auto-replay corrige la situation tout seul.

**[ÉCRAN - slide "Bonnes pratiques de gestion d'erreur"]**

1. **Consulte l'historique régulièrement** - même si tout semble fonctionner
2. **Configure les notifications** - OttoKit peut t'envoyer un email quand un workflow échoue (dans Settings)
3. **Utilise des données de test robustes** - évite les champs optionnels non gérés
4. **Prévois les cas limites** - un email vide, un montant à zéro, un nom avec des caractères spéciaux
5. **Dans le Module 5**, tu apprendras à définir des valeurs par défaut pour éviter les champs vides

**[ÉCRAN - slide "Récapitulatif auto-replay"]**

| Situation | Comportement |
|---|---|
| Erreur temporaire (API down 2 min) | Auto-replay réussit → workflow continue |
| Erreur permanente (mauvais ID spreadsheet) | 6 tentatives échouent → workflow stoppe |
| Action 2 échoue | Actions 3, 4, 5... ne s'exécutent pas |
| Action 1 réussit puis action 2 échoue | Action 1 n'est pas annulée (pas de rollback) |

Point important : il n'y a pas de rollback. Si l'action 1 a créé un contact FluentCRM et que l'action 2 échoue, le contact reste dans FluentCRM. OttoKit n'annule pas ce qui a déjà été fait.

**[TRANSITION - face caméra]**

Tu sais maintenant comment OttoKit gère les erreurs. Le Module 4 est terminé. Passe au quiz pour valider tes acquis avant d'attaquer le Module 5 sur le data mapping et les formatters.

---

**Points clés**
- L'auto-replay retente une action échouée 6 fois automatiquement
- Si une action échoue définitivement, les actions suivantes ne s'exécutent pas
- Il n'y a pas de rollback : les actions déjà réussies ne sont pas annulées
- L'historique montre le détail de chaque exécution, étape par étape
- Consulter l'historique régulièrement pour détecter les échecs silencieux

**Mots-clés SEO**
- OttoKit gestion erreur workflow
- auto-replay OttoKit
- debugger workflow OttoKit
- OttoKit historique exécution

---

## Notes de production - Module 4

### Captures à préparer
- Panneau latéral d'une action avec les 4 éléments visibles (app, événement, connexion, champs)
- Configuration action "Create Post" WordPress - champs titre, contenu, statut
- Sélecteur de données dynamiques dans un champ d'action
- Configuration action "Add Row" Google Sheets - mapping colonnes
- Configuration action "Send Email" Gmail - destinataire dynamique, sujet, corps
- Canvas avec workflow 3 actions (FluentCRM + Gmail + Sheets)
- Bouton "Test Action" et résultat "Success"
- Résultat d'un test échoué avec message d'erreur
- Historique des exécutions avec statuts succès/échec
- Détail d'une exécution échouée - étape par étape
- Toggle publication du workflow (Draft → Active)

### Environnement de démo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec :
  - WooCommerce installé (au moins 1 commande de test)
  - FluentCRM installé (pour l'action "Create Contact")
  - Au moins 1 utilisateur de test inscrit
- Google Sheet "Suivi commandes schoolsWP" avec colonnes : Date, Client, Email, Montant, Produit
- Google Sheet "Inscriptions schoolsWP" avec colonnes : Date, Nom, Email
- Compte Gmail connecté à OttoKit
- Adresse email de test (ne pas utiliser son email personnel pour les démos)

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 4.1 | 5 min |
| 4.2 | 6 min |
| 4.3 | 6 min |
| 4.4 | 6 min |
| 4.5 | 6 min |
| 4.6 | 5 min |
| 4.7 | 6 min |
| **Total M4** | **40 min** |

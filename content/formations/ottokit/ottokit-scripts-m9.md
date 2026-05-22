# Scripts vidéo — Module 9 : Intégrations SaaS : Google, Slack, Stripe, WhatsApp

**Formation** : Maîtriser OttoKit
**Module** : M9 — Intégrations SaaS : Google, Slack, Stripe, WhatsApp
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~43 min de vidéo
**Date** : 2026-03-30

---

## Leçon 9.1 — Google Sheets : dashboard automatisé de tes ventes

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Google Sheets

---

**[INTRO — face caméra]**

Tu veux un tableau de bord de tes ventes qui se met à jour tout seul. Pas besoin de Metabase, pas besoin de plugin analytics payant. Un Google Sheet + OttoKit, et chaque vente s'enregistre en temps réel.

**[ÉCRAN — screencast Google Sheets]**

[Ouvre Google Sheets]
[Crée un nouveau spreadsheet : "Dashboard Ventes schoolsWP"]
[Crée les colonnes dans la première ligne :]

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Date | Commande | Client | Email | Produit | Montant | Source |

[Fige la première ligne (Affichage > Figer > 1 ligne)]

On prépare le tableur. Les colonnes correspondent aux données qu'OttoKit va envoyer. La première ligne figée sert d'en-tête.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Vente WooCommerce → Dashboard Sheets"]
[Clique sur le bloc trigger]
[Sélectionne "WooCommerce" > "Order Completed"]
[Sélectionne la connexion WordPress]
[Clique sur "Fetch Data" > "Save"]

Le trigger est "Order Completed". On ne veut enregistrer que les ventes confirmées, pas les paniers abandonnés.

**[ÉCRAN — screencast action Google Sheets]**

[Clique sur "+" > sélectionne "Google Sheets"]
[Sélectionne l'action "Add Row"]
[Sélectionne la connexion Google]
[Sélectionne le spreadsheet "Dashboard Ventes schoolsWP"]
[Sélectionne la feuille "Sheet1"]
[Mappe les colonnes :]

| Colonne | Champ OttoKit |
|---------|---------------|
| Date | {{date_completed}} |
| Commande | {{order_id}} |
| Client | {{billing_first_name}} {{billing_last_name}} |
| Email | {{billing_email}} |
| Produit | {{line_items_name}} |
| Montant | {{total}} |
| Source | {{payment_method_title}} |

[Clique sur "Test Action"]
[Retourne dans Google Sheets pour montrer la ligne ajoutée]
[Clique sur "Save"]

Le mapping est direct. Chaque champ du trigger correspond à une colonne du tableur. Le test confirme que la ligne s'ajoute correctement.

**[ÉCRAN — screencast Google Sheets — formules et formatage]**

[Dans le Sheet, ajoute une ligne de totaux en bas :]
- Cellule F100 : =SOMME(F2:F99)
- Cellule G1 (nouvel onglet "Résumé") : =NB.VAL(A2:A999) pour le nombre de ventes
[Ajoute un filtre sur la colonne Date]
[Ajoute une mise en forme conditionnelle : montant > 100 EUR en vert]

Le tableur reçoit les données brutes. À toi d'ajouter les formules. Un total des ventes, un compteur de commandes, une mise en forme conditionnelle pour repérer les grosses commandes. Google Sheets fait le reste.

**[ÉCRAN — slide "Aller plus loin avec le dashboard"]**

- **Onglet "Résumé"** : formules SOMME, MOYENNE, NB.SI par mois
- **Graphique intégré** : courbe des ventes quotidiennes
- **Partage** : donne un accès lecture à ton associé ou ton comptable
- **Alertes Sheets** : notification email quand une cellule change

Tu n'as pas besoin d'un outil de Business Intelligence. Un Google Sheet bien structuré + OttoKit, c'est un dashboard fonctionnel et gratuit.

**[TRANSITION — face caméra]**

Ton dashboard de ventes tourne. Dans la prochaine leçon, on passe aux emails transactionnels : envoyer un email personnalisé automatiquement après chaque achat.

---

**Points clés**
- Préparer le tableur avant de configurer le workflow (colonnes = champs)
- Utiliser "Order Completed" (pas "Created") pour ne comptabiliser que les ventes confirmées
- Les formules Google Sheets transforment les données brutes en dashboard
- Ce dashboard est gratuit et partageable

**Mots-clés SEO**
- OttoKit Google Sheets dashboard
- tableau de bord ventes WordPress
- automatiser Google Sheets WooCommerce
- dashboard automatique WordPress

---

## Leçon 9.2 — Gmail / SMTP : emails transactionnels automatiques

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

WooCommerce envoie déjà des emails de confirmation. Mais ils sont génériques et souvent moches. Avec OttoKit + Gmail, tu peux envoyer des emails personnalisés, au bon moment, avec le ton de ta marque.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Email personnalisé post-achat"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Même trigger que la leçon précédente. La différence, c'est l'action.

**[ÉCRAN — screencast connexion Gmail]**

[Clique sur "+" > sélectionne "Gmail"]
[Si c'est la première connexion Gmail, montre le flux OAuth :]
[Clique sur "Connect Gmail"]
[Sélectionne le compte Google]
[Accepte les permissions : envoyer des emails en ton nom]
[Retourne dans OttoKit — connexion confirmée]

La connexion Gmail se fait une seule fois. Tu autorises OttoKit à envoyer des emails depuis ton adresse. C'est un OAuth standard — tes identifiants ne sont pas stockés par OttoKit.

**[ÉCRAN — screencast configuration de l'email]**

[Sélectionne l'action "Send Email"]
[Configure :]
- From Name : schoolsWP
- To : {{billing_email}}
- Subject : {{billing_first_name}}, ta commande #{{order_id}} est confirmée
- Body :

```
Bonjour {{billing_first_name}},

Ta commande #{{order_id}} de {{total}} EUR est confirmée. Voici le récap :

Produit : {{line_items_name}}
Montant : {{total}} EUR
Date : {{date_completed}}

Prochaine étape : tu recevras un email de suivi avec les informations d'accès.

Des questions ? Réponds directement à cet email.

Merci de ta confiance,
Michael — schoolsWP
```

[Montre le sélecteur de données dynamiques pour chaque champ variable]
[Clique sur "Test Action"]
[Ouvre Gmail pour montrer l'email reçu]

Chaque variable entre doubles accolades est remplacée par la donnée réelle. Le prénom, le numéro de commande, le montant, le produit — tout est dynamique. L'email est signé par une personne, pas par "noreply@".

**[ÉCRAN — slide "Gmail vs SMTP : lequel choisir ?"]**

| | Gmail | SMTP |
|---|---|---|
| Configuration | OAuth (2 clics) | Serveur, port, identifiants |
| Limite d'envoi | 500/jour (gratuit) | Dépend du fournisseur |
| Délivrabilité | Bonne (Google) | Dépend de la configuration |
| Cas d'usage | < 500 emails/jour | Volume important, domaine custom |
| OttoKit | App native | App "SMTP / Send Email" |

Si tu envoies moins de 500 emails par jour, Gmail suffit. Au-delà, configure un SMTP dédié (Brevo, Amazon SES, Mailgun). OttoKit supporte les deux.

**[ÉCRAN — slide "Bonnes pratiques emails transactionnels"]**

- Personnalise l'objet avec le prénom — les taux d'ouverture augmentent de 20%
- Signe avec ton vrai prénom, pas "L'équipe" — ça humanise
- Ajoute un call-to-action clair (lien vers le cours, lien vers le compte)
- N'envoie pas plus de 2 emails liés à la même commande dans les 24h

**[TRANSITION — face caméra]**

Les emails partent automatiquement. Prochaine leçon : on notifie l'équipe en temps réel avec Slack à chaque grosse vente.

---

**Points clés**
- La connexion Gmail OAuth se fait une seule fois
- Les variables dynamiques personnalisent chaque email automatiquement
- Limite Gmail : 500 emails/jour (au-delà, utiliser un SMTP)
- Signer avec un vrai prénom améliore l'engagement

**Mots-clés SEO**
- OttoKit Gmail email automatique
- email transactionnel WordPress
- automatiser email post-achat
- OttoKit SMTP configuration

---

## Leçon 9.3 — Slack : notifications équipe en temps réel

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Slack

---

**[INTRO — face caméra]**

Tu veux que toute l'équipe voie passer les ventes en temps réel. Pas dans un email qu'on oublie de lire — dans un channel Slack dédié. Et seulement les ventes au-dessus de 100 EUR, pour ne pas noyer le channel.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Vente > 100 EUR → notification Slack"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Le trigger est le même. La différence, c'est le filtre et la destination.

**[ÉCRAN — screencast ajout du Filter]**

[Clique sur "+" > sélectionne "Filter"]
[Configure : "total" is greater than "100"]
[Clique sur "Save"]

Le filtre laisse passer uniquement les commandes de plus de 100 EUR. Les petites commandes ne déclenchent pas de notification. Ça évite le bruit.

**[ÉCRAN — screencast connexion Slack]**

[Clique sur "+" > sélectionne "Slack"]
[Si c'est la première connexion, montre le flux OAuth :]
[Clique sur "Connect Slack"]
[Sélectionne le workspace Slack]
[Autorise OttoKit à publier des messages]
[Retourne dans OttoKit — connexion confirmée]

Comme pour Gmail, la connexion Slack se fait une seule fois via OAuth.

**[ÉCRAN — screencast configuration du message]**

[Sélectionne l'action "Send Channel Message"]
[Sélectionne le channel : #ventes]
[Configure le message :]

```
:moneybag: Nouvelle vente de {{total}} EUR !

Client : {{billing_first_name}} {{billing_last_name}}
Produit : {{line_items_name}}
Commande : #{{order_id}}
```

[Clique sur "Test Action"]
[Ouvre Slack pour montrer le message dans le channel #ventes]
[Clique sur "Save"]

Le message Slack supporte le formatage Markdown et les emojis. Ici, l'emoji moneybag attire l'œil. Les informations essentielles sont là : montant, client, produit, numéro de commande.

**[ÉCRAN — slide "Autres notifications Slack utiles"]**

- **Inscription formation** : ":mortar_board: Nouvel élève : {{student_name}} dans {{course_title}}"
- **Formulaire contact** : ":email: Nouveau lead : {{name}} — {{email}}"
- **Erreur workflow** : ":warning: Le workflow {{workflow_name}} a échoué"
- **Objectif atteint** : ":trophy: 100 ventes ce mois — bravo l'équipe !"

Slack, c'est ton centre de notifications internes. Tu choisis ce qui mérite d'apparaître et dans quel channel.

**[ÉCRAN — slide "Mentions et DM"]**

Tu peux aussi :
- Mentionner quelqu'un : `<@USER_ID>` dans le message pour notifier une personne spécifique
- Envoyer un message privé (DM) au lieu d'un channel
- Poster dans plusieurs channels avec plusieurs actions

**[TRANSITION — face caméra]**

L'équipe est notifiée en temps réel. Prochaine leçon : on passe à Stripe et la gestion automatisée des paiements et abonnements.

---

**Points clés**
- Le filtre > 100 EUR évite de noyer le channel avec les petites commandes
- La connexion Slack OAuth se fait une seule fois
- Le formatage Markdown et les emojis rendent les messages lisibles
- Slack est idéal pour les notifications internes (pas pour les clients)

**Mots-clés SEO**
- OttoKit Slack notification
- notification vente Slack WordPress
- automatiser notification équipe
- OttoKit Slack intégration

---

## Leçon 9.4 — Stripe : paiement → actions automatiques

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Stripe dashboard

---

**[INTRO — face caméra]**

Stripe gère tes paiements. Mais un paiement réussi, c'est le début d'un processus, pas la fin. Ouvrir l'accès à un cours, envoyer une facture, mettre à jour le CRM, notifier l'équipe. OttoKit automatise toute la chaîne post-paiement.

**[ÉCRAN — screencast connexion Stripe dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection"]
[Sélectionne "Stripe"]
[Montre le flux de connexion : API Key ou OAuth]
[Colle la Restricted API Key Stripe (pas la Secret Key)]
[Montre le badge "Connected"]

Pour connecter Stripe, tu utilises une API Key restreinte. Pas la clé secrète complète — une clé avec uniquement les permissions nécessaires. C'est une bonne pratique de sécurité.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Paiement Stripe → accès + CRM + notification"]
[Clique sur le bloc trigger]
[Sélectionne "Stripe"]
[Sélectionne l'événement "Payment Succeeded" ou "Checkout Session Completed"]
[Sélectionne la connexion Stripe]
[Clique sur "Fetch Data"]
[Montre les champs : customer_email, customer_name, amount, currency, product_name, subscription_id]
[Clique sur "Save"]

Le trigger "Payment Succeeded" se déclenche quand un paiement Stripe est confirmé. Les champs disponibles : email du client, nom, montant, devise, produit, identifiant d'abonnement.

**[ÉCRAN — screencast action 1 — FluentCRM tag "client"]**

[Clique sur "+" > sélectionne "FluentCRM"]
[Sélectionne "Add Tag to Contact"]
[Configure :]
- Email : {{customer_email}}
- Tag : "client"
- Create if not exists : oui

[Clique sur "Save"]

Première action : le contact passe de "prospect" à "client" dans FluentCRM. Le tag "client" est posé. Ça peut déclencher un autre workflow — par exemple, arrêter la séquence de nurturing.

**[ÉCRAN — screencast action 2 — Inscription TutorLMS]**

[Clique sur "+" > sélectionne "TutorLMS"]
[Sélectionne "Enroll Student in Course"]
[Configure :]
- Student Email : {{customer_email}}
- Course : Formation Premium schoolsWP

[Clique sur "Save"]

Deuxième action : ouvrir l'accès au cours. L'élève est automatiquement inscrit à la formation premium dans TutorLMS. Pas d'intervention manuelle, pas de délai.

**[ÉCRAN — screencast action 3 — Email de bienvenue premium]**

[Clique sur "+" > sélectionne "Send Email"]
[Configure :]
- To : {{customer_email}}
- Subject : Bienvenue dans la formation premium !
- Body :

```
Bonjour {{customer_name}},

Ton paiement de {{amount}} {{currency}} est confirmé. Ton accès à la formation premium est actif.

Connecte-toi ici pour commencer : [lien]

Premier conseil : commence par le Module 4 — c'est là que la magie commence.

Des questions ? Réponds à cet email.

Michael — schoolsWP
```

[Clique sur "Save"]

**[ÉCRAN — screencast vue globale]**

[Montre le workflow complet : Trigger Stripe → FluentCRM tag → TutorLMS inscription → Email]
[Active le workflow]

Le cycle complet : paiement confirmé → tag CRM "client" → inscription au cours → email de bienvenue. Quatre étapes, zéro intervention.

**[ÉCRAN — slide "Gérer les abonnements Stripe"]**

Pour les abonnements mensuels ou annuels :

| Événement Stripe | Action OttoKit |
|-----------------|----------------|
| Subscription Created | Inscrire au cours + tag "abonné" |
| Subscription Renewed | Mettre à jour la date d'expiration |
| Subscription Cancelled | Retirer le tag "abonné" + email de rétention |
| Payment Failed | Email "mettre à jour ta carte" |

Chaque événement Stripe peut déclencher un workflow différent. Tu gères tout le cycle de vie de l'abonnement.

**[TRANSITION — face caméra]**

Stripe est connecté. Prochaine leçon : WhatsApp Cloud API — envoyer des messages automatiques à tes clients sur leur téléphone.

---

**Points clés**
- Utiliser une API Key restreinte Stripe (pas la clé secrète)
- Le trigger "Payment Succeeded" couvre les paiements uniques et les abonnements
- Chaque événement Stripe (création, renouvellement, annulation) peut déclencher un workflow
- Le workflow combine CRM + LMS + email en une seule chaîne

**Mots-clés SEO**
- OttoKit Stripe intégration
- automatiser paiement Stripe WordPress
- Stripe WooCommerce OttoKit
- gestion abonnement automatique WordPress

---

## Leçon 9.5 — WhatsApp Cloud API : messages automatiques

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Meta Business Suite

---

**[INTRO — face caméra]**

Tes clients lisent leurs emails... parfois. Mais leurs messages WhatsApp ? Quasiment toujours. Envoyer une confirmation de commande ou un rappel de formation par WhatsApp, ça change le taux de lecture. OttoKit le permet via la WhatsApp Cloud API.

**[ÉCRAN — slide "Prérequis WhatsApp Cloud API"]**

Avant de commencer, tu as besoin de :

1. **Un compte Meta Business vérifié** — pas un compte perso, un compte business
2. **Une app dans Meta for Developers** — c'est gratuit
3. **Un numéro de téléphone dédié** — pas ton numéro perso
4. **Des templates de messages pré-approuvés** — obligatoire pour les messages sortants

C'est la partie la plus complexe de ce module. Une fois la configuration faite, l'envoi est automatique.

**[ÉCRAN — screencast Meta Business Suite]**

[Ouvre developers.facebook.com]
[Montre l'app Meta existante (ou le bouton "Create App")]
[Va dans WhatsApp > Getting Started]
[Montre le numéro de téléphone de test et le token d'accès temporaire]

Meta fournit un numéro de test et un token temporaire pour tes premiers essais. En production, tu utiliseras ton propre numéro et un token permanent.

**[ÉCRAN — screencast templates WhatsApp]**

[Va dans WhatsApp > Message Templates]
[Montre un template existant ou crée-en un :]
- Nom : confirmation_commande
- Langue : Français
- Catégorie : Transactional
- Corps :

```
Bonjour {{1}},

Ta commande #{{2}} de {{3}} EUR est confirmée.
Tu recevras un email de suivi sous 24h.

Merci — schoolsWP
```

[Soumets le template pour approbation]

Les templates doivent être approuvés par Meta avant utilisation. C'est une contrainte obligatoire. Les variables {{1}}, {{2}}, {{3}} seront remplies par OttoKit.

**[ÉCRAN — screencast connexion WhatsApp dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection" > "WhatsApp Cloud API"]
[Renseigne le Phone Number ID et le Access Token]
[Montre le badge "Connected"]

La connexion nécessite deux informations : l'identifiant de ton numéro de téléphone et le token d'accès. Les deux se trouvent dans ton dashboard Meta for Developers.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Commande → confirmation WhatsApp"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]
[Clique sur "+" > sélectionne "WhatsApp Cloud API"]
[Sélectionne l'action "Send Template Message"]
[Configure :]
- To : {{billing_phone}}
- Template : confirmation_commande
- Variable 1 : {{billing_first_name}}
- Variable 2 : {{order_id}}
- Variable 3 : {{total}}

[Clique sur "Test Action"]
[Montre le message reçu sur WhatsApp (screenshot ou téléphone)]
[Clique sur "Save"]

Le workflow mappe les variables du template avec les données de la commande. Le prénom, le numéro de commande, le montant — tout est injecté automatiquement.

**[ÉCRAN — slide "Points d'attention WhatsApp"]**

- **Format du numéro** : international avec indicatif (+33 pour la France) — pas de 06
- **Fenêtre de 24h** : tu peux envoyer un message libre uniquement si le client t'a écrit dans les 24h. Sinon, utilise un template approuvé
- **Coût** : WhatsApp Cloud API facture par conversation (environ 0.05 EUR par conversation en France)
- **RGPD** : le client doit avoir donné son consentement pour recevoir des messages WhatsApp

**[TRANSITION — face caméra]**

WhatsApp est branché. Prochaine leçon : on automatise la création d'événements Google Calendar après une inscription.

---

**Points clés**
- WhatsApp Cloud API nécessite un compte Meta Business vérifié
- Les templates de messages doivent être approuvés par Meta
- Le numéro de téléphone doit être au format international
- Coût approximatif : 0.05 EUR par conversation en France

**Mots-clés SEO**
- OttoKit WhatsApp Cloud API
- message WhatsApp automatique WordPress
- WhatsApp Business WordPress automatisation
- envoyer WhatsApp OttoKit

---

## Leçon 9.6 — Google Calendar : événements automatiques

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Google Calendar

---

**[INTRO — face caméra]**

Un élève s'inscrit à ta formation. Tu veux lui envoyer une invitation calendrier pour la session de bienvenue du lundi suivant. Manuellement, ça prend 2 minutes par élève. Avec 50 inscriptions par semaine, ça fait presque 2 heures. OttoKit le fait en zéro seconde.

**[ÉCRAN — screencast connexion Google Calendar]**

[Ouvre OttoKit > Connections]
[Si Google est déjà connecté, montre que Calendar est inclus dans la même connexion OAuth]
[Sinon, montre le flux OAuth Google avec la permission "Gérer les agendas"]

Si tu as déjà connecté Google Sheets ou Gmail, la connexion Google Calendar peut utiliser la même autorisation. Vérifie que la permission "Gérer les agendas" est incluse.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Inscription → invitation calendrier"]
[Trigger : TutorLMS > Student Enrolled in Course]
[Connexion WordPress > Fetch Data > Save]

Le trigger est l'inscription TutorLMS. On pourrait aussi utiliser un trigger Stripe (paiement) ou Fluent Forms (soumission formulaire).

**[ÉCRAN — screencast action Google Calendar]**

[Clique sur "+" > sélectionne "Google Calendar"]
[Sélectionne l'action "Create Event"]
[Configure :]
- Calendar : schoolsWP — Sessions de bienvenue
- Title : Session de bienvenue — {{course_title}}
- Start : [prochain lundi 10:00]
- End : [prochain lundi 10:30]
- Description :

```
Bienvenue dans "{{course_title}}" !

Cette session de 30 minutes te présente :
- Le plan du cours
- Comment poser tes questions
- Les ressources disponibles

Lien visio : [lien Google Meet]
```

- Attendees : {{student_email}}
- Send Notifications : Yes

[Clique sur "Test Action"]
[Ouvre Google Calendar pour montrer l'événement créé]
[Clique sur "Save"]

L'événement est créé dans ton agenda et l'invitation est envoyée à l'élève. Il reçoit un email avec le bouton "Ajouter à mon agenda". Le lien visio, la description, l'horaire — tout est pré-rempli.

**[ÉCRAN — slide "Cas d'usage Google Calendar + OttoKit"]**

- **Session de bienvenue** : invitation automatique après inscription
- **Rappel de webinar** : créer l'événement quand le participant s'inscrit
- **RDV client** : après un achat premium, bloquer un créneau coaching
- **Deadline interne** : quand un contenu est validé, créer un rappel "publication J+3"
- **Suivi formateur** : créer un événement "relance élève" 7 jours après inscription si inactif

**[TRANSITION — face caméra]**

L'agenda se remplit automatiquement. Dernière leçon avant le quiz : on automatise la gestion de projet avec Trello, ClickUp ou Asana.

---

**Points clés**
- Google Calendar utilise la même connexion OAuth que Sheets et Gmail
- L'action "Create Event" envoie automatiquement l'invitation par email
- Le champ "Attendees" ajoute l'élève comme participant
- Utile pour les sessions de bienvenue, webinars, coaching, rappels

**Mots-clés SEO**
- OttoKit Google Calendar automatisation
- créer événement automatique WordPress
- invitation calendrier automatique
- Google Calendar OttoKit intégration

---

## Leçon 9.7 — Trello / ClickUp / Asana : gestion de projet automatisée

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + Trello

---

**[INTRO — face caméra]**

Tu utilises Trello, ClickUp ou Asana pour gérer tes projets. À chaque nouveau client, tu crées manuellement une carte ou une tâche. Avec OttoKit, cette tâche se crée automatiquement — avec toutes les informations du client déjà remplies.

**[ÉCRAN — screencast connexion Trello dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection" > "Trello"]
[Montre le flux OAuth Trello]
[Autorise OttoKit à accéder au workspace Trello]
[Montre le badge "Connected"]

La connexion Trello suit le même schéma OAuth que Google ou Slack. Une seule autorisation, puis c'est automatique.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Nouveau client → tâche Trello"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Le trigger est une commande complétée. Chaque nouvelle vente crée une tâche dans ton outil de gestion de projet.

**[ÉCRAN — screencast action Trello]**

[Clique sur "+" > sélectionne "Trello"]
[Sélectionne l'action "Create Card"]
[Configure :]
- Board : schoolsWP — Opérations
- List : "Nouveaux clients"
- Name : Client : {{billing_first_name}} {{billing_last_name}} — #{{order_id}}
- Description :

```
Nouveau client depuis WooCommerce

Email : {{billing_email}}
Produit : {{line_items_name}}
Montant : {{total}} EUR
Date : {{date_completed}}

Tâches :
- [ ] Vérifier l'accès au cours
- [ ] Envoyer le kit de bienvenue
- [ ] Planifier la session onboarding
```

- Due Date : [+3 jours]
- Labels : "Onboarding"
- Members : [Assigner à un membre de l'équipe]

[Clique sur "Test Action"]
[Ouvre Trello pour montrer la carte créée dans la colonne "Nouveaux clients"]
[Clique sur "Save"]

La carte Trello contient tout : les informations du client, la liste des tâches à faire, une date limite, une étiquette et un responsable. L'équipe sait exactement quoi faire sans chercher les infos.

**[ÉCRAN — slide "ClickUp et Asana : même logique"]**

| Trello | ClickUp | Asana |
|--------|---------|-------|
| Create Card | Create Task | Create Task |
| Board / List | Space / List | Project / Section |
| Labels | Tags | Tags |
| Due Date | Due Date | Due Date |
| Members | Assignees | Assignees |

La logique est identique pour ClickUp et Asana. Seuls les noms changent. Tu choisis ton outil de gestion de projet, OttoKit s'adapte.

**[ÉCRAN — slide "Autres automatisations gestion de projet"]**

- **Nouveau lead → carte "À contacter"** dans la colonne prospection
- **Script validé → tâche "Produire vidéo module X"** assignée au monteur
- **Ticket support → carte avec priorité et date limite**
- **Fin de formation → déplacer la carte dans "Terminé"**
- **Rappel interne → créer une tâche quand un workflow échoue**

L'automatisation de la gestion de projet, c'est ce qui transforme un outil passif en système actif. Les tâches se créent sans que personne ait besoin d'y penser.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow complet : Trigger WooCommerce → Create Card Trello]
[Active le workflow]

**[TRANSITION — face caméra]**

Ce module est terminé. Tu sais maintenant connecter les principales apps SaaS à OttoKit : Google Sheets pour le reporting, Gmail pour les emails, Slack pour les notifications équipe, Stripe pour les paiements, WhatsApp pour les messages clients, Google Calendar pour les invitations, et Trello pour la gestion de projet. Passe au quiz pour valider tes acquis avant d'attaquer les webhooks et l'API dans le Module 10.

---

**Points clés**
- Trello, ClickUp et Asana fonctionnent de la même manière avec OttoKit
- La carte/tâche inclut les données du trigger (client, produit, montant)
- Les checklists et dates limites structurent le suivi
- L'automatisation transforme un outil de gestion passive en système proactif

**Mots-clés SEO**
- OttoKit Trello intégration
- automatiser gestion projet WordPress
- créer tâche automatique Trello ClickUp
- OttoKit gestion de projet automatisée

---

## Notes de production — Module 9

### Captures à préparer
- Google Sheets : spreadsheet "Dashboard Ventes schoolsWP" avec colonnes et lignes ajoutées
- Google Sheets : formules SOMME, graphique intégré, mise en forme conditionnelle
- Gmail : email personnalisé reçu avec données dynamiques
- Slack : message de notification dans le channel #ventes
- Stripe Dashboard : API Keys > Restricted Key
- OttoKit : connexion Stripe avec badge "Connected"
- Meta for Developers : WhatsApp > Getting Started (numéro test, token)
- Meta : WhatsApp Message Templates — template "confirmation_commande"
- WhatsApp : message reçu sur téléphone (screenshot)
- Google Calendar : événement créé avec invitation et lien visio
- Trello : carte créée dans la colonne "Nouveaux clients" avec description et checklist
- Canvas OttoKit : chaque workflow complet (7 workflows au total)

### Environnement de démo
- Compte OttoKit avec plan actif
- Site WordPress schoolsWP avec WooCommerce + TutorLMS + FluentCRM
- Google Workspace : Sheets, Gmail, Calendar connectés
- Workspace Slack avec channel #ventes
- Compte Stripe avec Restricted API Key (mode test)
- Compte Meta Business vérifié avec app WhatsApp Cloud API configurée
- Numéro WhatsApp de test + template approuvé
- Board Trello "schoolsWP — Opérations" avec colonne "Nouveaux clients"
- Téléphone pour screenshot WhatsApp

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 9.1 | 7 min |
| 9.2 | 6 min |
| 9.3 | 5 min |
| 9.4 | 7 min |
| 9.5 | 7 min |
| 9.6 | 5 min |
| 9.7 | 6 min |
| **Total M9** | **43 min** |

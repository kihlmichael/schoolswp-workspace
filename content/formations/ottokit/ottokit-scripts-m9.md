# Scripts video — Module 9 : Integrations SaaS : Google, Slack, Stripe, WhatsApp

**Formation** : Maitriser OttoKit
**Module** : M9 — Integrations SaaS : Google, Slack, Stripe, WhatsApp
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~43 min de video
**Date** : 2026-03-30

---

## Lecon 9.1 — Google Sheets : dashboard automatise de tes ventes

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Google Sheets

---

**[INTRO — face camera]**

Tu veux un tableau de bord de tes ventes qui se met a jour tout seul. Pas besoin de Metabase, pas besoin de plugin analytics payant. Un Google Sheet + OttoKit, et chaque vente s'enregistre en temps reel.

**[ECRAN — screencast Google Sheets]**

[Ouvre Google Sheets]
[Cree un nouveau spreadsheet : "Dashboard Ventes schoolsWP"]
[Cree les colonnes dans la premiere ligne :]

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Date | Commande | Client | Email | Produit | Montant | Source |

[Fige la premiere ligne (Affichage > Figer > 1 ligne)]

On prepare le tableur. Les colonnes correspondent aux donnees qu'OttoKit va envoyer. La premiere ligne figee sert d'en-tete.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Vente WooCommerce → Dashboard Sheets"]
[Clique sur le bloc trigger]
[Selectionne "WooCommerce" > "Order Completed"]
[Selectionne la connexion WordPress]
[Clique sur "Fetch Data" > "Save"]

Le trigger est "Order Completed". On ne veut enregistrer que les ventes confirmees, pas les paniers abandonnes.

**[ECRAN — screencast action Google Sheets]**

[Clique sur "+" > selectionne "Google Sheets"]
[Selectionne l'action "Add Row"]
[Selectionne la connexion Google]
[Selectionne le spreadsheet "Dashboard Ventes schoolsWP"]
[Selectionne la feuille "Sheet1"]
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
[Retourne dans Google Sheets pour montrer la ligne ajoutee]
[Clique sur "Save"]

Le mapping est direct. Chaque champ du trigger correspond a une colonne du tableur. Le test confirme que la ligne s'ajoute correctement.

**[ECRAN — screencast Google Sheets — formules et formatage]**

[Dans le Sheet, ajoute une ligne de totaux en bas :]
- Cellule F100 : =SOMME(F2:F99)
- Cellule G1 (nouvel onglet "Resume") : =NB.VAL(A2:A999) pour le nombre de ventes
[Ajoute un filtre sur la colonne Date]
[Ajoute une mise en forme conditionnelle : montant > 100 EUR en vert]

Le tableur recoit les donnees brutes. A toi d'ajouter les formules. Un total des ventes, un compteur de commandes, une mise en forme conditionnelle pour reperer les grosses commandes. Google Sheets fait le reste.

**[ECRAN — slide "Aller plus loin avec le dashboard"]**

- **Onglet "Resume"** : formules SOMME, MOYENNE, NB.SI par mois
- **Graphique integre** : courbe des ventes quotidiennes
- **Partage** : donne un acces lecture a ton associe ou ton comptable
- **Alertes Sheets** : notification email quand une cellule change

Tu n'as pas besoin d'un outil de Business Intelligence. Un Google Sheet bien structure + OttoKit, c'est un dashboard fonctionnel et gratuit.

**[TRANSITION — face camera]**

Ton dashboard de ventes tourne. Dans la prochaine lecon, on passe aux emails transactionnels : envoyer un email personnalise automatiquement apres chaque achat.

---

**Points cles**
- Preparer le tableur avant de configurer le workflow (colonnes = champs)
- Utiliser "Order Completed" (pas "Created") pour ne comptabiliser que les ventes confirmees
- Les formules Google Sheets transforment les donnees brutes en dashboard
- Ce dashboard est gratuit et partageable

**Mots-cles SEO**
- OttoKit Google Sheets dashboard
- tableau de bord ventes WordPress
- automatiser Google Sheets WooCommerce
- dashboard automatique WordPress

---

## Lecon 9.2 — Gmail / SMTP : emails transactionnels automatiques

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

WooCommerce envoie deja des emails de confirmation. Mais ils sont generiques et souvent moches. Avec OttoKit + Gmail, tu peux envoyer des emails personnalises, au bon moment, avec le ton de ta marque.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Email personnalise post-achat"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Meme trigger que la lecon precedente. La difference, c'est l'action.

**[ECRAN — screencast connexion Gmail]**

[Clique sur "+" > selectionne "Gmail"]
[Si c'est la premiere connexion Gmail, montre le flux OAuth :]
[Clique sur "Connect Gmail"]
[Selectionne le compte Google]
[Accepte les permissions : envoyer des emails en ton nom]
[Retourne dans OttoKit — connexion confirmee]

La connexion Gmail se fait une seule fois. Tu autorises OttoKit a envoyer des emails depuis ton adresse. C'est un OAuth standard — tes identifiants ne sont pas stockes par OttoKit.

**[ECRAN — screencast configuration de l'email]**

[Selectionne l'action "Send Email"]
[Configure :]
- From Name : schoolsWP
- To : {{billing_email}}
- Subject : {{billing_first_name}}, ta commande #{{order_id}} est confirmee
- Body :

```
Bonjour {{billing_first_name}},

Ta commande #{{order_id}} de {{total}} EUR est confirmee. Voici le recap :

Produit : {{line_items_name}}
Montant : {{total}} EUR
Date : {{date_completed}}

Prochaine etape : tu recevras un email de suivi avec les informations d'acces.

Des questions ? Reponds directement a cet email.

Merci de ta confiance,
Michael — schoolsWP
```

[Montre le selecteur de donnees dynamiques pour chaque champ variable]
[Clique sur "Test Action"]
[Ouvre Gmail pour montrer l'email recu]

Chaque variable entre doubles accolades est remplacee par la donnee reelle. Le prenom, le numero de commande, le montant, le produit — tout est dynamique. L'email est signe par une personne, pas par "noreply@".

**[ECRAN — slide "Gmail vs SMTP : lequel choisir ?"]**

| | Gmail | SMTP |
|---|---|---|
| Configuration | OAuth (2 clics) | Serveur, port, identifiants |
| Limite d'envoi | 500/jour (gratuit) | Depend du fournisseur |
| Delivrabilite | Bonne (Google) | Depend de la configuration |
| Cas d'usage | < 500 emails/jour | Volume important, domaine custom |
| OttoKit | App native | App "SMTP / Send Email" |

Si tu envoies moins de 500 emails par jour, Gmail suffit. Au-dela, configure un SMTP dedie (Brevo, Amazon SES, Mailgun). OttoKit supporte les deux.

**[ECRAN — slide "Bonnes pratiques emails transactionnels"]**

- Personnalise l'objet avec le prenom — les taux d'ouverture augmentent de 20%
- Signe avec ton vrai prenom, pas "L'equipe" — ca humanise
- Ajoute un call-to-action clair (lien vers le cours, lien vers le compte)
- N'envoie pas plus de 2 emails lies a la meme commande dans les 24h

**[TRANSITION — face camera]**

Les emails partent automatiquement. Prochaine lecon : on notifie l'equipe en temps reel avec Slack a chaque grosse vente.

---

**Points cles**
- La connexion Gmail OAuth se fait une seule fois
- Les variables dynamiques personnalisent chaque email automatiquement
- Limite Gmail : 500 emails/jour (au-dela, utiliser un SMTP)
- Signer avec un vrai prenom ameliore l'engagement

**Mots-cles SEO**
- OttoKit Gmail email automatique
- email transactionnel WordPress
- automatiser email post-achat
- OttoKit SMTP configuration

---

## Lecon 9.3 — Slack : notifications equipe en temps reel

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Slack

---

**[INTRO — face camera]**

Tu veux que toute l'equipe voie passer les ventes en temps reel. Pas dans un email qu'on oublie de lire — dans un channel Slack dedie. Et seulement les ventes au-dessus de 100 EUR, pour ne pas noyer le channel.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Vente > 100 EUR → notification Slack"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Le trigger est le meme. La difference, c'est le filtre et la destination.

**[ECRAN — screencast ajout du Filter]**

[Clique sur "+" > selectionne "Filter"]
[Configure : "total" is greater than "100"]
[Clique sur "Save"]

Le filtre laisse passer uniquement les commandes de plus de 100 EUR. Les petites commandes ne declenchent pas de notification. Ca evite le bruit.

**[ECRAN — screencast connexion Slack]**

[Clique sur "+" > selectionne "Slack"]
[Si c'est la premiere connexion, montre le flux OAuth :]
[Clique sur "Connect Slack"]
[Selectionne le workspace Slack]
[Autorise OttoKit a publier des messages]
[Retourne dans OttoKit — connexion confirmee]

Comme pour Gmail, la connexion Slack se fait une seule fois via OAuth.

**[ECRAN — screencast configuration du message]**

[Selectionne l'action "Send Channel Message"]
[Selectionne le channel : #ventes]
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

Le message Slack supporte le formatage Markdown et les emojis. Ici, l'emoji moneybag attire l'oeil. Les informations essentielles sont la : montant, client, produit, numero de commande.

**[ECRAN — slide "Autres notifications Slack utiles"]**

- **Inscription formation** : ":mortar_board: Nouvel eleve : {{student_name}} dans {{course_title}}"
- **Formulaire contact** : ":email: Nouveau lead : {{name}} — {{email}}"
- **Erreur workflow** : ":warning: Le workflow {{workflow_name}} a echoue"
- **Objectif atteint** : ":trophy: 100 ventes ce mois — bravo l'equipe !"

Slack, c'est ton centre de notifications internes. Tu choisis ce qui merite d'apparaitre et dans quel channel.

**[ECRAN — slide "Mentions et DM"]**

Tu peux aussi :
- Mentionner quelqu'un : `<@USER_ID>` dans le message pour notifier une personne specifique
- Envoyer un message prive (DM) au lieu d'un channel
- Poster dans plusieurs channels avec plusieurs actions

**[TRANSITION — face camera]**

L'equipe est notifiee en temps reel. Prochaine lecon : on passe a Stripe et la gestion automatisee des paiements et abonnements.

---

**Points cles**
- Le filtre > 100 EUR evite de noyer le channel avec les petites commandes
- La connexion Slack OAuth se fait une seule fois
- Le formatage Markdown et les emojis rendent les messages lisibles
- Slack est ideal pour les notifications internes (pas pour les clients)

**Mots-cles SEO**
- OttoKit Slack notification
- notification vente Slack WordPress
- automatiser notification equipe
- OttoKit Slack integration

---

## Lecon 9.4 — Stripe : paiement → actions automatiques

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Stripe dashboard

---

**[INTRO — face camera]**

Stripe gere tes paiements. Mais un paiement reussi, c'est le debut d'un processus, pas la fin. Ouvrir l'acces a un cours, envoyer une facture, mettre a jour le CRM, notifier l'equipe. OttoKit automatise toute la chaine post-paiement.

**[ECRAN — screencast connexion Stripe dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection"]
[Selectionne "Stripe"]
[Montre le flux de connexion : API Key ou OAuth]
[Colle la Restricted API Key Stripe (pas la Secret Key)]
[Montre le badge "Connected"]

Pour connecter Stripe, tu utilises une API Key restreinte. Pas la cle secrete complete — une cle avec uniquement les permissions necessaires. C'est une bonne pratique de securite.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Paiement Stripe → acces + CRM + notification"]
[Clique sur le bloc trigger]
[Selectionne "Stripe"]
[Selectionne l'evenement "Payment Succeeded" ou "Checkout Session Completed"]
[Selectionne la connexion Stripe]
[Clique sur "Fetch Data"]
[Montre les champs : customer_email, customer_name, amount, currency, product_name, subscription_id]
[Clique sur "Save"]

Le trigger "Payment Succeeded" se declenche quand un paiement Stripe est confirme. Les champs disponibles : email du client, nom, montant, devise, produit, identifiant d'abonnement.

**[ECRAN — screencast action 1 — FluentCRM tag "client"]**

[Clique sur "+" > selectionne "FluentCRM"]
[Selectionne "Add Tag to Contact"]
[Configure :]
- Email : {{customer_email}}
- Tag : "client"
- Create if not exists : oui

[Clique sur "Save"]

Premiere action : le contact passe de "prospect" a "client" dans FluentCRM. Le tag "client" est pose. Ca peut declencher un autre workflow — par exemple, arreter la sequence de nurturing.

**[ECRAN — screencast action 2 — Inscription TutorLMS]**

[Clique sur "+" > selectionne "TutorLMS"]
[Selectionne "Enroll Student in Course"]
[Configure :]
- Student Email : {{customer_email}}
- Course : Formation Premium schoolsWP

[Clique sur "Save"]

Deuxieme action : ouvrir l'acces au cours. L'eleve est automatiquement inscrit a la formation premium dans TutorLMS. Pas d'intervention manuelle, pas de delai.

**[ECRAN — screencast action 3 — Email de bienvenue premium]**

[Clique sur "+" > selectionne "Send Email"]
[Configure :]
- To : {{customer_email}}
- Subject : Bienvenue dans la formation premium !
- Body :

```
Bonjour {{customer_name}},

Ton paiement de {{amount}} {{currency}} est confirme. Ton acces a la formation premium est actif.

Connecte-toi ici pour commencer : [lien]

Premier conseil : commence par le Module 4 — c'est la que la magie commence.

Des questions ? Reponds a cet email.

Michael — schoolsWP
```

[Clique sur "Save"]

**[ECRAN — screencast vue globale]**

[Montre le workflow complet : Trigger Stripe → FluentCRM tag → TutorLMS inscription → Email]
[Active le workflow]

Le cycle complet : paiement confirme → tag CRM "client" → inscription au cours → email de bienvenue. Quatre etapes, zero intervention.

**[ECRAN — slide "Gerer les abonnements Stripe"]**

Pour les abonnements mensuels ou annuels :

| Evenement Stripe | Action OttoKit |
|-----------------|----------------|
| Subscription Created | Inscrire au cours + tag "abonne" |
| Subscription Renewed | Mettre a jour la date d'expiration |
| Subscription Cancelled | Retirer le tag "abonne" + email de rétention |
| Payment Failed | Email "mettre a jour ta carte" |

Chaque evenement Stripe peut declencher un workflow different. Tu geres tout le cycle de vie de l'abonnement.

**[TRANSITION — face camera]**

Stripe est connecte. Prochaine lecon : WhatsApp Cloud API — envoyer des messages automatiques a tes clients sur leur telephone.

---

**Points cles**
- Utiliser une API Key restreinte Stripe (pas la cle secrete)
- Le trigger "Payment Succeeded" couvre les paiements uniques et les abonnements
- Chaque evenement Stripe (creation, renouvellement, annulation) peut declencher un workflow
- Le workflow combine CRM + LMS + email en une seule chaine

**Mots-cles SEO**
- OttoKit Stripe integration
- automatiser paiement Stripe WordPress
- Stripe WooCommerce OttoKit
- gestion abonnement automatique WordPress

---

## Lecon 9.5 — WhatsApp Cloud API : messages automatiques

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Meta Business Suite

---

**[INTRO — face camera]**

Tes clients lisent leurs emails... parfois. Mais leurs messages WhatsApp ? Quasiment toujours. Envoyer une confirmation de commande ou un rappel de formation par WhatsApp, ca change le taux de lecture. OttoKit le permet via la WhatsApp Cloud API.

**[ECRAN — slide "Prerequis WhatsApp Cloud API"]**

Avant de commencer, tu as besoin de :

1. **Un compte Meta Business verifie** — pas un compte perso, un compte business
2. **Une app dans Meta for Developers** — c'est gratuit
3. **Un numero de telephone dedie** — pas ton numero perso
4. **Des templates de messages pre-approuves** — obligatoire pour les messages sortants

C'est la partie la plus complexe de ce module. Une fois la configuration faite, l'envoi est automatique.

**[ECRAN — screencast Meta Business Suite]**

[Ouvre developers.facebook.com]
[Montre l'app Meta existante (ou le bouton "Create App")]
[Va dans WhatsApp > Getting Started]
[Montre le numero de telephone de test et le token d'acces temporaire]

Meta fournit un numero de test et un token temporaire pour tes premiers essais. En production, tu utiliseras ton propre numero et un token permanent.

**[ECRAN — screencast templates WhatsApp]**

[Va dans WhatsApp > Message Templates]
[Montre un template existant ou cree-en un :]
- Nom : confirmation_commande
- Langue : Francais
- Categorie : Transactional
- Corps :

```
Bonjour {{1}},

Ta commande #{{2}} de {{3}} EUR est confirmee.
Tu recevras un email de suivi sous 24h.

Merci — schoolsWP
```

[Soumets le template pour approbation]

Les templates doivent etre approuves par Meta avant utilisation. C'est une contrainte obligatoire. Les variables {{1}}, {{2}}, {{3}} seront remplies par OttoKit.

**[ECRAN — screencast connexion WhatsApp dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection" > "WhatsApp Cloud API"]
[Renseigne le Phone Number ID et le Access Token]
[Montre le badge "Connected"]

La connexion necessite deux informations : l'identifiant de ton numero de telephone et le token d'acces. Les deux se trouvent dans ton dashboard Meta for Developers.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Commande → confirmation WhatsApp"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]
[Clique sur "+" > selectionne "WhatsApp Cloud API"]
[Selectionne l'action "Send Template Message"]
[Configure :]
- To : {{billing_phone}}
- Template : confirmation_commande
- Variable 1 : {{billing_first_name}}
- Variable 2 : {{order_id}}
- Variable 3 : {{total}}

[Clique sur "Test Action"]
[Montre le message recu sur WhatsApp (screenshot ou telephone)]
[Clique sur "Save"]

Le workflow mappe les variables du template avec les donnees de la commande. Le prenom, le numero de commande, le montant — tout est injecte automatiquement.

**[ECRAN — slide "Points d'attention WhatsApp"]**

- **Format du numero** : international avec indicatif (+33 pour la France) — pas de 06
- **Fenetre de 24h** : tu peux envoyer un message libre uniquement si le client t'a ecrit dans les 24h. Sinon, utilise un template approuve
- **Cout** : WhatsApp Cloud API facture par conversation (environ 0.05 EUR par conversation en France)
- **RGPD** : le client doit avoir donne son consentement pour recevoir des messages WhatsApp

**[TRANSITION — face camera]**

WhatsApp est branche. Prochaine lecon : on automatise la creation d'evenements Google Calendar apres une inscription.

---

**Points cles**
- WhatsApp Cloud API necessite un compte Meta Business verifie
- Les templates de messages doivent etre approuves par Meta
- Le numero de telephone doit etre au format international
- Cout approximatif : 0.05 EUR par conversation en France

**Mots-cles SEO**
- OttoKit WhatsApp Cloud API
- message WhatsApp automatique WordPress
- WhatsApp Business WordPress automatisation
- envoyer WhatsApp OttoKit

---

## Lecon 9.6 — Google Calendar : evenements automatiques

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Google Calendar

---

**[INTRO — face camera]**

Un eleve s'inscrit a ta formation. Tu veux lui envoyer une invitation calendrier pour la session de bienvenue du lundi suivant. Manuellement, ca prend 2 minutes par eleve. Avec 50 inscriptions par semaine, ca fait presque 2 heures. OttoKit le fait en zero seconde.

**[ECRAN — screencast connexion Google Calendar]**

[Ouvre OttoKit > Connections]
[Si Google est deja connecte, montre que Calendar est inclus dans la meme connexion OAuth]
[Sinon, montre le flux OAuth Google avec la permission "Gerer les agendas"]

Si tu as deja connecte Google Sheets ou Gmail, la connexion Google Calendar peut utiliser la meme autorisation. Verifie que la permission "Gerer les agendas" est incluse.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Inscription → invitation calendrier"]
[Trigger : TutorLMS > Student Enrolled in Course]
[Connexion WordPress > Fetch Data > Save]

Le trigger est l'inscription TutorLMS. On pourrait aussi utiliser un trigger Stripe (paiement) ou Fluent Forms (soumission formulaire).

**[ECRAN — screencast action Google Calendar]**

[Clique sur "+" > selectionne "Google Calendar"]
[Selectionne l'action "Create Event"]
[Configure :]
- Calendar : schoolsWP — Sessions de bienvenue
- Title : Session de bienvenue — {{course_title}}
- Start : [prochain lundi 10:00]
- End : [prochain lundi 10:30]
- Description :

```
Bienvenue dans "{{course_title}}" !

Cette session de 30 minutes te presente :
- Le plan du cours
- Comment poser tes questions
- Les ressources disponibles

Lien visio : [lien Google Meet]
```

- Attendees : {{student_email}}
- Send Notifications : Yes

[Clique sur "Test Action"]
[Ouvre Google Calendar pour montrer l'evenement cree]
[Clique sur "Save"]

L'evenement est cree dans ton agenda et l'invitation est envoyee a l'eleve. Il recoit un email avec le bouton "Ajouter a mon agenda". Le lien visio, la description, l'horaire — tout est pre-rempli.

**[ECRAN — slide "Cas d'usage Google Calendar + OttoKit"]**

- **Session de bienvenue** : invitation automatique apres inscription
- **Rappel de webinar** : creer l'evenement quand le participant s'inscrit
- **RDV client** : apres un achat premium, bloquer un creneau coaching
- **Deadline interne** : quand un contenu est valide, creer un rappel "publication J+3"
- **Suivi formateur** : creer un evenement "relance eleve" 7 jours apres inscription si inactif

**[TRANSITION — face camera]**

L'agenda se remplit automatiquement. Derniere lecon avant le quiz : on automatise la gestion de projet avec Trello, ClickUp ou Asana.

---

**Points cles**
- Google Calendar utilise la meme connexion OAuth que Sheets et Gmail
- L'action "Create Event" envoie automatiquement l'invitation par email
- Le champ "Attendees" ajoute l'eleve comme participant
- Utile pour les sessions de bienvenue, webinars, coaching, rappels

**Mots-cles SEO**
- OttoKit Google Calendar automatisation
- creer evenement automatique WordPress
- invitation calendrier automatique
- Google Calendar OttoKit integration

---

## Lecon 9.7 — Trello / ClickUp / Asana : gestion de projet automatisee

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + Trello

---

**[INTRO — face camera]**

Tu utilises Trello, ClickUp ou Asana pour gerer tes projets. A chaque nouveau client, tu crees manuellement une carte ou une tache. Avec OttoKit, cette tache se cree automatiquement — avec toutes les informations du client deja remplies.

**[ECRAN — screencast connexion Trello dans OttoKit]**

[Ouvre OttoKit > Connections]
[Clique sur "New Connection" > "Trello"]
[Montre le flux OAuth Trello]
[Autorise OttoKit a acceder au workspace Trello]
[Montre le badge "Connected"]

La connexion Trello suit le meme schema OAuth que Google ou Slack. Une seule autorisation, puis c'est automatique.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Nouveau client → tache Trello"]
[Trigger : WooCommerce > Order Completed]
[Connexion WordPress > Fetch Data > Save]

Le trigger est une commande completee. Chaque nouvelle vente cree une tache dans ton outil de gestion de projet.

**[ECRAN — screencast action Trello]**

[Clique sur "+" > selectionne "Trello"]
[Selectionne l'action "Create Card"]
[Configure :]
- Board : schoolsWP — Operations
- List : "Nouveaux clients"
- Name : Client : {{billing_first_name}} {{billing_last_name}} — #{{order_id}}
- Description :

```
Nouveau client depuis WooCommerce

Email : {{billing_email}}
Produit : {{line_items_name}}
Montant : {{total}} EUR
Date : {{date_completed}}

Taches :
- [ ] Verifier l'acces au cours
- [ ] Envoyer le kit de bienvenue
- [ ] Planifier la session onboarding
```

- Due Date : [+3 jours]
- Labels : "Onboarding"
- Members : [Assigner a un membre de l'equipe]

[Clique sur "Test Action"]
[Ouvre Trello pour montrer la carte creee dans la colonne "Nouveaux clients"]
[Clique sur "Save"]

La carte Trello contient tout : les informations du client, la liste des taches a faire, une date limite, une etiquette et un responsable. L'equipe sait exactement quoi faire sans chercher les infos.

**[ECRAN — slide "ClickUp et Asana : meme logique"]**

| Trello | ClickUp | Asana |
|--------|---------|-------|
| Create Card | Create Task | Create Task |
| Board / List | Space / List | Project / Section |
| Labels | Tags | Tags |
| Due Date | Due Date | Due Date |
| Members | Assignees | Assignees |

La logique est identique pour ClickUp et Asana. Seuls les noms changent. Tu choisis ton outil de gestion de projet, OttoKit s'adapte.

**[ECRAN — slide "Autres automatisations gestion de projet"]**

- **Nouveau lead → carte "A contacter"** dans la colonne prospection
- **Script valide → tache "Produire video module X"** assignee au monteur
- **Ticket support → carte avec priorite et date limite**
- **Fin de formation → deplacer la carte dans "Termine"**
- **Rappel interne → creer une tache quand un workflow echoue**

L'automatisation de la gestion de projet, c'est ce qui transforme un outil passif en systeme actif. Les taches se creent sans que personne ait besoin d'y penser.

**[ECRAN — screencast vue globale]**

[Montre le workflow complet : Trigger WooCommerce → Create Card Trello]
[Active le workflow]

**[TRANSITION — face camera]**

Ce module est termine. Tu sais maintenant connecter les principales apps SaaS a OttoKit : Google Sheets pour le reporting, Gmail pour les emails, Slack pour les notifications equipe, Stripe pour les paiements, WhatsApp pour les messages clients, Google Calendar pour les invitations, et Trello pour la gestion de projet. Passe au quiz pour valider tes acquis avant d'attaquer les webhooks et l'API dans le Module 10.

---

**Points cles**
- Trello, ClickUp et Asana fonctionnent de la meme maniere avec OttoKit
- La carte/tache inclut les donnees du trigger (client, produit, montant)
- Les checklists et dates limites structurent le suivi
- L'automatisation transforme un outil de gestion passive en systeme proactif

**Mots-cles SEO**
- OttoKit Trello integration
- automatiser gestion projet WordPress
- creer tache automatique Trello ClickUp
- OttoKit gestion de projet automatisee

---

## Notes de production — Module 9

### Captures a preparer
- Google Sheets : spreadsheet "Dashboard Ventes schoolsWP" avec colonnes et lignes ajoutees
- Google Sheets : formules SOMME, graphique integre, mise en forme conditionnelle
- Gmail : email personnalise recu avec donnees dynamiques
- Slack : message de notification dans le channel #ventes
- Stripe Dashboard : API Keys > Restricted Key
- OttoKit : connexion Stripe avec badge "Connected"
- Meta for Developers : WhatsApp > Getting Started (numero test, token)
- Meta : WhatsApp Message Templates — template "confirmation_commande"
- WhatsApp : message recu sur telephone (screenshot)
- Google Calendar : evenement cree avec invitation et lien visio
- Trello : carte creee dans la colonne "Nouveaux clients" avec description et checklist
- Canvas OttoKit : chaque workflow complet (7 workflows au total)

### Environnement de demo
- Compte OttoKit avec plan actif
- Site WordPress schoolsWP avec WooCommerce + TutorLMS + FluentCRM
- Google Workspace : Sheets, Gmail, Calendar connectes
- Workspace Slack avec channel #ventes
- Compte Stripe avec Restricted API Key (mode test)
- Compte Meta Business verifie avec app WhatsApp Cloud API configuree
- Numero WhatsApp de test + template approuve
- Board Trello "schoolsWP — Operations" avec colonne "Nouveaux clients"
- Telephone pour screenshot WhatsApp

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 9.1 | 7 min |
| 9.2 | 6 min |
| 9.3 | 5 min |
| 9.4 | 7 min |
| 9.5 | 7 min |
| 9.6 | 5 min |
| 9.7 | 6 min |
| **Total M9** | **43 min** |

# Scripts video — Module 13 : Webhooks et connexions externes

**Formation** : Maitriser FluentCRM
**Module** : M13 — Webhooks et connexions externes (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~50 min
**Prerequis** : M6 (automations de base), M7 (automation avancee)
**Date** : 2026-03-23

---

### Lecon 13.1 — Comprends les webhooks : incoming vs outgoing

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu utilises FluentCRM pour gerer tes contacts et tes automations. Mais ton business ne vit pas uniquement dans FluentCRM. Tu as des formulaires sur d'autres plateformes, un outil de paiement, peut-etre un CRM externe ou un tableau de bord Google Sheets. Et ces outils ne se parlent pas entre eux — sauf si tu les connectes. Les webhooks sont le pont entre FluentCRM et le reste de ton ecosysteme. Dans cette lecon, tu comprends ce que c'est, comment ca fonctionne, et la difference entre les deux types : incoming et outgoing.

**[ECRAN — slide "Qu'est-ce qu'un webhook ?"]**

[Montre un schema simple : Outil A → fleche → Outil B]

Etape 1 : un webhook, c'est un message HTTP envoye automatiquement d'un outil a un autre quand un evenement se produit. Pas de synchronisation periodique, pas de fichier CSV a exporter. L'evenement arrive, le message part instantanement.

Concretement : un client achete sur WooCommerce → WooCommerce envoie un webhook → FluentCRM recoit le message et ajoute le contact avec le bon tag. Tout ca en temps reel, sans intervention manuelle.

**[ECRAN — slide "Incoming vs Outgoing"]**

[Montre un schema avec deux fleches : une entrante, une sortante, FluentCRM au centre]

Etape 2 : il existe deux types de webhooks dans FluentCRM.

Incoming webhook — FluentCRM recoit des donnees. Un outil externe envoie une requete HTTP vers une URL unique generee par FluentCRM. Cas typique : un formulaire Typeform envoie les soumissions a FluentCRM pour creer un contact.

Outgoing webhook — FluentCRM envoie des donnees. Quand un evenement se produit dans FluentCRM (tag ajoute, automation declenchee), il envoie un payload JSON vers un outil externe. Cas typique : un contact atteint un certain score → FluentCRM envoie ses infos a n8n pour declencher une alerte Telegram.

**[ECRAN — slide "Quand utiliser quoi"]**

[Montre un tableau avec 3 colonnes : Scenario, Type, Exemple]

Etape 3 : voici comment choisir.

Tu veux que des donnees entrent dans FluentCRM depuis un outil externe ? Incoming webhook. Exemples : formulaire externe, plateforme de paiement, outil de scraping.

Tu veux que FluentCRM notifie un outil externe quand quelque chose se passe ? Outgoing webhook. Exemples : alerte Telegram, mise a jour Google Sheets, creation de tache dans un outil de gestion.

Tu veux les deux ? Combine les deux. C'est ce qu'on fait avec n8n dans les lecons suivantes.

**[ECRAN — slide "Anatomie d'un webhook"]**

[Montre un exemple de payload JSON simplifie]

Etape 4 : techniquement, un webhook c'est une requete HTTP POST qui transporte un payload JSON. Voici a quoi ca ressemble :

```json
{
  "email": "jean@example.com",
  "first_name": "Jean",
  "tags": ["acheteur", "cours-lms"],
  "event": "purchase_completed"
}
```

Tu n'as pas besoin de coder pour utiliser les webhooks — FluentCRM et les outils comme n8n gerent la partie technique. Mais comprendre cette structure t'aide a debugger quand quelque chose ne fonctionne pas.

**[TRANSITION — face camera]**

Tu sais maintenant ce qu'est un webhook et quand utiliser incoming ou outgoing. Ce sont les deux mecanismes qui permettent a FluentCRM de communiquer avec n'importe quel outil externe. Dans la prochaine lecon, tu configures ton premier incoming webhook — pour recevoir des donnees dans FluentCRM depuis l'exterieur.

---

**Points cles** :
- Webhook = message HTTP automatique envoye quand un evenement se produit
- Incoming webhook : FluentCRM recoit des donnees depuis un outil externe
- Outgoing webhook : FluentCRM envoie des donnees vers un outil externe
- Le payload est au format JSON — structure cle-valeur
- Pas besoin de coder — les outils gerent la partie technique

**Mots cles SEO** : FluentCRM webhook, incoming webhook FluentCRM, outgoing webhook FluentCRM, connecter FluentCRM outils externes, webhook WordPress CRM

---

### Lecon 13.2 — Configure un incoming webhook (recois des donnees externes)

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Un formulaire Typeform, une page de paiement Stripe, un outil de scraping — tous ces outils peuvent envoyer des donnees a FluentCRM. La condition : que FluentCRM expose une URL capable de recevoir ces donnees. C'est exactement ce que fait l'incoming webhook. Dans cette lecon, tu en configures un de A a Z, avec le mapping des champs et la securisation par secret key.

**[ECRAN — screencast FluentCRM > Settings > Incoming Webhooks]**

[Navigation vers FluentCRM > Settings > Incoming Webhooks]

Etape 1 : va dans FluentCRM, puis Settings, puis cherche la section "Incoming Webhooks" ou "REST API". Selon ta version de FluentCRM, l'emplacement exact peut varier. Tu cherches l'option qui te permet de creer une URL de reception de donnees.

[Montre le bouton "Create Webhook" ou equivalent]

Etape 2 : cree un nouveau webhook. Donne-lui un nom descriptif — par exemple "Typeform - Inscription Newsletter" ou "Stripe - Achat Cours LMS". Ce nom est interne, il te sert a identifier quel outil envoie des donnees vers ce point d'entree.

**[ECRAN — screencast URL du webhook]**

[Montre l'URL generee par FluentCRM]

Etape 3 : FluentCRM genere une URL unique. Elle ressemble a ca :

```
https://tonsite.com/?fluentcrm=1&route=contact&hash=abc123xyz
```

Cette URL est le point d'entree. Tout outil qui envoie une requete POST vers cette URL peut creer ou mettre a jour un contact dans FluentCRM. Note cette URL — tu la colles dans l'outil externe a l'etape suivante.

**[ECRAN — screencast mapping des champs]**

[Montre l'interface de mapping]

Etape 4 : configure le mapping des champs. FluentCRM doit savoir a quoi correspond chaque donnee recue. Le champ "email" de l'outil externe correspond au champ "Email" de FluentCRM. Le champ "name" correspond a "First Name". Si l'outil externe envoie des champs personnalises, tu les mappes vers des custom fields FluentCRM.

[Montre le mapping email → Email, name → First Name, phone → Phone]

Les champs standards sont mappes automatiquement si les noms correspondent. Pour les champs non standards, tu fais le mapping manuellement.

**[ECRAN — screencast configuration liste et tags]**

[Montre les options d'assignation automatique]

Etape 5 : configure les actions automatiques. A chaque donnee recue, FluentCRM peut automatiquement assigner le contact a une liste et lui poser des tags. Par exemple : liste "Leads Typeform", tag "source-typeform". Ca te permet de segmenter immediatement les contacts selon leur source d'acquisition.

[Configure la liste et les tags]

**[ECRAN — screencast secret key]**

[Montre le champ "Secret Key" ou "Authentication"]

Etape 6 : securise le webhook avec une secret key. Sans cette cle, n'importe qui connaissant ton URL pourrait injecter des contacts dans ta base. La secret key est un parametre supplementaire que l'outil externe doit inclure dans sa requete. Si la cle ne correspond pas, FluentCRM rejette la donnee.

[Montre ou copier la secret key]

Copie cette cle et ajoute-la dans la configuration du webhook cote outil externe. La plupart des outils (Typeform, Zapier, n8n) ont un champ dedie pour ca.

**[ECRAN — screencast test du webhook]**

[Montre un test avec un outil comme Postman ou le test integre]

Etape 7 : teste le webhook avant de le mettre en production. Envoie une requete de test avec des donnees fictives. Verifie que le contact apparait dans FluentCRM avec les bons champs, la bonne liste et les bons tags.

[Montre le contact cree dans FluentCRM apres le test]

Si le contact n'apparait pas, verifie trois choses : l'URL est correcte, la secret key est incluse, et le format JSON est valide.

**[TRANSITION — face camera]**

Ton incoming webhook est en place. FluentCRM peut maintenant recevoir des donnees depuis n'importe quel outil externe. Dans la prochaine lecon, on fait l'inverse : configurer un outgoing webhook pour que FluentCRM envoie des donnees vers l'exterieur.

---

**Points cles** :
- Incoming webhook = URL unique generee par FluentCRM pour recevoir des donnees externes
- Mapping des champs : associer les champs de l'outil externe aux champs FluentCRM
- Actions automatiques : assigner liste et tags a chaque contact recu
- Secret key : securiser le webhook pour empecher les injections non autorisees
- Toujours tester avec des donnees fictives avant la mise en production

**Mots cles SEO** : FluentCRM incoming webhook, recevoir donnees FluentCRM, webhook FluentCRM configuration, connecter Typeform FluentCRM, FluentCRM REST API

---

### Lecon 13.3 — Configure un outgoing webhook (envoie des donnees)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

FluentCRM sait maintenant recevoir des donnees. L'autre direction est tout aussi importante : envoyer des donnees vers l'exterieur quand un evenement se produit. Un contact atteint un score de 50 points → tu veux une alerte. Un tag "acheteur" est pose → tu veux mettre a jour un Google Sheet. C'est le role de l'outgoing webhook — et il se configure directement dans le builder d'automation.

**[ECRAN — screencast FluentCRM > Automations > Nouveau]**

[Cree une nouvelle automation]

Etape 1 : l'outgoing webhook n'est pas un reglage global — c'est une action dans une automation. Va dans Automations, cree une nouvelle automation. Choisis un trigger adapte a ton cas. Par exemple : "Tag Applied" — quand le tag "lead-qualifie" est pose sur un contact.

[Montre la selection du trigger "Tag Applied"]

**[ECRAN — screencast ajout de l'action webhook]**

[Ajoute une action dans le builder]

Etape 2 : dans le builder, ajoute une action. Cherche "Outgoing Webhook" ou "Send HTTP Request" dans la liste des actions disponibles. C'est cette action qui envoie des donnees vers un outil externe.

[Montre l'action "Outgoing Webhook" dans la liste]

Etape 3 : configure l'URL de destination. C'est l'URL de l'outil qui va recevoir les donnees — par exemple l'URL d'un webhook n8n, un endpoint Zapier, ou une URL Google Apps Script. Colle l'URL dans le champ prevu.

[Montre le champ URL et colle une URL n8n en exemple]

**[ECRAN — screencast configuration du payload]**

[Montre les options de payload]

Etape 4 : configure le payload — les donnees que FluentCRM envoie. Par defaut, FluentCRM envoie toutes les informations du contact : email, nom, tags, listes, custom fields, score. Tu peux personnaliser ce payload si tu veux envoyer uniquement certains champs.

[Montre le payload par defaut avec les champs du contact]

Voici un exemple de payload envoye par FluentCRM :

```json
{
  "contact": {
    "email": "jean@example.com",
    "first_name": "Jean",
    "last_name": "Dupont",
    "tags": ["lead-qualifie", "pilier-lms"],
    "lists": ["prospects"],
    "score": 52
  },
  "event": "tag_applied",
  "tag": "lead-qualifie"
}
```

L'outil de destination recoit exactement ces donnees et peut agir en consequence.

**[ECRAN — screencast headers et authentification]**

[Montre les options avancees]

Etape 5 : si l'outil de destination exige une authentification, ajoute les headers necessaires. Le plus courant : un header "Authorization" avec un token Bearer, ou un header personnalise avec une API key. Pour n8n en mode webhook basique, aucune authentification n'est necessaire — l'URL suffit.

[Montre l'ajout d'un header Authorization]

**[ECRAN — screencast test de l'automation]**

[Active l'automation et teste avec un contact]

Etape 6 : teste l'automation. Prends un contact de test, ajoute-lui le tag declencheur. L'automation doit se declencher, l'outgoing webhook doit envoyer la requete, et l'outil de destination doit recevoir les donnees.

[Montre le log de l'automation avec le webhook envoye]

Verifie dans le log de l'automation que l'action webhook a un statut "Success". Si tu vois "Failed", verifie l'URL de destination et les eventuels headers d'authentification.

**[TRANSITION — face camera]**

L'outgoing webhook est ton outil pour pousser des donnees depuis FluentCRM vers n'importe quelle destination. Combine-le avec les triggers d'automation et tu peux notifier, synchroniser, alerter en temps reel. Dans la prochaine lecon, on connecte FluentCRM a Zapier via ces memes webhooks.

---

**Points cles** :
- Outgoing webhook = action dans une automation qui envoie des donnees vers un outil externe
- Se configure dans le builder d'automation, pas dans les reglages globaux
- Le payload contient par defaut toutes les infos du contact (email, nom, tags, score)
- Headers pour l'authentification si l'outil de destination l'exige
- Toujours verifier le statut "Success" dans les logs d'automation

**Mots cles SEO** : FluentCRM outgoing webhook, envoyer donnees FluentCRM, webhook automation FluentCRM, FluentCRM HTTP request, FluentCRM notification externe

---

### Lecon 13.4 — Connecte FluentCRM a Zapier

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + Zapier

---

**[INTRO — face camera]**

Zapier est l'outil d'automatisation le plus connu. Si tu l'utilises deja, tu veux probablement le connecter a FluentCRM. Mauvaise nouvelle : il n'existe pas de connecteur natif FluentCRM dans Zapier. Bonne nouvelle : les webhooks que tu viens de configurer font exactement le meme travail. Dans cette lecon, tu connectes FluentCRM a Zapier dans les deux sens.

**[ECRAN — slide "FluentCRM + Zapier : 2 directions"]**

[Montre un schema : FluentCRM ↔ Zapier avec les deux fleches]

Etape 1 : la connexion fonctionne dans les deux sens.

Zapier vers FluentCRM : Zapier envoie des donnees vers l'incoming webhook de FluentCRM. Cas d'usage : un nouveau lead Calendly → Zapier → FluentCRM.

FluentCRM vers Zapier : l'outgoing webhook de FluentCRM envoie des donnees vers un Zap. Cas d'usage : tag "client" pose → FluentCRM → Zapier → ajout dans un Google Sheet.

**[ECRAN — screencast Zapier > Create Zap > Trigger Webhook]**

[Cree un nouveau Zap avec le trigger "Webhooks by Zapier"]

Etape 2 : commencons par FluentCRM vers Zapier. Dans Zapier, cree un nouveau Zap. Comme trigger, choisis "Webhooks by Zapier" puis "Catch Hook". Zapier genere une URL unique.

[Montre l'URL generee par Zapier]

Copie cette URL. Tu vas la coller dans FluentCRM.

**[ECRAN — screencast FluentCRM > Automation > Outgoing Webhook]**

[Ouvre l'automation avec l'outgoing webhook]

Etape 3 : dans FluentCRM, ouvre l'automation qui doit envoyer des donnees a Zapier. Ajoute une action "Outgoing Webhook" et colle l'URL Zapier comme destination. Le payload par defaut de FluentCRM suffit — Zapier recevra toutes les infos du contact.

[Colle l'URL Zapier dans le champ destination]

**[ECRAN — screencast Zapier > Test Trigger]**

[Teste le trigger dans Zapier]

Etape 4 : retourne dans Zapier et clique sur "Test trigger". Declenche l'automation dans FluentCRM avec un contact de test. Zapier doit capter la requete et afficher les donnees recues. Tu vois l'email, le nom, les tags — tout le payload.

[Montre les donnees recues dans Zapier]

Etape 5 : ajoute l'action de ton choix dans Zapier. Par exemple : "Google Sheets — Create Spreadsheet Row" pour logger chaque nouveau client dans un tableau. Mappe les champs FluentCRM vers les colonnes de ton Sheet.

[Montre le mapping des champs dans l'action Zapier]

**[ECRAN — screencast Zapier vers FluentCRM]**

[Cree un nouveau Zap avec l'action "Webhooks by Zapier > POST"]

Etape 6 : dans l'autre sens — Zapier vers FluentCRM. Cree un Zap avec le trigger de ton choix (nouveau lead Calendly, nouveau paiement Stripe, etc.). Comme action, choisis "Webhooks by Zapier" puis "POST". Colle l'URL de l'incoming webhook FluentCRM que tu as cree dans la lecon 13.2.

[Montre la configuration du POST avec l'URL FluentCRM]

Configure le body en JSON avec les champs attendus par FluentCRM : email, first_name, et les eventuels tags. N'oublie pas d'inclure la secret key si tu en as configure une.

**[ECRAN — screencast test complet]**

[Teste le Zap et verifie dans FluentCRM]

Etape 7 : teste le Zap complet. Declenche l'evenement source, verifie que Zapier envoie la requete, et confirme que le contact apparait dans FluentCRM avec les bons champs et tags.

[Montre le contact cree dans FluentCRM via Zapier]

**[TRANSITION — face camera]**

FluentCRM et Zapier sont connectes. Tu peux envoyer et recevoir des donnees dans les deux sens. C'est une solution qui fonctionne, mais Zapier a une limite : le plan gratuit est vite depasse et chaque Zap supplementaire coute. Dans la prochaine lecon, on voit n8n — l'alternative open source sans limite de workflows.

---

**Points cles** :
- Pas de connecteur natif FluentCRM dans Zapier — les webhooks font le travail
- FluentCRM → Zapier : outgoing webhook vers "Catch Hook" Zapier
- Zapier → FluentCRM : action POST vers l'incoming webhook FluentCRM
- Toujours tester le flux complet avant de mettre en production
- Limite Zapier : plan gratuit restreint, cout par Zap supplementaire

**Mots cles SEO** : FluentCRM Zapier, connecter FluentCRM Zapier, webhook Zapier FluentCRM, automatisation FluentCRM Zapier, FluentCRM integration Zapier

---

### Lecon 13.5 — Connecte FluentCRM a n8n : automatisation sans limites

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + n8n

---

**[INTRO — face camera]**

n8n est l'outil d'automatisation que j'utilise au quotidien pour schoolsWP. Contrairement a Zapier, il est open source, auto-hebergeable, et surtout : pas de limite de workflows. Tu peux creer autant d'automatisations que tu veux sans payer par execution. Et la connexion avec FluentCRM est bidirectionnelle — n8n recoit des donnees via webhook et en envoie via HTTP Request. Dans cette lecon, tu mets en place les deux sens.

**[ECRAN — slide "Architecture FluentCRM + n8n"]**

[Montre un schema : FluentCRM ↔ n8n ↔ (Telegram, Google Sheets, CRM externe, Slack)]

Etape 1 : voici l'architecture cible. FluentCRM est ton hub de contacts et d'automations email. n8n est ton orchestrateur — il recoit les evenements de FluentCRM et declenche des actions dans n'importe quel outil. L'inverse aussi : n8n capte des evenements externes et met a jour FluentCRM. C'est le combo le plus puissant pour un site WordPress.

**[ECRAN — screencast n8n > Nouveau workflow > Webhook node]**

[Cree un nouveau workflow dans n8n]

Etape 2 : dans n8n, cree un nouveau workflow. Ajoute un noeud "Webhook" comme point d'entree. Configure-le en methode POST. n8n genere une URL de production et une URL de test.

[Montre les deux URLs generees]

Copie l'URL de test pour commencer. Tu passeras a l'URL de production une fois que tout fonctionne. L'URL ressemble a :

```
https://ton-n8n.example.com/webhook-test/fluentcrm-events
```

**[ECRAN — screencast FluentCRM > Automation > Outgoing Webhook]**

[Ouvre une automation FluentCRM]

Etape 3 : dans FluentCRM, ouvre ou cree une automation. Ajoute un outgoing webhook avec l'URL n8n comme destination. Par exemple : trigger "Tag Applied" avec le tag "lead-qualifie" → action "Outgoing Webhook" vers n8n.

[Configure l'outgoing webhook avec l'URL n8n]

Etape 4 : dans n8n, clique sur "Listen for test event" sur le noeud Webhook. Puis dans FluentCRM, declenche l'automation avec un contact de test. n8n capte la requete et affiche le payload complet.

[Montre le payload recu dans n8n]

Tu vois toutes les donnees du contact : email, nom, tags, listes, score. A partir de la, tu peux faire ce que tu veux dans n8n.

**[ECRAN — screencast n8n > Ajout de noeuds d'action]**

[Ajoute des noeuds apres le webhook]

Etape 5 : voici trois actions concretes que tu peux enchainer apres le webhook.

Action 1 — Alerte Telegram. Ajoute un noeud "Telegram" configure avec ton bot. A chaque lead qualifie, tu recois un message instantane sur ton telephone avec le nom et l'email du contact.

[Montre le noeud Telegram configure]

Action 2 — Ajout Google Sheets. Ajoute un noeud "Google Sheets" pour logger le contact dans un tableau de reporting. Chaque nouvelle ligne = un lead qualifie.

[Montre le noeud Google Sheets configure]

Action 3 — Lead scoring avance. Ajoute un noeud "Code" pour calculer un score personnalise base sur les tags et l'historique du contact, puis un noeud "HTTP Request" pour renvoyer le score a FluentCRM via son API REST.

[Montre le noeud Code avec le calcul de score]

**[ECRAN — screencast n8n vers FluentCRM via HTTP Request]**

[Cree un nouveau workflow avec un HTTP Request vers FluentCRM]

Etape 6 : dans l'autre sens — n8n vers FluentCRM. Utilise le noeud "HTTP Request" pour appeler l'API REST de FluentCRM ou envoyer des donnees vers l'incoming webhook. Par exemple : un evenement dans Google Calendar → n8n → creation d'un contact dans FluentCRM avec le tag "rdv-pris".

[Montre la configuration du HTTP Request avec l'URL incoming webhook FluentCRM]

Configure la methode POST, le body en JSON avec les champs email, first_name, et les tags. Ajoute la secret key dans les parametres si necessaire.

**[ECRAN — screencast activation du workflow]**

[Active le workflow en production]

Etape 7 : une fois tes tests valides, active le workflow. Passe l'URL du webhook de "test" a "production" dans le noeud Webhook. Mets a jour l'URL dans FluentCRM. Le workflow tourne en continu — chaque evenement FluentCRM declenche la chaine d'actions.

[Montre le toggle "Active" du workflow]

**[TRANSITION — face camera]**

FluentCRM et n8n sont connectes dans les deux sens. Tu as un systeme d'automatisation complet : FluentCRM gere les contacts et les emails, n8n orchestre tout le reste. Alertes, reporting, lead scoring, synchronisation CRM — tout passe par ce duo. Dans la prochaine lecon, on met ca en pratique avec un cas concret : exporter tes contacts vers Google Sheets.

---

**Points cles** :
- n8n = orchestrateur open source, sans limite de workflows
- FluentCRM → n8n : outgoing webhook vers un noeud Webhook n8n
- n8n → FluentCRM : HTTP Request vers l'API REST ou l'incoming webhook
- 3 cas d'usage immediats : alerte Telegram, log Google Sheets, lead scoring avance
- Toujours tester avec l'URL de test avant de passer en production

**Mots cles SEO** : FluentCRM n8n, connecter FluentCRM n8n, automatisation FluentCRM n8n, webhook n8n FluentCRM, FluentCRM open source automation

---

### Lecon 13.6 — Cas d'usage : exporte tes contacts vers Google Sheets

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + n8n + Google Sheets

---

**[INTRO — face camera]**

Tu veux un tableau de bord de tes contacts FluentCRM dans Google Sheets. Pas un export CSV ponctuel — un flux continu. Chaque nouveau contact qualifie atterrit automatiquement dans une ligne de ton Sheet. C'est un cas d'usage classique et concret pour mettre en pratique la connexion FluentCRM → n8n → Google Sheets.

**[ECRAN — screencast Google Sheets > Preparation du tableau]**

[Montre un Google Sheet vide avec les en-tetes]

Etape 1 : prepare ton Google Sheet. Cree un nouveau tableur ou utilise un existant. Ajoute les en-tetes en premiere ligne :

- A1 : Date
- B1 : Email
- C1 : Prenom
- D1 : Nom
- E1 : Tags
- F1 : Score
- G1 : Source

[Montre les en-tetes configurees]

Ce tableau sera alimente automatiquement. Chaque ligne sera un contact envoye par FluentCRM via n8n.

**[ECRAN — screencast n8n > Nouveau workflow]**

[Cree le workflow dans n8n]

Etape 2 : dans n8n, cree un nouveau workflow. Nomme-le "FluentCRM → Google Sheets — Sync Contacts". Ajoute un noeud Webhook en methode POST. Copie l'URL de test.

[Montre le noeud Webhook configure]

**[ECRAN — screencast FluentCRM > Automation]**

[Cree l'automation dans FluentCRM]

Etape 3 : dans FluentCRM, cree une automation. Trigger : "Tag Applied" avec le tag "lead-qualifie" (ou tout autre tag qui marque un contact comme important). Action : "Outgoing Webhook" avec l'URL n8n.

[Montre l'automation configuree]

Teste : ajoute le tag a un contact de test et verifie que n8n recoit les donnees.

**[ECRAN — screencast n8n > Ajout du noeud Google Sheets]**

[Ajoute le noeud Google Sheets dans n8n]

Etape 4 : dans n8n, apres le noeud Webhook, ajoute un noeud "Google Sheets". Configure-le en mode "Append Row". Selectionne ton tableur et l'onglet cible.

[Montre la selection du Sheet et de l'onglet]

Etape 5 : mappe les champs. Voici le mapping :

- Date → `{{ $now.format('yyyy-MM-dd HH:mm') }}`
- Email → `{{ $json.contact.email }}`
- Prenom → `{{ $json.contact.first_name }}`
- Nom → `{{ $json.contact.last_name }}`
- Tags → `{{ $json.contact.tags.join(', ') }}`
- Score → `{{ $json.contact.score }}`
- Source → `"FluentCRM Webhook"`

[Montre le mapping champ par champ]

Les expressions exactes dependent de la structure du payload FluentCRM. Utilise le panneau de test de n8n pour explorer le JSON recu et ajuster les chemins.

**[ECRAN — screencast test complet]**

[Teste le flux de bout en bout]

Etape 6 : teste le flux complet. Dans FluentCRM, pose le tag declencheur sur un contact de test. Verifie dans n8n que le webhook est declenche. Verifie dans Google Sheets qu'une nouvelle ligne apparait avec les bonnes donnees.

[Montre la ligne ajoutee dans Google Sheets]

Etape 7 : active le workflow en production. Remplace l'URL de test par l'URL de production dans le noeud Webhook. Mets a jour l'URL dans FluentCRM. Desormais, chaque contact qualifie atterrit automatiquement dans ton Google Sheet.

[Montre le workflow actif]

**[TRANSITION — face camera]**

Tu as un pipeline de donnees en temps reel : FluentCRM → n8n → Google Sheets. Tu peux l'adapter — ajouter un filtre dans n8n pour ne logger que certains tags, ajouter une colonne calculee dans Sheets, ou dupliquer le workflow pour d'autres types de contacts. Dans la prochaine lecon, tu passes a la pratique avec un exercice guide.

---

**Points cles** :
- Google Sheet avec en-tetes preparees : Date, Email, Prenom, Nom, Tags, Score, Source
- Workflow n8n : Webhook → Google Sheets (Append Row)
- Mapping des champs via les expressions n8n (chemins JSON du payload FluentCRM)
- Tester d'abord en URL de test, puis passer en production
- Le tableau se remplit automatiquement a chaque contact qualifie

**Mots cles SEO** : FluentCRM Google Sheets, exporter contacts FluentCRM, sync FluentCRM Google Sheets, n8n Google Sheets FluentCRM, reporting contacts WordPress

---

### Lecon 13.7 — Exercice : Cree un webhook n8n qui ajoute un contact a l'achat

**Duree** : 7 min
**Type** : Exercice guide
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + n8n

---

**[INTRO — face camera]**

Tu sais configurer des webhooks incoming et outgoing, connecter FluentCRM a n8n, et pousser des donnees vers Google Sheets. Maintenant tu combines tout ca dans un scenario reel : un client achete un produit (via WooCommerce, TutorLMS ou n'importe quel outil de paiement), n8n recoit l'evenement et cree automatiquement un contact dans FluentCRM avec le tag correspondant. C'est l'automatisation de base de tout business en ligne.

**[ECRAN — slide "Scenario de l'exercice"]**

[Montre le schema : Achat → n8n Webhook → FluentCRM (contact + tag)]

Voici le scenario. Un client achete le cours "Maitriser FluentCRM". n8n recoit l'information d'achat via un webhook. n8n cree ou met a jour le contact dans FluentCRM avec le tag "acheteur-fluentcrm" et la liste "clients". Pas d'email, pas de formulaire — tout est automatise.

**[ECRAN — slide "Etapes de l'exercice"]**

[Montre les 5 etapes numerotees]

Tu vas suivre ces 5 etapes :

1. Cree un incoming webhook dans FluentCRM (avec secret key)
2. Cree un workflow n8n avec un noeud Webhook
3. Ajoute un noeud HTTP Request vers l'incoming webhook FluentCRM
4. Configure le payload JSON avec les infos du contact
5. Teste avec un achat simule

**[ECRAN — screencast etape 1 : FluentCRM incoming webhook]**

[Navigation vers FluentCRM > Settings > Incoming Webhooks]

Etape 1 : dans FluentCRM, cree un incoming webhook nomme "n8n — Achat Cours". Configure-le pour assigner automatiquement la liste "clients" et le tag "acheteur". Note l'URL et la secret key.

[Montre la creation et la copie de l'URL + secret key]

**[ECRAN — screencast etape 2 : n8n workflow]**

[Cree le workflow dans n8n]

Etape 2 : dans n8n, cree un nouveau workflow "WooCommerce Achat → FluentCRM". Ajoute un noeud Webhook en methode POST. Ce webhook simule l'evenement d'achat — en production, il serait remplace par le trigger WooCommerce ou le webhook de ta plateforme de paiement.

[Montre le noeud Webhook configure]

**[ECRAN — screencast etape 3 : HTTP Request vers FluentCRM]**

[Ajoute le noeud HTTP Request]

Etape 3 : apres le Webhook, ajoute un noeud "HTTP Request". Configure-le :

- Methode : POST
- URL : l'URL de l'incoming webhook FluentCRM (copiee a l'etape 1)
- Body : JSON

[Montre la configuration du HTTP Request]

Etape 4 : configure le body JSON :

```json
{
  "email": "{{ $json.customer_email }}",
  "first_name": "{{ $json.customer_first_name }}",
  "last_name": "{{ $json.customer_last_name }}",
  "tags": ["acheteur-fluentcrm"],
  "lists": ["clients"],
  "secret_key": "ta-secret-key-ici"
}
```

[Montre le body JSON configure]

Adapte les expressions `{{ $json.xxx }}` selon la structure du payload que ton systeme de paiement envoie. Si tu simules un achat pour le test, utilise des valeurs en dur.

**[ECRAN — screencast etape 5 : test]**

[Teste le flux complet]

Etape 5 : teste le flux. Envoie une requete de test vers le webhook n8n avec un payload simule :

```json
{
  "customer_email": "test-achat@example.com",
  "customer_first_name": "Marie",
  "customer_last_name": "Test",
  "product": "Maitriser FluentCRM",
  "amount": 97
}
```

[Montre l'envoi du test et le resultat dans n8n]

Verifie dans n8n que le HTTP Request retourne un statut 200. Puis va dans FluentCRM > Contacts et cherche "test-achat@example.com". Le contact doit apparaitre avec la liste "clients" et le tag "acheteur-fluentcrm".

[Montre le contact dans FluentCRM avec les bons tags]

**[TRANSITION — face camera]**

Si le contact apparait avec les bons tags et la bonne liste, l'exercice est reussi. Tu as un pipeline d'achat automatise : evenement de paiement → n8n → FluentCRM. En production, il te suffit de remplacer le webhook de test par le vrai trigger de ta plateforme de paiement. Dernier arret : le quiz pour valider tout le module.

---

**Points cles** :
- Scenario reel : achat → n8n → FluentCRM (creation de contact + tag + liste)
- Incoming webhook FluentCRM avec secret key pour la securite
- HTTP Request n8n en POST avec body JSON contenant email, nom, tags, liste
- Toujours tester avec des donnees fictives avant la mise en production
- En production : remplacer le webhook n8n par le vrai trigger de paiement

**Mots cles SEO** : FluentCRM webhook achat, automatiser achat FluentCRM, n8n WooCommerce FluentCRM, webhook achat WordPress, CRM automatisation paiement

---

### Lecon 13.8 — Quiz : Valide tes acquis M13

**Duree** : 5 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichees dans TutorLMS, pas de video

---

**Question 1** : Quelle est la difference entre un incoming webhook et un outgoing webhook dans FluentCRM ?

- A) L'incoming envoie des emails, l'outgoing recoit des emails
- B) L'incoming recoit des donnees depuis un outil externe, l'outgoing envoie des donnees vers un outil externe ✅
- C) L'incoming est gratuit, l'outgoing est payant
- D) Il n'y a pas de difference — les deux termes sont interchangeables

**Explication** : L'incoming webhook est une URL qui recoit des donnees depuis l'exterieur. L'outgoing webhook est une action qui envoie des donnees vers un outil externe quand un evenement se produit dans FluentCRM.

---

**Question 2** : Ou configures-tu un outgoing webhook dans FluentCRM ?

- A) Dans Settings > Integrations > Webhooks
- B) Dans le builder d'automation, comme une action ✅
- C) Dans Contacts > Export > Webhook
- D) Dans Email Campaigns > Settings

**Explication** : L'outgoing webhook est une action disponible dans le builder d'automation de FluentCRM. Il se declenche dans le cadre d'une automation, pas comme un reglage global.

---

**Question 3** : Pourquoi faut-il configurer une secret key sur un incoming webhook ?

- A) Pour chiffrer les emails envoyes par FluentCRM
- B) Pour empecher des requetes non autorisees de creer des contacts dans ta base ✅
- C) Pour que FluentCRM puisse se connecter a l'API de l'outil externe
- D) La secret key est facultative et n'a aucun impact sur la securite

**Explication** : Sans secret key, n'importe qui connaissant l'URL du webhook pourrait envoyer des requetes et injecter des contacts dans ta base FluentCRM. La secret key verifie que la requete provient bien d'une source autorisee.

---

**Question 4** : Tu veux connecter FluentCRM a Zapier. Quelle methode utilises-tu ?

- A) Le connecteur natif FluentCRM dans Zapier
- B) L'extension "Zapier for FluentCRM" disponible sur WordPress.org
- C) Les webhooks — incoming et outgoing — car il n'y a pas de connecteur natif ✅
- D) Un plugin tiers payant obligatoire

**Explication** : FluentCRM n'a pas de connecteur natif dans Zapier. La connexion passe par les webhooks : outgoing webhook FluentCRM vers "Catch Hook" Zapier, et action POST Zapier vers l'incoming webhook FluentCRM.

---

**Question 5** : Quel noeud n8n utilises-tu pour recevoir des donnees envoyees par FluentCRM ?

- A) Le noeud "HTTP Request"
- B) Le noeud "Webhook" ✅
- C) Le noeud "FluentCRM Trigger"
- D) Le noeud "Email Received"

**Explication** : Le noeud Webhook de n8n expose une URL capable de recevoir des requetes HTTP. FluentCRM envoie ses donnees via outgoing webhook vers cette URL. Le noeud HTTP Request sert a envoyer des requetes, pas a en recevoir.

---

**Question 6** : Dans le workflow n8n "FluentCRM → Google Sheets", quel mode configures-tu pour le noeud Google Sheets ?

- A) "Read Rows" — pour lire les donnees existantes
- B) "Update Row" — pour modifier une ligne existante
- C) "Append Row" — pour ajouter une nouvelle ligne a chaque contact ✅
- D) "Delete Row" — pour supprimer les doublons

**Explication** : Le mode "Append Row" ajoute une nouvelle ligne a chaque execution. Chaque contact envoye par FluentCRM cree une ligne supplementaire dans le Sheet, ce qui constitue un log continu.

---

**Question 7** : Tu configures un HTTP Request dans n8n pour envoyer un contact vers l'incoming webhook FluentCRM. Quel format de body utilises-tu ?

- A) XML avec les balises <contact> et <email>
- B) Form data (application/x-www-form-urlencoded)
- C) JSON avec les champs email, first_name, tags et la secret key ✅
- D) CSV avec les colonnes separees par des virgules

**Explication** : Les webhooks FluentCRM attendent un payload au format JSON contenant les champs du contact (email, first_name, last_name, tags, lists) et la secret key pour l'authentification.

---

**Question 8** : Quel est l'avantage principal de n8n par rapport a Zapier pour les connexions avec FluentCRM ?

- A) n8n a un connecteur natif FluentCRM, pas Zapier
- B) n8n est plus rapide que Zapier pour envoyer des webhooks
- C) n8n est open source et n'impose pas de limite de workflows — tu peux creer autant d'automatisations que necessaire ✅
- D) n8n ne necessite aucune configuration — tout est automatique

**Explication** : n8n est open source et auto-hebergeable. Tu peux creer autant de workflows que tu veux sans payer par execution, contrairement a Zapier qui facture par Zap et par execution au-dela du plan gratuit.

---

**Seuil de reussite** : 6/8 (75%)

**Message de reussite** : Module 13 valide. Tu maitrises les webhooks FluentCRM — incoming et outgoing — et tu sais connecter FluentCRM a Zapier, n8n et Google Sheets. Tu as les bases pour automatiser n'importe quelle integration entre FluentCRM et tes outils externes.

**Message d'echec** : Tu n'as pas atteint le seuil de 75%. Revois les lecons 13.1 a 13.6, en particulier la difference entre incoming et outgoing webhooks, et la connexion FluentCRM-n8n. Tu peux retenter le quiz autant de fois que necessaire.
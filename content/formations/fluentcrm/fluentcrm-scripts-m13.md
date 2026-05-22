# Scripts vidéo — Module 13 : Webhooks et connexions externes

**Formation** : Maîtriser FluentCRM
**Module** : M13 — Webhooks et connexions externes (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~50 min
**Prérequis** : M6 (automations de base), M7 (automation avancée)
**Date** : 2026-03-23

---

### Leçon 13.1 — Comprends les webhooks : incoming vs outgoing

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu utilises FluentCRM pour gérer tes contacts et tes automations. Mais ton business ne vit pas uniquement dans FluentCRM. Tu as des formulaires sur d'autres plateformes, un outil de paiement, peut-être un CRM externe ou un tableau de bord Google Sheets. Et ces outils ne se parlent pas entre eux — sauf si tu les connectes. Les webhooks sont le pont entre FluentCRM et le reste de ton écosystème. Dans cette leçon, tu comprends ce que c'est, comment ça fonctionne, et la différence entre les deux types : incoming et outgoing.

**[ÉCRAN — slide "Qu'est-ce qu'un webhook ?"]**

[Montre un schéma simple : Outil A → flèche → Outil B]

Étape 1 : un webhook, c'est un message HTTP envoyé automatiquement d'un outil à un autre quand un événement se produit. Pas de synchronisation périodique, pas de fichier CSV à exporter. L'événement arrive, le message part instantanément.

Concrètement : un client achète sur WooCommerce → WooCommerce envoie un webhook → FluentCRM reçoit le message et ajoute le contact avec le bon tag. Tout ça en temps réel, sans intervention manuelle.

**[ÉCRAN — slide "Incoming vs Outgoing"]**

[Montre un schéma avec deux flèches : une entrante, une sortante, FluentCRM au centre]

Étape 2 : il existe deux types de webhooks dans FluentCRM.

Incoming webhook — FluentCRM reçoit des données. Un outil externe envoie une requête HTTP vers une URL unique générée par FluentCRM. Cas typique : un formulaire Typeform envoie les soumissions à FluentCRM pour créer un contact.

Outgoing webhook — FluentCRM envoie des données. Quand un événement se produit dans FluentCRM (tag ajouté, automation déclenchée), il envoie un payload JSON vers un outil externe. Cas typique : un contact atteint un certain score → FluentCRM envoie ses infos à n8n pour déclencher une alerte Telegram.

**[ÉCRAN — slide "Quand utiliser quoi"]**

[Montre un tableau avec 3 colonnes : Scénario, Type, Exemple]

Étape 3 : voici comment choisir.

Tu veux que des données entrent dans FluentCRM depuis un outil externe ? Incoming webhook. Exemples : formulaire externe, plateforme de paiement, outil de scraping.

Tu veux que FluentCRM notifie un outil externe quand quelque chose se passe ? Outgoing webhook. Exemples : alerte Telegram, mise à jour Google Sheets, création de tâche dans un outil de gestion.

Tu veux les deux ? Combine les deux. C'est ce qu'on fait avec n8n dans les leçons suivantes.

**[ÉCRAN — slide "Anatomie d'un webhook"]**

[Montre un exemple de payload JSON simplifie]

Étape 4 : techniquement, un webhook c'est une requête HTTP POST qui transporte un payload JSON. Voici a quoi ca ressemble :

```json
{
  "email": "jean@example.com",
  "first_name": "Jean",
  "tags": ["acheteur", "cours-lms"],
  "event": "purchase_completed"
}
```

Tu n'as pas besoin de coder pour utiliser les webhooks — FluentCRM et les outils comme n8n gèrent la partie technique. Mais comprendre cette structure t'aide à débugger quand quelque chose ne fonctionne pas.

**[TRANSITION — face caméra]**

Tu sais maintenant ce qu'est un webhook et quand utiliser incoming ou outgoing. Ce sont les deux mécanismes qui permettent à FluentCRM de communiquer avec n'importe quel outil externe. Dans la prochaine leçon, tu configures ton premier incoming webhook — pour recevoir des données dans FluentCRM depuis l'extérieur.

---

**Points clés** :
- Webhook = message HTTP automatique envoyé quand un événement se produit
- Incoming webhook : FluentCRM reçoit des données depuis un outil externe
- Outgoing webhook : FluentCRM envoie des données vers un outil externe
- Le payload est au format JSON — structure clé-valeur
- Pas besoin de coder — les outils gèrent la partie technique

**Mots clés SEO** : FluentCRM webhook, incoming webhook FluentCRM, outgoing webhook FluentCRM, connecter FluentCRM outils externes, webhook WordPress CRM

---

### Leçon 13.2 — Configure un incoming webhook (reçois des données externes)

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Un formulaire Typeform, une page de paiement Stripe, un outil de scraping — tous ces outils peuvent envoyer des données à FluentCRM. La condition : que FluentCRM expose une URL capable de recevoir ces données. C'est exactement ce que fait l'incoming webhook. Dans cette leçon, tu en configures un de A à Z, avec le mapping des champs et la sécurisation par secret key.

**[ÉCRAN — screencast FluentCRM > Settings > Incoming Webhooks]**

[Navigation vers FluentCRM > Settings > Incoming Webhooks]

Étape 1 : va dans FluentCRM, puis Settings, puis cherche la section "Incoming Webhooks" ou "REST API". Selon ta version de FluentCRM, l'emplacement exact peut varier. Tu cherches l'option qui te permet de créer une URL de réception de données.

[Montre le bouton "Create Webhook" ou équivalent]

Étape 2 : crée un nouveau webhook. Donne-lui un nom descriptif — par exemple "Typeform - Inscription Newsletter" ou "Stripe - Achat Cours LMS". Ce nom est interne, il te sert à identifier quel outil envoie des données vers ce point d'entrée.

**[ÉCRAN — screencast URL du webhook]**

[Montre l'URL générée par FluentCRM]

Étape 3 : FluentCRM génère une URL unique. Elle ressemble à ça :

```
https://tonsite.com/?fluentcrm=1&route=contact&hash=abc123xyz
```

Cette URL est le point d'entrée. Tout outil qui envoie une requête POST vers cette URL peut créer ou mettre à jour un contact dans FluentCRM. Note cette URL — tu la colles dans l'outil externe à l'étape suivante.

**[ÉCRAN — screencast mapping des champs]**

[Montre l'interface de mapping]

Étape 4 : configure le mapping des champs. FluentCRM doit savoir à quoi correspond chaque donnée reçue. Le champ "email" de l'outil externe correspond au champ "Email" de FluentCRM. Le champ "name" correspond à "First Name". Si l'outil externe envoie des champs personnalisés, tu les mappes vers des custom fields FluentCRM.

[Montre le mapping email → Email, name → First Name, phone → Phone]

Les champs standards sont mappés automatiquement si les noms correspondent. Pour les champs non standards, tu fais le mapping manuellement.

**[ÉCRAN — screencast configuration liste et tags]**

[Montre les options d'assignation automatique]

Étape 5 : configure les actions automatiques. À chaque donnée reçue, FluentCRM peut automatiquement assigner le contact à une liste et lui poser des tags. Par exemple : liste "Leads Typeform", tag "source-typeform". Ça te permet de segmenter immédiatement les contacts selon leur source d'acquisition.

[Configure la liste et les tags]

**[ÉCRAN — screencast secret key]**

[Montre le champ "Secret Key" ou "Authentication"]

Étape 6 : sécurise le webhook avec une secret key. Sans cette clé, n'importe qui connaissant ton URL pourrait injecter des contacts dans ta base. La secret key est un paramètre supplémentaire que l'outil externe doit inclure dans sa requête. Si la clé ne correspond pas, FluentCRM rejette la donnée.

[Montre où copier la secret key]

Copie cette clé et ajoute-la dans la configuration du webhook côté outil externe. La plupart des outils (Typeform, Zapier, n8n) ont un champ dédié pour ça.

**[ÉCRAN — screencast test du webhook]**

[Montre un test avec un outil comme Postman ou le test intégré]

Étape 7 : teste le webhook avant de le mettre en production. Envoie une requête de test avec des données fictives. Vérifie que le contact apparaît dans FluentCRM avec les bons champs, la bonne liste et les bons tags.

[Montre le contact créé dans FluentCRM après le test]

Si le contact n'apparaît pas, vérifie trois choses : l'URL est correcte, la secret key est incluse, et le format JSON est valide.

**[TRANSITION — face caméra]**

Ton incoming webhook est en place. FluentCRM peut maintenant recevoir des données depuis n'importe quel outil externe. Dans la prochaine leçon, on fait l'inverse : configurer un outgoing webhook pour que FluentCRM envoie des données vers l'extérieur.

---

**Points clés** :
- Incoming webhook = URL unique générée par FluentCRM pour recevoir des données externes
- Mapping des champs : associer les champs de l'outil externe aux champs FluentCRM
- Actions automatiques : assigner liste et tags à chaque contact reçu
- Secret key : sécuriser le webhook pour empêcher les injections non autorisées
- Toujours tester avec des données fictives avant la mise en production

**Mots clés SEO** : FluentCRM incoming webhook, recevoir données FluentCRM, webhook FluentCRM configuration, connecter Typeform FluentCRM, FluentCRM REST API

---

### Leçon 13.3 — Configure un outgoing webhook (envoie des données)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

FluentCRM sait maintenant recevoir des données. L'autre direction est tout aussi importante : envoyer des données vers l'extérieur quand un événement se produit. Un contact atteint un score de 50 points → tu veux une alerte. Un tag "acheteur" est posé → tu veux mettre à jour un Google Sheet. C'est le rôle de l'outgoing webhook — et il se configure directement dans le builder d'automation.

**[ÉCRAN — screencast FluentCRM > Automations > Nouveau]**

[Cree une nouvelle automation]

Étape 1 : l'outgoing webhook n'est pas un réglage global — c'est une action dans une automation. Va dans Automations, crée une nouvelle automation. Choisis un trigger adapté à ton cas. Par exemple : "Tag Applied" — quand le tag "lead-qualifié" est posé sur un contact.

[Montre la sélection du trigger "Tag Applied"]

**[ÉCRAN — screencast ajout de l'action webhook]**

[Ajoute une action dans le builder]

Étape 2 : dans le builder, ajoute une action. Cherche "Outgoing Webhook" ou "Send HTTP Request" dans la liste des actions disponibles. C'est cette action qui envoie des données vers un outil externe.

[Montre l'action "Outgoing Webhook" dans la liste]

Étape 3 : configure l'URL de destination. C'est l'URL de l'outil qui va recevoir les données — par exemple l'URL d'un webhook n8n, un endpoint Zapier, ou une URL Google Apps Script. Colle l'URL dans le champ prévu.

[Montre le champ URL et colle une URL n8n en exemple]

**[ÉCRAN — screencast configuration du payload]**

[Montre les options de payload]

Étape 4 : configure le payload — les données que FluentCRM envoie. Par défaut, FluentCRM envoie toutes les informations du contact : email, nom, tags, listes, custom fields, score. Tu peux personnaliser ce payload si tu veux envoyer uniquement certains champs.

[Montre le payload par défaut avec les champs du contact]

Voici un exemple de payload envoyé par FluentCRM :

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

L'outil de destination reçoit exactement ces données et peut agir en conséquence.

**[ÉCRAN — screencast headers et authentification]**

[Montre les options avancées]

Étape 5 : si l'outil de destination exige une authentification, ajoute les headers nécessaires. Le plus courant : un header "Authorization" avec un token Bearer, ou un header personnalisé avec une API key. Pour n8n en mode webhook basique, aucune authentification n'est nécessaire — l'URL suffit.

[Montre l'ajout d'un header Authorization]

**[ÉCRAN — screencast test de l'automation]**

[Active l'automation et teste avec un contact]

Étape 6 : teste l'automation. Prends un contact de test, ajoute-lui le tag déclencheur. L'automation doit se déclencher, l'outgoing webhook doit envoyer la requête, et l'outil de destination doit recevoir les données.

[Montre le log de l'automation avec le webhook envoyé]

Vérifie dans le log de l'automation que l'action webhook a un statut "Success". Si tu vois "Failed", vérifie l'URL de destination et les éventuels headers d'authentification.

**[TRANSITION — face caméra]**

L'outgoing webhook est ton outil pour pousser des données depuis FluentCRM vers n'importe quelle destination. Combine-le avec les triggers d'automation et tu peux notifier, synchroniser, alerter en temps réel. Dans la prochaine leçon, on connecte FluentCRM à Zapier via ces mêmes webhooks.

---

**Points clés** :
- Outgoing webhook = action dans une automation qui envoie des données vers un outil externe
- Se configure dans le builder d'automation, pas dans les réglages globaux
- Le payload contient par défaut toutes les infos du contact (email, nom, tags, score)
- Headers pour l'authentification si l'outil de destination l'exige
- Toujours vérifier le statut "Success" dans les logs d'automation

**Mots clés SEO** : FluentCRM outgoing webhook, envoyer données FluentCRM, webhook automation FluentCRM, FluentCRM HTTP request, FluentCRM notification externe

---

### Leçon 13.4 — Connecte FluentCRM à Zapier

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + Zapier

---

**[INTRO — face caméra]**

Zapier est l'outil d'automatisation le plus connu. Si tu l'utilises déjà, tu veux probablement le connecter à FluentCRM. Mauvaise nouvelle : il n'existe pas de connecteur natif FluentCRM dans Zapier. Bonne nouvelle : les webhooks que tu viens de configurer font exactement le même travail. Dans cette leçon, tu connectes FluentCRM à Zapier dans les deux sens.

**[ÉCRAN — slide "FluentCRM + Zapier : 2 directions"]**

[Montre un schéma : FluentCRM ↔ Zapier avec les deux flèches]

Étape 1 : la connexion fonctionne dans les deux sens.

Zapier vers FluentCRM : Zapier envoie des données vers l'incoming webhook de FluentCRM. Cas d'usage : un nouveau lead Calendly → Zapier → FluentCRM.

FluentCRM vers Zapier : l'outgoing webhook de FluentCRM envoie des données vers un Zap. Cas d'usage : tag "client" posé → FluentCRM → Zapier → ajout dans un Google Sheet.

**[ÉCRAN — screencast Zapier > Create Zap > Trigger Webhook]**

[Cree un nouveau Zap avec le trigger "Webhooks by Zapier"]

Étape 2 : commençons par FluentCRM vers Zapier. Dans Zapier, crée un nouveau Zap. Comme trigger, choisis "Webhooks by Zapier" puis "Catch Hook". Zapier génère une URL unique.

[Montre l'URL générée par Zapier]

Copie cette URL. Tu vas la coller dans FluentCRM.

**[ÉCRAN — screencast FluentCRM > Automation > Outgoing Webhook]**

[Ouvre l'automation avec l'outgoing webhook]

Étape 3 : dans FluentCRM, ouvre l'automation qui doit envoyer des données à Zapier. Ajoute une action "Outgoing Webhook" et colle l'URL Zapier comme destination. Le payload par défaut de FluentCRM suffit — Zapier recevra toutes les infos du contact.

[Colle l'URL Zapier dans le champ destination]

**[ÉCRAN — screencast Zapier > Test Trigger]**

[Teste le trigger dans Zapier]

Étape 4 : retourne dans Zapier et clique sur "Test trigger". Déclenche l'automation dans FluentCRM avec un contact de test. Zapier doit capter la requête et afficher les données reçues. Tu vois l'email, le nom, les tags — tout le payload.

[Montre les données reçues dans Zapier]

Étape 5 : ajoute l'action de ton choix dans Zapier. Par exemple : "Google Sheets — Create Spreadsheet Row" pour logger chaque nouveau client dans un tableau. Mappe les champs FluentCRM vers les colonnes de ton Sheet.

[Montre le mapping des champs dans l'action Zapier]

**[ÉCRAN — screencast Zapier vers FluentCRM]**

[Cree un nouveau Zap avec l'action "Webhooks by Zapier > POST"]

Étape 6 : dans l'autre sens — Zapier vers FluentCRM. Crée un Zap avec le trigger de ton choix (nouveau lead Calendly, nouveau paiement Stripe, etc.). Comme action, choisis "Webhooks by Zapier" puis "POST". Colle l'URL de l'incoming webhook FluentCRM que tu as créé dans la leçon 13.2.

[Montre la configuration du POST avec l'URL FluentCRM]

Configure le body en JSON avec les champs attendus par FluentCRM : email, first_name, et les éventuels tags. N'oublie pas d'inclure la secret key si tu en as configuré une.

**[ÉCRAN — screencast test complet]**

[Teste le Zap et vérifié dans FluentCRM]

Étape 7 : teste le Zap complet. Déclenche l'événement source, vérifie que Zapier envoie la requête, et confirme que le contact apparaît dans FluentCRM avec les bons champs et tags.

[Montre le contact créé dans FluentCRM via Zapier]

**[TRANSITION — face caméra]**

FluentCRM et Zapier sont connectés. Tu peux envoyer et recevoir des données dans les deux sens. C'est une solution qui fonctionne, mais Zapier a une limite : le plan gratuit est vite dépassé et chaque Zap supplémentaire coûte. Dans la prochaine leçon, on voit n8n — l'alternative open source sans limite de workflows.

---

**Points clés** :
- Pas de connecteur natif FluentCRM dans Zapier — les webhooks font le travail
- FluentCRM → Zapier : outgoing webhook vers "Catch Hook" Zapier
- Zapier → FluentCRM : action POST vers l'incoming webhook FluentCRM
- Toujours tester le flux complet avant de mettre en production
- Limite Zapier : plan gratuit restreint, coût par Zap supplémentaire

**Mots clés SEO** : FluentCRM Zapier, connecter FluentCRM Zapier, webhook Zapier FluentCRM, automatisation FluentCRM Zapier, FluentCRM intégration Zapier

---

### Leçon 13.5 — Connecte FluentCRM à n8n : automatisation sans limites

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + n8n

---

**[INTRO — face caméra]**

n8n est l'outil d'automatisation que j'utilise au quotidien pour schoolsWP. Contrairement à Zapier, il est open source, auto-hébergeable, et surtout : pas de limite de workflows. Tu peux créer autant d'automatisations que tu veux sans payer par exécution. Et la connexion avec FluentCRM est bidirectionnelle — n8n reçoit des données via webhook et en envoie via HTTP Request. Dans cette leçon, tu mets en place les deux sens.

**[ÉCRAN — slide "Architecture FluentCRM + n8n"]**

[Montre un schéma : FluentCRM ↔ n8n ↔ (Telegram, Google Sheets, CRM externe, Slack)]

Étape 1 : voici l'architecture cible. FluentCRM est ton hub de contacts et d'automations email. n8n est ton orchestrateur — il reçoit les événements de FluentCRM et déclenche des actions dans n'importe quel outil. L'inverse aussi : n8n capte des événements externes et met à jour FluentCRM. C'est le combo le plus puissant pour un site WordPress.

**[ÉCRAN — screencast n8n > Nouveau workflow > Webhook node]**

[Cree un nouveau workflow dans n8n]

Étape 2 : dans n8n, crée un nouveau workflow. Ajoute un nœud "Webhook" comme point d'entrée. Configure-le en méthode POST. n8n génère une URL de production et une URL de test.

[Montre les deux URLs générées]

Copie l'URL de test pour commencer. Tu passeras à l'URL de production une fois que tout fonctionne. L'URL ressemble à :

```
https://ton-n8n.example.com/webhook-test/fluentcrm-events
```

**[ÉCRAN — screencast FluentCRM > Automation > Outgoing Webhook]**

[Ouvre une automation FluentCRM]

Étape 3 : dans FluentCRM, ouvre ou crée une automation. Ajoute un outgoing webhook avec l'URL n8n comme destination. Par exemple : trigger "Tag Applied" avec le tag "lead-qualifié" → action "Outgoing Webhook" vers n8n.

[Configure l'outgoing webhook avec l'URL n8n]

Étape 4 : dans n8n, clique sur "Listen for test event" sur le nœud Webhook. Puis dans FluentCRM, déclenche l'automation avec un contact de test. n8n capte la requête et affiche le payload complet.

[Montre le payload reçu dans n8n]

Tu vois toutes les données du contact : email, nom, tags, listes, score. À partir de là, tu peux faire ce que tu veux dans n8n.

**[ÉCRAN — screencast n8n > Ajout de noeuds d'action]**

[Ajoute des noeuds après le webhook]

Étape 5 : voici trois actions concrètes que tu peux enchainer après le webhook.

Action 1 — Alerte Telegram. Ajoute un nœud "Telegram" configuré avec ton bot. À chaque lead qualifié, tu reçois un message instantané sur ton téléphone avec le nom et l'email du contact.

[Montre le nœud Telegram configuré]

Action 2 — Ajout Google Sheets. Ajoute un nœud "Google Sheets" pour logger le contact dans un tableau de reporting. Chaque nouvelle ligne = un lead qualifié.

[Montre le nœud Google Sheets configuré]

Action 3 — Lead scoring avancé. Ajoute un nœud "Code" pour calculer un score personnalisé basé sur les tags et l'historique du contact, puis un nœud "HTTP Request" pour renvoyer le score à FluentCRM via son API REST.

[Montre le nœud Code avec le calcul de score]

**[ÉCRAN — screencast n8n vers FluentCRM via HTTP Request]**

[Crée un nouveau workflow avec un HTTP Request vers FluentCRM]

Étape 6 : dans l'autre sens — n8n vers FluentCRM. Utilise le nœud "HTTP Request" pour appeler l'API REST de FluentCRM ou envoyer des données vers l'incoming webhook. Par exemple : un événement dans Google Calendar → n8n → création d'un contact dans FluentCRM avec le tag "rdv-pris".

[Montre la configuration du HTTP Request avec l'URL incoming webhook FluentCRM]

Configure la méthode POST, le body en JSON avec les champs email, first_name, et les tags. Ajoute la secret key dans les paramètres si nécessaire.

**[ÉCRAN — screencast activation du workflow]**

[Active le workflow en production]

Étape 7 : une fois tes tests validés, active le workflow. Passe l'URL du webhook de "test" à "production" dans le nœud Webhook. Mets à jour l'URL dans FluentCRM. Le workflow tourne en continu — chaque événement FluentCRM déclenche la chaîne d'actions.

[Montre le toggle "Active" du workflow]

**[TRANSITION — face caméra]**

FluentCRM et n8n sont connectés dans les deux sens. Tu as un système d'automatisation complet : FluentCRM gère les contacts et les emails, n8n orchestre tout le reste. Alertes, reporting, lead scoring, synchronisation CRM — tout passe par ce duo. Dans la prochaine leçon, on met ça en pratique avec un cas concret : exporter tes contacts vers Google Sheets.

---

**Points clés** :
- n8n = orchestrateur open source, sans limite de workflows
- FluentCRM → n8n : outgoing webhook vers un nœud Webhook n8n
- n8n → FluentCRM : HTTP Request vers l'API REST ou l'incoming webhook
- 3 cas d'usage immédiats : alerte Telegram, log Google Sheets, lead scoring avancé
- Toujours tester avec l'URL de test avant de passer en production

**Mots clés SEO** : FluentCRM n8n, connecter FluentCRM n8n, automatisation FluentCRM n8n, webhook n8n FluentCRM, FluentCRM open source automation

---

### Leçon 13.6 — Cas d'usage : exporter tes contacts vers Google Sheets

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + n8n + Google Sheets

---

**[INTRO — face caméra]**

Tu veux un tableau de bord de tes contacts FluentCRM dans Google Sheets. Pas un export CSV ponctuel — un flux continu. Chaque nouveau contact qualifié atterrit automatiquement dans une ligne de ton Sheet. C'est un cas d'usage classique et concret pour mettre en pratique la connexion FluentCRM → n8n → Google Sheets.

**[ÉCRAN — screencast Google Sheets > Préparation du tableau]**

[Montre un Google Sheet vide avec les en-têtes]

Étape 1 : prépare ton Google Sheet. Crée un nouveau tableur ou utilise un existant. Ajoute les en-têtes en première ligne :

- A1 : Date
- B1 : Email
- C1 : Prénom
- D1 : Nom
- E1 : Tags
- F1 : Score
- G1 : Source

[Montre les en-têtes configurées]

Ce tableau sera alimenté automatiquement. Chaque ligne sera un contact envoyé par FluentCRM via n8n.

**[ÉCRAN — screencast n8n > Nouveau workflow]**

[Crée le workflow dans n8n]

Étape 2 : dans n8n, crée un nouveau workflow. Nomme-le "FluentCRM → Google Sheets — Sync Contacts". Ajoute un nœud Webhook en méthode POST. Copie l'URL de test.

[Montre le nœud Webhook configuré]

**[ÉCRAN — screencast FluentCRM > Automation]**

[Crée l'automation dans FluentCRM]

Étape 3 : dans FluentCRM, crée une automation. Trigger : "Tag Applied" avec le tag "lead-qualifie" (ou tout autre tag qui marque un contact comme important). Action : "Outgoing Webhook" avec l'URL n8n.

[Montre l'automation configurée]

Teste : ajoute le tag à un contact de test et vérifie que n8n reçoit les données.

**[ÉCRAN — screencast n8n > Ajout du nœud Google Sheets]**

[Ajoute le nœud Google Sheets dans n8n]

Étape 4 : dans n8n, après le nœud Webhook, ajoute un nœud "Google Sheets". Configure-le en mode "Append Row". Sélectionne ton tableur et l'onglet cible.

[Montre la sélection du Sheet et de l'onglet]

Étape 5 : mappe les champs. Voici le mapping :

- Date → `{{ $now.format('yyyy-MM-dd HH:mm') }}`
- Email → `{{ $json.contact.email }}`
- Prénom → `{{ $json.contact.first_name }}`
- Nom → `{{ $json.contact.last_name }}`
- Tags → `{{ $json.contact.tags.join(', ') }}`
- Score → `{{ $json.contact.score }}`
- Source → `"FluentCRM Webhook"`

[Montre le mapping champ par champ]

Les expressions exactes dépendent de la structure du payload FluentCRM. Utilise le panneau de test de n8n pour explorer le JSON reçu et ajuster les chemins.

**[ÉCRAN — screencast test complet]**

[Teste le flux de bout en bout]

Étape 6 : teste le flux complet. Dans FluentCRM, pose le tag déclencheur sur un contact de test. Vérifie dans n8n que le webhook est déclenché. Vérifie dans Google Sheets qu'une nouvelle ligne apparaît avec les bonnes données.

[Montre la ligne ajoutée dans Google Sheets]

Étape 7 : active le workflow en production. Remplace l'URL de test par l'URL de production dans le nœud Webhook. Mets à jour l'URL dans FluentCRM. Désormais, chaque contact qualifié atterrit automatiquement dans ton Google Sheet.

[Montre le workflow actif]

**[TRANSITION — face caméra]**

Tu as un pipeline de données en temps réel : FluentCRM → n8n → Google Sheets. Tu peux l'adapter — ajouter un filtre dans n8n pour ne logger que certains tags, ajouter une colonne calculée dans Sheets, ou dupliquer le workflow pour d'autres types de contacts. Dans la prochaine leçon, tu passes à la pratique avec un exercice guidé.

---

**Points clés** :
- Google Sheet avec en-têtes préparées : Date, Email, Prénom, Nom, Tags, Score, Source
- Workflow n8n : Webhook → Google Sheets (Append Row)
- Mapping des champs via les expressions n8n (chemins JSON du payload FluentCRM)
- Tester d'abord en URL de test, puis passer en production
- Le tableau se remplit automatiquement à chaque contact qualifié

**Mots clés SEO** : FluentCRM Google Sheets, exporter contacts FluentCRM, sync FluentCRM Google Sheets, n8n Google Sheets FluentCRM, reporting contacts WordPress

---

### Leçon 13.7 — Exercice : Crée un webhook n8n qui ajoute un contact à l'achat

**Durée** : 7 min
**Type** : Exercice guidé
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + n8n

---

**[INTRO — face caméra]**

Tu sais configurer des webhooks incoming et outgoing, connecter FluentCRM à n8n, et pousser des données vers Google Sheets. Maintenant tu combines tout ça dans un scénario réel : un client achète un produit (via WooCommerce, TutorLMS ou n'importe quel outil de paiement), n8n reçoit l'événement et crée automatiquement un contact dans FluentCRM avec le tag correspondant. C'est l'automatisation de base de tout business en ligne.

**[ÉCRAN — slide "Scénario de l'exercice"]**

[Montre le schéma : Achat → n8n Webhook → FluentCRM (contact + tag)]

Voici le scénario. Un client achète le cours "Maîtriser FluentCRM". n8n reçoit l'information d'achat via un webhook. n8n crée ou met à jour le contact dans FluentCRM avec le tag "acheteur-fluentcrm" et la liste "clients". Pas d'email, pas de formulaire — tout est automatisé.

**[ÉCRAN — slide "Étapes de l'exercice"]**

[Montre les 5 étapes numérotées]

Tu vas suivre ces 5 étapes :

1. Crée un incoming webhook dans FluentCRM (avec secret key)
2. Crée un workflow n8n avec un nœud Webhook
3. Ajoute un nœud HTTP Request vers l'incoming webhook FluentCRM
4. Configure le payload JSON avec les infos du contact
5. Teste avec un achat simulé

**[ÉCRAN — screencast étape 1 : FluentCRM incoming webhook]**

[Navigation vers FluentCRM > Settings > Incoming Webhooks]

Étape 1 : dans FluentCRM, crée un incoming webhook nommé "n8n — Achat Cours". Configure-le pour assigner automatiquement la liste "clients" et le tag "acheteur". Note l'URL et la secret key.

[Montre la création et la copie de l'URL + secret key]

**[ÉCRAN — screencast étape 2 : n8n workflow]**

[Crée le workflow dans n8n]

Étape 2 : dans n8n, crée un nouveau workflow "WooCommerce Achat → FluentCRM". Ajoute un nœud Webhook en méthode POST. Ce webhook simule l'événement d'achat — en production, il serait remplacé par le trigger WooCommerce ou le webhook de ta plateforme de paiement.

[Montre le nœud Webhook configuré]

**[ÉCRAN — screencast étape 3 : HTTP Request vers FluentCRM]**

[Ajoute le nœud HTTP Request]

Étape 3 : après le Webhook, ajoute un nœud "HTTP Request". Configure-le :

- Méthode : POST
- URL : l'URL de l'incoming webhook FluentCRM (copiée à l'étape 1)
- Body : JSON

[Montre la configuration du HTTP Request]

Étape 4 : configure le body JSON :

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

Adapte les expressions `{{ $json.xxx }}` selon la structure du payload que ton système de paiement envoie. Si tu simules un achat pour le test, utilise des valeurs en dur.

**[ÉCRAN — screencast étape 5 : test]**

[Teste le flux complet]

Étape 5 : teste le flux. Envoie une requête de test vers le webhook n8n avec un payload simulé :

```json
{
  "customer_email": "test-achat@example.com",
  "customer_first_name": "Marie",
  "customer_last_name": "Test",
  "product": "Maîtriser FluentCRM",
  "amount": 97
}
```

[Montre l'envoi du test et le résultat dans n8n]

Vérifie dans n8n que le HTTP Request retourne un statut 200. Puis va dans FluentCRM > Contacts et cherche "test-achat@example.com". Le contact doit apparaître avec la liste "clients" et le tag "acheteur-fluentcrm".

[Montre le contact dans FluentCRM avec les bons tags]

**[TRANSITION — face caméra]**

Si le contact apparaît avec les bons tags et la bonne liste, l'exercice est réussi. Tu as un pipeline d'achat automatisé : événement de paiement → n8n → FluentCRM. En production, il te suffit de remplacer le webhook de test par le vrai trigger de ta plateforme de paiement. Dernier arrêt : le quiz pour valider tout le module.

---

**Points clés** :
- Scénario réel : achat → n8n → FluentCRM (création de contact + tag + liste)
- Incoming webhook FluentCRM avec secret key pour la sécurité
- HTTP Request n8n en POST avec body JSON contenant email, nom, tags, liste
- Toujours tester avec des données fictives avant la mise en production
- En production : remplacer le webhook n8n par le vrai trigger de paiement

**Mots clés SEO** : FluentCRM webhook achat, automatiser achat FluentCRM, n8n WooCommerce FluentCRM, webhook achat WordPress, CRM automatisation paiement

---

### Leçon 13.8 — Quiz : Valide tes acquis M13

**Durée** : 5 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichées dans TutorLMS, pas de vidéo

---

**Question 1** : Quelle est la différence entre un incoming webhook et un outgoing webhook dans FluentCRM ?

- A) L'incoming envoie des emails, l'outgoing reçoit des emails
- B) L'incoming reçoit des données depuis un outil externe, l'outgoing envoie des données vers un outil externe ✅
- C) L'incoming est gratuit, l'outgoing est payant
- D) Il n'y a pas de différence — les deux termes sont interchangeables

**Explication** : L'incoming webhook est une URL qui reçoit des données depuis l'extérieur. L'outgoing webhook est une action qui envoie des données vers un outil externe quand un événement se produit dans FluentCRM.

---

**Question 2** : Où configures-tu un outgoing webhook dans FluentCRM ?

- A) Dans Settings > Integrations > Webhooks
- B) Dans le builder d'automation, comme une action ✅
- C) Dans Contacts > Export > Webhook
- D) Dans Email Campaigns > Settings

**Explication** : L'outgoing webhook est une action disponible dans le builder d'automation de FluentCRM. Il se déclenche dans le cadre d'une automation, pas comme un réglage global.

---

**Question 3** : Pourquoi faut-il configurer une secret key sur un incoming webhook ?

- A) Pour chiffrer les emails envoyés par FluentCRM
- B) Pour empêcher des requêtes non autorisées de créer des contacts dans ta base ✅
- C) Pour que FluentCRM puisse se connecter à l'API de l'outil externe
- D) La secret key est facultative et n'a aucun impact sur la sécurité

**Explication** : Sans secret key, n'importe qui connaissant l'URL du webhook pourrait envoyer des requêtes et injecter des contacts dans ta base FluentCRM. La secret key vérifie que la requête provient bien d'une source autorisée.

---

**Question 4** : Tu veux connecter FluentCRM à Zapier. Quelle méthode utilises-tu ?

- A) Le connecteur natif FluentCRM dans Zapier
- B) L'extension "Zapier for FluentCRM" disponible sur WordPress.org
- C) Les webhooks — incoming et outgoing — car il n'y a pas de connecteur natif ✅
- D) Un plugin tiers payant obligatoire

**Explication** : FluentCRM n'a pas de connecteur natif dans Zapier. La connexion passe par les webhooks : outgoing webhook FluentCRM vers "Catch Hook" Zapier, et action POST Zapier vers l'incoming webhook FluentCRM.

---

**Question 5** : Quel nœud n8n utilises-tu pour recevoir des données envoyées par FluentCRM ?

- A) Le nœud "HTTP Request"
- B) Le nœud "Webhook" ✅
- C) Le nœud "FluentCRM Trigger"
- D) Le nœud "Email Received"

**Explication** : Le nœud Webhook de n8n expose une URL capable de recevoir des requêtes HTTP. FluentCRM envoie ses données via outgoing webhook vers cette URL. Le nœud HTTP Request sert à envoyer des requêtes, pas à en recevoir.

---

**Question 6** : Dans le workflow n8n "FluentCRM → Google Sheets", quel mode configures-tu pour le noeud Google Sheets ?

- A) "Read Rows" — pour lire les données existantes
- B) "Update Row" — pour modifier une ligne existante
- C) "Append Row" — pour ajouter une nouvelle ligne a chaque contact ✅
- D) "Delete Row" — pour supprimer les doublons

**Explication** : Le mode "Append Row" ajoute une nouvelle ligne à chaque exécution. Chaque contact envoyé par FluentCRM crée une ligne supplémentaire dans le Sheet, ce qui constitue un log continu.

---

**Question 7** : Tu configures un HTTP Request dans n8n pour envoyer un contact vers l'incoming webhook FluentCRM. Quel format de body utilises-tu ?

- A) XML avec les balises <contact> et <email>
- B) Form data (application/x-www-form-urlencoded)
- C) JSON avec les champs email, first_name, tags et la secret key ✅
- D) CSV avec les colonnes séparées par des virgules

**Explication** : Les webhooks FluentCRM attendent un payload au format JSON contenant les champs du contact (email, first_name, last_name, tags, lists) et la secret key pour l'authentification.

---

**Question 8** : Quel est l'avantage principal de n8n par rapport à Zapier pour les connexions avec FluentCRM ?

- A) n8n a un connecteur natif FluentCRM, pas Zapier
- B) n8n est plus rapide que Zapier pour envoyer des webhooks
- C) n8n est open source et n'impose pas de limite de workflows — tu peux créer autant d'automatisations que nécessaire ✅
- D) n8n ne nécessite aucune configuration — tout est automatique

**Explication** : n8n est open source et auto-hébergeable. Tu peux créer autant de workflows que tu veux sans payer par exécution, contrairement à Zapier qui facture par Zap et par exécution au-delà du plan gratuit.

---

**Seuil de réussite** : 6/8 (75%)

**Message de réussite** : Module 13 valide. Tu maîtrises les webhooks FluentCRM — incoming et outgoing — et tu sais connecter FluentCRM à Zapier, n8n et Google Sheets. Tu as les bases pour automatiser n'importe quelle intégration entre FluentCRM et tes outils externes.

**Message d'échec** : Tu n'as pas atteint le seuil de 75%. Revois les leçons 13.1 à 13.6, en particulier la différence entre incoming et outgoing webhooks, et la connexion FluentCRM-n8n. Tu peux retenter le quiz autant de fois que nécessaire.
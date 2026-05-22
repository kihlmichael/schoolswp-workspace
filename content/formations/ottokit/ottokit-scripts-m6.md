# Scripts vidéo — Module 6 : Logique conditionnelle : Filter, Condition et Branch

**Formation** : Maîtriser OttoKit
**Module** : M6 — Logique conditionnelle : Filter, Condition et Branch
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~45 min de vidéo
**Date** : 2026-03-30

---

## Leçon 6.1 — Filter vs Condition : comprendre la différence fondamentale

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs, screencast OttoKit

---

**[INTRO — face caméra]**

Tu as un workflow qui tourne. Mais tu ne veux pas qu'il traite tout de la même manière. Certaines données doivent être bloquées, d'autres doivent prendre un chemin différent. C'est exactement le rôle de la logique conditionnelle dans OttoKit.

**[ÉCRAN — slide "Deux outils, deux approches"]**

OttoKit propose deux outils de logique qui se ressemblent mais qui font des choses très différentes :

1. **Filter** — c'est un gardien. Il bloque le workflow si la condition n'est pas remplie. Les actions après le Filter ne s'exécutent pas.

2. **Condition** — c'est un aiguillage. Il ajuste les données ou le comportement, mais le workflow continue toujours. Il ne bloque rien.

**[ÉCRAN — slide "Analogie du vigile et du panneau"]**

Pense à un immeuble.

- Le **Filter**, c'est le vigile à l'entrée. Si tu n'as pas ton badge, tu ne passes pas. Le workflow s'arrête là.
- La **Condition**, c'est le panneau d'orientation dans le hall. Tu es déjà entré. Le panneau t'indique : bureau A à droite, bureau B à gauche. Tu avances, mais le chemin s'adapte.

**[ÉCRAN — screencast OttoKit — scénario commande WooCommerce]**

[Ouvre un workflow avec un trigger WooCommerce "Order Created"]

Prenons un scénario concret : tu reçois une nouvelle commande.

[Ajoute un bloc Filter après le trigger]
[Configure la condition : "order_total" > 50]

Avec un Filter, tu dis : "Si la commande fait moins de 50 euros, on arrête tout. Pas d'email, pas de notification, rien." Le workflow s'arrête net.

[Supprime le Filter, ajoute un bloc Condition à la place]
[Configure : si "billing_country" = "FR" alors valeur = "Bonjour", sinon valeur = "Hello"]

Avec une Condition, tu dis : "Le workflow continue dans tous les cas. Mais si le client est en France, je mets 'Bonjour' dans l'email. Sinon, je mets 'Hello'." Le workflow continue, il s'adapte.

**[ÉCRAN — slide "Comparaison directe"]**

| | Filter | Condition |
|---|---|---|
| Rôle | Bloque ou laisse passer | Adapte sans bloquer |
| Si la condition est fausse | Le workflow s'arrête | Le workflow continue (avec la valeur "sinon") |
| Analogie | Vigile à l'entrée | Panneau d'orientation |
| Cas d'usage | Filtrer les commandes < 50 EUR | Personnaliser un email selon le pays |

**[ÉCRAN — slide "Quand utiliser lequel ?"]**

Voici la règle :

- Tu veux **éliminer** des données qui ne t'intéressent pas ? → Filter
- Tu veux **adapter** le comportement selon les données ? → Condition

C'est aussi simple que ça. Dans les prochaines leçons, on entre dans le détail de chacun.

**[TRANSITION — face caméra]**

Maintenant que tu vois la différence, on passe à la pratique. La prochaine leçon est dédiée au Filter App : comment bloquer un workflow quand les données ne correspondent pas.

---

**Points clés**
- Filter = gardien qui bloque le workflow si la condition est fausse
- Condition = aiguillage qui adapte sans jamais bloquer
- Filter pour éliminer, Condition pour adapter
- Toujours se demander : "je veux bloquer ou adapter ?"

**Mots-clés SEO**
- OttoKit Filter vs Condition
- logique conditionnelle OttoKit
- filtrer workflow OttoKit
- condition OttoKit WordPress

---

## Leçon 6.2 — Filter App : bloque un workflow si la condition n'est pas remplie

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Le Filter est ton premier outil de tri. Tu poses une condition, et si elle n'est pas remplie, le workflow s'arrête. Les actions suivantes ne s'exécutent pas. C'est propre, c'est net.

**[ÉCRAN — screencast OttoKit — création du workflow]**

[Ouvre OttoKit — app.ottokit.com]
[Crée un nouveau workflow : "Commande VIP — notification Slack"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data pour charger les champs]

On part d'un cas concret : tu veux être notifié sur Slack uniquement quand une commande dépasse 50 euros. Les petites commandes, tu ne veux pas les voir.

**[ÉCRAN — screencast OttoKit — ajout du Filter]**

[Clique sur le "+" après le trigger]
[Cherche "Filter" dans la liste des apps]
[Sélectionne "Filter"]

Le Filter se place entre le trigger et les actions. Il agit comme un checkpoint.

[Dans le panneau de configuration du Filter]

Tu vois un formulaire avec trois éléments :

1. **Field** — le champ à tester. Clique sur le sélecteur de données dynamiques.
[Sélectionne "total" depuis les données du trigger]

2. **Operator** — la comparaison. OttoKit propose : égal, différent, supérieur, inférieur, contient, ne contient pas, commence par, se termine par, est vide, n'est pas vide.
[Sélectionne "Greater than"]

3. **Value** — la valeur de référence.
[Tape "50"]

**[ÉCRAN — screencast OttoKit — opérateurs AND/OR]**

[Clique sur "Add condition"]

Tu peux ajouter plusieurs conditions. Par défaut, elles sont liées par AND — toutes doivent être vraies.

[Ajoute une deuxième condition : "status" = "processing"]

Ici, on dit : le montant doit être supérieur à 50 EUR **ET** le statut doit être "processing". Les deux conditions doivent être remplies.

[Montre le sélecteur AND / OR entre les conditions]

Tu peux changer en OR : l'une OU l'autre condition suffit. Mais pour notre cas, AND est le bon choix.

**[ÉCRAN — screencast OttoKit — ajout de l'action après le Filter]**

[Ajoute une action "Slack — Send Message" après le Filter]
[Configure : channel = #ventes, message = "Commande VIP de {billing_first_name} : {total} EUR"]

Si la commande passe le filtre (plus de 50 EUR + statut processing), le message Slack est envoyé. Sinon, rien. Le workflow s'arrête au Filter.

**[ÉCRAN — screencast OttoKit — test]**

[Clique sur "Test" ou "Run" pour tester le workflow]
[Montre une commande à 75 EUR — le Filter laisse passer — le message Slack part]
[Montre une commande à 30 EUR — le Filter bloque — pas de message Slack]

Voilà le résultat. 75 EUR : ça passe. 30 EUR : ça bloque. Exactement ce qu'on voulait.

**[ÉCRAN — slide "Ce qu'il faut retenir"]**

- Le Filter se place entre le trigger et les actions
- Si la condition est fausse, tout ce qui suit est ignoré
- Opérateurs disponibles : égal, différent, supérieur, inférieur, contient, commence par, est vide...
- AND = toutes les conditions vraies, OR = au moins une condition vraie
- Le Filter ne modifie pas les données, il les laisse passer ou les bloque

**[TRANSITION — face caméra]**

Tu sais maintenant filtrer. Mais parfois, tu ne veux pas bloquer — tu veux juste adapter. C'est le rôle du Condition App, qu'on voit dans la leçon suivante.

---

**Points clés**
- Le Filter se place entre le trigger et les actions comme un checkpoint
- Si la condition est fausse, les actions suivantes ne s'exécutent pas
- AND = toutes vraies, OR = au moins une vraie
- Le Filter ne modifie pas les données, il décide si le workflow continue

**Mots-clés SEO**
- OttoKit Filter App
- filtrer commande OttoKit
- OttoKit condition AND OR
- bloquer workflow OttoKit

---

## Leçon 6.3 — Condition App : change le comportement sans bloquer

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Le Condition App, c'est l'aiguillage de ton workflow. Il ne bloque rien. Il regarde une donnée et renvoie une valeur différente selon le résultat. Le workflow continue dans tous les cas.

**[ÉCRAN — screencast OttoKit — scénario email personnalisé]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Email bienvenue — personnalisé par pays"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data]

Notre scénario : tu veux envoyer un email de bienvenue après chaque commande. Mais le message d'intro change selon le pays du client. France → "Bonjour", Belgique → "Bonjour", autre → "Hello".

**[ÉCRAN — screencast OttoKit — ajout du Condition App]**

[Clique sur "+" après le trigger]
[Cherche "Condition" dans la liste des apps]
[Sélectionne "Condition"]

Le Condition App s'ouvre avec un formulaire différent du Filter. Ici, tu définis :

1. **Field** — le champ à tester
[Sélectionne "billing_country" depuis les données du trigger]

2. **Operator** — la comparaison
[Sélectionne "Equal to"]

3. **Value** — la valeur attendue
[Tape "FR"]

4. **Output if true** — ce que le Condition renvoie si c'est vrai
[Tape "Bonjour"]

5. **Output if false** — ce que le Condition renvoie si c'est faux
[Tape "Hello"]

**[ÉCRAN — screencast OttoKit — utilisation dans l'email]**

[Ajoute une action "Send Email" après le Condition]
[Dans le champ "Body", utilise le sélecteur de données dynamiques]
[Sélectionne la sortie du Condition App]
[Compose le message : "{output_condition}, merci pour ta commande !"]

Le Condition renvoie "Bonjour" ou "Hello" selon le pays. Tu utilises cette valeur directement dans ton email. Le workflow ne s'est jamais arrêté — il a juste adapté le contenu.

**[ÉCRAN — screencast OttoKit — conditions imbriquées]**

[Retourne sur le Condition App]
[Montre qu'on peut ajouter un second Condition App en série]

Tu peux enchaîner plusieurs Conditions. Par exemple :

- Condition 1 : pays = FR → "Bonjour" / autre → passe au Condition 2
- Condition 2 : pays = DE → "Hallo" / autre → "Hello"

C'est de l'imbrication. Mais attention : si tu as plus de 3 options, le Branch App (qu'on verra juste après) sera plus lisible.

**[ÉCRAN — slide "Filter vs Condition — rappel"]**

| Situation | Utilise |
|---|---|
| Tu veux ignorer certaines commandes | Filter |
| Tu veux personnaliser un message selon une donnée | Condition |
| Tu veux bloquer si un champ est vide | Filter |
| Tu veux afficher un prix en EUR ou USD selon le pays | Condition |

**[ÉCRAN — screencast OttoKit — test du workflow]**

[Teste avec un client FR — l'email contient "Bonjour"]
[Teste avec un client US — l'email contient "Hello"]

Ça fonctionne. Le même workflow, deux expériences différentes pour le client.

**[TRANSITION — face caméra]**

Le Condition fonctionne bien pour deux options : vrai ou faux. Mais que faire quand tu as 3, 4, ou 5 cas possibles ? C'est là que le Branch App entre en jeu.

---

**Points clés**
- Le Condition App ne bloque jamais le workflow
- Il renvoie une valeur différente selon que la condition est vraie ou fausse
- La sortie du Condition s'utilise dans les actions suivantes via le sélecteur dynamique
- Pour plus de 2-3 options, préférer le Branch App

**Mots-clés SEO**
- OttoKit Condition App
- personnaliser email OttoKit
- condition OttoKit workflow
- logique conditionnelle automatisation WordPress

---

## Leçon 6.4 — Branch App : crée des chemins multiples

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Le Filter bloque. La Condition adapte une valeur. Le Branch, lui, ouvre plusieurs chemins. Chaque branche a sa propre condition et ses propres actions. C'est l'outil idéal quand tu as 3 segments ou plus.

**[ÉCRAN — screencast OttoKit — scénario segmentation client]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Segmentation client — VIP / Standard / Inactif"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data]

Notre scénario : tu segmentes tes clients en 3 catégories. Chaque catégorie reçoit un traitement différent.

- **VIP** : commande > 200 EUR → email remerciement + tag CRM "VIP"
- **Standard** : commande entre 50 et 200 EUR → email confirmation classique
- **Inactif** : commande < 50 EUR → pas d'email, juste un log

**[ÉCRAN — screencast OttoKit — ajout du Branch App]**

[Clique sur "+" après le trigger]
[Cherche "Branch" dans la liste]
[Sélectionne "Branch"]

Le Branch s'ouvre et te montre un écran différent des autres apps. Tu vois des onglets ou des sections pour chaque branche.

[Montre l'interface Branch avec les branches par défaut]

Par défaut, OttoKit crée 2 branches. On va en ajouter une troisième.

**[ÉCRAN — screencast OttoKit — configuration des branches]**

[Configure la Branche 1 : "VIP"]
[Condition : "total" > 200]

Branche 1 : VIP. Si le montant dépasse 200 EUR.

[Configure la Branche 2 : "Standard"]
[Condition : "total" >= 50 AND "total" <= 200]

Branche 2 : Standard. Montant entre 50 et 200 EUR.

[Ajoute une Branche 3 : "Inactif"]
[Condition : "total" < 50]

Branche 3 : Inactif. Montant inférieur à 50 EUR.

**[ÉCRAN — screencast OttoKit — actions par branche]**

Maintenant, chaque branche a son propre chemin d'actions.

[Dans la Branche 1 "VIP"]
[Ajoute une action "Send Email" — objet : "Merci pour ta confiance, {billing_first_name}"]
[Ajoute une action "FluentCRM — Add Tag" — tag : "VIP"]

Pour le VIP : email personnalisé + tag CRM.

[Dans la Branche 2 "Standard"]
[Ajoute une action "Send Email" — objet : "Confirmation de ta commande #{order_id}"]

Pour le Standard : email de confirmation classique.

[Dans la Branche 3 "Inactif"]
[Ajoute une action "Google Sheets — Add Row" — log de la commande]

Pour l'Inactif : on note la commande dans un tableur, sans email.

**[ÉCRAN — slide "Vue d'ensemble du workflow"]**

```
Trigger: Nouvelle commande
    │
    ├── Branche VIP (> 200 EUR)
    │   ├── Email remerciement
    │   └── Tag CRM "VIP"
    │
    ├── Branche Standard (50-200 EUR)
    │   └── Email confirmation
    │
    └── Branche Inactif (< 50 EUR)
        └── Log Google Sheets
```

Trois chemins, trois expériences différentes. Un seul workflow.

**[ÉCRAN — screencast OttoKit — test]**

[Teste avec une commande à 350 EUR — branche VIP exécutée]
[Teste avec une commande à 85 EUR — branche Standard exécutée]
[Teste avec une commande à 25 EUR — branche Inactif exécutée]

Chaque commande prend le bon chemin. Les branches qui ne correspondent pas sont ignorées.

**[TRANSITION — face caméra]**

Le Branch est parfait quand tu connais tous tes segments à l'avance. Mais il existe un cousin proche : le Paths. Quelle différence ? On voit ça maintenant.

---

**Points clés**
- Le Branch crée plusieurs chemins avec des conditions et des actions distinctes
- Chaque branche fonctionne de manière indépendante
- Les branches qui ne correspondent pas sont ignorées
- Pour 3+ segments, le Branch est plus lisible que des Conditions imbriquées

**Mots-clés SEO**
- OttoKit Branch App
- segmentation client OttoKit
- branches multiples workflow
- automatisation conditionnelle WordPress

---

## Leçon 6.5 — Paths : un chemin parmi plusieurs

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Le Paths ressemble au Branch, mais avec une différence importante : seul le premier chemin dont la condition est vraie s'exécute. Les autres sont ignorés, même si leurs conditions sont aussi vraies.

**[ÉCRAN — slide "Branch vs Paths"]**

| | Branch | Paths |
|---|---|---|
| Combien de chemins s'exécutent ? | Tous ceux dont la condition est vraie | Un seul — le premier vrai |
| Analogie | Un carrefour avec feux verts multiples | Un aiguillage ferroviaire — une seule voie |
| Cas d'usage | Traiter plusieurs segments en parallèle | Router vers le premier cas qui matche |

Avec le Branch, si plusieurs conditions sont vraies en même temps, plusieurs branches s'exécutent. Avec le Paths, dès qu'une condition est vraie, on prend ce chemin et on ignore le reste.

**[ÉCRAN — screencast OttoKit — scénario routing ticket support]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Routing ticket support"]
[Ajoute un trigger "Form Submitted" (Fluent Forms)]
[Fait un Fetch Data]

Notre scénario : un formulaire de support avec un champ "catégorie". Selon la catégorie, le ticket est envoyé à la bonne équipe. Un seul destinataire par ticket.

**[ÉCRAN — screencast OttoKit — ajout du Paths]**

[Clique sur "+" après le trigger]
[Cherche "Paths" ou "Router" dans la liste des apps]
[Sélectionne l'app correspondante]

[Configure le Path 1 : "Technique"]
[Condition : "categorie" = "bug" OR "categorie" = "erreur"]

Path 1 : si le ticket parle d'un bug ou d'une erreur → équipe technique.

[Configure le Path 2 : "Commercial"]
[Condition : "categorie" = "facturation" OR "categorie" = "abonnement"]

Path 2 : si c'est une question de facturation → équipe commerciale.

[Configure le Path 3 : "General" (défaut)]
[Pas de condition — c'est le "catch-all"]

Path 3 : tout le reste → boîte email générale.

**[ÉCRAN — screencast OttoKit — actions par path]**

[Path 1 : action "Send Email" à support-tech@schoolswp.com]
[Path 2 : action "Send Email" à facturation@schoolswp.com]
[Path 3 : action "Send Email" à contact@schoolswp.com]

Chaque chemin envoie le ticket à la bonne adresse. Et comme c'est un Paths, un ticket "bug + facturation" ira uniquement à l'équipe technique (le premier chemin vrai).

**[ÉCRAN — slide "Quand utiliser Paths plutôt que Branch ?"]**

- Tu veux qu'un seul chemin s'exécute (routing, assignation, redirection) → **Paths**
- Tu veux que plusieurs chemins s'exécutent en parallèle (notifications, tags, logs) → **Branch**
- Tu as un cas "par défaut" (catch-all) → **Paths** avec un dernier chemin sans condition

**[ÉCRAN — screencast OttoKit — test]**

[Teste avec catégorie = "bug" — email envoyé à support-tech@]
[Teste avec catégorie = "facturation" — email envoyé à facturation@]
[Teste avec catégorie = "autre" — email envoyé à contact@]

Un ticket, un chemin. Pas de doublon.

**[TRANSITION — face caméra]**

Tu sais maintenant bloquer, adapter, segmenter et router. Il manque un dernier ingrédient pour construire des workflows intelligents : le temps. Le Delay App te permet d'ajouter des pauses entre les actions.

---

**Points clés**
- Paths = un seul chemin s'exécute (le premier dont la condition est vraie)
- Branch = tous les chemins vrais s'exécutent
- Utiliser un dernier Path sans condition comme "catch-all" (défaut)
- Idéal pour le routing : tickets, assignations, redirections

**Mots-clés SEO**
- OttoKit Paths
- router workflow OttoKit
- Branch vs Paths OttoKit
- aiguillage workflow automatisation

---

## Leçon 6.6 — Delay App : ajoute un délai dans ton workflow

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Jusqu'ici, tes workflows s'exécutent instantanément : trigger → actions → terminé. Mais parfois, tu veux attendre. Envoyer un email de relance 3 jours après l'achat. Demander un avis 15 jours après la livraison. C'est le rôle du Delay App.

**[ÉCRAN — screencast OttoKit — scénario relance J+3]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Relance J+3 — demande de feedback"]
[Ajoute un trigger WooCommerce "Order Completed"]
[Fait un Fetch Data]

Notre scénario : 3 jours après qu'une commande est marquée comme complétée, tu envoies un email pour demander un retour d'expérience.

**[ÉCRAN — screencast OttoKit — ajout du Delay App]**

[Clique sur "+" après le trigger]
[Cherche "Delay" dans la liste des apps]
[Sélectionne "Delay"]

Le Delay App a une interface très simple. Tu définis deux choses :

1. **Durée** — le nombre
[Tape "3"]

2. **Unité** — minutes, heures, jours
[Sélectionne "Days"]

C'est tout. Le workflow va attendre 3 jours à cet endroit précis avant de passer à l'action suivante.

**[ÉCRAN — screencast OttoKit — ajout de l'action après le Delay]**

[Ajoute une action "Send Email" après le Delay]
[Configure : destinataire = {billing_email}]
[Objet : "{billing_first_name}, comment s'est passé ta commande ?"]
[Corps : "Tu as reçu ta commande il y a quelques jours. On aimerait avoir ton avis..."]

L'email part 3 jours après la commande. Pas avant.

**[ÉCRAN — slide "Options de délai"]**

| Unité | Cas d'usage |
|---|---|
| Minutes | Notification de suivi immédiate (5-10 min) |
| Heures | Rappel dans la journée (2-4h) |
| Jours | Relance post-achat, demande d'avis (3-15j) |

Le Delay accepte des valeurs entières. Si tu veux 1 jour et 12 heures, tu peux mettre 36 heures. Ou enchaîner deux Delay.

**[ÉCRAN — slide "Attention : le Delay n'est pas un cron"]**

Point important : le Delay attend à partir du moment où le workflow atteint cette étape. Ce n'est pas un planificateur. Si le trigger se déclenche lundi à 14h et que tu mets un Delay de 3 jours, l'action suivante s'exécutera jeudi à 14h.

Si tu veux qu'une action se déclenche un jour précis (ex: chaque lundi à 9h), utilise le trigger Schedule qu'on a vu au Module 3. Le Delay, c'est du relatif.

**[ÉCRAN — screencast OttoKit — Delay dans le canvas]**

[Montre le workflow complet dans le canvas]
[Pointe le bloc Delay entre le trigger et l'action]
[Montre le badge "3 Days" affiché sur le bloc]

Dans le canvas, le bloc Delay affiche la durée. C'est visuel et lisible. Tu vois tout de suite qu'il y a une pause dans ton workflow.

**[TRANSITION — face caméra]**

Le Delay, c'est simple mais puissant. Et quand tu le combines avec le Filter, le Condition et le Branch, tu peux construire des séquences complètes. C'est exactement ce qu'on fait dans la prochaine leçon : un workflow de nurturing de A à Z.

---

**Points clés**
- Le Delay App met le workflow en pause pour une durée définie
- Unités : minutes, heures, jours
- Le délai est relatif (à partir du déclenchement), pas absolu
- Ne pas confondre Delay (pause dans un workflow) et Schedule (trigger planifié)

**Mots-clés SEO**
- OttoKit Delay App
- délai workflow OttoKit
- email relance automatique WordPress
- temporisation automatisation OttoKit

---

## Leçon 6.7 — Combiner logique et délai : workflow complet de nurturing

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Tu connais le Filter, la Condition, le Branch et le Delay. Chacun fait un truc bien. Mais la vraie puissance, c'est quand tu les combines. On va construire ensemble un workflow complet de nurturing, étape par étape.

**[ÉCRAN — slide "Le scénario : nurturing post-inscription schoolsWP"]**

Voici le scénario qu'on va construire. Un apprenant s'inscrit à la formation gratuite schoolsWP.

1. **J+0** — Email de bienvenue immédiat
2. **J+3** — Email "As-tu commencé le Module 1 ?"
3. **Check** — Vérification : a-t-il commencé M1 ?
4. **Branche OUI** → Email "Bravo, continue avec M2"
5. **Branche NON** → Email "On est là pour t'aider" + tag "relance"
6. **J+15** — Email demande d'avis

C'est un workflow qu'on utilise chez schoolsWP. Il combine tout ce qu'on a vu dans ce module.

**[ÉCRAN — screencast OttoKit — étape 1 : trigger + email bienvenue]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Nurturing inscription gratuite"]
[Ajoute un trigger "User Enrolled" (TutorLMS ou équivalent)]
[Fait un Fetch Data — récupère email, prénom, cours]

[Ajoute une action "Send Email"]
[Destinataire : {student_email}]
[Objet : "{student_first_name}, bienvenue dans la formation !"]
[Corps : "Tu viens de t'inscrire. Voici comment commencer..."]

Étape 1 : dès que quelqu'un s'inscrit, il reçoit un email de bienvenue. C'est immédiat.

**[ÉCRAN — screencast OttoKit — étape 2 : Delay 3 jours]**

[Ajoute un bloc Delay après l'email]
[Configure : 3 jours]

On attend 3 jours. Pas d'action pendant ce temps.

**[ÉCRAN — screencast OttoKit — étape 3 : email relance M1]**

[Ajoute une action "Send Email"]
[Objet : "{student_first_name}, as-tu commencé le Module 1 ?"]
[Corps : "Ça fait 3 jours que tu t'es inscrit. Le Module 1 t'attend..."]

À J+3, on envoie un email de relance. Simple et direct.

**[ÉCRAN — screencast OttoKit — étape 4 : Delay 1 jour + Branch]**

[Ajoute un Delay de 1 jour]

On attend encore un jour pour laisser le temps de réagir.

[Ajoute un bloc Branch après le Delay]

[Configure la Branche 1 : "A commencé"]
[Condition : vérification LMS — leçon complétée > 0]

[Configure la Branche 2 : "N'a pas commencé"]
[Condition : leçon complétée = 0]

**[ÉCRAN — screencast OttoKit — actions par branche]**

[Branche 1 "A commencé"]
[Ajoute une action "Send Email"]
[Objet : "Bravo {student_first_name}, tu es sur la bonne voie !"]
[Corps : "Tu as commencé le Module 1. Voici le Module 2..."]

Pour ceux qui ont commencé : encouragement + lien vers la suite.

[Branche 2 "N'a pas commencé"]
[Ajoute une action "Send Email"]
[Objet : "{student_first_name}, on est là pour t'aider"]
[Corps : "Pas encore commencé ? C'est normal. Voici 3 raisons de commencer aujourd'hui..."]
[Ajoute une action "FluentCRM — Add Tag" : "relance-m1"]

Pour ceux qui n'ont pas commencé : email de soutien + tag CRM pour suivi.

**[ÉCRAN — screencast OttoKit — étape 5 : Delay final + demande d'avis]**

[Après les deux branches, ajoute un Delay de 11 jours]

On attend 11 jours supplémentaires (J+15 au total depuis l'inscription).

[Ajoute une action "Send Email"]
[Objet : "Ton avis nous intéresse, {student_first_name}"]
[Corps : "Ça fait 15 jours que tu nous as rejoint. Qu'est-ce que tu en penses ?"]

**[ÉCRAN — slide "Vue d'ensemble du workflow"]**

```
Trigger: Inscription formation
    │
    ├── Email bienvenue (J+0)
    │
    ├── Delay 3 jours
    │
    ├── Email "As-tu commencé M1 ?" (J+3)
    │
    ├── Delay 1 jour
    │
    ├── Branch
    │   ├── A commencé → Email encouragement
    │   └── N'a pas commencé → Email soutien + Tag "relance-m1"
    │
    ├── Delay 11 jours
    │
    └── Email demande d'avis (J+15)
```

5 emails, 2 branches, 3 délais. Un seul workflow. Zéro intervention manuelle.

**[ÉCRAN — screencast OttoKit — vue canvas complète]**

[Montre le workflow complet dans le canvas OttoKit]
[Pointe chaque bloc : trigger → email → delay → email → delay → branch → actions → delay → email]

[Active le workflow]

Le workflow est prêt. Chaque nouvelle inscription déclenche cette séquence automatiquement.

**[TRANSITION — face caméra]**

Voilà un workflow qui travaille pour toi 24h/24. Tu as vu comment combiner les outils du Module 6 pour créer une vraie machine de nurturing. Place au quiz pour valider tes acquis.

---

**Points clés**
- Un workflow de nurturing combine Delay, Branch et actions email
- Toujours dessiner le workflow sur papier avant de le construire
- Les Delays s'additionnent : 3j + 1j + 11j = 15 jours au total
- Le Branch permet de traiter différemment les actifs et les inactifs
- Un seul workflow remplace des heures de relance manuelle

**Mots-clés SEO**
- OttoKit workflow nurturing
- séquence email automatique OttoKit
- automatisation relance WordPress
- workflow complet OttoKit formation

---

## Notes de production — Module 6

### Captures à préparer
- Canvas OttoKit avec bloc Filter — panneau de configuration visible (opérateurs, AND/OR)
- Canvas OttoKit avec bloc Condition — champs "if true" / "if false" visibles
- Canvas OttoKit avec bloc Branch — 3 branches déployées avec actions différentes
- Canvas OttoKit avec bloc Paths — interface de routing
- Canvas OttoKit avec bloc Delay — badge "3 Days" visible
- Workflow complet nurturing — vue canvas avec tous les blocs (trigger → email → delay → email → delay → branch → delay → email)
- Test Filter : commande 75 EUR passant, commande 30 EUR bloquée (vue History)
- Test Branch : 3 exécutions différentes selon le montant
- Slide comparatif Filter vs Condition (tableau)
- Slide comparatif Branch vs Paths (tableau)
- Slide schéma nurturing (diagramme)

### Environnement de démo
- Compte OttoKit (plan premium recommandé pour les workflows multi-étapes)
- Site WordPress schoolsWP avec WooCommerce (commandes de test à différents montants)
- FluentCRM installé et actif (pour les tags)
- TutorLMS ou équivalent LMS installé (pour le scénario nurturing)
- Fluent Forms avec un formulaire de support (champ catégorie)
- Compte Slack avec un channel #ventes
- Google Sheets vierge pour les logs

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 6.1 | 6 min |
| 6.2 | 6 min |
| 6.3 | 6 min |
| 6.4 | 7 min |
| 6.5 | 6 min |
| 6.6 | 6 min |
| 6.7 | 8 min |
| **Total M6** | **45 min** |

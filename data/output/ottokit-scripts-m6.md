# Scripts video — Module 6 : Logique conditionnelle : Filter, Condition et Branch

**Formation** : Maitriser OttoKit
**Module** : M6 — Logique conditionnelle : Filter, Condition et Branch
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~45 min de video
**Date** : 2026-03-30

---

## Lecon 6.1 — Filter vs Condition : comprendre la difference fondamentale

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs, screencast OttoKit

---

**[INTRO — face camera]**

Tu as un workflow qui tourne. Mais tu ne veux pas qu'il traite tout de la meme maniere. Certaines donnees doivent etre bloquees, d'autres doivent prendre un chemin different. C'est exactement le role de la logique conditionnelle dans OttoKit.

**[ECRAN — slide "Deux outils, deux approches"]**

OttoKit propose deux outils de logique qui se ressemblent mais qui font des choses tres differentes :

1. **Filter** — c'est un gardien. Il bloque le workflow si la condition n'est pas remplie. Les actions apres le Filter ne s'executent pas.

2. **Condition** — c'est un aiguillage. Il ajuste les donnees ou le comportement, mais le workflow continue toujours. Il ne bloque rien.

**[ECRAN — slide "Analogie du vigile et du panneau"]**

Pense a un immeuble.

- Le **Filter**, c'est le vigile a l'entree. Si tu n'as pas ton badge, tu ne passes pas. Le workflow s'arrete la.
- La **Condition**, c'est le panneau d'orientation dans le hall. Tu es deja entre. Le panneau t'indique : bureau A a droite, bureau B a gauche. Tu avances, mais le chemin s'adapte.

**[ECRAN — screencast OttoKit — scenario commande WooCommerce]**

[Ouvre un workflow avec un trigger WooCommerce "Order Created"]

Prenons un scenario concret : tu recois une nouvelle commande.

[Ajoute un bloc Filter apres le trigger]
[Configure la condition : "order_total" > 50]

Avec un Filter, tu dis : "Si la commande fait moins de 50 euros, on arrete tout. Pas d'email, pas de notification, rien." Le workflow s'arrete net.

[Supprime le Filter, ajoute un bloc Condition a la place]
[Configure : si "billing_country" = "FR" alors valeur = "Bonjour", sinon valeur = "Hello"]

Avec une Condition, tu dis : "Le workflow continue dans tous les cas. Mais si le client est en France, je mets 'Bonjour' dans l'email. Sinon, je mets 'Hello'." Le workflow continue, il s'adapte.

**[ECRAN — slide "Comparaison directe"]**

| | Filter | Condition |
|---|---|---|
| Role | Bloque ou laisse passer | Adapte sans bloquer |
| Si la condition est fausse | Le workflow s'arrete | Le workflow continue (avec la valeur "sinon") |
| Analogie | Vigile a l'entree | Panneau d'orientation |
| Cas d'usage | Filtrer les commandes < 50 EUR | Personnaliser un email selon le pays |

**[ECRAN — slide "Quand utiliser lequel ?"]**

Voici la regle :

- Tu veux **eliminer** des donnees qui ne t'interessent pas ? → Filter
- Tu veux **adapter** le comportement selon les donnees ? → Condition

C'est aussi simple que ca. Dans les prochaines lecons, on entre dans le detail de chacun.

**[TRANSITION — face camera]**

Maintenant que tu vois la difference, on passe a la pratique. La prochaine lecon est dediee au Filter App : comment bloquer un workflow quand les donnees ne correspondent pas.

---

**Points cles**
- Filter = gardien qui bloque le workflow si la condition est fausse
- Condition = aiguillage qui adapte sans jamais bloquer
- Filter pour eliminer, Condition pour adapter
- Toujours se demander : "je veux bloquer ou adapter ?"

**Mots-cles SEO**
- OttoKit Filter vs Condition
- logique conditionnelle OttoKit
- filtrer workflow OttoKit
- condition OttoKit WordPress

---

## Lecon 6.2 — Filter App : bloque un workflow si la condition n'est pas remplie

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Le Filter est ton premier outil de tri. Tu poses une condition, et si elle n'est pas remplie, le workflow s'arrete. Les actions suivantes ne s'executent pas. C'est propre, c'est net.

**[ECRAN — screencast OttoKit — creation du workflow]**

[Ouvre OttoKit — app.ottokit.com]
[Cree un nouveau workflow : "Commande VIP — notification Slack"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data pour charger les champs]

On part d'un cas concret : tu veux etre notifie sur Slack uniquement quand une commande depasse 50 euros. Les petites commandes, tu ne veux pas les voir.

**[ECRAN — screencast OttoKit — ajout du Filter]**

[Clique sur le "+" apres le trigger]
[Cherche "Filter" dans la liste des apps]
[Selectionne "Filter"]

Le Filter se place entre le trigger et les actions. Il agit comme un checkpoint.

[Dans le panneau de configuration du Filter]

Tu vois un formulaire avec trois elements :

1. **Field** — le champ a tester. Clique sur le selecteur de donnees dynamiques.
[Selectionne "total" depuis les donnees du trigger]

2. **Operator** — la comparaison. OttoKit propose : egal, different, superieur, inferieur, contient, ne contient pas, commence par, se termine par, est vide, n'est pas vide.
[Selectionne "Greater than"]

3. **Value** — la valeur de reference.
[Tape "50"]

**[ECRAN — screencast OttoKit — operateurs AND/OR]**

[Clique sur "Add condition"]

Tu peux ajouter plusieurs conditions. Par defaut, elles sont liees par AND — toutes doivent etre vraies.

[Ajoute une deuxieme condition : "status" = "processing"]

Ici, on dit : le montant doit etre superieur a 50 EUR **ET** le statut doit etre "processing". Les deux conditions doivent etre remplies.

[Montre le selecteur AND / OR entre les conditions]

Tu peux changer en OR : l'une OU l'autre condition suffit. Mais pour notre cas, AND est le bon choix.

**[ECRAN — screencast OttoKit — ajout de l'action apres le Filter]**

[Ajoute une action "Slack — Send Message" apres le Filter]
[Configure : channel = #ventes, message = "Commande VIP de {billing_first_name} : {total} EUR"]

Si la commande passe le filtre (plus de 50 EUR + statut processing), le message Slack est envoye. Sinon, rien. Le workflow s'arrete au Filter.

**[ECRAN — screencast OttoKit — test]**

[Clique sur "Test" ou "Run" pour tester le workflow]
[Montre une commande a 75 EUR — le Filter laisse passer — le message Slack part]
[Montre une commande a 30 EUR — le Filter bloque — pas de message Slack]

Voila le resultat. 75 EUR : ca passe. 30 EUR : ca bloque. Exactement ce qu'on voulait.

**[ECRAN — slide "Ce qu'il faut retenir"]**

- Le Filter se place entre le trigger et les actions
- Si la condition est fausse, tout ce qui suit est ignore
- Operateurs disponibles : egal, different, superieur, inferieur, contient, commence par, est vide...
- AND = toutes les conditions vraies, OR = au moins une condition vraie
- Le Filter ne modifie pas les donnees, il les laisse passer ou les bloque

**[TRANSITION — face camera]**

Tu sais maintenant filtrer. Mais parfois, tu ne veux pas bloquer — tu veux juste adapter. C'est le role du Condition App, qu'on voit dans la lecon suivante.

---

**Points cles**
- Le Filter se place entre le trigger et les actions comme un checkpoint
- Si la condition est fausse, les actions suivantes ne s'executent pas
- AND = toutes vraies, OR = au moins une vraie
- Le Filter ne modifie pas les donnees, il decide si le workflow continue

**Mots-cles SEO**
- OttoKit Filter App
- filtrer commande OttoKit
- OttoKit condition AND OR
- bloquer workflow OttoKit

---

## Lecon 6.3 — Condition App : change le comportement sans bloquer

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Le Condition App, c'est l'aiguillage de ton workflow. Il ne bloque rien. Il regarde une donnee et renvoie une valeur differente selon le resultat. Le workflow continue dans tous les cas.

**[ECRAN — screencast OttoKit — scenario email personnalise]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Email bienvenue — personnalise par pays"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data]

Notre scenario : tu veux envoyer un email de bienvenue apres chaque commande. Mais le message d'intro change selon le pays du client. France → "Bonjour", Belgique → "Bonjour", autre → "Hello".

**[ECRAN — screencast OttoKit — ajout du Condition App]**

[Clique sur "+" apres le trigger]
[Cherche "Condition" dans la liste des apps]
[Selectionne "Condition"]

Le Condition App s'ouvre avec un formulaire different du Filter. Ici, tu definis :

1. **Field** — le champ a tester
[Selectionne "billing_country" depuis les donnees du trigger]

2. **Operator** — la comparaison
[Selectionne "Equal to"]

3. **Value** — la valeur attendue
[Tape "FR"]

4. **Output if true** — ce que le Condition renvoie si c'est vrai
[Tape "Bonjour"]

5. **Output if false** — ce que le Condition renvoie si c'est faux
[Tape "Hello"]

**[ECRAN — screencast OttoKit — utilisation dans l'email]**

[Ajoute une action "Send Email" apres le Condition]
[Dans le champ "Body", utilise le selecteur de donnees dynamiques]
[Selectionne la sortie du Condition App]
[Compose le message : "{output_condition}, merci pour ta commande !"]

Le Condition renvoie "Bonjour" ou "Hello" selon le pays. Tu utilises cette valeur directement dans ton email. Le workflow ne s'est jamais arrete — il a juste adapte le contenu.

**[ECRAN — screencast OttoKit — conditions imbriquees]**

[Retourne sur le Condition App]
[Montre qu'on peut ajouter un second Condition App en serie]

Tu peux enchainer plusieurs Conditions. Par exemple :

- Condition 1 : pays = FR → "Bonjour" / autre → passe au Condition 2
- Condition 2 : pays = DE → "Hallo" / autre → "Hello"

C'est de l'imbrication. Mais attention : si tu as plus de 3 options, le Branch App (qu'on verra juste apres) sera plus lisible.

**[ECRAN — slide "Filter vs Condition — rappel"]**

| Situation | Utilise |
|---|---|
| Tu veux ignorer certaines commandes | Filter |
| Tu veux personnaliser un message selon une donnee | Condition |
| Tu veux bloquer si un champ est vide | Filter |
| Tu veux afficher un prix en EUR ou USD selon le pays | Condition |

**[ECRAN — screencast OttoKit — test du workflow]**

[Teste avec un client FR — l'email contient "Bonjour"]
[Teste avec un client US — l'email contient "Hello"]

Ca fonctionne. Le meme workflow, deux experiences differentes pour le client.

**[TRANSITION — face camera]**

Le Condition fonctionne bien pour deux options : vrai ou faux. Mais que faire quand tu as 3, 4, ou 5 cas possibles ? C'est la que le Branch App entre en jeu.

---

**Points cles**
- Le Condition App ne bloque jamais le workflow
- Il renvoie une valeur differente selon que la condition est vraie ou fausse
- La sortie du Condition s'utilise dans les actions suivantes via le selecteur dynamique
- Pour plus de 2-3 options, preferer le Branch App

**Mots-cles SEO**
- OttoKit Condition App
- personnaliser email OttoKit
- condition OttoKit workflow
- logique conditionnelle automatisation WordPress

---

## Lecon 6.4 — Branch App : cree des chemins multiples

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Le Filter bloque. La Condition adapte une valeur. Le Branch, lui, ouvre plusieurs chemins. Chaque branche a sa propre condition et ses propres actions. C'est l'outil ideal quand tu as 3 segments ou plus.

**[ECRAN — screencast OttoKit — scenario segmentation client]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Segmentation client — VIP / Standard / Inactif"]
[Ajoute un trigger WooCommerce "Order Created"]
[Fait un Fetch Data]

Notre scenario : tu segmentes tes clients en 3 categories. Chaque categorie recoit un traitement different.

- **VIP** : commande > 200 EUR → email remerciement + tag CRM "VIP"
- **Standard** : commande entre 50 et 200 EUR → email confirmation classique
- **Inactif** : commande < 50 EUR → pas d'email, juste un log

**[ECRAN — screencast OttoKit — ajout du Branch App]**

[Clique sur "+" apres le trigger]
[Cherche "Branch" dans la liste]
[Selectionne "Branch"]

Le Branch s'ouvre et te montre un ecran different des autres apps. Tu vois des onglets ou des sections pour chaque branche.

[Montre l'interface Branch avec les branches par defaut]

Par defaut, OttoKit cree 2 branches. On va en ajouter une troisieme.

**[ECRAN — screencast OttoKit — configuration des branches]**

[Configure la Branche 1 : "VIP"]
[Condition : "total" > 200]

Branche 1 : VIP. Si le montant depasse 200 EUR.

[Configure la Branche 2 : "Standard"]
[Condition : "total" >= 50 AND "total" <= 200]

Branche 2 : Standard. Montant entre 50 et 200 EUR.

[Ajoute une Branche 3 : "Inactif"]
[Condition : "total" < 50]

Branche 3 : Inactif. Montant inferieur a 50 EUR.

**[ECRAN — screencast OttoKit — actions par branche]**

Maintenant, chaque branche a son propre chemin d'actions.

[Dans la Branche 1 "VIP"]
[Ajoute une action "Send Email" — objet : "Merci pour ta confiance, {billing_first_name}"]
[Ajoute une action "FluentCRM — Add Tag" — tag : "VIP"]

Pour le VIP : email personnalise + tag CRM.

[Dans la Branche 2 "Standard"]
[Ajoute une action "Send Email" — objet : "Confirmation de ta commande #{order_id}"]

Pour le Standard : email de confirmation classique.

[Dans la Branche 3 "Inactif"]
[Ajoute une action "Google Sheets — Add Row" — log de la commande]

Pour l'Inactif : on note la commande dans un tableur, sans email.

**[ECRAN — slide "Vue d'ensemble du workflow"]**

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

Trois chemins, trois experiences differentes. Un seul workflow.

**[ECRAN — screencast OttoKit — test]**

[Teste avec une commande a 350 EUR — branche VIP executee]
[Teste avec une commande a 85 EUR — branche Standard executee]
[Teste avec une commande a 25 EUR — branche Inactif executee]

Chaque commande prend le bon chemin. Les branches qui ne correspondent pas sont ignorees.

**[TRANSITION — face camera]**

Le Branch est parfait quand tu connais tous tes segments a l'avance. Mais il existe un cousin proche : le Paths. Quelle difference ? On voit ca maintenant.

---

**Points cles**
- Le Branch cree plusieurs chemins avec des conditions et des actions distinctes
- Chaque branche fonctionne de maniere independante
- Les branches qui ne correspondent pas sont ignorees
- Pour 3+ segments, le Branch est plus lisible que des Conditions imbriquees

**Mots-cles SEO**
- OttoKit Branch App
- segmentation client OttoKit
- branches multiples workflow
- automatisation conditionnelle WordPress

---

## Lecon 6.5 — Paths : un chemin parmi plusieurs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Le Paths ressemble au Branch, mais avec une difference importante : seul le premier chemin dont la condition est vraie s'execute. Les autres sont ignores, meme si leurs conditions sont aussi vraies.

**[ECRAN — slide "Branch vs Paths"]**

| | Branch | Paths |
|---|---|---|
| Combien de chemins s'executent ? | Tous ceux dont la condition est vraie | Un seul — le premier vrai |
| Analogie | Un carrefour avec feux verts multiples | Un aiguillage ferroviaire — une seule voie |
| Cas d'usage | Traiter plusieurs segments en parallele | Router vers le premier cas qui matche |

Avec le Branch, si plusieurs conditions sont vraies en meme temps, plusieurs branches s'executent. Avec le Paths, des qu'une condition est vraie, on prend ce chemin et on ignore le reste.

**[ECRAN — screencast OttoKit — scenario routing ticket support]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Routing ticket support"]
[Ajoute un trigger "Form Submitted" (Fluent Forms)]
[Fait un Fetch Data]

Notre scenario : un formulaire de support avec un champ "categorie". Selon la categorie, le ticket est envoye a la bonne equipe. Un seul destinataire par ticket.

**[ECRAN — screencast OttoKit — ajout du Paths]**

[Clique sur "+" apres le trigger]
[Cherche "Paths" ou "Router" dans la liste des apps]
[Selectionne l'app correspondante]

[Configure le Path 1 : "Technique"]
[Condition : "categorie" = "bug" OR "categorie" = "erreur"]

Path 1 : si le ticket parle d'un bug ou d'une erreur → equipe technique.

[Configure le Path 2 : "Commercial"]
[Condition : "categorie" = "facturation" OR "categorie" = "abonnement"]

Path 2 : si c'est une question de facturation → equipe commerciale.

[Configure le Path 3 : "General" (defaut)]
[Pas de condition — c'est le "catch-all"]

Path 3 : tout le reste → boite email generale.

**[ECRAN — screencast OttoKit — actions par path]**

[Path 1 : action "Send Email" a support-tech@schoolswp.com]
[Path 2 : action "Send Email" a facturation@schoolswp.com]
[Path 3 : action "Send Email" a contact@schoolswp.com]

Chaque chemin envoie le ticket a la bonne adresse. Et comme c'est un Paths, un ticket "bug + facturation" ira uniquement a l'equipe technique (le premier chemin vrai).

**[ECRAN — slide "Quand utiliser Paths plutot que Branch ?"]**

- Tu veux qu'un seul chemin s'execute (routing, assignation, redirection) → **Paths**
- Tu veux que plusieurs chemins s'executent en parallele (notifications, tags, logs) → **Branch**
- Tu as un cas "par defaut" (catch-all) → **Paths** avec un dernier chemin sans condition

**[ECRAN — screencast OttoKit — test]**

[Teste avec categorie = "bug" — email envoye a support-tech@]
[Teste avec categorie = "facturation" — email envoye a facturation@]
[Teste avec categorie = "autre" — email envoye a contact@]

Un ticket, un chemin. Pas de doublon.

**[TRANSITION — face camera]**

Tu sais maintenant bloquer, adapter, segmenter et router. Il manque un dernier ingredient pour construire des workflows intelligents : le temps. Le Delay App te permet d'ajouter des pauses entre les actions.

---

**Points cles**
- Paths = un seul chemin s'execute (le premier dont la condition est vraie)
- Branch = tous les chemins vrais s'executent
- Utiliser un dernier Path sans condition comme "catch-all" (defaut)
- Ideal pour le routing : tickets, assignations, redirections

**Mots-cles SEO**
- OttoKit Paths
- router workflow OttoKit
- Branch vs Paths OttoKit
- aiguillage workflow automatisation

---

## Lecon 6.6 — Delay App : ajoute un delai dans ton workflow

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Jusqu'ici, tes workflows s'executent instantanement : trigger → actions → termine. Mais parfois, tu veux attendre. Envoyer un email de relance 3 jours apres l'achat. Demander un avis 15 jours apres la livraison. C'est le role du Delay App.

**[ECRAN — screencast OttoKit — scenario relance J+3]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Relance J+3 — demande de feedback"]
[Ajoute un trigger WooCommerce "Order Completed"]
[Fait un Fetch Data]

Notre scenario : 3 jours apres qu'une commande est marquee comme completee, tu envoies un email pour demander un retour d'experience.

**[ECRAN — screencast OttoKit — ajout du Delay App]**

[Clique sur "+" apres le trigger]
[Cherche "Delay" dans la liste des apps]
[Selectionne "Delay"]

Le Delay App a une interface tres simple. Tu definis deux choses :

1. **Duree** — le nombre
[Tape "3"]

2. **Unite** — minutes, heures, jours
[Selectionne "Days"]

C'est tout. Le workflow va attendre 3 jours a cet endroit precis avant de passer a l'action suivante.

**[ECRAN — screencast OttoKit — ajout de l'action apres le Delay]**

[Ajoute une action "Send Email" apres le Delay]
[Configure : destinataire = {billing_email}]
[Objet : "{billing_first_name}, comment s'est passe ta commande ?"]
[Corps : "Tu as recu ta commande il y a quelques jours. On aimerait avoir ton avis..."]

L'email part 3 jours apres la commande. Pas avant.

**[ECRAN — slide "Options de delai"]**

| Unite | Cas d'usage |
|---|---|
| Minutes | Notification de suivi immediate (5-10 min) |
| Heures | Rappel dans la journee (2-4h) |
| Jours | Relance post-achat, demande d'avis (3-15j) |

Le Delay accepte des valeurs entieres. Si tu veux 1 jour et 12 heures, tu peux mettre 36 heures. Ou enchacer deux Delay.

**[ECRAN — slide "Attention : le Delay n'est pas un cron"]**

Point important : le Delay attend a partir du moment ou le workflow atteint cette etape. Ce n'est pas un planificateur. Si le trigger se declenche lundi a 14h et que tu mets un Delay de 3 jours, l'action suivante s'executera jeudi a 14h.

Si tu veux qu'une action se declenche un jour precis (ex: chaque lundi a 9h), utilise le trigger Schedule qu'on a vu au Module 3. Le Delay, c'est du relatif.

**[ECRAN — screencast OttoKit — Delay dans le canvas]**

[Montre le workflow complet dans le canvas]
[Pointe le bloc Delay entre le trigger et l'action]
[Montre le badge "3 Days" affiche sur le bloc]

Dans le canvas, le bloc Delay affiche la duree. C'est visuel et lisible. Tu vois tout de suite qu'il y a une pause dans ton workflow.

**[TRANSITION — face camera]**

Le Delay, c'est simple mais puissant. Et quand tu le combines avec le Filter, le Condition et le Branch, tu peux construire des sequences completes. C'est exactement ce qu'on fait dans la prochaine lecon : un workflow de nurturing de A a Z.

---

**Points cles**
- Le Delay App met le workflow en pause pour une duree definie
- Unites : minutes, heures, jours
- Le delai est relatif (a partir du declenchement), pas absolu
- Ne pas confondre Delay (pause dans un workflow) et Schedule (trigger planifie)

**Mots-cles SEO**
- OttoKit Delay App
- delai workflow OttoKit
- email relance automatique WordPress
- temporisation automatisation OttoKit

---

## Lecon 6.7 — Combiner logique et delai : workflow complet de nurturing

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu connais le Filter, la Condition, le Branch et le Delay. Chacun fait un truc bien. Mais la vraie puissance, c'est quand tu les combines. On va construire ensemble un workflow complet de nurturing, etape par etape.

**[ECRAN — slide "Le scenario : nurturing post-inscription schoolsWP"]**

Voici le scenario qu'on va construire. Un apprenant s'inscrit a la formation gratuite schoolsWP.

1. **J+0** — Email de bienvenue immediat
2. **J+3** — Email "As-tu commence le Module 1 ?"
3. **Check** — Verification : a-t-il commence M1 ?
4. **Branche OUI** → Email "Bravo, continue avec M2"
5. **Branche NON** → Email "On est la pour t'aider" + tag "relance"
6. **J+15** — Email demande d'avis

C'est un workflow qu'on utilise chez schoolsWP. Il combine tout ce qu'on a vu dans ce module.

**[ECRAN — screencast OttoKit — etape 1 : trigger + email bienvenue]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Nurturing inscription gratuite"]
[Ajoute un trigger "User Enrolled" (TutorLMS ou equivalent)]
[Fait un Fetch Data — recupere email, prenom, cours]

[Ajoute une action "Send Email"]
[Destinataire : {student_email}]
[Objet : "{student_first_name}, bienvenue dans la formation !"]
[Corps : "Tu viens de t'inscrire. Voici comment commencer..."]

Etape 1 : des que quelqu'un s'inscrit, il recoit un email de bienvenue. C'est immediat.

**[ECRAN — screencast OttoKit — etape 2 : Delay 3 jours]**

[Ajoute un bloc Delay apres l'email]
[Configure : 3 jours]

On attend 3 jours. Pas d'action pendant ce temps.

**[ECRAN — screencast OttoKit — etape 3 : email relance M1]**

[Ajoute une action "Send Email"]
[Objet : "{student_first_name}, as-tu commence le Module 1 ?"]
[Corps : "Ca fait 3 jours que tu t'es inscrit. Le Module 1 t'attend..."]

A J+3, on envoie un email de relance. Simple et direct.

**[ECRAN — screencast OttoKit — etape 4 : Delay 1 jour + Branch]**

[Ajoute un Delay de 1 jour]

On attend encore un jour pour laisser le temps de reagir.

[Ajoute un bloc Branch apres le Delay]

[Configure la Branche 1 : "A commence"]
[Condition : verification LMS — lecon completee > 0]

[Configure la Branche 2 : "N'a pas commence"]
[Condition : lecon completee = 0]

**[ECRAN — screencast OttoKit — actions par branche]**

[Branche 1 "A commence"]
[Ajoute une action "Send Email"]
[Objet : "Bravo {student_first_name}, tu es sur la bonne voie !"]
[Corps : "Tu as commence le Module 1. Voici le Module 2..."]

Pour ceux qui ont commence : encouragement + lien vers la suite.

[Branche 2 "N'a pas commence"]
[Ajoute une action "Send Email"]
[Objet : "{student_first_name}, on est la pour t'aider"]
[Corps : "Pas encore commence ? C'est normal. Voici 3 raisons de commencer aujourd'hui..."]
[Ajoute une action "FluentCRM — Add Tag" : "relance-m1"]

Pour ceux qui n'ont pas commence : email de soutien + tag CRM pour suivi.

**[ECRAN — screencast OttoKit — etape 5 : Delay final + demande d'avis]**

[Apres les deux branches, ajoute un Delay de 11 jours]

On attend 11 jours supplementaires (J+15 au total depuis l'inscription).

[Ajoute une action "Send Email"]
[Objet : "Ton avis nous interesse, {student_first_name}"]
[Corps : "Ca fait 15 jours que tu nous as rejoint. Qu'est-ce que tu en penses ?"]

**[ECRAN — slide "Vue d'ensemble du workflow"]**

```
Trigger: Inscription formation
    │
    ├── Email bienvenue (J+0)
    │
    ├── Delay 3 jours
    │
    ├── Email "As-tu commence M1 ?" (J+3)
    │
    ├── Delay 1 jour
    │
    ├── Branch
    │   ├── A commence → Email encouragement
    │   └── N'a pas commence → Email soutien + Tag "relance-m1"
    │
    ├── Delay 11 jours
    │
    └── Email demande d'avis (J+15)
```

5 emails, 2 branches, 3 delais. Un seul workflow. Zero intervention manuelle.

**[ECRAN — screencast OttoKit — vue canvas complete]**

[Montre le workflow complet dans le canvas OttoKit]
[Pointe chaque bloc : trigger → email → delay → email → delay → branch → actions → delay → email]

[Active le workflow]

Le workflow est pret. Chaque nouvelle inscription declenche cette sequence automatiquement.

**[TRANSITION — face camera]**

Voila un workflow qui travaille pour toi 24h/24. Tu as vu comment combiner les outils du Module 6 pour creer une vraie machine de nurturing. Place au quiz pour valider tes acquis.

---

**Points cles**
- Un workflow de nurturing combine Delay, Branch et actions email
- Toujours dessiner le workflow sur papier avant de le construire
- Les Delays s'additionnent : 3j + 1j + 11j = 15 jours au total
- Le Branch permet de traiter differemment les actifs et les inactifs
- Un seul workflow remplace des heures de relance manuelle

**Mots-cles SEO**
- OttoKit workflow nurturing
- sequence email automatique OttoKit
- automatisation relance WordPress
- workflow complet OttoKit formation

---

## Notes de production — Module 6

### Captures a preparer
- Canvas OttoKit avec bloc Filter — panneau de configuration visible (operateurs, AND/OR)
- Canvas OttoKit avec bloc Condition — champs "if true" / "if false" visibles
- Canvas OttoKit avec bloc Branch — 3 branches deployees avec actions differentes
- Canvas OttoKit avec bloc Paths — interface de routing
- Canvas OttoKit avec bloc Delay — badge "3 Days" visible
- Workflow complet nurturing — vue canvas avec tous les blocs (trigger → email → delay → email → delay → branch → delay → email)
- Test Filter : commande 75 EUR passant, commande 30 EUR bloquee (vue History)
- Test Branch : 3 executions differentes selon le montant
- Slide comparatif Filter vs Condition (tableau)
- Slide comparatif Branch vs Paths (tableau)
- Slide schema nurturing (diagramme)

### Environnement de demo
- Compte OttoKit (plan premium recommande pour les workflows multi-etapes)
- Site WordPress schoolsWP avec WooCommerce (commandes de test a differents montants)
- FluentCRM installe et actif (pour les tags)
- TutorLMS ou equivalent LMS installe (pour le scenario nurturing)
- Fluent Forms avec un formulaire de support (champ categorie)
- Compte Slack avec un channel #ventes
- Google Sheets vierge pour les logs

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 6.1 | 6 min |
| 6.2 | 6 min |
| 6.3 | 6 min |
| 6.4 | 7 min |
| 6.5 | 6 min |
| 6.6 | 6 min |
| 6.7 | 8 min |
| **Total M6** | **45 min** |

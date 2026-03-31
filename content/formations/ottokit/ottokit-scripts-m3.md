# Scripts video — Module 3 : Triggers : les evenements qui declenchent tes automations

**Formation** : Maitriser OttoKit
**Module** : M3 — Triggers : les evenements qui declenchent tes automations
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~40 min de video
**Date** : 2026-03-30

---

## Lecon 3.1 — Triggers instantanes vs planifies : comprendre la difference

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs, screencast OttoKit

---

**[INTRO — face camera]**

Tous les workflows OttoKit commencent par un trigger. Mais tous les triggers ne fonctionnent pas de la meme maniere. Certains reagissent en temps reel, d'autres verifient a intervalles reguliers. Comprendre cette difference, c'est comprendre pourquoi ton workflow se declenche vite — ou pas.

**[ECRAN — slide "Deux familles de triggers"]**

OttoKit propose deux types de triggers :

1. **Triggers instantanes** — ils se declenchent en temps reel. Des que l'evenement se produit, le workflow demarre. Aucun delai.

2. **Triggers planifies (schedule)** — ils verifient a intervalles reguliers si quelque chose a change. Par defaut, toutes les 60 minutes. Si un nouvel element est detecte, le workflow se lance.

**[ECRAN — slide "Comparaison directe"]**

| | Instantane | Planifie |
|---|---|---|
| Delai | Immediat (< 1 seconde) | Jusqu'a 60 min |
| Fonctionnement | L'app envoie un signal a OttoKit | OttoKit interroge l'app |
| Exemple | Nouvelle commande WooCommerce | Nouvelle ligne Google Sheets |
| Icone OttoKit | Eclair | Horloge |
| Consomme des tasks au repos | Non | Non (seulement quand il detecte) |

**[ECRAN — screencast OttoKit]**

[Ouvre le canvas d'un workflow]
[Montre un trigger WooCommerce — pointe l'icone eclair "Instant"]
[Ouvre un second workflow avec Google Sheets — pointe l'icone horloge "Schedule"]
[Montre l'intervalle de verification dans les parametres du trigger planifie]

Comment savoir quel type tu as ? Regarde l'icone a cote du trigger dans le canvas. Un eclair = instantane. Une horloge = planifie. OttoKit l'affiche clairement.

**[ECRAN — slide "Quel impact pour toi ?"]**

En pratique :

- Si tu vends en ligne et tu veux envoyer un email de confirmation immediatement apres l'achat → il te faut un trigger instantane (WooCommerce le supporte).
- Si tu surveilles un Google Sheet pour detecter de nouvelles lignes → le delai de 60 minutes est normal. Ce n'est pas un bug, c'est le fonctionnement du trigger planifie.

Astuce : certaines apps supportent les deux types. Verifie toujours dans la liste des evenements de l'app.

**[TRANSITION — face camera]**

Maintenant que tu comprends la difference, on passe a la pratique. Dans la prochaine lecon, on configure ensemble un trigger WordPress instantane avec WooCommerce.

---

**Points cles**
- Trigger instantane = temps reel, se declenche des que l'evenement arrive
- Trigger planifie = verification periodique (par defaut toutes les 60 min)
- L'icone dans le canvas indique le type : eclair ou horloge
- Le choix du trigger impacte directement la latence de ton workflow

**Mots-cles SEO**
- OttoKit trigger instantane
- OttoKit trigger planifie
- difference trigger instant schedule OttoKit
- automatisation temps reel WordPress

---

## Lecon 3.2 — Configure un trigger WordPress (nouvelle commande WooCommerce)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

On entre dans le concret. Tu vas configurer ton premier trigger WordPress : detecter une nouvelle commande WooCommerce. C'est l'un des triggers les plus utilises, et c'est un trigger instantane.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit — app.ottokit.com]
[Clique sur "Create Workflow"]
[Donne un nom au workflow : "Nouvelle commande → notification"]

Premiere etape : on cree un nouveau workflow. Donne-lui un nom clair. C'est important pour s'y retrouver quand tu en auras 10 ou 20.

[Clique sur le bloc trigger "When this happens..."]

Le canvas s'ouvre avec un bloc trigger vide. Clique dessus.

**[ECRAN — screencast selection de l'app]**

[Dans le panneau lateral, tape "WooCommerce" dans la barre de recherche]
[Selectionne "WooCommerce"]

Tu choisis d'abord l'app. Ici, WooCommerce. OttoKit affiche la liste de toutes les apps connectees.

**[ECRAN — screencast selection de l'evenement]**

[Dans la liste des evenements, scrolle et selectionne "Order Created"]
[Pointe le badge "Instant" a cote de l'evenement]

Ensuite tu choisis l'evenement. "Order Created" — une commande est creee. Tu vois le badge "Instant" : ce trigger se declenche en temps reel.

**[ECRAN — screencast selection de la connexion]**

[Selectionne la connexion WordPress dans le dropdown]
[Si aucune connexion n'existe, montre brievement le bouton "Add Connection"]

Tu selectionnes ta connexion WordPress. C'est celle que tu as configuree dans le Module 2 quand tu as installe le plugin OttoKit sur ton site.

**[ECRAN — screencast configuration et Fetch Data]**

[Si des options supplementaires apparaissent (status de commande, etc.), montre-les]
[Clique sur le bouton "Fetch Data"]
[Attends que les donnees arrivent]
[Montre les champs retournes : order_id, billing_email, billing_first_name, total, items...]

Maintenant, l'etape la plus importante : clique sur "Fetch Data". OttoKit va chercher des donnees reelles depuis ton site. Ca te permet de voir exactement quels champs tu recevras quand une commande arrivera.

Tu vois les donnees ? order_id, billing_email, billing_first_name, total... Ce sont les champs que tu pourras utiliser dans tes actions.

[Clique sur "Save"]

On enregistre. Ton trigger est configure.

**[TRANSITION — face camera]**

Tu viens de configurer un trigger WordPress instantane. Le processus est toujours le meme : app → evenement → connexion → Fetch Data → enregistrer. Dans la prochaine lecon, on fait la meme chose avec une app SaaS.

---

**Points cles**
- Processus de configuration : app → evenement → connexion → Fetch Data → save
- WooCommerce "Order Created" est un trigger instantane
- "Fetch Data" recupere des donnees reelles pour tester
- Les champs retournes sont ceux que tu utiliseras dans les actions

**Mots-cles SEO**
- OttoKit trigger WooCommerce
- automatiser commande WooCommerce
- OttoKit WooCommerce configuration
- trigger WordPress OttoKit

---

## Lecon 3.3 — Configure un trigger SaaS (nouvelle ligne Google Sheets)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Apres un trigger WordPress, on passe a un trigger SaaS. On va detecter quand une nouvelle ligne est ajoutee dans un Google Sheet. C'est un trigger planifie — et tu vas voir la difference avec ce qu'on a fait avant.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Nouvelle ligne Sheets → action"]
[Clique sur le bloc trigger]

Meme demarche : on cree un workflow et on ouvre le bloc trigger.

**[ECRAN — screencast selection de l'app]**

[Tape "Google Sheets" dans la barre de recherche]
[Selectionne "Google Sheets"]

On selectionne Google Sheets.

**[ECRAN — screencast selection de l'evenement]**

[Selectionne "New Row Added" ou equivalent]
[Pointe le badge "Schedule" a cote de l'evenement]

L'evenement c'est "New Row Added". Regarde bien : pas d'eclair ici, mais une horloge. C'est un trigger planifie. OttoKit verifiera toutes les 60 minutes s'il y a de nouvelles lignes.

**[ECRAN — screencast connexion et configuration]**

[Selectionne la connexion Google — ou montre le bouton "Connect" si c'est la premiere fois]
[Montre la selection du spreadsheet dans le dropdown]
[Montre la selection de la feuille (sheet/tab)]

Tu selectionnes ta connexion Google, puis le spreadsheet exact, puis la feuille. OttoKit te guide etape par etape.

**[ECRAN — screencast Fetch Data]**

[Clique sur "Fetch Data"]
[Montre les champs retournes : colonnes du sheet avec leurs valeurs]

Comme avec WooCommerce, on fait un Fetch Data. Ici, OttoKit lit la derniere ligne de ton sheet et affiche les colonnes comme champs. Si ta premiere colonne s'appelle "Nom" et la deuxieme "Email", tu verras ces champs.

[Clique sur "Save"]

**[ECRAN — slide "Instant vs Schedule — ce qu'on vient de voir"]**

| WooCommerce (lecon 3.2) | Google Sheets (lecon 3.3) |
|---|---|
| Trigger instantane | Trigger planifie |
| Se declenche immediatement | Verifie toutes les 60 min |
| Badge eclair | Badge horloge |
| Meme processus de configuration | Meme processus de configuration |

Le processus est identique. La seule difference, c'est le timing.

**[TRANSITION — face camera]**

Tu sais maintenant configurer les deux types de triggers. Mais parfois, tu n'as pas besoin d'un evenement externe : tu veux que ton workflow se lance a une heure precise. C'est le Schedule App, et c'est la prochaine lecon.

---

**Points cles**
- Google Sheets "New Row Added" est un trigger planifie (toutes les 60 min)
- Le processus de configuration est le meme que pour un trigger WordPress
- La connexion Google necessite une autorisation OAuth
- Les colonnes du sheet deviennent les champs disponibles dans le workflow

**Mots-cles SEO**
- OttoKit Google Sheets trigger
- automatiser Google Sheets WordPress
- trigger planifie OttoKit
- OttoKit schedule trigger

---

## Lecon 3.4 — Schedule App : declenche un workflow a heure fixe

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Parfois, tu ne veux pas reagir a un evenement. Tu veux que ton workflow se lance automatiquement a une heure precise. Chaque lundi a 9h, envoyer un rapport. Chaque jour a 18h, sauvegarder des donnees. C'est le role du Schedule App.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Rapport hebdomadaire"]
[Clique sur le bloc trigger]
[Tape "Schedule" dans la barre de recherche]
[Selectionne "Schedule App"]

Le Schedule App n'est pas lie a un plugin ou a un service. C'est un trigger interne a OttoKit. Il remplace le cron WordPress — en mieux, parce qu'il est fiable et ne depend pas du trafic sur ton site.

**[ECRAN — screencast configuration de la recurrence]**

[Selectionne l'evenement "Schedule" ou "Recurring Schedule"]
[Montre les options de recurrence : Daily, Weekly, Monthly]
[Selectionne "Weekly"]
[Choisis le jour : "Monday"]
[Choisis l'heure : "09:00"]

Tu parametres la frequence. Ici, chaque lundi a 9h. Tu peux aussi choisir "Daily" pour tous les jours, ou "Monthly" pour une fois par mois a une date precise.

**[ECRAN — screencast fuseau horaire]**

[Montre le champ fuseau horaire / timezone]
[Selectionne "Europe/Paris"]

Attention au fuseau horaire. Par defaut, OttoKit peut utiliser UTC. Si tu es en France, selectionne "Europe/Paris" pour que 9h corresponde a 9h chez toi, pas 9h a Londres.

**[ECRAN — screencast Fetch Data et save]**

[Clique sur "Fetch Data"]
[Montre les donnees retournees : date, heure, jour de la semaine]
[Clique sur "Save"]

Le Fetch Data du Schedule App retourne la date et l'heure d'execution. Pas grand-chose, mais c'est normal : c'est un declencheur temporel, pas un evenement de donnees.

**[ECRAN — slide "Cas d'usage concrets"]**

Voici quand utiliser le Schedule App :

- **Rapport quotidien** : chaque matin, recuperer les ventes de la veille et les envoyer par email
- **Nettoyage hebdomadaire** : chaque dimanche, archiver les commandes anciennes
- **Relance mensuelle** : le 1er du mois, envoyer un recapitulatif aux clients inactifs
- **Sauvegarde** : chaque nuit, exporter des donnees vers Google Sheets
- **Veille concurrentielle** : chaque lundi, lancer un workflow de scraping

**[TRANSITION — face camera]**

Le Schedule App est ton cron WordPress fiable et visuel. Dans la prochaine lecon, on passe au trigger le plus flexible : le webhook.

---

**Points cles**
- Le Schedule App declenche un workflow a heure fixe (pas en reaction a un evenement)
- Options : quotidien, hebdomadaire, mensuel
- Toujours verifier le fuseau horaire (defaut = UTC)
- Remplace le cron WordPress de maniere fiable

**Mots-cles SEO**
- OttoKit Schedule App
- cron WordPress OttoKit
- automatiser heure fixe OttoKit
- workflow planifie OttoKit

---

## Lecon 3.5 — Webhook trigger : recois des donnees de n'importe ou

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit + outil externe

---

**[INTRO — face camera]**

Le webhook, c'est le trigger universel. N'importe quel service capable d'envoyer une requete HTTP peut declencher ton workflow OttoKit. Tu n'as pas besoin qu'il soit dans la liste des integrations.

**[ECRAN — slide "Comment ca fonctionne"]**

Le principe est simple :

1. OttoKit te genere une URL unique
2. Tu donnes cette URL a un service externe
3. Quand ce service envoie des donnees a cette URL, ton workflow se declenche

C'est un trigger instantane. Des que les donnees arrivent, le workflow demarre.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Webhook test"]
[Clique sur le bloc trigger]
[Tape "Webhook" dans la barre de recherche]
[Selectionne "Webhook / API"]
[Selectionne l'evenement "Receive Data from Webhook"]

On selectionne le trigger Webhook. OttoKit affiche immediatement une URL unique.

**[ECRAN — screencast copie de l'URL]**

[Montre l'URL generee par OttoKit]
[Selectionne et copie l'URL]

Voici ton URL webhook. Copie-la. C'est cette URL que tu vas coller dans le service externe qui doit envoyer les donnees.

**[ECRAN — screencast test avec un outil externe]**

[Ouvre un nouvel onglet avec Webhook.site ou Postman ou Reqbin — ou utilise curl]
[Colle l'URL webhook OttoKit]
[Configure une requete POST avec un payload JSON simple :]

```json
{
  "nom": "Jean Dupont",
  "email": "jean@example.com",
  "action": "inscription"
}
```

[Envoie la requete]

Pour tester, on va envoyer des donnees manuellement. Tu peux utiliser un outil comme Postman, Reqbin, ou meme la ligne de commande. L'important, c'est d'envoyer une requete POST a l'URL avec un body JSON.

**[ECRAN — screencast retour dans OttoKit]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" ou verifie que les donnees sont arrivees]
[Montre les champs recus : nom, email, action]
[Clique sur "Save"]

De retour dans OttoKit, tu vois les donnees que tu viens d'envoyer. Les champs "nom", "email" et "action" sont maintenant disponibles pour tes actions.

**[ECRAN — slide "Cas d'usage concrets"]**

Quand utiliser un webhook :

- **n8n vers OttoKit** : un workflow n8n envoie un signal quand un traitement se termine
- **Formulaire externe** : un formulaire Typeform ou Tally envoie les reponses a OttoKit
- **Service sur mesure** : ton propre script Python ou API envoie des donnees
- **Zapier vers OttoKit** : combiner deux plateformes d'automatisation
- **Stripe** : Stripe envoie un evenement de paiement directement a OttoKit

**[TRANSITION — face camera]**

Le webhook ouvre des possibilites enormes. Dans la prochaine lecon, on decouvre deux triggers plus simples mais tres pratiques : le Trigger Button et le RSS Feed.

---

**Points cles**
- Le webhook genere une URL unique qui recoit des donnees en POST
- C'est un trigger instantane — le workflow demarre immediatement
- N'importe quel service capable d'envoyer une requete HTTP peut declencher le workflow
- Toujours tester avec un envoi manuel avant de mettre en production

**Mots-cles SEO**
- OttoKit webhook trigger
- webhook WordPress automatisation
- recevoir donnees webhook OttoKit
- connecter n'importe quel service OttoKit

---

## Lecon 3.6 — Trigger Button et RSS Feed : cas d'usage pratiques

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tous les triggers ne sont pas automatiques. Parfois tu veux declencher un workflow toi-meme, en un clic depuis le dashboard. Et parfois, tu veux surveiller un flux RSS pour reagir a de nouveaux articles. On couvre les deux dans cette lecon.

**[ECRAN — screencast OttoKit — Trigger Button]**

[Cree un nouveau workflow : "Declenchement manuel"]
[Clique sur le bloc trigger]
[Tape "Button" dans la barre de recherche]
[Selectionne "Trigger Button" ou "Manual Trigger"]

Le Trigger Button te permet de lancer un workflow a la demande, directement depuis le dashboard OttoKit. Pas d'evenement externe, pas de planning. Tu cliques, ca se lance.

**[ECRAN — screencast configuration du bouton]**

[Montre les options de configuration — champs personnalises si disponibles]
[Clique sur "Save"]

La configuration est minimale. Tu n'as pas besoin de connexion externe ni de Fetch Data. Le trigger attend simplement que tu appuies sur le bouton.

**[ECRAN — screencast execution manuelle]**

[Reviens sur la liste des workflows]
[Montre le bouton "Run" ou "Execute" a cote du workflow]
[Clique dessus]
[Montre l'execution dans l'historique]

Pour lancer le workflow, tu cliques sur "Run" depuis le dashboard. Tu vois l'execution apparaitre dans l'historique.

**[ECRAN — slide "Quand utiliser le Trigger Button"]**

- **Test** : tu construis un workflow et tu veux le tester sans attendre l'evenement reel
- **Action ponctuelle** : envoyer un email de relance a une liste specifique
- **Maintenance** : lancer un nettoyage ou une synchronisation a la demande
- **Demo** : montrer un workflow a un client ou un collegue

**[ECRAN — screencast OttoKit — RSS Feed]**

[Cree un nouveau workflow : "Veille concurrentielle"]
[Clique sur le bloc trigger]
[Tape "RSS" dans la barre de recherche]
[Selectionne "RSS Feed"]
[Selectionne l'evenement "New Item in Feed"]

Le trigger RSS surveille un flux RSS. Quand un nouvel article apparait, le workflow se declenche.

**[ECRAN — screencast configuration RSS]**

[Colle une URL de flux RSS — par exemple https://wpmarmite.com/feed/]
[Montre l'intervalle de verification]
[Clique sur "Fetch Data"]
[Montre les champs retournes : title, link, description, pubDate]
[Clique sur "Save"]

Tu colles l'URL du flux RSS et OttoKit le surveille a intervalles reguliers. Le Fetch Data te montre les champs disponibles : titre de l'article, lien, description, date de publication.

**[ECRAN — slide "Cas d'usage RSS"]**

- **Veille concurrentielle** : surveiller les blogs de tes concurrents et recevoir une alerte Slack
- **Curation** : detecter de nouveaux articles dans ta niche et les ajouter dans un Google Sheet
- **Reseaux sociaux** : quand ton propre blog publie, partager automatiquement sur Twitter/X

**[TRANSITION — face camera]**

Tu connais maintenant tous les types de triggers OttoKit. Dans la prochaine lecon, on plonge dans les donnees : quand un trigger se declenche, quelles informations tu recois exactement ?

---

**Points cles**
- Trigger Button = declenchement manuel depuis le dashboard
- RSS Feed = surveillance automatique d'un flux RSS
- Le bouton est ideal pour les tests et les actions ponctuelles
- Le RSS est un trigger planifie (verification periodique)

**Mots-cles SEO**
- OttoKit trigger button
- OttoKit RSS feed automatisation
- declenchement manuel OttoKit
- veille automatisee WordPress OttoKit

---

## Lecon 3.7 — Types de donnees trigger : comprendre ce que tu recois

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Quand un trigger se declenche, il ne fait pas que lancer le workflow. Il transporte des donnees. Et ces donnees, c'est ce que tu vas utiliser dans toutes tes actions. Comprendre ce que tu recois, c'est la cle pour construire des workflows qui fonctionnent.

**[ECRAN — screencast OttoKit — workflow WooCommerce]**

[Ouvre un workflow existant avec un trigger WooCommerce "Order Created"]
[Clique sur le bloc trigger]
[Montre les donnees du Fetch Data deja charge]

Reprenons notre trigger WooCommerce. Quand une commande arrive, voici ce que tu recois :

[Pointe les champs un par un]
- `order_id` — le numero de commande
- `status` — le statut (processing, completed...)
- `total` — le montant
- `billing_first_name`, `billing_last_name` — le nom du client
- `billing_email` — son email
- `billing_phone` — son telephone
- `line_items` — les produits commandes

Chaque trigger a sa propre structure de donnees. Un trigger WooCommerce ne renvoie pas les memes champs qu'un trigger Google Sheets.

**[ECRAN — screencast OttoKit — workflow Google Sheets]**

[Ouvre un workflow avec un trigger Google Sheets "New Row Added"]
[Montre les donnees du Fetch Data]

Avec Google Sheets, les champs correspondent aux colonnes de ton tableur. Si ta feuille a les colonnes "Nom", "Email", "Telephone", ce sont ces champs que tu retrouves.

[Pointe les champs : column_a / nom, column_b / email, etc.]

**[ECRAN — slide "Le role du Fetch Data"]**

Le bouton "Fetch Data" fait deux choses :

1. **Il teste la connexion** — il verifie que le trigger peut acceder a l'app
2. **Il charge des donnees exemples** — il recupere des donnees reelles pour que tu voies les champs disponibles

Sans Fetch Data, tu ne sais pas quels champs tu peux utiliser dans tes actions. C'est pour ca qu'il faut toujours le faire.

**[ECRAN — screencast OttoKit — utilisation des champs dans une action]**

[Ajoute une action "Send Email" apres le trigger WooCommerce]
[Dans le champ "To", montre le selecteur de donnees dynamiques]
[Selectionne "billing_email" depuis les donnees du trigger]
[Dans le champ "Subject", tape "Merci pour ta commande #" et selectionne "order_id"]
[Dans le corps de l'email, selectionne "billing_first_name"]

Voici comment tu utilises les donnees du trigger. Dans chaque champ d'une action, tu peux inserer des valeurs dynamiques issues du trigger. Tu cliques sur le selecteur et tu choisis le champ.

"billing_email" pour l'adresse du destinataire. "order_id" pour le numero de commande dans l'objet. "billing_first_name" pour personnaliser le message.

**[ECRAN — slide "Conseils pratiques"]**

- Fais toujours un Fetch Data avant de configurer tes actions
- Si le Fetch Data ne retourne rien, verifie qu'il y a des donnees recentes dans l'app source
- Les noms de champs peuvent varier entre les apps — lis-les attentivement
- Certains champs sont des objets imbriques (comme line_items) — tu peux acceder aux sous-champs

**[TRANSITION — face camera]**

Tu sais maintenant comment fonctionnent les triggers, comment les configurer, et comment exploiter les donnees qu'ils transportent. Le Module 3 est termine. Passe au quiz pour valider tes acquis avant d'attaquer le Module 4 sur les actions.

---

**Points cles**
- Chaque trigger transporte des donnees specifiques a l'app et a l'evenement
- "Fetch Data" charge des donnees reelles pour voir les champs disponibles
- Les champs du trigger sont utilisables dans toutes les actions du workflow
- Toujours faire un Fetch Data avant de configurer les actions

**Mots-cles SEO**
- OttoKit donnees trigger
- data mapping OttoKit
- Fetch Data OttoKit
- champs dynamiques OttoKit workflow

---

## Notes de production — Module 3

### Captures a preparer
- Canvas OttoKit avec trigger WooCommerce — badge "Instant" visible
- Canvas OttoKit avec trigger Google Sheets — badge "Schedule" visible
- Configuration Schedule App — ecran recurrence + fuseau horaire
- URL webhook generee par OttoKit — panneau de configuration
- Outil de test webhook (Postman ou Reqbin) avec payload JSON
- Trigger Button — bouton "Run" sur le dashboard
- Configuration RSS Feed — URL + Fetch Data
- Panneau Fetch Data avec champs retournes (WooCommerce + Google Sheets)
- Selecteur de donnees dynamiques dans une action email

### Environnement de demo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec WooCommerce installe (au moins 1 commande de test)
- Google Sheet avec quelques lignes de donnees (colonnes : Nom, Email, Telephone)
- Outil de test HTTP (Postman, Reqbin, ou curl)
- Flux RSS actif (ex: blog schoolsWP ou WPMarmite)

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 3.1 | 6 min |
| 3.2 | 6 min |
| 3.3 | 5 min |
| 3.4 | 6 min |
| 3.5 | 7 min |
| 3.6 | 5 min |
| 3.7 | 5 min |
| **Total M3** | **40 min** |

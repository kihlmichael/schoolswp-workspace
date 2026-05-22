# Scripts vidéo — Module 3 : Triggers : les événements qui déclenchent tes automations

**Formation** : Maîtriser OttoKit
**Module** : M3 — Triggers : les événements qui déclenchent tes automations
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~40 min de vidéo
**Date** : 2026-03-30

---

## Leçon 3.1 — Triggers instantanés vs planifiés : comprendre la différence

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs, screencast OttoKit

---

**[INTRO — face caméra]**

Tous les workflows OttoKit commencent par un trigger. Mais tous les triggers ne fonctionnent pas de la même manière. Certains réagissent en temps réel, d'autres vérifient à intervalles réguliers. Comprendre cette différence, c'est comprendre pourquoi ton workflow se déclenche vite — ou pas.

**[ÉCRAN — slide "Deux familles de triggers"]**

OttoKit propose deux types de triggers :

1. **Triggers instantanés** — ils se déclenchent en temps réel. Dès que l'événement se produit, le workflow démarre. Aucun délai.

2. **Triggers planifiés (schedule)** — ils vérifient à intervalles réguliers si quelque chose a changé. Par défaut, toutes les 60 minutes. Si un nouvel élément est détecté, le workflow se lance.

**[ÉCRAN — slide "Comparaison directe"]**

| | Instantané | Planifié |
|---|---|---|
| Délai | Immédiat (< 1 seconde) | Jusqu'à 60 min |
| Fonctionnement | L'app envoie un signal à OttoKit | OttoKit interroge l'app |
| Exemple | Nouvelle commande WooCommerce | Nouvelle ligne Google Sheets |
| Icône OttoKit | Éclair | Horloge |
| Consomme des tasks au repos | Non | Non (seulement quand il détecte) |

**[ÉCRAN — screencast OttoKit]**

[Ouvre le canvas d'un workflow]
[Montre un trigger WooCommerce — pointe l'icône éclair "Instant"]
[Ouvre un second workflow avec Google Sheets — pointe l'icône horloge "Schedule"]
[Montre l'intervalle de vérification dans les paramètres du trigger planifié]

Comment savoir quel type tu as ? Regarde l'icône à côté du trigger dans le canvas. Un éclair = instantané. Une horloge = planifié. OttoKit l'affiche clairement.

**[ÉCRAN — slide "Quel impact pour toi ?"]**

En pratique :

- Si tu vends en ligne et tu veux envoyer un email de confirmation immédiatement après l'achat → il te faut un trigger instantané (WooCommerce le supporte).
- Si tu surveilles un Google Sheet pour détecter de nouvelles lignes → le délai de 60 minutes est normal. Ce n'est pas un bug, c'est le fonctionnement du trigger planifié.

Astuce : certaines apps supportent les deux types. Vérifie toujours dans la liste des événements de l'app.

**[TRANSITION — face caméra]**

Maintenant que tu comprends la différence, on passe à la pratique. Dans la prochaine leçon, on configure ensemble un trigger WordPress instantané avec WooCommerce.

---

**Points clés**
- Trigger instantané = temps réel, se déclenche dès que l'événement arrive
- Trigger planifié = vérification périodique (par défaut toutes les 60 min)
- L'icône dans le canvas indique le type : éclair ou horloge
- Le choix du trigger impacte directement la latence de ton workflow

**Mots-clés SEO**
- OttoKit trigger instantané
- OttoKit trigger planifié
- différence trigger instant schedule OttoKit
- automatisation temps réel WordPress

---

## Leçon 3.2 — Configure un trigger WordPress (nouvelle commande WooCommerce)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

On entre dans le concret. Tu vas configurer ton premier trigger WordPress : détecter une nouvelle commande WooCommerce. C'est l'un des triggers les plus utilisés, et c'est un trigger instantané.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit — app.ottokit.com]
[Clique sur "Create Workflow"]
[Donne un nom au workflow : "Nouvelle commande → notification"]

Première étape : on crée un nouveau workflow. Donne-lui un nom clair. C'est important pour s'y retrouver quand tu en auras 10 ou 20.

[Clique sur le bloc trigger "When this happens..."]

Le canvas s'ouvre avec un bloc trigger vide. Clique dessus.

**[ÉCRAN — screencast sélection de l'app]**

[Dans le panneau latéral, tape "WooCommerce" dans la barre de recherche]
[Sélectionne "WooCommerce"]

Tu choisis d'abord l'app. Ici, WooCommerce. OttoKit affiche la liste de toutes les apps connectées.

**[ÉCRAN — screencast sélection de l'événement]**

[Dans la liste des événements, scrolle et sélectionne "Order Created"]
[Pointe le badge "Instant" à côté de l'événement]

Ensuite tu choisis l'événement. "Order Created" — une commande est créée. Tu vois le badge "Instant" : ce trigger se déclenche en temps réel.

**[ÉCRAN — screencast sélection de la connexion]**

[Sélectionne la connexion WordPress dans le dropdown]
[Si aucune connexion n'existe, montre brièvement le bouton "Add Connection"]

Tu sélectionnes ta connexion WordPress. C'est celle que tu as configurée dans le Module 2 quand tu as installé le plugin OttoKit sur ton site.

**[ÉCRAN — screencast configuration et Fetch Data]**

[Si des options supplémentaires apparaissent (status de commande, etc.), montre-les]
[Clique sur le bouton "Fetch Data"]
[Attends que les données arrivent]
[Montre les champs retournés : order_id, billing_email, billing_first_name, total, items...]

Maintenant, l'étape la plus importante : clique sur "Fetch Data". OttoKit va chercher des données réelles depuis ton site. Ça te permet de voir exactement quels champs tu recevras quand une commande arrivera.

Tu vois les données ? order_id, billing_email, billing_first_name, total... Ce sont les champs que tu pourras utiliser dans tes actions.

[Clique sur "Save"]

On enregistre. Ton trigger est configuré.

**[TRANSITION — face caméra]**

Tu viens de configurer un trigger WordPress instantané. Le processus est toujours le même : app → événement → connexion → Fetch Data → enregistrer. Dans la prochaine leçon, on fait la même chose avec une app SaaS.

---

**Points clés**
- Processus de configuration : app → événement → connexion → Fetch Data → save
- WooCommerce "Order Created" est un trigger instantané
- "Fetch Data" récupère des données réelles pour tester
- Les champs retournés sont ceux que tu utiliseras dans les actions

**Mots-clés SEO**
- OttoKit trigger WooCommerce
- automatiser commande WooCommerce
- OttoKit WooCommerce configuration
- trigger WordPress OttoKit

---

## Leçon 3.3 — Configure un trigger SaaS (nouvelle ligne Google Sheets)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Après un trigger WordPress, on passe à un trigger SaaS. On va détecter quand une nouvelle ligne est ajoutée dans un Google Sheet. C'est un trigger planifié — et tu vas voir la différence avec ce qu'on a fait avant.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Nouvelle ligne Sheets → action"]
[Clique sur le bloc trigger]

Même démarche : on crée un workflow et on ouvre le bloc trigger.

**[ÉCRAN — screencast sélection de l'app]**

[Tape "Google Sheets" dans la barre de recherche]
[Sélectionne "Google Sheets"]

On sélectionne Google Sheets.

**[ÉCRAN — screencast sélection de l'événement]**

[Sélectionne "New Row Added" ou équivalent]
[Pointe le badge "Schedule" à côté de l'événement]

L'événement c'est "New Row Added". Regarde bien : pas d'éclair ici, mais une horloge. C'est un trigger planifié. OttoKit vérifiera toutes les 60 minutes s'il y a de nouvelles lignes.

**[ÉCRAN — screencast connexion et configuration]**

[Sélectionne la connexion Google — ou montre le bouton "Connect" si c'est la première fois]
[Montre la sélection du spreadsheet dans le dropdown]
[Montre la sélection de la feuille (sheet/tab)]

Tu sélectionnes ta connexion Google, puis le spreadsheet exact, puis la feuille. OttoKit te guide étape par étape.

**[ÉCRAN — screencast Fetch Data]**

[Clique sur "Fetch Data"]
[Montre les champs retournés : colonnes du sheet avec leurs valeurs]

Comme avec WooCommerce, on fait un Fetch Data. Ici, OttoKit lit la dernière ligne de ton sheet et affiche les colonnes comme champs. Si ta première colonne s'appelle "Nom" et la deuxième "Email", tu verras ces champs.

[Clique sur "Save"]

**[ÉCRAN — slide "Instant vs Schedule — ce qu'on vient de voir"]**

| WooCommerce (leçon 3.2) | Google Sheets (leçon 3.3) |
|---|---|
| Trigger instantané | Trigger planifié |
| Se déclenche immédiatement | Vérifie toutes les 60 min |
| Badge éclair | Badge horloge |
| Même processus de configuration | Même processus de configuration |

Le processus est identique. La seule différence, c'est le timing.

**[TRANSITION — face caméra]**

Tu sais maintenant configurer les deux types de triggers. Mais parfois, tu n'as pas besoin d'un événement externe : tu veux que ton workflow se lance à une heure précise. C'est le Schedule App, et c'est la prochaine leçon.

---

**Points clés**
- Google Sheets "New Row Added" est un trigger planifié (toutes les 60 min)
- Le processus de configuration est le même que pour un trigger WordPress
- La connexion Google nécessite une autorisation OAuth
- Les colonnes du sheet deviennent les champs disponibles dans le workflow

**Mots-clés SEO**
- OttoKit Google Sheets trigger
- automatiser Google Sheets WordPress
- trigger planifié OttoKit
- OttoKit schedule trigger

---

## Leçon 3.4 — Schedule App : déclenche un workflow à heure fixe

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Parfois, tu ne veux pas réagir à un événement. Tu veux que ton workflow se lance automatiquement à une heure précise. Chaque lundi à 9h, envoyer un rapport. Chaque jour à 18h, sauvegarder des données. C'est le rôle du Schedule App.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Rapport hebdomadaire"]
[Clique sur le bloc trigger]
[Tape "Schedule" dans la barre de recherche]
[Sélectionne "Schedule App"]

Le Schedule App n'est pas lié à un plugin ou à un service. C'est un trigger interne à OttoKit. Il remplace le cron WordPress — en mieux, parce qu'il est fiable et ne dépend pas du trafic sur ton site.

**[ÉCRAN — screencast configuration de la récurrence]**

[Sélectionne l'événement "Schedule" ou "Recurring Schedule"]
[Montre les options de récurrence : Daily, Weekly, Monthly]
[Sélectionne "Weekly"]
[Choisis le jour : "Monday"]
[Choisis l'heure : "09:00"]

Tu paramètres la fréquence. Ici, chaque lundi à 9h. Tu peux aussi choisir "Daily" pour tous les jours, ou "Monthly" pour une fois par mois à une date précise.

**[ÉCRAN — screencast fuseau horaire]**

[Montre le champ fuseau horaire / timezone]
[Sélectionne "Europe/Paris"]

Attention au fuseau horaire. Par défaut, OttoKit peut utiliser UTC. Si tu es en France, sélectionne "Europe/Paris" pour que 9h corresponde à 9h chez toi, pas 9h à Londres.

**[ÉCRAN — screencast Fetch Data et save]**

[Clique sur "Fetch Data"]
[Montre les données retournées : date, heure, jour de la semaine]
[Clique sur "Save"]

Le Fetch Data du Schedule App retourne la date et l'heure d'exécution. Pas grand-chose, mais c'est normal : c'est un déclencheur temporel, pas un événement de données.

**[ÉCRAN — slide "Cas d'usage concrets"]**

Voici quand utiliser le Schedule App :

- **Rapport quotidien** : chaque matin, récupérer les ventes de la veille et les envoyer par email
- **Nettoyage hebdomadaire** : chaque dimanche, archiver les commandes anciennes
- **Relance mensuelle** : le 1er du mois, envoyer un récapitulatif aux clients inactifs
- **Sauvegarde** : chaque nuit, exporter des données vers Google Sheets
- **Veille concurrentielle** : chaque lundi, lancer un workflow de scraping

**[TRANSITION — face caméra]**

Le Schedule App est ton cron WordPress fiable et visuel. Dans la prochaine leçon, on passe au trigger le plus flexible : le webhook.

---

**Points clés**
- Le Schedule App déclenche un workflow à heure fixe (pas en réaction à un événement)
- Options : quotidien, hebdomadaire, mensuel
- Toujours vérifier le fuseau horaire (défaut = UTC)
- Remplace le cron WordPress de manière fiable

**Mots-clés SEO**
- OttoKit Schedule App
- cron WordPress OttoKit
- automatiser heure fixe OttoKit
- workflow planifié OttoKit

---

## Leçon 3.5 — Webhook trigger : reçois des données de n'importe où

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit + outil externe

---

**[INTRO — face caméra]**

Le webhook, c'est le trigger universel. N'importe quel service capable d'envoyer une requête HTTP peut déclencher ton workflow OttoKit. Tu n'as pas besoin qu'il soit dans la liste des intégrations.

**[ÉCRAN — slide "Comment ça fonctionne"]**

Le principe est simple :

1. OttoKit te génère une URL unique
2. Tu donnes cette URL à un service externe
3. Quand ce service envoie des données à cette URL, ton workflow se déclenche

C'est un trigger instantané. Dès que les données arrivent, le workflow démarre.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Webhook test"]
[Clique sur le bloc trigger]
[Tape "Webhook" dans la barre de recherche]
[Sélectionne "Webhook / API"]
[Sélectionne l'événement "Receive Data from Webhook"]

On sélectionne le trigger Webhook. OttoKit affiche immédiatement une URL unique.

**[ÉCRAN — screencast copie de l'URL]**

[Montre l'URL générée par OttoKit]
[Sélectionne et copie l'URL]

Voici ton URL webhook. Copie-la. C'est cette URL que tu vas coller dans le service externe qui doit envoyer les données.

**[ÉCRAN — screencast test avec un outil externe]**

[Ouvre un nouvel onglet avec Webhook.site ou Postman ou Reqbin — ou utilise curl]
[Colle l'URL webhook OttoKit]
[Configure une requête POST avec un payload JSON simple :]

```json
{
  "nom": "Jean Dupont",
  "email": "jean@example.com",
  "action": "inscription"
}
```

[Envoie la requête]

Pour tester, on va envoyer des données manuellement. Tu peux utiliser un outil comme Postman, Reqbin, ou même la ligne de commande. L'important, c'est d'envoyer une requête POST à l'URL avec un body JSON.

**[ÉCRAN — screencast retour dans OttoKit]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" ou vérifie que les données sont arrivées]
[Montre les champs reçus : nom, email, action]
[Clique sur "Save"]

De retour dans OttoKit, tu vois les données que tu viens d'envoyer. Les champs "nom", "email" et "action" sont maintenant disponibles pour tes actions.

**[ÉCRAN — slide "Cas d'usage concrets"]**

Quand utiliser un webhook :

- **n8n vers OttoKit** : un workflow n8n envoie un signal quand un traitement se termine
- **Formulaire externe** : un formulaire Typeform ou Tally envoie les réponses à OttoKit
- **Service sur mesure** : ton propre script Python ou API envoie des données
- **Zapier vers OttoKit** : combiner deux plateformes d'automatisation
- **Stripe** : Stripe envoie un événement de paiement directement à OttoKit

**[TRANSITION — face caméra]**

Le webhook ouvre des possibilités énormes. Dans la prochaine leçon, on découvre deux triggers plus simples mais très pratiques : le Trigger Button et le RSS Feed.

---

**Points clés**
- Le webhook génère une URL unique qui reçoit des données en POST
- C'est un trigger instantané — le workflow démarre immédiatement
- N'importe quel service capable d'envoyer une requête HTTP peut déclencher le workflow
- Toujours tester avec un envoi manuel avant de mettre en production

**Mots-clés SEO**
- OttoKit webhook trigger
- webhook WordPress automatisation
- recevoir données webhook OttoKit
- connecter n'importe quel service OttoKit

---

## Leçon 3.6 — Trigger Button et RSS Feed : cas d'usage pratiques

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Tous les triggers ne sont pas automatiques. Parfois tu veux déclencher un workflow toi-même, en un clic depuis le dashboard. Et parfois, tu veux surveiller un flux RSS pour réagir à de nouveaux articles. On couvre les deux dans cette leçon.

**[ÉCRAN — screencast OttoKit — Trigger Button]**

[Crée un nouveau workflow : "Déclenchement manuel"]
[Clique sur le bloc trigger]
[Tape "Button" dans la barre de recherche]
[Sélectionne "Trigger Button" ou "Manual Trigger"]

Le Trigger Button te permet de lancer un workflow à la demande, directement depuis le dashboard OttoKit. Pas d'événement externe, pas de planning. Tu cliques, ça se lance.

**[ÉCRAN — screencast configuration du bouton]**

[Montre les options de configuration — champs personnalisés si disponibles]
[Clique sur "Save"]

La configuration est minimale. Tu n'as pas besoin de connexion externe ni de Fetch Data. Le trigger attend simplement que tu appuies sur le bouton.

**[ÉCRAN — screencast exécution manuelle]**

[Reviens sur la liste des workflows]
[Montre le bouton "Run" ou "Execute" à côté du workflow]
[Clique dessus]
[Montre l'exécution dans l'historique]

Pour lancer le workflow, tu cliques sur "Run" depuis le dashboard. Tu vois l'exécution apparaître dans l'historique.

**[ÉCRAN — slide "Quand utiliser le Trigger Button"]**

- **Test** : tu construis un workflow et tu veux le tester sans attendre l'événement réel
- **Action ponctuelle** : envoyer un email de relance à une liste spécifique
- **Maintenance** : lancer un nettoyage ou une synchronisation à la demande
- **Démo** : montrer un workflow à un client ou un collègue

**[ÉCRAN — screencast OttoKit — RSS Feed]**

[Crée un nouveau workflow : "Veille concurrentielle"]
[Clique sur le bloc trigger]
[Tape "RSS" dans la barre de recherche]
[Sélectionne "RSS Feed"]
[Sélectionne l'événement "New Item in Feed"]

Le trigger RSS surveille un flux RSS. Quand un nouvel article apparaît, le workflow se déclenche.

**[ÉCRAN — screencast configuration RSS]**

[Colle une URL de flux RSS — par exemple https://wpmarmite.com/feed/]
[Montre l'intervalle de vérification]
[Clique sur "Fetch Data"]
[Montre les champs retournés : title, link, description, pubDate]
[Clique sur "Save"]

Tu colles l'URL du flux RSS et OttoKit le surveille à intervalles réguliers. Le Fetch Data te montre les champs disponibles : titre de l'article, lien, description, date de publication.

**[ÉCRAN — slide "Cas d'usage RSS"]**

- **Veille concurrentielle** : surveiller les blogs de tes concurrents et recevoir une alerte Slack
- **Curation** : détecter de nouveaux articles dans ta niche et les ajouter dans un Google Sheet
- **Réseaux sociaux** : quand ton propre blog publie, partager automatiquement sur Twitter/X

**[TRANSITION — face caméra]**

Tu connais maintenant tous les types de triggers OttoKit. Dans la prochaine leçon, on plonge dans les données : quand un trigger se déclenche, quelles informations tu reçois exactement ?

---

**Points clés**
- Trigger Button = déclenchement manuel depuis le dashboard
- RSS Feed = surveillance automatique d'un flux RSS
- Le bouton est idéal pour les tests et les actions ponctuelles
- Le RSS est un trigger planifié (vérification périodique)

**Mots-clés SEO**
- OttoKit trigger button
- OttoKit RSS feed automatisation
- déclenchement manuel OttoKit
- veille automatisée WordPress OttoKit

---

## Leçon 3.7 — Types de données trigger : comprendre ce que tu reçois

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Quand un trigger se déclenche, il ne fait pas que lancer le workflow. Il transporte des données. Et ces données, c'est ce que tu vas utiliser dans toutes tes actions. Comprendre ce que tu reçois, c'est la clé pour construire des workflows qui fonctionnent.

**[ÉCRAN — screencast OttoKit — workflow WooCommerce]**

[Ouvre un workflow existant avec un trigger WooCommerce "Order Created"]
[Clique sur le bloc trigger]
[Montre les données du Fetch Data déjà chargé]

Reprenons notre trigger WooCommerce. Quand une commande arrive, voici ce que tu reçois :

[Pointe les champs un par un]
- `order_id` — le numéro de commande
- `status` — le statut (processing, completed...)
- `total` — le montant
- `billing_first_name`, `billing_last_name` — le nom du client
- `billing_email` — son email
- `billing_phone` — son téléphone
- `line_items` — les produits commandés

Chaque trigger a sa propre structure de données. Un trigger WooCommerce ne renvoie pas les mêmes champs qu'un trigger Google Sheets.

**[ÉCRAN — screencast OttoKit — workflow Google Sheets]**

[Ouvre un workflow avec un trigger Google Sheets "New Row Added"]
[Montre les données du Fetch Data]

Avec Google Sheets, les champs correspondent aux colonnes de ton tableur. Si ta feuille a les colonnes "Nom", "Email", "Téléphone", ce sont ces champs que tu retrouves.

[Pointe les champs : column_a / nom, column_b / email, etc.]

**[ÉCRAN — slide "Le rôle du Fetch Data"]**

Le bouton "Fetch Data" fait deux choses :

1. **Il teste la connexion** — il vérifie que le trigger peut accéder à l'app
2. **Il charge des données exemples** — il récupère des données réelles pour que tu voies les champs disponibles

Sans Fetch Data, tu ne sais pas quels champs tu peux utiliser dans tes actions. C'est pour ça qu'il faut toujours le faire.

**[ÉCRAN — screencast OttoKit — utilisation des champs dans une action]**

[Ajoute une action "Send Email" après le trigger WooCommerce]
[Dans le champ "To", montre le sélecteur de données dynamiques]
[Sélectionne "billing_email" depuis les données du trigger]
[Dans le champ "Subject", tape "Merci pour ta commande #" et sélectionne "order_id"]
[Dans le corps de l'email, sélectionne "billing_first_name"]

Voici comment tu utilises les données du trigger. Dans chaque champ d'une action, tu peux insérer des valeurs dynamiques issues du trigger. Tu cliques sur le sélecteur et tu choisis le champ.

"billing_email" pour l'adresse du destinataire. "order_id" pour le numéro de commande dans l'objet. "billing_first_name" pour personnaliser le message.

**[ÉCRAN — slide "Conseils pratiques"]**

- Fais toujours un Fetch Data avant de configurer tes actions
- Si le Fetch Data ne retourne rien, vérifie qu'il y a des données récentes dans l'app source
- Les noms de champs peuvent varier entre les apps — lis-les attentivement
- Certains champs sont des objets imbriqués (comme line_items) — tu peux accéder aux sous-champs

**[TRANSITION — face caméra]**

Tu sais maintenant comment fonctionnent les triggers, comment les configurer, et comment exploiter les données qu'ils transportent. Le Module 3 est terminé. Passe au quiz pour valider tes acquis avant d'attaquer le Module 4 sur les actions.

---

**Points clés**
- Chaque trigger transporte des données spécifiques à l'app et à l'événement
- "Fetch Data" charge des données réelles pour voir les champs disponibles
- Les champs du trigger sont utilisables dans toutes les actions du workflow
- Toujours faire un Fetch Data avant de configurer les actions

**Mots-clés SEO**
- OttoKit données trigger
- data mapping OttoKit
- Fetch Data OttoKit
- champs dynamiques OttoKit workflow

---

## Notes de production — Module 3

### Captures à préparer
- Canvas OttoKit avec trigger WooCommerce — badge "Instant" visible
- Canvas OttoKit avec trigger Google Sheets — badge "Schedule" visible
- Configuration Schedule App — écran récurrence + fuseau horaire
- URL webhook générée par OttoKit — panneau de configuration
- Outil de test webhook (Postman ou Reqbin) avec payload JSON
- Trigger Button — bouton "Run" sur le dashboard
- Configuration RSS Feed — URL + Fetch Data
- Panneau Fetch Data avec champs retournés (WooCommerce + Google Sheets)
- Sélecteur de données dynamiques dans une action email

### Environnement de démo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec WooCommerce installé (au moins 1 commande de test)
- Google Sheet avec quelques lignes de données (colonnes : Nom, Email, Téléphone)
- Outil de test HTTP (Postman, Reqbin, ou curl)
- Flux RSS actif (ex: blog schoolsWP ou WPMarmite)

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 3.1 | 6 min |
| 3.2 | 6 min |
| 3.3 | 5 min |
| 3.4 | 6 min |
| 3.5 | 7 min |
| 3.6 | 5 min |
| 3.7 | 5 min |
| **Total M3** | **40 min** |

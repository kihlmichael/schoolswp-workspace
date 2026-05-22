# Scripts vidéo — Module 10 : Webhooks et API : connecter n'importe quel service

**Formation** : Maîtriser OttoKit
**Module** : M10 — Webhooks et API : connecter n'importe quel service
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~45 min de vidéo
**Date** : 2026-03-30

---

## Leçon 10.1 — Webhooks : le pont universel entre les outils

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides explicatifs, schéma animé

---

**[INTRO — face caméra]**

OttoKit propose plus de 1 300 intégrations natives. Mais ton outil préféré n'est peut-être pas dans la liste. Ou alors, tu veux connecter ton propre script, ton propre API, ton propre système. C'est exactement le rôle des webhooks.

**[ÉCRAN — slide "Le problème"]**

Imagine : tu utilises un outil de facturation français, un CRM sur mesure, ou un script Python qui tourne sur ton serveur. Aucun de ces outils n'a d'intégration native dans OttoKit. Sans webhook, tu es bloqué.

**[ÉCRAN — slide "Webhook = messagerie entre deux outils"]**

Un webhook, c'est une URL. Un outil envoie des données à cette URL. L'autre outil les reçoit et agit. Pas de câble, pas de plugin, pas de configuration complexe. Une simple adresse web suffit.

Concrètement :

1. **L'outil A** génère un événement (un paiement, un formulaire soumis, un article créé)
2. **L'outil A** envoie les données à une URL (le webhook)
3. **L'outil B** reçoit les données et exécute une action

C'est une communication à sens unique : un outil parle, l'autre écoute.

**[ÉCRAN — schéma animé "Anatomie d'un webhook"]**

Un webhook transporte trois éléments :

- **L'URL** : l'adresse où envoyer les données. OttoKit la génère automatiquement.
- **Le payload** : les données elles-mêmes, en format JSON. C'est le contenu du message.
- **Les headers** : des informations supplémentaires — le type de contenu, un secret de sécurité, une signature.

```json
{
  "event": "order_created",
  "customer_email": "jean@example.com",
  "total": 49.90,
  "product": "Formation WordPress"
}
```

Voici un payload type. C'est du JSON — des paires clé/valeur. Quand OttoKit reçoit ce payload, il peut utiliser chaque champ dans les actions du workflow.

**[ÉCRAN — slide "Deux directions"]**

Les webhooks fonctionnent dans deux sens :

| Direction | Ce que ça fait | Exemple |
|---|---|---|
| **Webhook entrant** | OttoKit reçoit des données | Stripe envoie un paiement → OttoKit déclenche un workflow |
| **Webhook sortant** | OttoKit envoie des données | OttoKit notifie ton serveur qu'un utilisateur s'est inscrit |

Dans les prochaines leçons, on voit les deux.

**[ÉCRAN — slide "Webhook vs API"]**

Dernière distinction importante :

- **Webhook** = l'outil externe envoie des données à OttoKit quand un événement se produit. C'est du push.
- **API App** = OttoKit va chercher des données ou envoie des commandes à un service externe. C'est du pull (ou du push à la demande).

Les deux sont complémentaires. On couvre l'API App dans la leçon 10.3.

**[TRANSITION — face caméra]**

Tu comprends maintenant le mécanisme. Dans la prochaine leçon, on passe à la pratique : tu vas créer ton premier webhook entrant et recevoir des données en temps réel dans OttoKit.

---

**Points clés**
- Un webhook est une URL qui reçoit ou envoie des données entre deux outils
- Le payload est au format JSON (paires clé/valeur)
- Webhook entrant = OttoKit reçoit ; webhook sortant = OttoKit envoie
- Les webhooks permettent de connecter des outils qui n'ont pas d'intégration native

**Mots-clés SEO**
- OttoKit webhook
- webhook WordPress automatisation
- connecter API OttoKit
- webhook entrant sortant OttoKit

---

## Leçon 10.2 — Webhook entrant : OttoKit reçoit des données

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit + Postman

---

**[INTRO — face caméra]**

On met les mains dedans. Tu vas créer un webhook dans OttoKit, puis lui envoyer des données depuis Postman. À la fin de cette leçon, tu auras un workflow qui se déclenche quand un service externe lui parle.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit — app.ottokit.com]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Webhook entrant — test"]
[Clique sur le bloc trigger "When this happens..."]

On commence par créer un workflow et ouvrir le bloc trigger.

**[ÉCRAN — screencast sélection du trigger webhook]**

[Dans le panneau latéral, tape "Webhook" dans la barre de recherche]
[Sélectionne "Webhook / API"]
[Sélectionne l'événement "Receive Data from Webhook"]

Tu choisis le trigger "Receive Data from Webhook". C'est le webhook entrant : OttoKit attend que quelqu'un lui envoie des données.

**[ÉCRAN — screencast URL générée]**

[Montre l'URL webhook générée par OttoKit]
[Sélectionne l'URL et la copie]

OttoKit te génère une URL unique. C'est ton adresse webhook. Copie-la. N'importe quel outil capable d'envoyer une requête HTTP POST peut utiliser cette URL.

**[ÉCRAN — screencast Postman]**

[Ouvre Postman dans un nouvel onglet]
[Crée une nouvelle requête]
[Sélectionne la méthode "POST"]
[Colle l'URL webhook OttoKit dans le champ URL]
[Va dans l'onglet "Body" > sélectionne "raw" > sélectionne "JSON"]
[Tape le payload suivant :]

```json
{
  "nom": "Marie Dupont",
  "email": "marie@schoolswp.com",
  "formation": "Maîtriser OttoKit",
  "montant": 97
}
```

[Clique sur "Send"]
[Montre la réponse 200 OK]

On utilise Postman pour simuler un service externe. On envoie une requête POST avec un body JSON. Le code 200 confirme qu'OttoKit a bien reçu les données.

Si tu n'as pas Postman, tu peux aussi utiliser Reqbin (gratuit, dans le navigateur) ou curl en ligne de commande.

**[ÉCRAN — screencast retour OttoKit]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" dans le panneau du trigger]
[Montre les champs reçus : nom, email, formation, montant]

De retour dans OttoKit, clique sur "Fetch Data". Tu vois les champs que tu viens d'envoyer : nom, email, formation, montant. Ce sont ces champs que tu pourras utiliser dans toutes les actions de ton workflow.

**[ÉCRAN — screencast ajout d'une action rapide]**

[Ajoute une action "Send Email" après le trigger]
[Dans le champ "To", sélectionne le champ dynamique "email"]
[Dans le champ "Subject", tape "Bienvenue dans {{formation}}"]
[Dans le corps, tape "Bonjour {{nom}}, merci pour ton inscription !"]
[Clique sur "Save"]

Pour vérifier que tout fonctionne, on ajoute une action email. On injecte les champs du webhook directement dans l'email. Chaque valeur du payload devient une variable utilisable.

**[ÉCRAN — screencast activation du workflow]**

[Active le workflow (toggle ON)]
[Reviens dans Postman]
[Renvoie la même requête]
[Reviens dans OttoKit > History]
[Montre l'exécution réussie avec le détail des données]

On active le workflow et on renvoie la requête. Dans l'historique, tu vois l'exécution complète : le trigger a capturé les données, l'email a été envoyé. Tout roule.

**[TRANSITION — face caméra]**

Ton premier webhook entrant fonctionne. Tu peux maintenant recevoir des données de Postman, d'un script, de n8n, de Stripe — de n'importe quel outil. Dans la prochaine leçon, on fait l'inverse : OttoKit envoie des requêtes vers une API externe.

---

**Points clés**
- Le trigger "Receive Data from Webhook" génère une URL unique
- Tout service envoyant un POST JSON à cette URL déclenche le workflow
- "Fetch Data" charge les champs reçus pour les rendre disponibles dans les actions
- Tester avec Postman ou Reqbin avant de brancher un vrai service

**Mots-clés SEO**
- OttoKit webhook entrant
- recevoir données webhook OttoKit
- OttoKit Postman test webhook
- trigger webhook WordPress OttoKit

---

## Leçon 10.3 — API App : OttoKit envoie des requêtes HTTP

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Le webhook entrant, c'est OttoKit qui reçoit. L'API App, c'est OttoKit qui envoie. Tu peux appeler n'importe quelle API REST : OpenAI, Google, un service custom, ton propre serveur. C'est l'action la plus polyvalente d'OttoKit.

**[ÉCRAN — slide "API App — le couteau suisse"]**

L'API App te permet de :

- Envoyer des requêtes **GET** (lire des données)
- Envoyer des requêtes **POST** (envoyer des données)
- Ajouter des **headers** (authentification, content-type)
- Recevoir et traiter la **réponse**

C'est une action, pas un trigger. Tu la places après un trigger dans ton workflow.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre un workflow existant ou en crée un nouveau : "API OpenAI — résumé de cours"]
[Le trigger est déjà configuré — par exemple un Schedule App quotidien]
[Clique sur "Add Step" pour ajouter une action]
[Tape "API" dans la barre de recherche]
[Sélectionne "API App" ou "Webhook / API"]
[Sélectionne l'action "Send Data via Webhook / API Call"]

On ajoute l'API App comme action dans un workflow. C'est ici que tu configures ta requête HTTP.

**[ÉCRAN — screencast configuration de l'URL et méthode]**

[Dans le champ "URL", tape : https://api.openai.com/v1/chat/completions]
[Dans le champ "Method", sélectionne "POST"]

On va appeler l'API OpenAI pour générer un résumé de cours. L'URL, c'est l'endpoint de l'API. La méthode, c'est POST parce qu'on envoie des données.

**[ÉCRAN — screencast configuration des headers]**

[Dans la section "Headers", ajoute deux headers :]
[Header 1 — Key: "Content-Type", Value: "application/json"]
[Header 2 — Key: "Authorization", Value: "Bearer sk-...ta-cle-api..."]

Les headers, c'est la carte d'identité de ta requête. "Content-Type" dit à l'API qu'on envoie du JSON. "Authorization" contient ta clé API. Chaque API a ses propres exigences — consulte toujours la documentation.

**[ÉCRAN — screencast configuration du body]**

[Dans la section "Body", sélectionne "Raw / JSON"]
[Tape le body suivant :]

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Tu es un assistant pédagogique. Résume en 3 phrases."
    },
    {
      "role": "user",
      "content": "Résume le cours suivant : Introduction à WooCommerce..."
    }
  ],
  "max_tokens": 200
}
```

Le body, c'est le contenu de ta requête. Ici, on envoie un prompt à OpenAI. Tu peux bien sûr injecter des champs dynamiques depuis le trigger — par exemple, le contenu du cours qui vient d'un Google Sheet.

**[ÉCRAN — screencast test de l'action]**

[Clique sur "Test Action" ou "Fetch Data"]
[Montre la réponse de l'API : un objet JSON avec le résumé généré]
[Pointe le champ "choices[0].message.content" qui contient le texte]

OttoKit envoie la requête et affiche la réponse. Tu vois le JSON retourné par OpenAI. Le résumé se trouve dans `choices[0].message.content`. On verra comment extraire ce champ dans la leçon 10.5.

**[ÉCRAN — slide "Autres API que tu peux appeler"]**

Quelques exemples concrets :

- **OpenAI** — générer du texte, des résumés, des descriptions produit
- **Google Translate** — traduire un contenu automatiquement
- **Stripe** — vérifier le statut d'un paiement
- **Ton propre serveur** — envoyer des données à un script PHP ou Python
- **SMS (Twilio, OVH)** — envoyer un SMS de confirmation

Du moment que le service a une API REST et de la documentation, tu peux l'appeler depuis OttoKit.

**[TRANSITION — face caméra]**

L'API App ouvre des possibilités énormes. Mais avant de les exploiter, on va combiner webhook et API App dans un scénario concret : connecter OttoKit à n8n. C'est la leçon suivante.

---

**Points clés**
- L'API App envoie des requêtes HTTP (GET, POST) vers n'importe quelle API REST
- Configuration : URL + méthode + headers + body
- L'authentification passe souvent par un header "Authorization: Bearer ..."
- Toujours tester l'action avant d'activer le workflow

**Mots-clés SEO**
- OttoKit API App
- appeler API externe OttoKit
- OttoKit OpenAI intégration
- requête HTTP OttoKit workflow

---

## Leçon 10.4 — Connecter OttoKit à n8n via webhook

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit + n8n

---

**[INTRO — face caméra]**

n8n et OttoKit ne sont pas concurrents. Ce sont des partenaires. n8n excelle dans les traitements complexes — scraping, IA, logique avancée. OttoKit excelle dans les actions WordPress — créer un article, envoyer un email, inscrire un étudiant. Connecter les deux, c'est avoir le meilleur des deux mondes.

**[ÉCRAN — slide "Le scénario"]**

Voici le flux qu'on va construire :

1. **n8n** reçoit un brief et génère un article avec l'IA
2. **n8n** envoie l'article au webhook OttoKit
3. **OttoKit** crée un brouillon WordPress avec le bon titre, le bon contenu et la bonne catégorie

n8n fait le travail lourd. OttoKit fait l'action WordPress.

**[ÉCRAN — screencast OttoKit — création du webhook]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "n8n → Publier article WordPress"]
[Configure un trigger webhook (comme en leçon 10.2)]
[Copie l'URL webhook générée]

Première étape : on crée le webhook dans OttoKit. On récupère l'URL. C'est cette URL que n8n va appeler.

**[ÉCRAN — screencast n8n — workflow existant]**

[Ouvre n8n — montre un workflow simple avec un nœud "AI Generate" ou équivalent]
[Le workflow produit un titre et un contenu d'article]
[Ajoute un nœud "HTTP Request" à la fin du workflow]

Côté n8n, on a déjà un workflow qui génère du contenu. On ajoute un nœud HTTP Request à la fin.

**[ÉCRAN — screencast n8n — configuration du HTTP Request]**

[Dans le nœud HTTP Request :]
[Method : POST]
[URL : colle l'URL webhook OttoKit]
[Body Type : JSON]
[Configure le body :]

```json
{
  "titre": "{{ $json.title }}",
  "contenu": "{{ $json.content }}",
  "categorie": "WordPress",
  "statut": "draft"
}
```

[Exécute le nœud pour tester]

On configure la requête POST vers l'URL OttoKit. Le body contient les données de l'article : titre, contenu, catégorie, statut. Les expressions n8n (`{{ $json.title }}`) injectent les valeurs du nœud précédent.

**[ÉCRAN — screencast OttoKit — Fetch Data]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" sur le trigger]
[Montre les champs reçus : titre, contenu, catégorie, statut]

OttoKit a bien reçu les données. On voit les quatre champs.

**[ÉCRAN — screencast OttoKit — action WordPress]**

[Ajoute une action "WordPress" > "Create Post"]
[Dans le champ "Title", sélectionne le champ dynamique "titre"]
[Dans le champ "Content", sélectionne "contenu"]
[Dans le champ "Category", sélectionne "catégorie"]
[Dans le champ "Status", sélectionne "statut" (ou tape "draft")]
[Clique sur "Save"]

On ajoute l'action WordPress "Create Post". On mappe chaque champ du webhook vers le bon champ WordPress. Titre → titre. Contenu → contenu. Et on met le statut en brouillon pour relire avant publication.

**[ÉCRAN — screencast test complet]**

[Active le workflow OttoKit]
[Reviens dans n8n]
[Exécute le workflow n8n]
[Reviens dans OttoKit > History — montre l'exécution réussie]
[Ouvre WordPress admin > Articles > montre le brouillon créé]

On teste la chaîne complète. n8n génère l'article, l'envoie au webhook, OttoKit crée le brouillon. Dans WordPress, l'article est là, prêt à être relu et publié.

**[TRANSITION — face caméra]**

Tu viens de créer un pont entre deux plateformes. Ce pattern — n8n pour le traitement, OttoKit pour l'action WordPress — c'est exactement ce qu'on utilise chez schoolsWP pour automatiser la production de contenu. Dans la prochaine leçon, on apprend à lire et utiliser la réponse d'une API.

---

**Points clés**
- n8n traite les données complexes, OttoKit exécute les actions WordPress
- Le pont se fait via un webhook : n8n envoie un POST, OttoKit reçoit et agit
- Toujours mapper les champs du webhook vers les champs WordPress
- Ce pattern fonctionne avec n'importe quel outil capable d'envoyer un POST

**Mots-clés SEO**
- connecter OttoKit n8n
- n8n webhook OttoKit WordPress
- automatiser publication WordPress n8n
- pont n8n OttoKit

---

## Leçon 10.5 — Parser la réponse d'une API

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Quand tu appelles une API avec l'API App, tu reçois une réponse. Mais cette réponse est un gros bloc JSON. Tu ne veux pas tout — tu veux un champ précis. Extraire ce champ, c'est ce qu'on appelle "parser la réponse". Et c'est indispensable pour utiliser le résultat dans la suite de ton workflow.

**[ÉCRAN — slide "Le problème"]**

Reprenons l'exemple OpenAI de la leçon 10.3. La réponse ressemble à ça :

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "WooCommerce est le plugin e-commerce de référence..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 45,
    "completion_tokens": 67,
    "total_tokens": 112
  }
}
```

Ce qui t'intéresse, c'est uniquement le texte dans `choices[0].message.content`. Tout le reste, c'est de la métadonnée.

**[ÉCRAN — screencast OttoKit — réponse API brute]**

[Ouvre le workflow avec l'action API App configurée dans la leçon 10.3]
[Montre la réponse brute retournée après le test]
[Pointe l'arborescence JSON dans le panneau de données OttoKit]

Après avoir testé l'action API App, OttoKit affiche la réponse complète. Tu vois une arborescence de données. C'est ici que tu repères le chemin vers le champ que tu veux.

**[ÉCRAN — screencast OttoKit — navigation dans la réponse]**

[Dans le panneau de données, déplie "choices"]
[Déplie l'élément [0]]
[Déplie "message"]
[Pointe "content" — c'est le texte généré]

Le chemin complet est : `choices` → `[0]` → `message` → `content`. OttoKit te permet de naviguer dans cette arborescence visuellement.

**[ÉCRAN — screencast OttoKit — utiliser le champ dans l'action suivante]**

[Ajoute une action après l'API App — par exemple "WordPress" > "Create Post"]
[Dans le champ "Content" de l'action WordPress]
[Clique sur le sélecteur de données dynamiques]
[Navigue dans les données de l'étape précédente (API App)]
[Sélectionne "choices > 0 > message > content"]

Pour utiliser cette valeur dans une action suivante, tu ouvres le sélecteur de données dynamiques. Tu navigues dans les données de l'étape API App et tu sélectionnes le champ exact. OttoKit insère la référence automatiquement.

**[ÉCRAN — slide "Cas concrets de parsing"]**

| API appelée | Ce que tu extrais | Chemin |
|---|---|---|
| OpenAI | Le texte généré | `choices[0].message.content` |
| Stripe | Le statut du paiement | `data.status` |
| Google Translate | Le texte traduit | `data.translations[0].translatedText` |
| API custom | Un ID retourné | `result.id` |

Chaque API a sa propre structure de réponse. Consulte la documentation pour connaître le format exact.

**[ÉCRAN — slide "Conseils pratiques"]**

- Toujours tester l'action API App avant de parser — tu as besoin de la réponse réelle
- Si un champ est un tableau (comme `choices`), tu accèdes au premier élément avec `[0]`
- Si la réponse est vide ou en erreur, vérifie tes headers et ton body
- Utilise un Formatter après l'API App si tu veux nettoyer ou transformer la donnée

**[TRANSITION — face caméra]**

Tu sais maintenant lire et exploiter la réponse d'une API. Dans la prochaine leçon, on fait l'inverse : OttoKit envoie des données à un service externe via un webhook sortant.

---

**Points clés**
- La réponse d'une API est un objet JSON avec une structure arborescente
- Tu navigues dans l'arborescence pour trouver le champ exact que tu veux
- Le sélecteur de données dynamiques te permet d'injecter ce champ dans l'action suivante
- Toujours tester l'appel API pour voir la réponse réelle avant de configurer le parsing

**Mots-clés SEO**
- OttoKit parser réponse API
- extraire données API OttoKit
- JSON parsing OttoKit workflow
- OttoKit data mapping API

---

## Leçon 10.6 — Webhook sortant : OttoKit notifie un service externe

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Jusqu'ici, OttoKit recevait des données ou appelait des API. Maintenant, on fait l'inverse : OttoKit envoie des données à un service externe quand un événement se produit sur ton site. C'est le webhook sortant.

**[ÉCRAN — slide "Le scénario"]**

Un nouvel étudiant s'inscrit à ta formation sur WordPress. Tu veux :

1. Détecter l'inscription (trigger TutorLMS)
2. Envoyer les informations de l'étudiant à ton tableau de bord personnalisé (un Google Sheet, un endpoint custom, ou n8n)

Le webhook sortant est l'action qui envoie ces données.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Inscription → Notifier serveur"]
[Configure un trigger — par exemple TutorLMS "Student Enrolled" ou WordPress "User Registered"]
[Fait un Fetch Data sur le trigger — montre les champs disponibles : user_email, display_name, course_name]

Le trigger détecte l'inscription et capture les données de l'étudiant.

**[ÉCRAN — screencast ajout de l'action webhook sortant]**

[Clique sur "Add Step"]
[Tape "Webhook" ou "API" dans la recherche]
[Sélectionne "Webhook / API" > "Send Data via Webhook / API Call"]

L'action "Send Data via Webhook / API Call" est la même que l'API App. La différence, c'est l'intention : ici, tu envoies des données vers un endpoint que tu contrôles.

**[ÉCRAN — screencast configuration de la requête]**

[Dans le champ URL, tape une URL de destination — par exemple : https://ton-serveur.com/api/new-student]
[Méthode : POST]
[Headers : Content-Type: application/json]
[Body — sélectionne "Raw / JSON" et configure :]

```json
{
  "source": "OttoKit",
  "event": "new_enrollment",
  "student_email": "{{user_email}}",
  "student_name": "{{display_name}}",
  "course": "{{course_name}}",
  "timestamp": "{{current_date_time}}"
}
```

[Montre l'insertion des champs dynamiques du trigger dans le body]

Tu construis le body avec les données du trigger. Chaque champ entre doubles accolades est une valeur dynamique qui sera remplacée par les vraies données au moment de l'exécution.

**[ÉCRAN — screencast test avec webhook.site]**

[Ouvre webhook.site dans un nouvel onglet]
[Copie l'URL temporaire fournie par webhook.site]
[Colle cette URL dans le champ URL de l'action OttoKit]
[Teste l'action]
[Reviens sur webhook.site — montre les données reçues]

Pour tester sans avoir de vrai serveur, utilise webhook.site. C'est un outil gratuit qui te donne une URL temporaire et affiche tout ce qu'il reçoit. Tu vérifies que les données sont bien envoyées avant de brancher ton vrai endpoint.

**[ÉCRAN — slide "Cas d'usage concrets"]**

- **Dashboard personnalisé** : envoyer les données de vente à ton propre tableau de bord
- **n8n** : notifier un workflow n8n pour déclencher un traitement complexe (IA, enrichissement)
- **CRM externe** : ajouter un contact dans un CRM qui n'a pas d'intégration native
- **Logging** : enregistrer chaque action importante dans un Google Sheet ou une base de données
- **Slack custom** : envoyer une notification formatée avec des données précises

**[TRANSITION — face caméra]**

Tu sais maintenant envoyer des données depuis OttoKit vers n'importe quel service. Mais un webhook sans sécurité, c'est une porte ouverte. Dans la prochaine leçon, on verrouille tout ça.

---

**Points clés**
- Le webhook sortant utilise l'action "Send Data via Webhook / API Call"
- Tu construis le body JSON avec les champs dynamiques du trigger
- webhook.site est l'outil idéal pour tester sans serveur
- Le webhook sortant transforme OttoKit en émetteur de données vers n'importe quel endpoint

**Mots-clés SEO**
- OttoKit webhook sortant
- envoyer données OttoKit API
- webhook sortant WordPress
- OttoKit notifier service externe

---

## Leçon 10.7 — Sécuriser ses webhooks : secrets, validation, HTTPS

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides + screencast OttoKit

---

**[INTRO — face caméra]**

Un webhook, c'est une URL accessible publiquement. N'importe qui peut lui envoyer des données. Si tu ne le sécurises pas, quelqu'un pourrait déclencher ton workflow avec de fausses données — ou pire, injecter du contenu sur ton site WordPress. On va voir comment éviter ça.

**[ÉCRAN — slide "Les 3 risques"]**

Sans sécurité, ton webhook est exposé à :

1. **Déclenchement non autorisé** — quelqu'un envoie un POST à ton URL et déclenche ton workflow
2. **Fausses données** — le payload contient des informations incorrectes ou malveillantes
3. **Interception** — les données transitent en clair sur le réseau

**[ÉCRAN — slide "Protection 1 : le secret webhook"]**

La première protection, c'est un secret partagé. Le principe :

1. Tu définis un mot de passe secret dans OttoKit
2. Le service qui envoie les données inclut ce secret dans un header
3. OttoKit vérifie que le secret correspond avant de traiter les données

Si le secret ne correspond pas, OttoKit ignore la requête.

**[ÉCRAN — screencast OttoKit — configuration du secret]**

[Ouvre un workflow avec un trigger webhook]
[Dans les paramètres du trigger, montre le champ "Secret" ou "Webhook Secret"]
[Tape un secret : "mon-secret-schoolswp-2026"]
[Clique sur "Save"]

Tu définis le secret dans le trigger webhook. C'est une chaîne de caractères — utilise quelque chose de long et aléatoire. Pas "password123".

**[ÉCRAN — screencast Postman — ajout du header secret]**

[Ouvre Postman avec la requête webhook]
[Dans l'onglet "Headers", ajoute un header :]
[Key : "X-Webhook-Secret" ou le nom spécifié par OttoKit]
[Value : "mon-secret-schoolswp-2026"]
[Envoie la requête — montre le succès]

Côté émetteur, tu ajoutes le même secret dans un header. OttoKit compare les deux. Si ça correspond, le workflow se déclenche. Sinon, la requête est rejetée.

[Supprime le header secret]
[Renvoie la requête — montre le rejet ou l'absence de déclenchement]

Sans le secret, la requête est ignorée. Ton workflow est protégé.

**[ÉCRAN — slide "Protection 2 : HTTPS obligatoire"]**

Deuxième protection : toujours utiliser HTTPS. L'URL webhook générée par OttoKit commence par `https://` — c'est déjà bon. Mais si tu crées des webhooks sortants vers ton propre serveur, assure-toi que l'URL de destination utilise aussi HTTPS.

Pourquoi ? Sans HTTPS, les données transitent en clair. N'importe qui sur le réseau peut les lire — y compris les clés API dans les headers.

**[ÉCRAN — slide "Protection 3 : valider le payload"]**

Troisième protection : valider le contenu. Avant d'utiliser les données d'un webhook dans ton workflow, vérifie :

- Que les champs attendus sont présents (email, nom, etc.)
- Que les valeurs ont le bon format (un email ressemble à un email)
- Utilise des conditions OttoKit (Filter ou Condition) pour rejeter les données invalides

**[ÉCRAN — screencast OttoKit — ajout d'une condition de validation]**

[Dans le workflow, ajoute une action "Condition" après le trigger webhook]
[Configure la condition : "email" contains "@"]
[Branche True → action WordPress / Branche False → action "Stop"]

Par exemple, tu ajoutes une condition qui vérifie que le champ "email" contient bien un "@". Si oui, le workflow continue. Sinon, il s'arrête. C'est un filet de sécurité simple mais efficace.

**[ÉCRAN — slide "Checklist sécurité webhook"]**

Avant de mettre un webhook en production :

- [ ] Secret configuré et partagé avec l'émetteur
- [ ] URL en HTTPS (entrant et sortant)
- [ ] Validation du payload avec une condition
- [ ] Workflow testé avec des données valides ET invalides
- [ ] Secret stocké dans un endroit sécurisé (pas dans un Google Doc public)

**[TRANSITION — face caméra]**

Le Module 10 est bouclé. Tu sais recevoir des données, envoyer des requêtes API, connecter OttoKit à n8n, parser des réponses, envoyer des notifications, et sécuriser le tout. Passe au quiz pour valider tes acquis avant d'attaquer le Module 11 sur les AI Agents.

---

**Points clés**
- Un webhook non sécurisé peut être déclenché par n'importe qui
- Le secret webhook empêche les déclenchements non autorisés
- HTTPS protège les données en transit
- Une condition de validation filtre les payloads invalides

**Mots-clés SEO**
- sécuriser webhook OttoKit
- OttoKit webhook secret
- HTTPS webhook WordPress
- validation webhook OttoKit

---

## Notes de production — Module 10

### Captures à préparer
- Schéma animé : mécanisme webhook (émetteur → URL → récepteur)
- Slide comparaison webhook entrant vs sortant
- Slide comparaison webhook vs API (push vs pull)
- Screencast OttoKit : création trigger webhook + URL générée
- Screencast Postman : requête POST avec payload JSON
- Screencast OttoKit : Fetch Data avec champs reçus
- Screencast OttoKit : action API App — configuration URL, headers, body
- Screencast n8n : nœud HTTP Request vers webhook OttoKit
- Screencast OttoKit : parsing réponse API — navigation arborescence JSON
- Screencast OttoKit : sélecteur de données dynamiques
- Screencast webhook.site : réception des données
- Screencast OttoKit : configuration secret webhook
- Screencast Postman : header secret + test rejet

### Environnement de démo
- Compte OttoKit (plan premium recommandé pour les tests API)
- Postman (application desktop ou version web)
- webhook.site (gratuit, navigateur)
- Clé API OpenAI (pour la démo API App)
- Instance n8n (https://schoolswp-n8n.wp1.host ou instance locale)
- Site WordPress schoolsWP avec TutorLMS ou WooCommerce
- Google Sheet pour l'exemple de logging

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 10.1 | 6 min |
| 10.2 | 7 min |
| 10.3 | 7 min |
| 10.4 | 6 min |
| 10.5 | 6 min |
| 10.6 | 6 min |
| 10.7 | 6 min |
| **Total M10** | **44 min** |

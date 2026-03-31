# Scripts video — Module 10 : Webhooks et API : connecter n'importe quel service

**Formation** : Maitriser OttoKit
**Module** : M10 — Webhooks et API : connecter n'importe quel service
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~45 min de video
**Date** : 2026-03-30

---

## Lecon 10.1 — Webhooks : le pont universel entre les outils

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides explicatifs, schema anime

---

**[INTRO — face camera]**

OttoKit propose plus de 1 300 integrations natives. Mais ton outil prefere n'est peut-etre pas dans la liste. Ou alors, tu veux connecter ton propre script, ton propre API, ton propre systeme. C'est exactement le role des webhooks.

**[ECRAN — slide "Le probleme"]**

Imagine : tu utilises un outil de facturation francais, un CRM sur mesure, ou un script Python qui tourne sur ton serveur. Aucun de ces outils n'a d'integration native dans OttoKit. Sans webhook, tu es bloque.

**[ECRAN — slide "Webhook = messagerie entre deux outils"]**

Un webhook, c'est une URL. Un outil envoie des donnees a cette URL. L'autre outil les recoit et agit. Pas de cable, pas de plugin, pas de configuration complexe. Une simple adresse web suffit.

Concretement :

1. **L'outil A** genere un evenement (un paiement, un formulaire soumis, un article cree)
2. **L'outil A** envoie les donnees a une URL (le webhook)
3. **L'outil B** recoit les donnees et execute une action

C'est une communication a sens unique : un outil parle, l'autre ecoute.

**[ECRAN — schema anime "Anatomie d'un webhook"]**

Un webhook transporte trois elements :

- **L'URL** : l'adresse ou envoyer les donnees. OttoKit la genere automatiquement.
- **Le payload** : les donnees elles-memes, en format JSON. C'est le contenu du message.
- **Les headers** : des informations supplementaires — le type de contenu, un secret de securite, une signature.

```json
{
  "event": "order_created",
  "customer_email": "jean@example.com",
  "total": 49.90,
  "product": "Formation WordPress"
}
```

Voici un payload type. C'est du JSON — des paires cle/valeur. Quand OttoKit recoit ce payload, il peut utiliser chaque champ dans les actions du workflow.

**[ECRAN — slide "Deux directions"]**

Les webhooks fonctionnent dans deux sens :

| Direction | Ce que ca fait | Exemple |
|---|---|---|
| **Webhook entrant** | OttoKit recoit des donnees | Stripe envoie un paiement → OttoKit declenche un workflow |
| **Webhook sortant** | OttoKit envoie des donnees | OttoKit notifie ton serveur qu'un utilisateur s'est inscrit |

Dans les prochaines lecons, on voit les deux.

**[ECRAN — slide "Webhook vs API"]**

Derniere distinction importante :

- **Webhook** = l'outil externe envoie des donnees a OttoKit quand un evenement se produit. C'est du push.
- **API App** = OttoKit va chercher des donnees ou envoie des commandes a un service externe. C'est du pull (ou du push a la demande).

Les deux sont complementaires. On couvre l'API App dans la lecon 10.3.

**[TRANSITION — face camera]**

Tu comprends maintenant le mecanisme. Dans la prochaine lecon, on passe a la pratique : tu vas creer ton premier webhook entrant et recevoir des donnees en temps reel dans OttoKit.

---

**Points cles**
- Un webhook est une URL qui recoit ou envoie des donnees entre deux outils
- Le payload est au format JSON (paires cle/valeur)
- Webhook entrant = OttoKit recoit ; webhook sortant = OttoKit envoie
- Les webhooks permettent de connecter des outils qui n'ont pas d'integration native

**Mots-cles SEO**
- OttoKit webhook
- webhook WordPress automatisation
- connecter API OttoKit
- webhook entrant sortant OttoKit

---

## Lecon 10.2 — Webhook entrant : OttoKit recoit des donnees

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit + Postman

---

**[INTRO — face camera]**

On met les mains dedans. Tu vas creer un webhook dans OttoKit, puis lui envoyer des donnees depuis Postman. A la fin de cette lecon, tu auras un workflow qui se declenche quand un service externe lui parle.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit — app.ottokit.com]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Webhook entrant — test"]
[Clique sur le bloc trigger "When this happens..."]

On commence par creer un workflow et ouvrir le bloc trigger.

**[ECRAN — screencast selection du trigger webhook]**

[Dans le panneau lateral, tape "Webhook" dans la barre de recherche]
[Selectionne "Webhook / API"]
[Selectionne l'evenement "Receive Data from Webhook"]

Tu choisis le trigger "Receive Data from Webhook". C'est le webhook entrant : OttoKit attend que quelqu'un lui envoie des donnees.

**[ECRAN — screencast URL generee]**

[Montre l'URL webhook generee par OttoKit]
[Selectionne l'URL et la copie]

OttoKit te genere une URL unique. C'est ton adresse webhook. Copie-la. N'importe quel outil capable d'envoyer une requete HTTP POST peut utiliser cette URL.

**[ECRAN — screencast Postman]**

[Ouvre Postman dans un nouvel onglet]
[Cree une nouvelle requete]
[Selectionne la methode "POST"]
[Colle l'URL webhook OttoKit dans le champ URL]
[Va dans l'onglet "Body" > selectionne "raw" > selectionne "JSON"]
[Tape le payload suivant :]

```json
{
  "nom": "Marie Dupont",
  "email": "marie@schoolswp.com",
  "formation": "Maitriser OttoKit",
  "montant": 97
}
```

[Clique sur "Send"]
[Montre la reponse 200 OK]

On utilise Postman pour simuler un service externe. On envoie une requete POST avec un body JSON. Le code 200 confirme qu'OttoKit a bien recu les donnees.

Si tu n'as pas Postman, tu peux aussi utiliser Reqbin (gratuit, dans le navigateur) ou curl en ligne de commande.

**[ECRAN — screencast retour OttoKit]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" dans le panneau du trigger]
[Montre les champs recus : nom, email, formation, montant]

De retour dans OttoKit, clique sur "Fetch Data". Tu vois les champs que tu viens d'envoyer : nom, email, formation, montant. Ce sont ces champs que tu pourras utiliser dans toutes les actions de ton workflow.

**[ECRAN — screencast ajout d'une action rapide]**

[Ajoute une action "Send Email" apres le trigger]
[Dans le champ "To", selectionne le champ dynamique "email"]
[Dans le champ "Subject", tape "Bienvenue dans {{formation}}"]
[Dans le corps, tape "Bonjour {{nom}}, merci pour ton inscription !"]
[Clique sur "Save"]

Pour verifier que tout fonctionne, on ajoute une action email. On injecte les champs du webhook directement dans l'email. Chaque valeur du payload devient une variable utilisable.

**[ECRAN — screencast activation du workflow]**

[Active le workflow (toggle ON)]
[Reviens dans Postman]
[Renvoie la meme requete]
[Reviens dans OttoKit > History]
[Montre l'execution reussie avec le detail des donnees]

On active le workflow et on renvoie la requete. Dans l'historique, tu vois l'execution complete : le trigger a capture les donnees, l'email a ete envoye. Tout roule.

**[TRANSITION — face camera]**

Ton premier webhook entrant fonctionne. Tu peux maintenant recevoir des donnees de Postman, d'un script, de n8n, de Stripe — de n'importe quel outil. Dans la prochaine lecon, on fait l'inverse : OttoKit envoie des requetes vers une API externe.

---

**Points cles**
- Le trigger "Receive Data from Webhook" genere une URL unique
- Tout service envoyant un POST JSON a cette URL declenche le workflow
- "Fetch Data" charge les champs recus pour les rendre disponibles dans les actions
- Tester avec Postman ou Reqbin avant de brancher un vrai service

**Mots-cles SEO**
- OttoKit webhook entrant
- recevoir donnees webhook OttoKit
- OttoKit Postman test webhook
- trigger webhook WordPress OttoKit

---

## Lecon 10.3 — API App : OttoKit envoie des requetes HTTP

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Le webhook entrant, c'est OttoKit qui recoit. L'API App, c'est OttoKit qui envoie. Tu peux appeler n'importe quelle API REST : OpenAI, Google, un service custom, ton propre serveur. C'est l'action la plus polyvalente d'OttoKit.

**[ECRAN — slide "API App — le couteau suisse"]**

L'API App te permet de :

- Envoyer des requetes **GET** (lire des donnees)
- Envoyer des requetes **POST** (envoyer des donnees)
- Ajouter des **headers** (authentification, content-type)
- Recevoir et traiter la **reponse**

C'est une action, pas un trigger. Tu la places apres un trigger dans ton workflow.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow existant ou en cree un nouveau : "API OpenAI — resume de cours"]
[Le trigger est deja configure — par exemple un Schedule App quotidien]
[Clique sur "Add Step" pour ajouter une action]
[Tape "API" dans la barre de recherche]
[Selectionne "API App" ou "Webhook / API"]
[Selectionne l'action "Send Data via Webhook / API Call"]

On ajoute l'API App comme action dans un workflow. C'est ici que tu configures ta requete HTTP.

**[ECRAN — screencast configuration de l'URL et methode]**

[Dans le champ "URL", tape : https://api.openai.com/v1/chat/completions]
[Dans le champ "Method", selectionne "POST"]

On va appeler l'API OpenAI pour generer un resume de cours. L'URL, c'est l'endpoint de l'API. La methode, c'est POST parce qu'on envoie des donnees.

**[ECRAN — screencast configuration des headers]**

[Dans la section "Headers", ajoute deux headers :]
[Header 1 — Key: "Content-Type", Value: "application/json"]
[Header 2 — Key: "Authorization", Value: "Bearer sk-...ta-cle-api..."]

Les headers, c'est la carte d'identite de ta requete. "Content-Type" dit a l'API qu'on envoie du JSON. "Authorization" contient ta cle API. Chaque API a ses propres exigences — consulte toujours la documentation.

**[ECRAN — screencast configuration du body]**

[Dans la section "Body", selectionne "Raw / JSON"]
[Tape le body suivant :]

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Tu es un assistant pedagogique. Resume en 3 phrases."
    },
    {
      "role": "user",
      "content": "Resume le cours suivant : Introduction a WooCommerce..."
    }
  ],
  "max_tokens": 200
}
```

Le body, c'est le contenu de ta requete. Ici, on envoie un prompt a OpenAI. Tu peux bien sur injecter des champs dynamiques depuis le trigger — par exemple, le contenu du cours qui vient d'un Google Sheet.

**[ECRAN — screencast test de l'action]**

[Clique sur "Test Action" ou "Fetch Data"]
[Montre la reponse de l'API : un objet JSON avec le resume genere]
[Pointe le champ "choices[0].message.content" qui contient le texte]

OttoKit envoie la requete et affiche la reponse. Tu vois le JSON retourne par OpenAI. Le resume se trouve dans `choices[0].message.content`. On verra comment extraire ce champ dans la lecon 10.5.

**[ECRAN — slide "Autres API que tu peux appeler"]**

Quelques exemples concrets :

- **OpenAI** — generer du texte, des resumes, des descriptions produit
- **Google Translate** — traduire un contenu automatiquement
- **Stripe** — verifier le statut d'un paiement
- **Ton propre serveur** — envoyer des donnees a un script PHP ou Python
- **SMS (Twilio, OVH)** — envoyer un SMS de confirmation

Du moment que le service a une API REST et de la documentation, tu peux l'appeler depuis OttoKit.

**[TRANSITION — face camera]**

L'API App ouvre des possibilites enormes. Mais avant de les exploiter, on va combiner webhook et API App dans un scenario concret : connecter OttoKit a n8n. C'est la lecon suivante.

---

**Points cles**
- L'API App envoie des requetes HTTP (GET, POST) vers n'importe quelle API REST
- Configuration : URL + methode + headers + body
- L'authentification passe souvent par un header "Authorization: Bearer ..."
- Toujours tester l'action avant d'activer le workflow

**Mots-cles SEO**
- OttoKit API App
- appeler API externe OttoKit
- OttoKit OpenAI integration
- requete HTTP OttoKit workflow

---

## Lecon 10.4 — Connecter OttoKit a n8n via webhook

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit + n8n

---

**[INTRO — face camera]**

n8n et OttoKit ne sont pas concurrents. Ce sont des partenaires. n8n excelle dans les traitements complexes — scraping, IA, logique avancee. OttoKit excelle dans les actions WordPress — creer un article, envoyer un email, inscrire un etudiant. Connecter les deux, c'est avoir le meilleur des deux mondes.

**[ECRAN — slide "Le scenario"]**

Voici le flux qu'on va construire :

1. **n8n** recoit un brief et genere un article avec l'IA
2. **n8n** envoie l'article au webhook OttoKit
3. **OttoKit** cree un brouillon WordPress avec le bon titre, le bon contenu et la bonne categorie

n8n fait le travail lourd. OttoKit fait l'action WordPress.

**[ECRAN — screencast OttoKit — creation du webhook]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "n8n → Publier article WordPress"]
[Configure un trigger webhook (comme en lecon 10.2)]
[Copie l'URL webhook generee]

Premiere etape : on cree le webhook dans OttoKit. On recupere l'URL. C'est cette URL que n8n va appeler.

**[ECRAN — screencast n8n — workflow existant]**

[Ouvre n8n — montre un workflow simple avec un noeud "AI Generate" ou equivalent]
[Le workflow produit un titre et un contenu d'article]
[Ajoute un noeud "HTTP Request" a la fin du workflow]

Cote n8n, on a deja un workflow qui genere du contenu. On ajoute un noeud HTTP Request a la fin.

**[ECRAN — screencast n8n — configuration du HTTP Request]**

[Dans le noeud HTTP Request :]
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

[Execute le noeud pour tester]

On configure la requete POST vers l'URL OttoKit. Le body contient les donnees de l'article : titre, contenu, categorie, statut. Les expressions n8n (`{{ $json.title }}`) injectent les valeurs du noeud precedent.

**[ECRAN — screencast OttoKit — Fetch Data]**

[Reviens dans OttoKit]
[Clique sur "Fetch Data" sur le trigger]
[Montre les champs recus : titre, contenu, categorie, statut]

OttoKit a bien recu les donnees. On voit les quatre champs.

**[ECRAN — screencast OttoKit — action WordPress]**

[Ajoute une action "WordPress" > "Create Post"]
[Dans le champ "Title", selectionne le champ dynamique "titre"]
[Dans le champ "Content", selectionne "contenu"]
[Dans le champ "Category", selectionne "categorie"]
[Dans le champ "Status", selectionne "statut" (ou tape "draft")]
[Clique sur "Save"]

On ajoute l'action WordPress "Create Post". On mappe chaque champ du webhook vers le bon champ WordPress. Titre → titre. Contenu → contenu. Et on met le statut en brouillon pour relire avant publication.

**[ECRAN — screencast test complet]**

[Active le workflow OttoKit]
[Reviens dans n8n]
[Execute le workflow n8n]
[Reviens dans OttoKit > History — montre l'execution reussie]
[Ouvre WordPress admin > Articles > montre le brouillon cree]

On teste la chaine complete. n8n genere l'article, l'envoie au webhook, OttoKit cree le brouillon. Dans WordPress, l'article est la, pret a etre relu et publie.

**[TRANSITION — face camera]**

Tu viens de creer un pont entre deux plateformes. Ce pattern — n8n pour le traitement, OttoKit pour l'action WordPress — c'est exactement ce qu'on utilise chez schoolsWP pour automatiser la production de contenu. Dans la prochaine lecon, on apprend a lire et utiliser la reponse d'une API.

---

**Points cles**
- n8n traite les donnees complexes, OttoKit execute les actions WordPress
- Le pont se fait via un webhook : n8n envoie un POST, OttoKit recoit et agit
- Toujours mapper les champs du webhook vers les champs WordPress
- Ce pattern fonctionne avec n'importe quel outil capable d'envoyer un POST

**Mots-cles SEO**
- connecter OttoKit n8n
- n8n webhook OttoKit WordPress
- automatiser publication WordPress n8n
- pont n8n OttoKit

---

## Lecon 10.5 — Parser la reponse d'une API

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Quand tu appelles une API avec l'API App, tu recois une reponse. Mais cette reponse est un gros bloc JSON. Tu ne veux pas tout — tu veux un champ precis. Extraire ce champ, c'est ce qu'on appelle "parser la reponse". Et c'est indispensable pour utiliser le resultat dans la suite de ton workflow.

**[ECRAN — slide "Le probleme"]**

Reprenons l'exemple OpenAI de la lecon 10.3. La reponse ressemble a ca :

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "WooCommerce est le plugin e-commerce de reference..."
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

Ce qui t'interesse, c'est uniquement le texte dans `choices[0].message.content`. Tout le reste, c'est de la metadonnee.

**[ECRAN — screencast OttoKit — reponse API brute]**

[Ouvre le workflow avec l'action API App configuree dans la lecon 10.3]
[Montre la reponse brute retournee apres le test]
[Pointe l'arborescence JSON dans le panneau de donnees OttoKit]

Apres avoir teste l'action API App, OttoKit affiche la reponse complete. Tu vois une arborescence de donnees. C'est ici que tu reperes le chemin vers le champ que tu veux.

**[ECRAN — screencast OttoKit — navigation dans la reponse]**

[Dans le panneau de donnees, deplie "choices"]
[Deplie l'element [0]]
[Deplie "message"]
[Pointe "content" — c'est le texte genere]

Le chemin complet est : `choices` → `[0]` → `message` → `content`. OttoKit te permet de naviguer dans cette arborescence visuellement.

**[ECRAN — screencast OttoKit — utiliser le champ dans l'action suivante]**

[Ajoute une action apres l'API App — par exemple "WordPress" > "Create Post"]
[Dans le champ "Content" de l'action WordPress]
[Clique sur le selecteur de donnees dynamiques]
[Navigue dans les donnees de l'etape precedente (API App)]
[Selectionne "choices > 0 > message > content"]

Pour utiliser cette valeur dans une action suivante, tu ouvres le selecteur de donnees dynamiques. Tu navigues dans les donnees de l'etape API App et tu selectionnes le champ exact. OttoKit insere la reference automatiquement.

**[ECRAN — slide "Cas concrets de parsing"]**

| API appelee | Ce que tu extrais | Chemin |
|---|---|---|
| OpenAI | Le texte genere | `choices[0].message.content` |
| Stripe | Le statut du paiement | `data.status` |
| Google Translate | Le texte traduit | `data.translations[0].translatedText` |
| API custom | Un ID retourne | `result.id` |

Chaque API a sa propre structure de reponse. Consulte la documentation pour connaitre le format exact.

**[ECRAN — slide "Conseils pratiques"]**

- Toujours tester l'action API App avant de parser — tu as besoin de la reponse reelle
- Si un champ est un tableau (comme `choices`), tu accedes au premier element avec `[0]`
- Si la reponse est vide ou en erreur, verifie tes headers et ton body
- Utilise un Formatter apres l'API App si tu veux nettoyer ou transformer la donnee

**[TRANSITION — face camera]**

Tu sais maintenant lire et exploiter la reponse d'une API. Dans la prochaine lecon, on fait l'inverse : OttoKit envoie des donnees a un service externe via un webhook sortant.

---

**Points cles**
- La reponse d'une API est un objet JSON avec une structure arborescente
- Tu navigues dans l'arborescence pour trouver le champ exact que tu veux
- Le selecteur de donnees dynamiques te permet d'injecter ce champ dans l'action suivante
- Toujours tester l'appel API pour voir la reponse reelle avant de configurer le parsing

**Mots-cles SEO**
- OttoKit parser reponse API
- extraire donnees API OttoKit
- JSON parsing OttoKit workflow
- OttoKit data mapping API

---

## Lecon 10.6 — Webhook sortant : OttoKit notifie un service externe

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Jusqu'ici, OttoKit recevait des donnees ou appelait des API. Maintenant, on fait l'inverse : OttoKit envoie des donnees a un service externe quand un evenement se produit sur ton site. C'est le webhook sortant.

**[ECRAN — slide "Le scenario"]**

Un nouvel etudiant s'inscrit a ta formation sur WordPress. Tu veux :

1. Detecter l'inscription (trigger TutorLMS)
2. Envoyer les informations de l'etudiant a ton tableau de bord personnalise (un Google Sheet, un endpoint custom, ou n8n)

Le webhook sortant est l'action qui envoie ces donnees.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Inscription → Notifier serveur"]
[Configure un trigger — par exemple TutorLMS "Student Enrolled" ou WordPress "User Registered"]
[Fait un Fetch Data sur le trigger — montre les champs disponibles : user_email, display_name, course_name]

Le trigger detecte l'inscription et capture les donnees de l'etudiant.

**[ECRAN — screencast ajout de l'action webhook sortant]**

[Clique sur "Add Step"]
[Tape "Webhook" ou "API" dans la recherche]
[Selectionne "Webhook / API" > "Send Data via Webhook / API Call"]

L'action "Send Data via Webhook / API Call" est la meme que l'API App. La difference, c'est l'intention : ici, tu envoies des donnees vers un endpoint que tu controles.

**[ECRAN — screencast configuration de la requete]**

[Dans le champ URL, tape une URL de destination — par exemple : https://ton-serveur.com/api/new-student]
[Methode : POST]
[Headers : Content-Type: application/json]
[Body — selectionne "Raw / JSON" et configure :]

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

Tu construis le body avec les donnees du trigger. Chaque champ entre doubles accolades est une valeur dynamique qui sera remplacee par les vraies donnees au moment de l'execution.

**[ECRAN — screencast test avec webhook.site]**

[Ouvre webhook.site dans un nouvel onglet]
[Copie l'URL temporaire fournie par webhook.site]
[Colle cette URL dans le champ URL de l'action OttoKit]
[Teste l'action]
[Reviens sur webhook.site — montre les donnees recues]

Pour tester sans avoir de vrai serveur, utilise webhook.site. C'est un outil gratuit qui te donne une URL temporaire et affiche tout ce qu'il recoit. Tu verifies que les donnees sont bien envoyees avant de brancher ton vrai endpoint.

**[ECRAN — slide "Cas d'usage concrets"]**

- **Dashboard personnalise** : envoyer les donnees de vente a ton propre tableau de bord
- **n8n** : notifier un workflow n8n pour declencher un traitement complexe (IA, enrichissement)
- **CRM externe** : ajouter un contact dans un CRM qui n'a pas d'integration native
- **Logging** : enregistrer chaque action importante dans un Google Sheet ou une base de donnees
- **Slack custom** : envoyer une notification formatee avec des donnees precises

**[TRANSITION — face camera]**

Tu sais maintenant envoyer des donnees depuis OttoKit vers n'importe quel service. Mais un webhook sans securite, c'est une porte ouverte. Dans la prochaine lecon, on verrouille tout ca.

---

**Points cles**
- Le webhook sortant utilise l'action "Send Data via Webhook / API Call"
- Tu construis le body JSON avec les champs dynamiques du trigger
- webhook.site est l'outil ideal pour tester sans serveur
- Le webhook sortant transforme OttoKit en emetteur de donnees vers n'importe quel endpoint

**Mots-cles SEO**
- OttoKit webhook sortant
- envoyer donnees OttoKit API
- webhook sortant WordPress
- OttoKit notifier service externe

---

## Lecon 10.7 — Securiser ses webhooks : secrets, validation, HTTPS

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides + screencast OttoKit

---

**[INTRO — face camera]**

Un webhook, c'est une URL accessible publiquement. N'importe qui peut lui envoyer des donnees. Si tu ne le securises pas, quelqu'un pourrait declencher ton workflow avec de fausses donnees — ou pire, injecter du contenu sur ton site WordPress. On va voir comment eviter ca.

**[ECRAN — slide "Les 3 risques"]**

Sans securite, ton webhook est expose a :

1. **Declenchement non autorise** — quelqu'un envoie un POST a ton URL et declenche ton workflow
2. **Fausses donnees** — le payload contient des informations incorrectes ou malveillantes
3. **Interception** — les donnees transitent en clair sur le reseau

**[ECRAN — slide "Protection 1 : le secret webhook"]**

La premiere protection, c'est un secret partage. Le principe :

1. Tu definis un mot de passe secret dans OttoKit
2. Le service qui envoie les donnees inclut ce secret dans un header
3. OttoKit verifie que le secret correspond avant de traiter les donnees

Si le secret ne correspond pas, OttoKit ignore la requete.

**[ECRAN — screencast OttoKit — configuration du secret]**

[Ouvre un workflow avec un trigger webhook]
[Dans les parametres du trigger, montre le champ "Secret" ou "Webhook Secret"]
[Tape un secret : "mon-secret-schoolswp-2026"]
[Clique sur "Save"]

Tu definis le secret dans le trigger webhook. C'est une chaine de caracteres — utilise quelque chose de long et aleatoire. Pas "password123".

**[ECRAN — screencast Postman — ajout du header secret]**

[Ouvre Postman avec la requete webhook]
[Dans l'onglet "Headers", ajoute un header :]
[Key : "X-Webhook-Secret" ou le nom specifie par OttoKit]
[Value : "mon-secret-schoolswp-2026"]
[Envoie la requete — montre le succes]

Cote emetteur, tu ajoutes le meme secret dans un header. OttoKit compare les deux. Si ca correspond, le workflow se declenche. Sinon, la requete est rejetee.

[Supprime le header secret]
[Renvoie la requete — montre le rejet ou l'absence de declenchement]

Sans le secret, la requete est ignoree. Ton workflow est protege.

**[ECRAN — slide "Protection 2 : HTTPS obligatoire"]**

Deuxieme protection : toujours utiliser HTTPS. L'URL webhook generee par OttoKit commence par `https://` — c'est deja bon. Mais si tu crees des webhooks sortants vers ton propre serveur, assure-toi que l'URL de destination utilise aussi HTTPS.

Pourquoi ? Sans HTTPS, les donnees transitent en clair. N'importe qui sur le reseau peut les lire — y compris les cles API dans les headers.

**[ECRAN — slide "Protection 3 : valider le payload"]**

Troisieme protection : valider le contenu. Avant d'utiliser les donnees d'un webhook dans ton workflow, verifie :

- Que les champs attendus sont presents (email, nom, etc.)
- Que les valeurs ont le bon format (un email ressemble a un email)
- Utilise des conditions OttoKit (Filter ou Condition) pour rejeter les donnees invalides

**[ECRAN — screencast OttoKit — ajout d'une condition de validation]**

[Dans le workflow, ajoute une action "Condition" apres le trigger webhook]
[Configure la condition : "email" contains "@"]
[Branche True → action WordPress / Branche False → action "Stop"]

Par exemple, tu ajoutes une condition qui verifie que le champ "email" contient bien un "@". Si oui, le workflow continue. Sinon, il s'arrete. C'est un filet de securite simple mais efficace.

**[ECRAN — slide "Checklist securite webhook"]**

Avant de mettre un webhook en production :

- [ ] Secret configure et partage avec l'emetteur
- [ ] URL en HTTPS (entrant et sortant)
- [ ] Validation du payload avec une condition
- [ ] Workflow teste avec des donnees valides ET invalides
- [ ] Secret stocke dans un endroit securise (pas dans un Google Doc public)

**[TRANSITION — face camera]**

Le Module 10 est boucle. Tu sais recevoir des donnees, envoyer des requetes API, connecter OttoKit a n8n, parser des reponses, envoyer des notifications, et securiser le tout. Passe au quiz pour valider tes acquis avant d'attaquer le Module 11 sur les AI Agents.

---

**Points cles**
- Un webhook non securise peut etre declenche par n'importe qui
- Le secret webhook empeche les declenchements non autorises
- HTTPS protege les donnees en transit
- Une condition de validation filtre les payloads invalides

**Mots-cles SEO**
- securiser webhook OttoKit
- OttoKit webhook secret
- HTTPS webhook WordPress
- validation webhook OttoKit

---

## Notes de production — Module 10

### Captures a preparer
- Schema anime : mecanisme webhook (emetteur → URL → recepteur)
- Slide comparaison webhook entrant vs sortant
- Slide comparaison webhook vs API (push vs pull)
- Screencast OttoKit : creation trigger webhook + URL generee
- Screencast Postman : requete POST avec payload JSON
- Screencast OttoKit : Fetch Data avec champs recus
- Screencast OttoKit : action API App — configuration URL, headers, body
- Screencast n8n : noeud HTTP Request vers webhook OttoKit
- Screencast OttoKit : parsing reponse API — navigation arborescence JSON
- Screencast OttoKit : selecteur de donnees dynamiques
- Screencast webhook.site : reception des donnees
- Screencast OttoKit : configuration secret webhook
- Screencast Postman : header secret + test rejet

### Environnement de demo
- Compte OttoKit (plan premium recommande pour les tests API)
- Postman (application desktop ou version web)
- webhook.site (gratuit, navigateur)
- Cle API OpenAI (pour la demo API App)
- Instance n8n (https://schoolswp-n8n.wp1.host ou instance locale)
- Site WordPress schoolsWP avec TutorLMS ou WooCommerce
- Google Sheet pour l'exemple de logging

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 10.1 | 6 min |
| 10.2 | 7 min |
| 10.3 | 7 min |
| 10.4 | 6 min |
| 10.5 | 6 min |
| 10.6 | 6 min |
| 10.7 | 6 min |
| **Total M10** | **44 min** |

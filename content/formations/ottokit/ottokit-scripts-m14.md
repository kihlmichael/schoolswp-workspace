# Scripts video — Module 14 : OttoKit vs n8n vs Zapier : choisir le bon outil

**Formation** : Maitriser OttoKit
**Module** : M14 — OttoKit vs n8n vs Zapier : choisir le bon outil
**Lecons** : 6 videos + 1 quiz (10 questions)
**Duree totale** : ~40 min de video
**Date** : 2026-03-30

---

## Lecon 14.1 — Le paysage des outils d'automatisation en 2026

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides cartographie outils

---

**[INTRO — face camera]**

Tu connais OttoKit. Mais OttoKit n'est pas le seul outil d'automatisation. En 2026, il en existe des dizaines. Certains sont generiques, d'autres sont specialises WordPress. Certains sont gratuits, d'autres coutent des centaines d'euros par mois. Pour faire le bon choix, tu dois d'abord connaitre le terrain.

**[ECRAN — slide "Les 6 acteurs principaux"]**

Voici les 6 outils que tu vas rencontrer le plus souvent :

**1. OttoKit** (anciennement SureTriggers)
- Par Brainstorm Force (les createurs d'Astra et Spectra)
- Cloud + plugin WordPress natif
- 1 310+ integrations
- AI Agents et MCP integres
- A partir de 39$/mois (facturation annuelle)

**2. Zapier**
- Le leader historique de l'automatisation no-code
- Cloud pur, pas de plugin WordPress natif
- 7 000+ integrations — le catalogue le plus large
- A partir de 20$/mois, mais monte vite (100$+ pour du volume)

**3. Make** (anciennement Integromat)
- Cloud, interface visuelle tres appreciee
- 1 800+ integrations
- Pricing intermediaire
- Bonne gestion des API et des scenarios complexes

**4. n8n**
- Self-hosted (gratuit) ou cloud (payant)
- 400+ noeuds natifs
- Code possible (JavaScript, Python)
- Plus technique, plus puissant, pas d'AI Agents natif

**5. Uncanny Automator**
- Plugin WordPress uniquement
- Connecte les plugins WP entre eux
- Pas de connexion aux apps externes (ou tres limitee)
- Simple et fiable pour des automatisations purement WordPress

**6. Bit Integrations (anciennement Bit Flows)**
- Plugin WordPress
- Connecte formulaires et CRM
- Plus limite, mais gratuit pour les bases

**[ECRAN — slide "La carte du marche"]**

[Matrice 2 axes : Simplicite (vertical) vs Puissance (horizontal)]
[Placement des 6 outils sur la matrice]

```
Simplicite ↑
            |  Uncanny Automator
            |         Bit Flows
            |  OttoKit        Make
            |         Zapier
            |                   n8n
            +------------------------→ Puissance
```

En bas a droite : puissant mais complexe (n8n). En haut a gauche : simple mais limite (Uncanny Automator, Bit Flows). OttoKit, Zapier et Make sont au milieu — un compromis entre accessibilite et capacites.

**[ECRAN — slide "Les questions a se poser"]**

Avant de comparer, pose-toi ces 5 questions :

1. **Combien d'automatisations ai-je besoin ?** (5 ou 500 ?)
2. **Mon ecosysteme est-il centre sur WordPress ?** (ou multi-plateforme ?)
3. **Quel est mon budget mensuel ?** (0, 50, 200$ ?)
4. **Ai-je besoin d'heberger moi-meme ?** (conformite, securite ?)
5. **Quel est mon niveau technique ?** (no-code, low-code, code ?)

Les reponses a ces questions orientent directement vers le bon outil.

**[TRANSITION — face camera]**

Maintenant qu'on a la vue d'ensemble, on va comparer OttoKit face a face avec chaque concurrent. On commence par le plus connu : Zapier.

---

**Points cles**
- 6 outils principaux en 2026 : OttoKit, Zapier, Make, n8n, Uncanny Automator, Bit Flows
- Chaque outil a un positionnement different (simplicite vs puissance, generique vs WordPress)
- 5 questions guident le choix : volume, ecosysteme, budget, hebergement, niveau technique
- Il n'y a pas d'outil parfait — il y a l'outil adapte a ton contexte

**Mots-cles SEO**
- comparatif automatisation WordPress 2026
- OttoKit vs Zapier vs n8n
- meilleur outil automatisation WordPress
- alternative Zapier WordPress

---

## Lecon 14.2 — OttoKit vs Zapier : cout, integrations, WordPress

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs

---

**[INTRO — face camera]**

Zapier est la reference du marche. Plus de 7 000 integrations, une marque connue, des millions d'utilisateurs. Mais est-ce le meilleur choix quand ton ecosysteme est centre sur WordPress ? Comparons point par point.

**[ECRAN — slide "Comparatif sur 5 criteres"]**

| Critere | OttoKit | Zapier |
|---|---|---|
| **Integration WordPress** | Native (plugin) — acces direct aux hooks WP, WooCommerce, LMS, CRM | Via API/webhook — pas de plugin, pas d'acces natif aux hooks |
| **Nombre d'integrations** | 1 310+ | 7 000+ |
| **AI integree** | AI Agents + MCP | AI Actions (beta) |
| **Pricing (entree)** | 39$/mois (annuel) | 20$/mois (Starter — 750 tasks) |
| **Pricing (volume)** | 99$/mois (50K tasks) | 100$+/mois des 2 000 tasks |

**[ECRAN — slide "Critere 1 : Integration WordPress"]**

C'est la difference fondamentale. OttoKit a un plugin installe sur ton WordPress. Ce plugin donne un acces direct aux evenements internes : un utilisateur s'inscrit, un formulaire est soumis, un cours est termine, un tag CRM est ajoute.

Zapier n'a pas de plugin WordPress. Pour connecter WordPress a Zapier, tu passes par des plugins tiers (WP Webhooks, Zapier for WooCommerce) ou par l'API REST. Ca fonctionne, mais c'est un intermediaire supplementaire. Et chaque intermediaire est un point de fragilite.

**[ECRAN — slide "Critere 2 : Catalogue d'integrations"]**

Zapier a clairement l'avantage ici. 7 000 integrations contre 1 310. Si tu as besoin de connecter des apps de niche — un CRM specifique, un outil de comptabilite exotique, un logiciel metier — Zapier a plus de chances de le supporter.

Mais pose-toi la question : combien d'apps connectes-tu reellement ? La plupart des utilisateurs WordPress en utilisent 5 a 10. Et ces 5 a 10 sont presque toujours supportees par OttoKit.

**[ECRAN — slide "Critere 3 : Cout a volume"]**

C'est ici que la difference se creuse. Calculons pour 10 000 tasks par mois :

- **OttoKit** : 99$/mois (plan Pro, 50 000 tasks) → largement couvert
- **Zapier** : environ 200-300$/mois (plan Team ou plus) → le pricing de Zapier augmente rapidement avec le volume

Sur un an, ca represente une difference de 1 200 a 2 400$. Pour un freelance ou une petite entreprise, c'est significatif.

**[ECRAN — slide "Critere 4 : Experience utilisateur"]**

Les deux interfaces sont visuelles. Zapier utilise un editeur lineaire (etape par etape). OttoKit utilise un canvas (drag-and-drop). Le canvas est plus flexible pour les workflows avec des branches et des conditions.

Question de preference : si tu aimes la linerarite, Zapier. Si tu preferes voir l'ensemble du workflow d'un coup, OttoKit.

**[ECRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Ton ecosysteme est centre sur WordPress
- Tu veux une integration native avec tes plugins WP
- Tu geres un volume de tasks moyen a eleve
- Tu veux les AI Agents integres

**Choisis Zapier si** :
- Tu connectes beaucoup d'apps non-WordPress
- Tu as besoin d'une app de niche que seul Zapier supporte
- Le volume de tasks est faible (< 750/mois — le plan Starter suffit)

**[TRANSITION — face camera]**

Zapier est fort sur le catalogue universel. Mais pour WordPress, OttoKit est plus pertinent et moins cher. Comparons maintenant avec un outil tres different : n8n.

---

**Points cles**
- OttoKit : integration WordPress native, pricing avantageux a volume, AI Agents
- Zapier : catalogue d'integrations plus large (7 000+), mais pas de plugin WordPress
- A 10 000 tasks/mois, OttoKit coute 2 a 3 fois moins cher que Zapier
- Le choix depend de l'ecosysteme : centre WordPress → OttoKit, multi-plateforme → Zapier

**Mots-cles SEO**
- OttoKit vs Zapier
- OttoKit vs Zapier prix
- alternative Zapier WordPress moins cher
- OttoKit ou Zapier automatisation

---

## Lecon 14.3 — OttoKit vs n8n : cloud vs self-hosted, simple vs puissant

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs

---

**[INTRO — face camera]**

n8n, c'est l'outil des developpeurs et des tech-savvy. Open-source, self-hosted, avec la possibilite d'ecrire du code dans les workflows. Chez schoolsWP, on utilise les deux : OttoKit pour les automatisations WordPress, n8n pour les pipelines de contenu et les traitements complexes. Comparons.

**[ECRAN — slide "Comparatif sur 5 criteres"]**

| Critere | OttoKit | n8n |
|---|---|---|
| **Hebergement** | Cloud (geré par OttoKit) | Self-hosted (gratuit) ou cloud (payant) |
| **Interface** | Canvas visuel, no-code | Canvas visuel + code (JS/Python) |
| **Integrations** | 1 310+ (natives) | 400+ noeuds + HTTP/code custom |
| **AI** | AI Agents + MCP natifs | Pas d'AI Agents natif |
| **WordPress** | Plugin natif (hooks directs) | Via webhook ou API REST |
| **Cout** | 39$/mois (annuel) | Gratuit (self-hosted) ou 20€+/mois (cloud) |

**[ECRAN — slide "Architecture : cloud vs self-hosted"]**

C'est la difference la plus importante.

**OttoKit** est entierement cloud. Tu crees un compte, tu connectes tes apps, tu construis tes workflows. L'infrastructure est geree par OttoKit. Tu ne touches a aucun serveur.

**n8n self-hosted** tourne sur ton propre serveur. Tu installes, tu configures, tu mets a jour, tu geres les backups. En echange, tu as un controle total sur tes donnees et aucune limite de tasks.

Si tu n'as pas de serveur et que tu ne veux pas en gerer un, OttoKit. Si tu as deja un VPS et que tu es a l'aise avec Docker, n8n self-hosted peut etre gratuit a vie.

**[ECRAN — slide "Complexite : no-code vs low-code"]**

**OttoKit** est no-code. Tu selectionnes des apps, tu mappes des champs, tu publies. Pas de code a ecrire. C'est accessible a quelqu'un qui n'a jamais programme.

**n8n** est low-code. Tu peux faire beaucoup sans coder, mais les noeuds Code (JavaScript, Python) sont ce qui rend n8n vraiment puissant. Transformer des donnees, appeler des API custom, gerer des boucles complexes — c'est la que n8n brille.

Si tu ne codes pas → OttoKit. Si tu es a l'aise avec JavaScript ou Python → n8n debloque des possibilites qu'OttoKit n'offre pas.

**[ECRAN — slide "WordPress natif vs webhook"]**

OttoKit se connecte a WordPress via un plugin. Il accede directement aux hooks WordPress, WooCommerce, FluentCRM, TutorLMS. Le trigger "un utilisateur complete un cours" est un evenement natif.

n8n se connecte a WordPress via webhook ou API REST. Ca fonctionne, mais tu dois configurer le webhook cote WordPress (avec un plugin tiers ou du code). C'est moins direct.

Pour les automatisations purement WordPress, OttoKit est plus rapide a configurer.

**[ECRAN — slide "AI et agents"]**

OttoKit a integre les AI Agents et le protocole MCP directement dans la plateforme. Tu peux creer des agents qui utilisent tes workflows comme outils.

n8n n'a pas d'AI Agents natif. Tu peux appeler des API d'IA (OpenAI, Claude) via des noeuds HTTP ou Code, mais il n'y a pas de systeme d'agents integre. C'est plus manuel.

**[ECRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Tu veux du no-code pur
- Tes automatisations sont centrees sur WordPress
- Tu veux les AI Agents et MCP
- Tu ne veux pas gerer de serveur

**Choisis n8n si** :
- Tu veux un controle total (donnees, infrastructure)
- Tu codes en JavaScript ou Python
- Tu as des pipelines complexes (transformation de donnees, boucles, API custom)
- Tu veux zero cout d'outil (self-hosted)

**[TRANSITION — face camera]**

Ce n'est pas OttoKit ou n8n. C'est souvent OttoKit et n8n. On verra comment les combiner a la fin du module. Avant ca, comparons OttoKit avec Make.

---

**Points cles**
- OttoKit = cloud, no-code, WordPress natif, AI Agents
- n8n = self-hosted possible, code possible, plus de controle, pas d'AI Agents
- OttoKit pour les automatisations WordPress ; n8n pour les pipelines complexes
- Les deux ne sont pas concurrents — ils sont complementaires

**Mots-cles SEO**
- OttoKit vs n8n
- OttoKit vs n8n comparatif
- n8n WordPress automatisation
- OttoKit ou n8n lequel choisir

---

## Lecon 14.4 — OttoKit vs Make : interface, pricing, performance

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs

---

**[INTRO — face camera]**

Make — anciennement Integromat — est un concurrent direct d'OttoKit et Zapier. Interface visuelle, tarification au volume, bonne gestion des API. Voyons ou chacun se positionne.

**[ECRAN — slide "Comparatif sur 5 criteres"]**

| Critere | OttoKit | Make |
|---|---|---|
| **Interface** | Canvas drag-and-drop | Canvas visuel (scenarios) |
| **Integrations** | 1 310+ | 1 800+ |
| **WordPress natif** | Oui (plugin) | Non (via HTTP/webhook) |
| **AI** | AI Agents + MCP | AI (modules ChatGPT, etc.) |
| **Pricing** | 39$/mois (annuel) | 9$/mois (10K ops) a 16$/mois (40K ops) |

**[ECRAN — slide "Interface et experience"]**

Les deux outils utilisent un canvas visuel. Mais l'approche est differente.

**Make** utilise des "scenarios" avec des cercles connectes par des lignes. C'est tres visuel. Les filtres, les routeurs et les iterateurs sont des composants graphiques que tu places sur le canvas. L'interface est appreciee pour sa clarte.

**OttoKit** utilise un canvas avec des blocs rectangulaires. L'approche est similaire, mais le vocabulaire et l'organisation different. OttoKit mise davantage sur la simplicite de configuration que sur la richesse visuelle.

Les deux sont visuels et accessibles. Question de preference personnelle.

**[ECRAN — slide "Pricing : operations vs tasks"]**

Attention, les unites ne sont pas les memes :

- **OttoKit** compte en **tasks** : 1 action executee = 1 task
- **Make** compte en **operations** : chaque module execute = 1 operation (y compris les filtres et les transformations dans certains cas)

Un scenario Make avec 5 modules peut consommer 5 operations pour un seul run. Le calcul n'est pas toujours direct.

En entree de gamme, Make est moins cher (9$/mois pour 10K operations). Mais compare bien : 10K operations Make ne correspondent pas a 10K tasks OttoKit.

**[ECRAN — slide "WordPress : le point de bascule"]**

C'est la meme histoire qu'avec Zapier. Make n'a pas de plugin WordPress natif. Tu connectes WordPress via HTTP requests, webhooks ou modules generiques.

OttoKit a le plugin. Les events WordPress, WooCommerce, FluentCRM, TutorLMS sont accessibles directement. Pas de configuration supplementaire.

Si WordPress est ton ecosysteme principal, OttoKit a un avantage structurel.

**[ECRAN — slide "API et scenarios complexes"]**

Make a un point fort : la gestion des API. Les modules HTTP, JSON, et les fonctions de transformation de donnees sont robustes. Si tu fais beaucoup d'appels API custom, de parsing de donnees, ou de scenarios avec des branches complexes, Make est bien equipe.

OttoKit couvre ces cas mais avec moins de granularite. Pour des scenarios purement API, Make est souvent plus comfortable.

**[ECRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Tu es centre sur WordPress
- Tu veux les AI Agents et MCP
- Tu preferes un prix previsible par task

**Choisis Make si** :
- Tu fais beaucoup d'appels API custom
- Tu as besoin des 1 800+ integrations
- Tu veux un pricing d'entree tres bas
- Tes automatisations ne sont pas centrees sur WordPress

**[TRANSITION — face camera]**

Tu as maintenant les elements pour comparer OttoKit avec Zapier, n8n et Make. Mais au lieu de choisir en theorie, utilisons un arbre de decision. C'est ce qu'on fait dans la prochaine lecon.

---

**Points cles**
- Make et OttoKit ont des interfaces visuelles similaires (canvas)
- Pricing : Make compte en operations, OttoKit en tasks — comparer avec prudence
- Make excelle sur les API custom et les scenarios complexes
- OttoKit excelle sur l'integration WordPress native et les AI Agents

**Mots-cles SEO**
- OttoKit vs Make
- OttoKit vs Integromat
- Make ou OttoKit WordPress
- comparatif Make OttoKit automatisation

---

## Lecon 14.5 — Arbre de decision : quel outil pour quel besoin

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides arbre de decision, exercice 3 scenarios

---

**[INTRO — face camera]**

Tu connais les forces et faiblesses de chaque outil. Mais quand un client te demande "je dois automatiser ca, qu'est-ce que tu recommandes ?", il faut une reponse rapide et fondee. Voici l'arbre de decision que j'utilise.

**[ECRAN — slide "Arbre de decision — 5 questions"]**

```
Question 1 : Ton ecosysteme est-il centre sur WordPress ?
├── OUI → Question 2
└── NON → Question 4

Question 2 : As-tu besoin de connecter des apps externes (non-WordPress) ?
├── NON (WordPress pur) → Uncanny Automator ou OttoKit
└── OUI → Question 3

Question 3 : As-tu besoin d'AI Agents ou de + de 1000 integrations ?
├── OUI → OttoKit
└── NON (quelques apps simples) → OttoKit ou Make

Question 4 : As-tu besoin de coder dans tes workflows ?
├── OUI → n8n
└── NON → Question 5

Question 5 : Le volume de tasks est-il eleve (> 5000/mois) ?
├── OUI → Make ou OttoKit
└── NON → Zapier (plan Starter) ou Make
```

**[ECRAN — slide "Matrice de decision visuelle"]**

| Besoin | Meilleur choix | Alternative |
|---|---|---|
| WordPress pur (plugins entre eux) | Uncanny Automator | OttoKit |
| WordPress + apps SaaS | OttoKit | Make |
| WordPress + AI Agents + MCP | OttoKit | — |
| Multi-plateforme, pas de WordPress | Zapier ou Make | — |
| Pipelines complexes, code custom | n8n | Make |
| Budget zero, self-hosted | n8n (self-hosted) | — |
| Volume eleve, cout maitrise | OttoKit ou n8n | Make |

**[ECRAN — slide "Scenario 1 : Sophie, formatrice en ligne"]**

Appliquons l'arbre a 3 scenarios reels.

**Sophie** vend des formations sur WordPress avec TutorLMS. Elle veut automatiser l'inscription, l'email de bienvenue et l'ajout dans FluentCRM.

- Ecosysteme centre sur WordPress ? **Oui.**
- Apps externes ? **Non** — tout est dans WordPress.
- AI Agents ? **Non** — pas besoin pour l'instant.

Recommandation : **OttoKit**. Integration native avec TutorLMS et FluentCRM. Pas besoin de Zapier pour ca.

**[ECRAN — slide "Scenario 2 : Marc, e-commercant multi-canal"]**

**Marc** vend sur WooCommerce, Amazon et Shopify. Il veut synchroniser les stocks entre les 3 plateformes et envoyer les commandes dans son ERP.

- Ecosysteme centre sur WordPress ? **Partiellement** — il a WooCommerce mais aussi Amazon et Shopify.
- Apps externes ? **Oui** — Amazon, Shopify, ERP.
- Code necessaire ? **Probablement** — la synchronisation de stocks est complexe.

Recommandation : **n8n** pour le pipeline de synchronisation (code + API custom). **OttoKit** pour les automatisations WooCommerce internes. Deux outils, chacun dans son domaine.

**[ECRAN — slide "Scenario 3 : Julie, coach avec peu de budget"]**

**Julie** est coach. Elle a un site WordPress avec un formulaire de contact. Elle veut que chaque formulaire soumis arrive dans Google Sheets et declenche un email.

- Ecosysteme centre sur WordPress ? **Oui.**
- Apps externes ? **Oui** — Google Sheets.
- Volume ? **Faible** — 50 formulaires par mois.
- Budget ? **Le moins possible.**

Recommandation : **OttoKit** (plan gratuit si disponible) ou **Make** (9$/mois). Pour 50 tasks par mois, les deux font le travail. OttoKit a l'avantage du plugin WordPress natif.

**[ECRAN — slide "Le calcul ROI : Zapier vs OttoKit pour 10K tasks/mois"]**

Pour finir, un calcul concret :

| | OttoKit Pro | Zapier Team |
|---|---|---|
| Tasks/mois | 50 000 | ~10 000 |
| Cout mensuel | 99$ | ~200-300$ |
| Cout annuel | 1 188$ | 2 400-3 600$ |
| Economie OttoKit | — | 1 200 a 2 400$/an |

Pour un createur de cours en ligne qui genere 10 000 tasks par mois (inscriptions, emails, CRM, notifications), OttoKit coute 2 a 3 fois moins cher que Zapier. L'economie annuelle paye largement l'investissement en configuration.

**[TRANSITION — face camera]**

L'arbre de decision te donne une reponse en 30 secondes. Mais la reponse la plus puissante, c'est souvent de combiner deux outils. C'est exactement ce qu'on fait chez schoolsWP. On en parle dans la prochaine lecon.

---

**Points cles**
- 5 questions suffisent pour orienter vers le bon outil
- WordPress pur → OttoKit ou Uncanny Automator
- Multi-plateforme + code → n8n
- Volume eleve + budget controle → OttoKit ou n8n self-hosted
- Le ROI OttoKit vs Zapier est clair a 10K+ tasks/mois

**Mots-cles SEO**
- choisir outil automatisation WordPress
- OttoKit vs Zapier vs n8n decision
- quel outil automatisation 2026
- comparatif cout automatisation WordPress

---

## Lecon 14.6 — Combiner OttoKit + n8n : le meilleur des deux mondes

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides architecture hybride, schema de flux

---

**[INTRO — face camera]**

Chez schoolsWP, on ne choisit pas entre OttoKit et n8n. On utilise les deux. OttoKit gere tout ce qui touche a WordPress. n8n gere les pipelines de contenu, les appels API complexes et les traitements de donnees. Les deux communiquent par webhook. Voici comment ca marche.

**[ECRAN — slide "Le principe : chacun dans son domaine"]**

```
WordPress (OttoKit)          Pipelines (n8n)
─────────────────           ──────────────
Inscriptions                 Production contenu
Commandes WooCommerce        Analyse SEO
Emails FluentCRM             Appels API (Claude, Firecrawl)
Notifications Slack          Transformation de donnees
Tags et segments CRM         Synchronisation externe
       │                            │
       └────── webhook ──────────────┘
```

OttoKit reste dans WordPress. n8n fait tout ce qui depasse WordPress. Le webhook est le pont entre les deux.

**[ECRAN — slide "Exemple 1 : Inscription → Pipeline de bienvenue"]**

Voici un flux reel :

1. Un utilisateur s'inscrit sur le site → **OttoKit detecte** (trigger WordPress natif)
2. OttoKit ajoute le contact dans FluentCRM → **OttoKit execute** (action WordPress)
3. OttoKit envoie un webhook a n8n avec les donnees de l'inscrit → **pont webhook**
4. n8n lance un pipeline : generer un email personnalise avec Claude, verifier le profil LinkedIn, enrichir les donnees → **n8n execute** (traitement complexe)
5. n8n renvoie les donnees enrichies a OttoKit via webhook → **pont webhook**
6. OttoKit met a jour le contact FluentCRM avec les donnees enrichies → **OttoKit execute**

Chaque outil fait ce qu'il fait de mieux. OttoKit n'essaie pas de faire du traitement API complexe. n8n n'essaie pas de gerer les hooks WordPress.

**[ECRAN — slide "Exemple 2 : Publication automatique de contenu"]**

Un autre flux schoolsWP :

1. n8n genere un article via le pipeline de contenu (analyse SEO → redaction → audit)
2. n8n envoie l'article fini via webhook a OttoKit
3. OttoKit publie l'article dans WordPress (via le plugin natif)
4. OttoKit declenche les actions post-publication : email a la liste, notification Slack, mise a jour du tableau de bord

n8n produit. OttoKit distribue.

**[ECRAN — slide "Comment configurer le webhook pont"]**

Le webhook est simple a configurer :

**Cote OttoKit (envoi)** :
- Ajoute une action "Webhook" dans ton workflow
- Colle l'URL du webhook n8n
- Selectionne les donnees a envoyer (email, nom, ID)

**Cote n8n (reception)** :
- Cree un noeud "Webhook" comme trigger
- Copie l'URL generee
- Colle-la dans l'action OttoKit

**Cote n8n (envoi retour)** :
- Ajoute un noeud "HTTP Request" en fin de workflow
- Cible l'URL du webhook OttoKit

Ca prend 5 minutes a configurer. Et ca fonctionne de facon fiable.

**[ECRAN — slide "Architecture hybride schoolsWP"]**

Voici l'architecture complete :

```
┌─────────────────────────────┐
│   OttoKit (WordPress)       │
│                             │
│  Triggers WordPress         │
│  → Inscriptions             │
│  → Commandes                │
│  → Formulaires              │
│                             │
│  Actions WordPress          │
│  → Emails FluentCRM         │
│  → Publication articles     │
│  → Notifications            │
│  → Mise a jour CRM          │
└──────────┬──────────────────┘
           │ webhooks
┌──────────▼──────────────────┐
│   n8n (Pipelines)           │
│                             │
│  Production de contenu      │
│  → Analyse SEO (API)        │
│  → Redaction (Claude API)   │
│  → Audit qualite            │
│                             │
│  Traitements complexes      │
│  → Enrichissement donnees   │
│  → Synchronisation externe  │
│  → Reporting automatise     │
└─────────────────────────────┘
```

**[ECRAN — slide "Quand combiner, quand choisir un seul"]**

Tu n'as pas toujours besoin des deux. Voici le guide :

- **WordPress seul** (inscriptions, emails, CRM) → OttoKit suffit
- **Pipelines complexes seuls** (API, code, data) → n8n suffit
- **WordPress + pipelines complexes** → OttoKit + n8n combines
- **Budget zero** → n8n self-hosted pour tout (avec webhook WordPress)

**[TRANSITION — face camera]**

OttoKit et n8n ensemble, c'est ce qui fait tourner schoolsWP au quotidien. Chaque outil dans son domaine, relies par un pont webhook. C'est la derniere lecon de contenu de cette formation. On valide tout ca dans le quiz final.

---

**Points cles**
- OttoKit pour WordPress (triggers, actions, CRM, emails)
- n8n pour les pipelines complexes (API, code, data, contenu)
- Le webhook est le pont : 5 minutes a configurer, fiable en production
- On combine quand le besoin couvre les deux domaines

**Mots-cles SEO**
- OttoKit et n8n ensemble
- combiner OttoKit n8n webhook
- architecture automatisation WordPress hybride
- OttoKit n8n schoolsWP

---

## Lecon 14.7 — Quiz final M14 — 10 questions

**Duree** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif — 10 questions. Pas de script video. Questions generees dans le LMS.

---

# Notes de production — Module 14

**Angle schoolsWP** : Module ancre dans l'experience reelle — schoolsWP utilise OttoKit (WordPress) ET n8n (pipelines contenu). L'arbre de decision est calibre pour les createurs de cours en ligne. Le calcul ROI compare Zapier et OttoKit sur 10K tasks/mois — le coeur de cible schoolsWP.

**Faits cles integres dans les scripts** :
- OttoKit : 1 310+ integrations, AI Agents + MCP, 39$/mois annuel, par Brainstorm Force
- Zapier : 7 000+ integrations, pas de plugin WP natif, 20$/mois starter mais 100$+ a volume
- n8n : self-hosted gratuit ou cloud, 400+ noeuds, code JS/Python, pas d'AI Agents natif
- Make : 1 800+ integrations, 9$/mois entree, bonne gestion API, pas de plugin WP
- Uncanny Automator : WordPress-only, simple, pas d'apps externes

**Assets necessaires** :
- Matrice de positionnement (simplicite vs puissance) avec les 6 outils
- Tableaux comparatifs (OttoKit vs Zapier, vs n8n, vs Make)
- Arbre de decision en 5 questions
- 3 fiches personas (Sophie, Marc, Julie)
- Schema architecture hybride OttoKit + n8n
- Tableau calcul ROI Zapier vs OttoKit

**Enchainement des lecons** :
- 14.1 → 14.2 : du panorama au premier duel (OttoKit vs Zapier)
- 14.2 → 14.3 : du concurrent commercial au concurrent technique (n8n)
- 14.3 → 14.4 : de n8n a Make (couvrir les 3 principaux concurrents)
- 14.4 → 14.5 : des comparaisons a la decision (synthese)
- 14.5 → 14.6 : de la decision a l'action (combiner les outils)

**Quiz final M14 — 10 questions suggerees** (a generer dans le LMS) :
1. Combien d'integrations propose OttoKit ? (1 310+)
2. Quelle est la difference principale entre OttoKit et Zapier pour WordPress ? (plugin natif)
3. n8n est-il gratuit ? (oui en self-hosted, payant en cloud)
4. Qu'est-ce qui fait le pont entre OttoKit et n8n ? (webhook)
5. Pour 10K tasks/mois, lequel est le moins cher : OttoKit ou Zapier ? (OttoKit)
6. Make compte en operations ou en tasks ? (operations)
7. Quel outil recommander pour des automatisations purement WordPress sans apps externes ? (Uncanny Automator ou OttoKit)
8. Quel outil permet d'ecrire du code JavaScript dans les workflows ? (n8n)
9. OttoKit propose des AI Agents natifs — vrai ou faux ? (vrai)
10. Quel est le cas d'usage ideal pour combiner OttoKit + n8n ? (WordPress + pipelines complexes)

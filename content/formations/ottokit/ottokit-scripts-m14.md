# Scripts vidéo — Module 14 : OttoKit vs n8n vs Zapier : choisir le bon outil

**Formation** : Maîtriser OttoKit
**Module** : M14 — OttoKit vs n8n vs Zapier : choisir le bon outil
**Leçons** : 6 vidéos + 1 quiz (10 questions)
**Durée totale** : ~40 min de vidéo
**Date** : 2026-03-30

---

## Leçon 14.1 — Le paysage des outils d'automatisation en 2026

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides cartographie outils

---

**[INTRO — face caméra]**

Tu connais OttoKit. Mais OttoKit n'est pas le seul outil d'automatisation. En 2026, il en existe des dizaines. Certains sont génériques, d'autres sont spécialisés WordPress. Certains sont gratuits, d'autres coûtent des centaines d'euros par mois. Pour faire le bon choix, tu dois d'abord connaître le terrain.

**[ÉCRAN — slide "Les 6 acteurs principaux"]**

Voici les 6 outils que tu vas rencontrer le plus souvent :

**1. OttoKit** (anciennement SureTriggers)
- Par Brainstorm Force (les créateurs d'Astra et Spectra)
- Cloud + plugin WordPress natif
- 1 310+ intégrations
- AI Agents et MCP intégrés
- À partir de 39$/mois (facturation annuelle)

**2. Zapier**
- Le leader historique de l'automatisation no-code
- Cloud pur, pas de plugin WordPress natif
- 7 000+ intégrations — le catalogue le plus large
- À partir de 20$/mois, mais monte vite (100$+ pour du volume)

**3. Make** (anciennement Integromat)
- Cloud, interface visuelle très appréciée
- 1 800+ intégrations
- Pricing intermédiaire
- Bonne gestion des API et des scénarios complexes

**4. n8n**
- Self-hosted (gratuit) ou cloud (payant)
- 400+ nœuds natifs
- Code possible (JavaScript, Python)
- Plus technique, plus puissant, pas d'AI Agents natif

**5. Uncanny Automator**
- Plugin WordPress uniquement
- Connecte les plugins WP entre eux
- Pas de connexion aux apps externes (ou très limitée)
- Simple et fiable pour des automatisations purement WordPress

**6. Bit Integrations (anciennement Bit Flows)**
- Plugin WordPress
- Connecte formulaires et CRM
- Plus limité, mais gratuit pour les bases

**[ÉCRAN — slide "La carte du marche"]**

[Matrice 2 axes : Simplicité (vertical) vs Puissance (horizontal)]
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

En bas à droite : puissant mais complexe (n8n). En haut à gauche : simple mais limité (Uncanny Automator, Bit Flows). OttoKit, Zapier et Make sont au milieu — un compromis entre accessibilité et capacités.

**[ÉCRAN — slide "Les questions a se poser"]**

Avant de comparer, pose-toi ces 5 questions :

1. **Combien d'automatisations ai-je besoin ?** (5 ou 500 ?)
2. **Mon écosystème est-il centré sur WordPress ?** (ou multi-plateforme ?)
3. **Quel est mon budget mensuel ?** (0, 50, 200$ ?)
4. **Ai-je besoin d'héberger moi-même ?** (conformité, sécurité ?)
5. **Quel est mon niveau technique ?** (no-code, low-code, code ?)

Les réponses à ces questions orientent directement vers le bon outil.

**[TRANSITION — face caméra]**

Maintenant qu'on a la vue d'ensemble, on va comparer OttoKit face à face avec chaque concurrent. On commence par le plus connu : Zapier.

---

**Points clés**
- 6 outils principaux en 2026 : OttoKit, Zapier, Make, n8n, Uncanny Automator, Bit Flows
- Chaque outil a un positionnement différent (simplicité vs puissance, générique vs WordPress)
- 5 questions guident le choix : volume, écosystème, budget, hébergement, niveau technique
- Il n'y a pas d'outil parfait — il y a l'outil adapte a ton contexte

**Mots-clés SEO**
- comparatif automatisation WordPress 2026
- OttoKit vs Zapier vs n8n
- meilleur outil automatisation WordPress
- alternative Zapier WordPress

---

## Leçon 14.2 — OttoKit vs Zapier : coût, intégrations, WordPress

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs

---

**[INTRO — face caméra]**

Zapier est la référence du marché. Plus de 7 000 intégrations, une marque connue, des millions d'utilisateurs. Mais est-ce le meilleur choix quand ton écosystème est centré sur WordPress ? Comparons point par point.

**[ÉCRAN — slide "Comparatif sur 5 criteres"]**

| Critère | OttoKit | Zapier |
|---|---|---|
| **Intégration WordPress** | Native (plugin) — accès direct aux hooks WP, WooCommerce, LMS, CRM | Via API/webhook — pas de plugin, pas d'accès natif aux hooks |
| **Nombre d'intégrations** | 1 310+ | 7 000+ |
| **AI intégrée** | AI Agents + MCP | AI Actions (beta) |
| **Pricing (entrée)** | 39$/mois (annuel) | 20$/mois (Starter — 750 tasks) |
| **Pricing (volume)** | 99$/mois (50K tasks) | 100$+/mois des 2 000 tasks |

**[ÉCRAN — slide "Critère 1 : Intégration WordPress"]**

C'est la différence fondamentale. OttoKit a un plugin installé sur ton WordPress. Ce plugin donne un accès direct aux événements internes : un utilisateur s'inscrit, un formulaire est soumis, un cours est terminé, un tag CRM est ajouté.

Zapier n'a pas de plugin WordPress. Pour connecter WordPress à Zapier, tu passes par des plugins tiers (WP Webhooks, Zapier for WooCommerce) ou par l'API REST. Ça fonctionne, mais c'est un intermédiaire supplémentaire. Et chaque intermédiaire est un point de fragilité.

**[ÉCRAN — slide "Critère 2 : Catalogue d'intégrations"]**

Zapier a clairement l'avantage ici. 7 000 intégrations contre 1 310. Si tu as besoin de connecter des apps de niche — un CRM spécifique, un outil de comptabilité exotique, un logiciel métier — Zapier a plus de chances de le supporter.

Mais pose-toi la question : combien d'apps connectes-tu réellement ? La plupart des utilisateurs WordPress en utilisent 5 à 10. Et ces 5 à 10 sont presque toujours supportées par OttoKit.

**[ÉCRAN — slide "Critère 3 : Coût à volume"]**

C'est ici que la différence se creuse. Calculons pour 10 000 tasks par mois :

- **OttoKit** : 99$/mois (plan Pro, 50 000 tasks) → largement couvert
- **Zapier** : environ 200-300$/mois (plan Team ou plus) → le pricing de Zapier augmente rapidement avec le volume

Sur un an, ça représente une différence de 1 200 à 2 400$. Pour un freelance ou une petite entreprise, c'est significatif.

**[ÉCRAN — slide "Critere 4 : Experience utilisateur"]**

Les deux interfaces sont visuelles. Zapier utilise un éditeur linéaire (étape par étape). OttoKit utilise un canvas (drag-and-drop). Le canvas est plus flexible pour les workflows avec des branches et des conditions.

Question de préférence : si tu aimes la linéarité, Zapier. Si tu préfères voir l'ensemble du workflow d'un coup, OttoKit.

**[ÉCRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Ton écosystème est centré sur WordPress
- Tu veux une intégration native avec tes plugins WP
- Tu gères un volume de tasks moyen à élevé
- Tu veux les AI Agents intégrés

**Choisis Zapier si** :
- Tu connectes beaucoup d'apps non-WordPress
- Tu as besoin d'une app de niche que seul Zapier supporte
- Le volume de tasks est faible (< 750/mois — le plan Starter suffit)

**[TRANSITION — face caméra]**

Zapier est fort sur le catalogue universel. Mais pour WordPress, OttoKit est plus pertinent et moins cher. Comparons maintenant avec un outil très différent : n8n.

---

**Points clés**
- OttoKit : intégration WordPress native, pricing avantageux à volume, AI Agents
- Zapier : catalogue d'intégrations plus large (7 000+), mais pas de plugin WordPress
- À 10 000 tasks/mois, OttoKit coûte 2 à 3 fois moins cher que Zapier
- Le choix dépend de l'écosystème : centré WordPress → OttoKit, multi-plateforme → Zapier

**Mots-clés SEO**
- OttoKit vs Zapier
- OttoKit vs Zapier prix
- alternative Zapier WordPress moins cher
- OttoKit ou Zapier automatisation

---

## Leçon 14.3 — OttoKit vs n8n : cloud vs self-hosted, simple vs puissant

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs

---

**[INTRO — face caméra]**

n8n, c'est l'outil des développeurs et des tech-savvy. Open-source, self-hosted, avec la possibilité d'écrire du code dans les workflows. Chez schoolsWP, on utilise les deux : OttoKit pour les automatisations WordPress, n8n pour les pipelines de contenu et les traitements complexes. Comparons.

**[ÉCRAN — slide "Comparatif sur 5 criteres"]**

| Critère | OttoKit | n8n |
|---|---|---|
| **Hébergement** | Cloud (géré par OttoKit) | Self-hosted (gratuit) ou cloud (payant) |
| **Interface** | Canvas visuel, no-code | Canvas visuel + code (JS/Python) |
| **Intégrations** | 1 310+ (natives) | 400+ nœuds + HTTP/code custom |
| **AI** | AI Agents + MCP natifs | Pas d'AI Agents natif |
| **WordPress** | Plugin natif (hooks directs) | Via webhook ou API REST |
| **Coût** | 39$/mois (annuel) | Gratuit (self-hosted) ou 20€+/mois (cloud) |

**[ÉCRAN — slide "Architecture : cloud vs self-hosted"]**

C'est la différence la plus importante.

**OttoKit** est entièrement cloud. Tu crées un compte, tu connectes tes apps, tu construis tes workflows. L'infrastructure est gérée par OttoKit. Tu ne touches à aucun serveur.

**n8n self-hosted** tourne sur ton propre serveur. Tu installes, tu configures, tu mets à jour, tu gères les backups. En échange, tu as un contrôle total sur tes données et aucune limite de tasks.

Si tu n'as pas de serveur et que tu ne veux pas en gérer un, OttoKit. Si tu as déjà un VPS et que tu es à l'aise avec Docker, n8n self-hosted peut être gratuit à vie.

**[ÉCRAN — slide "Complexite : no-code vs low-code"]**

**OttoKit** est no-code. Tu sélectionnes des apps, tu mappes des champs, tu publies. Pas de code à écrire. C'est accessible à quelqu'un qui n'a jamais programmé.

**n8n** est low-code. Tu peux faire beaucoup sans coder, mais les nœuds Code (JavaScript, Python) sont ce qui rend n8n vraiment puissant. Transformer des données, appeler des API custom, gérer des boucles complexes — c'est là que n8n brille.

Si tu ne codes pas → OttoKit. Si tu es à l'aise avec JavaScript ou Python → n8n débloque des possibilités qu'OttoKit n'offre pas.

**[ÉCRAN — slide "WordPress natif vs webhook"]**

OttoKit se connecte a WordPress via un plugin. Il accede directement aux hooks WordPress, WooCommerce, FluentCRM, TutorLMS. Le trigger "un utilisateur complete un cours" est un evenement natif.

n8n se connecte à WordPress via webhook ou API REST. Ça fonctionne, mais tu dois configurer le webhook côté WordPress (avec un plugin tiers ou du code). C'est moins direct.

Pour les automatisations purement WordPress, OttoKit est plus rapide a configurer.

**[ÉCRAN — slide "AI et agents"]**

OttoKit a intégré les AI Agents et le protocole MCP directement dans la plateforme. Tu peux créer des agents qui utilisent tes workflows comme outils.

n8n n'a pas d'AI Agents natif. Tu peux appeler des API d'IA (OpenAI, Claude) via des nœuds HTTP ou Code, mais il n'y a pas de système d'agents intégré. C'est plus manuel.

**[ÉCRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Tu veux du no-code pur
- Tes automatisations sont centrees sur WordPress
- Tu veux les AI Agents et MCP
- Tu ne veux pas gérer de serveur

**Choisis n8n si** :
- Tu veux un contrôle total (données, infrastructure)
- Tu codes en JavaScript ou Python
- Tu as des pipelines complexes (transformation de données, boucles, API custom)
- Tu veux zéro coût d'outil (self-hosted)

**[TRANSITION — face caméra]**

Ce n'est pas OttoKit ou n8n. C'est souvent OttoKit et n8n. On verra comment les combiner à la fin du module. Avant ça, comparons OttoKit avec Make.

---

**Points clés**
- OttoKit = cloud, no-code, WordPress natif, AI Agents
- n8n = self-hosted possible, code possible, plus de contrôle, pas d'AI Agents
- OttoKit pour les automatisations WordPress ; n8n pour les pipelines complexes
- Les deux ne sont pas concurrents — ils sont complémentaires

**Mots-clés SEO**
- OttoKit vs n8n
- OttoKit vs n8n comparatif
- n8n WordPress automatisation
- OttoKit ou n8n lequel choisir

---

## Leçon 14.4 — OttoKit vs Make : interface, pricing, performance

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs

---

**[INTRO — face caméra]**

Make — anciennement Integromat — est un concurrent direct d'OttoKit et Zapier. Interface visuelle, tarification au volume, bonne gestion des API. Voyons où chacun se positionne.

**[ÉCRAN — slide "Comparatif sur 5 criteres"]**

| Critère | OttoKit | Make |
|---|---|---|
| **Interface** | Canvas drag-and-drop | Canvas visuel (scénarios) |
| **Intégrations** | 1 310+ | 1 800+ |
| **WordPress natif** | Oui (plugin) | Non (via HTTP/webhook) |
| **AI** | AI Agents + MCP | AI (modules ChatGPT, etc.) |
| **Pricing** | 39$/mois (annuel) | 9$/mois (10K ops) à 16$/mois (40K ops) |

**[ÉCRAN — slide "Interface et experience"]**

Les deux outils utilisent un canvas visuel. Mais l'approche est différente.

**Make** utilise des "scénarios" avec des cercles connectés par des lignes. C'est très visuel. Les filtres, les routeurs et les itérateurs sont des composants graphiques que tu places sur le canvas. L'interface est appréciée pour sa clarté.

**OttoKit** utilise un canvas avec des blocs rectangulaires. L'approche est similaire, mais le vocabulaire et l'organisation diffèrent. OttoKit mise davantage sur la simplicité de configuration que sur la richesse visuelle.

Les deux sont visuels et accessibles. Question de préférence personnelle.

**[ÉCRAN — slide "Pricing : opérations vs tasks"]**

Attention, les unites ne sont pas les memes :

- **OttoKit** compte en **tasks** : 1 action exécutée = 1 task
- **Make** compte en **opérations** : chaque module exécuté = 1 opération (y compris les filtres et les transformations dans certains cas)

Un scénario Make avec 5 modules peut consommer 5 opérations pour un seul run. Le calcul n'est pas toujours direct.

En entrée de gamme, Make est moins cher (9$/mois pour 10K opérations). Mais compare bien : 10K opérations Make ne correspondent pas à 10K tasks OttoKit.

**[ÉCRAN — slide "WordPress : le point de bascule"]**

C'est la même histoire qu'avec Zapier. Make n'a pas de plugin WordPress natif. Tu connectes WordPress via HTTP requests, webhooks ou modules génériques.

OttoKit a le plugin. Les events WordPress, WooCommerce, FluentCRM, TutorLMS sont accessibles directement. Pas de configuration supplémentaire.

Si WordPress est ton écosystème principal, OttoKit a un avantage structurel.

**[ÉCRAN — slide "API et scénarios complexes"]**

Make a un point fort : la gestion des API. Les modules HTTP, JSON, et les fonctions de transformation de données sont robustes. Si tu fais beaucoup d'appels API custom, de parsing de données, ou de scénarios avec des branches complexes, Make est bien équipé.

OttoKit couvre ces cas mais avec moins de granularité. Pour des scénarios purement API, Make est souvent plus confortable.

**[ÉCRAN — slide "Verdict"]**

**Choisis OttoKit si** :
- Tu es centre sur WordPress
- Tu veux les AI Agents et MCP
- Tu préfères un prix prévisible par task

**Choisis Make si** :
- Tu fais beaucoup d'appels API custom
- Tu as besoin des 1 800+ intégrations
- Tu veux un pricing d'entrée très bas
- Tes automatisations ne sont pas centrées sur WordPress

**[TRANSITION — face caméra]**

Tu as maintenant les éléments pour comparer OttoKit avec Zapier, n8n et Make. Mais au lieu de choisir en théorie, utilisons un arbre de décision. C'est ce qu'on fait dans la prochaine leçon.

---

**Points clés**
- Make et OttoKit ont des interfaces visuelles similaires (canvas)
- Pricing : Make compte en opérations, OttoKit en tasks — comparer avec prudence
- Make excelle sur les API custom et les scénarios complexes
- OttoKit excelle sur l'intégration WordPress native et les AI Agents

**Mots-clés SEO**
- OttoKit vs Make
- OttoKit vs Integromat
- Make ou OttoKit WordPress
- comparatif Make OttoKit automatisation

---

## Leçon 14.5 — Arbre de décision : quel outil pour quel besoin

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides arbre de décision, exercice 3 scénarios

---

**[INTRO — face caméra]**

Tu connais les forces et faiblesses de chaque outil. Mais quand un client te demande "je dois automatiser ça, qu'est-ce que tu recommandes ?", il faut une réponse rapide et fondée. Voici l'arbre de décision que j'utilise.

**[ÉCRAN — slide "Arbre de décision — 5 questions"]**

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

**[ÉCRAN — slide "Matrice de décision visuelle"]**

| Besoin | Meilleur choix | Alternative |
|---|---|---|
| WordPress pur (plugins entre eux) | Uncanny Automator | OttoKit |
| WordPress + apps SaaS | OttoKit | Make |
| WordPress + AI Agents + MCP | OttoKit | — |
| Multi-plateforme, pas de WordPress | Zapier ou Make | — |
| Pipelines complexes, code custom | n8n | Make |
| Budget zero, self-hosted | n8n (self-hosted) | — |
| Volume élevé, coût maîtrisé | OttoKit ou n8n | Make |

**[ÉCRAN — slide "Scénario 1 : Sophie, formatrice en ligne"]**

Appliquons l'arbre à 3 scénarios réels.

**Sophie** vend des formations sur WordPress avec TutorLMS. Elle veut automatiser l'inscription, l'email de bienvenue et l'ajout dans FluentCRM.

- Écosystème centré sur WordPress ? **Oui.**
- Apps externes ? **Non** — tout est dans WordPress.
- AI Agents ? **Non** — pas besoin pour l'instant.

Recommandation : **OttoKit**. Intégration native avec TutorLMS et FluentCRM. Pas besoin de Zapier pour ça.

**[ÉCRAN — slide "Scénario 2 : Marc, e-commerçant multi-canal"]**

**Marc** vend sur WooCommerce, Amazon et Shopify. Il veut synchroniser les stocks entre les 3 plateformes et envoyer les commandes dans son ERP.

- Écosystème centré sur WordPress ? **Partiellement** — il a WooCommerce mais aussi Amazon et Shopify.
- Apps externes ? **Oui** — Amazon, Shopify, ERP.
- Code nécessaire ? **Probablement** — la synchronisation de stocks est complexe.

Recommandation : **n8n** pour le pipeline de synchronisation (code + API custom). **OttoKit** pour les automatisations WooCommerce internes. Deux outils, chacun dans son domaine.

**[ÉCRAN — slide "Scénario 3 : Julie, coach avec peu de budget"]**

**Julie** est coach. Elle a un site WordPress avec un formulaire de contact. Elle veut que chaque formulaire soumis arrive dans Google Sheets et déclenche un email.

- Écosystème centré sur WordPress ? **Oui.**
- Apps externes ? **Oui** — Google Sheets.
- Volume ? **Faible** — 50 formulaires par mois.
- Budget ? **Le moins possible.**

Recommandation : **OttoKit** (plan gratuit si disponible) ou **Make** (9$/mois). Pour 50 tasks par mois, les deux font le travail. OttoKit a l'avantage du plugin WordPress natif.

**[ÉCRAN — slide "Le calcul ROI : Zapier vs OttoKit pour 10K tasks/mois"]**

Pour finir, un calcul concret :

| | OttoKit Pro | Zapier Team |
|---|---|---|
| Tasks/mois | 50 000 | ~10 000 |
| Coût mensuel | 99$ | ~200-300$ |
| Coût annuel | 1 188$ | 2 400-3 600$ |
| Économie OttoKit | — | 1 200 à 2 400$/an |

Pour un créateur de cours en ligne qui génère 10 000 tasks par mois (inscriptions, emails, CRM, notifications), OttoKit coûte 2 à 3 fois moins cher que Zapier. L'économie annuelle paye largement l'investissement en configuration.

**[TRANSITION — face caméra]**

L'arbre de décision te donne une réponse en 30 secondes. Mais la réponse la plus puissante, c'est souvent de combiner deux outils. C'est exactement ce qu'on fait chez schoolsWP. On en parle dans la prochaine leçon.

---

**Points clés**
- 5 questions suffisent pour orienter vers le bon outil
- WordPress pur → OttoKit ou Uncanny Automator
- Multi-plateforme + code → n8n
- Volume élevé + budget contrôlé → OttoKit ou n8n self-hosted
- Le ROI OttoKit vs Zapier est clair à 10K+ tasks/mois

**Mots-clés SEO**
- choisir outil automatisation WordPress
- OttoKit vs Zapier vs n8n décision
- quel outil automatisation 2026
- comparatif coût automatisation WordPress

---

## Leçon 14.6 — Combiner OttoKit + n8n : le meilleur des deux mondes

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides architecture hybride, schéma de flux

---

**[INTRO — face caméra]**

Chez schoolsWP, on ne choisit pas entre OttoKit et n8n. On utilise les deux. OttoKit gère tout ce qui touche à WordPress. n8n gère les pipelines de contenu, les appels API complexes et les traitements de données. Les deux communiquent par webhook. Voici comment ça marche.

**[ÉCRAN — slide "Le principe : chacun dans son domaine"]**

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

OttoKit reste dans WordPress. n8n fait tout ce qui dépasse WordPress. Le webhook est le pont entre les deux.

**[ÉCRAN — slide "Exemple 1 : Inscription → Pipeline de bienvenue"]**

Voici un flux reel :

1. Un utilisateur s'inscrit sur le site → **OttoKit détecte** (trigger WordPress natif)
2. OttoKit ajoute le contact dans FluentCRM → **OttoKit exécute** (action WordPress)
3. OttoKit envoie un webhook à n8n avec les données de l'inscrit → **pont webhook**
4. n8n lance un pipeline : générer un email personnalisé avec Claude, vérifier le profil LinkedIn, enrichir les données → **n8n exécute** (traitement complexe)
5. n8n renvoie les données enrichies à OttoKit via webhook → **pont webhook**
6. OttoKit met à jour le contact FluentCRM avec les données enrichies → **OttoKit exécute**

Chaque outil fait ce qu'il fait de mieux. OttoKit n'essaie pas de faire du traitement API complexe. n8n n'essaie pas de gérer les hooks WordPress.

**[ÉCRAN — slide "Exemple 2 : Publication automatique de contenu"]**

Un autre flux schoolsWP :

1. n8n génère un article via le pipeline de contenu (analyse SEO → rédaction → audit)
2. n8n envoie l'article fini via webhook a OttoKit
3. OttoKit publie l'article dans WordPress (via le plugin natif)
4. OttoKit déclenche les actions post-publication : email à la liste, notification Slack, mise à jour du tableau de bord

n8n produit. OttoKit distribue.

**[ÉCRAN — slide "Comment configurer le webhook pont"]**

Le webhook est simple a configurer :

**Côté OttoKit (envoi)** :
- Ajoute une action "Webhook" dans ton workflow
- Colle l'URL du webhook n8n
- Sélectionne les données à envoyer (email, nom, ID)

**Côté n8n (réception)** :
- Crée un nœud "Webhook" comme trigger
- Copie l'URL generee
- Colle-la dans l'action OttoKit

**Côté n8n (envoi retour)** :
- Ajoute un nœud "HTTP Request" en fin de workflow
- Cible l'URL du webhook OttoKit

Ça prend 5 minutes à configurer. Et ça fonctionne de façon fiable.

**[ÉCRAN — slide "Architecture hybride schoolsWP"]**

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

**[ÉCRAN — slide "Quand combiner, quand choisir un seul"]**

Tu n'as pas toujours besoin des deux. Voici le guide :

- **WordPress seul** (inscriptions, emails, CRM) → OttoKit suffit
- **Pipelines complexes seuls** (API, code, data) → n8n suffit
- **WordPress + pipelines complexes** → OttoKit + n8n combinés
- **Budget zero** → n8n self-hosted pour tout (avec webhook WordPress)

**[TRANSITION — face caméra]**

OttoKit et n8n ensemble, c'est ce qui fait tourner schoolsWP au quotidien. Chaque outil dans son domaine, reliés par un pont webhook. C'est la dernière leçon de contenu de cette formation. On valide tout ça dans le quiz final.

---

**Points clés**
- OttoKit pour WordPress (triggers, actions, CRM, emails)
- n8n pour les pipelines complexes (API, code, data, contenu)
- Le webhook est le pont : 5 minutes à configurer, fiable en production
- On combine quand le besoin couvre les deux domaines

**Mots-clés SEO**
- OttoKit et n8n ensemble
- combiner OttoKit n8n webhook
- architecture automatisation WordPress hybride
- OttoKit n8n schoolsWP

---

## Leçon 14.7 — Quiz final M14 — 10 questions

**Durée** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif — 10 questions. Pas de script vidéo. Questions générées dans le LMS.

---

# Notes de production — Module 14

**Angle schoolsWP** : Module ancré dans l'expérience réelle — schoolsWP utilise OttoKit (WordPress) ET n8n (pipelines contenu). L'arbre de décision est calibré pour les créateurs de cours en ligne. Le calcul ROI compare Zapier et OttoKit sur 10K tasks/mois — le cœur de cible schoolsWP.

**Faits clés intégrés dans les scripts** :
- OttoKit : 1 310+ intégrations, AI Agents + MCP, 39$/mois annuel, par Brainstorm Force
- Zapier : 7 000+ intégrations, pas de plugin WP natif, 20$/mois starter mais 100$+ à volume
- n8n : self-hosted gratuit ou cloud, 400+ nœuds, code JS/Python, pas d'AI Agents natif
- Make : 1 800+ intégrations, 9$/mois entrée, bonne gestion API, pas de plugin WP
- Uncanny Automator : WordPress-only, simple, pas d'apps externes

**Assets nécessaires** :
- Matrice de positionnement (simplicité vs puissance) avec les 6 outils
- Tableaux comparatifs (OttoKit vs Zapier, vs n8n, vs Make)
- Arbre de décision en 5 questions
- 3 fiches personas (Sophie, Marc, Julie)
- Schéma architecture hybride OttoKit + n8n
- Tableau calcul ROI Zapier vs OttoKit

**Enchaînement des leçons** :
- 14.1 → 14.2 : du panorama au premier duel (OttoKit vs Zapier)
- 14.2 → 14.3 : du concurrent commercial au concurrent technique (n8n)
- 14.3 → 14.4 : de n8n à Make (couvrir les 3 principaux concurrents)
- 14.4 → 14.5 : des comparaisons à la décision (synthèse)
- 14.5 → 14.6 : de la décision à l'action (combiner les outils)

**Quiz final M14 — 10 questions suggérées** (à générer dans le LMS) :
1. Combien d'intégrations propose OttoKit ? (1 310+)
2. Quelle est la différence principale entre OttoKit et Zapier pour WordPress ? (plugin natif)
3. n8n est-il gratuit ? (oui en self-hosted, payant en cloud)
4. Qu'est-ce qui fait le pont entre OttoKit et n8n ? (webhook)
5. Pour 10K tasks/mois, lequel est le moins cher : OttoKit ou Zapier ? (OttoKit)
6. Make compte en opérations ou en tasks ? (opérations)
7. Quel outil recommander pour des automatisations purement WordPress sans apps externes ? (Uncanny Automator ou OttoKit)
8. Quel outil permet d'écrire du code JavaScript dans les workflows ? (n8n)
9. OttoKit propose des AI Agents natifs — vrai ou faux ? (vrai)
10. Quel est le cas d'usage idéal pour combiner OttoKit + n8n ? (WordPress + pipelines complexes)

# Formation "FluentBoards de zéro à pro" — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produire et lancer en 9 semaines la première formation payante schoolsWP (FluentBoards standalone, audience D bâtisseur écosystème Fluent, stack TutorLMS + FluentCart + FluentCRM), prix 67 € early bird puis 97 €, avec 40 leçons, 4 livrables téléchargeables et un tunnel complet testé end-to-end.

**Architecture :** Course TutorLMS unique à 7 sections × 5-7 leçons, hébergé sur schoolswp.com. Chaque leçon suit un format standard (objectif + contexte + démo screen MP4 + texte + pièges + checklist). Fil rouge narratif = construire un Board Agence FluentBoards réutilisable, exporté en JSON à la fin du module 7. Tunnel FluentCart checkout + order bump → FluentCRM welcome automation + bridge inscription TutorLMS → accès cours. Acquisition = email liste + LinkedIn + article SEO schoolswp.com.

**Tech Stack :** TutorLMS (hébergement cours), FluentCart (checkout), FluentCRM (email + automation bridge), FluentBoards Pro (board fil rouge + live démos), n8n (10 workflows téléchargeables), OBS ou Loom (démos screen MP4), skill cc-design (sales page + PDF livrables), agents schoolsWP (studio, brain-lite, radar, pulse, flow) pour drafts parallélisables.

**Spec référence :** [docs/superpowers/specs/2026-04-21-formation-fluentboards-design.md](../specs/2026-04-21-formation-fluentboards-design.md)

**Note format :** Ce plan mélange des tâches de code (scripts, JSON workflows) et des tâches de production contenu (leçons, livrables, sales page). Pour les tâches contenu, les "steps" sont adaptés : draft → review → publish → commit au lieu de test → fail → impl → pass → commit. L'esprit reste atomique et vérifiable.

---

## Patterns réutilisables

Trois patterns utilisés dans les tâches ci-dessous. Chaque référence à un pattern cite son nom explicitement.

### Pattern L — Production d'une leçon TutorLMS

Appliqué à chacune des 40 leçons. Le brief complet de chaque leçon (objectif, pièges, checklist) est donné dans la tâche qui l'invoque.

1. **Draft texte** : déléguer à l'agent `studio` via une invocation précise incluant (a) l'objectif de la leçon, (b) les sources archivées à lire (paths exacts dans `content/docs/fluentboards/`), (c) la structure obligatoire (Objectif → Contexte → [placeholder démo] → Texte structuré → Pièges → Checklist), (d) la longueur cible (1 000-1 500 mots), (e) le tutoiement et les mots interdits `.claude/rules/branding.md`. Sortie : fichier `content/formations/fluentboards/modules/NN-module/NN-lesson.md`.
2. **Revue draft** : Michael relit, corrige ton/précision technique, marque les points à démoer en captures fixes vs clip MP4.
3. **Captures annotées** : screenshots de FluentBoards réel (board fil rouge), annotés (flèches + callouts) via Snagit/Flameshot. Sauvegardés dans `content/formations/fluentboards/assets/captures/NN-lesson/`.
4. **Démo screen MP4** : enregistrement OBS (ou Loom si clip < 5 min) selon le template OBS défini en Task 0.8. Clip 30-90 s, résolution 1920×1080, curseur visible, sans voix off AI ; voix humaine ou mute + callouts selon leçon. Sauvegardé dans `content/formations/fluentboards/assets/demos/NN-lesson.mp4`.
5. **Upload TutorLMS** : wp-admin → TutorLMS → Course "FluentBoards de zéro à pro" → Section N → Nouvelle leçon. Coller texte (markdown transformé en blocs Gutenberg), uploader le MP4 dans la médiathèque WP (dossier /formations/fluentboards/), intégrer dans la leçon, uploader les captures.
6. **Commit** : `git add content/formations/fluentboards/modules/NN/lesson.md content/formations/fluentboards/assets/captures/NN-lesson/` puis `git commit -m "feat(formation-fb): module N leçon N.M - titre"`. Les MP4 ne sont pas commités (trop lourds), ils restent sur WP + une copie locale non versionnée. `content/formations/fluentboards/assets/demos/` est ajouté au `.gitignore` dès Task 0.1.

### Pattern Q — Production d'un quiz TutorLMS

Appliqué 7 fois (un par module).

1. **Draft QCM** : déléguer à `studio` avec brief (a) le module concerné, (b) les objectifs pédagogiques des leçons de ce module, (c) 5-8 questions QCM à 4 choix chacune, (d) 1 bonne réponse + explication 1-2 phrases par question. Sortie : `content/formations/fluentboards/modules/NN-module/quiz.md`.
2. **Revue** : Michael relit, ajuste difficulté (viser taux réussite moyen ~75 %).
3. **Upload TutorLMS** : wp-admin → Course → Section N → Nouveau quiz. Seuil passage 70 %. Pas bloquant (l'apprenant peut continuer même s'il rate).
4. **Commit** : `git add content/formations/fluentboards/modules/NN/quiz.md` puis `git commit -m "feat(formation-fb): quiz module N"`.

### Pattern W — Production d'un workflow n8n téléchargeable

Appliqué 10 fois (3 workflows inclus formation + 7 order bump).

1. **Construction n8n** : sur l'instance n8n (schoolswp-n8n.wp1.host), créer le workflow en mode test. Nœuds nommés explicitement, credentials référencés par nom pas par ID.
2. **Test fonctionnel** : déclencher manuellement, vérifier que la task apparaît dans le board FluentBoards cible (ou l'action attendue).
3. **Export JSON** : n8n UI → workflow menu → Download → JSON. Sauvegarder dans `content/formations/fluentboards/livrables/workflows-n8n/NN-slug.json`.
4. **Sanitize** : ouvrir le JSON, vérifier qu'aucun credential inline (webhook secrets, API keys). Les credentials doivent être référencés par nom, l'utilisateur devra les reconfigurer.
5. **Doc README** : dans le même dossier, `README.md` décrivant prérequis + import steps pour chaque workflow.
6. **Commit** : `git add content/formations/fluentboards/livrables/workflows-n8n/` puis `git commit -m "feat(formation-fb): n8n workflow NN - titre"`.

---

## Phase 0 — Setup technique (S1 première moitié)

### Task 0.1: Créer l'arborisation repo

**Files :**
- Create : `content/formations/fluentboards/plan.md`
- Create : `content/formations/fluentboards/modules/01-setup/.gitkeep` (et idem 02-structurer/, 03-piloter/, 04-collaborer/, 05-automatiser/, 06-mesurer/, 07-industrialiser/)
- Create : `content/formations/fluentboards/livrables/workflows-n8n/.gitkeep`
- Create : `content/formations/fluentboards/assets/captures/.gitkeep`
- Modify : `.gitignore` (ajouter `content/formations/fluentboards/assets/demos/`)

- [ ] **Step 1 : créer l'arborescence**

```
cd "d:/VS Code/CLAUDE CODE/projects/schoolswp"
mkdir -p content/formations/fluentboards/modules/01-setup
mkdir -p content/formations/fluentboards/modules/02-structurer
mkdir -p content/formations/fluentboards/modules/03-piloter
mkdir -p content/formations/fluentboards/modules/04-collaborer
mkdir -p content/formations/fluentboards/modules/05-automatiser
mkdir -p content/formations/fluentboards/modules/06-mesurer
mkdir -p content/formations/fluentboards/modules/07-industrialiser
mkdir -p content/formations/fluentboards/livrables/workflows-n8n
mkdir -p content/formations/fluentboards/assets/captures
mkdir -p content/formations/fluentboards/assets/demos
mkdir -p content/formations/fluentboards/sales
touch content/formations/fluentboards/modules/01-setup/.gitkeep
```

(Répéter le touch .gitkeep pour les 6 autres modules + livrables/workflows-n8n/ + assets/captures/.)

- [ ] **Step 2 : ajouter assets/demos/ au .gitignore**

Ajouter à la fin de `.gitignore` :

```
# Formation FluentBoards - MP4 demos non versionnés (lourds)
content/formations/fluentboards/assets/demos/
```

- [ ] **Step 3 : créer plan.md initial**

Fichier `content/formations/fluentboards/plan.md` avec la liste des 40 leçons (reproduire la table de la spec section 3 + la liste complète des leçons attendues par module tirée de la Task 1.1 ci-dessous). Ce fichier sert de tableau de bord de prod.

- [ ] **Step 4 : commit**

`git add content/formations/fluentboards/ .gitignore` puis `git commit -m "chore(formation-fb): scaffold arborescence repo formation"`.

---

### Task 0.2: Vérifier les prérequis stack

**Files :** aucun dans le repo (vérification externe)

- [ ] **Step 1 : checker TutorLMS**

wp-admin schoolswp.com → Plugins → vérifier TutorLMS actif + licence Pro active. Si pas Pro, noter (peut limiter certaines features).

- [ ] **Step 2 : checker FluentCart**

wp-admin → Plugins → FluentCart actif + licence active. Aller dans FluentCart → Products → vérifier qu'au moins le flow "créer un produit" fonctionne.

- [ ] **Step 3 : checker FluentCRM**

wp-admin → Plugins → FluentCRM actif + licence active. Vérifier au moins 1 liste existe, 1 tag existe (pour les automations).

- [ ] **Step 4 : checker FluentBoards Pro**

wp-admin → Plugins → FluentBoards actif + licence Pro active. Ouvrir FluentBoards → vérifier l'accès aux features Pro (recurring tasks, custom fields, webhooks).

- [ ] **Step 5 : vérifier FluentRoadmap (point critique)**

wp-admin → Plugins → chercher FluentRoadmap. Si présent et actif : bon, Module 6 peut inclure Roadmap. Si absent ou licence séparée non active : écrire note dans `content/formations/fluentboards/plan.md` — Module 6 retirera le volet Roadmap, focus Reports + Time Tracking. Mettre à jour la spec en conséquence (modifier la table des modules).

- [ ] **Step 6 : checker n8n**

Ouvrir l'instance n8n, vérifier accès + credentials FluentBoards existants (webhook, API key). Si credential FluentBoards absent : créer en suivant doc officielle.

- [ ] **Step 7 : documenter**

Créer `content/formations/fluentboards/plan.md` section "Prérequis vérifiés" avec status de chaque item + date. Commit : `git add content/formations/fluentboards/plan.md` puis `git commit -m "chore(formation-fb): verify stack prerequisites"`.

---

### Task 0.3: Tester le bridge FluentCart ↔ TutorLMS (Plan A ou Plan B)

**Files :**
- Modify : `content/formations/fluentboards/plan.md` (section "Bridge choisi")

- [ ] **Step 1 : checker Plan A (bridge natif)**

wp-admin → FluentCart → Settings → Integrations, chercher "TutorLMS" ou "LMS". Si présent et officiel : c'est le Plan A.

- [ ] **Step 2 : si Plan A présent, tester**

Créer un produit FluentCart de test "Formation FluentBoards - TEST" à 1 €, associer au cours TutorLMS (cours à créer au Step 4 de Task 0.4, donc revenir à cette tâche ensuite). Acheter le produit avec un compte test. Vérifier que l'utilisateur est inscrit au cours TutorLMS automatiquement.

- [ ] **Step 3 : si Plan A absent, activer Plan B (fallback FluentCRM)**

FluentCRM → Automations → créer nouvelle automation :
- Trigger : "FluentCart - Order Completed"
- Condition : "Product ID = <ID du produit formation>"
- Action 1 : "Add contact to list 'Formation FluentBoards acheteurs'"
- Action 2 : "Execute webhook" pointant sur un endpoint WP qui appelle l'API TutorLMS pour enroll l'utilisateur au cours. Alternative plus simple : utiliser le connecteur FluentCRM "Enroll in Course" s'il existe pour TutorLMS.

- [ ] **Step 4 : documenter la décision**

Dans `content/formations/fluentboards/plan.md` section "Bridge choisi", noter Plan A ou Plan B + la procédure exacte utilisée + captures de la config dans `assets/captures/bridge/`.

- [ ] **Step 5 : commit**

`git add content/formations/fluentboards/plan.md content/formations/fluentboards/assets/captures/bridge/` puis `git commit -m "feat(formation-fb): FluentCart-TutorLMS bridge documented"`.

---

### Task 0.4: Créer le cours TutorLMS squelette

**Files :** aucun dans le repo (configuration WP)

- [ ] **Step 1 : créer le cours**

wp-admin → TutorLMS → Courses → Add New
- Titre : "FluentBoards de zéro à pro"
- Slug : `formations-fluentboards-de-zero-a-pro` (règle evergreen : pas de date, pas de "schoolswp" dans le slug)
- Catégorie : créer "Formations schoolsWP" si absente
- Instructor : Michael KIHL
- Course level : Intermediate
- Course durée : 8-12 h (estimation apprenant)
- Description : placeholder (sera remplie avec le draft sales page plus tard)

- [ ] **Step 2 : créer les 7 sections (vides)**

Course Builder → ajouter 7 sections dans l'ordre : Setup / Structurer / Piloter / Collaborer / Automatiser / Mesurer / Industrialiser.

- [ ] **Step 3 : configurer la visibilité "Private"**

Status du cours : "Private" (pas publish). Seuls les acheteurs auront accès via le bridge FluentCart.

- [ ] **Step 4 : configurer le certificat**

TutorLMS → Certificates → choisir template par défaut ou créer un template personnalisé avec logo schoolsWP. Condition d'émission : 100 % de complétion + tous les quiz ≥ 70 %.

- [ ] **Step 5 : capture + doc**

Screenshots de la structure créée, sauvés dans `content/formations/fluentboards/assets/captures/setup-tutorlms/`. Commit : `git add content/formations/fluentboards/assets/captures/setup-tutorlms/` puis `git commit -m "chore(formation-fb): TutorLMS course skeleton 7 sections"`.

---

### Task 0.5: Créer le produit FluentCart + checkout

**Files :** aucun dans le repo (configuration WP)

- [ ] **Step 1 : créer le produit**

FluentCart → Products → Add New
- Name : "Formation FluentBoards de zéro à pro"
- Price : 67 € (early bird — sera modifié en S9)
- Type : One-time payment (pas subscription)
- Description : placeholder
- Associated course : sélectionner le cours créé en Task 0.4 (si Plan A natif) sinon skip

- [ ] **Step 2 : créer l'order bump**

FluentCart → Products → Add New (produit séparé "Pack Workflows n8n Avancés" à 27 €, one-time). Puis dans le produit formation → Settings → Order Bumps → ajouter ce produit.

- [ ] **Step 3 : configurer la sales page FluentCart (temporaire)**

URL : `schoolswp.com/checkout/formation-fluentboards/` — sales page courte par défaut de FluentCart. Sera remplacée en Phase 6 par la vraie sales page cc-design à `schoolswp.com/formations/fluentboards/`.

- [ ] **Step 4 : tester l'achat en mode sandbox**

Configurer passerelle de paiement en mode test (Stripe test mode ou similaire). Acheter le produit avec une carte de test. Vérifier : commande créée, email envoyé, order bump proposé et optable.

- [ ] **Step 5 : doc + commit**

`git add content/formations/fluentboards/plan.md` puis `git commit -m "chore(formation-fb): FluentCart product + order bump + sandbox tested"`.

---

### Task 0.6: Créer l'automation FluentCRM welcome + bridge TutorLMS

**Files :** aucun dans le repo (configuration WP)

- [ ] **Step 1 : créer les listes et tags**

FluentCRM → Lists → créer "Formation FluentBoards acheteurs" + "Formation FluentBoards abandons checkout" (pour future relance).
FluentCRM → Tags → créer "formation-fluentboards" + "early-bird" (tag les 30 premiers).

- [ ] **Step 2 : créer l'automation "Welcome + enroll"**

FluentCRM → Automations → New :
- Trigger : FluentCart Order Completed pour le produit Formation FluentBoards
- Action 1 : Add tag "formation-fluentboards"
- Action 2 : Add to list "Formation FluentBoards acheteurs"
- Action 3 : Enroll in TutorLMS course (si disponible en natif) OU webhook API TutorLMS (selon Plan B décidé en Task 0.3)
- Action 4 : Send email (template à créer Step 3)
- Action 5 : Wait 7 days → Send email follow-up (template à créer en Task 7.2)
- Action 6 : Wait 23 days (= J+30 total) → Send email upsell (template à créer plus tard)

- [ ] **Step 3 : créer l'email welcome template**

FluentCRM → Email Templates → New
- Subject : "Bienvenue dans FluentBoards de zéro à pro — ton accès est prêt"
- Contenu : lien direct vers le cours TutorLMS + lien téléchargement pack ressources + promesse support "réponse sous 48 h". Tutoiement, signature Michael.

- [ ] **Step 4 : tester l'automation avec un achat de test**

Refaire un achat avec compte test (Step 4 de Task 0.5). Vérifier :
- User enrolled dans le cours TutorLMS
- Tag "formation-fluentboards" appliqué
- Email welcome reçu < 60 s
- Liens dans l'email fonctionnels

- [ ] **Step 5 : commit**

`git add content/formations/fluentboards/assets/captures/automation/ content/formations/fluentboards/plan.md` puis `git commit -m "feat(formation-fb): FluentCRM welcome automation + enrollment tested"`.

---

### Task 0.7: Test end-to-end complet du tunnel (squelette)

**Files :** aucun (test)

- [ ] **Step 1 : simulation achat complet**

Depuis un compte WP différent (pas admin), ouvrir la page checkout FluentCart. Acheter. Checker ces 12 points dans l'ordre :

1. Checkout FluentCart passe OK (CB + SEPA test)
2. Order bump 27 € activable → panier mis à jour
3. Email post-achat FluentCRM reçu < 60 s
4. Lien email → user connecté TutorLMS → inscrit au cours
5. Accès au cours → les 7 sections visibles (vides pour l'instant)
6. Quiz non publié (normal — pas encore créés)
7. Zone ressources : placeholder (vide pour l'instant, OK)
8. Démarrer leçon 1.1 (placeholder) → progression trackée
9. Tenter rembourser la commande → FluentCart remboursement OK
10. Vérifier que l'user est désinscrit (ou pas — décider : on laissera l'accès même en cas de refund, principe "pas de rétrocession d'accès" ? ou on révoque ?) — à décider et documenter.
11. Désinscrire la newsletter depuis pied d'email — bouton présent, fonctionne
12. Reinscrire (nouveau checkout) → aucune trace résiduelle de l'ancien refund bloque

- [ ] **Step 2 : documenter résultats + tickets à fixer**

Si Step 1 échoue sur un point → créer ticket dans `content/formations/fluentboards/plan.md` section "QA blockers S1".

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/plan.md` puis `git commit -m "test(formation-fb): e2e tunnel test 12 checkpoints squelette"`.

---

### Task 0.8: Setup template OBS pour démos screen

**Files :**
- Create : `content/formations/fluentboards/assets/obs-template/README.md`
- Create : `content/formations/fluentboards/assets/obs-template/scene-collection.json` (export OBS)

- [ ] **Step 1 : configurer OBS**

OBS Studio → nouvelle scene collection "Formation FluentBoards". Scène principale :
- Source "Display Capture" → écran principal 1920×1080
- Filtre "Crop/Pad" si besoin de cropper le panneau latéral du navigateur
- Overlay : logo schoolsWP en bas à droite (PNG transparent 120×120)
- Curseur visible : activer dans paramètres capture
- Microphone (si voix) : source audio séparée, compression + noise suppression activées

- [ ] **Step 2 : définir intro/outro 2 s**

Deux scènes additionnelles :
- "Intro" : fond noir + logo schoolsWP centré + texte "FluentBoards de zéro à pro" (affichable 2 s)
- "Outro" : idem avec texte "suite dans la prochaine leçon" (affichable 2 s)

Configurer transitions (fade 300 ms).

- [ ] **Step 3 : définir preset d'enregistrement**

OBS → Settings → Output :
- Mode : Simple
- Recording format : MP4
- Encoder : x264 (ou NVENC si carte GPU dispo)
- Bitrate : 6 000 Kbps
- Résolution sortie : 1920×1080 @ 30 fps

- [ ] **Step 4 : exporter la scene collection**

OBS → Scene Collection → Export → sauvegarder à `content/formations/fluentboards/assets/obs-template/scene-collection.json`.

- [ ] **Step 5 : rédiger le README template**

`content/formations/fluentboards/assets/obs-template/README.md` décrivant : prérequis OBS version, comment importer la scene collection, réglages audio/vidéo, convention de nommage des fichiers (NN-slug.mp4), durée cible 30-90 s, obligation de couper en tête/queue avec Shotcut si plus long.

- [ ] **Step 6 : commit**

`git add content/formations/fluentboards/assets/obs-template/` puis `git commit -m "chore(formation-fb): OBS template + README for screen demos"`.

---

### Task 0.9: Créer le board fil rouge "Agence Template v0"

**Files :**
- Create : `content/formations/fluentboards/livrables/board-snapshots/v0-initial.json`

- [ ] **Step 1 : créer le board dans FluentBoards Pro**

wp-admin → FluentBoards → New Board
- Name : "Agence Template"
- Description : "Board fil rouge de la formation"
- Pas de stages pour l'instant (seront créés au module 2, on garde le board brut)

- [ ] **Step 2 : export snapshot v0**

FluentBoards → Board → Settings → Export (si feature existe, sinon via wp-cli ou plugin export). Fichier exporté → renommer et ranger dans `content/formations/fluentboards/livrables/board-snapshots/v0-initial.json`.

- [ ] **Step 3 : sanitize**

Ouvrir le JSON, vérifier : pas d'ID utilisateur interne, pas de tokens, pas de chemins serveur absolus. Si présents : les neutraliser ou noter pour le script de sanitization final en Task 5.3.

- [ ] **Step 4 : commit**

`git add content/formations/fluentboards/livrables/board-snapshots/` puis `git commit -m "feat(formation-fb): board agence template v0 (initial empty)"`.

---

## Phase 1 — Module 1 Setup (S1 seconde moitié)

### Task 1.1: Définir le découpage détaillé des 40 leçons

**Files :**
- Modify : `content/formations/fluentboards/plan.md` (ajouter section "Leçons détaillées")

- [ ] **Step 1 : écrire la liste des 40 leçons avec objectif pédagogique en 1 phrase**

Dans `content/formations/fluentboards/plan.md`, section "Leçons détaillées", reproduire cette table (servira de référence pour toutes les Tasks 1.x à 5.x) :

**Module 1 — Setup (5 leçons)**
- 1.1 Pourquoi FluentBoards — contextualiser l'outil, ses forces vs Trello/Asana/ClickUp, le "tout-dans-WP"
- 1.2 Installation du plugin — installer FluentBoards (Free puis Pro), activation licence
- 1.3 Ajuster la position dans le menu WP — feature méconnue, améliore l'UX pour tout user WP
- 1.4 Free vs Pro : ce que tu as vraiment — matrice comparative exhaustive
- 1.5 Créer ton premier board — board vierge, naming, description, preview

**Module 2 — Structurer (6 leçons)**
- 2.1 Stages : créer, renommer, réorganiser
- 2.2 Stage default assignee : qui prend la task quand elle arrive
- 2.3 Task templates : structurer une task type
- 2.4 Custom fields : texte, date, select, multi-select
- 2.5 Labels + couleurs : catégoriser visuellement
- 2.6 Card view preferences : ce que l'œil voit sans ouvrir la task

**Module 3 — Piloter (6 leçons)**
- 3.1 Créer une task complète : dates, priorité, description, label, assignee
- 3.2 Sous-tâches + groupes de sous-tâches
- 3.3 Task actions : move, clone, archive, bulk
- 3.4 Recurring tasks : quand/pourquoi/comment
- 3.5 Task status filter
- 3.6 Advanced filtering : par label, date, assignee, custom field

**Module 4 — Collaborer (6 leçons)**
- 4.1 Member roles : admin, editor, view-only
- 4.2 Notifications settings
- 4.3 Daily reminder
- 4.4 Frontend Portal — paramétrage + partage client
- 4.5 Profile + task overview
- 4.6 Pinned boards

**Module 5 — Automatiser (6 leçons)**
- 5.1 Incoming webhook : créer une task depuis n'importe quelle app
- 5.2 Outgoing webhook : envoyer un événement FB vers n8n/Slack/Discord
- 5.3 Intégration Fluent Forms : submit → task auto
- 5.4 Intégration FluentCRM : contact ↔ board
- 5.5 Intégration FluentSupport : ticket → task
- 5.6 Stockage externe : S3 / R2 / Backblaze / DigitalOcean

**Module 6 — Mesurer (5 leçons, ou 4 si FluentRoadmap non licencié)**
- 6.1 Time tracking sur les tasks
- 6.2 FluentBoards Reports : dashboard agrégé
- 6.3 FluentRoadmap : créer une roadmap publique — *skippé si licence FluentRoadmap absente*
- 6.4 Roadmap settings — *skippé si licence FluentRoadmap absente*
- 6.5 Lire les reports : interpréter les métriques pour piloter l'équipe

**Module 7 — Industrialiser (6 leçons)**
- 7.1 Board folders : organiser 10+ boards clients
- 7.2 Bulk actions — table view
- 7.3 Import/Export d'un board entier
- 7.4 Migrer depuis Trello
- 7.5 Migrer depuis Asana
- 7.6 FINAL : exporter le board agence template + packaging du livrable

Total : 5 + 6 + 6 + 6 + 6 + 5 + 6 = **40 leçons** (39 si FluentRoadmap skippé).

- [ ] **Step 2 : commit**

`git add content/formations/fluentboards/plan.md` puis `git commit -m "docs(formation-fb): plan détaillé 40 leçons par module"`.

---

### Task 1.2: Produire les 5 leçons du Module 1 Setup

Appliquer le **Pattern L** à chacune des 5 leçons ci-dessous.

**Files (créés par le pattern) :**
- Create : `content/formations/fluentboards/modules/01-setup/01-pourquoi-fluentboards.md`
- Create : `content/formations/fluentboards/modules/01-setup/02-installation.md`
- Create : `content/formations/fluentboards/modules/01-setup/03-position-menu-wp.md`
- Create : `content/formations/fluentboards/modules/01-setup/04-free-vs-pro.md`
- Create : `content/formations/fluentboards/modules/01-setup/05-premier-board.md`

**Briefs des leçons :**

- [ ] **Leçon 1.1 Pourquoi FluentBoards** — Pattern L
  - Objectif : "À la fin, tu sauras pourquoi FluentBoards bat Trello/Asana/ClickUp pour un pro WP + tu identifieras le scénario type qui justifie la migration."
  - Sources : `content/docs/fluentboards/pages/fluentboards-com.md`, `blog/introducing-fluentboards.md`, `pages/trello-vs-fluentboards.md`, `youtube/01-jDNdINFMZ5w.md`
  - Pièges : ne pas promettre "remplace tout" (nuance : adapté à qui a déjà WP comme hub)
  - Démo : 60 s — captures annotées comparant Trello ouvert dans un onglet vs board FluentBoards intégré dans wp-admin.

- [ ] **Leçon 1.2 Installation du plugin** — Pattern L
  - Objectif : "À la fin, FluentBoards Free puis Pro sont installés, activés, licence validée."
  - Sources : `docs/fluentboards-installation-guide.md`, `docs/fluentboards-licence-activation.md`
  - Pièges : licence saisie depuis le mauvais compte WPManageNinja, Pro installé avant Free (conflit).
  - Démo : 60 s install Free depuis WP repo puis Pro depuis zip + activation licence.

- [ ] **Leçon 1.3 Ajuster la position dans le menu WP** — Pattern L
  - Objectif : "À la fin, tu sais déplacer FluentBoards dans le menu wp-admin pour éviter qu'il soit en bas à oublié."
  - Sources : `docs/fluentboards-menu-position-in-wordpress.md`
  - Pièges : position conflictuelle avec d'autres plugins qui utilisent le même index.
  - Démo : 30 s avant/après placement.

- [ ] **Leçon 1.4 Free vs Pro — ce que tu as vraiment** — Pattern L
  - Objectif : "À la fin, tu sais exactement quelles features nécessitent Pro et peux justifier l'upgrade auprès de ton boss/client."
  - Sources : `pages/free-vs-pro.md`, `blog/fluentboards-free-vs-pro.md`, `youtube/13-Azqd7iixFMk.md`
  - Format : tableau comparatif 2 colonnes.
  - Pas de démo vidéo obligatoire (tableau suffit), ou 45 s sur un feature Pro précis.

- [ ] **Leçon 1.5 Créer ton premier board** — Pattern L
  - Objectif : "À la fin, tu as un board 'Agence Template' créé (le fil rouge de la formation)."
  - Sources : `docs/how-to-create-a-new-board.md`, `docs/onboarding-board.md`, `docs/boards-view.md`, `youtube/26-sJbRqlo5HA8.md`
  - Pièges : oublier de nommer correctement (naming convention : "Client - Projet"), créer un board "test" et l'utiliser en prod.
  - Démo : 60 s création board + premier look UI.
  - **Spécial** : à la fin, Michael crée vraiment le board "Agence Template" (déjà fait en Task 0.9 — juste montrer la création en démo).

---

### Task 1.3: Produire le quiz du Module 1

Appliquer le **Pattern Q** pour le Module 1. Brief pour studio :
- 7 questions QCM couvrant les 5 leçons
- Mix facile (positionnement / Free vs Pro) et technique (licence, menu position)
- Chaque question = 4 choix + 1 bonne réponse + explication 2 phrases

Fichier : `content/formations/fluentboards/modules/01-setup/quiz.md`

- [ ] **Appliquer Pattern Q complet.**

---

### Task 1.4: Export board snapshot v-M1 + commit fin S1

**Files :**
- Create : `content/formations/fluentboards/livrables/board-snapshots/v-M1-after-module-1.json`

- [ ] **Step 1 : exporter le board FluentBoards après module 1**

À ce stade, le board "Agence Template" est encore vierge (aucun stage créé — ça vient au module 2). Exporter quand même pour snapshot versionné. Export JSON depuis FluentBoards UI → sauver dans `livrables/board-snapshots/v-M1-after-module-1.json`.

- [ ] **Step 2 : sanitize (neutraliser IDs persistants)**

Inspecter le JSON, remplacer les IDs internes sensibles par des placeholders si nécessaire.

- [ ] **Step 3 : commit + tag Git**

`git add content/formations/fluentboards/livrables/board-snapshots/v-M1-after-module-1.json` puis `git commit -m "feat(formation-fb): board snapshot after module 1"` puis `git tag formation-fb-module-1-done`.

---

## Phase 2 — Modules 2 + 3 (S2)

### Task 2.1: Produire les 6 leçons du Module 2 Structurer

Appliquer **Pattern L** pour chaque leçon. Pendant la production, Michael crée dans le board "Agence Template" : les stages "Backlog / En cours / Review / Done", un stage default assignee, un task template, 3 custom fields (Priorité, Client, Deadline), 5 labels colorés.

**Files :**
- Create : `content/formations/fluentboards/modules/02-structurer/01-stages.md`
- Create : `content/formations/fluentboards/modules/02-structurer/02-stage-default-assignee.md`
- Create : `content/formations/fluentboards/modules/02-structurer/03-task-templates.md`
- Create : `content/formations/fluentboards/modules/02-structurer/04-custom-fields.md`
- Create : `content/formations/fluentboards/modules/02-structurer/05-labels-couleurs.md`
- Create : `content/formations/fluentboards/modules/02-structurer/06-card-view-preferences.md`

**Briefs :**

- [ ] **Leçon 2.1 Stages — créer, renommer, réorganiser** — Pattern L
  - Objectif : "À la fin, le board Agence a 4 stages nommés et ordonnés."
  - Sources : `docs/how-to-create-a-new-stage.md`, `youtube/05-jTD7SjyXcHk.md`
  - Pièges : trop de stages (viser 4-6 max), renommer après coup casse le routage webhooks.

- [ ] **Leçon 2.2 Stage default assignee** — Pattern L
  - Objectif : "À la fin, le stage 'Backlog' assigne automatiquement à toi-même les nouvelles tasks."
  - Sources : `docs/stage-default-assignee.md`
  - Pièges : assigner à un user supprimé = tasks orphelines.

- [ ] **Leçon 2.3 Task templates** — Pattern L
  - Objectif : "À la fin, tu as un template 'Nouveau projet client' qui préremplit 8 sous-tâches types."
  - Sources : `docs/task-template.md`
  - Pièges : template trop chargé, apprenant le vide à chaque fois.

- [ ] **Leçon 2.4 Custom fields** — Pattern L
  - Objectif : "À la fin, le board Agence a 3 custom fields : Priorité (select), Client (texte), Deadline (date)."
  - Sources : `docs/custom-fields-for-task.md`
  - Pièges : multi-select mal géré par certains filtres → préférer select simple quand c'est binaire.

- [ ] **Leçon 2.5 Labels + couleurs** — Pattern L
  - Objectif : "À la fin, 5 labels colorés existent : Bug, Feature, Doc, Ops, Sales."
  - Sources : à extraire de `docs/task-action.md` + notes de release
  - Pièges : 20 labels = illisibilité, viser 5-8 max.

- [ ] **Leçon 2.6 Card view preferences** — Pattern L
  - Objectif : "À la fin, tu vois sur la card : titre + assignee avatar + label color + deadline + custom field Priorité."
  - Sources : `docs/card-view-preference-settings.md`

---

### Task 2.2: Produire le quiz du Module 2 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 2, 6 questions QCM.

---

### Task 2.3: Export board snapshot v-M2

- [ ] Step 1 : export JSON + sanitize + commit (idem Task 1.4 avec `v-M2-after-module-2.json` et tag `formation-fb-module-2-done`)

---

### Task 2.4: Produire les 6 leçons du Module 3 Piloter

Appliquer **Pattern L**. Michael peuple le board avec des tasks réelles : ~10 tasks de démo réparties sur les 4 stages, certaines avec sous-tâches, une recurring, des priorités variées.

**Files :**
- Create : `content/formations/fluentboards/modules/03-piloter/01-creer-task.md`
- Create : `content/formations/fluentboards/modules/03-piloter/02-sous-taches.md`
- Create : `content/formations/fluentboards/modules/03-piloter/03-task-actions.md`
- Create : `content/formations/fluentboards/modules/03-piloter/04-recurring-tasks.md`
- Create : `content/formations/fluentboards/modules/03-piloter/05-task-status-filter.md`
- Create : `content/formations/fluentboards/modules/03-piloter/06-advanced-filtering.md`

**Briefs :**

- [ ] **Leçon 3.1 Créer une task complète** — Pattern L
  - Objectif : "À la fin, le board a 5 tasks peuplées avec dates + assignee + description + label + priorité."
  - Sources : `docs/task-action.md`, `youtube/26-sJbRqlo5HA8.md`
  - Pièges : ne pas mettre de deadline → task oubliée.

- [ ] **Leçon 3.2 Sous-tâches + groupes de sous-tâches** — Pattern L
  - Objectif : "À la fin, une task client type a 8 sous-tâches groupées en 2 phases (Setup / Livraison)."
  - Sources : `docs/task-action.md` + changelog récent
  - Pièges : sous-tâches mal groupées = perte visibilité.

- [ ] **Leçon 3.3 Task actions — move, clone, archive, bulk** — Pattern L
  - Objectif : "À la fin, tu sais cloner une task, la déplacer entre stages, l'archiver, et faire des actions bulk en table view."
  - Sources : `docs/task-action.md`
  - Pièges : archive ≠ suppression.

- [ ] **Leçon 3.4 Recurring tasks** — Pattern L
  - Objectif : "À la fin, tu as une task récurrente hebdo 'Réunion équipe' qui se duplique automatiquement chaque lundi."
  - Sources : `docs/recurring-task.md`, `youtube/12-oUNoetTf8sg.md`
  - Pièges : récurrence trop fréquente → spam de tasks identiques.

- [ ] **Leçon 3.5 Task status filter** — Pattern L
  - Objectif : "À la fin, tu sais filtrer les tasks par status (pending / in progress / completed / cancelled)."
  - Sources : `docs/task-action.md`

- [ ] **Leçon 3.6 Advanced filtering** — Pattern L
  - Objectif : "À la fin, tu sais combiner 3 filtres : label + assignee + deadline pour une vue ciblée."
  - Sources : changelog + blog posts récents
  - Démo : 90 s sur un board peuplé.

---

### Task 2.5: Produire le quiz du Module 3 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 3, 7 questions QCM.

---

### Task 2.6: Export board snapshot v-M3

- [ ] Idem Task 1.4 avec `v-M3-after-module-3.json` et tag `formation-fb-module-3-done`.

---

## Phase 3 — Module 4 + début Module 5 (S3)

### Task 3.1: Produire les 6 leçons du Module 4 Collaborer

Appliquer **Pattern L**. Michael invite 1-2 users tests (emails poubelle) + configure le Frontend Portal sur une URL dédiée `/portail-client/`.

**Files :**
- Create : `content/formations/fluentboards/modules/04-collaborer/01-member-roles.md`
- Create : `content/formations/fluentboards/modules/04-collaborer/02-notifications.md`
- Create : `content/formations/fluentboards/modules/04-collaborer/03-daily-reminder.md`
- Create : `content/formations/fluentboards/modules/04-collaborer/04-frontend-portal.md`
- Create : `content/formations/fluentboards/modules/04-collaborer/05-profile-task-overview.md`
- Create : `content/formations/fluentboards/modules/04-collaborer/06-pinned-boards.md`

**Briefs :**

- [ ] **Leçon 4.1 Member roles** — Pattern L
  - Objectif : "À la fin, tu as invité 2 users : un éditeur + un view-only."
  - Sources : `docs/member-roles.md`
  - Pièges : donner admin par défaut, puis galère à rétrograder.

- [ ] **Leçon 4.2 Notifications settings** — Pattern L
  - Objectif : "À la fin, tu reçois un email quand une task te mentionne, mais pas pour chaque changement mineur."
  - Sources : `docs/notification-settings.md`
  - Pièges : tout cocher → spam → apprenant désactive tout.

- [ ] **Leçon 4.3 Daily reminder** — Pattern L
  - Objectif : "À la fin, tu reçois un mail quotidien à 9 h avec tes tasks du jour."
  - Sources : `docs/daily-reminder-settings.md`

- [ ] **Leçon 4.4 Frontend Portal — paramétrage + partage client** — Pattern L — **CRUCIAL**
  - Objectif : "À la fin, tu as un portail client fonctionnel à `schoolswp.com/portail-client/` où le client voit uniquement son board + ses tasks."
  - Sources : `docs/frontend-portal-settings.md`, `youtube/06-KszublJN0xY.md`, `youtube/19-tn-xUbVtOtY.md`
  - Pièges : portail public sans auth → fuite données. Toujours exiger login.
  - Démo : 90 s setup portal + ouverture avec compte client test.

- [ ] **Leçon 4.5 Profile + task overview** — Pattern L
  - Objectif : "À la fin, tu trouves ton profil utilisateur + la vue 'My Tasks' transversale aux boards."
  - Sources : `docs/fluentboards-profile-and-task-overview.md`

- [ ] **Leçon 4.6 Pinned boards** — Pattern L
  - Objectif : "À la fin, tu as pinné le board Agence en premier de ta sidebar."
  - Sources : `docs/pinned-boards.md`

---

### Task 3.2: Produire le quiz du Module 4 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 4, 7 questions QCM.

---

### Task 3.3: Export board snapshot v-M4

- [ ] Idem Task 1.4 avec `v-M4-after-module-4.json` et tag `formation-fb-module-4-done`.

---

### Task 3.4: Produire les 3 premières leçons du Module 5 Automatiser (50 %)

Appliquer **Pattern L**. Module 5 est le plus dense — les 3 premières leçons posent les bases webhook.

**Files :**
- Create : `content/formations/fluentboards/modules/05-automatiser/01-incoming-webhook.md`
- Create : `content/formations/fluentboards/modules/05-automatiser/02-outgoing-webhook.md`
- Create : `content/formations/fluentboards/modules/05-automatiser/03-integration-fluent-forms.md`

**Briefs :**

- [ ] **Leçon 5.1 Incoming webhook — créer une task depuis n'importe quelle app** — Pattern L — **CRUCIAL**
  - Objectif : "À la fin, tu génères une URL webhook FluentBoards et tu crées une task via POST JSON depuis un client HTTP (prouvant que n'importe quelle app peut le faire)."
  - Sources : `docs/incoming-webhook.md`, `youtube/08-csZCb6rO1bQ.md`, `youtube/27-zl0Ot_Y3Y8k.md`
  - Pièges : oublier que le hash webhook = auth (fuite URL = fuite accès).
  - Démo : 90 s création URL + POST via Postman ou httpie → task apparaît.
  - **Bonus** : ce webhook est celui qu'on utilisera dans le pipeline schoolsWP (déjà en place — voir `tools/scripts/notify-audit-card.py` — Michael peut citer ce cas d'usage réel).

- [ ] **Leçon 5.2 Outgoing webhook — envoyer un événement FB** — Pattern L
  - Objectif : "À la fin, quand une task change de stage sur FluentBoards, un webhook sort vers n8n pour router vers Slack/Discord."
  - Sources : `docs/outgoing-webhooks.md`, `blog/fluentboards-outgoing-webhooks.md`
  - Pièges : surcharger avec trop d'événements outgoing (rate limit + spam).

- [ ] **Leçon 5.3 Intégration Fluent Forms — submit → task auto** — Pattern L
  - Objectif : "À la fin, tu as un formulaire Fluent Forms dont chaque submission crée une task dans le board Agence (stage 'Nouveaux leads')."
  - Sources : `docs/fluentboards-integration-with-fluent-forms.md`, `youtube/10-39rF5Pmwf9o.md`, `blog/how-fluent-forms-complements-fluentboards.md`
  - Démo : 90 s création formulaire + connecteur + test submission.

---

## Phase 4 — Fin Module 5 + Module 6 (S4)

### Task 4.1: Produire les 3 dernières leçons du Module 5

Appliquer **Pattern L**.

**Files :**
- Create : `content/formations/fluentboards/modules/05-automatiser/04-integration-fluentcrm.md`
- Create : `content/formations/fluentboards/modules/05-automatiser/05-integration-fluentsupport.md`
- Create : `content/formations/fluentboards/modules/05-automatiser/06-stockage-externe.md`

**Briefs :**

- [ ] **Leçon 5.4 Intégration FluentCRM — contact ↔ board** — Pattern L
  - Objectif : "À la fin, quand tu crées une task liée à un contact CRM, tu as accès direct à sa fiche sans quitter FluentBoards."
  - Sources : `docs/fluentboards-integration-with-fluentcrm.md`, `blog/how-fluentcrm-complement-fluentboards.md`
  - Pièges : sync bidirectionnelle pas garantie — c'est du lien, pas de la copie.

- [ ] **Leçon 5.5 Intégration FluentSupport — ticket → task** — Pattern L
  - Objectif : "À la fin, un ticket FluentSupport escaladé crée une task dans le board Dev."
  - Sources : `docs/fluentboards-integration-with-fluentsupport.md`

- [ ] **Leçon 5.6 Stockage externe — S3/R2/Backblaze/DigitalOcean** — Pattern L
  - Objectif : "À la fin, les pièces jointes des tasks vont sur Cloudflare R2 (ou S3) au lieu du serveur WP."
  - Sources : les 4 docs S3/R2/Backblaze/DigitalOcean dans `content/docs/fluentboards/docs/`
  - Pièges : CORS mal configuré → pièces jointes qui ne chargent pas depuis le navigateur.
  - **Conseil** : focus R2 par défaut (moins cher, pas de egress fees), alternatives mentionnées en annexe.

---

### Task 4.2: Produire le quiz du Module 5 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 5, **8 questions QCM** (module dense).

---

### Task 4.3: Produire les leçons du Module 6 Mesurer

Appliquer **Pattern L**. **5 leçons si FluentRoadmap licencié, 4 sinon** (décision prise en Task 0.2 Step 5).

**Files (version 5 leçons) :**
- Create : `content/formations/fluentboards/modules/06-mesurer/01-time-tracking.md`
- Create : `content/formations/fluentboards/modules/06-mesurer/02-reports.md`
- Create : `content/formations/fluentboards/modules/06-mesurer/03-fluentroadmap-public.md` *(conditionnel)*
- Create : `content/formations/fluentboards/modules/06-mesurer/04-roadmap-settings.md` *(conditionnel)*
- Create : `content/formations/fluentboards/modules/06-mesurer/05-lire-les-reports.md`

**Briefs :**

- [ ] **Leçon 6.1 Time tracking sur les tasks** — Pattern L
  - Objectif : "À la fin, tu démarres un chronomètre sur une task + tu logs manuellement du temps rétroactivement."
  - Sources : `docs/task-time-tracking.md`

- [ ] **Leçon 6.2 FluentBoards Reports** — Pattern L
  - Objectif : "À la fin, tu as ouvert le dashboard reports et tu comprends les 5 KPI principaux (tasks par stage, tasks terminées / semaine, tasks en retard, top assignees, temps cumulé)."
  - Sources : `docs/fluentboard-reports.md`, `youtube/25-QoCrKupLTbM.md`

- [ ] **Leçon 6.3 FluentRoadmap — créer une roadmap publique** *(conditionnel — skip si licence absente)* — Pattern L
  - Objectif : "À la fin, tu publies une roadmap produit en lecture seule à `schoolswp.com/roadmap/`."
  - Sources : `docs/fluentboards-roadmap-overview.md`, `youtube/04-24D5NdmPGCU.md`, `youtube/23-t5F8OgQeDIY.md`

- [ ] **Leçon 6.4 Roadmap settings** *(conditionnel)* — Pattern L
  - Objectif : "À la fin, la roadmap publique a les bonnes permissions + branding."
  - Sources : `docs/roadmap-settings.md`

- [ ] **Leçon 6.5 Lire les reports — interpréter pour piloter** — Pattern L
  - Objectif : "À la fin, tu identifies les 3 signaux d'alerte dans un board (stage 'Review' qui s'engorge, tasks en retard > 5 %, assignee saturé)."
  - Sources : synthèse leçon 6.2 + `blog/project-management-kpis.md`, `blog/project-monitoring-phase.md`
  - Pas de démo obligatoire — texte analytique + captures de 3 scénarios de dashboards.

---

### Task 4.4: Produire le quiz du Module 6 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 6, 6 questions QCM.

---

### Task 4.5: Export board snapshots v-M5 et v-M6

- [ ] **Step 1** : export v-M5 + commit + tag `formation-fb-module-5-done`
- [ ] **Step 2** : export v-M6 + commit + tag `formation-fb-module-6-done`

---

## Phase 5 — Module 7 + livrables annexes (S5)

### Task 5.1: Produire les 6 leçons du Module 7 Industrialiser

Appliquer **Pattern L**. Module culminant — la leçon 7.6 est celle où Michael fait l'export final du Board Agence Template.

**Files :**
- Create : `content/formations/fluentboards/modules/07-industrialiser/01-board-folders.md`
- Create : `content/formations/fluentboards/modules/07-industrialiser/02-bulk-actions.md`
- Create : `content/formations/fluentboards/modules/07-industrialiser/03-import-export.md`
- Create : `content/formations/fluentboards/modules/07-industrialiser/04-migrer-depuis-trello.md`
- Create : `content/formations/fluentboards/modules/07-industrialiser/05-migrer-depuis-asana.md`
- Create : `content/formations/fluentboards/modules/07-industrialiser/06-export-template-final.md`

**Briefs :**

- [ ] **Leçon 7.1 Board folders** — Pattern L
  - Objectif : "À la fin, tu as 3 folders 'Clients actifs / Clients dormants / Interne' avec chacun 2-3 boards."
  - Sources : `docs/boards-with-folders.md`

- [ ] **Leçon 7.2 Bulk actions (table view)** — Pattern L
  - Objectif : "À la fin, tu déplaces 10 tasks d'un seul coup en table view + assignes une label à 20 tasks."
  - Sources : `blog/table-view-for-project-management.md` + docs récents

- [ ] **Leçon 7.3 Import/Export d'un board entier** — Pattern L
  - Objectif : "À la fin, tu exportes un board en JSON et tu l'importes dans un autre site WP."
  - Sources : `docs/import-boards-into-fluentboards.md`

- [ ] **Leçon 7.4 Migrer depuis Trello** — Pattern L
  - Objectif : "À la fin, tu as importé un board Trello complet (cards + labels + members) dans FluentBoards."
  - Sources : `docs/import-from-trello.md`, `youtube/07-ILQlmRk1qz4.md`, `youtube/24-99VfIHTnYj0.md`
  - Pièges : checklists Trello converties en sous-tâches (pas toujours fidèle).

- [ ] **Leçon 7.5 Migrer depuis Asana** — Pattern L
  - Objectif : "À la fin, tu as importé un projet Asana complet dans FluentBoards."
  - Sources : `docs/import-boards-from-asana.md`, `youtube/09-iXgVw3wctOE.md`

- [ ] **Leçon 7.6 FINAL — exporter le board agence template + packaging** — Pattern L — **CULMINATION**
  - Objectif : "À la fin, tu as téléchargé le fichier `board-template-agence.json` et tu sais le réimporter pour chaque nouveau client."
  - Démo : 5 min step-by-step — export + sanitize + import dans un nouveau board blank.
  - **Spécial** : cette leçon inclut le download link vers le livrable final dans TutorLMS zone ressources.

---

### Task 5.2: Produire le quiz du Module 7 — Pattern Q

- [ ] Appliquer Pattern Q complet pour Module 7, 6 questions QCM.

---

### Task 5.3: Exporter + sanitize le Board Agence Template final

**Files :**
- Create : `content/formations/fluentboards/livrables/board-template-agence.json`
- Create : `content/formations/fluentboards/livrables/board-snapshots/v-M7-final.json` (snapshot archive)
- Create : `tools/scripts/sanitize-fluentboards-export.py`

- [ ] **Step 1 : finaliser le board dans FluentBoards**

Dernière passe : vérifier que le board "Agence Template" contient :
- 4 stages nommés proprement (Backlog / En cours / Review / Done)
- 1 stage default assignee configuré
- 1 task template "Nouveau projet client" avec 8 sous-tâches types
- 3 custom fields (Priorité / Client / Deadline)
- 5 labels colorés
- 2-3 exemples de tasks avec sous-tâches
- 1 recurring task "Réunion équipe hebdo"
- Webhooks configurés : 1 incoming + 1 outgoing (URLs placeholder à remplacer par l'utilisateur)

- [ ] **Step 2 : export JSON**

FluentBoards UI → Board → Settings → Export → JSON. Déplacer le fichier téléchargé vers `content/formations/fluentboards/livrables/board-template-agence.json` + copie dans `board-snapshots/v-M7-final.json`.

- [ ] **Step 3 : écrire le script de sanitization**

Créer `tools/scripts/sanitize-fluentboards-export.py`. Le script doit :

1. Accepter 2 arguments CLI : `INPUT.json OUTPUT.json`
2. Parser le JSON avec `json.loads`
3. Walker récursif (dict + list) qui remplace la valeur des clés sensibles (`user_email`, `user_id`, `author_id`, `created_by`, `updated_by`) par la chaîne `REPLACE_ME`
4. Après re-sérialisation, appliquer 2 regex textuelles :
   - Remplacer `/webhook/<32+ chars hex>` par `/webhook/REPLACE_ME_TOKEN`
   - Remplacer `https://schoolswp.com` par `https://YOUR-WP-SITE.com`
5. Écrire le résultat vers `OUTPUT.json` en UTF-8
6. Print `Sanitized: SRC -> DST`

Respecter le style ruff-compatible du repo (4 spaces, line-length 120, import `from __future__ import annotations`).

- [ ] **Step 4 : appliquer le script in-place**

```
cd "d:/VS Code/CLAUDE CODE/projects/schoolswp"
.venv/Scripts/python tools/scripts/sanitize-fluentboards-export.py content/formations/fluentboards/livrables/board-template-agence.json content/formations/fluentboards/livrables/board-template-agence.json
```

Vérifier manuellement que : aucun email @schoolswp.com ou @michaelkihl.fr ne reste, aucun webhook token hex ne reste, les URLs pointent sur YOUR-WP-SITE.com.

- [ ] **Step 5 : test d'import réel**

Sur un autre site WP (site test), installer FluentBoards + importer le fichier sanitized. Vérifier que l'import crée un board avec stages + task templates + custom fields corrects.

- [ ] **Step 6 : commit**

`git add tools/scripts/sanitize-fluentboards-export.py content/formations/fluentboards/livrables/` puis `git commit -m "feat(formation-fb): board agence template final + sanitize + snapshot v-M7"` puis `git tag formation-fb-module-7-done`.

---

### Task 5.4: Produire la Checklist setup PDF

**Files :**
- Create : `content/formations/fluentboards/livrables/checklist-setup.md`
- Create : `content/formations/fluentboards/livrables/checklist-setup.html`
- Create : `content/formations/fluentboards/livrables/checklist-setup.pdf`

- [ ] **Step 1 : draft Markdown**

Structure : header logo + titre "Checklist setup FluentBoards", 4 sections (Avant d'installer / Installation / Configuration de base / Premier board), environ 30 cases à cocher (2 pages imprimables), footer URL formation + QR code optionnel.

- [ ] **Step 2 : générer HTML via skill cc-design**

Brief : format A4 portrait 2 pages, brand schoolsWP, reproduire exactement le Markdown, cases à cocher visuelles (pas de form HTML), print-ready (print.css inclus). Output : `content/formations/fluentboards/livrables/checklist-setup.html`.

- [ ] **Step 3 : convertir HTML vers PDF**

Utiliser le script `tools/scripts/html_to_pdf.py` (existe déjà, réutilisé pour PDF Telegram ecosystem 2026-04-20) ou équivalent weasyprint :

```
.venv/Scripts/python tools/scripts/html_to_pdf.py content/formations/fluentboards/livrables/checklist-setup.html content/formations/fluentboards/livrables/checklist-setup.pdf
```

- [ ] **Step 4 : commit**

`git add content/formations/fluentboards/livrables/checklist-setup.md content/formations/fluentboards/livrables/checklist-setup.html content/formations/fluentboards/livrables/checklist-setup.pdf` puis `git commit -m "feat(formation-fb): livrable checklist setup PDF"`.

---

### Task 5.5: Produire le Tableau de routage webhooks

**Files :**
- Create : `content/formations/fluentboards/livrables/webhook-routing-table.md`
- Create : `content/formations/fluentboards/livrables/webhook-routing-table.html`

- [ ] **Step 1 : draft Markdown**

Matrice "Source événement → Payload clé → Stage cible FluentBoards → Tag automatique". Sources à couvrir : Fluent Forms, FluentCRM, FluentSupport, Google Form (via n8n), Typeform (via n8n), Email parsing (via n8n), GitHub issues (via n8n), webhook générique. Format tableau 5-6 colonnes, ~15-20 lignes.

- [ ] **Step 2 : rendre en HTML via cc-design**

Output : `content/formations/fluentboards/livrables/webhook-routing-table.html`. Design : tableau 1 page landscape, lisible projeté.

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/livrables/webhook-routing-table.md content/formations/fluentboards/livrables/webhook-routing-table.html` puis `git commit -m "feat(formation-fb): livrable tableau routage webhooks"`.

---

### Task 5.6: Produire les 3 workflows n8n (formation base)

Appliquer **Pattern W** pour chacun.

**Files :**
- Create : `content/formations/fluentboards/livrables/workflows-n8n/01-bug-github-to-task.json`
- Create : `content/formations/fluentboards/livrables/workflows-n8n/02-lead-form-to-task-crm.json`
- Create : `content/formations/fluentboards/livrables/workflows-n8n/03-support-ticket-to-task.json`
- Create : `content/formations/fluentboards/livrables/workflows-n8n/README.md`

**Briefs :**

- [ ] **Workflow 01 — Bug GitHub → task FluentBoards** — Pattern W
  - Trigger : webhook GitHub (issue created avec label "bug")
  - Action : POST vers incoming webhook FluentBoards (stage "Bugs", label "GitHub")

- [ ] **Workflow 02 — Lead Fluent Forms → task + contact FluentCRM** — Pattern W
  - Trigger : webhook Fluent Forms submission
  - Action 1 : upsert contact FluentCRM (par email)
  - Action 2 : POST task FluentBoards (stage "Leads", label "inbound")

- [ ] **Workflow 03 — Ticket FluentSupport → task** — Pattern W
  - Trigger : webhook FluentSupport (ticket new)
  - Action : POST task FluentBoards (stage "Support", priorité = priorité ticket)

- [ ] **README du dossier workflows-n8n/**

Instructions d'import + prérequis + credentials à configurer.

- [ ] **Commit final du lot**

`git add content/formations/fluentboards/livrables/workflows-n8n/` puis `git commit -m "feat(formation-fb): 3 workflows n8n formation base"`.

---

### Task 5.7: Produire les 7 workflows n8n additionnels (order bump)

Appliquer **Pattern W** pour chacun.

**Files :**
- Create : `content/formations/fluentboards/livrables/workflows-n8n/04-*.json` à `10-*.json` (7 fichiers) + mise à jour du README.

**Briefs :**

- [ ] **04 — Lead FluentForms + score > 70 → task high-priority + contact CRM**
- [ ] **05 — Recap hebdo Slack/Telegram avec tasks en retard** (cron hebdo → fetch tasks en retard → message → Slack + Telegram)
- [ ] **06 — Création automatique de sous-tâches depuis un template** (task créée avec tag "template:new-client" → 8 sous-tâches prédéfinies)
- [ ] **07 — Archivage automatique des tasks > 60 jours** (cron quotidien → fetch tasks stage Done > 60 j → archiver)
- [ ] **08 — Import en masse de tasks depuis un Google Sheet** (trigger manuel avec URL sheet → lire rows → POST tasks)
- [ ] **09 — Synchro bidirectionnelle FluentBoards ↔ Notion** (si faisable — sinon remplacer par Airtable)
- [ ] **10 — Notification Discord enrichie avec 3 outils (gif, markdown, threads)** (outgoing webhook FluentBoards sur task completed → POST Discord riche)

- [ ] **Mise à jour README + commit groupé**

`git add content/formations/fluentboards/livrables/workflows-n8n/` puis `git commit -m "feat(formation-fb): 7 workflows n8n order bump"`.

---

## Phase 6 — Sales page + videos + tunnel (S6)

### Task 6.1: Draft la copy de la sales page

**Files :**
- Create : `content/formations/fluentboards/sales/sales-copy.md`

- [ ] **Step 1 : déléguer à l'agent studio (ou pulse pour positioning)**

Brief : produire la copy complète (~2000 mots) suivant la structure spec :
- Headline + sub-headline
- Video pitch placeholder
- Ce qui est inclus (7 modules + 4 livrables + certificat + support email + garantie)
- Qu'est-ce que tu vas savoir faire (résultats concrets)
- Pour qui
- Pas pour toi si (exclusions)
- Preuve sociale (placeholder avec [TESTIMONIAL] marker)
- Démo board template (description des screenshots)
- Bio
- Pricing early bird 67 € / public 97 € + order bump 27 €
- Garantie 14 jours
- FAQ 10 questions
- CTA final FOMO

Tutoiement. Aucun mot interdit (`.claude/rules/branding.md`). Tone = direct, concret, preuves-first.

- [ ] **Step 2 : relecture + ajustements Michael**

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/sales/sales-copy.md` puis `git commit -m "feat(formation-fb): sales page copy draft"`.

---

### Task 6.2: Construire la sales page HTML via skill cc-design

**Files :**
- Create : `content/formations/fluentboards/sales/sales-page.html`
- Create : `content/formations/fluentboards/sales/sales-page-assets/` (images exportées board template, screenshots modules)

- [ ] **Step 1 : invoquer le skill cc-design**

Brief :
- Source copy : `content/formations/fluentboards/sales/sales-copy.md`
- Brand : schoolsWP (cf. `content/docs/BRAND_RULES.md`)
- Format : landing page 1 colonne, responsive mobile-first
- Composants : hero (headline + video placeholder + CTA early bird), features list, testimonials placeholder, démo board template (screenshots + caption), pricing box, FAQ accordéon, CTA final avec compte à rebours FluentCart
- Pas d'animations lourdes
- Print CSS inclus

- [ ] **Step 2 : valider rendu**

Ouvrir `sales-page.html` dans navigateur. Vérifier :
- Rendu brand-strict (couleurs, typographies, logo)
- Tous les CTA pointent bien vers FluentCart checkout URL
- Mobile : 320px, 768px, 1024px → pas de débordement
- Lighthouse : Performance ≥ 90, Accessibility ≥ 95

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/sales/sales-page.html content/formations/fluentboards/sales/sales-page-assets/` puis `git commit -m "feat(formation-fb): sales page HTML built via cc-design"`.

---

### Task 6.3: Publier la sales page sur schoolswp.com

**Files :** aucun dans le repo (publication WP)

- [ ] **Step 1 : créer la page WP**

wp-admin → Pages → Add New
- Title : "Formation FluentBoards de zéro à pro"
- Slug : `formations-fluentboards-de-zero-a-pro`
- URL cible : `schoolswp.com/formations/fluentboards/` (créer d'abord une page parent "Formations" si elle n'existe pas)

- [ ] **Step 2 : intégrer le HTML**

Soit coller le HTML dans un bloc HTML Gutenberg (simple, rapide). Soit créer un template page dédié via Kadence child theme. Choisir l'option simple pour MVP.

- [ ] **Step 3 : QA en live**

URL fonctionne, tous les liens internes (CTA) vers FluentCart checkout, meta tags title + description SEO + og:image, robot meta `index,follow`.

- [ ] **Step 4 : Rank Math SEO meta**

Via wp-admin UI (API REST silent-ignore — cf. mémoire `reference_rank_math_rest_limits.md`). Title + description + focus keyword "formation fluentboards".

- [ ] **Step 5 : commit des notes**

`git add content/formations/fluentboards/sales/README.md` puis `git commit -m "chore(formation-fb): sales page published at schoolswp.com"`.

---

### Task 6.4: Enregistrer la video pitch 90 s

**Files :**
- Create local (non versionné) : `content/formations/fluentboards/assets/demos/_pitch-90s.mp4`
- Create : `content/formations/fluentboards/sales/video-pitch-90s-script.md`

- [ ] **Step 1 : écrire le script 90 s**

Structure :
- 0-10 s : hook (douleur audience D)
- 10-50 s : promesse formation + 3 résultats clés
- 50-80 s : démo ultra-rapide du Board Agence Template
- 80-90 s : CTA vers sales page

- [ ] **Step 2 : enregistrer**

Via OBS (template défini en Task 0.8), éventuellement avec face cam si Michael veut. Sinon screen-only + callouts.

- [ ] **Step 3 : monter + uploader**

Couper intro/outro si besoin. Export MP4 1080p. Uploader sur YouTube non-listé OU directement en self-hosted WP (dossier médiathèque /formations/).

- [ ] **Step 4 : intégrer dans la sales page**

Remplacer le placeholder video dans `sales-page.html` (Task 6.2) par l'embed YouTube ou la balise `<video>` self-hosted.

- [ ] **Step 5 : commit**

`git add content/formations/fluentboards/sales/video-pitch-90s-script.md` puis `git commit -m "feat(formation-fb): video pitch 90s script + embedded in sales page"`.

---

### Task 6.5: Enregistrer la video welcome 2 min (intro cours)

**Files :**
- Create local (non versionné) : `content/formations/fluentboards/assets/demos/_welcome-2min.mp4`
- Create : `content/formations/fluentboards/modules/00-welcome/welcome-script.md`

- [ ] **Step 1 : créer la section "0. Welcome" dans TutorLMS**

wp-admin → TutorLMS → Course → Ajouter section en position 0 "Démarre ici" avec 1 leçon "Bienvenue".

- [ ] **Step 2 : écrire le script 2 min**

Structure :
- 0-30 s : bienvenue, pourquoi tu as acheté cette formation
- 30-60 s : overview des 7 modules + fil rouge
- 60-90 s : comment utiliser la plateforme (progression, quiz, certificat, ressources)
- 90-120 s : promesse support + "prochaine leçon : Setup 1.1"

- [ ] **Step 3 : enregistrer + monter + uploader**

- [ ] **Step 4 : publier dans TutorLMS section 0**

Coller embed video + texte de transition.

- [ ] **Step 5 : commit**

`git add content/formations/fluentboards/modules/00-welcome/welcome-script.md` puis `git commit -m "feat(formation-fb): video welcome 2min + section 0 TutorLMS"`.

---

### Task 6.6: Polish thank-you page FluentCart

**Files :** aucun dans le repo (config WP)

- [ ] **Step 1 : personnaliser la thank-you page**

FluentCart → Settings → Thank-you page :
- Titre : "Bienvenue dans FluentBoards de zéro à pro !"
- Message : instructions courtes (email + lien direct cours) + rappel support 48 h + lien télécharger pack ressources
- Optionnel : placeholder upsell (pour v2, skip maintenant)

- [ ] **Step 2 : QA**

Refaire un achat test, vérifier que la thank-you page affiche bien le contenu.

- [ ] **Step 3 : commit des notes**

`git add content/formations/fluentboards/plan.md` puis `git commit -m "chore(formation-fb): thank-you page personalized"`.

---

### Task 6.7: QA end-to-end complet du tunnel (Gate S6)

**Files :** aucun (test)

- [ ] **Step 1 : refaire les 12 checkpoints de Task 0.7 avec le contenu réel en place**

Tout est peuplé cette fois (sales page, 7 modules, 4 livrables, videos, emails automations). Aucun placeholder ne doit rester dans le parcours apprenant.

- [ ] **Step 2 : ajouter 4 checkpoints supplémentaires**

13. Vidéo pitch sur sales page joue sans erreur sur mobile + desktop
14. Vidéo welcome dans TutorLMS joue dès connexion
15. Certificat généré correctement après avoir tout complété en mode test
16. Download des 4 livrables fonctionne (JSON import réel, PDF s'ouvre, workflows s'importent dans n8n)

- [ ] **Step 3 : si tout OK, tagger la release**

`git commit --allow-empty -m "chore(formation-fb): S6 QA passed ready for pre-launch"` puis `git tag formation-fb-ready-for-launch`.

---

## Phase 7 — Pré-lancement SEO + contenu (S7)

### Task 7.1: Publier l'article "FluentBoards avis complet"

**Files :**
- Create : `content/articles/fluentboards-avis/v3.md` (structure standard article pipeline schoolsWP)

- [ ] **Step 1 : brief SEO**

Via agent `radar` : brief SEO pour le mot-clé "fluentboards avis" + variantes + intent commercial.

- [ ] **Step 2 : production pipeline**

Via `brain-lite.bat` (pipeline 5 étapes) :

```
cd "d:/VS Code/CLAUDE CODE/projects/schoolswp"
brain-lite.bat --keyword "fluentboards avis" --intent commerciale --pilier crm
```

L'intent "commerciale" oriente vers une review qui convertit. Pilier "crm" car FluentBoards s'intègre dans l'écosystème crm-fluentcrm.

- [ ] **Step 3 : ajouter les captures réelles**

Rappel mémoire `project_review_accounts.md` : Michael a un compte Pro FluentBoards → captures réelles, pas IA ni scraping.

- [ ] **Step 4 : ajouter le CTA formation**

Encart dédié "Si tu veux maîtriser FluentBoards de A à Z, on a une formation dédiée" → lien `schoolswp.com/formations/fluentboards/`.

- [ ] **Step 5 : publier sur WP**

Via MCP novamira-schoolswp-com ou UI wp-admin. Metadata SEO via UI Rank Math (pas REST — cf. mémoire).

- [ ] **Step 6 : commit**

`git add content/articles/fluentboards-avis/` puis `git commit -m "feat(articles): fluentboards-avis commerciale pilier crm published"`.

---

### Task 7.2: Rédiger la séquence email lancement (4 emails)

**Files :**
- Create : `content/formations/fluentboards/sales/email-sequence.md`

- [ ] **Step 1 : déléguer à studio (rédaction) + flow (setup FluentCRM)**

Brief 4 emails :

1. **Email #1 — J-3 : teaser**
   - Subject : "Je prépare quelque chose depuis 9 semaines"
   - Corps : raconte pourquoi tu as créé cette formation, problème résolu, promesse rendez-vous J0
2. **Email #2 — J0 : annonce lancement + early bird**
   - Subject : "C'est ouvert — 30 places à 67 € (au lieu de 97 €)"
   - Corps : promesse + ce qui est inclus + CTA sales page + compte à rebours
3. **Email #3 — J+3 : social proof + FAQ**
   - Subject : "Ce que disent les 8 premiers acheteurs"
   - Corps : 2-3 témoignages (réels ou preuves concrètes premiers achats) + 3 FAQ
4. **Email #4 — J+7 : last call early bird**
   - Subject : "Dernières heures à 67 € (puis 97 €)"
   - Corps : urgence + rappel garantie 14 j + CTA final

- [ ] **Step 2 : créer dans FluentCRM**

Email Campaigns → New pour chaque email. Scheduler au bon jour.

- [ ] **Step 3 : test envoi à soi-même**

Envoyer chaque email à une adresse test avant activation. Vérifier : rendu HTML desktop + mobile, liens fonctionnels, unsubscribe visible.

- [ ] **Step 4 : commit**

`git add content/formations/fluentboards/sales/email-sequence.md` puis `git commit -m "feat(formation-fb): email sequence 4 emails J-3 to J+7"`.

---

### Task 7.3: Rédiger les 3 posts LinkedIn

**Files :**
- Create : `content/formations/fluentboards/sales/linkedin-posts.md`

- [ ] **Step 1 : déléguer à pulse**

Brief :
- Post #1 (J-3) : teaser — question "comment tu gères tes projets clients dans WP ?" + preview formation
- Post #2 (J0) : annonce lancement avec carousel image 5 slides (module + livrable à chaque slide)
- Post #3 (J+7) : bilan early bird (nombre places vendues, premiers retours apprenants)

Format : 1200-1500 caractères par post, tutoiement, 3-5 hashtags pertinents, CTA en dernière ligne.

- [ ] **Step 2 : production visuelle (Canva ou skill cc-design)**

3 images/carrousels : #1 hero image formation, #2 carousel 5 slides, #3 screenshot + métriques.

- [ ] **Step 3 : planifier dans Blotato**

Via skill `social-media-manager` ou UI Blotato, planifier les 3 posts aux bonnes dates.

- [ ] **Step 4 : commit**

`git add content/formations/fluentboards/sales/linkedin-posts.md` puis `git commit -m "feat(formation-fb): 3 LinkedIn posts teaser launch bilan"`.

---

### Task 7.4: Vérifier la tagification "early-bird" dans FluentCRM

**Files :** aucun (config WP)

- [ ] **Step 1 : créer une automation "tag early-bird aux 30 premiers"**

FluentCRM → Automations → modifier l'automation "Welcome + enroll" (Task 0.6). Ajouter Action : si `count(contacts with tag 'formation-fluentboards') <= 30` alors add tag 'early-bird'. Alternative plus simple : tag manuellement les 30 premiers en fin de lancement.

- [ ] **Step 2 : test**

Faire un achat test, vérifier que le tag 'early-bird' est bien appliqué.

---

### Task 7.5: Gate pré-lancement

- [ ] **Step 1 : checklist finale**

Sur `content/formations/fluentboards/plan.md`, section "Checklist pré-lancement" :
- Cours TutorLMS : 7 modules + 40 leçons + 7 quiz + certificat OK
- 4 livrables publiés et téléchargeables
- Sales page en ligne + mobile OK + Lighthouse ≥ 90
- FluentCart checkout + order bump testés
- FluentCRM automation welcome + 4 emails séquence OK
- Video pitch 90 s + video welcome 2 min publiées
- Article "FluentBoards avis" publié sur schoolswp.com
- 3 posts LinkedIn planifiés dans Blotato
- QA 12+4 checkpoints Task 6.7 passés

- [ ] **Step 2 : tag release candidate**

`git commit --allow-empty -m "chore(formation-fb): pre-launch checklist complete RC1"` puis `git tag formation-fb-rc1`.

---

## Phase 8 — Lancement early bird (S8)

### Task 8.1: J-3 — teaser email + LinkedIn post #1

- [ ] **Step 1** : déclencher email #1 dans FluentCRM (scheduled → check envoi OK)
- [ ] **Step 2** : publier LinkedIn post #1 via Blotato (check rendu post live)
- [ ] **Step 3** : monitor — ouvertures email, impressions LinkedIn, clics vers sales page.

---

### Task 8.2: J0 — Lancement officiel

- [ ] **Step 1** : activer l'offre early bird dans FluentCart (vérifier prix 67 € + compteur 30 places affiché)
- [ ] **Step 2** : déclencher email #2 dans FluentCRM
- [ ] **Step 3** : publier LinkedIn post #2 avec carousel
- [ ] **Step 4** : annoncer dans tes canaux schoolsWP existants — newsletter, Discord, etc.
- [ ] **Step 5** : monitor heures H+2 / H+6 / H+24 — ventes early bird, CTR email, erreurs tunnel (si support email reçoit plus de 2 questions = bug, diagnostiquer)
- [ ] **Step 6** : noter les bugs/frictions dans `plan.md` section "Launch day log"

---

### Task 8.3: J+3 — Rappel mi-campagne

- [ ] **Step 1** : déclencher email #3 social proof
- [ ] **Step 2** : mettre à jour sales page avec "X / 30 places vendues"
- [ ] **Step 3** : monitor ventes et ajuster

---

### Task 8.4: J+7 — Last call

- [ ] **Step 1** : déclencher email #4 last call
- [ ] **Step 2** : publier LinkedIn post #3 bilan
- [ ] **Step 3** : fin de journée — clore l'early bird, passer le prix à 97 €

wp-admin → FluentCart → Product Formation → Price : 97 €. Sauver. Sales page : modifier le HTML (enlever le badge "early bird 67 € jusqu'à 30 places" → remplacer par prix public 97 €). Commit le diff : `git add content/formations/fluentboards/sales/sales-page.html` puis `git commit -m "chore(formation-fb): end of early bird switch to public price 97€"`.

---

## Phase 9 — Transition prix public + bilan (S9)

### Task 9.1: Recueillir feedback apprenants

**Files :**
- Create : `content/formations/fluentboards/feedback/s9-launch-feedback.md`

- [ ] **Step 1 : envoyer email enquête à tous les acheteurs**

FluentCRM → Campaign one-shot à la liste "Formation FluentBoards acheteurs" :
- Subject : "3 questions pour améliorer la formation"
- 3 questions : (a) Qu'as-tu trouvé le plus utile ? (b) Qu'est-ce qui manque ? (c) Note NPS (0-10)

- [ ] **Step 2 : compiler les réponses** dans `feedback/s9-launch-feedback.md`

---

### Task 9.2: Bilan métriques

**Files :**
- Create : `content/formations/fluentboards/feedback/s9-metrics-review.md`

- [ ] **Step 1 : extraire métriques**

- Ventes early bird : nombre / 30 places
- Ventes post-early : nombre
- Taux conversion sales page (via Fathom/Plausible/GSC)
- Taux adoption order bump
- Taux ouverture + CTR emails
- Taux démarrage cours TutorLMS (user → leçon 1.1)
- Taux complétion (user → module 7)
- Taux remboursement

- [ ] **Step 2 : rédiger bilan**

Dans `feedback/s9-metrics-review.md` : synthèse + analyse (vs cibles spec section 8.3) + décisions pour M+1.

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/feedback/` puis `git commit -m "docs(formation-fb): S9 launch metrics review + apprentis feedback"`.

---

### Task 9.3: Planifier les ajustements M+1

**Files :**
- Modify : `content/formations/fluentboards/plan.md` (section "Backlog v1.1")

- [ ] **Step 1 : lister les quick wins**

Basé sur feedback + métriques, lister :
- Leçons à améliorer (score quiz bas = leçon peu claire)
- FAQ à enrichir (questions récurrentes dans support)
- Tunnel : ajustements sales page si conversion < 2 %

- [ ] **Step 2 : prioriser**

Top 5 tickets à fixer dans les 2 semaines, reste en backlog.

- [ ] **Step 3 : commit**

`git add content/formations/fluentboards/plan.md` puis `git commit -m "docs(formation-fb): v1.1 backlog from S9 learnings"`.

---

### Task 9.4: Décision scope v2 + enchaînement catalogue

**Files :**
- Create : `docs/superpowers/specs/next-decisions-fluent-catalogue.md` (placeholder pour future session brainstorming)

- [ ] **Step 1 : d'après résultats S8-S9**

Si ventes > 20 → préparer upsell OTO "Agency Review" + décider formation #2 (FluentCRM probable).
Si ventes 10-20 → optimiser acquisition avant de produire #2.
Si ventes < 10 → diagnostiquer offre + audience avant tout.

- [ ] **Step 2 : note courte pour la prochaine session brainstorming**

Fichier `docs/superpowers/specs/next-decisions-fluent-catalogue.md` avec les décisions à prendre + inputs requis (métriques S9 déjà compilées).

- [ ] **Step 3 : commit + clôture**

`git add docs/superpowers/specs/next-decisions-fluent-catalogue.md` puis `git commit -m "docs(formation-fb): next-decisions note for v2 catalogue session"` puis `git tag formation-fb-v1-shipped`.

---

## Définition de "done" globale du plan

Le plan est **done** quand tous les tags Git suivants sont posés :

- [ ] `formation-fb-module-1-done` à `formation-fb-module-7-done` (7 tags)
- [ ] `formation-fb-ready-for-launch` (fin S6)
- [ ] `formation-fb-rc1` (fin S7, pré-lancement validé)
- [ ] `formation-fb-v1-shipped` (fin S9, bilan + backlog v1.1 documenté)

---

## Self-Review (effectuée par l'auteur du plan)

**1. Couverture de la spec**

- Spec §2 Cadrage produit → Tasks 0.2, 0.3 (prérequis + bridge) ✅
- Spec §3 Architecture pédagogique → Task 1.1 (plan 40 leçons) + 1.2 à 5.1 (production 40 leçons) ✅
- Spec §3 Livrables 4 items → Tasks 5.3, 5.4, 5.5, 5.6 + 5.7 ✅
- Spec §4 Parcours apprenant → Tasks 0.4, 0.6, 6.5, 6.6 ✅
- Spec §5 Tunnel + pricing → Tasks 0.5, 6.1-6.3, 6.6, 8.4 ✅
- Spec §6 Acquisition → Tasks 7.1, 7.2, 7.3 ✅
- Spec §7 Planning + délégation → cadre global (9 phases) + patterns L/Q/W ✅
- Spec §8 QA + métriques → Tasks 0.7, 6.7, 9.1, 9.2 ✅
- Spec §9 Structure fichiers → Task 0.1 ✅
- Spec §10 Dépendances → Task 0.2 ✅
- Spec §11 v2 → Task 9.4 (note décisions) ✅
- Spec §12 Done MVP → "Définition de done globale" ci-dessus ✅

**2. Scan placeholders**

Aucun "TBD/TODO/implement later/similar to Task N". Les 40 leçons + 7 quiz + 10 workflows n8n sont décomposés nominativement avec objectif, sources archivées exactes et pattern référencé par nom explicite.

**3. Cohérence types/noms**

- Patterns L / Q / W utilisés par nom dans toutes les tâches de production contenu ✅
- Conventions slugs respectées (pas de date ni "schoolswp") ✅
- Tags Git : nomenclature cohérente `formation-fb-*` ✅
- Tous les paths de fichiers sources (`content/docs/fluentboards/...`) vérifiés contre la liste réelle INDEX.md scrapée en session brainstorming ✅

**4. Points de vigilance signalés**

- **Task 0.2 Step 5** : FluentRoadmap licence = gate décisif. Si absent, Module 6 passe de 5 à 4 leçons (Task 4.3 indique explicitement les leçons conditionnelles).
- **Task 0.3** : Bridge FluentCart ↔ TutorLMS = Plan A (natif) ou Plan B (fallback FluentCRM). Décision dès S1, documentée.
- **Task 5.3 Step 5** : test d'import du Board Template sur un autre site WP = critique pour la valeur livrable. Ne pas skipper.
- **Tasks 6.4 + 6.5** : videos = tournages par Michael. Si pas dispo à temps (licences ElevenLabs + HeyGen absentes — mémoire `project_youtube_production_stack.md`), options de repli : voice-over humaine simple, screen-only + callouts + sous-titres texte, ou report v2.
- **Phase 8** : lancement en temps réel. Nécessite la présence active de Michael (pas déléguable à un agent). Bloquer agenda.

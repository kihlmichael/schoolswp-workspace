# 🧠 schoolsWP — Notion Content Engine

## Architecture

```
📄 Articles      ←→  🧠 Clusters         (relation dual)
📄 Articles      ←→  🔌 Plugins & Outils (relation dual)
📊 Dashboard KPI →   vues filtrées sur Articles + Clusters
```

**Principe** : chaque article est un actif mesuré sur 4 axes (SEO / LLM / Conversion / Autorité).
Le Score Global agrège les 4 scores en un seul indicateur de santé.

---

## 1. Setup automatisé (recommandé)

### Prérequis

1. Créer une Notion Integration : [notion.so/my-integrations](https://www.notion.so/my-integrations)
   - Capabilities : Read / Update / Insert content
   - Copier la clé : `secret_xxx`
2. Créer une page Notion vide "schoolsWP Content Engine"
   - Partager la page avec l'integration (bouton "Connect to")
   - Copier l'ID de la page depuis l'URL (`notion.so/PAGE_ID?v=...`)

### Exécution

```bash
NOTION_API_KEY=secret_xxx \
NOTION_PARENT_PAGE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
node scripts/setup-notion.js
```

### Ce que le script crée

- 3 databases (Articles + Clusters + Plugins & Outils)
- 4 relations croisées (dual_property)
- 3 formules (Score Global, Action, % Complétude)
- 4 rollups (Trafic total, Score moyen, Revenus cluster, Revenus générés)
- 6 clusters initiaux + 5 plugins initiaux

### Module Priorité Automatique (à activer séparément)

```bash
NOTION_API_KEY=secret_xxx \
NOTION_ARTICLES_DB_ID=xxx \
node scripts/add-notion-seo-priority.js
```

Ajoute 6 propriétés SEO à la base Articles existante (voir section 2.1 bis).

---

## 2. Schema des 3 bases

### 2.1 📄 Articles — propriétés complètes

| Propriété | Type | Notes |
|-----------|------|-------|
| Titre | Title | Titre éditorial complet |
| URL | URL | URL WordPress publiée |
| Statut | Select | Idée / En cours / Publié / Optimisation |
| Type | Select | Pilier / Satellite / Comparatif / Tutoriel |
| **Cluster** | Relation → Clusters | Cluster sémantique de rattachement |
| Mot-clé principal | Text | Mot-clé cible principal |
| Intent | Select | Informationnelle / Comparative / Décisionnelle |
| Score SEO | Number | /100 — issu du pipeline Content Machine |
| Score LLM | Number | /100 — AI Overview + Citation LLM |
| Score Conversion | Number | /100 — CTA, tunnel, maillage |
| Score Autorité | Number | /100 — expertise, backlinks, cluster |
| **Score Global** | Formula | Calculé automatiquement (voir formule) |
| **Action** | Formula | Label décisionnel basé sur Score Global |
| Position moyenne | Number | GSC — Position moyenne 28j |
| Impressions | Number | GSC — Impressions 28j |
| Clics | Number | GSC — Clics organiques 28j |
| CTR | Number (%) | GSC — CTR moyen 28j |
| Temps moyen (min) | Number | GA4 — Engagement time |
| Taux clic affilié | Number (%) | Clics sortants / sessions |
| Leads générés | Number | Opt-ins / demandes liés à cet article |
| Revenus estimés | Number (€) | CA affilié + leads attribués |
| Présent AI Overview ? | Checkbox | Cocher si l'article apparaît dans AI Overview |
| Citation LLM ? | Checkbox | Cocher si cité par ChatGPT / Gemini / Perplexity |
| CTA optimisé ? | Checkbox | CTA testé et converti |
| Maillage entrant | Number | Nb de liens internes pointant vers cet article |
| Maillage sortant | Number | Nb de liens internes depuis cet article |
| Lien Google Doc | URL | Lien vers le doc Content Machine V2 |
| Date création | Date | Date de publication initiale |
| Dernière MAJ | Date | Dernière mise à jour |

### 2.1 bis 📊 Articles — Module Priorité Automatique (add-notion-seo-priority.js)

| Propriété | Type | Notes |
|-----------|------|-------|
| Volume | Number | Volume de recherche mensuel estimé (GSC, Ahrefs, DataForSEO) |
| Difficulté | Number | KD 0–100 — plus c'est élevé, plus c'est concurrentiel |
| Position actuelle | Number | Position GSC si publié · **100 si article non encore créé** |
| Intent stratégique | Select | Business direct / Autorité / Satellite / Opportunité rapide |
| **Potentiel brut** | Formula | `round(Volume / (Difficulté + 1))` — volume accessible |
| **Score Opportunité** | Formula | Pondération 3 axes : 40% volume · 30% position · 30% intent |

**Formule Score Opportunité** :
```
round(
  (Volume / (Difficulté + 1))                     × 0.4
  + position_score                                × 0.3
  + intent_score                                  × 0.3
)

position_score : > 20 → 10 · 11-20 → 6 · 4-10 → 3 · ≤ 3 → 1
intent_score   : Business direct → 10 · Autorité → 7 · Opportunité rapide → 8 · Satellite → 5
```

**Interprétation** :

| Cas | Profil | Action |
|-----|--------|--------|
| Score élevé + Position > 20 | Jackpot — fort volume, non classé | Écrire maintenant |
| Score élevé + Position 5-15 | Quick Win — optimisation rapide | Title + FAQ + maillage |
| Score moyen + Intent Business direct | Stratégique long terme | Planifier dans le cluster |

**Vues à créer manuellement** :

- **🚀 Priorité rédaction** — tri Score Opportunité DESC, aucun filtre
- **⚡ Quick Wins** — filtres : Position > 5 ET Position < 20 ET Volume > 200, tri Score Opportunité DESC

---

### 2.2 🧠 Clusters — propriétés complètes

| Propriété | Type | Notes |
|-----------|------|-------|
| Nom cluster | Title | ex : "CRM WordPress" |
| **Article pilier** | Relation → Articles | Page pilier du cluster |
| **Articles satellites** | Relation → Articles | Tous les articles du cluster |
| **Trafic total** | Rollup (sum Clics) | Clics organiques cumulés |
| **Score moyen cluster** | Rollup (avg Score Global) | Santé moyenne du cluster |
| **Revenus cluster** | Rollup (sum Revenus estimés) | CA total attribuable au cluster |
| Priorité | Select | Haute / Moyenne / Basse |
| Statut | Select | Actif / En construction / Planifié |
| **% Complétude** | Formula | "Complet ✅" si ≥ 5 articles, sinon "À renforcer 🔧" |

---

### 2.3 🔌 Plugins & Outils — propriétés complètes

| Propriété | Type | Notes |
|-----------|------|-------|
| Nom outil | Title | ex : "FluentCRM" |
| Catégorie | Select | CRM / LMS / Builder / SEO / E-commerce / Performance / Automatisation |
| **Articles liés** | Relation → Articles | Articles qui mentionnent/comparent cet outil |
| **Revenus générés** | Rollup (sum Revenus estimés) | CA affilié total via articles liés |
| Type | Select | Partenaire / Testé / Neutre |
| Score recommandation | Number | /10 — recommandation subjective schoolsWP |
| Lien affilié | URL | URL affilié trackée |
| Notes | Text | Contexte, conditions affilié, notes de test |

---

## 3. Formules (copy-paste)

### Score Global (Articles)

```
round(
  (prop("Score SEO") * 0.25) +
  (prop("Score LLM") * 0.15) +
  (prop("Score Conversion") * 0.30) +
  (prop("Score Autorité") * 0.30)
)
```

### Action (Articles)

```
if(
  prop("Score Global") >= 95, "✅ Actif Premium",
  if(
    prop("Score Global") >= 85, "🟢 Actif Performant",
    if(
      prop("Score Global") >= 70, "🟡 Optimiser",
      "🔴 Révision Stratégique"
    )
  )
)
```

### % Complétude (Clusters)

```
if(length(prop("Articles satellites")) >= 5, "Complet ✅", "À renforcer 🔧")
```

---

## 4. Page Dashboard KPI (configuration manuelle)

> La page Dashboard n'est pas créable via API. Suivre ces étapes dans Notion.

### Étape 1 — Créer la page

Dans la page parente "schoolsWP Content Engine" :
→ Nouveau bloc → Page → Titre : "📊 Dashboard KPI"

### Étape 2 — Ajouter 4 vues filtrées de la base Articles

Dans la page Dashboard, ajouter un bloc "Linked database view" pointant vers Articles.
Créer 4 vues :

---

#### Vue 1 — 🔥 Articles à optimiser

- **Type de vue** : Table
- **Filtre** : Score Global < 85
- **Tri** : Score Global ASC (les plus urgents en premier)
- **Colonnes visibles** : Titre, Cluster, Score Global, Action, Position moyenne, CTR, Dernière MAJ
- **Colonnes masquées** : tout le reste

---

#### Vue 2 — 🚀 Actifs Premium

- **Type de vue** : Gallery ou Table
- **Filtre** : Score Global ≥ 90
- **Tri** : Revenus estimés DESC
- **Colonnes visibles** : Titre, Cluster, Score Global, Action, Clics, Revenus estimés
- **Couleur carte** : Score Global (vert = ≥ 95)

---

#### Vue 3 — 🧱 Clusters incomplets

- **Vue sur** : base Clusters (pas Articles)
- **Type de vue** : Table
- **Filtre** : % Complétude = "À renforcer 🔧"
- **Tri** : Priorité (Haute → Basse)
- **Colonnes visibles** : Nom cluster, % Complétude, Trafic total, Score moyen cluster, Priorité, Statut

---

#### Vue 4 — 💰 Top revenus

- **Type de vue** : Table
- **Filtre** : Revenus estimés > 0
- **Tri** : Revenus estimés DESC
- **Colonnes visibles** : Titre, Cluster, Revenus estimés, Clics, Score Global, Taux clic affilié, Leads générés

---

### Étape 3 — Ajouter la Vue Executive

En haut de la page Dashboard, ajouter une section "🎯 Vue Executive" avec :

**Scorecards** (blocs Notion "Callout" ou formules liées) :
- Nombre total d'articles : `=countall(Articles)` ← créer une DB view avec count
- Score moyen global : rollup visible dans un bloc

Ou plus simplement : créer une vue de type **Board** sur la base Articles avec :
- Regroupement par : **Action** (4 colonnes : Actif Premium / Actif Performant / Optimiser / Révision)
- Chaque carte affiche : Score Global, Clics, Cluster

---

## 5. Intégration n8n

### notion-kpi-tracker.json (déjà créé)

Ce workflow reçoit les données de chaque article généré par Content Machine V2
et crée automatiquement une page dans la base Articles.

**Configurer** :
1. Dans n8n : importer `workflows/notion-kpi-tracker.json`
2. Dans le node `Code - Build Notion Payload` :
   - Remplacer `VOTRE_NOTION_DATABASE_ID` → ID de la base Articles
3. Activer le workflow

**Données transmises automatiquement depuis V2** :
- Mot-clé, sujet, intent, pilier, objectif, audience
- Score SEO, Score Conversion, Score Autorité, Publish Score
- Priorité (A/B/C), Diagnostic, Lien Google Doc
- Cluster role + maillage + satellites

**Données à renseigner manuellement** :
- URL (après publication WordPress)
- Position moyenne, Impressions, Clics, CTR (via GSC ou kpi-dashboard-updater.json)
- Présent AI Overview ?, Citation LLM ? (mensuel)
- Revenus estimés, Leads générés (mensuel)

---

### kpi-dashboard-updater.json (Google Sheets → peut alimenter Notion)

Le workflow met à jour les données GSC chaque lundi. Pour synchroniser ces données
dans Notion, ajouter un node HTTP après le node "Code - Parse GSC + Compute Scores"
qui envoie un PATCH vers l'API Notion pour chaque article :

```
PATCH https://api.notion.com/v1/pages/{PAGE_ID}
{
  "properties": {
    "Position moyenne": { "number": 4.2 },
    "Clics":            { "number": 312 },
    "Impressions":      { "number": 8500 },
    "CTR":              { "number": 0.0367 },
    "Dernière MAJ":     { "date": { "start": "2026-03-01" } }
  }
}
```

Nécessite un mapping `Mot-clé → Notion Page ID` (stocker dans Google Sheets colonne S).

---

## 6. Rythme d'utilisation

```
Après chaque article généré (auto) :
  ✅ notion-kpi-tracker.json crée la fiche dans Articles
  → Ajouter manuellement : URL + Cluster (relation)

Chaque lundi (auto via kpi-dashboard-updater.json) :
  ✅ Google Sheets DASHBOARD mis à jour (GSC + Score Global)
  → Reporter manuellement Position/Clics/CTR dans Notion OU brancher le sync

Mensuel (30 min) :
  → Cocher "Présent AI Overview ?" et "Citation LLM ?" pour chaque article
  → Vue 3 (Clusters incomplets) → décision production
  → Mettre à jour Revenus estimés sur les articles affiliés

Trimestriel (1h) :
  → Vue Executive Board → état du portefeuille
  → Vue 2 (Actifs Premium) → quels articles méritent une mise à jour ?
  → Vue 4 (Top revenus) → où concentrer les efforts CRO ?
  → Lancer Content Factory W3 sur 2-3 articles Score Global < 70
```

---

## 7. Score ROI Cluster (add-notion-roi-cluster.js)

Ajoute à la base **Clusters** 6 rollups + 3 formules pour piloter le ROI par cluster.

### Propriétés ajoutées

| Propriété | Type | Source |
|-----------|------|--------|
| Impressions totales | Rollup (sum) | Articles satellites → Impressions |
| CTR moyen cluster | Rollup (avg) | Articles satellites → CTR |
| Position moyenne cluster | Rollup (avg) | Articles satellites → Position moyenne |
| Score Autorité moyen | Rollup (avg) | Articles satellites → Score Autorité |
| Leads cluster total | Rollup (sum) | Articles satellites → Leads générés |
| Nombre d'articles | Rollup (count_all) | Articles satellites → Titre |
| **Taux conversion (%)** | Formula | `if(Trafic > 0, round(Leads/Trafic × 10000)/100, 0)` |
| **Score ROI Cluster** | Formula | Voir formule ci-dessous |
| **Label ROI** | Formula | 🚀 ≥90 · 🟢 ≥80 · 🟡 ≥70 · 🔴 <70 |

### Formule Score ROI Cluster

```
min(100, round(
  (Trafic total cluster / 1000) × 0.25
  + (Revenus cluster / 500)     × 0.30
  + (Score Autorité moyen / 100) × 0.20
  + if(% Complétude == "Complet ✅", 1, 0.5) × 0.25
) × 100)
```

**Calibrage** : ajuster les dénominateurs (1000, 500) selon les volumes réels du site.

### Commande ROI Cluster

```bash
NOTION_API_KEY=secret_xxx \
NOTION_CLUSTERS_DB_ID=xxx \
node scripts/add-notion-roi-cluster.js
```

### Vues ROI Cluster à créer

- **🎯 Priorité Business** — tri Score ROI Cluster DESC, toutes colonnes ROI
- **🔍 Potentiel sous-exploité** — Score ROI < 70 ET Impressions > 500
- **📈 À compléter en priorité** — % Complétude = "À renforcer 🔧" ET Score Autorité moyen > 60

---

## 8. Roadmap Content Trimestrielle (setup-notion-roadmap.js)

Crée une page de pilotage stratégique par trimestre + enrichit la base Clusters.

### Contenu créé par le script

**Phase 1 — 4 propriétés dans la base Clusters** :

| Propriété       | Type   | Valeurs                             |
| --------------- | ------ | ----------------------------------- |
| Priorité Q[N]   | Select | Haute / Moyenne / Basse             |
| Impact business | Select | Très élevé / Élevé / Moyen / Faible |
| Difficulté SEO  | Number | KD 0-100                            |
| ROI potentiel   | Select | Très élevé / Élevé / Moyen / Faible |

**Phase 2 — Page "🗓 Roadmap Content Q[N] [YEAR]"** avec 4 blocs :

1. Vue Stratégique — Thème + KPI cibles (trafic/leads/revenus/articles/score)
2. Priorités Clusters — Sélection + instructions linked database view
3. Backlog Stratégique — Articles Idée intent Décisionnelle/Comparative
4. Plan 90 jours — Mois 1 Fondations / Mois 2 Expansion / Mois 3 Optimisation
5. Weekly Check — 5 KPI à tracker chaque lundi
6. Vision Long Terme — Objectif annuel + jalons

### Commande Roadmap

```bash
NOTION_API_KEY=secret_xxx \
NOTION_PARENT_PAGE_ID=xxx \
NOTION_CLUSTERS_DB_ID=xxx \
node scripts/setup-notion-roadmap.js --quarter Q1 --year 2026
```

Options : `--quarter Q1|Q2|Q3|Q4` · `--year YYYY` · `--skip-clusters`

### Vues Roadmap à créer manuellement

- **🎯 Clusters prioritaires Q[N]** — Clusters avec Priorité Q[N] = Haute, tri ROI potentiel
- **📋 Backlog stratégique** — Articles Idée + intent Décisionnelle/Comparative
- **📈 Weekly Check** — Articles mis à jour cette semaine OU Score Global < 80

---

## 9. Connexion Looker Studio (optionnel)

Notion ne connecte pas directement à Looker Studio.
Deux approches :

**Option A — Via Google Sheets** :
Le workflow `kpi-dashboard-updater.json` maintient Google Sheets à jour.
Looker Studio lit Google Sheets (connecteur natif). Architecture déjà documentée
dans `docs/looker-studio-dashboard.md`.

**Option B — Via export Notion CSV** :
Exporter la base Articles en CSV → importer dans Google Sheets → connecter à Looker Studio.
Automation possible via l'API Notion + un workflow n8n hebdomadaire.

---

## 8. Checklist de lancement

```
□ Integration Notion créée et partagée avec la page parente
□ Script setup-notion.js exécuté sans erreur
□ 3 IDs de bases sauvegardés dans .env
□ notion-kpi-tracker.json importé dans n8n + NOTION_DATABASE_ID configuré
□ Page "📊 Dashboard KPI" créée avec 4 vues filtrées
□ Vue Executive Board (regroupement par Action) configurée
□ 6 clusters initiaux visibles dans la base Clusters
□ Test : envoyer un webhook manuel vers /notion-kpi → vérifier création article
□ Partage du workspace Notion avec l'équipe (si applicable)
```

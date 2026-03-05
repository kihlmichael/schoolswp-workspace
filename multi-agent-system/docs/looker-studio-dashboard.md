# 📊 schoolsWP — Looker Studio Dashboard Setup

## Architecture

```
GSC (URL Impression)   ──►  Page 1 : Vue Executive
                       ──►  Page 2 : Performance SEO
                       ──►  Page 3 : Analyse Cluster
                       ──►  Page 4 : Optimisation Stratégique

GA4 (optionnel)        ──►  Page 4 : Corrélation Business
```

**Principe** : un seul rapport, 4 pages, pilotage complet de schoolsWP comme un média stratégique.
Chaque page répond à une question concrète — on ne regarde pas "est-ce que j'ai du trafic" mais
"quel cluster gagne, quel pilier faiblit, où injecter l'effort".

---

## 1. Sources de données

### 1.1 Google Search Console — URL Impression

> Utiliser **URL Impression** (pas "Site Impression") pour avoir la dimension Page + Requête simultanément.

1. Nouveau rapport Looker Studio → **Ajouter des données**
2. Chercher **Google Search Console**
3. Choisir le site `https://schoolswp.com/`
4. Table : **URL Impression**
5. Nommer la source : `GSC — schoolsWP`
6. Cocher **"Inclure les données Today"** si disponible

Dimensions disponibles :
| Dimension | Usage |
|-----------|-------|
| `Page` | URL complète de l'article |
| `Query` | Mot-clé saisi par l'internaute |
| `Date` | Jour (format YYYYMMDD) |
| `Country` | Pays |
| `Device` | Desktop / Mobile / Tablet |
| `Search Type` | Web / Image / Video |

Métriques disponibles :
| Métrique | Usage |
|----------|-------|
| `Clicks` | Clics organiques |
| `Impressions` | Nombre d'affichages SERP |
| `CTR` | Taux de clic (Clicks / Impressions) |
| `Position` | Position moyenne pondérée |

### 1.2 GA4 (optionnel — Page 4)

1. Ajouter données → **Google Analytics 4**
2. Sélectionner la propriété schoolsWP
3. Nommer : `GA4 — schoolsWP`
4. Dimensions utiles : `Page path`, `Session source / medium`
5. Métriques utiles : `Sessions`, `Engaged sessions`, `Engagement rate`, `Average engagement time`

> Pour joindre GSC + GA4 : créer un champ calculé `Page path` normalisé dans les deux sources
> (retirer `https://schoolswp.com` du champ `Page` GSC via REGEXP_REPLACE).

---

## 2. Champs personnalisés (à créer avant les pages)

> Menu Ressources → Gérer les sources de données → Modifier → + Ajouter un champ.
> Créer tous ces champs sur la source **GSC — schoolsWP**.

---

### 2.1 Cluster

**Nom** : `Cluster`
**Type** : Texte
**Formule** :

```
CASE
  WHEN REGEXP_CONTAINS(Page, "(?i)\\bcrm\\b|fluentcrm|hubspot-wordpress")
    THEN "CRM WordPress"
  WHEN REGEXP_CONTAINS(Page, "(?i)\\blms\\b|tutor-lms|learnpress|lifterLMS|formation")
    THEN "LMS WordPress"
  WHEN REGEXP_CONTAINS(Page, "(?i)woocommerce|boutique|ecommerce|e-commerce|shop")
    THEN "WooCommerce"
  WHEN REGEXP_CONTAINS(Page, "(?i)automatisation|n8n|zapier|make\\.com|webhook|workflow")
    THEN "Automatisation"
  WHEN REGEXP_CONTAINS(Page, "(?i)performance|vitesse|cache|wp-rocket|pagespeed|core-web")
    THEN "Performance"
  WHEN REGEXP_CONTAINS(Page, "(?i)comparatif|comparaison|\\bvs\\b|-vs-|meilleur-plugin")
    THEN "Comparatifs"
  WHEN REGEXP_CONTAINS(Page, "(?i)\\bseo\\b|yoast|rankmath|rank-math|mots-cles|balise")
    THEN "SEO WordPress"
  ELSE "Autres"
END
```

---

### 2.2 Catégorie Position

**Nom** : `Catégorie Position`
**Type** : Texte
**Formule** :

```
CASE
  WHEN Position <= 3  THEN "🥇 Top 3"
  WHEN Position <= 10 THEN "🟢 Page 1"
  WHEN Position <= 20 THEN "🟡 Page 2"
  WHEN Position <= 50 THEN "🟠 Page 3-5"
  ELSE                     "🔴 Au-delà"
END
```

---

### 2.3 Performance CTR

**Nom** : `Performance CTR`
**Type** : Texte
**Formule** :

```
CASE
  WHEN CTR >= 0.10 THEN "🟢 Excellent (≥10%)"
  WHEN CTR >= 0.05 THEN "🟡 Correct (5–10%)"
  WHEN CTR >= 0.02 THEN "🟠 Faible (2–5%)"
  ELSE                   "🔴 Critique (<2%)"
END
```

---

### 2.4 Potentiel Rapide

**Nom** : `Potentiel Rapide`
**Type** : Texte
**Formule** :

```
CASE
  WHEN Position >= 4  AND Position <= 10 AND Impressions >= 200
    THEN "🎯 Quick Win (p4-10)"
  WHEN Position >= 11 AND Position <= 20 AND Impressions >= 500
    THEN "🔍 À travailler (p11-20)"
  WHEN Position >= 4  AND Position <= 10
    THEN "📈 Surveiller"
  ELSE "—"
END
```

---

### 2.5 Type Requête LLM

**Nom** : `Type Requête LLM`
**Type** : Texte
**Formule** :

```
CASE
  WHEN REGEXP_CONTAINS(Query, "(?i)^(comment|pourquoi|quand|qu.est|quelle?|quel|combien|est-ce).{15,}")
    THEN "🧠 Requête info longue (LLM)"
  WHEN LENGTH(Query) >= 35
    THEN "🧠 Longue traîne"
  WHEN LENGTH(Query) >= 20
    THEN "📍 Traîne moyenne"
  ELSE "⚡ Générique"
END
```

---

### 2.6 Page (normalisée — pour jointure GA4)

**Nom** : `Page Path`
**Type** : Texte
**Formule** :

```
REGEXP_REPLACE(Page, "https://schoolswp\\.com", "")
```

---

## 3. Page 1 — Vue Executive

### Objectif
Vision macro immédiate. Réponse en 10 secondes à : "Comment va schoolsWP cette semaine ?"

### Configuration de la plage de dates
- Contrôle de dates : **30 derniers jours** (défaut)
- Ajouter un 2e contrôle : **Comparaison période précédente** (MoM)

### Layout (ordre des widgets)

#### Ligne 1 — Scorecards (4 cartes KPI)

| Widget | Métrique | Options |
|--------|----------|---------|
| Scorecard 1 | `Clicks` | Comparaison période précédente → afficher % variation |
| Scorecard 2 | `Impressions` | Comparaison période précédente |
| Scorecard 3 | `CTR` | Format % · Comparaison |
| Scorecard 4 | `Position` | Tri croissant · Comparaison |

> Config scorecards : Données → Agrégation = SUM pour Clicks/Impressions, AVG pour CTR/Position.
> Activer "Afficher la comparaison" + "Afficher les flèches".

#### Ligne 2 — Série temporelle

- **Type** : Graphique en courbes (Time Series)
- **Dimension** : `Date`
- **Métriques** : `Clicks` + `Impressions` (axe secondaire)
- **Période** : 90 jours
- **Options** : Lisser les courbes activé

#### Ligne 3 — Top 10 Pages | Top 10 Requêtes (côte à côte)

**Table Top 10 Pages** :
- Dimension : `Page`
- Métriques : `Clicks`, `Impressions`, `CTR`, `Position`, `Cluster`
- Tri : Clicks DESC
- Lignes : 10
- Pagination : désactivée

**Table Top 10 Requêtes** :
- Dimension : `Query`
- Métriques : `Clicks`, `Impressions`, `CTR`, `Position`
- Tri : Clicks DESC
- Lignes : 10

#### Ligne 4 — KPI Stratégiques (3 cartes)

| Widget | Filtre | Description |
|--------|--------|-------------|
| Scorecard "Articles Top 3" | Position <= 3 | Nombre de pages en position ≤ 3 |
| Scorecard "Pages Pos 4-10" | Position entre 4 et 10 | Pages page 1 hors podium |
| Scorecard "Opportunités (p5-15 + >500 imp)" | Potentiel Rapide = "🎯 Quick Win" | Pages à fort potentiel |

> Pour ces scorecards : utiliser Filtre de graphique (segment de données).

---

## 4. Page 2 — Performance SEO Détaillée

### Objectif
Drill-down sur chaque page/requête. Identifier les patterns de performance.

### Contrôles (barre de filtres en haut)

1. **Contrôle de dates** — plage personnalisée
2. **Menu déroulant : Cluster** — dimension `Cluster` (tous les clusters)
3. **Menu déroulant : Catégorie Position** — dimension `Catégorie Position`
4. **Saisie de texte : Filtre URL** — dimension `Page`, filtre contient

### Tableau principal (grande table)

Dimensions :
- `Page`
- `Query`
- `Cluster`
- `Catégorie Position`
- `Performance CTR`
- `Potentiel Rapide`

Métriques :
- `Clicks`
- `Impressions`
- `CTR` (format %)
- `Position` (format décimal 1 chiffre)

Options :
- Tri par défaut : `Position` ASC
- Lignes par page : 25
- Mise en forme conditionnelle Position :
  - ≤ 3 → fond vert clair
  - 4-10 → fond jaune clair
  - > 10 → fond rouge clair

### Graphique complémentaire

**Bubble chart (Impressions vs CTR, taille = Clicks)** :
- Axe X : `Impressions`
- Axe Y : `CTR`
- Taille bulle : `Clicks`
- Dimension couleur : `Cluster`
- Objectif : identifier les pages à fort volume mais CTR faible

### Filtres URL recommandés (créer via Segment de données)

Ajouter des raccourcis filtre dans la description ou sous forme de liens :
```
Page contient : /crm/          → Cluster CRM
Page contient : /lms/          → Cluster LMS
Page contient : /woocommerce/  → Cluster WooCommerce
Page contient : /comparatif/   → Comparatifs
Page contient : /performance/  → Performance
Page contient : /automatisation/ → Automatisation
```

---

## 5. Page 3 — Analyse Cluster (Topical Authority)

### Objectif
Comprendre quelle thématique domine, laquelle stagne. Décisions de production éditoriale.

### Section A — Vue macro clusters

**Bar chart — Clics par Cluster** :
- Dimension : `Cluster`
- Métrique : `Clicks`
- Tri : DESC
- Couleur : une couleur par cluster (palette schoolsWP)

**Bar chart — Impressions par Cluster** :
- Même configuration, métrique : `Impressions`

### Section B — Tableau Cluster

| Dimension | Métriques |
|-----------|-----------|
| `Cluster` | `Clicks` · `Impressions` · `CTR` · `Position` · Nombre de pages* |

> *Nombre de pages : créer champ calculé `COUNT_DISTINCT(Page)` ou utiliser métrique Record Count.

Options :
- Ajouter mini graphique en barres sur la colonne Clicks (sparkline)
- Tri : Clicks DESC

### Section C — Croissance MoM par Cluster

**Table avec comparaison de période** :
- Dimension : `Cluster`
- Métrique : `Clicks` avec comparaison M-1
- Afficher : variation absolue + variation %
- Mise en forme conditionnelle : vert si croissance > 0, rouge si < 0

### Section D — Scatter plot Autorité vs Performance

**Graphique dispersion** :
- Axe X : `Impressions` (volume de visibilité)
- Axe Y : `Clicks` (performance réelle)
- Dimension : `Cluster`
- Objectif : identifier clusters à forte visibilité / faible clic (problème CTR) vs clusters équilibrés

### Section E — Tableau Pages par Cluster

**Table drill-down** :
- Dimensions : `Page` + `Cluster`
- Métriques : `Clicks`, `Impressions`, `CTR`, `Position`, `Potentiel Rapide`
- Filtre interactif : cliquer sur un cluster dans le bar chart filtre cette table automatiquement
- Activer : **Interactions du graphique → Filtre croisé** sur le bar chart

---

## 6. Page 4 — Optimisation Stratégique

### Objectif
Décisions actionnables cette semaine. Priorisation des efforts SEO + LLM + CRO.

### Section A — Quick Wins (position 4-15)

**Table Quick Wins** :

Filtre de données :
- `Position` >= 4 ET `Position` <= 15

Dimensions :
- `Page`
- `Cluster`
- `Query`
- `Position`
- `Performance CTR`
- `Potentiel Rapide`

Métriques :
- `Clicks`
- `Impressions`
- `CTR`

Tri : `Position` ASC puis `Impressions` DESC

Actions éditoriales associées (texte fixe dans rapport) :
```
Position 4-6 : optimiser le title tag + H1
Position 7-10 : améliorer l'intro + ajouter FAQ
Position 11-15 : retravailler l'angle + maillage interne
Toutes : ajouter bloc "Réponse rapide" (LLM-ready)
```

---

### Section B — Opportunités LLM / AI Visibility

**Table Requêtes Longues Informationnelles** :

Filtre de données :
- `Type Requête LLM` contient "LLM" OU `Type Requête LLM` = "🧠 Longue traîne"
- `Impressions` >= 100

Dimensions :
- `Query`
- `Page`
- `Type Requête LLM`
- `Position`

Métriques :
- `Clicks`
- `Impressions`
- `CTR`

Tri : `Impressions` DESC

> Ces requêtes sont celles pour lesquelles un bloc "Réponse rapide" structuré
> peut capter les AI Overviews de Google et les citations LLM (ChatGPT, Gemini, Perplexity).

---

### Section C — Pages sous-performantes (CTR faible sur page 1)

**Table CTR critique malgré bonne position** :

Filtre de données :
- `Position` <= 10
- `CTR` <= 0.03 (3%)
- `Impressions` >= 200

Dimensions :
- `Page`
- `Cluster`
- `Position`
- `Performance CTR`

Métriques :
- `Impressions`
- `Clicks`
- `CTR`

Tri : `Impressions` DESC

> Ces pages sont visibles mais pas cliquées : problème de title / meta description / date visible / snippet.

---

### Section D — Corrélation Business (si GA4 connecté)

> Nécessite jointure GSC + GA4 sur champ `Page Path` (cf. section 2.6).

**Table Trafic vs Engagement** :
- Dimension : `Page path` (commun aux deux sources)
- Métriques GSC : `Clicks`, `Position`
- Métriques GA4 : `Sessions`, `Engagement rate`, `Average engagement time`

**Scorecard "Pages fort trafic / faible engagement"** :
- Filtre : `Clicks` > 100 AND `Engagement rate` < 0.40

> Identifier les pages qui attirent mais ne convertissent pas :
> cibles prioritaires pour CTA, tunnel, lead magnet.

---

## 7. Configuration avancée

### 7.1 Palette de couleurs schoolsWP

Dans Style → Couleurs du rapport :
```
Primaire  : #00D400
Secondaire: #00A100
Accent    : #E668D4
Texte     : #1A1A2E
Fond      : #FFFFFF
Neutre    : #F5F5F5
```

### 7.2 Plages de dates recommandées par page

| Page | Plage par défaut | Comparaison |
|------|-----------------|-------------|
| Vue Executive | 28 derniers jours | 28j précédents |
| Performance SEO | 90 derniers jours | Aucune (drill-down) |
| Analyse Cluster | 90 derniers jours | M-1 |
| Optimisation | 28 derniers jours | Aucune (snapshot) |

### 7.3 Segments de données réutilisables

Créer dans Ressources → Gérer les segments :

**Segment "Pages Piliers"** :
```
Page REGEXP_MATCH ".*/(crm|lms|performance|automatisation|woocommerce|seo)-wordpress.*"
```

**Segment "Quick Wins"** :
```
Position >= 4 AND Position <= 15 AND Impressions >= 200
```

**Segment "Requêtes LLM"** :
```
LENGTH(Query) >= 25 OR Query REGEXP_MATCH "^(comment|pourquoi|quelle?).*"
```

### 7.4 Alertes par email (Looker Studio)

Looker Studio natif ne supporte pas les alertes. Alternatives :
- Utiliser le workflow `kpi-dashboard-updater.json` (Slack digest hebdomadaire)
- Google Sheets + formule FILTER + Apps Script `MailApp.sendEmail()`
- Data Studio Add-on : **Supermetrics Alerts**

---

## 8. Checklist de lancement

```
□ Source GSC "URL Impression" connectée (schoolswp.com)
□ 6 champs personnalisés créés (Cluster, Catégorie Position, Performance CTR,
  Potentiel Rapide, Type Requête LLM, Page Path)
□ Page 1 : 4 scorecards + courbe + 2 tables + 3 KPI stratégiques
□ Page 2 : 4 contrôles + grande table + bubble chart
□ Page 3 : 2 bar charts + table cluster + scatter + table drill-down (filtre croisé activé)
□ Page 4 : 4 sections (Quick Wins + LLM + CTR faible + [GA4])
□ Palette #00D400 / #00A100 / #E668D4 appliquée
□ Plages de dates configurées par page
□ Partage en lecture avec michael@schoolswp.com
□ Lien dans le README du projet
```

---

## 9. Rythme d'analyse recommandé

```
Hebdomadaire (15 min — Page 4 : Optimisation) :
  → Opportunités position 5–15
  → 2 articles à pousser cette semaine
  → 1 requête LLM à adresser

Mensuel (45 min — Page 3 : Clusters) :
  → Quel cluster progresse ?
  → Quel cluster stagne → décision production
  → Mise à jour AI Overview + Citation LLM dans le KPI Dashboard

Trimestriel (2h — Page 1 + 3) :
  → Tendance trafic 90j
  → Clusters déséquilibrés (volume sans clic, clic sans engagement)
  → Lancer Content Factory V3 sur articles Score Global < 70
  → Identifier 3 nouveaux satellites à produire par pilier faible
```

---

## 10. Intégration avec le KPI Dashboard

Ce Looker Studio est la **couche visualisation** du système. Les données GSC
qu'il affiche sont les mêmes que celles injectées automatiquement chaque lundi
par le workflow `kpi-dashboard-updater.json` dans Google Sheets.

Architecture complète :

```
GSC API  ──► n8n kpi-dashboard-updater  ──► Google Sheets DASHBOARD
                                                    │
                                         ┌──────────┴──────────┐
                                         │                     │
                              Looker Studio                Slack Digest
                           (visualisation temps réel)    (alerte hebdo)
```

> Looker Studio lit le Google Sheet DASHBOARD en temps réel via le connecteur
> Google Sheets — ajouter l'onglet DASHBOARD comme 3e source de données pour
> superposer les scores internes (Score SEO / Conversion / Autorité / Score Global)
> aux données GSC brutes.

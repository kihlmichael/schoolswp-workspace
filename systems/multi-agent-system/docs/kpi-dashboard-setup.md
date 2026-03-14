# 📊 schoolsWP — KPI Dashboard Setup

## Architecture

```
Content Machine V2  ──► IDEAS sheet     (production pipeline)
KPI Dashboard       ──► DASHBOARD sheet (mesure + GSC + Score Global)
Notion KPI Tracker  ──► Notion DB       (vue alternative / mobile)
```

---

## 1. Google Sheets — Onglet DASHBOARD

Créer un onglet `DASHBOARD` dans le même fichier Google Sheets que IDEAS.

### Colonnes (ordre exact, ligne 1 = headers)

| Col | Nom | Rempli par | Notes |
|-----|-----|-----------|-------|
| A | Sujet | Manuel / V2 | Titre éditorial |
| B | Mot-clé | Manuel / V2 | Mot-clé principal |
| C | URL publiée | **Manuel** | URL WordPress complète (requis pour GSC) |
| D | Type | Manuel | Pilier / Satellite / Hub |
| E | Pilier | Manuel | SEO / LMS / CRM / Performance / Automatisation / Ecommerce |
| F | Score SEO | V2 → copier | Score interne V2 /100 |
| G | Score Conversion | V2 → copier | Score interne V2 /100 |
| H | Score Autorité | V2 → copier | Score interne V2 /100 |
| I | AI Overview | **Manuel** | `oui` / `non` (mettre à jour mensuellement) |
| J | Citation LLM | **Manuel** | `oui` / `non` (vérifier sur ChatGPT/Gemini) |
| K | LLM Score | Auto (workflow) | Calculé : (AI Overview + Citation) / 2 → 0-100 |
| L | Score Global | Auto (workflow) | = SEO×25% + LLM×15% + Conv×30% + Auth×30% |
| M | Action | Auto (workflow) | ✅ / 🟢 / 🟡 / 🔴 |
| N | [GSC] Position | Auto (workflow) | Position moyenne 28 jours |
| O | [GSC] CTR % | Auto (workflow) | CTR moyen 28 jours |
| P | [GSC] Impressions | Auto (workflow) | Impressions 28 jours |
| Q | [GSC] Clics | Auto (workflow) | Clics organiques 28 jours |
| R | Dernière MAJ | Auto (workflow) | Date dernier refresh GSC |
| S | Lien Google Doc | V2 → copier | Lien vers le doc V2 |
| T | Statut | Manuel | Brouillon / Publié / À réviser |

### Formule Score Global (alternative Google Sheets)

Si tu ne passes pas par le workflow n8n, utilise cette formule en colonne L :

```
=IFERROR(
  ROUND(
    (F2*0.25) + (K2*0.15) + (G2*0.30) + (H2*0.30),
    0
  ),
  0
)
```

### Formule Action (colonne M) — Google Sheets

```
=IF(L2="","",
  IF(L2>=95,"✅ Actif premium",
    IF(L2>=85,"🟢 Actif performant",
      IF(L2>=70,"🟡 Optimiser",
        "🔴 Révision stratégique"
      )
    )
  )
)
```

### Formule LLM Score (colonne K) — Google Sheets

```
=IFERROR(
  ROUND(
    (IF(I2="oui",100,IF(I2="non",0,50)) +
     IF(J2="oui",100,IF(J2="non",0,50))) / 2,
    0
  ),
  50
)
```

---

## 2. Onglet CLUSTERS (vue macro)

Créer un onglet `CLUSTERS` avec ces formules (ex: pilier SEO en ligne 2) :

| Col | Nom | Formule |
|-----|-----|---------|
| A | Pilier | `SEO` (valeur fixe) |
| B | Nb articles | `=COUNTIF(DASHBOARD!E:E,A2)` |
| C | Score Global moyen | `=IFERROR(AVERAGEIF(DASHBOARD!E:E,A2,DASHBOARD!L:L),0)` |
| D | Clics 28j | `=IFERROR(SUMIF(DASHBOARD!E:E,A2,DASHBOARD!Q:Q),0)` |
| E | Trafic moyen / article | `=IFERROR(D2/B2,0)` |
| F | Articles ≥ 85 | `=COUNTIFS(DASHBOARD!E:E,A2,DASHBOARD!L:L,">="&85)` |
| G | % actifs performants | `=IFERROR(F2/B2,0)` (format %) |

Lignes : SEO / LMS / CRM / Performance / Automatisation / Ecommerce

---

## 3. Workflow n8n — kpi-dashboard-updater.json

### Prérequis

1. **Google Sheets credential** : `Google Sheets` (OAuth2 — déjà configuré si V2 fonctionne)
2. **Google Search Console credential** : créer une credential `oAuth2Api` nommée `Google Search Console OAuth2`
   - Scopes : `https://www.googleapis.com/auth/webmasters.readonly`
   - Client ID/Secret : depuis Google Cloud Console (même projet que Sheets)
3. **Slack Webhook** : `VOTRE_SLACK_WEBHOOK_URL`

### Variables à remplacer dans le JSON

| Placeholder | Valeur |
|-------------|--------|
| `VOTRE_GOOGLE_SHEET_ID` | ID du Google Sheet (dans l'URL) |
| `VOTRE_SLACK_WEBHOOK_URL` | Webhook Slack entrant |
| `https://schoolswp.com/` | URL exacte du site dans GSC |

### Pipeline

```
Lundi 7h00
  → GSheets Read DASHBOARD (toutes les lignes avec URL publiée)
  → Code: Filter (URL vide = ignoré) + dates (J-28 → aujourd'hui)
  → Code: Build GSC query (endpoint + payload)
  → HTTP: POST GSC API → response {rows: [{keys, clicks, impressions, ctr, position}]}
  → Code: JOIN articles + GSC | compute Score Global | retourne N items
  → GSheets: appendOrUpdate DASHBOARD (match sur Mot-clé)
  → Code: Aggregate → top 5 + alertes + clusters (runOnceForAllItems)
  → HTTP: Slack weekly digest
```

### Score Global — formule appliquée dans n06

```
SEO_réel   = IF position GSC connue:
               ROUND((Score_SEO + CTR_bonus + Position_bonus) / 3)
             ELSE:
               Score_SEO
             (CTR_bonus = min(100, CTR/4 × 100))
             (Position_bonus = max(0, 110 - position × 5.5))

LLM_Score  = IF AI_Overview ET Citation LLM renseignés:
               ROUND((AI_score + Citation_score) / 2)
             ELSE: 50 (neutre par défaut)

Score_Global = ROUND(
  SEO_réel   × 0.25  +
  LLM_Score  × 0.15  +
  Score_Conv × 0.30  +
  Score_Auth × 0.30
)
```

### Interprétation Score Global

| Score | Label | Action |
|-------|-------|--------|
| ≥ 95 | ✅ Actif premium | Conserver, surveiller mensuel |
| 85–94 | 🟢 Actif performant | Surveiller CTR, envisager update |
| 70–84 | 🟡 Optimiser | CTA, structure, maillage |
| < 70 | 🔴 Révision stratégique | Réécriture ou dépublication |

---

## 4. Looker Studio — Connexion

1. **Source** : connecter le Google Sheet (onglet DASHBOARD) comme source de données
2. **Métriques clés** :
   - Score Global (indicateur jauge 0-100)
   - [GSC] Clics (timeseries)
   - Score SEO / Score Conversion / Score Autorité (barres)
3. **Dimensions** : Pilier, Type, Action, Mot-clé
4. **Filtres suggérés** :
   - Pilier = SEO / LMS / CRM...
   - Score Global < 70 (vue alertes)
   - Type = Pilier (vue piliers uniquement)
5. **Mise à jour** : Looker Studio reflète les données Sheets en temps réel

---

## 5. Connecter GSC + GA4 (optionnel)

### GSC natif dans Looker Studio
- Ajouter une 2ème source : `Google Search Console` (connecteur natif)
- Joindre sur le champ `Page` (URL) avec la colonne `URL publiée` du DASHBOARD

### GA4 pour Scroll Depth + Temps page
- Dans GA4 : configurer `scroll_depth` en événement personnalisé (≥ 60%)
- Via Google Analytics connector Looker Studio ou exporter via BigQuery

---

## 6. Workflow KPI (récap hebdo)

```
Lundi matin (auto) :
  ✅ KPI Dashboard mis à jour (GSC + Score Global)
  ✅ Slack digest : top 5 / alertes / par pilier

Manuellement (mensuel) :
  → Remplir AI Overview + Citation LLM dans DASHBOARD
  → LLM Score se recalcule au prochain refresh

Trimestriel :
  → Comparer positions GSC (tendance)
  → Identifier clusters incomplets (onglet CLUSTERS)
  → Lancer Content Factory V3 sur articles < 70
```

# schoolsWP Growth OS — V5 GSC Update & CTR Brain

Première version qui raisonne comme un vrai système éditorial piloté par les données.
Mélange 3 sources de vérité : veille externe (RSS) + existant éditorial + données GSC réelles.

---

## Les 4 questions centrales

À chaque sujet entrant, la machine répond à :

1. Ce sujet mérite-t-il une action ?
2. A-t-on déjà une page proche sur schoolsWP ?
3. Cette page sous-performe-t-elle dans GSC ?
4. La meilleure action est-elle : nouveau contenu, update, ou optimisation CTR ?

---

## Vue d'ensemble

```text
A. Flux veille externe
RSS Feed Trigger
→ Normalize Item
→ Fetch Article
→ Clean Content
→ Scoring AI
→ Parse Score JSON

B. Flux données SEO internes
→ Existing Content Lookup
→ GSC Page Lookup
→ GSC Query Lookup
→ Content Performance Formatter

C. Cerveau stratégique
→ Strategic Growth Decision AI
→ Parse Strategy JSON
→ Content + SEO + CTR Generator AI
→ Parse Output JSON
→ Strategic Scoring
→ Action Router

D. Sorties
├─ Social Queue
├─ New Article Queue
├─ Update Existing Queue
├─ CTR Optimization Queue
├─ Pillar Resource Queue
├─ Monetization Queue
└─ X Auto Publish
```

---

## 6 actions possibles

| Action            | Condition                                        |
| ----------------- | ------------------------------------------------ |
| `social_only`     | Sujet utile, pas assez fort pour toucher au site |
| `new_article`     | Sujet neuf, pas de vraie page existante          |
| `update_existing` | Le sujet enrichit mieux une page déjà publiée    |
| `optimize_ctr`    | Page existante avec impressions mais CTR faible  |
| `pillar_resource` | Sujet qui mérite une ressource plus structurée   |
| `archive`         | Pas d'action                                     |

---

## 7 Google Sheets recommandées

### 1) `content_master`

Base centrale de tout ce que le workflow produit.

```text
id | date_detected | source_name | source_title | source_url | source_date
source_author | source_excerpt | article_clean_text | suggested_category
suggested_topic | relevance_score | linkedin_score | x_score | novelty_score
actionability_score | global_score | decision | reason | strategic_action
action_reason | best_existing_url | best_existing_title | cannibalization_risk
seo_potential | ai_citation_potential | business_potential | editorial_priority
content_type_recommended | search_intent | seo_keyword | seo_angle | seo_title
seo_meta_description | h2_outline | ctr_rewrite_title | ctr_rewrite_meta
ctr_opportunity_level | monetization_angle | recommended_offer_type
recommended_status | x_auto_publish | linkedin_review_required
published_x | published_linkedin | status | notes
```

### 2) `site_content_index`

Index maison des contenus schoolsWP.

```text
url | title | content_type | target_keyword | primary_topic | angle
last_updated | content_status | notes
```

### 3) `gsc_pages`

Vue page-level (export GSC).

```text
page | clicks | impressions | ctr | position | period_start | period_end
needs_ctr_work | needs_update | notes
```

### 4) `gsc_queries`

Vue query-level (export GSC).

```text
query | page | clicks | impressions | ctr | position | period_start | period_end
query_intent | notes
```

### 5) `queue_updates`

Contenus existants à enrichir.

```text
id | date_added | best_existing_url | best_existing_title | source_title | source_url
action_reason | seo_keyword | seo_title | seo_meta_description | h2_outline
priority | status | note
```

### 6) `queue_ctr_optimizations`

File CTR — critique.

```text
id | date_added | page_url | page_title | current_ctr | current_position
main_query | current_title | current_meta | suggested_title | suggested_meta
ctr_opportunity_level | reason | priority | status | note
```

### 7) `queue_new_articles`

Nouveaux contenus.

```text
id | date_added | source_title | source_url | blog_draft_idea | seo_keyword
seo_angle | seo_title | seo_meta_description | h2_outline | search_intent
priority | status | note
```

---

## Règles de détection des opportunités CTR

| Niveau  | Critères                                                    |
| ------- | ----------------------------------------------------------- |
| Forte   | impressions ≥ 300, position ≤ 12, CTR < 2.5%                |
| Moyenne | impressions ≥ 100, position ≤ 15, CTR < 3%                  |
| Faible  | peu d'impressions, position trop basse, ou CTR déjà correct |

---

## Prompt — Strategic Growth Decision AI

```text
Tu es un stratège de croissance éditoriale pour schoolsWP.

Ta mission : analyser une source de veille et décider de la meilleure action de croissance éditoriale en croisant :
- la valeur du sujet
- l'existant éditorial
- les performances SEO réelles issues de Google Search Console

Contexte schoolsWP :
- univers : WordPress, SEO, automatisation, performance, business de créateurs, plugins, e-learning, monétisation
- ton : direct, utile, concret, pédagogique
- objectif : renforcer l'autorité, améliorer le SEO, éviter les doublons, détecter les opportunités de CTR, produire des ressources utiles et citables par les IA

Tu dois choisir UNE seule action principale parmi :
- social_only
- new_article
- update_existing
- optimize_ctr
- pillar_resource
- archive

Tu dois aussi évaluer :
- le risque de cannibalisation
- le potentiel SEO
- le potentiel citations IA
- le potentiel business
- la priorité réelle
- l'opportunité CTR

Retourne UNIQUEMENT un JSON valide :

{
  "strategic_action": "",
  "action_reason": "",
  "best_existing_url": "",
  "best_existing_title": "",
  "cannibalization_risk": "",
  "seo_potential": "",
  "ai_citation_potential": "",
  "business_potential": "",
  "editorial_priority": "",
  "content_type_recommended": "",
  "search_intent": "",
  "ctr_opportunity_level": "",
  "update_recommended": "",
  "new_article_recommended": "",
  "ctr_optimization_recommended": "",
  "pillar_recommended": ""
}

Règles :
- strategic_action = social_only / new_article / update_existing / optimize_ctr / pillar_resource / archive
- cannibalization_risk = low / medium / high
- seo_potential = low / medium / high
- ai_citation_potential = low / medium / high
- business_potential = low / medium / high
- editorial_priority = low / medium / high
- content_type_recommended = guide / tutorial / comparison / opinion / resource / roundup / social_post
- search_intent = informational / commercial / navigational / mixed
- ctr_opportunity_level = low / medium / high
- update_recommended = yes / no
- new_article_recommended = yes / no
- ctr_optimization_recommended = yes / no
- pillar_recommended = yes / no

Données source :
Titre : {{ $json.source_title }}
URL : {{ $json.source_url }}
Extrait : {{ $json.source_excerpt }}
Topic : {{ $json.suggested_topic }}
Contenu : {{ $json.article_clean_text }}

Mémoire éditoriale :
{{ $json.editorial_memory || "aucune" }}

Contenus existants proches :
{{ $json.existing_content_context || "aucun contenu proche trouvé" }}

Données GSC page :
{{ $json.gsc_page_context || "aucune donnée GSC page" }}

Données GSC requêtes :
{{ $json.gsc_query_context || "aucune donnée GSC requête" }}
```

---

## Prompt — Content + SEO + CTR Generator AI

```text
Tu es le moteur éditorial SEO et CTR de schoolsWP.

Ta mission : générer des sorties exploitables selon la décision stratégique déjà prise.

Tu dois produire :
1. un post LinkedIn
2. un contenu X
3. un snippet newsletter
4. une idée d'article ou de mise à jour
5. un mot-clé SEO cible
6. un angle SEO
7. un title SEO
8. une meta description
9. un mini plan H2
10. une proposition de title orientée CTR
11. une proposition de meta orientée CTR
12. un angle de monétisation
13. un type d'offre recommandé
14. un statut recommandé

Retourne UNIQUEMENT un JSON valide :

{
  "linkedin_post": "",
  "x_thread": ["", "", "", ""],
  "newsletter_snippet": "",
  "blog_draft_idea": "",
  "seo_keyword": "",
  "seo_angle": "",
  "seo_title": "",
  "seo_meta_description": "",
  "h2_outline": ["", "", "", ""],
  "ctr_rewrite_title": "",
  "ctr_rewrite_meta": "",
  "monetization_angle": "",
  "recommended_offer_type": "",
  "recommended_status": "",
  "hashtags": ["", "", ""]
}

Règles :
- linkedin_post : utile, crédible, concret
- x_thread : 1 à 4 blocs max
- seo_title : clair, naturel, non putaclic
- seo_meta_description : utile, lisible, honnête
- ctr_rewrite_title : plus cliquable sans tomber dans le piège du putaclic
- ctr_rewrite_meta : orientée clic honnête, bénéfice clair
- recommended_offer_type = affiliate / course / guide / newsletter / consulting / no_offer
- recommended_status = approved / review / archive

Contexte :
Décision stratégique : {{ $json.strategic_action }}
Raison : {{ $json.action_reason }}
Type recommandé : {{ $json.content_type_recommended }}
Intention : {{ $json.search_intent }}
Potentiel SEO : {{ $json.seo_potential }}
Potentiel citations IA : {{ $json.ai_citation_potential }}
Opportunité CTR : {{ $json.ctr_opportunity_level }}
Titre source : {{ $json.source_title }}
Contenu : {{ $json.article_clean_text }}
```

---

## Code node — Format GSC Page Context

```javascript
const rows = $input.all().map((i) => i.json);

const pageContext = rows
  .slice(0, 5)
  .map((row, index) => {
    return `${index + 1}. URL: ${row.page || ""} | Clicks: ${row.clicks || ""} | Impressions: ${row.impressions || ""} | CTR: ${row.ctr || ""} | Position: ${row.position || ""}`;
  })
  .join("\n");

return [{ json: { gsc_page_context: pageContext || "aucune donnée page" } }];
```

## Code node — Format GSC Query Context

```javascript
const rows = $input.all().map((i) => i.json);

const queryContext = rows
  .slice(0, 8)
  .map((row, index) => {
    return `${index + 1}. Query: ${row.query || ""} | Page: ${row.page || ""} | Clicks: ${row.clicks || ""} | Impressions: ${row.impressions || ""} | CTR: ${row.ctr || ""} | Position: ${row.position || ""}`;
  })
  .join("\n");

return [
  { json: { gsc_query_context: queryContext || "aucune donnée requête" } },
];
```

---

## Code node — Strategic Growth Scoring

```javascript
const prev = $input.first().json;

const globalScore = Number(prev.global_score || 0);
const xScore = Number(prev.x_score || 0);

const seoPotential = (prev.seo_potential || "").toLowerCase();
const aiCitationPotential = (prev.ai_citation_potential || "").toLowerCase();
const businessPotential = (prev.business_potential || "").toLowerCase();
const editorialPriority = (prev.editorial_priority || "").toLowerCase();
const ctrOpportunity = (prev.ctr_opportunity_level || "").toLowerCase();
const cannibalizationRisk = (prev.cannibalization_risk || "").toLowerCase();

let seoScore = 0;
if (seoPotential === "high") seoScore += 5;
if (seoPotential === "medium") seoScore += 3;

let authorityScore = 0;
if (aiCitationPotential === "high") authorityScore += 4;
if (aiCitationPotential === "medium") authorityScore += 2;

let businessScore = 0;
if (businessPotential === "high") businessScore += 5;
if (businessPotential === "medium") businessScore += 3;

let priorityScore = 0;
if (editorialPriority === "high") priorityScore += 4;
if (editorialPriority === "medium") priorityScore += 2;

let ctrScore = 0;
if (ctrOpportunity === "high") ctrScore += 5;
if (ctrOpportunity === "medium") ctrScore += 3;

let cannibalizationPenalty = 0;
if (cannibalizationRisk === "high") cannibalizationPenalty = 4;
if (cannibalizationRisk === "medium") cannibalizationPenalty = 2;

const xAutoPublish =
  globalScore >= 8 &&
  xScore >= 8 &&
  cannibalizationRisk === "low" &&
  prev.recommended_status === "approved" &&
  prev.strategic_action === "social_only";

return [
  {
    json: {
      ...prev,
      seo_score: seoScore,
      authority_score: authorityScore,
      business_score: businessScore,
      priority_score: priorityScore,
      ctr_score: ctrScore,
      cannibalization_penalty: cannibalizationPenalty,
      x_auto_publish: xAutoPublish ? "yes" : "no",
      linkedin_review_required: "yes",
      published_x: "no",
      published_linkedin: "no",
      status: prev.recommended_status || "review",
    },
  },
];
```

---

## Routeur d'action V5

| Branche           | Condition                                            |
| ----------------- | ---------------------------------------------------- |
| `optimize_ctr`    | `{{ $json.strategic_action === "optimize_ctr" }}`    |
| `new_article`     | `{{ $json.strategic_action === "new_article" }}`     |
| `update_existing` | `{{ $json.strategic_action === "update_existing" }}` |
| `pillar_resource` | `{{ $json.strategic_action === "pillar_resource" }}` |
| `social_only`     | `{{ $json.strategic_action === "social_only" }}`     |

---

## Queue CTR Optimization — mapping Sheets

| Colonne Sheets          | Valeur                              |
| ----------------------- | ----------------------------------- | --- | ------ |
| `id`                    | `{{ $json.id }}`                    |
| `date_added`            | `{{ $json.date_detected }}`         |
| `page_url`              | `{{ $json.best_existing_url }}`     |
| `page_title`            | `{{ $json.best_existing_title }}`   |
| `current_ctr`           | `{{ $json.current_ctr               |     | "" }}` |
| `current_position`      | `{{ $json.current_position          |     | "" }}` |
| `main_query`            | `{{ $json.seo_keyword               |     | "" }}` |
| `current_title`         | `{{ $json.current_title             |     | "" }}` |
| `current_meta`          | `{{ $json.current_meta              |     | "" }}` |
| `suggested_title`       | `{{ $json.ctr_rewrite_title }}`     |
| `suggested_meta`        | `{{ $json.ctr_rewrite_meta }}`      |
| `ctr_opportunity_level` | `{{ $json.ctr_opportunity_level }}` |
| `reason`                | `{{ $json.action_reason }}`         |
| `priority`              | `{{ $json.editorial_priority }}`    |
| `status`                | `pending`                           |

---

## Ordre final des nodes V5

```text
1.  RSS Feed Trigger
2.  Normalize Item
3.  Fetch Article
4.  Clean Content
5.  Scoring AI
6.  Parse Score JSON
7.  If Decision = generate?
    false →
        8.  If Decision = review?
            true  → 9.  Review Sheet
            false → 10. Archive Sheet
    true →
        11. Exact Dedup Check
        12. If Exact Duplicate?
            true  → 10. Archive Sheet
            false →
                13. Existing Content Lookup
                14. Format Existing Content Context
                15. Editorial Memory Lookup
                16. Format Editorial Memory
                17. GSC Page Lookup
                18. Format GSC Page Context
                19. GSC Query Lookup
                20. Format GSC Query Context
                21. Strategic Growth Decision AI
                22. Parse Strategy JSON
                23. Content + SEO + CTR Generator AI
                24. Parse Output JSON
                25. Strategic Growth Scoring
                26. Store Master Sheet
                27. If X Auto Publish?
                    true  → 28. X Post → 29. Update Publication Log
                    false → 30. X Review Queue
                31. LinkedIn Review Queue
                32. If strategic_action = new_article    → 33. New Article Queue
                34. If strategic_action = update_existing → 35. Update Existing Queue
                36. If strategic_action = optimize_ctr   → 37. CTR Optimization Queue
                38. If strategic_action = pillar_resource → 39. Pillar Resource Queue
                40. If Monetization Queue?               → 41. Monetization Queue
```

---

## Ordre de déploiement recommandé

| Étape   | Ce qu'on fait                                      |
| ------- | -------------------------------------------------- |
| Étape 1 | V2 stable + V3 mémoire éditoriale, sans GSC        |
| Étape 2 | Export GSC régulier vers Google Sheets             |
| Étape 3 | Logique `optimize_ctr` + `queue_ctr_optimizations` |

La brique CTR est la plus rentable à court terme — gains immédiats sans nouveau contenu.

---

## Modules spécialisés recommandés (après V5)

### Module A — CTR Recovery Engine

Détecte les pages avec beaucoup d'impressions, position correcte, CTR trop faible.
Génère : 10 titles + 5 metas + 1 angle de repositionnement.

→ Implémenté en tant que workflows séparés : `schoolsWP CTR Hunter` + `schoolsWP CTR Judge`

### Module B — Content Update Engine

Prend un article existant et génère :

- sections à ajouter
- H2 à injecter
- FAQ à créer
- définitions plus "citations IA"
- éléments à retirer
- meilleure promesse SEO

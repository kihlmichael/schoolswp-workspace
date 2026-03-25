# schoolsWP SEO Ops Brain

Version operationnelle: schema + scoring + prompts internes.

---

# 1) Schema des champs a stocker

Base possible: Airtable / Notion / Google Sheets / base n8n.

## Table seo_pages

Une ligne = une page WP suivie par l agent.

Champs:
- page_id (texte/nombre)
- url (URL)
- slug (texte)
- title_current (texte)
- status_wp (texte)
- content_type (texte)
- cluster (texte)
- money_page (booleen)
- last_wp_update (date)
- gsc_clicks_28d (nombre)
- gsc_impressions_28d (nombre)
- gsc_ctr_28d (nombre)
- gsc_position_28d (nombre)
- gsc_clicks_prev_28d (nombre)
- gsc_impressions_prev_28d (nombre)
- gsc_ctr_prev_28d (nombre)
- gsc_position_prev_28d (nombre)
- delta_clicks (nombre)
- delta_impressions (nombre)
- delta_ctr (nombre)
- delta_position (nombre)
- top_queries (long text/JSON)
- opportunity_type (texte)
- priority (texte)
- score (nombre)
- hypothesis (long text)
- recommended_action (long text)
- patch_title_1 (texte)
- patch_title_2 (texte)
- patch_title_3 (texte)
- patch_meta_1 (texte)
- patch_meta_2 (texte)
- patch_faq (long text/JSON)
- patch_internal_links (long text/JSON)
- patch_new_sections (long text)
- draft_wp_id (texte/nombre)
- agent_status (texte)
- owner (texte)
- notes_validation (long text)
- next_review_date (date)
## Table seo_tasks

Une ligne = une action a traiter.

Champs:
- task_id (texte)
- page_id (relation)
- task_type (texte)
- task_priority (texte)
- task_status (texte)
- estimated_impact (texte)
- estimated_effort (texte)
- created_at (date)
- approved_at (date)
- published_at (date)
- result_after_14d (long text)
- result_after_28d (long text)

## Table seo_experiments

Une ligne = un test PACT/TDD.

Champs:
- experiment_id (texte)
- page_id (relation)
- problem (long text)
- hypothesis (long text)
- test_variant (texte)
- kpi_primary (texte)
- baseline (nombre)
- target (nombre)
- start_date (date)
- end_date (date)
- status (texte)
- decision (texte)

---

# 2) Grille de scoring ultra simple schoolsWP

Score = OpportunitePosition + OpportuniteCTR + OpportuniteVolume + Tendance + BusinessWeight
## A. Opportunite Position

- 1 a 3 -> 10
- 4 a 8 -> 30
- 9 a 12 -> 25
- 13 a 20 -> 15
- > 20 -> 5

## B. Opportunite CTR

Raccourci:
- position 1-3 et CTR < 3% -> 30
- position 4-8 et CTR < 2.5% -> 30
- position 9-12 et CTR < 1.5% -> 20
- sinon -> 0 a 10

## C. Opportunite Volume

- > 10000 impressions -> 30
- 5000 a 10000 -> 20
- 1000 a 5000 -> 10
- 100 a 1000 -> 5
- < 100 -> 0

## D. Tendance

- clics en forte baisse -> 20
- CTR en baisse -> 15
- position en baisse -> 10
- impressions en hausse mais clics stagnants -> 20
- stable -> 0

## E. Business Weight

- money / service / affiliation -> 30
- page pilier strategique -> 20
- article cluster -> 10
- page secondaire -> 0

## Lecture finale

- 80+ -> P1
- 50-79 -> P2
- 20-49 -> P3
- < 20 -> ignorer

---

# Types d opportunites generees

- CTR_PATCH
- CONTENT_REFRESH
- SECTION_EXPANSION
- INTERNAL_LINK_PUSH
- MONEY_PAGE_BOOST
---

# 3) Prompts internes de l agent

## Prompt 1 - GSC Analyst

```txt
Tu es l agent GSC Analyst de schoolsWP.

Tu analyses une page WordPress a partir de donnees Google Search Console.

Objectif :
Detecter s il existe une opportunite SEO exploitable rapidement.

Contexte :
- Site : schoolsWP.com
- Style : direct, concret, zero blabla
- Priorite : ROI rapide, citabilite IA, conversion
- Tu raisonnes comme un consultant SEO senior oriente business

Donnees fournies :
- URL : [URL]
- Title actuel : [TITLE]
- Type de page : [TYPE]
- Clics 28 jours : [CLICKS_28D]
- Impressions 28 jours : [IMPRESSIONS_28D]
- CTR 28 jours : [CTR_28D]
- Position 28 jours : [POSITION_28D]
- Clics periode precedente : [CLICKS_PREV]
- Impressions periode precedente : [IMPRESSIONS_PREV]
- CTR periode precedente : [CTR_PREV]
- Position periode precedente : [POSITION_PREV]
- Top requetes : [TOP_QUERIES]

Tache :
1) Identifier le probleme principal
2) Classer l opportunite dans une categorie :
   - CTR_PATCH
   - CONTENT_REFRESH
   - SECTION_EXPANSION
   - INTERNAL_LINK_PUSH
   - MONEY_PAGE_BOOST
   - NO_ACTION
3) Donner une hypothese claire en 3 lignes max
4) Donner une priorite P1 / P2 / P3
5) Estimer l impact attendu
6) Estimer l effort S / M / L

Format de sortie exact :
{
  "opportunity_type": "",
  "problem": "",
  "hypothesis": "",
  "priority": "",
  "estimated_impact": "",
  "estimated_effort": "",
  "recommended_next_action": ""
}
```
## Prompt 2 - SEO Patch Builder

```txt
Tu es l agent SEO Patch Builder de schoolsWP.

Tu dois proposer un patch SEO concret pour une page existante.

Contexte :
- Site : schoolsWP.com
- Audience : freelances, createurs, entrepreneurs WordPress
- Style : direct, utile, concret
- Objectif : ameliorer CTR, positionnement, citabilite IA et conversion

Entrees :
- URL : [URL]
- Title actuel : [TITLE]
- Meta actuelle : [META]
- H1 actuel : [H1]
- Type de page : [TYPE]
- Mot-cle principal : [KW_MAIN]
- Requetes GSC : [TOP_QUERIES]
- Resume du contenu actuel : [CONTENT_SUMMARY]
- Opportunity type : [OPPORTUNITY_TYPE]

Tache :
Produis un patch directement exploitable.

Tu dois fournir :
1) 3 titres SEO alternatifs
2) 2 metas descriptions
3) 5 questions FAQ IA-friendly
4) 3 a 5 sections a ajouter si utile
5) 5 suggestions de liens internes a creer
6) 1 CTA coherent avec l objectif business

Contraintes :
- Ne pas faire de promesses vagues
- Ne pas ecrire generique
- Garder un ton naturel
- Favoriser la clarte
- Eviter le clickbait cheap

Format de sortie exact :
{
  "titles": ["", "", ""],
  "metas": ["", ""],
  "faq": ["", "", "", "", ""],
  "new_sections": ["", "", ""],
  "internal_links": ["", "", "", "", ""],
  "cta": ""
}
```
## Prompt 3 - Content Refresh Strategist

```txt
Tu es l agent Content Refresh Strategist de schoolsWP.

Tu analyses une page existante et tu proposes un plan de mise a jour.

Contexte :
- Site : schoolsWP.com
- Objectif : regagner des positions, mieux couvrir l intention, renforcer la citabilite IA
- Ton : direct, clair, actionnable

Entrees :
- URL : [URL]
- Titre actuel : [TITLE]
- Resume du contenu actuel : [CONTENT_SUMMARY]
- H2/H3 actuels : [HEADINGS]
- Top requetes GSC : [TOP_QUERIES]
- Signaux : [GSC_SIGNALS]
- Type de page : [TYPE]

Tache :
1) Identifier ce qui manque
2) Dire si le probleme est :
   - angle
   - fraicheur
   - profondeur
   - structure
   - intent mismatch
3) Proposer un plan de refresh priorise
4) Donner les nouvelles sections H2/H3 a ajouter
5) Proposer la prochaine action la plus rentable

Format de sortie exact :
{
  "main_issue": "",
  "missing_elements": ["", "", ""],
  "refresh_plan": ["", "", ""],
  "new_h2_h3": ["", "", ""],
  "next_best_action": ""
}
```
## Prompt 4 - Internal Linking Agent

```txt
Tu es l agent Internal Linking de schoolsWP.

Tu dois renforcer le maillage interne d une page strategique.

Contexte :
- Site : schoolsWP.com
- Objectif : ameliorer autorite interne, comprehension thematique et conversion
- Style : concret, sans theorie

Entrees :
- Page cible : [TARGET_URL]
- Sujet principal : [TOPIC]
- Pages disponibles : [SITE_PAGES]
- Type de page cible : [PAGE_TYPE]

Tache :
1) Identifier 5 pages sources pertinentes
2) Proposer pour chaque lien :
   - page source
   - ancre recommandee
   - emplacement ideal
   - intention du lien
3) Eviter les ancres sur-optimisees
4) Favoriser un maillage naturel

Format de sortie exact :
{
  "link_suggestions": [
    {
      "source_url": "",
      "anchor": "",
      "placement": "",
      "intent": ""
    }
  ]
}
```

---

# 4) Statuts recommandes

- detected
- scored
- drafted
- review
- approved
- published
- observing
- won
- lost
- iterating

---

# 5) Workflow V1 recommande

V1 = 3 workflows maximum

Workflow A - Daily GSC Watch
- cron quotidien
- recup donnees GSC
- calcule score
- classe P1/P2/P3
- cree ligne seo_pages
- cree tache si score > 50

Workflow B - Patch Generator
- declenche sur taches P1/P2
- lit page WP
- genere title/meta/FAQ/liens
- cree brouillon ou fiche validation

Workflow C - Approval + Publish
- statut = approved
- pousse le draft dans WP
- log date
- passe en observing

---

# 6) Roadmap recommandee

Phase 1
- Google Sheets ou Airtable pour la base
- n8n pour l orchestration
- WordPress REST pour lecture + drafts

Phase 2
- ajout maillage interne
- ajout briefs refresh
- ajout scoring business pages

Phase 3
- FluentBoards pour pilotage editorial
- FluentCRM pour sequences
- dashboard gains J+14 / J+28

---

# 7) Nom officiel

schoolsWP SEO Ops Brain

# Runbook : Idee → Publication

Flux principal schoolsWP — de l'idee brute a l'article publie.
Chaque etape est un checkpoint humain ou un agent automatise.

---

## Vue d'ensemble

```
IDEE ─→ QUALIFICATION ─→ STRATEGIE ─→ GENERATION ─→ AUDIT ─→ DECISION ─→ PUBLICATION
  1          2               3            4            5          6            7
```

Duree totale : 15-30 min (automatise) + revue humaine

---

## Etape 1 — Idee

**Qui** : Humain
**Entree** : observation, GSC, veille, backlog
**Sortie** : mot-cle brut + intention pressentie

Sources d'idees :
- Google Search Console (requetes impressions sans clics)
- Backlog dans `core/tasks/todo.md`
- Niche Scout : `.venv/Scripts/python -m agents.niche_scout.cli --thematique "LMS WordPress"`
- Audit piliers : `.venv/Scripts/python -m agents.pillar_authority.cli --all`
- Veille concurrentielle manuelle (WPMarmite, Jeremie Dornbusch, Jeune Cadre Dynamique)

**Checkpoint humain** : Le sujet vaut-il un article ? Filtrer les idees a faible ROI avant d'engager le pipeline.

---

## Etape 2 — Qualification

**Qui** : Humain + agents
**Entree** : mot-cle brut
**Sortie** : mot-cle valide, intent, pilier, objectif business

### 2a. Classifier l'intention

| Intent | Signal | Exemple |
|--------|--------|---------|
| informationnelle | "c'est quoi", "comment" | "c'est quoi fluentcrm" |
| comparative | "vs", "ou", "meilleur" | "tutor lms vs learndash" |
| decisionnelle | "avis", "prix", "rentable" | "fluentcrm avis" |
| navigationnelle | nom de marque | "fluentcrm login" |

### 2b. Assigner le pilier

`LMS` | `CRM` | `SEO` | `automatisation` | `ecommerce` | `freelance` | `formation`

### 2c. Definir l'objectif business

`email` (capture) | `affiliation` (monetisation) | `formation` (vente) | `offre` (service)

### 2d. Valider avec le scoring strategique (optionnel)

```bash
.venv/Scripts/python -m agents.niche_scout.scorer_cli --keyword "mot cle" --pillar LMS
```

**Checkpoint humain** : intent + pilier + objectif confirmes. Si le sujet est hors pilier, le rejeter ou le requalifier.

---

## Etape 3 — Strategie

**Qui** : Agent (BrainLiteAgent ou Strategic Brain)
**Entree** : keyword, intent, pilier
**Sortie** : topic H1, angle differenciant, audience cible, ROI check

### Option A — Brain Lite (rapide, 1 appel LLM, ~15s)

Integre dans le Content Factory. Pas d'appel separe necessaire.

### Option B — Strategic Brain (raisonnement complet, ~60s)

```bash
.venv/Scripts/python -m agents.strategic_brain.cli
```

Produit un rapport avec commandes CLI exactes a executer.

### Option C — Pipeline strategique complet (profondeur maximale)

Executer dans l'ordre — chaque agent enrichit le suivant :

```bash
.venv/Scripts/python -m agents.knowledge_graph.cli
.venv/Scripts/python -m agents.pillar_authority.cli --all
.venv/Scripts/python -m agents.cocon_builder.cli --pillar lms
.venv/Scripts/python -m agents.roi_editorial_plan.cli
.venv/Scripts/python -m agents.strategic_brain.cli
```

**Checkpoint humain** : ROI check. Si `roi_ok: false`, soit abandonner soit forcer avec `--force`.

---

## Etape 4 — Generation

**Qui** : Agent (Content Factory ou Article Pipeline)
**Entree** : keyword, intent, pilier, angle
**Sortie** : article V1 → V2 (+ V3, V4 si options activees)

### Option A — Content Factory (pipeline complet, ~4-8 min)

```bash
.venv/Scripts/python -m agents.content_factory.cli \
  --keyword "lms wordpress rentable" \
  --intent decisionnelle \
  --pillar LMS \
  --objective affiliation \
  --save-dir content/articles/lms-rentable/
```

Enchaine automatiquement : strategie → generation → audit → cluster.

Fichiers produits :
```
content/articles/lms-rentable/
  strategy.md       # Angle strategique
  v1.md             # Brouillon (SeoWriterAgent)
  audit-seo.md      # Audit SEO /100
  audit-llm.md      # Audit citabilite IA /100
  audit-conversion.md  # Audit conversion /100
  audit-topical.md  # Audit autorite /100
  v2.md             # Article edite
  cluster.md        # Plan cluster semantique
  meta.md           # Meta SEO + FAQ schema
```

### Option B — Article Pipeline seul (sans audit 4 modules, ~2-4 min)

```bash
.venv/Scripts/python -m agents.article_pipeline.cli \
  --topic "Choisir un LMS WordPress rentable" \
  --keyword "lms wordpress rentable" \
  --intent decisionnelle \
  --angle "focus ROI freelance, pas de jargon" \
  --save-dir content/articles/lms-rentable/
```

Options disponibles :
- `--include-serp` : simulation SERP Top 5 (+2 min)
- `--skip-llm` : pas d'optimisation LLM-SEO
- `--skip-ner` : pas d'enrichissement NER semantique
- `--skip-links` : pas de maillage interne
- `--skip-meta` : pas d'extraction meta

### Option C — Brain Lite (pipeline allege, ~2 min)

```bash
.venv/Scripts/python -m agents.article_pipeline.brain_lite_cli \
  --keyword "fluentcrm avis" \
  --intent informationnelle \
  --pilier crm
```

**Checkpoint humain** : Ouvrir `v1.md` ou `v2.md`. L'article repond-il a l'intention ? Le ton est-il schoolsWP ? Sinon, corriger l'angle et relancer.

---

## Etape 5 — Audit

**Qui** : Agent (Publish Ready)
**Entree** : article markdown + keyword
**Sortie** : Publish Score /100 + plan d'action priorise

Si tu as utilise le Content Factory (etape 4A), l'audit est deja inclus. Sinon :

```bash
.venv/Scripts/python -m agents.publish_ready.cli \
  --file content/articles/lms-rentable/v2.md \
  --keyword "lms wordpress rentable" \
  --intent decisionnelle \
  --pillar LMS \
  --save-dir content/articles/lms-rentable/
```

### Les 4 modules d'audit (executes en parallele)

| Module | Poids | Ce qu'il mesure |
|--------|-------|-----------------|
| SEO Structure | 30% | H1/H2/H3, keyword density, maillage, meta |
| Citabilite IA | 25% | Reponse rapide, blocs extractibles, definitions, snippets |
| Conversion & CTA | 25% | Clarte probleme, orientation action, CTA, business alignment |
| Autorite Thematique | 20% | Couverture, connexions, coherence, positionnement, cluster |

### Formule Publish Score

```
Publish Score = SEO * 0.30 + LLM * 0.25 + Conversion * 0.25 + Autorite * 0.20
```

### Avec auto-correction du module le plus faible

```bash
.venv/Scripts/python -m agents.publish_ready.cli \
  --file content/articles/lms-rentable/v2.md \
  --keyword "lms wordpress rentable" \
  --fix-weakest --threshold 85 \
  --save-dir content/articles/lms-rentable/
```

**Checkpoint humain** : Lire le plan d'action priorise. Appliquer les 3 premieres actions manuellement si necessaire.

---

## Etape 6 — Decision

**Qui** : Humain
**Entree** : Publish Score + plan d'action
**Sortie** : go / no-go / iteration

| Publish Score | Decision | Action |
|---------------|----------|--------|
| >= 90 | Publication immediate | → Etape 7 |
| 80-89 | Ajustements mineurs | Appliquer 1-2 corrections, re-auditer |
| 70-79 | Revision ciblee | Corriger le module le plus faible, relancer `--fix-weakest` |
| < 70 | Reecriture | Revoir l'angle strategique, relancer depuis l'etape 3 |

### Boucle d'amelioration (si score < 90)

```
v2.md → publish_ready --fix-weakest → v2-fixed.md → publish_ready (re-audit) → decision
```

Maximum 2 iterations. Si le score ne monte pas apres 2 passes, le probleme est strategique (angle, intent, ou sujet) — revenir a l'etape 2.

**Checkpoint humain** : Decision finale. Relire l'article complet avant publication. Verifier : tutoiement, mots interdits, chiffres sourcs, CTA non agressif.

---

## Etape 7 — Publication

**Qui** : Humain (+ n8n optionnel)
**Entree** : article final + meta SEO
**Sortie** : article publie sur schoolswp.com

### 7a. Preparer les assets

- [ ] Article final (v2.md ou v2-fixed.md)
- [ ] Meta title + description (meta.md)
- [ ] FAQ schema markup (dans meta.md)
- [ ] Images avec metadonnees SEO (skill `wp-image-metadata-seo`)
- [ ] Maillage interne (links.md → inserer les liens dans l'article)
- [ ] Cluster plan (cluster.md → planifier les articles satellites)

### 7b. Publier sur WordPress

Publication manuelle via l'editeur WordPress ou via WP-CLI :

```bash
# Upload via n8n webhook (si configure)
# Ou copier-coller dans l'editeur Gutenberg
```

### 7c. Post-publication

- [ ] Verifier le rendu sur mobile
- [ ] Tester les liens internes
- [ ] Soumettre l'URL dans Google Search Console
- [ ] Planifier les articles satellites du cluster (cluster.md)
- [ ] Ajouter au tracking dans `core/tasks/todo.md`

---

## Raccourcis

### Article rapide (skip strategie)

```bash
.venv/Scripts/python -m agents.article_pipeline.cli \
  --topic "..." --keyword "..." --intent comparative --angle "..." \
  --save-dir content/articles/mon-sujet/
```

### Audit seul (article existant)

```bash
.venv/Scripts/python -m agents.publish_ready.cli \
  --file mon-article.md --keyword "mon mot cle" \
  --save-dir content/articles/mon-sujet/
```

### Pipeline complet en une commande

```bash
.venv/Scripts/python -m agents.content_factory.cli \
  --keyword "mot cle" --intent decisionnelle --pillar LMS \
  --save-dir content/articles/mon-sujet/
```

---

## Arbre de decision

```
As-tu un mot-cle valide ?
├── Non → Etape 1 (Niche Scout, GSC, veille)
└── Oui
    ├── Intent + pilier definis ?
    │   ├── Non → Etape 2 (Qualification)
    │   └── Oui
    │       ├── Besoin de profondeur strategique ?
    │       │   ├── Oui → Etape 3 Option C (pipeline strategique)
    │       │   └── Non → Etape 4 (generation directe)
    │       │       ├── Article complet + audit → Content Factory (4A)
    │       │       ├── Article seul → Article Pipeline (4B)
    │       │       └── Brouillon rapide → Brain Lite (4C)
    │       └── Article existant a auditer ?
    │           └── Oui → Etape 5 (Publish Ready)
    └── Publish Score >= 90 ?
        ├── Oui → Etape 7 (Publication)
        └── Non → Etape 6 (Decision : corriger ou rewriter)
```

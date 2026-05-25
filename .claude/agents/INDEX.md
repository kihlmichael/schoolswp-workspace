# schoolsWP Project Sub-Agents — Index complet

<!-- AUTO:HEADER:START -->
**Total** : 28 sub-agents | **Mis à jour** : 2026-05-21
<!-- AUTO:HEADER:END -->

**Structure** : un fichier `.md` par agent dans `.claude/agents/`, frontmatter YAML (`name`, `description`, `model`, `tools`)

> Sub-agents Claude Code dispatchables via le tool Agent (parallélisables, contexte isolé). Différents de :
> - la fleet `schoolswp-agents/` (4 instances autonomes en process séparé, leurs propres `CLAUDE.md` + `soul.md` + mémoire)
> - les agents Python (`core/agents-py/`, 28 scripts CLI héritant de `BaseContentAgent`)
>
> Pour les règles de conflit qui doivent rester chargées en contexte, voir [CLAUDE.md](../../CLAUDE.md) (section Project Sub-Agents).

---

## Routing Priority — quel agent pour quelle demande

Tables d'arbitrage anti-collision. Les règles fines de conflit sont en bas (section « Règles de conflit »).

### Production éditoriale schoolsWP

| Input utilisateur | Agent à dispatcher |
|---|---|
| Rédaction article, newsletter, brief éditorial, tutoriel, guide | `studio` |
| Cocon sémantique, brief SEO, keyword analysis, maillage interne | `radar` |
| Post LinkedIn, Bluesky, Pinterest text, YouTube description/titre, recyclage social | `pulse` |
| FluentCRM, OttoKit, n8n, Fluent Forms, sales funnels, webhooks | `flow` |
| Adaptation EN → FR d'un framework ou doc stratégique | `framework-adapter-fr` |
| Post Reddit FR/EN, commentaire thread, shortlist subs | `reddit` |
| Brief thruuu `.docx` → article schoolsWP publiable (pipeline complet orchestré, statut `REVIEW_REQUIRED`) | `thruuu-article-orchestrator` |

### YouTube OS (pipeline vidéo schoolsWP)

| Input utilisateur | Agent à dispatcher |
|---|---|
| « Je veux faire une vidéo sur X » (orchestration complète) | `youtube-os-orchestrator` |
| Idées vidéo priorisées (P1/P2/P3) à partir d'un sujet/plugin/opportunité | `youtube-strategy-scout` |
| Script complet 9 sections (hook → CTA) + notes tournage + B-roll | `youtube-script-writer` |
| Titres x5, description, chapitres, tags, hashtags, commentaire épinglé | `youtube-seo-packager` |
| Brief miniature (3 variantes A/B/C) + composition + prompt image | `youtube-thumbnail-director` |
| Vidéo longue → Shorts + sous-titres FR/EN/DE + posts LinkedIn | `youtube-clipper` |
| Checklist publication, blocage tant que statut ≠ `APPROVED` | `youtube-publisher-scheduler` |
| Données YouTube → une action prioritaire + test suivant | `youtube-analytics-learner` |
| Audit livrable avant validation (clarté, ton, crédibilité, risques) | `youtube-quality-auditor` |

> **Règle fondatrice YouTube OS** : statut par défaut `REVIEW_REQUIRED`, aucune publication publique sans validation humaine explicite. Livrables dans `content/youtube/`, traces de pipeline dans `runs/youtube-os/`.

### SEO / techniques

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit technique SEO, schema, Core Web Vitals, sitemap/robots, meta tags | `seo-specialist` |

### Pinterest

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit compte Pinterest, Ads, scaling horizontal, creatives IA, SEO Pinterest, retargeting | `pinterest-expert` |

### Design / UI

| Input utilisateur | Agent à dispatcher |
|---|---|
| Frontend, landing page, dashboard, marketing page via MCP aidesigner | `aidesigner-frontend` |

### Acquisition payante

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit Google Ads Search, plans d'acquisition, landing ads, mots-clés, tracking, QS, décisions GO/FIX/PAUSE/STOP | `ads-operator` |

### Publication externe (hors schoolsWP)

| Input utilisateur | Agent à dispatcher |
|---|---|
| Article via Skoatch API + push draft WordPress sur michaelkihl.fr (ou autre site WP non-schoolsWP) | `skoatch-publisher` |

### Code review / qualité (read-only)

| Input utilisateur | Agent à dispatcher |
|---|---|
| Review de code après implémentation, avant merge d'une PR, audit d'un diff (5 axes) | `code-reviewer` |
| Détection décision architecturale → ADR pattern Nygard | `adr-writer` |
| Review adversariale d'un plan d'implémentation (5 dimensions) | `plan-challenger` |
| LLM-as-Judge qualité avant commit/action | `output-evaluator` |
| Détection silent failures, swallowed errors, fallbacks dangereux | `silent-failure-hunter` |

### Harness / infra

| Input utilisateur | Agent à dispatcher |
|---|---|
| Tuning harness Claude Code (reliability, cost, throughput) | `harness-optimizer` |

### Hors schoolsWP (projets personnels)

| Input utilisateur | Agent à dispatcher |
|---|---|
| AI influencer / OFM (identity design, photo prompt batches Alexya) | `ofm-bot` |

---

## Tables détaillées par groupe

<!-- AUTO:TABLES:START -->

### Contenu éditorial schoolsWP

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `flow` | sonnet | Read, Write, Edit, Bash, Glob, Grep | Use this agent for CRM, email marketing, and automation tasks on schoolsWP. |
| `framework-adapter-fr` | sonnet | Glob, Grep, ListMcpResourcesTool, Read, ReadMcpResourceTool, WebFetch, WebSearch, Edit, NotebookEdit, Write, Bash | Use this agent when the user needs to adapt, translate, or rewrite an English-language framework, methodology, or strategic document into natural, high-quality French. |
| `pulse` | haiku | Read, Write, Edit, Glob, Grep | Use this agent for social media content and community tasks for schoolsWP. |
| `radar` | sonnet | Read, Write, Edit, Glob, Grep | Use this agent for SEO and GEO tasks related to schoolsWP. |
| `reddit` | sonnet | Read, Write, Edit, Glob, Grep | Use this agent for Reddit content and strategy tasks for schoolsWP. |
| `studio` | opus | Read, Write, Edit, Bash, Glob, Grep | Use this agent when the user asks to write, draft, or create content for schoolsWP. |
| `thruuu-article-orchestrator` | opus | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | Use this agent to orchestrate the full pipeline that turns a thruuu content brief (.docx) into a publish-ready schoolsWP article, in an isolated context. |

### YouTube OS

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `youtube-analytics-learner` | opus | (par défaut) | Analyse les performances YouTube schoolsWP et transforme les données en décisions éditoriales concrètes. |
| `youtube-clipper` | opus | (par défaut) | Découpe les vidéos longues schoolsWP en extraits courts, Shorts, sous-titres FR/EN/DE, posts LinkedIn et checklists de publication. |
| `youtube-os-orchestrator` | opus | (par défaut) | Pilote le YouTube OS schoolsWP. À utiliser pour transformer une idée, un article, une vidéo longue ou une opportunité en pipeline YouTube complet. |
| `youtube-publisher-scheduler` | opus | (par défaut) | Prépare la publication YouTube schoolsWP, vérifie les éléments de mise en ligne et bloque toute publication sans validation humaine. |
| `youtube-quality-auditor` | opus | (par défaut) | Audite les livrables YouTube schoolsWP avant validation humaine : clarté, crédibilité, ton, risques, affiliation et publication. |
| `youtube-script-writer` | opus | (par défaut) | Rédige des scripts YouTube schoolsWP clairs, pédagogiques et actionnables à partir d'une idée, d'un brief, d'un article ou d'un plugin. |
| `youtube-seo-packager` | opus | (par défaut) | Prépare le package SEO YouTube schoolsWP : titres, description, chapitres, tags, hashtags et commentaire épinglé. |
| `youtube-strategy-scout` | opus | (par défaut) | Trouve et priorise des idées de vidéos YouTube schoolsWP à partir d'un sujet, d'un article, d'un plugin, d'une question ou d'une opportunité SEO. |
| `youtube-thumbnail-director` | opus | (par défaut) | Crée des briefs de miniatures YouTube schoolsWP lisibles, sobres, premium utiles et cohérents avec l'identité visuelle. |

### Spécialistes domaine

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `ads-operator` | opus | Read, Grep, Glob, Bash | Opérateur SEA schoolsWP / michaelkihl.fr. À utiliser pour audits Google Ads Search, plans d'acquisition, landing ads, budget, mots-clés, négatifs, tracking, Quality Score, conversions hors-ligne, et d… |
| `aidesigner-frontend` | (défaut) | (par défaut) | Use this skill when the user wants to create or redesign a frontend, landing page, dashboard, marketing page, or other UI with AIDesigner. |
| `pinterest-expert` | opus | (par défaut) | Agent Pinterest expert base sur les enseignements de Luc Bermond (1606 unites, 215 videos). |
| `seo-specialist` | sonnet | Read, Grep, Glob, Bash, WebSearch, WebFetch | SEO specialist for technical SEO audits, on-page optimization, structured data, Core Web Vitals, and content/keyword mapping. |
| `skoatch-publisher` | sonnet | Read, Write, Edit, Bash, Glob, Grep | Use this agent when the user wants to generate articles via Skoatch API and push them as WordPress drafts on michaelkihl.fr or another connected non-schoolsWP site. |

### Code review / qualité — read-only

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `adr-writer` | opus | Read, Grep, Glob | Architecture Decision Record generator agent — read-only. Detects architectural decisions in code changes, classifies criticality, and generates ADRs in the pattern-oriented ADR format by Michael Nyga… |
| `code-reviewer` | sonnet | Read, Grep, Glob, Bash | Senior code reviewer, read-only. Evaluates a diff across 5 axes (correctness, readability, architecture, security, performance) and returns categorized findings with an APPROVE or REQUEST CHANGES verd… |
| `output-evaluator` | haiku | Read, Grep, Glob | Evaluate Claude Code outputs for quality before commit/action (LLM-as-a-Judge pattern) |
| `plan-challenger` | opus | Read, Grep, Glob | Adversarial plan review agent — read-only. Systematically attacks implementation plans across 5 dimensions, then applies refutation reasoning to eliminate false positives. Never modifies code. |
| `silent-failure-hunter` | sonnet | Read, Grep, Glob, Bash | Review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation. |

### Harness / infra

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `harness-optimizer` | sonnet | Read, Grep, Glob, Bash, Edit | Analyze and improve the local agent harness configuration for reliability, cost, and throughput. |

### Hors schoolsWP (projets personnels)

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `ofm-bot` | opus | Read, Write, Edit, Glob, Grep | Use this agent for AI influencer / OFM content production tasks (identity design, photo prompt batches for Alexya engine). |

<!-- AUTO:TABLES:END -->

---

## Règles de conflit (anti-collision)

> Ces règles **doivent rester chargées en contexte** (donc dupliquées dans `CLAUDE.md`) car elles évitent les mauvais dispatches en cours de session.

- **`studio` vs YouTube OS** : `studio` rédige du contenu éditorial schoolsWP (article, newsletter, brief, script générique). Pour une vidéo YouTube complète avec pipeline (script → SEO → thumbnail → publication), passer par `youtube-os-orchestrator`. Pour un script vidéo isolé : `studio` reste OK.
- **`pulse` vs YouTube OS** : `pulse` produit la description / titre d'une vidéo YouTube ponctuelle. `youtube-seo-packager` produit le package SEO complet (5 titres, description, chapitres, tags, hashtags, commentaire épinglé) dans le cadre d'un pipeline.
- **`pulse` vs `pinterest-expert`** : `pulse` rédige le texte pin (titre + description). `pinterest-expert` audite / scale / pilote Ads / SEO Pinterest organique.
- **`flow` vs `pulse`** : `flow` = mécanique CRM/automation/n8n. `pulse` = copy social. La pipeline Pinterest technique (n8n + Placid + Tailwind) reste `flow`.
- **`radar` vs `seo-specialist`** : `radar` = SEO éditorial schoolsWP (cocons, briefs, maillage). `seo-specialist` = SEO technique générique (schema, Core Web Vitals, sitemap, audit serveur).
- **`skoatch-publisher` isolation** : **interdit sur schoolswp.com** (BRAND_RULES incompatibles). michaelkihl.fr uniquement, ou autre site WP non-schoolsWP sur demande explicite.
- **`ofm-bot` isolation** : aucun chevauchement avec schoolsWP (utiliser `studio` / `radar` / `pulse` / `flow`). Pas de génération d'image standalone (utiliser nano-banana directement).
- **Quartet `studio` / `radar` / `pulse` / `flow`** : mirror la fleet `schoolswp-agents/` (instances autonomes) mais en sub-agents projet dispatchables en parallèle dans la session courante.
- **`thruuu-article-orchestrator` vs `studio`** : l'orchestrateur traite uniquement un pipeline complet à partir d'un brief thruuu `.docx` (gap analysis → rédaction → humanisation → linking → QA editor-in-chief). `studio` reste le défaut pour tout contenu éditorial générique (newsletter, script, brief, article sans brief `.docx`). L'orchestrateur s'appuie sur le skill `thruuu-writer`, il ne le duplique pas. Il ne publie jamais : statut de sortie `REVIEW_REQUIRED`.

---

## Maintenance

Les zones marquées `<!-- AUTO:HEADER -->` (compteur + date) et `<!-- AUTO:TABLES -->` (tables détaillées par groupe) sont régénérées par le script [tools/scripts/agents-registry.py](../../tools/scripts/agents-registry.py) :

    .venv/Scripts/python tools/scripts/agents-registry.py            # rapport (lecture seule)
    .venv/Scripts/python tools/scripts/agents-registry.py --sync     # régénère INDEX.md
    .venv/Scripts/python tools/scripts/agents-registry.py --check    # exit 1 si désynchronisé (CI / pre-commit)

**Pour ajouter un agent** :

1. Créer `.claude/agents/<nom>.md` avec frontmatter (`name`, `description`, `model`, `tools`).
2. Ajouter `"<nom>": "<groupe>"` dans le dict `GROUPS` de `tools/scripts/agents-registry.py`.
3. Ajouter une entrée routing manuelle (section « Routing Priority » de cet INDEX) — pas auto-générée car c'est de la sémantique humaine.
4. Lancer `--sync` pour régénérer les tables détaillées et le compteur.

**Pour supprimer un agent** : retirer le fichier `.md`, l'entrée du dict `GROUPS`, le routing, puis `--sync`.

**Pour renommer** : `name:` dans le frontmatter fait foi pour le dispatch, pas le nom de fichier (exemple : `pinterest.md` expose `pinterest-expert`). Mettre à jour `GROUPS` et le routing en conséquence.

**Agent non classé** : si un `.md` existe mais n'est pas dans `GROUPS`, le script le range dans le groupe « Non classé » et alerte. À mapper explicitement.

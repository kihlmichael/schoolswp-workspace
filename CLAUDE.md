# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Data Safety — Suppressions

Interdiction totale d'utiliser `rm` (dont `rm -rf`), `sudo`, ou toute commande destructrice.

Toute suppression doit passer par la corbeille :

```bash
trash <chemin>          # fichier ou dossier
trash dist/*            # via glob
```

Ne jamais vider la corbeille automatiquement.

## Setup initial

**Python (une seule fois après un clone) :**

```powershell
# Depuis projects/schoolswp/ dans PowerShell
pip install uv
uv sync          # installe les dépendances depuis uv.lock
```

Si `uv` n'est pas dans le PATH après installation, utiliser le chemin complet :

```powershell
& "$env:APPDATA\Python\Python313\Scripts\uv.exe" sync
```

**JS (si usage des packages Node) :**

```bash
npm install
```

---

## Python Environment

Toutes les commandes Python doivent être lancées depuis `projects/schoolswp/` avec l'un des deux venvs — ne jamais mélanger :

| Venv | Chemin | Utilisé par |
| --- | --- | --- |
| Root venv | `.venv/Scripts/python` | Tous les `python -m agents.*` |
| Legacy venv | `tools/scripts/legacy/scripts/.venv/Scripts/python` | `brain.bat` et `brain-lite.bat` uniquement |

Sur Windows + Bash, `source .venv/Scripts/activate` ne persiste pas entre les appels. Toujours utiliser le chemin complet.

## Key Commands

**Content factory (pipeline complet — génération + audit + cluster) :**

```bat
brain.bat --keyword "lms wordpress rentable" --intent décisionnelle --pillar LMS
brain.bat --keyword "tutor lms vs learndash" --intent comparative --pillar LMS --include-ner
brain.bat --file content/articles/lms/v3.md --kw "lms wordpress" --intent décisionnelle
```

Flags `brain.bat` : `--keyword` | `--file` + `--kw`, `--intent`, `--pillar`, `--objective`, `--include-serp`, `--include-ner`, `--no-links`, `--no-cluster`, `--force`, `--save-dir`, `--model`

- `--intent` : `informationnelle` | `commerciale` | `décisionnelle` | `comparative` | `navigationnelle`
- `--pillar` : `LMS` | `CRM` | `SEO` | `automatisation` | `ecommerce` | `freelance` | `formation`
- `--objective` : `email` | `affiliation` | `formation` | `offre`

**Brain Lite (pipeline 5 étapes, sans NER/SERP) :**

```bat
brain-lite.bat --keyword "fluentcrm avis" --intent informationnelle --pilier crm
```

**Agents individuels :**

```bash
.venv/Scripts/python -m agents.schoolswp_brain.cli --query "..." --mode seo-writer
# modes : seo-writer | plugin-comparator | wp-architect | automation-consultant

.venv/Scripts/python -m agents.article_pipeline.cli --topic "..." --keyword "..." --intent comparative --angle "..."
.venv/Scripts/python -m agents.publish_ready.cli --file article.md --keyword "..."
.venv/Scripts/python -m agents.seo_auditor.cli --file article.md --keyword "..." [--fix]
.venv/Scripts/python -m agents.strategic_brain.cli

# Exploration de niches (syntaxe spécifique — utilise --thematique, pas --keyword)
.venv/Scripts/python -m agents.niche_scout.cli --thematique "LMS WordPress" [--focus "automatisation"] [--context "..."]
.venv/Scripts/python -m agents.niche_scout.scorer_cli --niches niches.md        # score /10 par niche
.venv/Scripts/python -m agents.niche_scout.batch_scorer_cli --file niches.md    # batch scoring
.venv/Scripts/python -m agents.niche_scout.data_scorer_cli --csv data.csv       # scoring depuis CSV
```

**Linting :**

```bash
.venv/Scripts/python -m ruff check core/agents-py/
.venv/Scripts/python -m ruff format core/agents-py/
```

## JS Dependencies

`package.json` contient des dépendances JS (pas de bundler configuré — usage direct via Node) :

| Package | Usage |
| --- | --- |
| `@anthropic-ai/claude-agent-sdk` | SDK Agent Claude côté JS |
| `@mendable/firecrawl-js` | Web scraping |
| `@pinecone-database/pinecone` | Recherche vectorielle |
| `@wordpress/data` | Accès au store WordPress (Gutenberg) |

## Agent Architecture

Deux couches complémentaires :

- `core/agents-md/` — System prompts Markdown par agent (index : `core/agents-md/INDEX.md`)
- `core/agents-py/` — Implémentations Python (`agent.py` + `cli.py` par agent)

Tous les agents héritent de `BaseContentAgent` (`core/agents-py/base.py`) — async, retourne `str` (markdown).

**Modules principaux :**

| Module | Rôle |
| --- | --- |
| `agents.content_factory.cli` | Pipeline complet : strategy → article → audit → cluster (`brain.bat`) |
| `agents.article_pipeline.cli` | Pipeline séquentiel 5-7 agents (Writer→Auditor→Editor→LLM→Meta) |
| `agents.article_pipeline.brain_lite_cli` | Pipeline simplifié 5 étapes (`brain-lite.bat`) |
| `agents.publish_ready.cli` | 4 audits parallèles (SEO + LLM + Conversion + Topical) |
| `agents.schoolswp_brain.cli` | Agent stratégique (4 modes : seo-writer, plugin-comparator, wp-architect, automation-consultant) |
| `agents.schoolswp_brain.workflow_cli` | Workflows W1 (SeoAudit), W2 (Competitive), W3 (ContentFactory) |
| `agents.seo_auditor.cli` | Audit SEO /100 + `--fix` |
| `agents.llm_seo.cli` | Citabilité IA /100 + `--inject` |
| `agents.conversion_auditor.cli` | Audit conversion /100 + `--inject` |
| `agents.topical_authority.cli` | Autorité thématique /100 + `--expand` |
| `agents.knowledge_graph.cli` | Graphe éditorial — inventaire sujets + gaps |
| `agents.pillar_authority.cli` | Audit autorité par pilier (`--all` → `audit/piliers/summary.md`) |
| `agents.cocon_builder.cli` | Cocon sémantique par pilier |
| `agents.roi_editorial_plan.cli` | Plan éditorial auto-priorisé ROI |
| `agents.strategic_brain.cli` | Orchestrateur décisionnel → commandes CLI prêtes |
| `agents.kpi_dashboard.cli` | Dashboard KPI éditorial + `--export-json` pour Sheets/Notion |
| `agents.seo_competitor_analyst.cli` | Gap analysis SEO vs concurrent |
| `agents.niche_scout.cli` | Exploration niches SEO + scoring |
| `agents.cluster_architect.cli` | Architecture cluster sémantique |
| `agents.seo_writer.cli` | Rédaction SEO standalone |
| `agents.automation_consultant.cli` | Conseil automation n8n / WordPress |
| `agents.plugin_comparator.cli` | Comparaison plugins WordPress (tableaux, scoring) |
| `agents.lms_trainer.cli` | Spécialiste LMS (LearnDash, TutorLMS, LifterLMS) |
| `agents.wp_business_teacher.cli` | Stratégie business enseignant WordPress |
| `agents.wp_digital_sales.cli` | Optimisation ventes digitales WordPress |
| `agents.wp_freelance_teacher.cli` | Guide freelance formateur WordPress |
| `agents.wp_premium_freelance.cli` | Positionnement premium freelance WordPress |
| `agents.wp_profit_architect.cli` | Architecture rentabilité WordPress |
| `agents.wp_teacher.cli` | Conseiller pédagogique WordPress enseignant |

**Pipeline stratégique recommandé (ordre) :**

```bash
.venv/Scripts/python -m agents.knowledge_graph.cli            # → content/docs/knowledge-graph.md
.venv/Scripts/python -m agents.pillar_authority.cli --all     # → audit/piliers/summary.md
.venv/Scripts/python -m agents.cocon_builder.cli --pillar lms # → cocons/lms.md
.venv/Scripts/python -m agents.roi_editorial_plan.cli         # → plans/plan-roi.md
.venv/Scripts/python -m agents.strategic_brain.cli            # → decisions/brain-report.md
```

**Publish Score formula :**

```text
Score = SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20
```

Seuils : ≥90 → publication immédiate | 80-89 → ajustements mineurs | 70-79 → révision ciblée | <70 → réécriture

## Branding

- Toujours `schoolsWP` — jamais `SchoolsWP`, `schoolswp`, `Schoolswp`
- Site : `schoolswp.com` (sans `www.`)
- Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de
- Source de vérité : `content/docs/BRAND_RULES.md`

## Code Conventions

**Python** — PEP 8, 4 espaces, ruff, Python 3.11+, line-length 120

**JSON/JS** — 2 espaces, pas de trailing comma, UTF-8, LF

**Shell** — shebang `#!/usr/bin/env bash`, 2 espaces

**Fichiers** — kebab-case (jamais camelCase)

**Commits** — conventionnel en anglais : `feat:`, `fix:`, `chore:`, `docs:`

**Branches** — `feature/*` ou `fix/*` depuis `main`

**Nommage workflows n8n** — `[Status] Source > Destination: Description (ID)`

**Status** : `[InDev]` `[InTesting]` `[Staging]` `[Prod]` `[Offline]` `[ForDeletion]`

## n8n Integration

- **Instance** : `https://schoolswp-n8n.wp1.host` (hébergé — pas Docker local)
- **MCP** : configuré dans `.mcp.json` (ne pas modifier sans accord)
- **Règles complètes** : `systems/n8n/CLAUDE.md` et `systems/n8n/Règles du jeu – automatisation n8n.md`
- Ne jamais modifier les JSON de workflows à la main : passer par le MCP ou l'interface n8n

**typeVersions max confirmées :**

| Node | Version max |
| --- | --- |
| scheduleTrigger | 1.2 |
| httpRequest | 4.2 |
| googleSheets | 4.5 |
| openAi (langchain) | 1.8 |
| code | 2 |
| set | 3.4 |
| if | 2.2 |
| merge | 3.1 |

Contrainte Code node : `$helpers.httpRequest()` non disponible dans le task runner n8n 2.0 — utiliser un nœud HTTP Request séparé.

Contrainte Google Sheets : `appendOrUpdate` — le champ `matchingColumns` ne peut pas être vide.

**Nommage credentials** : `Service_Environment_Type` — ex: `GoogleSheets_Production_OAuth`

**Backup n8n** : scripts dans `systems/n8n-backup/` (`backup-n8n.sh`, `restore-n8n.sh`). Déployer sur le serveur n8n, pas en local. Voir `systems/n8n-backup/README.md` pour le déploiement complet.

## Security

- `.env` jamais versionné. `.mcp.json` dans `.gitignore` — utiliser `.mcp.json.example` comme template.
- Credentials n8n sanitisés avant export.
- Vérifier `.gitignore` avant tout commit.

## Execution Protocol

1. Plan dans `core/tasks/todo.md` (tâche courante) ou `core/tasks/plans/` (plans multi-étapes)
2. Exécution pas à pas
3. Vérification
4. Lessons dans `core/tasks/lessons.md`

## Skills Registry

Skills Claude Code pour ce projet répartis sur :

| Emplacement | Rôle |
| --- | --- |
| `.claude/skills/` (projet) | Skills locaux schoolsWP |
| `d:\VS Code\CLAUDE CODE\.claude\skills\` (workspace) | Skills workspace — 83 skills FR (n8n, WP, SEO…) |
| `.agents/skills/` (workspace) | Source library — 42 skills, descriptions FR synchronisées |

**Sync registre vers Google Sheets :**

```bash
.venv/Scripts/python "d:/VS Code/CLAUDE CODE/.claude/skills/.registry/skills_registry.py" --sync
```

**INDEX des skills projet** : `.claude/skills/INDEX.md`

## Reference Docs

### Chargés automatiquement

- `@.claude/docs/schoolswp-method.md` — 6 frameworks (SPECS, Decision Engine, CREDO, DITO, PACT, TDD)
- `@.claude/docs/schoolswp-stack.md` — stack officielle
- `@.claude/docs/schoolswp-style-guide.md` — guide rédactionnel

### Disponibles à la demande (via `@`)

- `.claude/docs/schoolswp-seo-engine.md` — moteur SEO
- `.claude/docs/schoolswp-content-engine.md` — pipeline de production
- `.claude/docs/schoolswp-authority-engine.md` — système d'autorité
- `.claude/docs/schoolswp-auto-router.md` — logique de routage automatique
- `.claude/docs/schoolswp-gsc-radar.md` — intégration Google Search Console
- `.claude/docs/schoolswp-seo-ops-brain.md` — orchestration SEO ops
- `.claude/docs/schoolswp-authority-domination-24m.md` — plan autorité 24 mois
- `core/agents-py/CLAUDE.md` — conventions Python agents, patterns, pipeline flags

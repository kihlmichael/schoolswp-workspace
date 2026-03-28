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

```bash
pip install uv && uv sync                    # Python deps (une seule fois)
cp .env.example .env                         # puis remplir les clés
cp .mcp.json.example .mcp.json               # puis remplir les clés API MCP
npm install                                   # JS deps (optionnel)
```

Si `uv` n'est pas dans le PATH : `& "$env:APPDATA\Python\Python313\Scripts\uv.exe" sync`

Variables clés `.env` : `ANTHROPIC_API_KEY` (obligatoire), `MODEL_WRITER` (défaut: `claude-sonnet-4-6`), `FIRECRAWL_API_KEY`, `N8N_*`, `GOOGLE_WORKSPACE_CLI_CLIENT_ID/SECRET`. Recherche : `agents/.env` → `.env` → `multi-agent-system/.env`.

## Python Environment

Projet `schoolswp-agents` v0.1.0 — Python `>=3.11`. Gestionnaire : `uv` (lock file `uv.lock`). Synchroniser : `uv sync` depuis la racine projet.

Dépendances principales : `anthropic>=0.49.0`, `python-dotenv>=1.0.0`. Dev : `pytest>=8.0`, `pytest-asyncio>=0.24`.

**Venv** : `.venv/Scripts/python` — seul venv actif. Sur Windows + Bash, `activate` ne persiste pas — utiliser le chemin complet.

> **Note** : `brain.bat` et `brain-lite.bat` référencent un legacy venv (`tools/scripts/legacy/scripts/.venv/`) qui n'existe plus. Utiliser le root venv directement : `.venv/Scripts/python -m agents.content_factory.cli ...`

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

Entry point réel : `agents.article_pipeline.brain_lite_cli` (le `.bat` est un wrapper).

**Agents individuels** (pattern : `.venv/Scripts/python -m agents.<module>.cli`) :

```bash
.venv/Scripts/python -m agents.schoolswp_brain.cli --query "..." --mode seo-writer
.venv/Scripts/python -m agents.article_pipeline.cli --topic "..." --keyword "..." --intent comparative
.venv/Scripts/python -m agents.publish_ready.cli --file article.md --keyword "..."
.venv/Scripts/python -m agents.seo_auditor.cli --file article.md --keyword "..." [--fix]
.venv/Scripts/python -m agents.niche_scout.cli --thematique "LMS WordPress" [--focus "auto"]
```

Table complète des 28 modules dans `.claude/rules/python-agents.md`.

**Linting :**

```bash
.venv/Scripts/python -m ruff check core/agents-py/    # lint
.venv/Scripts/python -m ruff format core/agents-py/   # format
```

Hook `ruff-check.sh` auto-exécuté après chaque Edit/Write sur `.py`.

**Tests :**

```bash
.venv/Scripts/python -m pytest tests/                  # tous les tests
.venv/Scripts/python -m pytest tests/test_base.py -v   # un fichier
.venv/Scripts/python -m pytest tests/test_base.py::test_safe_read_path_rejects_traversal -v  # un test
```

pytest configuré avec `asyncio_mode = "auto"` — pas besoin de décorateur `@pytest.mark.asyncio` sur les tests async.

Fixtures (`tests/conftest.py`) : `fake_env` (mock `ANTHROPIC_API_KEY` + `MODEL_WRITER`), `mock_anthropic_client` (factory — appeler pour obtenir un mock, pas un mock direct), `tmp_article` (fichier .md dans `tmp_path`). Note import : conftest.py enregistre `core/agents-py/` comme package `agents` dans `sys.modules` — pas besoin de path hack dans les tests.

**Fichiers de test existants :**

| Fichier | Couverture |
| --- | --- |
| `test_base.py` | `safe_read_path` / `safe_write_path` — protection path traversal |
| `test_agent_contract.py` | Contrat agent async (héritage BaseContentAgent, signature `run()`) |
| `test_article_pipeline_contract.py` | Contrat pipeline article (structure, étapes) |
| `test_audit_dataclasses.py` | Dataclasses d'audit (parsing, sérialisation) |
| `test_content_factory_contract.py` | Contrat content factory (orchestration pipeline) |
| `test_pipelines_e2e.py` | Tests e2e pipelines (intégration multi-agents) |
| `test_publish_ready_contract.py` | Contrat publish_ready (4 audits parallèles) |
| `test_seo_auditor_agent.py` | Agent SEO auditor — logique métier |
| `test_seo_auditor_cli.py` | CLI parsing seo_auditor |

**Skills slash commands** (`.claude/skills/`) : `/audit`, `/brain-lite`, `/publish-repo`, `/skill-creator`, `/todo`

## JS Dependencies

`package.json` : `@anthropic-ai/claude-agent-sdk`, `@mendable/firecrawl-js`, `@pinecone-database/pinecone`, `@wordpress/data`. Pas de bundler — usage direct via Node.

## Agent Architecture

→ Détails complets dans `.claude/rules/python-agents.md` (chargé auto quand tu travailles dans `core/agents-py/`)

Résumé : 28 agents Python héritant de `BaseContentAgent`, async, retourne markdown. Chaque agent = `agent.py` + `cli.py`. **La table complète des modules CLI est dans `.claude/rules/python-agents.md`** — ne pas dupliquer ici.

**BaseContentAgent contract** (`core/agents-py/base.py`) :

```python
class BaseContentAgent:
    name: str = "base"                    # identifiant agent
    system_prompt: str = ""               # prompt système
    max_tokens: int = 4096               # limite par défaut (surcharger si besoin)
    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self._client = AsyncAnthropic()
    async def call_llm(self, user_message: str, *, max_tokens: int | None = None) -> str:
        # Méthode standard — élimine le boilerplate (system prompt + model auto-injectés)
    async def run(self, **kwargs) -> str:  # DOIT retourner du markdown
```

**Path traversal protection** — tout CLI utilisant des chemins fichiers doit passer par :
- `safe_read_path(file_arg)` → valide + résout un chemin en lecture (lève `ValueError` si hors CWD)
- `safe_write_path(path_arg)` → idem pour l'écriture

Logger racine : `logging.getLogger("agents")` — les sous-agents utilisent `logging.getLogger("agents.mon_agent")`.

**Principaux entry points :**

| Module | Rôle |
| --- | --- |
| `agents.content_factory.cli` | Pipeline complet : strategy → article → audit → cluster (`brain.bat`) |
| `agents.article_pipeline.cli` | Pipeline séquentiel 5-7 agents (Writer→Auditor→Editor→LLM→Meta) |
| `agents.schoolswp_brain.cli` | Agent stratégique (4 modes : seo-writer, plugin-comparator, wp-architect, automation-consultant) |
| `agents.publish_ready.cli` | 4 audits parallèles (SEO + LLM + Conversion + Topical) |
| `agents.strategic_brain.cli` | Orchestrateur décisionnel → commandes CLI prêtes |
| `agents.seo_auditor.cli` | Audit SEO /100 + `--fix` auto-correct |

**Publish Score (publish_ready.cli) :**

```text
Publish Score = SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20
```

Seuils : ≥90 → publication immédiate | 80-89 → ajustements mineurs | 70-79 → révision ciblée | <70 → réécriture

**Pipeline stratégique recommandé (exécuter dans l'ordre) :**

```bash
.venv/Scripts/python -m agents.knowledge_graph.cli            # → content/docs/knowledge-graph.md
.venv/Scripts/python -m agents.pillar_authority.cli --all     # → audit/piliers/summary.md
.venv/Scripts/python -m agents.cocon_builder.cli --pillar lms # → cocons/lms.md
.venv/Scripts/python -m agents.roi_editorial_plan.cli         # → plans/plan-roi.md
.venv/Scripts/python -m agents.strategic_brain.cli            # → decisions/brain-report.md
```

**Logs** : `logs/agents.log` (rotation 10 MB × 5 fichiers). Format : `YYYY-MM-DDTHH:MM:SS | LEVEL | logger | message`. DEBUG → fichier uniquement, WARNING+ → console + fichier.

**Fichiers intermédiaires pipeline** (`--save-dir`) : `strategy.md` → `v1.md` → `audit-seo.md` → `audit-llm.md` → `audit-conversion.md` → `audit-topical.md` → `v2.md` → `cluster.md` → `meta.md`. Pour `article_pipeline` : `v1.md` → `audit.md` → `serp-sim.md` → `v2.md` → `v3.md` → `ner.json` → `meta.md`.

## Workspace Structure

```text
projects/schoolswp/
├── agents/             # Namespace package (.env only — CLIs use sys.path.insert, conftest registers sys.modules)
├── core/
│   ├── agents-md/      # Agent system prompts as .md files (INDEX.md is the index)
│   ├── agents-py/      # Python agent source files (base.py + one subdir per agent)
│   ├── playbooks/      # Strategic playbooks (.md)
│   ├── skills/         # Local Claude Code skills
│   └── tasks/          # Active mission (todo.md) and lessons (lessons.md)
├── systems/
│   ├── n8n/            # n8n rules doc and config
│   └── workflows/      # n8n workflow JSON exports
├── apps/               # vscode-agent-visual (active), brand-reveal, telegram-bot, claude-telegram-poc, video-marketing, _archive/, _prototypes/
├── content/
│   ├── articles/       # Generated articles (save-dir outputs from pipeline)
│   ├── docs/           # Brand rules, SEO reports
│   └── pages/          # WordPress pages draft
├── tools/
│   └── scripts/        # Python utility scripts, gdrive tools
├── infra/              # Docker, Prometheus config
├── data/               # Reports, artifacts, outputs
├── tests/              # pytest tests (asyncio_mode = auto)
├── *.py (root)         # 9 scripts n8n one-shot (fix_workflow.py, patch_*.py) — maintenance workflows via API
└── .claude/            # Claude Code rules, commands, local skills
```

## schoolsWP OS — Strategic Layers (apply in order)

When reasoning about schoolsWP strategy, always work through these layers in sequence:

1. Positionnement
2. Intent SEO
3. Architecture WordPress
4. Automation
5. Monétisation
6. Autorité

## Branding

→ Détails dans `.claude/rules/branding.md` (chargé auto quand tu travailles dans `content/`)

Résumé : toujours `schoolsWP`, tutoiement, mots interdits. Source de vérité : `content/docs/BRAND_RULES.md`

## Code Conventions

**Python** — PEP 8, 4 espaces, ruff (rules: E/F/W/I, ignore E501), Python 3.11+, line-length 120

**JSON/JS** — 2 espaces, pas de trailing comma, UTF-8, LF

**Shell** — shebang `#!/usr/bin/env bash`, 2 espaces

**Fichiers** — kebab-case (jamais camelCase)

**Commits** — conventionnel en anglais : `feat:`, `fix:`, `chore:`, `docs:`

**Branches** — `feature/*`, `fix/*`, `chore/*` depuis `main`

## Scoped Rules (`.claude/rules/`)

Regles chargees automatiquement selon le dossier de travail :

| Fichier | Scope | Contenu |
| --- | --- | --- |
| `python-agents.md` | `core/agents-py/**` | Architecture agents, modules CLI, pipeline |
| `n8n-integration.md` | `systems/**` | typeVersions, contraintes Code node, nommage |
| `branding.md` | `content/**` | Nom, ton, mots interdits |
| `tools-services.md` | `tools/**` | Scripts utilitaires, services |

## n8n Integration

→ Détails complets dans `.claude/rules/n8n-integration.md` (chargé auto quand tu travailles dans `systems/`)

Résumé : instance `https://schoolswp-n8n.wp1.host`, MCP dans `.mcp.json`, ne jamais modifier les JSON a la main. typeVersions, contraintes Code node et nommage dans la rule.

## Tools & Services

→ Détails dans `.claude/rules/tools-services.md` (chargé auto quand tu travailles dans `tools/`)

## Pre-commit Hooks

Installation (une seule fois) : `pip install pre-commit && pre-commit install`

Hooks exécutés dans l'ordre : 1. `secrets-scan` (détecte clés/tokens), 2. `ruff` lint + format (`--fix` auto-repair), 3. `pip-audit` (vulnérabilités dépendances). Mise à jour : `pre-commit autoupdate`.

## CI (GitHub Actions)

Workflow : `.github/workflows/ci.yml` — lance sur push/PR vers `main`.

3 checks : `ruff check` (lint) → `ruff format --check` → `pytest tests/ -v --cov --cov-report=term-missing`. Pas de deploy, pas de secrets — juste la barriere anti-regression. CI utilise `uv run` (pas `.venv/Scripts/python`). Coverage minimum : `fail_under = 40`, source `core/agents-py`, omit `*/cli.py`, `*/brain_lite_cli.py`, `*/__main__.py` (configuré dans `pyproject.toml`).

## Security

- `.env` jamais versionné. `.mcp.json` dans `.gitignore` — utiliser `.mcp.json.example` comme template.
- Credentials n8n sanitisés avant export.
- Vérifier `.gitignore` avant tout commit.
- Dependabot configuré (`.github/dependabot.yml`) : mises à jour pip + npm hebdomadaires (lundi), max 5 PRs.

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

| Document | Contenu |
| --- | --- |
| `schoolswp-auto-router.md` | 6 modes opérationnels (Architect, Strategist, Producer, Transformer, Experiment, Optimizer) |
| `schoolswp-seo-engine.md` | Philosophie SEO (pillar pages, clusters, optimisation continue) |
| `schoolswp-content-engine.md` | Système de production et repurposing de contenu |
| `schoolswp-authority-engine.md` | Construction d'autorité (3 niveaux : pilier, cluster, satellite) |
| `schoolswp-gsc-radar.md` | Analyse d'opportunités GSC |
| `schoolswp-seo-ops-brain.md` | SEO opérationnel (schéma, scoring, prompts internes) |
| `schoolswp-seo-agent.md` | Agent SEO automatisé (3 boucles : Radar, Ops, Publishing) |
| `schoolswp-authority-domination-24m.md` | Plan stratégique 24 mois (4 piliers) |

### Sub-CLAUDE.md (chargés automatiquement selon le dossier actif)

- `core/agents-py/CLAUDE.md` — conventions Python agents, patterns, création d'agent
- `systems/n8n/CLAUDE.md` — typeVersions confirmées, nommage, contraintes Code node

### Contribution

- `CONTRIBUTING.md` — guidelines de contribution (structure PR, conventions, checklist)

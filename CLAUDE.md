# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Trois systèmes d'agents distincts, ne pas confondre :**
>
> - `core/agents-py/` — scripts Python (28 modules CLI, lancés via `.venv/Scripts/python -m agents.<module>.cli`)
> - `.claude/agents/*.md` — sub-agents Claude Code projet (27 spécialistes dispatchés via Agent tool, table « Project Sub-Agents » plus bas)
> - `schoolswp-agents/` — fleet de 4 instances Claude Code autonomes (process séparé), chacune avec son propre `CLAUDE.md`

## Data Safety — Suppressions

Interdiction totale d'utiliser rm (dont rm -rf), sudo, ou toute commande destructrice. trash-cli n'est pas installé sur cette machine Windows.

Pour supprimer : demander confirmation utilisateur, puis suppression manuelle via Explorer (Corbeille Windows). Script PowerShell Remove-Item toléré uniquement pour artefacts reproductibles (caches, node_modules, builds) après feu vert explicite. Pour les skills archivés, suivre le pattern mémorisé dans feedback_skill_archival.md (gut YAML + bandeau + delete manuel).

## Setup initial

```bash
pip install uv && uv sync                    # Python deps (une seule fois)
cp .env.example .env                         # puis remplir les clés
cp .mcp.json.example .mcp.json               # puis remplir les clés API MCP
npm install                                   # JS deps (optionnel)
```

Si `uv` n'est pas dans le PATH : `& "$env:APPDATA\Python\Python313\Scripts\uv.exe" sync`

Variables clés `.env` : `ANTHROPIC_API_KEY` (obligatoire), `MODEL_WRITER` (défaut: `claude-sonnet-4-6`), `FIRECRAWL_API_KEY`, `N8N_*`, `GOOGLE_WORKSPACE_CLI_CLIENT_ID/SECRET`. Recherche : `agents/.env` → `.env` → `multi-agent-system/.env`.

## Session Start

Avant toute tâche, lire dans cet ordre :

1. `core/tasks/todo.md` — état de la mission en cours
2. `core/tasks/lessons.md` — leçons documentées (obligatoire avant tout refactoring d'agents)
3. `CLAUDE.local.md` — contraintes temporaires de session (s'il contient quelque chose)

**Garde-fous comportementaux** : `.claude/rules/karpathy-principles.md` — 4 principes (think before coding, simplicity first, surgical changes, goal-driven execution). Pas auto-chargés via `paths:` ; à consulter avant tout refactoring ou tâche d'édition non-triviale.

## Data Knowledge

Before answering or searching the web, always check the Obsidian wiki located at `D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP`, especially the schoolsWP knowledge base and Claude Code bridge documentation.

## Python Environment

Projet `schoolswp-agents` v0.1.0 — Python `>=3.11`. Gestionnaire : `uv` (lock file `uv.lock`). Synchroniser : `uv sync` depuis la racine projet.

Dépendances principales : `anthropic>=0.49.0`, `python-dotenv>=1.0.0`. Dev : `pytest>=8.0`, `pytest-asyncio>=0.24`.

**Venv** : `.venv/Scripts/python` — seul venv actif. Sur Windows + Bash, `activate` ne persiste pas — utiliser le chemin complet.

## Key Commands

**Content factory (pipeline complet — génération + audit + cluster) :**

```bash
# Via .bat (raccourci Windows — appelle .venv\Scripts\python)
brain.bat --keyword "lms wordpress rentable" --intent décisionnelle --pillar LMS

# Ou directement via Python
.venv/Scripts/python -m agents.content_factory.cli --keyword "lms wordpress rentable" --intent décisionnelle --pillar LMS
.venv/Scripts/python -m agents.content_factory.cli --keyword "tutor lms vs learndash" --intent comparative --pillar LMS --include-ner
.venv/Scripts/python -m agents.content_factory.cli --file content/articles/lms/v3.md --kw "lms wordpress" --intent décisionnelle
```

Flags : `--keyword` | `--file` + `--kw`, `--intent`, `--pillar`, `--objective`, `--include-serp`, `--include-ner`, `--no-links`, `--no-cluster`, `--force`, `--save-dir`, `--model`

- `--intent` : `informationnelle` | `commerciale` | `décisionnelle` | `comparative` | `navigationnelle`
- `--pillar` : `LMS` | `CRM` | `SEO` | `automatisation` | `ecommerce` | `freelance` | `formation`
- `--objective` : `email` | `affiliation` | `formation` | `offre`

**Brain Lite (pipeline 5 étapes, sans NER/SERP) :**

```bash
brain-lite.bat --keyword "fluentcrm avis" --intent informationnelle --pilier crm
# Ou: .venv/Scripts/python -m agents.article_pipeline.brain_lite_cli --keyword "fluentcrm avis" --intent informationnelle --pilier crm
```

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

**Claude Code hooks actifs** (.claude/hooks/, registered in .claude/settings.json) :

- ruff-check (PostToolUse Edit/Write .py) : lint + format auto
- prettier-format (PostToolUse Edit/Write JS/TS/JSON/MD/CSS/YML/HTML) : `npx prettier --write`
- dangerous-actions-blocker (PreToolUse Bash) : bloque commandes destructives (rm sur root, dd if, mkfs, fork bombs)
- output-secrets-scanner (PostToolUse) : scanne les outputs pour API keys / tokens / private keys
- prompt-injection-detector (PreToolUse Bash/Write/Edit/WebFetch) : détecte role override, delimiter injection, nested cmd. **Attention** : faux positifs fréquents quand le contenu Edit/Write contient certains mots-clés sécurité ou des extensions de fichier shell entre backticks. Voir mémoire `feedback_hook_backtick_bug.md`.

**Tests :**

```bash
.venv/Scripts/python -m pytest tests/                  # tous les tests
.venv/Scripts/python -m pytest tests/test_base.py -v   # un fichier
.venv/Scripts/python -m pytest tests/test_base.py::test_safe_read_path_rejects_traversal -v  # un test
```

pytest configuré avec `asyncio_mode = "auto"` — pas besoin de décorateur `@pytest.mark.asyncio` sur les tests async.

Fixtures (`tests/conftest.py`) : `fake_env` (mock `ANTHROPIC_API_KEY` + `MODEL_WRITER`), `mock_anthropic_client` (factory — appeler pour obtenir un mock, pas un mock direct), `tmp_article` (fichier .md dans `tmp_path`). Note import : conftest.py enregistre `core/agents-py/` comme package `agents` dans `sys.modules` — pas besoin de path hack dans les tests.

**Ajouter un test** : créer `tests/test_<module>.py`, importer la fixture `fake_env` pour mocker les env vars. Pattern type :

```python
import pytest
from agents.<module>.agent import MonAgent

async def test_mon_agent_run(fake_env):
    agent = MonAgent()
    assert agent.name == "mon-agent"
    # Ne pas appeler l'API réelle — mocker call_llm ou utiliser mock_anthropic_client
```

Coverage : voir section CI plus bas.

**Slash commands projet** (`.claude/commands/`) : `/audit`, `/audit-codebase`, `/brain-lite`, `/cocon-batch`, `/publish-repo`, `/skill-creator`, `/todo`, `/aidesigner`, `/veille`

## JS Dependencies

`package.json` : `@anthropic-ai/claude-agent-sdk`, `@mendable/firecrawl-js`, `@pinecone-database/pinecone`, `@wordpress/data`. Pas de bundler — usage direct via Node.

## Agent Architecture

Résumé : ~28 agents Python héritant de `BaseContentAgent` (async, retourne markdown). Chaque agent = `agent.py` + `cli.py`.

**Détails complets auto-chargés selon le contexte :**
- `core/agents-py/CLAUDE.md` — contrat `BaseContentAgent`, conventions CLI, création d'agent
- `.claude/rules/python-agents.md` — table complète des modules CLI, pipeline stratégique, Publish Score, namespace `agents.*`

**Multi-provider LLM** (`core/agents-py/providers/`) : abstraction via préfixe model — `"claude-sonnet-4-6"` (Anthropic, défaut), `"openai:gpt-4o"`, `"gemini:gemini-2.0-flash"`, `"deepseek:..."`, `"ollama:llama3.3:70b"`. Configurer via `MODEL_WRITER` env var ou `--model` CLI.

**Logs** : `logs/agents.log` (rotation 10 MB × 5 fichiers). Format : `YYYY-MM-DDTHH:MM:SS | LEVEL | logger | message`. DEBUG → fichier uniquement, WARNING+ → console + fichier. Logger racine `logging.getLogger("agents")`, sous-agents `logging.getLogger("agents.mon_agent")`.

**Fichiers intermédiaires pipeline** (`--save-dir`) : `strategy.md` → `v1.md` → `audit-seo.md` → `audit-llm.md` → `audit-conversion.md` → `audit-topical.md` → `v2.md` → `cluster.md` → `meta.md`. Pour `article_pipeline` : `v1.md` → `audit.md` → `serp-sim.md` → `v2.md` → `v3.md` → `ner.json` → `meta.md`.

## Workspace Structure — points non-évidents

Organisation générale découvrable via `ls`. Pièges à connaître :

- `agents/` (racine) — **namespace package vide**, pas du code. Les CLI font `sys.path.insert(0, project_root)` pour résoudre `agents.*` vers `core/agents-py/`. `agents/telegram-claude/` = sous-repo Node.js (pont Telegram, own `.git`). Les sub-agents Claude Code vivent désormais tous dans `.claude/agents/` (migration terminée).
- `core/agents-py/` — source des 28 agents Python. Distinct de `core/agents-md/` (system prompts LLM en markdown) et de `schoolswp-agents/` (fleet Claude Code autonome avec leurs propres `CLAUDE.md` + `soul.md` + mémoire).
- `apps/video-marketing/` et `apps/vscode-agent-visual/` ont leur propre `CLAUDE.md`. `apps/hyperframes/` = scaffold Remotion+FFmpeg (skills `external-hyperframes/` + `external-liveavatar/`, install npm pas encore lancé). `apps/_archive/` et `apps/_prototypes/` à ignorer.
- `tools/wp-media-upload/` — pipeline upload images articles vers schoolswp.com avec métadonnées SEO complètes (XPTitle, alt, etc.) + auto-backup + strip préfixe numérique. Commandes `cli.py init/list/upload`. Michael invoque "upload les images de l'article X", je pilote.
  - **Prérequis bloquant** : ExifTool installé via winget user scope (`AppData/Local/Programs/ExifTool/`) hors PATH système. Exporter le dossier au PATH avant chaque appel `cli.py upload` sinon "ExifTool not found".
- **Autres outils tools/** : html-to-png/ (HTML vers PNG retina + métadonnées SEO bakées), image-meta-seo/, check-tutor-docs-changes/ (watcher docs Tutor LMS), thruuu-writer/, ultimate-scraper/, mcp-servers/, wp-mu-plugins/, services/, scripts/, legacy/.
- **Apps annexes** (sans sub-CLAUDE.md) : apps/telegram-bot/, apps/claude-md-generator/, apps/brand-reveal/, apps/claude-telegram-poc/. Voir leur README respectif.
- **Racine** : 9 scripts Python one-shot (`fix_workflow.py`, `patch_*.py`) = maintenance n8n via API. `gmail-filters.xml` = config persistante réimportable dans Gmail Settings.
- `content/audits/` — système d'audits articles avec snapshots datés (créé 2026-05-07). Structure `<slug>/<YYYY-MM-DD>/` archive GSC + DataForSEO + thruuu + snapshot article actuel. Permet le diff entre dates (mesure d'impact refonte, suivi positions, traçabilité décisions). Conventions complètes : `content/audits/CONVENTIONS.md`. Index : `content/audits/_registry.md`. Distinct de `content/decisions/` (briefs/arbitrages, pilotage) et `content/articles/` (contenu publié).
- `content/decisions/` — briefs et arbitrages éditoriaux (couche pilotage en amont des articles).
- `content/inspirations/` — captures visuelles, twitter cards, drafts UI (préparation, pas du contenu publié).
- `content/calendrier-edito/` — planning éditorial.
- `content/social-series/` — séries de posts cross-plateforme.
- `content/youtube/` — pipeline YouTube OS (créé 2026-05-16). Sous-dossiers : `ideas/`, `scripts/`, `seo-packages/`, `thumbnails/`, `clips/` (avec `source/`, `exports/`, `subtitles/`, `shorts/`, `social-posts/`, `checklists/`), `publishing/`, `analytics/`. Traces de pipeline dans `runs/youtube-os/`. Géré par les 9 sub-agents `youtube-*` (voir section « Project Sub-Agents »).
- Sub-CLAUDE.md auto-chargés : `core/agents-py/`, `systems/n8n/`, `apps/video-marketing/`, `apps/vscode-agent-visual/`.

## Workspace Hygiene — anomalies connues à ne pas toucher sans investigation

- Dossier nommé littéralement avec accolades, du genre {agents,hooks,commands}/ à la racine — résidu d'une brace expansion bash qui a foiré sur Windows. À auditer puis supprimer manuellement via Explorer.
- `systems/multi-agent-system/multi-agent-system/` — sous-dossier dupliqué imbriqué, avec son propre venv et data/memory.db. Origine non documentée, vérifier avant tout cleanup.
- Doublons de chemin `content/articles/articles/lms-*/` — à fusionner avec `content/articles/lms-*/` après diff.
- 3 backups MCP à la racine : .mcp.json.bak, .mcp.json.fluent, .mcp.backup.json. Vérifier les secrets pré-rotation avant suppression. Incidents documentés 2026-04-21 et 2026-04-29.
- .coverage à la racine = artefact pytest, vérifier qu'il est bien gitignored.

**Racine polluée à nettoyer** : ~12 scripts de debug VM préfixés .tmp-vm- (extension shell), ~4 scripts Python préfixés tmp-, ~7 fichiers texte de debug (callout.txt, col_*.txt, first40.txt, orig_sample.txt, sc_block.txt, toc_ctx.txt, wp_raw_now.txt), 11 captures slide-*.png + 4 captures iter*-screenshot.png, et 8 transcripts 2026-03-28_youtube_*.md qui appartiennent à content/.

**Mémoire interne Claude Code** : le fichier MEMORY.md du workspace `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\` approche le plafond de chargement de 24 KB et est tronqué. Garder les entrées d'index sous 200 chars, déporter le détail dans les fichiers topic.

## Project Sub-Agents (`.claude/agents/`)

27 sub-agents Claude Code dispatchés via le tool Agent (parallélisable, contexte isolé). Différents de la fleet `schoolswp-agents/` (instances autonomes en process séparé) et des agents Python (`core/agents-py/`, scripts CLI).

**Catalogue complet + routing par input** : [.claude/agents/INDEX.md](.claude/agents/INDEX.md). Tables auto-régénérées par [tools/scripts/agents-registry.py](tools/scripts/agents-registry.py) (modes `--sync`, `--check`).

### Récap par groupe

| Groupe | Agents | Usage |
| --- | --- | --- |
| **Éditorial schoolsWP** | `studio`, `radar`, `pulse`, `flow`, `framework-adapter-fr`, `reddit` | Production articles, SEO, social, CRM/automation, adaptation EN→FR |
| **YouTube OS** | `youtube-os-orchestrator` + 8 sous-agents (`strategy-scout`, `script-writer`, `seo-packager`, `thumbnail-director`, `clipper`, `publisher-scheduler`, `analytics-learner`, `quality-auditor`) | Pipeline vidéo complet. Livrables dans `content/youtube/`, traces dans `runs/youtube-os/`. **Statut par défaut `REVIEW_REQUIRED`, aucune publication sans validation humaine.** |
| **Spécialistes domaine** | `seo-specialist`, `pinterest-expert`, `aidesigner-frontend`, `ads-operator`, `skoatch-publisher` | SEO technique, Pinterest, UI/landing via aidesigner, Google Ads, Skoatch + WP draft (**hors schoolswp.com**) |
| **Code review / qualité (read-only)** | `code-reviewer`, `adr-writer`, `plan-challenger`, `output-evaluator`, `silent-failure-hunter` | Review de code 5 axes, ADR Nygard, review adversariale, LLM-as-Judge, détection silent failures |
| **Infra / harness** | `harness-optimizer` | Tuning Claude Code (reliability, cost, throughput) |
| **Hors schoolsWP (perso)** | `ofm-bot` | AI influencer / OFM. Isolation stricte. |

### Règles de conflit (anti-collision)

- **`studio` vs YouTube OS** : `studio` = contenu éditorial schoolsWP générique (article, newsletter, brief, script isolé). Vidéo complète avec pipeline (script → SEO → thumbnail → publication) = `youtube-os-orchestrator`.
- **`pulse` vs `youtube-seo-packager`** : `pulse` = description/titre YouTube ponctuel. Package SEO complet (5 titres, chapitres, tags, hashtags, commentaire épinglé) en cours de pipeline = `youtube-seo-packager`.
- **`radar` vs `seo-specialist`** : `radar` = SEO éditorial schoolsWP (cocons, briefs, maillage). `seo-specialist` = SEO technique générique (schema, CWV, sitemap, audit serveur).
- **`flow` vs `pulse`** : `flow` = mécanique CRM/automation/n8n. `pulse` = copy social. Pipeline Pinterest technique (n8n + Placid + Tailwind) reste `flow`.
- **`skoatch-publisher` isolation** : **interdit sur schoolswp.com** (BRAND_RULES incompatibles). michaelkihl.fr uniquement, ou autre site WP non-schoolsWP sur demande explicite.
- **`ofm-bot` isolation** : aucun chevauchement avec schoolsWP. Pas de génération d'image standalone (utiliser nano-banana directement).
- **Quartet `studio` / `radar` / `pulse` / `flow`** : mirror la fleet `schoolswp-agents/` mais en sub-agents projet (dispatchables en parallèle dans la session courante).

## Multi-Agent Fleet (`schoolswp-agents/`)

4 agents Claude Code autonomes, chacun avec son propre `CLAUDE.md`, `soul.md` (personnalité), mémoire persistante et skills locaux. Distinct des agents Python dans `core/agents-py/` — ici ce sont des instances Claude Code complètes, pas des scripts.

| Agent | Rôle | Model |
| --- | --- | --- |
| `content-studio` | Rédaction, tutoriels, optimisation contenu | opus |
| `crm-automation` | Automatisation WordPress, CRM/LMS | opus |
| `seo-geo` | Audit SEO, GEO/AIO, maillage interne | opus |
| `social-community` | Contenu social, gestion communautaire | haiku |

Ressources partagées dans `shared/` : contacts, skills (branding, voice, stack WordPress). Les configs agents (frontmatter YAML : name, model, description) sont dans `agents/*.md` — ne pas confondre avec `core/agents-md/` qui contient les system prompts LLM des agents Python.

## schoolsWP OS — Strategic Layers (apply in order)

When reasoning about schoolsWP strategy, always work through these layers in sequence:

1. Positionnement
2. Intent SEO
3. Architecture WordPress
4. Automation
5. Monétisation
6. Autorité

## Branding

Toujours `schoolsWP` (jamais schoolswp, SchoolsWP, etc.), tutoiement, mots interdits dans `.claude/rules/branding.md`. Source de vérité : `content/docs/BRAND_RULES.md`.

## Code Conventions

**Python** — PEP 8, 4 espaces, ruff (rules: E/F/W/I, ignore E501), Python 3.11+, line-length 120

**JSON/JS** — 2 espaces, pas de trailing comma, UTF-8, LF

**Shell** — shebang `#!/usr/bin/env bash`, 2 espaces

**Fichiers** — kebab-case (jamais camelCase)

**Commits** — conventionnel en anglais : `feat:`, `fix:`, `chore:`, `docs:`

**Branches** — `feature/*`, `fix/*`, `chore/*` depuis `main`

## Session Naming

Convention pour nommer les sessions Claude Code (via `/rename`) :

- Feature : `feature/nom-court` (ex: `feature/lms-search`)
- Fix : `fix/description-bug` (ex: `fix/pipeline-timeout`)
- Audit : `audit/cible` (ex: `audit/seo-homepage`)
- Content : `content/sujet` (ex: `content/tutor-lms-guide`)

Nommer chaque session dès qu'elle dépasse 5 échanges.

## Scoped Rules (`.claude/rules/`)

Règles chargées automatiquement quand Claude **lit un fichier** correspondant au glob `paths:` du frontmatter (pas au changement de dossier courant) :

| Fichier | Glob `paths:` | Contenu |
| --- | --- | --- |
| `python-agents.md` | `core/agents-py/**` | Architecture agents, modules CLI, pipeline |
| `n8n-integration.md` | `systems/**` | typeVersions, contraintes Code node, nommage |
| `branding.md` | `content/**` | Nom, ton, mots interdits |
| `tools-services.md` | `tools/**` | Scripts utilitaires, services |

## n8n Integration

Instance : `https://schoolswp-n8n.wp1.host`. Ne jamais modifier les JSON de workflow à la main — passer par le MCP `n8n-mcp`. Détails (typeVersions, contraintes Code node, nommage) : `.claude/rules/n8n-integration.md`.

## MCP Servers

Configurés dans `.mcp.json` (gitignored, template `.mcp.json.example`) :

| Serveur | Usage |
| --- | --- |
| `n8n-mcp` | Workflows n8n (CRUD, exécutions, audit) |
| `novamira-schoolswp-com` | REST API WordPress schoolswp.com (abilities discovery + execution) |
| `wordpress-studio` | WordPress Studio CLI MCP (sites locaux, preview, push/pull WP.com, WP-CLI managé) |
| `gsc-mcp` | Google Search Console (analytics, URL inspect, sitemaps) — auth OAuth Desktop, creds dans `.credentials/gsc-client-secrets.json` (gitignored) |
| `dataforseo` | SEO/keyword data, rank tracking, SERP |
| `firecrawl` | Web scraping/search |
| `apify` | Web scraping actors marketplace |
| `wisewand` | Génération de contenu service |
| `aidesigner` | Design HTML (génération + refine, OAuth, Pro 25 $/mois = 100 crédits) |
| `nano-banana` | Image generation Gemini (modèle GA en direct, pas le `-preview` cassé) |
| `higgsfield` | Higgsfield AI (génération vidéo/image cinématique via HTTP MCP distant) |
| `heygen` | HeyGen avatars + vidéos AI (HTTP MCP officiel `mcp.heygen.com/mcp/v1/`, OAuth, crédits du plan) |
| `chrome-devtools` | Inspection navigateur (Lighthouse, console, network) |
| `claude-code-guide` | Doc Claude Code locale (search_guide, search_official_docs) |
| `fluentcrm` | FluentCRM (contacts, listes, tags, campagnes, smart links) |
| `discord` | Discord (messages, channels, webhooks, forum posts) |
| `github` | GitHub API |
| `rapidapi-{linkedin,twitter,instagram,youtube}` | Endpoints sociaux RapidAPI |

**Stockage des secrets** : les clés API MCP vivent dans `.claude/settings.local.json` (bloc `env`, gitignored), **jamais dans `.env`** ni hardcodées dans `.mcp.json`. `.env` est pour les variables des scripts Python (`ANTHROPIC_API_KEY`, etc.). `claude mcp list` peut fuiter ces valeurs dans les transcripts JSONL — incident RapidAPI 2026-04-21 rotaté.

## Pre-commit Hooks

Installation (une seule fois) : `pip install pre-commit && pre-commit install`

Hooks exécutés dans l'ordre : 1. `secrets-scan` (détecte clés/tokens), 2. `ruff` lint + format (`--fix` auto-repair), 3. `pip-audit` (vulnérabilités dépendances). Mise à jour : `pre-commit autoupdate`.

## CI (GitHub Actions)

Workflow : `.github/workflows/ci.yml` — lance sur push/PR vers `main`.

3 checks : `ruff check` (lint) → `ruff format --check` → `pytest tests/ -v --cov --cov-report=term-missing`. Pas de deploy, pas de secrets — juste la barriere anti-regression. CI utilise `uv run` (pas `.venv/Scripts/python`). Coverage minimum : `fail_under = 50`, source `core/agents-py`, omit `*/cli.py`, `*/brain_lite_cli.py`, `*/__main__.py` (configuré dans `pyproject.toml`).

## Security

- `.env` jamais versionné. `.mcp.json` dans `.gitignore` — utiliser `.mcp.json.example` comme template.
- Credentials n8n sanitisés avant export.
- Vérifier `.gitignore` avant tout commit.
- Dependabot configuré (`.github/dependabot.yml`) : mises à jour pip + npm hebdomadaires (lundi), max 5 PRs.

## Execution Protocol

1. Plan dans `core/tasks/todo.md` (tâche courante). Pour plans multi-étapes, créer `core/tasks/plans/<nom>.md` (le dossier sera créé à la demande).
2. Exécution pas à pas
3. Vérification
4. Lessons dans `core/tasks/lessons.md`

**Lessons clés** : path traversal, secrets gitignore fortress, venv Windows = chemin complet, signatures agents = grep tous les appelants. Liste complète et à jour dans `core/tasks/lessons.md` — à lire avant tout refactoring d'agents.

## Skills Registry

**Source unique** : tous les skills Claude Code sont dans `.claude/skills/` (projet schoolsWP), organisés par catégorie. Consolidation effectuée le 2026-04-17 — plus aucun skill au niveau workspace, utilisateur global ou `.agents/skills/`.

> Compte exact : voir `INDEX.md` ou lancer `skills_registry.py --sync`. Les nombres dérivent vite — ne pas les figer ici.

**Sync registre vers Google Sheets :**

```bash
.venv/Scripts/python .claude/skills/.registry/skills_registry.py --sync
```

**INDEX des skills projet** : `.claude/skills/INDEX.md` (catalogue + tables de routing complètes)

**Skills externes** (invocation manuelle uniquement, ne pas auto-déclencher) :

- `external-antigravity/` (16 skills, 2026-04-18) — sélection filtrée WP/SEO/GEO-AEO/perf/conversion. 4 doublons isolés dans `_to-delete/`.
- `external-cc-design/` — design HTML haute fidélité (slide decks, prototypes, landing). Brand strict, 0 $. Préférer aidesigner pour exploration (T0), cc-design pour prod finale (T1).
- `external-design-systems/` (73 DESIGN.md, 2026-04-30) — bibliothèque brand-grade (Stripe, Notion, Linear, Cursor, Supabase, Anthropic, Vercel, Figma, Resend, Cal.com, Mistral, etc.). Source : nexu-io/open-design (Apache 2.0, fork pré-stubbing de awesome-design-md). Référence éducative + brief brand pour aidesigner/cc-design + modèle pour formaliser un futur DESIGN.md schoolsWP. Pas de skill de création — voir `external-design-systems/INDEX.md` pour le routing par cas d'usage.
- `external-open-design/` (3 skills HTML, 2026-04-30) — `email-marketing` (newsletter featured), `pricing-page` (offres tiers comparatif + FAQ), `docs-page` (mockup doc 3 colonnes). Source : nexu-io/open-design (Apache 2.0). Frontmatter modifié pour anti-conflit avec skills schoolsWP existants (lead-magnet-schoolswp, mini-offre-page-de-vente, etc.). Pattern d'invocation : charger un DESIGN.md (external-design-systems ou BRAND_RULES.md) puis lire le sous-skill. Voir `external-open-design/INDEX.md` pour le routing.
- `external-video-use/` (2026-04-27) — édition vidéo conversationnelle (transcribe, cut, color grade, subtitles). Sous-clone gitignored, deps dans venv racine.
- `external-ecc/` — gateguard fact-forcing pre-edit (1 skill cherry-picked, 4 candidats rejetés).
- `external-hyperframes/` + `external-liveavatar/` — Remotion + avatars AI (FFmpeg requis).
- `external-heygen/` — skills HeyGen (avatars + vidéos AI). Pattern de prod confirmé 2026-05-06 : lipsync via audioUrl externe (digital_twin + audio mp3/wav HTTPS public, sans voiceId/script). Voix clone HeyGen cassée API → ElevenLabs en amont.
- `external-obsidian/` — skill `defuddle` cherry-picked depuis kepano/obsidian-skills (MIT, 2026-05-04). Préférer à WebFetch/firecrawl pour veille article rapide. CLI npm 0.18.1 installé global. 4 autres skills upstream skipped (pas de vault Obsidian côté projet).
- `external-astra-spectra/` (2026-05-20) : skill cloné depuis github.com/wpformation/claude-skill-astra-spectra (MIT, Fabrice Ducarme). Base de connaissance Spectra (48 blocs Gutenberg) pour générer ou refondre des pages WordPress. Hors stack schoolsWP (Kadence) : invocation manuelle uniquement, frontmatter modifié anti auto-trigger. Conservé comme ressource pour une future formation ou un tutoriel WordPress.

Lock cohérence : `.claude/skills/.registry/lock_external_skills.py` génère `external-skills-lock.json` pour les 35 skills `external-*`. Routine reval Q3 2026.

### Routing — quel skill pour quelle demande

Tables de routing complètes (production éditoriale, SEO/cocons, landing/email/conversion, YouTube, social, branding) : voir [.claude/skills/INDEX.md#routing-priority](.claude/skills/INDEX.md). Les **règles de conflit** ci-dessous restent ici car elles guident le déclenchement automatique.

**Règles de conflit** :

- `schoolswp-content-studio` ne doit PAS se déclencher sur une demande d'article SEO long — c'est `schoolswp-article-workflow` ou `thruuu-writer`.
- `cocon-map-schoolswp` ne doit PAS se déclencher sur une demande de UN cluster pour UN mot-clé — c'est `cluster-cocon-automatique`.
- `brain-autonome` arbitre à l'échelle du SITE (tous cocons confondus). `cocon-roi-prioritization` priorise DANS UN cocon donné. Ne pas les confondre.
- `landing-page-factory` (affiliation tiers) vs `mini-offre-page-de-vente` (offre propre) vs `lead-magnet-schoolswp` (capture newsletter) : 3 types de pages distincts, ne pas confondre.
- `plugin-email-sequence` (découverte plugin par affiliation) vs séquence welcome lead magnet (→ `lead-magnet-schoolswp`) vs recyclage email reçu (→ `email-to-content`) : rôles opposés malgré le thème email commun.
- `schoolswp-youtube-studio` (vidéo longue 16:9) vs `youtube-shorts-schoolswp` (Shorts 9:16) : formats distincts, ne pas confondre. `schoolswp-youtube-studio` produit un BRIEF thumbnail, pas le design final — handoff vers `thumbnail-strategist` pour la conception visuelle.
- `youtube-omnichannel-engine` pilote / score / distribue, il ne produit pas de contenu vidéo brut.
- `social-media-manager` = orchestration + adaptation + publication multi-plateformes (via Blotato). La CRÉATION de copy originale passe par les skills plateforme : `linkedin` pour LinkedIn, `instagram-strategy` pour Instagram. NE PAS l'utiliser comme skill par défaut pour "fais-moi un post".
- `pinterest-strategy` (stratégie / pilotage / SEO / boards) vs `pinterest-pipeline` (exécution automatisée brief → Canva → API → analytics) : rôles complémentaires, ne pas confondre.
- `clairtexte` (correction LANGUE : grammaire/orthographe/ponctuation) vs `branding` (audit VOIX : ton/clarté/densité/pédagogie) : 2 hygiénies distinctes, ne pas confondre. `clairtexte` ne touche pas au style ; `branding` ne corrige pas les fautes de langue.
- `branding` est strictement en mode `check` (audit). Toute création de contenu passe par les skills plateforme/format spécialisés — `branding` ne draft, ne rewrite, ne repurpose pas.
- `apps/video-marketing/` (Remotion / React, structurelle) vs `apps/hyperframes/` (HyperFrames / HTML+GSAP, courte durée) : Remotion pour vidéos multi-scènes, cours formation TutorLMS, governance theme.ts/texts.ts. HyperFrames pour intros ≤30s, overlays sociaux, recyclage article→vidéo, shader transitions. **Défaut = Remotion** si les deux peuvent faire le job. HyperFrames seulement si l'usage le justifie (intro courte, overlay, transition shader). Skills `/hyperframes`, `/hyperframes-cli`, `/gsap` réservés aux compositions dans `apps/hyperframes/`.

**Import externe `external-antigravity/` (2026-04-18)** :

16 skills importés depuis `sickn33/antigravity-awesome-skills` dans `.claude/skills/external-antigravity/` — sélection filtrée WordPress / SEO / GEO-AEO / perf / conversion / contenu. Les 4 doublons détectés (`form-cro`, `n8n-code-javascript`, `n8n-mcp-tools-expert`, `n8n-workflow-patterns`) sont isolés dans `external-antigravity/_to-delete/` et exclus automatiquement du scan registry (règle d'exclusion `_to-delete` dans `skills_registry.py`). À supprimer manuellement via Explorer quand tu seras prêt.

Règles de conflit spécifiques aux skills importés :

- `email-sequence` (antigravity, nurturing générique VO anglaise) vs `plugin-email-sequence` (schoolsWP, découverte plugin par affiliation FR) vs `email-to-content` (recyclage email reçu). 3 intentions distinctes.
- `seo-aeo-internal-linking` (antigravity) ne doit PAS se déclencher automatiquement — doublonne Link Whisper + radar agent schoolsWP. Invocation manuelle uniquement comme outil de reasoning stratégique.
- `wordpress-centric-high-seo-optimized-blogwriting-skill` (antigravity, VO anglaise) ne doit PAS se déclencher sur les demandes d'article SEO long FR — c'est `schoolswp-article-workflow` ou `thruuu-writer`. Le skill antigravity reste utile pour inspiration structurelle (truth boxes, WP-ready output).
- `copywriting-psychologist` (antigravity, persuasion scientifique EN) vs skills copy internes : pas de collision, s'active pour copy conversion psychologique référencée (JTBD, ELM). Peut cohabiter avec `branding` (check) et `clairtexte` (langue).

**Skills archivés** (invocation manuelle uniquement, YAML gutté) : liste + raisons + dates dans [.claude/skills/_archive/INDEX.md](.claude/skills/_archive/INDEX.md). Toute nouvelle archive = ligne ajoutée là-bas, pas ici.

## Passerelle Obsidian

Canal contrôlé entre le projet schoolsWP et le vault Obsidian schoolsWP (`D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\`). Pas une synchronisation.

**Asymétrie d'autorité :**

- Vault Obsidian = autorité finale de la **mémoire longue validée**.
- Projet Claude Code = autorité finale de l'**opérationnel**.
- Mémoire interne Claude Code (`C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\`) = **technique**, ne remplace pas le wiki, n'a pas autorité sur lui.

**Localisation passerelle** :

- Côté projet : [`obsidian-bridge/`](obsidian-bridge/README.md) (README, SOP, templates, `.gitignore`)
- Côté vault : `00_systeme/claude-code-bridge/` (5 sous-dossiers + README + SOP)

**Ce que Claude Code peut lire dans le vault** :

- `claude.md`, `index.md`, `log.md` à la racine du vault (charte, index, journal)
- `00_systeme/claude-code-bridge/inbox-vers-claude/**`
- `07_projects/schoolswp/**` (uniquement si demandé explicitement, lecture seule)
- `01_inbox/**` (uniquement si demandé)

**Ce que Claude Code peut écrire dans le vault** :

- **Principalement** `00_systeme/claude-code-bridge/outbox-depuis-claude/**` (ou `decisions-proposees/`, `syntheses-proposees/`) - Markdown propre avec frontmatter standard.
- **Exception consolidation post-transport (SOP v1.1+)** : Claude peut modifier `08_sources/<sub-zone>/` (rename index/synthèse, archivage version périmée dans `_normalisation/`, mise à jour d'index existant) **uniquement après transport humain effectif** et sans toucher au contenu source-brute déjà transporté.
- **Append au log.md du vault** : autorisé uniquement pour tracer les actions de l'exception ci-dessus (append-only strict, jamais modifier les entrées passées).
- **Jamais** dans les autres zones stables : `02_drafts/`, `03_synthesis/`, `04_memory/`, `05_sop/`, `06_decisions/`, `07_projects/`, `09_archive/`.

**Ce que Claude Code ne doit jamais toucher** :

- `.obsidian/` (config Obsidian)
- `claude.md`, `index.md` du vault (gouvernance, modifs Michaël uniquement)
- Les entrées passées de `log.md` (append-only strict, modification interdite même par Claude)
- Le contenu source-brute déjà transporté dans `08_sources/<sub-zone>/<videos|docs|...>/` (intouchable, modifs par Michaël uniquement)
- Les fiches d'identité schoolsWP stabilisées en phase 2 et 3 (mission, audience, positionnement, voix-editoriale, piliers)

**Règle absolue du vault** : aucune modification durable du wiki sans entrée correspondante dans `log.md` du vault. Toute promotion d'un draft `outbox-depuis-claude/` vers une zone stable passe par Michaël (validation L0). Les actions de consolidation post-transport (exception SOP 8.2) suivent la même règle : Claude doit appender l'entrée log lui-même.

**Procédure complète** : [obsidian-bridge/SOP-claude-obsidian-bridge.md](obsidian-bridge/SOP-claude-obsidian-bridge.md) (v1.1, MAJ 2026-05-05 avec exception 8.2 et 8.3).

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
- `apps/video-marketing/CLAUDE.md` — Remotion video system, theme.ts/texts.ts governance, QA protocol
- `apps/vscode-agent-visual/CLAUDE.md` — VS Code extension architecture, postMessage IPC, Canvas animation

### Contribution

- `CONTRIBUTING.md` — guidelines de contribution (structure PR, conventions, checklist)

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

schoolsWP OS: a Python AI content factory for the schoolsWP WordPress ecosystem (SEO content production, agents, n8n automations, monetization). This directory is its own git repo (root = `projects/schoolswp/`). Default content language: **French** (governance docs and code comments may be FR or EN).

## Layered context (read the right layer, do not duplicate)

Detail lives in scoped files, not here. This file is the big-picture map; defer to the layers below for specifics.

- .claude/rules/python-agents.md - agent architecture, the full module/CLI table, the strategic pipeline, the Publish Score formula. Read it before working in core/agents-py/.
- `core/agents-py/CLAUDE.md` - per-agent conventions (agent.py + cli.py pattern, argparse rules, pipeline dataclasses).
- `.claude/rules/n8n-integration.md` - n8n typeVersions, Code node task-runner constraints, workflow/credential naming. Read before touching `systems/n8n/` or `systems/workflows/`.
- `.claude/rules/branding.md` + `content/docs/BRAND_RULES.md` + `content/docs/BRAND_CHECKLIST.md` - full branding source of truth for `content/**`.
- `.claude/rules/tools-services.md` - what each script/service in `tools/` does (Drive scripts, MCP servers, image/PDF/upload tooling).
- `.claude/rules/karpathy-principles.md` - execution discipline (think before coding, simplicity, surgical changes).
- The workspace root `../../CLAUDE.md` plus `docs/standards-code.md` and `docs/runbooks-operationnels.md` govern cross-project standards.

## Commands

All commands run from `projects/schoolswp/` using the project venv (interpreter path shown in the block below; Windows).

```bash
# Setup
pip install uv && uv sync
cp .env.example .env && cp .mcp.json.example .mcp.json   # both are gitignored

# Lint + format (matches CI: .github/workflows/ci.yml)
.venv/Scripts/python -m ruff check core/agents-py/
.venv/Scripts/python -m ruff format --check core/agents-py/

# Tests
.venv/Scripts/python -m pytest tests/ -v                            # full suite
.venv/Scripts/python -m pytest tests/test_seo_auditor_agent.py -v   # single file
.venv/Scripts/python -m pytest tests/ -k thruuu -v                  # by keyword
.venv/Scripts/python -m pytest tests/ --cov --cov-report=term-missing  # coverage (fail_under=50)

# Content pipelines (Windows .bat wrappers around agents.* CLIs)
brain.bat --keyword "lms wordpress" --intent decisionnelle --pillar LMS   # full factory: strategy -> article -> 4 audits -> cluster
brain-lite.bat --keyword "fluentcrm avis" --intent informationnelle       # lighter 5-step pipeline

# Single agent (every agent exposes a CLI; --model and --output are universal)
.venv/Scripts/python -m agents.<module>.cli [args]
.venv/Scripts/python -m agents.seo_auditor.cli content/articles/x.md --kw "lms wordpress" --fix
```

Note: `audit.ps1` at the root is an unrelated disk audit, not the content audit. For the publish audit use the /audit skill or `agents.publish_ready.cli`. `planner.bat` and `publisher.bat` drive the YouTube brief-publisher skill scripts.

CI runs on push/PR to `main`: uv sync, then ruff check, ruff format check, then pytest with coverage. Pre-commit hooks (mandatory, see `.pre-commit-config.yaml`): a secrets scan, ruff (lint + format), and pip-audit. Use the no-verify flag only when a hook itself is broken, and document why in the commit message.

## Architecture (big picture)

**Agents are the core.** Two complementary layers per agent capability:

- `core/agents-md/` - the system prompts (one Markdown file per agent; index in `core/agents-md/INDEX.md`).
- `core/agents-py/` - the implementations. Every agent is a subfolder with `agent.py` (a class extending `BaseContentAgent`) and `cli.py` (argparse entry point).

**The agents.\* namespace trick:** the `agents/` folder at the repo root is an _empty namespace package_; the actual code lives in `core/agents-py/`. Each CLI does `sys.path.insert(0, project_root)` so that `from agents.seo_auditor.agent import ...` resolves into `core/agents-py/`. When adding code, put it under `core/agents-py/`, never under the root `agents/`.

**`BaseContentAgent` (`core/agents-py/base.py`)** is the shared base every agent extends:

- async, `run(**kwargs)` returns `str` (markdown), never JSON;
- model auto-resolved via `resolve_provider()` (env `MODEL_WRITER`, default `claude-sonnet-4-6`; multi-provider support via `core/agents-py/providers/`);
- the API key is auto-loaded from `.env` (search order: `agents/.env` -> repo root `.env` -> `multi-agent-system/.env`);
- rotating file logging to `logs/agents.log`;
- path-traversal guards `safe_read_path()` / `safe_write_path()` - use these for any file argument coming from a CLI.

**Pipelines compose agents.** `brain.bat` -> `agents.content_factory.cli` runs strategy -> article -> 4 parallel audits -> semantic cluster. Independent steps fan out with `asyncio.gather`; results are carried in dataclasses (`PipelineResult`, `WorkflowResult`). The four audit axes (SEO, LLM citability, conversion, topical authority) combine into a weighted Publish Score. The exact thresholds, the formula, and the authoritative table of every agent module and its CLI live in the scoped agent rules file referenced under Layered context above. Consult it instead of re-deriving from the code.

**Where things live:**

- `core/` - the OS (agents-md, agents-py, playbooks, tasks, skills).
- `content/` - editorial output and the brand source of truth (articles, formations, audits, slides, docs/BRAND_RULES.md, etc.).
- `systems/` - n8n framework and exported workflows, multi-agent-system, pinterest/linkedin pipelines, security.
- `tools/` - utility scripts and standalone services (MCP servers, image/PDF tooling, WP media upload, Drive scripts).
- `infra/`, `data/`, `logs/` - config, artifacts, runtime logs.
- The repo root holds many one-shot / scratch files (`.tmp-*`, `patch_*.py`, `fix_workflow.py`). Treat these as disposable and do not re-run without checking relevance (see `.claude/rules/tools-services.md`).

**MCP servers** are configured in `.mcp.json` (gitignored; template `.mcp.json.example`). Do not edit `.mcp.json` casually. The Novamira MCP adapter is the primary path to schoolswp.com WordPress; the `agents.*` pipelines are LLM-only and do not publish.

## Conventions

- Python: PEP 8, 4-space indent, line-length 120, ruff (`E,F,W,I`, `E501` ignored). Filenames kebab-case, never camelCase.
- Commits: Conventional, in English (`feat:`, `fix:`, `chore:`, `docs:`, `security:`, `refactor:`, `test:`). Never commit directly to `main`; branch first (`feature/*`, `fix/*`, `chore/*`, `docs/*`). One working branch at a time. See `CONTRIBUTING.md`.
- Never commit secrets: `.env`, `.mcp.json`, `settings.local.json` stay gitignored.
- n8n: never hand-edit workflow JSON; go through the MCP or the n8n UI, then export to `systems/workflows/workflows/`.

## Core Guidelines

- **TT5 & Gutenberg First**: Always prioritize native block editor controls, templates, and patterns over custom code. Use `theme.json` as the design system.
- **schoolsWP Naming Rule**: Always write the brand name exactly as **schoolsWP** (never _SchoolsWP_, _schoolswp_, etc.), even at the start of a sentence.
- **Typographic Restriction**: Never use em dashes or en dashes. Use simple hyphens (`-`), colons, periods, or parentheses instead.
- **Tone Rule**: For French content, always use **"tu"** (tutoiement) and write in a direct, pedagogical, human tone (avoid "nous", "notre", "nos", etc.).
- **Langue de la documentation** : Toute la documentation de suivi (action logs, synthèses d'audit, README d'audits, etc.) doit être rédigée exclusivement en Français.
- **Risk Control Tiers**: Before invoking any Level 3 tool (e.g., editing `theme.json`, deleting patterns, altering header/footer), you must present the planned changes and ask for human validation.

## Reference docs

- **Master SOP Guide**: [SOP-schoolswp-novamira.md](file:///D:/VS%20Code/CLAUDE%20CODE/projects/schoolswp/docs/SOP-schoolswp-novamira.md)
- **Gutenberg Build & Integration skill**: [schoolswp-native-builds](file:///D:/VS%20Code/CLAUDE%20CODE/projects/schoolswp/.claude/skills/schoolswp-native-builds/SKILL.md)
- **Idea to PR runbook**: `docs/runbook-idea-to-pr.md`

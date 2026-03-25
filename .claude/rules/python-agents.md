---
description: Architecture agents Python — BaseContentAgent, patterns, modules CLI
paths: ["core/agents-py/**", "agents/**"]
---

# Agent Architecture

Deux couches complémentaires :

- `core/agents-md/` — System prompts Markdown par agent (index : `core/agents-md/INDEX.md`)
- `core/agents-py/` — Implémentations Python (`agent.py` + `cli.py` par agent)

Tous les agents héritent de `BaseContentAgent` (`core/agents-py/base.py`) — async, retourne `str` (markdown). Inclut : auto-loading `.env`, logging rotatif, protection path traversal (`safe_read_path()`/`safe_write_path()`).

**Pattern d'un agent** : chaque agent = un sous-dossier avec `agent.py` (classe héritant de `BaseContentAgent`) + `cli.py` (argparse, toujours `--model` et `--output`). Certains agents ont des sous-modules (ex: `article_pipeline/` a `pipeline.py`, `writer.py`, `auditor.py`, `editor.py`).

## Modules principaux

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
| `agents.thruuu_writer.cli` | Transforme un brief thruuu (.docx) en article markdown |

## Pipeline stratégique recommandé

```bash
.venv/Scripts/python -m agents.knowledge_graph.cli            # → content/docs/knowledge-graph.md
.venv/Scripts/python -m agents.pillar_authority.cli --all     # → audit/piliers/summary.md
.venv/Scripts/python -m agents.cocon_builder.cli --pillar lms # → cocons/lms.md
.venv/Scripts/python -m agents.roi_editorial_plan.cli         # → plans/plan-roi.md
.venv/Scripts/python -m agents.strategic_brain.cli            # → decisions/brain-report.md
```

## Publish Score

```text
Score = SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20
```

Seuils : ≥90 → publication immédiate | 80-89 → ajustements mineurs | 70-79 → révision ciblée | <70 → réécriture

## Namespace `agents.*`

Chaque CLI fait `sys.path.insert(0, project_root)` au démarrage. Le dossier `agents/` à la racine est un namespace package vide — le vrai code est dans `core/agents-py/`. Python résout `from agents.seo_auditor.agent import ...` via le path manipulé.

## Conventions

Voir `core/agents-py/CLAUDE.md` pour les conventions détaillées, patterns et pipeline flags.

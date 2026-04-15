# Agents Python — Inventaire

28 modules CLI dans `core/agents-py/`. Héritent tous de `BaseContentAgent`, async, retournent du markdown.

## Pattern d'invocation

```bash
.venv/Scripts/python -m agents.<module>.cli [args]
```

Tous les agents supportent `--model` (défaut : `claude-sonnet-4-6`). Multi-provider via préfixe : `gemini:`, `openai:`, `deepseek:`, `ollama:`, ou Anthropic par défaut.

## Orchestrateurs principaux

| Module | Rôle | Raccourci |
|---|---|---|
| `content_factory` | Pipeline complet (strategy → v1 → audits → v2 → cluster → meta) | `brain.bat` |
| `article_pipeline` | Pipeline article (v1 → audit → serp-sim → v2 → v3 → ner → meta) | — |
| `article_pipeline.brain_lite_cli` | Pipeline léger 5 étapes sans NER/SERP | `brain-lite.bat` |

## Agents de rédaction

| Module | Rôle |
|---|---|
| `seo_writer` | Rédaction SEO-optimisée |
| `thruuu_writer` | Brief-to-article (format Thruuu) |
| `lms_trainer` | Contenu pédagogique LMS |
| `wp_business_teacher` | WordPress business |
| `wp_freelance_teacher` | WordPress freelance |
| `wp_premium_freelance` | WordPress freelance premium |
| `wp_teacher` | WordPress généraliste |
| `wp_digital_sales` | Sales digital WordPress |
| `wp_profit_architect` | Architecture profit WordPress |

## Agents d'audit

| Module | Rôle |
|---|---|
| `seo_auditor` | Audit SEO (avec `--fix`) |
| `publish_ready` | 4 audits parallèles + Publish Score |
| `conversion_auditor` | Audit conversion |
| `llm_seo` | Optimisation GEO/AIO (réponses LLM) |

## Agents stratégiques

| Module | Rôle |
|---|---|
| `schoolswp_brain` | Cerveau central (modes seo-writer, etc.) |
| `strategic_brain` | Stratégie générale |
| `niche_scout` | Exploration de niches |
| `cluster_architect` | Architecture de clusters sémantiques |
| `cocon_builder` | Construction de cocons |
| `pillar_authority` | Pages piliers d'autorité |
| `topical_authority` | Autorité topique |
| `plugin_comparator` | Comparaison plugins WP |
| `seo_competitor_analyst` | Analyse concurrents SEO |
| `knowledge_graph` | Graphe de connaissances |
| `kpi_dashboard` | Tableau de bord KPIs |
| `roi_editorial_plan` | Plan éditorial ROI |
| `automation_consultant` | Conseil automation |

## Publish Score

```
Publish Score = SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20
```

Seuils : ≥90 publication immédiate | 80-89 ajustements mineurs | 70-79 révision ciblée | <70 réécriture.

## Fichiers clés

- `core/agents-py/base.py` — classe `BaseContentAgent` (contrat async + `call_llm()`)
- `core/agents-py/providers/` — abstraction multi-provider LLM
- `core/agents-md/` — system prompts par agent (index dans `INDEX.md`)
- `.claude/rules/python-agents.md` — règles auto-chargées dans `core/agents-py/`

## Tests

```bash
.venv/Scripts/python -m pytest tests/              # tous
.venv/Scripts/python -m pytest tests/test_base.py -v
```

Coverage minimum : 50% (`pyproject.toml`). CLIs exclus de la couverture.

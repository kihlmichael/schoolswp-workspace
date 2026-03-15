# Plan — schoolsWP Brain Workflows (W1, W2, W3)

## Context

L'agent `SchoolswpBrainAgent` est opérationnel (mode single-shot, 1256 lignes de system prompt stratégique).
L'objectif est d'ajouter **3 workflows de production multi-étapes** orchestrés en Python, activables via CLI.
Ces workflows réutilisent l'agent brain existant pour les étapes de génération d'articles, et ajoutent des
sous-agents dédiés (focalisés) pour les étapes spécialisées (audit, analyse SERP, formats multi-canal).

Pattern de référence : `agents/article_pipeline/pipeline.py` (4 agents séquentiels → `PipelineResult` dataclass).

---

## Fichiers à créer / modifier

| Fichier | Action |
|---------|--------|
| `agents/schoolswp_brain/workflows.py` | CRÉER — constantes prompts, WorkflowResult, 5 sous-agents, 3 classes workflow |
| `agents/schoolswp_brain/workflow_cli.py` | CRÉER — CLI unifié avec 3 sous-commandes |
| `agents/schoolswp_brain/agent.py` | MODIFIER — ajouter 2 entrées à `_MODES` (ligne 1184) |
| `agents/schoolswp_brain/__init__.py` | MODIFIER — exporter les 3 workflow classes + WorkflowResult |

---

## Architecture `workflows.py`

### WorkflowResult dataclass
```python
@dataclass
class WorkflowResult:
    workflow: str   # "w1-seo-audit" | "w2-competitive-angle" | "w3-content-factory"
    keyword: str
    topic: str
    # W1
    v1: str = ""
    audit: str = ""
    v2: str = ""
    # W2
    serp_analysis: str = ""
    differentiating_angle: str = ""
    # W3
    article: str = ""
    newsletter: str = ""
    linkedin: str = ""
    twitter_thread: str = ""
    faq_aio: str = ""
    youtube_description: str = ""
    steps_completed: list[str] = field(default_factory=list)
```

### Constantes prompts (nommage)
```
W1_AUDITOR_SYSTEM    — audit V1 (4 dimensions : sémantique, exemples, FAQ, maillage)
W1_EDITOR_SYSTEM     — génère V2 à partir de V1 + audit

W2_SERP_ANALYST_SYSTEM   — analyse paysage SERP pour un mot-clé
W2_ANGLE_BUILDER_SYSTEM  — construit l'angle différenciant schoolsWP

W3_NEWSLETTER_SYSTEM  — résumé newsletter (150-250 mots)
W3_LINKEDIN_SYSTEM    — post LinkedIn (1200-1500 chars)
W3_TWITTER_SYSTEM     — thread X (5-8 tweets, format [N/8])
W3_FAQ_AIO_SYSTEM     — FAQ AIO/GEO + JSON-LD FAQPage
W3_YOUTUBE_SYSTEM     — description YouTube (150-300 mots + timestamps)
```

### Sous-agents privés (inline, module-only)
```python
_W1AuditorAgent(BaseContentAgent)   — max_tokens=2048
_W1EditorAgent(BaseContentAgent)    — max_tokens=4096
_W2SerpAnalystAgent(BaseContentAgent) — max_tokens=2048
_W2AngleBuilderAgent(BaseContentAgent) — max_tokens=1500
_W3FormatAgent(BaseContentAgent)    — max_tokens=1024 (générique, system injecté au __init__)
```

### 3 classes Workflow

**W1 — `SeoAuditWorkflow`**
```python
async def run(keyword, intent, audience, context=None, on_step=None) -> WorkflowResult
# Step 1 : SchoolswpBrainAgent(mode="seo-writer") → v1
# Step 2 : _W1AuditorAgent → audit
# Step 3 : _W1EditorAgent(v1, audit) → v2
```

**W2 — `CompetitiveAngleWorkflow`**
```python
async def run(keyword, topic, intent=None, context=None, on_step=None) -> WorkflowResult
# Step 1 : _W2SerpAnalystAgent → serp_analysis
# Step 2 : _W2AngleBuilderAgent(serp_analysis) → differentiating_angle
```

**W3 — `ContentFactoryWorkflow`**
```python
async def run(keyword, topic, intent, context=None, on_step=None) -> WorkflowResult
# Step 1 : SchoolswpBrainAgent(mode="seo-writer") → article  [séquentiel]
# Steps 2-6 : asyncio.gather(newsletter, linkedin, twitter, faq_aio, youtube)  [parallèle]
```

---

## Architecture `workflow_cli.py`

Subcommands argparse :
```
python -m agents.schoolswp_brain.workflow_cli seo-audit \
  --keyword "plugin cache WordPress" --intent comparative \
  --audience "freelance WordPress intermédiaire" --save-dir articles/cache/

python -m agents.schoolswp_brain.workflow_cli competitive \
  --keyword "LMS WordPress" --topic "Choisir son LMS WordPress" \
  --save-dir articles/lms-angle/

python -m agents.schoolswp_brain.workflow_cli content-factory \
  --keyword "FluentCRM vs ActiveCampaign" \
  --topic "FluentCRM vs ActiveCampaign : lequel choisir ?" \
  --intent comparative --save-dir articles/fluentcrm/
```

Save-dir outputs :
- `seo-audit` → v1.md / audit.md / v2.md
- `competitive` → serp-analysis.md / angle.md
- `content-factory` → article.md / newsletter.md / linkedin.md / twitter.md / faq-aio.md / youtube.md

Step logging : réutilise le pattern `_step_log(step, content)` de `article_pipeline/cli.py`.

---

## Modifications `agent.py`

Ligne ~1184 — `_MODES` dict, ajouter :
```python
"w1-article": "article V1 avec analyse stratégique complète",
"w3-article": "article base pour content factory multi-format",
```

---

## Max tokens par étape

| Étape | max_tokens |
|-------|-----------|
| W1 Step 1 (article V1) | 8192 (hérité SchoolswpBrainAgent) |
| W1 Step 2 (audit) | 2048 |
| W1 Step 3 (V2) | 4096 |
| W2 Step 1 (SERP) | 2048 |
| W2 Step 2 (angle) | 1500 |
| W3 Step 1 (article) | 8192 (hérité) |
| W3 Steps 2-6 (formats) | 1024 chacun |

---

## Vérification

```bash
# Test W1
python -m agents.schoolswp_brain.workflow_cli seo-audit \
  --keyword "meilleur plugin SEO WordPress" --intent comparative \
  --audience "freelance WordPress débutant" --save-dir /tmp/w1-test/

# Test W2
python -m agents.schoolswp_brain.workflow_cli competitive \
  --keyword "LMS WordPress" --topic "Choisir son LMS WordPress en 2026"

# Test W3
python -m agents.schoolswp_brain.workflow_cli content-factory \
  --keyword "FluentCRM avis" --topic "FluentCRM : mon avis après 6 mois" \
  --intent informationnelle --save-dir /tmp/w3-test/
```

Vérifier : présence des fichiers dans save-dir, contenu markdown valide, branding schoolsWP,
tutoiement appliqué, mots interdits absents.

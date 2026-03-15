# Plan — Brain Workflows W1, W2, W3

**Date** : 2026-03-15
**Statut** : En cours

---

## W1 — SEO Audit Workflow

**Objectif** : Audit SEO automatisé d'un article existant

**Commande** :
```bash
.venv/Scripts/python -m agents.schoolswp_brain.workflow_cli seo-audit --keyword "..." --intent informationnelle
```

**Étapes** :
1. Récupération article depuis Google Sheets IDEAS
2. Audit SEO /100 (SeoAuditorAgent)
3. Audit LLM SEO /100 (LlmSeoAgent)
4. Calcul Publish Score
5. Mise à jour Notion KPI

---

## W2 — Competitive Analysis Workflow

**Objectif** : Gap analysis SEO vs concurrent principal

**Commande** :
```bash
.venv/Scripts/python -m agents.schoolswp_brain.workflow_cli competitive --keyword "..." --competitor "wpmarmite.com"
```

**Étapes** :
1. Export keywords concurrents (DataForSEO)
2. Gap analysis (SeoCompetitorAnalystAgent)
3. Opportunités triées par impact/effort
4. Rapport Notion

---

## W3 — Content Factory Workflow

**Objectif** : Pipeline complet de production (= brain.bat)

**Commande** :
```bash
.venv/Scripts/python -m agents.schoolswp_brain.workflow_cli content-factory --keyword "..." --intent décisionnelle --pillar LMS
```

**Étapes** :
1. Stratégie (SchoolswpBrainAgent)
2. Rédaction (SeoWriterAgent)
3. Audits parallèles (SEO + LLM + Conversion + Topical)
4. Édition (SeoEditorAgent)
5. Cluster sémantique (ClusterArchitectAgent)
6. Meta (MetaAgent)
7. Sauvegarde Google Docs + Sheets

---

## Notes d'implémentation

- `workflow_cli.py` à créer dans `agents/schoolswp_brain/`
- Réutilise `ArticlePipeline` pour W3
- W1 et W2 : agents standalone, pas de pipeline
- Outputs : fichiers locaux + optionnel Notion/Sheets via n8n webhook

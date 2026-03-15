# SEO Workflow — schoolsWP

Workflow SEO automatisé en 10 tâches pour schoolswp.com.

## Structure

```
systems/seo-workflow/
├── README.md                    # Ce fichier
├── orchestrator.md              # Agent orchestrateur
├── tasks/                       # 10 tâches SEO
│   ├── 01-inventaire-seo.md
│   ├── 02-analyse-gsc.md
│   ├── 03-audit-technique.md
│   ├── 04-analyse-serp.md
│   ├── 05-gap-analysis.md
│   ├── 06-content-brief.md
│   ├── 07-optimisation-existant.md
│   ├── 08-maillage-interne.md
│   ├── 09-eeat-signals.md
│   └── 10-roadmap-finale.md
├── skills/                      # Skills spécialisés
│   ├── gsc-opportunity-scanner.md
│   ├── seo-crawl-hygiene.md
│   ├── hreflang-multilang-auditor.md
│   └── eeat-template-builder.md
├── templates/
│   └── sheets-schema.md           # Schéma Google Sheets
├── n8n/
│   └── seo-workflow.json          # Workflow n8n
├── diagrams/
│   ├── workflow-overview.mmd
│   └── n8n-flow.mmd
└── reports/
    ├── impact-effort-matrix.md
    └── quick-wins.md
```

## 10 Tâches

| # | Tâche | Skill | Output |
|---|-------|-------|--------|
| T1 | Inventaire SEO | seo-crawl-hygiene | CSV URLs |
| T2 | Analyse GSC | gsc-opportunity-scanner | Opportunités triées |
| T3 | Audit technique | — | Issues list |
| T4 | Analyse SERP | — | Gaps keywords |
| T5 | Gap analysis | seo-competitor-gap-radar | Delta vs WPMarmite |
| T6 | Content brief | brain | Brief structuré |
| T7 | Optimisation existant | seo-audit | Scores /100 |
| T8 | Maillage interne | — | Plan maillage |
| T9 | E-E-A-T signals | eeat-template-builder | Blocs E-E-A-T |
| T10 | Roadmap finale | — | Backlog priorisé |

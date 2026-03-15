# Workflow SEO séquentiel — schoolsWP

Système opérationnel en 10 tâches pour transformer l'audit SEO de schoolsWP.com en actions concrètes.

## Vue d'ensemble

```
flowchart LR
  T1[1. Inventaire] --> T2[2. Crawl & Index]
  T2 --> T3[3. GSC]
  T3 --> T4[4. Benchmark]
  T4 --> T5[5. Clusters]
  T5 --> T6[6. Maillage]
  T6 --> T7[7. Multilingue]
  T7 --> T8[8. E-E-A-T]
  T8 --> T9[9. Conversion]
  T9 --> T10[10. Roadmap]
```

## Structure

```
systems/seo-workflow/
├── README.md                        ← ce fichier
├── orchestrator.md                  ← agent orchestrateur principal
├── tasks/
│   ├── 01-inventaire-seo.md
│   ├── 02-crawl-indexation.md
│   ├── 03-analyse-gsc.md
│   ├── 04-benchmark-dataforseo.md
│   ├── 05-clusters-cannibalisation.md
│   ├── 06-maillage-interne.md
│   ├── 07-seo-multilingue.md
│   ├── 08-eeat-credibilite.md
│   ├── 09-conversion-seo.md
│   └── 10-roadmap-finale.md
├── skills/
│   ├── seo-crawl-hygiene.md
│   ├── gsc-opportunity-scanner.md
│   ├── hreflang-multilang-auditor.md
│   └── eeat-template-builder.md
├── templates/
│   ├── sheets-schema.md             ← schémas de tous les onglets Google Sheets
│   └── docs-template.md             ← gabarits Google Docs par tâche
├── diagrams/
│   ├── workflow-overview.mmd
│   └── n8n-flow.mmd
├── n8n/
│   └── seo-workflow.json
├── roadmap/
│   └── roadmap-30-60-90.md
└── reports/
    ├── impact-effort-matrix.md
    └── quick-wins.md
```

## Skills existants réutilisables

| Tâche         | Skills existants (dans `.claude/skills/`)            |
| ------------- | ---------------------------------------------------- |
| T4 Benchmark  | `seo-competitor-gap-radar`                           |
| T5 Clusters   | `cluster-cocon-automatique`, `topical-authority-map` |
| T6 Maillage   | `m1m3-urls-internal-linking`                         |
| T9 Conversion | `money-pages-framework`, `affiliation-optimizer`     |
| T10 Roadmap   | `authority-domination-roadmap`                       |

## Skills nouveaux créés ici

| Skill                        | Tâche(s) |
| ---------------------------- | -------- |
| `seo-crawl-hygiene`          | T2       |
| `gsc-opportunity-scanner`    | T3       |
| `hreflang-multilang-auditor` | T7       |
| `eeat-template-builder`      | T8       |

## Google Sheets requis

Créer un Google Sheet avec ces onglets dans l'ordre :

| Onglet           | Tâche | Schéma                                                                                                |
| ---------------- | ----- | ----------------------------------------------------------------------------------------------------- |
| `01_Inventory`   | T1    | url, type_page, langue, cluster, sous_cluster, role_SEO, role_business, priorite, observations, notes |
| `02_Hygiene`     | T2    | url_or_pattern, issue, action, impact, effort, priority, status                                       |
| `03_GSC`         | T3    | url, query, impressions, clics, ctr, position, issue, action, priority                                |
| `04_Competitors` | T4    | competiteur, cluster, mot_cle, presence_schoolsWP, gap, opportunite, priorite                         |
| `05_Clusters`    | T5    | cluster, pilier, satellites, complete, cannibal_risk, gaps, action                                    |
| `06_Linking`     | T6    | source, cible, anchor, context, reason_SEO, reason_CRO, priority                                      |
| `07_Multilang`   | T7    | url_fr, url_en, url_de, hreflang_ok, canonical_ok, parite, action, priority                           |
| `08_EEAT`        | T8    | url, type_page, eeat_gaps, ameliore, impact, priority                                                 |
| `09_Conversion`  | T9    | url, intention, objectif_business, CTA_actuel, probleme, optimisation, priority                       |
| `10_Backlog`     | T10   | id, action, categorie, impact_SEO, impact_business, effort, priorite, etat, owner                     |

## Règles système

1. **Observable** = donnée visible et vérifiable sans outil externe (structure menu, URL visible, tag HTML)
2. **Hypothèse à valider** = donnée nécessitant GSC, crawl ou API pour être confirmée
3. **Bonne pratique** = recommandation Google Search Central ou DataForSEO documentée
4. Chaque action doit être rattachée à l'un des trois types ci-dessus
5. Aucune recommandation purement spéculative — toujours préciser le type

## Déclenchement

- Manuel : lancer `orchestrator.md` avec les inputs disponibles
- n8n : voir `n8n/seo-workflow.json` — trigger cron hebdomadaire ou manuel
- Ordre strict : T1 → T2 → ... → T10. Ne pas sauter de tâche.

# Systems & Pipelines — Inventaire

Systèmes d'automatisation et pipelines métier dans `systems/`. Chaque sous-dossier = un pipeline structurant.

## Pipelines actifs

| System | Stack | Rôle |
|---|---|---|
| **linkedin-prospecting** | Apify + Unipile + Claude + Hunter.io + n8n | Pipeline V4 de prospection LinkedIn à partir d'un post URL. Kit SOP complet. |
| **pinterest-pipeline** | n8n + Placid + Tailwind | Pipeline de production Pinterest (briefs, analytics, data). CLAUDE.md + SOP.md dédiés. |
| **seo-workflow** | n8n + orchestrator | Workflow SEO automatisé en 10 tâches pour schoolswp.com. Diagrammes + roadmap. |
| **multi-agent-system** | Python + agents | Framework d'orchestration d'agents multi-agents (docs, scripts, workflows). |
| **n8n** | n8n self-hosted (Docker) | Audit SEO mensuel automatisé (20 du mois), PDF + email + Slack. CLAUDE.md dédié + règles du jeu. |
| **n8n-backup** | Bash + n8n API | Backup automatisé de n8n self-hosted (`backup-n8n.sh`, `restore-n8n.sh`). |
| **workflows** | JSON n8n | Collection de workflows exportés (auto-readme, auto-rename, linkedin-post, hub-sync…). |
| **security** | Docs + reports | Conformité GDPR, registre de traitements, rotation policy, pentest reports, incidents. |

## Instance n8n

- URL : `https://schoolswp-n8n.wp1.host`
- Règle d'or : **jamais** modifier les JSON de workflows à la main → passer par MCP `n8n-mcp`
- Contraintes (typeVersions, Code node) : `.claude/rules/n8n-integration.md`

## Sécurité (`systems/security/`)

- `gdpr-compliance.md` — conformité RGPD
- `registre-traitements.md` — registre des traitements
- `rotation-policy.md` — politique de rotation des secrets
- `pentest-report-*.md` — rapports pentest datés
- `incidents/` — journal d'incidents

## Sub-CLAUDE.md auto-chargés

- `systems/n8n/CLAUDE.md` — typeVersions confirmées, nommage, contraintes Code node
- `systems/pinterest-pipeline/CLAUDE.md` — règles pipeline Pinterest

## À savoir

- `linkedin-prospecting` : ne pas confondre `systems/linkedin-prospecting/` (SOP + prompts + schemas) avec les scripts `tools/scripts/`
- `multi-agent-system/` contient un sous-dossier du même nom — doublon d'organisation à nettoyer éventuellement

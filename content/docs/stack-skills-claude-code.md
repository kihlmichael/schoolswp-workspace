# Skills Claude Code — Inventaire

Les skills sont des capacités activables à la volée (slash commands ou invocation auto). Ils vivent dans 3 emplacements complémentaires.

## Architecture à 3 couches

| Emplacement | Rôle |
|---|---|
| `.claude/skills/` (projet schoolsWP) | Skills locaux projet, organisés par catégorie |
| `d:\VS Code\CLAUDE CODE\.claude\skills\` (workspace) | Skills workspace FR adaptés schoolsWP |
| `C:\Users\micha\.claude\skills\` (global) | Skills génériques tous projets |

## Catégories projet (`.claude/skills/`)

- **affiliation** — skills liés programmes affiliés
- **authority** — construction d'autorité, expertise
- **code-review-and-quality** — review multi-axes avant merge
- **contenu** — rédaction, production éditoriale
- **documentation-and-adrs** — ADR, docs architecture
- **engines** — moteurs SEO/contenu internes
- **git-workflow-and-versioning** — discipline git
- **ia-llm** — intégration LLM, prompts, API
- **incremental-implementation** — tranches verticales, petits commits
- **n8n** — workflows n8n
- **ops** — opérationnel, runbooks
- **planning-and-task-breakdown** — décomposition de tâches
- **seo** — SEO technique et éditorial
- **social** — contenu social
- **telegram-claude** — pont Telegram → Claude

## Skills slash commands principaux

| Commande | Usage |
|---|---|
| `/audit` | Audit de publication (4 audits parallèles) |
| `/brain-lite` | Pipeline brain-lite (5 étapes sans NER/SERP) |
| `/publish-repo` | Publication et gestion repo |
| `/skill-creator` | Créer un nouveau skill |
| `/todo` | Tableau de bord de mission |
| `/commit` | Workflow de commit discipliné |

## Sync vers Google Sheets

Le registre est synchronisé vers un spreadsheet dédié :

```bash
.venv/Scripts/python "d:/VS Code/CLAUDE CODE/.claude/skills/.registry/skills_registry.py" --sync
```

Source de vérité : `.claude/skills/INDEX.md` (projet) et `INDEX.md` de chaque dossier workspace.

## Format YAML frontmatter

```yaml
---
name: mon-skill
description: Une ligne claire de quand invoquer le skill
allowed-tools: Read, Edit, Bash    # optionnel
---
```

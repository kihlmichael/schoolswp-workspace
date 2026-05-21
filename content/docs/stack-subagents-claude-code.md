# Subagents Claude Code : inventaire

Trois systèmes d'agents distincts dans ce projet. Ne pas les confondre.

| Système | Emplacement | Nature |
| --- | --- | --- |
| Sub-agents Claude Code projet | `.claude/agents/*.md` | 27 configs YAML dispatchables via l'outil `Agent` (contexte isolé, parallélisables) |
| Fleet multi-agents autonome | `schoolswp-agents/` | 4 instances Claude Code complètes, process séparé, mémoire persistante |
| Agents Python | `core/agents-py/` | 28 scripts CLI héritant de `BaseContentAgent` (pas des sub-agents) |

## 1. Sub-agents Claude Code (`.claude/agents/`)

Catalogue complet, tables de routing et règles de conflit : [.claude/agents/INDEX.md](../../.claude/agents/INDEX.md). Le compteur et les tables détaillées y sont régénérés par le script de registre des agents (voir la section « Maintenance » de l'INDEX).

Dispatch via l'outil `Agent` avec `subagent_type` = valeur du champ `name:` du frontmatter (pas le nom de fichier : `pinterest.md` expose `pinterest-expert`).

Groupes : éditorial schoolsWP, YouTube OS, spécialistes domaine, code review / qualité, harness, hors schoolsWP.

**Subagents built-in Claude Code** : `general-purpose`, `Explore` (recherche rapide), `Plan` (architecte), `statusline-setup`, `claude-code-guide`.

## 2. Multi-Agent Fleet (`schoolswp-agents/`)

Instances Claude Code autonomes, chacune avec son propre `CLAUDE.md`, `soul.md` (personnalité), mémoire persistante et skills locaux.

| Agent | Rôle | Modèle |
| --- | --- | --- |
| `content-studio` | Rédaction, tutoriels, optimisation contenu | opus |
| `crm-automation` | Automatisation WordPress, CRM/LMS | opus |
| `seo-geo` | Audit SEO, GEO/AIO, maillage interne | opus |
| `social-community` | Contenu social, communauté | haiku |

Ressources partagées dans `schoolswp-agents/shared/` : contacts, skills (branding, voice, stack WordPress).

## Quand utiliser quoi

| Situation | Outil |
| --- | --- |
| Exploration rapide du codebase | `Explore` |
| Design d'implémentation | `Plan` |
| Question ouverte multi-étapes | `general-purpose` |
| Production de contenu schoolsWP | `studio` |
| Brief SEO, cocon sémantique | `radar` |
| Séquence CRM / automation / n8n | `flow` |
| Post social (LinkedIn, Bluesky, Pinterest, YouTube) | `pulse` |
| Review de code avant merge | `code-reviewer` |
| Session autonome longue | Fleet `schoolswp-agents/` |

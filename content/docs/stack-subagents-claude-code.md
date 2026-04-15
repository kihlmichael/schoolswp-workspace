# Subagents Claude Code — Inventaire

Deux systèmes distincts dans ce workspace. Ne pas confondre avec les agents Python (`core/agents-py/`) qui sont des scripts CLI.

## 1. Subagents Claude Code (`agents/*.md`)

Configurations YAML invocables via l'outil `Agent`. Utilisent `subagent_type` = nom du fichier.

| Subagent | Rôle | Modèle |
|---|---|---|
| `content-studio` | Rédaction articles, newsletters, tutoriels, scripts vidéo | opus |
| `seo-radar` | SEO/GEO, cocons sémantiques, briefs, maillage | opus |
| `crm-flow` | CRM, email automation, n8n, FluentCRM, OttoKit | opus |
| `social-pulse` | Social (LinkedIn, Bluesky, Pinterest, YouTube) | haiku |
| `code-reviewer` | Review de code indépendante | opus |

**Subagents built-in Claude Code** : `general-purpose`, `Explore` (recherche rapide), `Plan` (architecte), `statusline-setup`, `claude-code-guide`, `framework-adapter-fr`.

## 2. Multi-Agent Fleet (`schoolswp-agents/`)

Instances Claude Code autonomes, chacune avec son propre `CLAUDE.md`, `soul.md` (personnalité), mémoire persistante et skills locaux.

| Agent | Rôle | Modèle |
|---|---|---|
| `content-studio` | Rédaction, tutoriels, optimisation contenu | opus |
| `crm-automation` | Automatisation WordPress, CRM/LMS | opus |
| `seo-geo` | Audit SEO, GEO/AIO, maillage interne | opus |
| `social-community` | Contenu social, communauté | haiku |

Ressources partagées dans `schoolswp-agents/shared/` : contacts, skills (branding, voice, stack WordPress).

## Quand utiliser quoi

| Situation | Outil |
|---|---|
| Exploration rapide du codebase | `Explore` |
| Design d'implémentation | `Plan` |
| Question ouverte multi-étapes | `general-purpose` |
| Production de contenu schoolsWP | `content-studio` (subagent) |
| Brief SEO schoolsWP | `seo-radar` |
| Séquence CRM / automation | `crm-flow` |
| Post social | `social-pulse` |
| Review indépendante | `code-reviewer` |
| Session autonome longue | Fleet `schoolswp-agents/` |

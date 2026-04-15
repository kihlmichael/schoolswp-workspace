# MCP Servers — Inventaire

Les MCP (Model Context Protocol) servers exposent des outils externes à Claude. Configurés à 2 niveaux.

## Niveau projet (`projects/schoolswp/.mcp.json`)

Fichier gitignoré — template dans `.mcp.json.example`.

| Server | Rôle |
|---|---|
| `n8n-mcp` | Gestion workflows n8n (instance schoolswp-n8n.wp1.host) |
| `novamira-schoolswp-com` | WordPress REST API du site schoolswp.com |
| `github` | API GitHub (issues, PRs, repos) |
| `firecrawl` | Scraping web et recherche |
| `apify` | Actors de scraping (LinkedIn, etc.) |
| `dataforseo` | Données SEO, volumes keywords, SERP |
| `wisewand` | Service de génération de contenu |
| `zipwp` | Création de sites WordPress |
| `rapidapi-linkedin` | Endpoints LinkedIn |
| `rapidapi-twitter` | Endpoints Twitter/X |
| `rapidapi-instagram` | Endpoints Instagram |
| `rapidapi-youtube` | Endpoints YouTube |

## Niveau workspace (`.claude/settings.json`)

Servers partagés entre tous les projets Claude Code :

| Server | Rôle |
|---|---|
| `memory` | Mémoire persistante cross-session |
| `filesystem` | Accès filesystem étendu |
| `playwright` | Automation navigateur |
| `supabase` | Base Supabase |
| `exa` | Recherche web sémantique |
| `context7` | Documentation librairies à jour |
| `telegram` | Pont Telegram |
| `Canva` | Design (via claude.ai) |
| `Gmail` | Email (via claude.ai) |
| `Google Calendar` | Calendrier (via claude.ai) |
| `Notion` | Workspace Notion (via claude.ai) |

## Patterns d'usage

- **Recherche SEO** : `dataforseo` (volumes, concurrence) + `firecrawl` (contenu SERP)
- **Publication WordPress** : `novamira-schoolswp-com` (pages, articles, médias)
- **Automation** : `n8n-mcp` (créer/modifier workflows) + `github` (triggers)
- **Social scraping** : `rapidapi-*` ou `apify`
- **Docs techniques** : `context7` (toujours à jour) plutôt que connaissance LLM

## Sécurité

- `.mcp.json` toujours gitignored
- Credentials à remplir via `.mcp.json.example` comme template
- Jamais commiter de tokens ou clés

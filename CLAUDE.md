# schoolsWP — Workspace Claude Code

Projet : schoolsWP (schoolswp.com)
Owner : Michael KIHL
Stack : n8n automation, Python scripting, Docker, WordPress (via API)

## Branding

- "schoolsWP" s'ecrit TOUJOURS "schoolsWP" — JAMAIS "SchoolsWP", "schoolswp", "Schoolswp"
- "WP" reste toujours en majuscules
- Le site est schoolswp.com (pas www.)
- Dans les communications : toujours "schoolsWP" en premier usage, ensuite "le projet" ou "la plateforme"

## Conventions de code

### Python
- Style PEP 8, indent 4 espaces
- Formatter : ruff (ou black)
- Linter : ruff

### JSON / JavaScript
- Indent 2 espaces, pas de trailing comma
- UTF-8, LF line endings

### YAML
- Indent 2 espaces

### Shell (bash)
- Shebang : `#!/usr/bin/env bash`
- Indent 2 espaces

### Nommage workflows n8n
- Format : `[Status] Source > Destination: Description (ID)`
- Status : `[InDev]`, `[InTesting]`, `[Staging]`, `[Prod]`, `[Offline]`, `[ForDeletion]`

### Nommage credentials
- Format : `Service_Environment_Type`
- Exemples : `Salesforce_Production_OAuth`, `PostgreSQL_Staging_Password`

### Fichiers
- kebab-case pour les noms de fichiers (jamais camelCase)

## Structure du workspace

```
workflows/          Workflows n8n (JSON)
scripts/            Scripts bash (backup, deploy, health-check)
config/             Docker-compose, Prometheus, Grafana
docs/               Documentation technique
claude-telegram-poc/ POC bot Telegram (Python)
```

## Regles Claude Code

- Langue : repondre en francais par defaut
- Ne JAMAIS modifier .env ou fichiers contenant des secrets sans demander
- Ne JAMAIS faire de force push, reset --hard, ou rm -rf
- Toujours proposer un plan avant les modifications structurelles
- Utiliser les skills disponibles (branding, n8n-*, marketing, etc.) quand pertinent
- Commits : messages en anglais, format conventionnel (feat:, fix:, chore:, docs:)
- Branche de travail par defaut : feature/* ou fix/* depuis main

## MCP et Integrations

- n8n-mcp est configure dans .mcp.json (ne pas modifier sans accord)
- Skills Claude Code disponibles :
  - n8n : n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns
  - Contenu : branding, marketing, wordpress, dev-wordpress
  - Social : linkedin, youtube, facebook, discord, slack, whatsapp
  - Outils : firecrawl, notion, googledrive, remotion, openai-imagegen, openai-whisper, gemini
  - Audit : code-audit
- Workflows automatises accessibles via n8n API

## Securite

- Ne JAMAIS commit de secrets, API keys, tokens
- Les .env ne sont JAMAIS versionnes
- .mcp.json contient des cles API : il est dans .gitignore, utiliser .mcp.json.example comme template
- Verifier que .gitignore est a jour avant tout commit
- Les credentials n8n doivent etre sanitizees avant export

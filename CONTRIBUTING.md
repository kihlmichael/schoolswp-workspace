# Contributing to schoolsWP Automation

Owner: Michael KIHL
Project: schoolsWP (schoolswp.com)

## Branding

- Always write **schoolsWP** (lowercase "schools", uppercase "WP")
- Never use "SchoolsWP", "schoolswp", or "Schoolswp"

## Git Workflow

### Branches

- `main` — stable, production-ready
- `feature/*` — new features
- `fix/*` — bug fixes
- `chore/*` — maintenance, tooling, config

### Commit Messages

Use conventional commits (English):

```
feat: add new workflow for SEO monitoring
fix: correct error handler in backup script
chore: update docker-compose config
docs: add troubleshooting for webhook timeout
```

### Pull Request Process

1. Create a branch from `main`
2. Make your changes with atomic commits
3. Test locally (health check, lint)
4. Submit a pull request with a clear description
5. Wait for review before merging

## Adding an n8n Workflow

1. Create the workflow in the n8n UI
2. Export as JSON to `systems/workflows/workflows/`
3. Follow the naming convention: `[Status] Source > Destination: Description (ID)`
4. Sanitize all credentials before committing
5. Add a README in `systems/workflows/workflows/templates/` if it's a reusable template

### Workflow Status Tags

| Tag | Meaning |
|-----|---------|
| `[InDev]` | In development |
| `[InTesting]` | Being tested |
| `[Staging]` | Pre-production |
| `[Prod]` | Production |
| `[Offline]` | Disabled |
| `[ForDeletion]` | Scheduled for removal |

### Credential Naming

Format: `Service_Environment_Type`

Examples: `Salesforce_Production_OAuth`, `PostgreSQL_Staging_Password`

## Code Standards

### Python

- PEP 8 compliant
- Indent: 4 spaces
- Formatter: ruff or black
- Linter: ruff

### JSON

- Indent: 2 spaces
- No trailing commas
- UTF-8 encoding

### Shell Scripts

- Shebang: `#!/usr/bin/env bash`
- Indent: 2 spaces
- LF line endings

### File Naming

- Use kebab-case: `my-workflow-name.json`
- Never use camelCase for filenames

## Security

- Never commit `.env` files, API keys, or tokens
- Always check `.gitignore` before committing
- Sanitize n8n credentials before exporting workflows
- Store secrets in `.env` (local) or a secrets manager (production)

## Documentation

- Document new workflows with a README in `systems/workflows/workflows/templates/`
- Keep `content/docs/` up to date for troubleshooting guides
- Write documentation in French (project language)

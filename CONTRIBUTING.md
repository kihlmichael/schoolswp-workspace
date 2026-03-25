# Contributing to schoolsWP Automation

Owner: Michael KIHL
Project: schoolsWP (schoolswp.com)

## Branding

- Always write **schoolsWP** (lowercase "schools", uppercase "WP")
- Never use "SchoolsWP", "schoolswp", or "Schoolswp"

## Git Governance

### Branches

| Branch | Role | Protected |
|--------|------|-----------|
| `main` | Stable, production-ready. Single source of truth. | Yes |
| `feature/*` | New features | No |
| `fix/*` | Bug fixes | No |
| `chore/*` | Maintenance, tooling, config | No |
| `docs/*` | Documentation only | No |

### Rules

1. **Never commit directly to `main`** — always branch, then merge via PR or fast-forward.
2. **One working branch at a time** — finish or shelve before starting another.
3. **Pre-commit hooks are mandatory** — `--no-verify` only when the hook itself is broken (document why in the commit message).
4. **No secrets in git** — `.env`, `.mcp.json`, `settings.local.json` stay in `.gitignore`. Pre-commit hook scans for patterns.
5. **Conventional commits in English** — prefix with `feat:`, `fix:`, `chore:`, `docs:`, `security:`, `refactor:`, `test:`.

### Commit Messages

```
feat: add new workflow for SEO monitoring
fix: correct error handler in backup script
chore: update docker-compose config
docs: add troubleshooting for webhook timeout
security: add path traversal protection
```

### Workflow

```
main ──────────────────────────────────── (protected)
  \                                  /
   feature/my-feature ──────────────  (branch, work, merge back)
```

1. `git checkout -b feature/my-feature main`
2. Work with atomic commits
3. Test locally (lint, tests)
4. Push and merge to `main` (PR or fast-forward)
5. Delete the feature branch after merge

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

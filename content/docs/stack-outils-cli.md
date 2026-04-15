# Outils CLI — Pense-bête

Outils en ligne de commande utilisés dans le workspace schoolsWP.

## Gestion de code et git

| Outil | Usage |
|---|---|
| `git` | Versioning — branches : `feature/*`, `fix/*`, `chore/*` depuis `main` |
| `gh` | GitHub CLI — `gh pr create`, `gh issue view`, `gh repo view` |
| `pre-commit` | Hooks pre-commit (secrets-scan, ruff, pip-audit) — `pre-commit install` une fois |

## Python

| Outil | Usage |
|---|---|
| `uv` | Gestionnaire de deps (lock `uv.lock`) — `uv sync` depuis la racine |
| `.venv/Scripts/python` | Interpréteur du venv (chemin complet obligatoire sur Windows+Bash) |
| `ruff` | Lint + format — `.venv/Scripts/python -m ruff check core/agents-py/` |
| `pytest` | Tests (asyncio auto) — `.venv/Scripts/python -m pytest tests/` |

## Google Workspace

| Outil | Usage |
|---|---|
| `gws` | Google Workspace CLI — `gws drive files list`, `gws sheets spreadsheets get` |

Exemples :
```bash
gws drive files list --params '{"pageSize":10}'
gws drive files create --json '{"name":"doc","mimeType":"application/vnd.google-apps.document"}' --upload file.md
gws sheets spreadsheets values get --params '{"spreadsheetId":"...","range":"Feuille 1!A1:C10"}'
```

## OpenAI Codex (plugin Claude Code)

| Commande | Usage |
|---|---|
| `!codex login` | Authentification Codex |
| `npm install -g @openai/codex` | Install manuelle si besoin |

Slash commands : voir fiche "Codex Plugin pour Claude Code — Guide d'usage".

## Node.js

| Outil | Usage |
|---|---|
| `node` | v24+ installé |
| `npm` | v11+ — `npm install -g <pkg>` pour les outils globaux |
| `npx` | Exécution one-shot de packages |

## Pipelines schoolsWP (raccourcis .bat)

| Raccourci | Commande équivalente |
|---|---|
| `brain.bat` | `.venv/Scripts/python -m agents.content_factory.cli` |
| `brain-lite.bat` | `.venv/Scripts/python -m agents.article_pipeline.brain_lite_cli` |

## Règles de sécurité

- **Jamais** : `rm`, `rm -rf`, `sudo`, `doas`
- Utiliser `trash <path>` pour toute suppression
- Ne jamais vider la corbeille automatiquement
- `.env` et `.mcp.json` jamais commités

## Claude Code (slash commands)

| Commande | Usage |
|---|---|
| `/plugin` | Gestion plugins |
| `/reload-plugins` | Recharger après install |
| `/help` | Aide Claude Code |
| `/fast` | Toggle fast mode |
| `/rename` | Renommer la session |

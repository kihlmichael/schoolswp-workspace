---
description: Tools, services et scripts utilitaires du projet
paths: ["tools/**"]
---

# Tools & Services

| Répertoire | Contenu |
| --- | --- |
| `tools/scripts/` | Scripts utilitaires Python : audit/migration Google Drive (`gdrive-*.py`), scripts Notion (`setup-notion-*.js`) |
| `tools/scripts/legacy/` | Scripts dépréciés et venv legacy — ne pas modifier |
| `tools/services/rapidapi-mcp/` | Serveur MCP RapidAPI (`server.py`) — wraps les endpoints RapidAPI |
| `tools/services/pdf-service/` | Service PDF Node.js (Dockerfile inclus) |
| `tools/services/schoolsWP-drive-organizer/` | Scripts Google Apps Script pour audit et migration Drive |
| `tools/image-meta-seo/` | Générateur de métadonnées SEO pour images (server.py + index.html) |
| `tools/wp-media-upload/` | Upload batch d'images WP avec métadonnées SEO + EXIF (`cli.py upload --article <slug>`) — manifest YAML par article, ExifTool requis pour baker XP* |

**Google Drive scripts** (depuis `projects/schoolswp/`) :
```bash
.venv/Scripts/python tools/scripts/gdrive-audit.py        # audit structure Drive
.venv/Scripts/python tools/scripts/gdrive-rename.py       # renommage batch
.venv/Scripts/python tools/scripts/gdrive-dispatch-docs.py # dispatch Google Docs
```
Auth : variables d'env `GOOGLE_WORKSPACE_CLI_CLIENT_ID` / `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET` (ne pas utiliser `client_secret.json`).

## Fichiers racine ponctuels

Scripts one-shot à la racine — ne pas relancer sans vérifier s'ils sont encore pertinents :

| Fichier | Rôle |
| --- | --- |
| `patch_*.py` (×8) | Patches one-shot appliqués sur le workflow n8n `PkFO7Of9BrMfl8Ed` via l'API REST n8n |
| `fix_workflow.py` | Correctif ponctuel sur le même workflow (restructuration nœuds + connexions) |
| `ccpa.config.json` | Template de config pour l'app Telegram (`apps/claude-telegram-poc/`) — `botToken` à remplir |
| `temp-n8n-skills/` | Dossier de travail temporaire pour tests de skills n8n — peut être archivé |

Ces scripts contiennent une clé API n8n hardcodée — ne pas commiter de nouvelles modifications sans la déplacer dans `.env`.

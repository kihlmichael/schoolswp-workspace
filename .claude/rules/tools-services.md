---
description: Tools, services et scripts utilitaires du projet
paths: ["tools/**"]
---

# Tools & Services

| Répertoire | Contenu |
| --- | --- |
| `tools/scripts/` | Scripts utilitaires Python : audit/migration Google Drive (`gdrive-*.py`), scripts Notion (`setup-notion-*.js`) |
| `tools/scripts/legacy/` | Scripts dépréciés et venv legacy — ne pas modifier |
| `tools/scripts/mcp-sheet-sync/` | Sync du Google Sheet [schoolsWP - MCP Servers](https://docs.google.com/spreadsheets/d/1IAYk6TPU1s8W81lfV4r0mEGH_0VyfwsZo53GkuEwe9k/edit) (inventaire MCP `.mcp.json` + sessions Claude.ai). `push-mcp-sheet.py` (append batché via gws) + `style-mcp-sheet.py` (branding schoolsWP : header dark + vert, zebra, bordures) + `mcp-sheet-rows.json` (44 rows source de vérité). Workflow d'ajout dans le README. |
| `tools/services/rapidapi-mcp/` | Serveur MCP RapidAPI (`server.py`) — wraps les endpoints RapidAPI |
| `tools/services/pdf-service/` | Service PDF Node.js (Dockerfile inclus) |
| `tools/services/schoolsWP-drive-organizer/` | Scripts Google Apps Script pour audit et migration Drive |
| `tools/image-meta-seo/` | Générateur de métadonnées SEO pour images (server.py + index.html) |
| `tools/wp-media-upload/` | Upload batch d'images WP avec métadonnées SEO + EXIF (`cli.py upload --article <slug>`) — manifest YAML par article, ExifTool requis pour baker XP* |
| `tools/html-to-png/` | Convertit `slide-*.html` en PNG via Playwright (Chromium headless). Format par défaut 1080x1350 (Instagram 4:5), options `--width` / `--height` / `--scale` / `--selector`. Lancement : `node tools/html-to-png/capture.mjs <dossier>`. Utilisé pour les carrousels Instagram schoolsWP. |
| `tools/skoatch/` | Client Python + CLI pour l'API Skoatch (Laravel Sanctum bearer). Genere des articles SEO via Skoatch.com avec polling asynchrone integre. **Isole du pipeline schoolsWP** — destine a un autre site WordPress (BRAND_RULES schoolsWP incompatibles avec output Skoatch). Skill associe : `dev/skoatch-api`. Token dans `tools/skoatch/.env` (gitignored) ou `SKOATCH_TOKEN` au .env racine. |
| `tools/thruuu_client/` | Client Python pour l'API SERP thruuu v2 (Bearer `THRUUU_API_KEY` du `.env` racine). Réutilisé par le serveur MCP `tools/mcp-servers/thruuu/` et par le workflow n8n `systems/n8n/workflows/thruuu-serp-analysis.json`. Voir [tools/thruuu_client/README.md](../../tools/thruuu_client/README.md) pour les 3 modes (Py / MCP / n8n). 17 tests unitaires dans `tests/test_thruuu_client.py`. |

**Google Drive scripts** (depuis `projects/schoolswp/`) :
```bash
.venv/Scripts/python tools/scripts/gdrive-audit.py        # audit structure Drive
.venv/Scripts/python tools/scripts/gdrive-rename.py       # renommage batch
.venv/Scripts/python tools/scripts/gdrive-dispatch-docs.py # dispatch Google Docs
.venv/Scripts/python tools/scripts/gdrive-upload.py FICHIER --folder ID --name NOM --mime MIME  # upload binaire (PDF, image, zip)
.venv/Scripts/python tools/scripts/gdrive-upload.py FICHIER.md --folder ID --google-doc --name NOM  # convertir markdown/html/txt en Google Doc natif
```
Auth : variables d'env `GOOGLE_WORKSPACE_CLI_CLIENT_ID` / `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET` (ne pas utiliser `client_secret.json`).

gdrive-upload.py s'appuie sur le CLI gws (streaming multipart). Voie à privilégier quand le MCP create_file échoue sur un binaire volumineux (limite base64 inline environ 240 Ko). En cas d'échec, vérifier gws auth status (champ token_valid) et relancer gws auth login si besoin.

L'option `--google-doc` convertit un `.md` / `.html` / `.txt` en Google Doc natif à l'import (source = type réel, cible = `application/vnd.google-apps.document`). Utile pour aligner scripts et docs sur un dossier Drive en Google Docs. Pour envoyer un fichier Drive à la corbeille : `gws drive files update --params "{\"fileId\": \"...\"}" --json "{\"trashed\": true}"` (passer le JSON via Bash, pas PowerShell : cmd.exe retire les guillemets).

## Fichiers racine ponctuels

Scripts one-shot à la racine — ne pas relancer sans vérifier s'ils sont encore pertinents :

| Fichier | Rôle |
| --- | --- |
| `patch_*.py` (×8) | Patches one-shot appliqués sur le workflow n8n `PkFO7Of9BrMfl8Ed` via l'API REST n8n |
| `fix_workflow.py` | Correctif ponctuel sur le même workflow (restructuration nœuds + connexions) |
| `ccpa.config.json` | Template de config pour l'app Telegram (`apps/claude-telegram-poc/`) — `botToken` à remplir |
| `temp-n8n-skills/` | Dossier de travail temporaire pour tests de skills n8n — peut être archivé |

Ces scripts contiennent une clé API n8n hardcodée — ne pas commiter de nouvelles modifications sans la déplacer dans `.env`.

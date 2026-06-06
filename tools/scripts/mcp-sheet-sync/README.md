# mcp-sheet-sync

Sync du Google Sheet [schoolsWP - MCP Servers](https://docs.google.com/spreadsheets/d/1IAYk6TPU1s8W81lfV4r0mEGH_0VyfwsZo53GkuEwe9k/edit) — inventaire de tous les MCP servers utilises par le projet (.mcp.json local + sessions Claude.ai).

## Fichiers

- `mcp-sheet-rows.json` — payload de 44 rows (30 dans .mcp.json + 14 Claude.ai session). Source de verite cote local.
- `push-mcp-sheet.py` — append les rows dans le Sheet via gws (batched, 8 rows par appel pour passer la limite cmd Windows).
- `style-mcp-sheet.py` — applique le branding schoolsWP (header dark #0F1419 + vert #00D400, zebra, bordures vertes, wrap, freeze row + col 1).

## Workflow d'ajout d'un nouveau MCP

1. Editer `mcp-sheet-rows.json` : ajouter une ligne dans `values[]` avec les 7 colonnes (Nom, Source, Transport, Endpoint, Description, Outils, Statut).
2. Cote Sheet, clear les data rows :

   gws sheets spreadsheets values clear --params '{"spreadsheetId": "1IAYk6TPU1s8W81lfV4r0mEGH_0VyfwsZo53GkuEwe9k", "range": "Feuille 1!A2:G1000"}'

3. Re-push tout :

   .venv/Scripts/py tools/scripts/mcp-sheet-sync/push-mcp-sheet.py

4. (Optionnel) reformater si le banding a saute :

   .venv/Scripts/py tools/scripts/mcp-sheet-sync/style-mcp-sheet.py

## Prerequis

- gws CLI authentifie (cf. memoire `reference_gws_oauth_refresh.md`)
- venv projet active (`.venv/Scripts/py` resout vers Python 3.14)

## TODO (routine eventuelle)

Si la maintenance manuelle devient penible, automatiser avec un script qui :

1. parse `.mcp.json` racine projet pour les 29 MCP locaux,
2. introspecte chaque MCP pour recuperer la liste des tools exposes (via `claude mcp list` ou direct stdio),
3. fusionne avec la section "Claude.ai session" (statique, listee dans le system reminder de Claude Code),
4. regenere `mcp-sheet-rows.json` puis push + style.

Pour l'instant, edition manuelle suffisante (rythme ~1 ajout MCP par mois).

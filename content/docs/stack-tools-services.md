# Tools & Services — Inventaire

Utilitaires dans `tools/`. Trois grandes catégories : services (dockerisés ou long-running), outils spécialisés, scripts one-shot.

## Services (`tools/services/`)

| Service | Stack | Rôle |
|---|---|---|
| **pdf-service** | Node.js + Docker | Génération PDF à la demande (Dockerfile fourni). |
| **rapidapi-mcp** | Python (`server.py`) | Wrapper MCP pour RapidAPI (expose les endpoints sociaux). |

## Outils spécialisés (`tools/`)

| Outil | Stack | Rôle |
|---|---|---|
| **image-meta-seo** | Python (`server.py`) + HTML | Serveur local de métadonnées SEO pour images. |
| **thruuu-writer** | Markdown + briefs | Convertisseur brief → article (GUIDELINE_EXAMPLE.md, GUIDELINE_MAKER.md). |
| **ultimate-scraper** | Claude Code + Apify | Scraper universel piloté en langage naturel. Config + prompts. |
| **legacy** | — | Scripts dépréciés (ne pas utiliser). |

## Scripts utilitaires (`tools/scripts/`)

**28 scripts Python** — principaux groupes :

### Google Drive
- `backup_wp_to_drive.py` — backup WordPress → Drive
- `create_drive_folders.py` — création arborescence Drive
- `fill_drive_docs.py` — remplissage de Google Docs
- `gdrive-audit.py` — audit Drive
- `gdrive-cleanup-root.py` — nettoyage racine Drive
- `gdrive-dispatch-docs.py` / `dispatch-pdf.py` / `dispatch-sheets.py` — dispatch de fichiers
- `gdrive-migration-apply.py` — migration Drive

### CCI (data fetching)
- `cci-v2-auth.py`, `cci-v2-read.py`, `cci-v2-read-all.py`, `cci-v2-write.py`, `cci-v3-write.py` — pipeline CCI

### Autres
- Scripts ponctuels pour diverses automatisations

## Commandes utiles

```bash
# Service PDF (dockerisé)
cd tools/services/pdf-service && docker build -t pdf-service . && docker run -p 3000:3000 pdf-service

# RapidAPI MCP
python tools/services/rapidapi-mcp/server.py

# Image SEO
python tools/image-meta-seo/server.py

# Script Drive
python tools/scripts/gdrive-audit.py
```

## À savoir

- `tools/services/` = ressources long-running (serveurs, Docker)
- `tools/<nom>/` (hors services) = utilitaires à usage ponctuel ou projets à part entière
- `tools/scripts/` = one-shot Python, à lancer manuellement
- `tools/legacy/` = archive, ne pas utiliser
- Toujours vérifier qu'un script ne nécessite pas de credentials avant de le lancer (voir `credentials-*.json`)

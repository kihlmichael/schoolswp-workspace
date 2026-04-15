# CLAUDE.md — Pinterest Pipeline

Regles Claude Code pour le sous-systeme `systems/pinterest-pipeline/`.

## Source de verite

`SOP.md` dans ce dossier. Toute question sur le workflow, les etats, les validations → lire la SOP.

## Regles strictes

1. **Machine d'etat** : ne jamais sauter un etat. Transitions sequentielles uniquement.
2. **Validation humaine** : 3 gates obligatoires (brief, design, publish). Jamais de publication sans `publish_approved = true`.
3. **Anti-doublon** : verifier `published_pin_id` + `content_hash` avant toute publication.
4. **Export local** : toujours telecharger l'image Canva dans `/exports` AVANT publication Pinterest.
5. **Pas de suppression** : `trash` uniquement, jamais `rm`.
6. **Secrets** : `PINTEREST_ACCESS_TOKEN`, `PINTEREST_REFRESH_TOKEN`, `CANVA_API_KEY` dans `.env` uniquement.
7. **Dry-run** : supporter `--dry-run` sur chaque script.

## Conventions fichiers

- Briefs : `briefs/YYYY-MM-DD-pin-XXX.json`
- Exports : `exports/pin-XXX.png`
- Analytics : `analytics/YYYY-MM-DD.json`
- Logs : `logs/state-transitions.log`, `logs/publish.log`

## Commandes

```bash
# Generer un brief
.venv/Scripts/python src/brief.py --source-url "https://schoolswp.com/article" --board-key seo-wordpress

# Exporter un visuel
.venv/Scripts/python src/canva.py --pin-id pin-001 --export

# Publier un pin
.venv/Scripts/python src/pinterest.py --pin-id pin-001 --publish

# Sync analytics
.venv/Scripts/python src/analytics.py --sync

# Dry-run complet
.venv/Scripts/python src/pinterest.py --pin-id pin-001 --publish --dry-run
```

## Canva

- Chemin A (Enterprise) : Autofill via `create-autofill-job`
- Chemin B (assiste) : `generate-design` / `generate-design-structured` + `export-design` via MCP
- Format : PNG 1000x1500, accent `#00D400`, typo Montserrat Bold

## Pinterest API

- Endpoints : `/media`, `/pins`, `/pins/{id}/analytics`, `/user_account/analytics/top_pins`
- Scopes : `boards:read`, `boards:write`, `pins:read`, `pins:write`, `user_accounts:read`
- Toujours tester en sandbox avant production

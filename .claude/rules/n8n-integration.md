---
description: Règles n8n — typeVersions, contraintes Code node, nommage
paths: ["systems/n8n/**", "systems/workflows/**"]
---

# n8n Integration

- **Instance** : `https://schoolswp-n8n.wp1.host` (hébergé — pas Docker local)
- **MCP** : configuré dans `.mcp.json` (ne pas modifier sans accord)
- **Règles complètes** : `systems/n8n/CLAUDE.md` et `systems/n8n/Règles du jeu – automatisation n8n.md`
- Ne jamais modifier les JSON de workflows à la main : passer par le MCP ou l'interface n8n
- **Workflows exportés** : `systems/workflows/workflows/`

## typeVersions max confirmées

| Node | Version max |
| --- | --- |
| scheduleTrigger | 1.2 |
| httpRequest | 4.2 |
| googleSheets | 4.5 |
| openAi (langchain) | 1.8 |
| code | 2 |
| set | 3.4 |
| if | 2.2 |
| merge | 3.1 |
| webhook | 2 |
| notion | 2.2 |
| airtable | 2.1 |

## Contraintes Code node (task runner n8n)

- `$helpers.httpRequest()` non disponible — utiliser un nœud HTTP Request séparé.
- `$input.all()` / `$input.first()` : **stripés** par le task runner → utiliser `items[0].json` à la place.
- `$('NodeName').item.json` dans un Code node : aussi stripé selon le contexte d'exécution → passer les données via un **Set node avec expressions** (le moteur d'expressions n8n supporte `$('NodeName').first().json.xxx`, pas le task runner Code).
- Pour passer des données d'un nœud non-adjacent : ajouter un Set node intermédiaire qui lit `$('NomNoeud').first().json.champ` et l'injecte dans l'item courant.

Contrainte Google Sheets : `appendOrUpdate` — le champ `matchingColumns` ne peut pas être vide.

## Nommage

**Workflows** : `[Status] Source > Destination: Description (ID)`

**Status** : `[InDev]` `[InTesting]` `[Staging]` `[Prod]` `[Offline]` `[ForDeletion]`

**Credentials** : `Service_Environment_Type` — ex: `GoogleSheets_Production_OAuth`

**Backup** : scripts dans `systems/n8n-backup/` (`backup-n8n.sh`, `restore-n8n.sh`). Déployer sur le serveur n8n, pas en local.

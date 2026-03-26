# CLAUDE.md — systems/n8n/

Règles et conventions pour les workflows n8n schoolsWP.

## typeVersions confirmées (max)

| Node | Version max | Notes |
|------|-------------|-------|
| scheduleTrigger | 1.2 | |
| httpRequest | 4.2 | |
| googleSheets | 4.5 | |
| openAi (langchain) | 1.8 | `@n8n/n8n-nodes-langchain.openAi` |
| code | 2 | |
| set | 3.4 | |
| if | 2.2 | |
| merge | 3.1 | |
| webhook | 2 | |
| notion | 2.2 | |
| airtable | 2.1 | |

## Webhook auth pattern

Tous les webhooks exposés doivent valider le secret via un Code node :

```javascript
// Validate Secret (Code node — toujours en premier après le Webhook)
const secret = $input.first().headers['x-webhook-secret'];
if (secret !== $vars.WEBHOOK_SECRET) {
  throw new Error('Unauthorized: invalid webhook secret');
}
return $input.all();
```

**Ne jamais hardcoder le secret** — toujours lire depuis `$vars.WEBHOOK_SECRET`.

## Variables n8n ($vars)

Toutes les valeurs sensibles sont stockées dans n8n Variables (Settings → Variables) :

| Variable | Usage |
|----------|-------|
| `WEBHOOK_SECRET` | Auth webhooks |
| `DISCORD_WEBHOOK_SEO` | Notifications Discord canal SEO |
| `THRUUU_JWT` | Bearer token API Thruuu (rotation 90j) |
| `AIRTABLE_BASE_ID` | ID base Airtable articles |
| `NOTION_KPI_DB_ID` | ID DB Notion KPI semaine |
| `NOTION_ARTICLES_DB_ID` | ID DB Notion articles |
| `GSHEET_SCORES_ID` | ID Google Sheet scores |
| `N8N_API_KEY` | Clé API n8n (backup workflow) |

## Thruuu JWT — rotation

Le JWT Thruuu expire tous les ~30 jours. Procédure :
1. Récupérer nouveau token sur app.thruuu.com
2. Mettre à jour `THRUUU_JWT` dans n8n Variables
3. Le workflow `[Prod] Thruuu Token Health Check` alerte sur Discord si 401

## Code node — contraintes

- `$helpers.httpRequest()` **non disponible** dans le task runner n8n 2.0
- Utiliser un nœud **HTTP Request séparé** pour les appels HTTP depuis le Code
- `$vars.*` disponible en lecture dans les Code nodes et expressions

## Google Sheets — appendOrUpdate

Le champ `matchingColumns` **ne peut pas être vide** — toujours spécifier au moins une colonne de matching (ex: `keyword`, `workflow_id`, `id`).

## Nommage workflows

`[Status] Source > Destination: Description`

Status valides : `[InDev]` `[InTesting]` `[Staging]` `[Prod]` `[Offline]` `[ForDeletion]`

## Nommage credentials

`Service_Environment_Type` — ex: `GoogleSheets_Production_OAuth`, `Anthropic_Production_API`

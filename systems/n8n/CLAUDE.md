# CLAUDE.md — systems/n8n/

Contexte spécifique aux workflows n8n schoolsWP.

## Instance

- **URL** : `https://schoolswp-n8n.wp1.host` (hébergé — pas Docker local)
- **Accès** : via MCP `n8n-mcp` (config dans `.mcp.json` à la racine du projet)
- **Règles complètes** : `Règles du jeu – automatisation n8n.md` (ce répertoire)

## typeVersions — CRITIQUE

Le MCP retourne les dernières versions disponibles dans sa base, qui peuvent être plus récentes que ce que l'instance supporte. **Toujours utiliser les versions confirmées** (stockées dans l'auto-memory).

Versions max confirmées sur cette instance :

| Node | Version max |
|---|---|
| scheduleTrigger | 1.2 |
| httpRequest | 4.2 |
| googleSheets | 4.5 |
| openAi (langchain) | 1.8 |
| code | 2 |
| set | 3.4 |
| if | 2.2 |
| merge | 3.1 |

## Nommage obligatoire

**Workflows** : `[Status] Source > Destination: Description (ID)`
**Status** : `[InDev]` `[InTesting]` `[Staging]` `[Prod]` `[Offline]` `[ForDeletion]`
**Credentials** : `Service_Environment_Type` — ex: `GoogleSheets_Production_OAuth`

## Workflows exportés

Fichiers JSON dans `workflows/` — exports manuels depuis l'interface n8n.
Ne jamais modifier les JSON à la main : passer par le MCP ou l'interface.

## Code node — contraintes

- `$helpers.httpRequest()` **non disponible** dans le task runner n8n 2.0
- Pour les appels HTTP depuis un Code node : utiliser un nœud HTTP Request séparé
- `appendOrUpdate` (Google Sheets) : `matchingColumns` ne peut pas être vide

## Gestion des secrets — Variables n8n ($vars)

**Règle** : aucun token ou clé API ne doit être hardcodé dans un nœud Code ou HTTP.
Passer par `Settings → Variables` dans l'interface n8n.

### Variables à configurer (Settings → Variables)

| Variable | Usage | Workflows concernés |
|---|---|---|
| `WEBHOOK_SECRET_GEO_FILL` | Auth webhook GEO Architect Bulk Fill | `3JE0YzrhoiusJZ6T` |
| `WEBHOOK_SECRET_THRUUU` | Auth webhook Thruuu Monitoring Results | `Im1Khan3gJwhJkuu` |
| `WEBHOOK_SECRET_AGENT` | Auth webhook Agent Orchestrator Callback | `WocLwnUAZPaZFitG` |
| `THRUUU_TOKEN` | Bearer token API Thruuu (JWT) | GEO Architect Bulk Fill |

### Pattern d'authentification webhook (standard schoolsWP)

Insérer un nœud Code `Validate Secret` juste après chaque Webhook :

```javascript
const expectedSecret = ($vars && $vars.WEBHOOK_SECRET_XXX) ? $vars.WEBHOOK_SECRET_XXX.trim() : '';
const providedSecret = ($input.first().headers['x-webhook-secret'] || '').trim();
if (!expectedSecret) { throw new Error('Security: WEBHOOK_SECRET_XXX not configured in n8n Variables'); }
if (providedSecret !== expectedSecret) { throw new Error('401 Unauthorized: invalid webhook secret'); }
return $input.all();
```

### Pattern lecture token depuis $vars (ex: Thruuu)

Dans un nœud Code, lire le token via :
```javascript
const token = ($vars && $vars.THRUUU_TOKEN) ? $vars.THRUUU_TOKEN.trim() : '';
if (!token) throw new Error('THRUUU_TOKEN non configuré dans n8n Variables');
```

**Note Thruuu** : le JWT expire tous les ~30 jours. À renouveler dans n8n Settings → Variables et dans le dashboard Thruuu. Voir `systems/security/rotation-policy.md` pour le calendrier.

# Spec — Workflow n8n `gsc-monitor-monthly`

> **Statut** : ✅ ACTIF depuis le 2026-05-28 (testé bout en bout, cron 1er du mois 9h Paris)
> **Workflow ID** : `uJHqrSylq1uKgc8Z`
> **URL** : https://schoolswp-n8n.wp1.host/workflow/uJHqrSylq1uKgc8Z
> **Cible** : workflow n8n sur `https://schoolswp-n8n.wp1.host/`

## ⚡ Finalisation avant activation (état au 2026-05-28)

1. ~~Credential GSC~~ ✅ **FAIT le 2026-05-28** : credential `Google Search Console account` (id `2aeYRfnaaLhozl9Y`, type `googleSearchConsoleOAuth2Api`) créé + connecté + rattaché aux 2 nodes `GSC Current/Previous 28d`. **Testé** (exécution manuelle 34238, status success) : auth OK, 10 piliers matchés, rapport markdown généré. NB : `rowLimit` monté de 250 à 5000 pour capturer les piliers à faible trafic (sinon hors top 250 par clics → faux "aucune donnée").
2. ~~chatId Telegram~~ ✅ **FAIT le 2026-05-28** : chatId `1020689775` (user ID perso de Michael, source `.env` NEMOCLAW_TELEGRAM_ALLOWED_CHAT_IDS) renseigné dans `Notify Telegram`. Pré-requis : Michael doit avoir fait `/start` avec le bot `schoolswp_yt_bot` sinon le bot ne peut pas initier le DM (403).
3. ~~Dossier Drive~~ ✅ **FAIT le 2026-05-28** : dossier `schoolsWP - Audits GSC monthly` (id `1o9-GWVYoa77bu5qS6DjJ8BHbZQ3Ksmcg`, compte michaelkihlpro@gmail.com) créé + câblé sur `Archive to Drive`. Test confirmé : `gsc-monthly-2026-05.md` archivé dedans.
4. ~~2 piliers manquants~~ ✅ **FAIT le 2026-05-28** : les 10 piliers sont câblés (SEO = `/seo-wordpress/`, Ecommerce = `/ecommerce-wordpress/`, hubs de catégorie validés GSC). Plus rien à ajouter ni corriger côté piliers.
5. ~~Activer~~ ✅ **FAIT le 2026-05-28** : workflow activé (`active: true`) après test complet bout en bout réussi (exécution 34247, envois réels Discord BOTS + Telegram + Drive confirmés). 1re vraie exécution planifiée : 1er du mois prochain 9h Paris.

### Corrections de slugs appliquées le 2026-05-28 (validation terrain Michael + GSC/WP)
- `fluentcrm-automatisations-indispensables` → `fluentcrm-automations-indispensables` (slug réel sans "ati")
- `ottokit-vs-zapier` (inexistant) → `suretriggers-vs-zapier` (post 54309, FR de l'EN `suretriggers-ottokit-vs-zapier`)
- `core-web-vitals-wordpress` + `hebergement-wordpress` : confirmés OK
- Corrections appliquées **à la fois** dans `pillars.yaml` et dans le node `Prepare GSC Dates & Pillars` du workflow live (patchNodeField, versionId `fe86f009`).

## ✅ Credentials déjà câblés
- Node `Notify Telegram` → `Telegram - schoolswp_yt_bot` (telegramApi) — auto-câblé à la création
- Node `Archive to Drive` → `Google Drive - schoolsWP` (googleDriveOAuth2Api) — auto-câblé à la création
- Node `Notify Discord` → `Discord - schoolsWP - ⏐🤖⏐ʙᴏᴛꜱ` (discordWebhookApi, id `7jPmTW9DQTLNPUxz`, canal BOTS) — câblé le 2026-05-28 (node converti de HTTP placeholder vers node Discord natif, `operation=sendLegacy`)

> ⚠️ Vérifier que `schoolswp_yt_bot` est bien le bon bot (sinon swapper vers le bot orchestrateur). Vérifier aussi le folder Drive cible (par défaut racine — créer/choisir "schoolsWP / Audits / GSC monthly").

---

> **Date spec initiale** : 2026-05-27
> **Note** : la section ci-dessous documente l'architecture de référence (le workflow réel suit ce design).

---

## 1. Objectif

Pousser chaque 1er du mois à 9h Paris un rapport GSC consolidé sur les 10 piliers schoolsWP (positions, clics, impressions, CTR) avec deltas vs M-1, vers 3 canaux : Discord webhook, Telegram bot, Google Drive (archive markdown daté).

## 2. Sources de vérité

- **Liste des piliers** : [tools/scripts/gsc-monitor/pillars.yaml](../../../tools/scripts/gsc-monitor/pillars.yaml) (8 confirmés + 2 TODO Michael)
- **Script local équivalent** : [tools/scripts/gsc-monitor/gsc_monthly_report.py](../../../tools/scripts/gsc-monitor/gsc_monthly_report.py) (dry-run testé OK le 2026-05-27)
- **Pattern n8n existant** : routine `plugins-snapshot` (lundis 9h Paris) — mémoire `reference_routine_plugins_snapshot.md`

## 3. Cron + fuseau

- Cron : `0 7 1 * *` (= 9h Paris en CEST été / 8h Paris en CET hiver)
- Rebump CET fin octobre → passer à `0 8 1 * *` pour rester à 9h Paris (pattern Michael)

## 4. Architecture nodes

```
[Schedule Trigger v1.3]
     │ cron "0 7 1 * *"
     ▼
[Code v2 : Load pillars] mode=runOnceForAllItems
     │ output = array of 10 {id, label, url, confirmed}
     │ (hardcoder pillars dans le code OU lire depuis Google Sheets sur Drive)
     ▼
[Split In Batches v3] batchSize=1
     │
     ▼ (loop)
[HTTP Request v4.4 : GSC current 28d]
     │ method: POST
     │ URL: https://searchconsole.googleapis.com/webmasters/v3/sites/https%3A%2F%2Fschoolswp.com%2F/searchAnalytics/query
     │ auth: Google OAuth2 API (credential 'gsc-schoolswp' déjà câblé côté n8n)
     │ body: {
     │   "startDate": "<28j avant fin de mois M-1>",
     │   "endDate": "<dernier jour de mois M-1>",
     │   "dimensions": ["page"],
     │   "rowLimit": 1,
     │   "dimensionFilterGroups": [{
     │     "filters": [{"dimension": "page", "operator": "equals", "expression": "{{ $json.url }}"}]
     │   }]
     │ }
     ▼
[HTTP Request v4.4 : GSC previous 28d] (mêmes params, dates M-2)
     ▼
[Code v2 : Compute delta & build row] mode=runOnceForEachItem
     │ output = {pillar, clicks, dClicks%, position, dPosition, impressions, dImpressions%, alert}
     │ alert = "ROUGE" si position dégrade >3, clics -30%, impressions -40% (seuils pillars.yaml)
     ▼ (back to loop until all 10 done)
[Aggregate v1 : combine all rows]
     │ output = single item with rows[] array + summary stats
     ▼
[Code v2 : Format markdown report]
     │ output = {markdown, telegramText, discordContent, dateLabel}
     ▼
[Parallel branches via Merge]
     ├──▶ [HTTP Request : Discord webhook]
     │       POST {webhook_url} { content: discordContent }
     │
     ├──▶ [Telegram v1.2 : sendMessage]
     │       chat_id = "{{ $env.TELEGRAM_CHAT_ID_MICHAEL }}"
     │       text = telegramText (markdown_v2 parse mode)
     │
     └──▶ [Google Drive v3 : createFromText]
             folder = "schoolsWP / Audits / GSC monthly"
             filename = "gsc-monthly-{{ $now.toFormat('yyyy-MM') }}.md"
             content = markdown
```

## 5. Credentials n8n requis

| Credential n8n | Type | Usage | À vérifier |
|---|---|---|---|
| `gsc-schoolswp` | Google OAuth2 | HTTP Request → Search Console API | Probablement déjà câblé pour autres workflows. Sinon : créer via n8n UI, scope `https://www.googleapis.com/auth/webmasters.readonly` |
| `discord-routines-webhook` | Generic / Header Auth | Webhook URL stockée comme env var ou direct dans node | URL webhook = canal `#schoolswp-routines` (mémoire `reference_discord_webhook_routines.md`) |
| `telegram-schoolswp-bot` | Telegram API | Token de `@schoolswp_bot` | Probablement déjà câblé (mémoire `project_telegram_ecosystem_welcome.md`) |
| `google-drive-michael` | Google OAuth2 | Drive node | Probablement déjà câblé pour les exports |

## 6. Format de sortie

### Discord webhook (markdown allégé, ≤2000 char)
```
**Rapport GSC schoolsWP — Mai 2026**
Période : 2026-04-03 → 2026-04-30 (vs 2026-03-06 → 2026-04-02)

🟢 LMS pilier : 12→18 clics (+50%), pos 8.3→5.1 (+3.2)
🟢 Kadence : 63→71 clics (+13%), pos 7.6→6.9 (+0.7)
🔴 5euros : 68→42 clics (-38%), pos 8.0→11.4 (-3.4) — ALERTE
...

Top mover : LMS pilier (+3.2 rangs)
Risque : 5euros (-38% clics)

Archive : drive.google.com/...
```

### Telegram (markdown v2, plus court, focus alertes)
```
*GSC schoolsWP — Mai 2026*

🔴 *5euros* −38% clics, pos −3.4 rangs
🟢 *LMS pilier* +50% clics, pos +3.2 rangs

Détails : Drive (lien)
```

### Drive archive (markdown complet)
Format `content/audits/gsc-monthly/YYYY-MM.md` (cf. template généré par le script local v1).

## 7. Seuils d'alerte (de pillars.yaml)
- `position_drop: 3` (perd 3+ rangs)
- `clicks_drop_pct: 30` (clics baissent ≥30% vs M-1)
- `impressions_drop_pct: 40` (impressions ≥40%)

## 8. Procédure de création du workflow

À faire en **session courte dédiée** (~30 min) :

1. Lancer Claude Code avec le MCP `claude_ai_n8n` connecté
2. `get_sdk_reference` (déjà documenté ici)
3. `get_node_types` pour les 6 nodes ci-dessous avec discriminators :
   ```js
   [
     "n8n-nodes-base.scheduleTrigger",
     {nodeId: "n8n-nodes-base.code", mode: "runOnceForAllItems"},
     "n8n-nodes-base.httpRequest",
     "n8n-nodes-base.splitInBatches",
     {nodeId: "n8n-nodes-base.discord", resource: "message", operation: "sendLegacy"},
     {nodeId: "n8n-nodes-base.telegram", resource: "message", operation: "sendMessage"},
     {nodeId: "n8n-nodes-base.googleDrive", resource: "file", operation: "createFromText"}
   ]
   ```
4. Écrire le workflow SDK en suivant le diagramme de la section 4
5. `validate_workflow` (itérer jusqu'à OK)
6. `create_workflow_from_code` avec `name: "gsc-monitor-monthly"` et `description: "Rapport GSC mensuel sur 10 piliers schoolsWP avec deltas vs M-1, notifie Discord/Telegram/Drive"`
7. Activer le workflow côté n8n UI (toggle Active = ON)
8. Première exécution manuelle pour vérifier (1er juin sera la vraie 1ère prod)

## 9. Points en suspens à clarifier avant création

- [ ] Michael : compléter les 2 piliers manquants (SEO + Ecommerce/FluentCart) dans pillars.yaml
- [ ] Vérifier qu'un credential GSC OAuth est déjà actif côté n8n (sinon créer en pré-requis)
- [ ] Récupérer l'URL webhook Discord `#schoolswp-routines`
- [ ] Récupérer le chat_id Telegram de Michael (mémoire `reference_bots_messaging_sheet.md`)
- [ ] Choisir le folder Drive cible (créer "schoolsWP / Audits / GSC monthly" si absent)

## 10. Référence

- pillars.yaml : sources de vérité de la liste piliers
- gsc_monthly_report.py : équivalent local pour dev/test (dry-run dispo)
- verify_pillar_slugs.py : vérification existence URLs WP
- Mémoires liées : `reference_routine_plugins_snapshot.md`, `reference_discord_webhook_routines.md`, `project_notification_pipelines.md`, `reference_bots_messaging_sheet.md`

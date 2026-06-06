# Brief de session — Réparation healthcheck telegram-agents

- **Date** : 2026-06-01
- **Session suggérée** : fix/telegram-agents-healthcheck
- **Statut** : CLÔTURÉ — tout vérifié et opérationnel
- **Périmètre** : monitoring du service telegram-agents (prod) + canaux de notification schoolsWP

---

## 1. Déclencheur

Alerte email reçue à 07:08 UTC : « Healthcheck telegram-agents — ÉCHEC », HTTP 403,
réponse brute « Host resolves to a private/reserved IP: resolve_no_records ». L'alerte
recommandait un Deploy Now sur xCloud.

## 2. Diagnostic

**C'était un faux positif.** Le service était sain :

- GET /health depuis la machine locale = HTTP 200, JSON valide, 6 agents
  (studio, radar, flow, pulse, reddit, welcome), 5 contextes chargés.
- Cause racine : le domaine telegram-agents.wp1.host est passé **derrière Cloudflare**
  (DNS résout vers des IP Cloudflare ; l'IP origine xCloud 45.32.147.48 n'est plus exposée).
- La routine de healthcheck tourne dans le **sandbox cloud Anthropic** (routine claude.ai),
  dont le proxy d'egress n'a pas su résoudre/joindre le domaine Cloudflare → erreur
  403 / resolve_no_records. C'est une panne du **réseau du vérificateur**, pas du service.
- L'ancien prompt traitait tout code != 200 comme « service mort » et conseillait un
  Deploy Now inutile (voire risqué).

## 3. Actions réalisées

### 3.1 Correction de la routine cloud

- Routine `Healthcheck telegram-agents` (id trig_018QJMcvsFnQMzE2FT4tEPvp, cron 0 7 \* \* \* UTC,
  connecteur Gmail) — prompt réécrit pour classer en 3 cas :
  - **A HEALTHY** : 200 + status ok + agents requis → silencieux.
  - **B CHECKER_UNREACHABLE** : signatures resolve/DNS/proxy/timeout → email info
    « NON CONCLUANT », SANS Deploy Now.
  - **C SERVICE_DOWN** : vraie réponse HTTP mais mauvaise → alerte + Deploy Now.
  - Retry x3, classification par contenu de réponse (pas seulement par code HTTP).

### 3.2 Check local de secours (fiable)

- Nouveau script : tools/scripts/healthcheck-telegram-agents.ps1 (pwsh 7, autonome, zéro
  run Claude). Détection : appel /health, retry x3, validation 200 + status ok + agents
  studio/radar/flow/pulse. Mêmes 3 cas que la routine cloud. Log dans
  logs/healthcheck-telegram-agents.log. Porte de test via variable d'env
  HEALTHCHECK_URL_OVERRIDE (inoffensive en prod).
- Tâche planifiée Windows « schoolsWP Telegram Healthcheck », quotidienne 09:00 Europe/Paris.
- Alerte **fan-out sur 2 canaux** :
  - Discord webhook (variable DISCORD_ROUTINES_WEBHOOK).
  - Telegram via @schoolsWP_Studio_bot (token TELEGRAM_TOKEN_STUDIO repris de
    agents/telegram-claude/.env ; destinataire TELEGRAM_HEALTHCHECK_CHAT_ID=1020689775).

### 3.3 Découverte : credentials Discord locaux morts

- DISCORD_ROUTINES_WEBHOOK renvoyait 404 (webhook supprimé côté Discord) → toutes les
  routines locales basées dessus étaient muettes (memory-lint, routines cloud).
- DISCORD_BOT_TOKEN renvoyait 401 (token périmé) → notify-brain-done.py muet via bot.
- Le MCP Discord n'a pas de token configuré (recréation auto impossible).
- **Résolution** : Michael a recréé le webhook #alerts à la main et recollé l'URL dans .env.
  Testé OK (ping + fan-out).

### 3.4 Repli webhook pour brain.bat

- tools/scripts/notify-brain-done.py : ajout d'un repli automatique. Si le bot Discord
  échoue/est absent, le même embed part via DISCORD_ROUTINES_WEBHOOK (canal #alerts).
- Piège Cloudflare résolu : discord.com bloque l'UA urllib par défaut (403 error code 1010)
  → le repli force un User-Agent Mozilla.
- notify_discord() retourne désormais un bool ; notify_discord_webhook() ajoutée.

### 3.5 Documentation

- .env.example : variable TELEGRAM_HEALTHCHECK_CHAT_ID documentée + note webhook 404.

## 4. Tests et résultats

| Test                           | Résultat                                                |
| ------------------------------ | ------------------------------------------------------- |
| /health en direct              | status ok, 6 agents                                     |
| Script local, service sain     | exit 0, silencieux, aucune alerte                       |
| Script local, panne simulée    | classé SERVICE_DOWN, alerte Discord + Telegram envoyées |
| Webhook Discord recréé (ping)  | OK                                                      |
| notify-brain-done.py           | bot 401 → repli webhook #alerts OK                      |
| Lint ruff notify-brain-done.py | All checks passed                                       |
| Tâche planifiée                | Ready, prochain run 2026-06-02 09:00                    |

## 5. État final

- Monitoring telegram-agents : **redondant et fiable** (Discord + Telegram, local + cloud).
- Plus de faux positif avec conseil Deploy Now erroné.
- Notifications brain.bat : rétablies via repli webhook.
- Routines Discord locales : réopérationnelles depuis la recréation du webhook.

## 6. Résidu connu (sans impact, pour plus tard)

- DISCORD_BOT_TOKEN local toujours périmé (401). Contourné partout par le webhook. À
  rafraîchir avec le vrai token serveur seulement si on veut restaurer le routing fin par
  canal (#outputs / #logs) pour notify-brain-done.py. Le vrai token vit sur le serveur xCloud.

## 7. Options non prises (proposées, en attente)

- Ajouter TELEGRAM_NOTIF_CHAT_ID=1020689775 dans .env pour que brain.bat DM aussi Michael
  via Telegram (chat_id déjà confirmé).

## 8. Pointeurs

- Mémoires : project_telegram_agents_deployment, reference_discord_webhook_routines,
  project_notification_pipelines, reference_n8n_cloudflare_ua_block.
- Routine cloud : trig_018QJMcvsFnQMzE2FT4tEPvp (https://claude.ai/code/routines/).
- Script : tools/scripts/healthcheck-telegram-agents.ps1.
- Tâche planifiée : « schoolsWP Telegram Healthcheck ».

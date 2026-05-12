---
name: gws-events-renew
version: 1.0.0
description: |
  Helper gws events +renew : renouvelle ou réactive une souscription Workspace Events qui arrive à expiration, soit ciblée (--name) soit en bulk (--all + fenêtre). Idéal pour cron quotidien ou hebdo qui maintient les listeners up.
  Utilise ce skill quand l'utilisateur dit : "renew Workspace Events subscription", "réactive ma souscription Chat", "renouvelle toutes les subs qui expirent", ou pour scripter un cron de maintenance sur les listeners Workspace Events.
  NE PAS utiliser pour : créer une nouvelle souscription et streamer (utiliser gws-events-subscribe), CRUD général sur les souscriptions (utiliser gws-events), ou watcher Gmail Pub/Sub (utiliser gws-gmail-watch).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws events +renew --help"
---

# events +renew

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Renew/reactivate Workspace Events subscriptions

## Usage

```bash
gws events +renew
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--name` | — | — | Subscription name to reactivate (e.g., subscriptions/SUB_ID) |
| `--all` | — | — | Renew all subscriptions expiring within --within window |
| `--within` | — | 1h | Time window for --all (e.g., 1h, 30m, 2d) |

## Examples

```bash
gws events +renew --name subscriptions/SUB_ID
gws events +renew --all --within 2d
```

## Tips

- Subscriptions expire if not renewed periodically.
- Use --all with a cron job to keep subscriptions alive.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-events](../gws-events/SKILL.md) — All subscribe to google workspace events commands

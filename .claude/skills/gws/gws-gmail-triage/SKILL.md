---
name: gws-gmail-triage
version: 1.0.0
description: |
  Helper gws gmail +triage : résumé compact de l'inbox non lue (sender, subject, date), default 20 messages, --query pour custom search Gmail. Idéal pour standup matinal ou triage rapide en CLI.
  Utilise ce skill quand l'utilisateur dit : "qu'est-ce que j'ai en inbox", "triage Gmail", "mes mails non lus", "show unread", ou pour piloter un récap quotidien d'inbox.
  NE PAS utiliser pour : lire le contenu d'un message (utiliser gws-gmail-read), watcher en temps réel (utiliser gws-gmail-watch), résumé multi-services standup (utiliser gws-workflow-standup-report qui agrège meetings + tasks).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws gmail +triage --help"
---

# gmail +triage

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Show unread inbox summary (sender, subject, date)

## Usage

```bash
gws gmail +triage
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--max` | — | 20 | Maximum messages to show (default: 20) |
| `--query` | — | — | Gmail search query (default: is:unread) |
| `--labels` | — | — | Include label names in output |

## Examples

```bash
gws gmail +triage
gws gmail +triage --max 5 --query 'from:boss'
gws gmail +triage --format json | jq '.[].subject'
gws gmail +triage --labels
```

## Tips

- Read-only — never modifies your mailbox.
- Defaults to table output format.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-gmail](../gws-gmail/SKILL.md) — All send, read, and manage email commands

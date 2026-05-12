---
name: gws-workflow
version: 1.0.0
description: |
  Workflows cross-services Google Workspace via la CLI gws : agrège plusieurs APIs (Gmail + Calendar + Tasks + Drive + Chat) en une seule commande pour résoudre un cas d'usage productivité (standup, meeting prep, weekly digest, file announce, email-to-task).
  Utilise ce skill quand l'utilisateur dit : "workflow Google", "automate productivity", "list les helpers cross-services", ou pour découvrir quel workflow gws couvre déjà ton cas avant de coder un script custom.
  NE PAS utiliser pour : opération sur un seul service (utiliser gws-gmail / gws-calendar / etc.), workflow n8n côté schoolwp-n8n.wp1.host (utiliser le MCP n8n-mcp), ou pipeline de contenu schoolsWP (utiliser brain.bat, agents-py).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow --help"
---

# workflow (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws workflow <resource> <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| [`+standup-report`](../gws-workflow-standup-report/SKILL.md) | Today's meetings + open tasks as a standup summary |
| [`+meeting-prep`](../gws-workflow-meeting-prep/SKILL.md) | Prepare for your next meeting: agenda, attendees, and linked docs |
| [`+email-to-task`](../gws-workflow-email-to-task/SKILL.md) | Convert a Gmail message into a Google Tasks entry |
| [`+weekly-digest`](../gws-workflow-weekly-digest/SKILL.md) | Weekly summary: this week's meetings + unread email count |
| [`+file-announce`](../gws-workflow-file-announce/SKILL.md) | Announce a Drive file in a Chat space |

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws workflow --help

# Inspect a method's required params, types, and defaults
gws schema workflow.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.


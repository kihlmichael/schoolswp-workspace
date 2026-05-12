---
name: gws-workflow-email-to-task
version: 1.0.0
description: |
  Helper gws workflow +email-to-task : convertit un message Gmail (par ID) en entrée Google Tasks dans la tasklist voulue (default @default). Le titre, lien et metadata sont remplis auto depuis le mail.
  Utilise ce skill quand l'utilisateur dit : "transforme ce mail en tâche", "email to task", "Gmail → Google Tasks", "ajoute ce mail à ma to-do", ou pour scripter un triage inbox vers Tasks.
  NE PAS utiliser pour : lire un mail (utiliser gws-gmail-read), répondre à un mail (utiliser gws-gmail-reply), créer une tâche from scratch (utiliser gws-tasks), ou conversion vers FluentBoards (utiliser le MCP fluentboards).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow +email-to-task --help"
---

# workflow +email-to-task

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Convert a Gmail message into a Google Tasks entry

## Usage

```bash
gws workflow +email-to-task --message-id <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--message-id` | ✓ | — | Gmail message ID to convert |
| `--tasklist` | — | @default | Task list ID (default: @default) |

## Examples

```bash
gws workflow +email-to-task --message-id MSG_ID
gws workflow +email-to-task --message-id MSG_ID --tasklist LIST_ID
```

## Tips

- Reads the email subject as the task title and snippet as notes.
- Creates a new task — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

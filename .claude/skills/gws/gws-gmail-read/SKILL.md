---
name: gws-gmail-read
version: 1.0.0
description: |
  Helper gws gmail +read : lit un message Gmail par ID et extrait son body (plain ou html) et optionnellement les headers (From, To, Subject, Date). Sortie shell-friendly pour parsing par jq ou pipe.
  Utilise ce skill quand l'utilisateur dit : "lis le mail ID...", "récupère le contenu de ce message Gmail", "extract body Gmail", "récupère les headers", ou pour pipeline qui parse un mail entrant et le transforme.
  NE PAS utiliser pour : lister l'inbox non lue (utiliser gws-gmail-triage), répondre au message (utiliser gws-gmail-reply), convertir le mail en tâche (utiliser gws-workflow-email-to-task), ou recherche multi-messages (utiliser gws-gmail).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws gmail +read --help"
---

# gmail +read

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Read a message and extract its body or headers

## Usage

```bash
gws gmail +read --id <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--id` | ✓ | — | The Gmail message ID to read |
| `--headers` | — | — | Include headers (From, To, Subject, Date) in the output |
| `--format` | — | text | Output format (text, json) |
| `--html` | — | — | Return HTML body instead of plain text |
| `--dry-run` | — | — | Show the request that would be sent without executing it |

## Examples

```bash
gws gmail +read --id 18f1a2b3c4d
gws gmail +read --id 18f1a2b3c4d --headers
gws gmail +read --id 18f1a2b3c4d --format json | jq '.body'
```

## Tips

- Converts HTML-only messages to plain text automatically.
- Handles multipart/alternative and base64 decoding.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-gmail](../gws-gmail/SKILL.md) — All send, read, and manage email commands

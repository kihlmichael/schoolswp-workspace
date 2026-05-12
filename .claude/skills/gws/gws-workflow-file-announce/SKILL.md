---
name: gws-workflow-file-announce
version: 1.0.0
description: |
  Helper gws workflow +file-announce : annonce un fichier Drive (par ID) dans un space Google Chat avec carte enrichie (titre, type, owner, lien). Une commande shell pour notifier l'équipe d'un livrable.
  Utilise ce skill quand l'utilisateur dit : "annonce ce fichier dans Chat", "post Drive file in space", "notifie le team du nouveau Doc", "Drive → Chat space", ou pour brancher un workflow "upload Drive puis annonce".
  NE PAS utiliser pour : envoyer un message texte simple (utiliser gws-chat-send), uploader le fichier sur Drive en amont (utiliser gws-drive-upload puis chaîner), ou annonce sur Discord / Telegram (utiliser le MCP discord ou telegram).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow +file-announce --help"
---

# workflow +file-announce

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Announce a Drive file in a Chat space

## Usage

```bash
gws workflow +file-announce --file-id <ID> --space <SPACE>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--file-id` | ✓ | — | Drive file ID to announce |
| `--space` | ✓ | — | Chat space name (e.g. spaces/SPACE_ID) |
| `--message` | — | — | Custom announcement message |
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +file-announce --file-id FILE_ID --space spaces/ABC123
gws workflow +file-announce --file-id FILE_ID --space spaces/ABC123 --message 'Check this out!'
```

## Tips

- This is a write command — sends a Chat message.
- Use `gws drive +upload` first to upload the file, then announce it here.
- Fetches the file name from Drive to build the announcement.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

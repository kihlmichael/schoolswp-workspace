---
name: gws-chat-send
version: 1.0.0
description: |
  Helper gws chat +send : envoie un message texte dans un space Google Chat (spaces/AAAA...). Une commande shell pour notifier équipe ou robot, parfait pour pipelines CI ou notifications n8n.
  Utilise ce skill quand l'utilisateur dit : "envoie un message Google Chat", "ping le space X", "notifie la team sur Chat", "post dans le space LMS", ou pour brancher une alerte Chat dans un workflow.
  NE PAS utiliser pour : opérations de gestion de space ou membership (utiliser gws-chat), annoncer un fichier Drive avec carte enrichie (utiliser gws-workflow-file-announce), ou notifier Discord (utiliser le MCP discord).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws chat +send --help"
---

# chat +send

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Send a message to a space

## Usage

```bash
gws chat +send --space <NAME> --text <TEXT>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--space` | ✓ | — | Space name (e.g. spaces/AAAA...) |
| `--text` | ✓ | — | Message text (plain text) |

## Examples

```bash
gws chat +send --space spaces/AAAAxxxx --text 'Hello team!'
```

## Tips

- Use 'gws chat spaces list' to find space names.
- For cards or threaded replies, use the raw API instead.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-chat](../gws-chat/SKILL.md) — All manage chat spaces and messages commands

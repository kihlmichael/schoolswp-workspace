---
name: gws-docs-write
version: 1.0.0
description: |
  Helper gws docs +write : ajoute du texte (append) à un Google Doc existant, en plain text. Une commande shell pour journaliser, logger, ou pousser une note dans un Doc partagé.
  Utilise ce skill quand l'utilisateur dit : "ajoute X à mon Google Doc", "log dans le Doc équipe", "append note dans gdoc", "écris dans le Doc ID...", ou pour un journal automatisé piloté par n8n.
  NE PAS utiliser pour : créer un nouveau Google Doc, formatage riche, batchUpdate avec styles ou tableaux (passer par l'API Docs raw, hors périmètre helper actuel), uploader un Doc existant depuis disque (utiliser gws-drive-upload avec conversion Google Docs).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws docs +write --help"
---

# docs +write

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Append text to a document

## Usage

```bash
gws docs +write --document <ID> --text <TEXT>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--document` | ✓ | — | Document ID |
| `--text` | ✓ | — | Text to append (plain text) |

## Examples

```bash
gws docs +write --document DOC_ID --text 'Hello, world!'
```

## Tips

- Text is inserted at the end of the document body.
- For rich formatting, use the raw batchUpdate API instead.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-docs](../gws-docs/SKILL.md) — All read and write google docs commands

---
name: gws-drive-upload
version: 1.0.0
description: |
  Helper gws drive +upload : upload un fichier local vers Google Drive avec détection auto du MIME type, support parent folder et drive partagé. Une commande shell adaptée pour pipelines (export Sheets, snapshots, archives).
  Utilise ce skill quand l'utilisateur dit : "upload sur Drive", "push ce fichier sur Google Drive", "envoie ce CSV sur Drive", "save to shared drive", ou pour automatiser l'archivage de sorties d'agents Python.
  NE PAS utiliser pour : opérations de partage / permissions / move / rename (utiliser gws-drive), annoncer le fichier après upload dans un Chat space (utiliser gws-workflow-file-announce en aval), ou upload média WordPress (utiliser tools/wp-media-upload).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws drive +upload --help"
---

# drive +upload

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Upload a file with automatic metadata

## Usage

```bash
gws drive +upload <file>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `<file>` | ✓ | — | Path to file to upload |
| `--parent` | — | — | Parent folder ID |
| `--name` | — | — | Target filename (defaults to source filename) |

## Examples

```bash
gws drive +upload ./report.pdf
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive +upload ./data.csv --name 'Sales Data.csv'
```

## Tips

- MIME type is detected automatically.
- Filename is inferred from the local path unless --name is given.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-drive](../gws-drive/SKILL.md) — All manage files, folders, and shared drives commands

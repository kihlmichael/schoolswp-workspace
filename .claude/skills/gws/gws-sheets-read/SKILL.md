---
name: gws-sheets-read
version: 1.0.0
description: |
  Helper gws sheets +read : lit les valeurs d'une plage Google Sheets (spreadsheet ID + range A1, ex Sheet1!A1:B2). Sortie shell-friendly (json par défaut) pour piping.
  Utilise ce skill quand l'utilisateur dit : "read Google Sheets", "lis ce range Sheets", "récupère les valeurs du Sheet", "pull données Sheets en CLI", ou pour pipeline qui consomme des Sheets en input.
  NE PAS utiliser pour : ajouter des lignes (utiliser gws-sheets-append), opérations API avancées (utiliser gws-sheets), ou conversion d'un Sheet en visualisation (faire le rendu côté agent, ce helper fournit juste les valeurs brutes).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws sheets +read --help"
---

# sheets +read

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Read values from a spreadsheet

## Usage

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | ✓ | — | Spreadsheet ID |
| `--range` | ✓ | — | Range to read (e.g. 'Sheet1!A1:B2') |

## Examples

```bash
gws sheets +read --spreadsheet ID --range "Sheet1!A1:D10"
gws sheets +read --spreadsheet ID --range Sheet1
```

## Tips

- Read-only — never modifies the spreadsheet.
- For advanced options, use the raw values.get API.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-sheets](../gws-sheets/SKILL.md) — All read and write spreadsheets commands

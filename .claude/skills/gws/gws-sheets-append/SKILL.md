---
name: gws-sheets-append
version: 1.0.0
description: |
  Helper gws sheets +append : ajoute une ligne à un Google Sheet (spreadsheet ID + valeurs CSV). Idéal pour log, journal, dump récurrent depuis script ou n8n.
  Utilise ce skill quand l'utilisateur dit : "append row Google Sheets", "log dans un Sheet", "ajoute une ligne au tableau de bord", "push données dans Sheets", ou pour brancher une routine de log léger sans batchUpdate.
  NE PAS utiliser pour : lire des valeurs (utiliser gws-sheets-read), opérations avancées type formules / formatage / batchUpdate (utiliser gws-sheets), ou import CSV multi-colonnes Ninja Tables côté WordPress (différent stack, voir reference_ninja_tables_rest.md).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws sheets +append --help"
---

# sheets +append

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Append a row to a spreadsheet

## Usage

```bash
gws sheets +append --spreadsheet <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | ✓ | — | Spreadsheet ID |
| `--values` | — | — | Comma-separated values (simple strings) |
| `--json-values` | — | — | JSON array of rows, e.g. '[["a","b"],["c","d"]]' |

## Examples

```bash
gws sheets +append --spreadsheet ID --values 'Alice,100,true'
gws sheets +append --spreadsheet ID --json-values '[["a","b"],["c","d"]]'
```

## Tips

- Use --values for simple single-row appends.
- Use --json-values for bulk multi-row inserts.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-sheets](../gws-sheets/SKILL.md) — All read and write spreadsheets commands

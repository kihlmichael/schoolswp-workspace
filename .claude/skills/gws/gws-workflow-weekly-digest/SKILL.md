---
name: gws-workflow-weekly-digest
version: 1.0.0
description: |
  Helper gws workflow +weekly-digest : résumé hebdo combinant les meetings de la semaine (Calendar) et le compteur d'inbox non lue (Gmail). Sortie json / table / yaml / csv pour rapport vendredi soir ou lundi matin.
  Utilise ce skill quand l'utilisateur dit : "weekly digest", "récap de la semaine Workspace", "résumé hebdo Google", "what's coming this week", ou pour brancher un mail / Discord weekly automatisé.
  NE PAS utiliser pour : récap journalier (utiliser gws-workflow-standup-report), prep d'une réunion précise (utiliser gws-workflow-meeting-prep), ou audit GSC hebdo schoolsWP (utiliser le MCP gsc-mcp).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow +weekly-digest --help"
---

# workflow +weekly-digest

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Weekly summary: this week's meetings + unread email count

## Usage

```bash
gws workflow +weekly-digest
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +weekly-digest
gws workflow +weekly-digest --format table
```

## Tips

- Read-only — never modifies data.
- Combines calendar agenda (week) with gmail triage summary.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

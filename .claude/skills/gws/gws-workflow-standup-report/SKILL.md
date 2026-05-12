---
name: gws-workflow-standup-report
version: 1.0.0
description: |
  Helper gws workflow +standup-report : agrège les meetings du jour (Calendar) + les tâches ouvertes (Tasks) en un résumé standup, sortie json / table / yaml / csv. Idéal pour cron matinal Slack / Discord / Chat.
  Utilise ce skill quand l'utilisateur dit : "standup report", "résumé du matin", "meetings + tasks aujourd'hui", "daily digest Workspace", ou pour brancher un récap quotidien automatique vers Discord / Chat.
  NE PAS utiliser pour : agenda seul (utiliser gws-calendar-agenda), to-do Tasks seule (utiliser gws-tasks), récap hebdo avec inbox count (utiliser gws-workflow-weekly-digest), ou prep d'une réunion précise (utiliser gws-workflow-meeting-prep).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow +standup-report --help"
---

# workflow +standup-report

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Today's meetings + open tasks as a standup summary

## Usage

```bash
gws workflow +standup-report
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +standup-report
gws workflow +standup-report --format table
```

## Tips

- Read-only — never modifies data.
- Combines calendar agenda (today) with tasks list.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

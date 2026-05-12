---
name: gws-calendar-agenda
version: 1.0.0
description: |
  Helper gws calendar +agenda : liste les événements à venir sur tous les calendriers, avec filtres rapides today / tomorrow / this-week. Sortie shell-friendly pour piping (jq, n8n, standup).
  Utilise ce skill quand l'utilisateur dit : "qu'est-ce que j'ai aujourd'hui", "agenda demain", "mes prochains rdv", "events this week", ou pour brancher un standup automatisé.
  NE PAS utiliser pour : créer un événement (utiliser gws-calendar-insert), opérations API avancées type freebusy ou ACL (utiliser gws-calendar), ou résumé multi-services standup (utiliser gws-workflow-standup-report qui chaîne agenda + tasks).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws calendar +agenda --help"
---

# calendar +agenda

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Show upcoming events across all calendars

## Usage

```bash
gws calendar +agenda
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--today` | — | — | Show today's events |
| `--tomorrow` | — | — | Show tomorrow's events |
| `--week` | — | — | Show this week's events |
| `--days` | — | — | Number of days ahead to show |
| `--calendar` | — | — | Filter to specific calendar name or ID |
| `--timezone` | — | — | IANA timezone override (e.g. America/Denver). Defaults to Google account timezone. |

## Examples

```bash
gws calendar +agenda
gws calendar +agenda --today
gws calendar +agenda --week --format table
gws calendar +agenda --days 3 --calendar 'Work'
gws calendar +agenda --today --timezone America/New_York
```

## Tips

- Read-only — never modifies events.
- Queries all calendars by default; use --calendar to filter.
- Uses your Google account timezone by default; override with --timezone.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-calendar](../gws-calendar/SKILL.md) — All manage calendars and events commands

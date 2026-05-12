---
name: gws-calendar-insert
version: 1.0.0
description: |
  Helper gws calendar +insert : crée un événement Google Calendar avec summary, start, end, invités, lieu, rappels, en une seule commande shell. Idéal pour automatisation ponctuelle ou batch (n8n, scripts, recipes).
  Utilise ce skill quand l'utilisateur dit : "ajoute un événement", "crée un rdv dans Google Calendar", "bloque un créneau", "invite X et Y le tel jour", ou pour scripter des inserts répétés (relances, rappels équipe).
  NE PAS utiliser pour : explorer l'API Calendar complète (utiliser gws-calendar), lister mon agenda à venir (utiliser gws-calendar-agenda), batch d'invitations à un événement existant (utiliser le recipe recipe-batch-invite-to-event si présent), ou conversation libre côté claude.ai (utiliser le MCP Google_Calendar).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws calendar +insert --help"
---

# calendar +insert

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

create a new event

## Usage

```bash
gws calendar +insert --summary <TEXT> --start <TIME> --end <TIME>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--calendar` | — | primary | Calendar ID (default: primary) |
| `--summary` | ✓ | — | Event summary/title |
| `--start` | ✓ | — | Start time (ISO 8601, e.g., 2024-01-01T10:00:00Z) |
| `--end` | ✓ | — | End time (ISO 8601) |
| `--location` | — | — | Event location |
| `--description` | — | — | Event description/body |
| `--attendee` | — | — | Attendee email (can be used multiple times) |
| `--meet` | — | — | Add a Google Meet video conference link |

## Examples

```bash
gws calendar +insert --summary 'Standup' --start '2026-06-17T09:00:00-07:00' --end '2026-06-17T09:30:00-07:00'
gws calendar +insert --summary 'Review' --start ... --end ... --attendee alice@example.com
gws calendar +insert --summary 'Meet' --start ... --end ... --meet
```

## Tips

- Use RFC3339 format for times (e.g. 2026-06-17T09:00:00-07:00).
- The --meet flag automatically adds a Google Meet link to the event.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-calendar](../gws-calendar/SKILL.md) — All manage calendars and events commands

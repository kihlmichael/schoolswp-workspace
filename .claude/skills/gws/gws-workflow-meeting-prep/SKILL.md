---
name: gws-workflow-meeting-prep
version: 1.0.0
description: |
  Helper gws workflow +meeting-prep : prépare ta prochaine réunion (agenda, attendees, docs linkés depuis l'event Calendar). Sortie json / table / yaml / csv pour briefing rapide.
  Utilise ce skill quand l'utilisateur dit : "prépare ma prochaine réunion", "meeting prep Google", "qui assiste à mon prochain rdv", "docs linkés à ma réunion", ou pour brancher un briefing automatique 15 min avant le meeting.
  NE PAS utiliser pour : récap journalier (utiliser gws-workflow-standup-report), résumé hebdo (utiliser gws-workflow-weekly-digest), récupération de transcript après le meeting (utiliser gws-meet), ou création d'un nouveau meeting (utiliser gws-calendar-insert).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws workflow +meeting-prep --help"
---

# workflow +meeting-prep

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Prepare for your next meeting: agenda, attendees, and linked docs

## Usage

```bash
gws workflow +meeting-prep
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--calendar` | — | primary | Calendar ID (default: primary) |
| `--format` | — | — | Output format: json (default), table, yaml, csv |

## Examples

```bash
gws workflow +meeting-prep
gws workflow +meeting-prep --calendar Work
```

## Tips

- Read-only — never modifies data.
- Shows the next upcoming event with attendees and description.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-workflow](../gws-workflow/SKILL.md) — All cross-service productivity workflows commands

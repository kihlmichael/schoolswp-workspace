---
name: recipe-post-mortem-setup
version: 1.0.0
description: |
  Crée un Google Docs post-mortem avec sections types (Summary, Timeline, Root Cause, Action Items), planifie la réunion de revue, puis notifie l'équipe dans Chat. Setup incident en 3 mouvements.
  Utilise ce skill quand l'utilisateur dit : "lance le post-mortem", "prépare le RCA de l'incident X", "setup la review post-incident", ou pour démarrer un cycle post-mortem cross-canal après un incident.
  NE PAS utiliser pour : juste créer un Docs vide (utiliser gws-docs), planifier une réunion sans doc (utiliser recipe-schedule-recurring-event ou gws-calendar), ou notifier sans setup post-mortem (utiliser recipe-send-team-announcement).
metadata:
  openclaw:
    category: "recipe"
    domain: "engineering"
    requires:
      bins: ["gws"]
      skills: ["gws-docs", "gws-calendar", "gws-chat"]
---

# Set Up Post-Mortem

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-calendar`, `gws-chat`

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

## Steps

1. Create post-mortem doc: `gws docs +write --title 'Post-Mortem: [Incident]' --body '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'`
2. Schedule review meeting: `gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --attendee team@company.com --start '2026-03-16T14:00:00' --end '2026-03-16T15:00:00'`
3. Notify in Chat: `gws chat +send --space spaces/ENG_SPACE --text '🔍 Post-mortem scheduled for [Incident].'`


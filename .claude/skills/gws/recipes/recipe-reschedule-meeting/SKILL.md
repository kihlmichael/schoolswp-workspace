---
name: recipe-reschedule-meeting
version: 1.0.0
description: |
  Déplace un événement Google Calendar existant vers un nouveau créneau et notifie automatiquement les participants via sendUpdates=all. Patch ciblé sur start/end avec timezone.
  Utilise ce skill quand l'utilisateur dit : "reporte la réunion à demain", "décale ce meeting", "change l'horaire de l'événement et préviens tout le monde", ou pour replanifier un événement existant proprement.
  NE PAS utiliser pour : créer un nouvel événement (utiliser gws-calendar events insert ou recipe-schedule-recurring-event), annuler une réunion (utiliser gws-calendar events delete), ou prévenir sans bouger l'horaire (utiliser gws-gmail).
metadata:
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins: ["gws"]
      skills: ["gws-calendar"]
---

# Reschedule a Google Calendar Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Move a Google Calendar event to a new time and automatically notify all attendees.

## Steps

1. Find the event: `gws calendar +agenda`
2. Get event details: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
3. Update the time: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"start": {"dateTime": "2025-01-22T14:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-22T15:00:00", "timeZone": "America/New_York"}}'`


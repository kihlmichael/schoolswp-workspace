---
name: recipe-schedule-recurring-event
version: 1.0.0
description: |
  Crée un événement Google Calendar récurrent avec règle RRULE, attendees et timezone, puis vérifie sa création dans l'agenda. Standup hebdo, sync mensuelle, weekly review.
  Utilise ce skill quand l'utilisateur dit : "crée un standup récurrent tous les lundis", "planifie une weekly à répétition", "événement Calendar avec récurrence X", ou pour poser une cadence régulière dans l'agenda.
  NE PAS utiliser pour : déplacer une réunion existante (utiliser recipe-reschedule-meeting), planifier un one-shot non répété (utiliser gws-calendar events insert), ou planifier la semaine globale (utiliser recipe-plan-weekly-schedule).
metadata:
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins: ["gws"]
      skills: ["gws-calendar"]
---

# Schedule a Recurring Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Create a recurring Google Calendar event with attendees.

## Steps

1. Create recurring event: `gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Weekly Standup", "start": {"dateTime": "2024-03-18T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2024-03-18T09:30:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"], "attendees": [{"email": "team@company.com"}]}'`
2. Verify it was created: `gws calendar +agenda --days 14 --format table`


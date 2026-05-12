---
name: recipe-batch-invite-to-event
version: 1.0.0
description: |
  Ajoute une liste de participants a un evenement Google Calendar deja existant et declenche les notifications via sendUpdates=all.
  Utilise ce skill quand l'utilisateur dit : "invite ces personnes a la reunion", "ajoute X au meeting", "batch invite calendar", ou fournit une liste d'emails a coller sur un event existant.
  NE PAS utiliser pour : creer un nouvel evenement avec attendees (utiliser gws-calendar insert direct), trouver un creneau commun avant invitation (utiliser recipe-find-free-time), ou creer plusieurs events depuis un Sheet (utiliser recipe-create-events-from-sheet).
metadata:
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins: ["gws"]
      skills: ["gws-calendar"]
---

# Add Multiple Attendees to a Calendar Event

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Add a list of attendees to an existing Google Calendar event and send notifications.

## Steps

1. Get the event: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Add attendees: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"attendees": [{"email": "alice@company.com"}, {"email": "bob@company.com"}, {"email": "carol@company.com"}]}'`
3. Verify attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`


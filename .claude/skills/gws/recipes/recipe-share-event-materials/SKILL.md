---
name: recipe-share-event-materials
version: 1.0.0
description: |
  Récupère la liste des participants d'un événement Google Calendar et partage automatiquement un ou plusieurs fichiers Drive en lecture avec chacun. Pre-meeting prep côté Drive.
  Utilise ce skill quand l'utilisateur dit : "partage ces docs avec tous les invités du meeting", "envoie les supports aux attendees de la visio", "distribue les fichiers de la réunion", ou pour briefer les participants avant un événement.
  NE PAS utiliser pour : partager avec une liste fixe hors événement (utiliser recipe-share-doc-and-notify ou recipe-share-folder-with-team), planifier la réunion elle-même (utiliser gws-calendar), ou retracer la présence post-meeting (utiliser recipe-review-meet-participants).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-calendar", "gws-drive"]
---

# Share Files with Meeting Attendees

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`, `gws-drive`

Share Google Drive files with all attendees of a Google Calendar event.

## Steps

1. Get event attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Share file with each attendee: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "attendee@company.com"}'`
3. Verify sharing: `gws drive permissions list --params '{"fileId": "FILE_ID"}' --format table`


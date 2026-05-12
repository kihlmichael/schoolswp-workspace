---
name: recipe-find-free-time
version: 1.0.0
description: |
  Interroge la disponibilite Google Calendar de plusieurs utilisateurs via freebusy query, identifie les creneaux communs libres, et cree l'event sur le slot retenu.
  Utilise ce skill quand l'utilisateur dit : "trouve un creneau libre commun", "quand X et Y sont dispos", "cherche un slot reunion entre nous", ou veut une analyse free/busy multi-personnes avant invitation.
  NE PAS utiliser pour : ajouter des participants a un event existant deja date (utiliser recipe-batch-invite-to-event), bloquer du focus time sur son propre calendrier (utiliser recipe-block-focus-time), ou creer plusieurs events depuis un Sheet (utiliser recipe-create-events-from-sheet).
metadata:
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins: ["gws"]
      skills: ["gws-calendar"]
---

# Find Free Time Across Calendars

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Query Google Calendar free/busy status for multiple users to find a meeting slot.

## Steps

1. Query free/busy: `gws calendar freebusy query --json '{"timeMin": "2024-03-18T08:00:00Z", "timeMax": "2024-03-18T18:00:00Z", "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]}'`
2. Review the output to find overlapping free slots
3. Create event in the free slot: `gws calendar +insert --summary 'Meeting' --attendee user1@company.com --attendee user2@company.com --start '2024-03-18T14:00:00' --end '2024-03-18T14:30:00'`


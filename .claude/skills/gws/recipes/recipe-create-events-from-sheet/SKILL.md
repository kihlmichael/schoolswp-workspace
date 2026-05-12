---
name: recipe-create-events-from-sheet
version: 1.0.0
description: |
  Lit les donnees d'evenements depuis un Google Sheets et cree les entrees Google Calendar correspondantes ligne par ligne, avec attendees inclus.
  Utilise ce skill quand l'utilisateur dit : "cree les events depuis cette sheet", "import les rendez-vous du tableau dans Calendar", "transforme cette sheet en calendrier", ou a un planning tabule a deverser dans Calendar.
  NE PAS utiliser pour : ajouter des participants a un event existant (utiliser recipe-batch-invite-to-event), creer un seul event ponctuel (utiliser gws-calendar insert direct), ou bloquer du focus time recurrent (utiliser recipe-block-focus-time).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets", "gws-calendar"]
---

# Create Google Calendar Events from a Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-calendar`

Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.

## Steps

1. Read event data: `gws sheets +read --spreadsheet SHEET_ID --range "Events!A2:D"`
2. For each row, create a calendar event: `gws calendar +insert --summary 'Team Standup' --start '2026-01-20T09:00:00' --end '2026-01-20T09:30:00' --attendee alice@company.com --attendee bob@company.com`


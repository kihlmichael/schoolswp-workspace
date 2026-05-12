---
name: recipe-log-deal-update
version: 1.0.0
description: |
  Trouve la feuille de suivi pipeline, lit l'état courant et ajoute une nouvelle ligne pour tracer une mise à jour de deal commercial. Pattern append vers un CRM léger en Sheets.
  Utilise ce skill quand l'utilisateur dit : "log ce deal", "trace cette mise à jour pipeline", "ajoute la ligne deal dans le suivi", ou pour journaliser un changement de statut commercial dans un Sheets.
  NE PAS utiliser pour : créer la feuille pipeline initiale (utiliser gws-sheets), reporter sur les deals existants (utiliser recipe-generate-report-from-sheet), ou suivre des contacts hors deals (utiliser recipe-sync-contacts-to-sheet).
metadata:
  openclaw:
    category: "recipe"
    domain: "sales"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets", "gws-drive"]
---

# Log Deal Update to Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Append a deal status update to a Google Sheets sales tracking spreadsheet.

## Steps

1. Find the tracking sheet: `gws drive files list --params '{"q": "name = '\''Sales Pipeline'\'' and mimeType = '\''application/vnd.google-apps.spreadsheet'\''"}'`
2. Read current data: `gws sheets +read --spreadsheet SHEET_ID --range "Pipeline!A1:F"`
3. Append new row: `gws sheets +append --spreadsheet SHEET_ID --range 'Pipeline' --values '["2024-03-15", "Acme Corp", "Proposal Sent", "$50,000", "Q2", "jdoe"]'`


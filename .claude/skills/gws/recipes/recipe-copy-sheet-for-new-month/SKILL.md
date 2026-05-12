---
name: recipe-copy-sheet-for-new-month
version: 1.0.0
description: |
  Duplique un onglet template Google Sheets pour un nouveau mois de tracking, puis renomme l'onglet copie avec le nom du mois.
  Utilise ce skill quand l'utilisateur dit : "copie le template pour fevrier", "duplique l'onglet pour le nouveau mois", "prepare le tracker du mois prochain", ou veut un nouvel onglet mensuel base sur un modele.
  NE PAS utiliser pour : creer un nouveau Sheet entier vierge (utiliser gws-drive files create), backup du Sheet en CSV (utiliser recipe-backup-sheet-as-csv), ou setup un tracker des depenses depuis zero (utiliser recipe-create-expense-tracker).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets"]
---

# Copy a Google Sheet for a New Month

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Duplicate a Google Sheets template tab for a new month of tracking.

## Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Copy the template sheet: `gws sheets spreadsheets sheets copyTo --params '{"spreadsheetId": "SHEET_ID", "sheetId": 0}' --json '{"destinationSpreadsheetId": "SHEET_ID"}'`
3. Rename the new tab: `gws sheets spreadsheets batchUpdate --params '{"spreadsheetId": "SHEET_ID"}' --json '{"requests": [{"updateSheetProperties": {"properties": {"sheetId": 123, "title": "February 2025"}, "fields": "title"}}]}'`


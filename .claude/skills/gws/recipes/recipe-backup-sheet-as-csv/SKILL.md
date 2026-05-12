---
name: recipe-backup-sheet-as-csv
version: 1.0.0
description: |
  Exporte un Google Sheets en fichier CSV pour backup local ou traitement hors ligne. Recipe atomique qui combine gws-sheets et gws-drive.
  Utilise ce skill quand l'utilisateur dit : "backup ce Google Sheets", "exporte la sheet en CSV", "telecharge la sheet en local", ou demande une copie CSV figee d'un onglet.
  NE PAS utiliser pour : lire des cellules dans la session sans fichier (utiliser gws-sheets), telecharger un dossier complet de fichiers Drive (utiliser recipe-bulk-download-folder), ou exporter un Google Doc en PDF (utiliser gws-drive export direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets", "gws-drive"]
---

# Export a Google Sheet as CSV

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Export a Google Sheets spreadsheet as a CSV file for local backup or processing.

## Steps

1. Get spreadsheet details: `gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'`
2. Export as CSV: `gws drive files export --params '{"fileId": "SHEET_ID", "mimeType": "text/csv"}'`
3. Or read values directly: `gws sheets +read --spreadsheet SHEET_ID --range 'Sheet1' --format csv`


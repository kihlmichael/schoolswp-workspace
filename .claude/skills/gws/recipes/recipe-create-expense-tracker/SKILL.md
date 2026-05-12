---
name: recipe-create-expense-tracker
version: 1.0.0
description: |
  Configure depuis zero un Google Sheets de suivi de depenses avec en-tetes Date/Categorie/Description/Montant, premiere ligne d'exemple et partage manager en lecture.
  Utilise ce skill quand l'utilisateur dit : "monte un tracker de depenses", "cree un Sheet pour suivre mes frais", "setup un expense tracker partage", ou demarre un fichier de suivi budget perso ou pro.
  NE PAS utiliser pour : dupliquer un onglet template existant pour un nouveau mois (utiliser recipe-copy-sheet-for-new-month), exporter un Sheet en CSV (utiliser recipe-backup-sheet-as-csv), ou ajouter des lignes a un tracker deja construit (utiliser gws-sheets append direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets", "gws-drive"]
---

# Create a Google Sheets Expense Tracker

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.

## Steps

1. Create spreadsheet: `gws drive files create --json '{"name": "Expense Tracker 2025", "mimeType": "application/vnd.google-apps.spreadsheet"}'`
2. Add headers: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["Date", "Category", "Description", "Amount"]'`
3. Add first entry: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["2025-01-15", "Travel", "Flight to NYC", "450.00"]'`
4. Share with manager: `gws drive permissions create --params '{"fileId": "SHEET_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "manager@company.com"}'`


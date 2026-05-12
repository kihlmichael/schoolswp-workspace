---
name: recipe-generate-report-from-sheet
version: 1.0.0
description: |
  Lit les données d'un Google Sheets et génère un Google Docs formaté avec les insights. Pipeline read-then-write : Sheets en source, Docs en livrable.
  Utilise ce skill quand l'utilisateur dit : "génère un rapport depuis cette feuille", "transforme ces données en doc", "rapport mensuel à partir du Sheets", ou pour produire un livrable Docs lisible depuis un dataset tabulaire.
  NE PAS utiliser pour : juste lire un Sheets (utiliser gws-sheets directement), générer un dashboard live qui s'auto-met-à-jour (utiliser des formules ou Looker), ou créer un Docs vierge (utiliser gws-docs).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets", "gws-docs", "gws-drive"]
---

# Generate a Google Docs Report from Sheet Data

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-docs`, `gws-drive`

Read data from a Google Sheet and create a formatted Google Docs report.

## Steps

1. Read the data: `gws sheets +read --spreadsheet SHEET_ID --range "Sales!A1:D"`
2. Create the report doc: `gws docs documents create --json '{"title": "Sales Report - January 2025"}'`
3. Write the report: `gws docs +write --document-id DOC_ID --text '## Sales Report - January 2025

### Summary
Total deals: 45
Revenue: $125,000

### Top Deals
1. Acme Corp - $25,000
2. Widget Inc - $18,000'`
4. Share with stakeholders: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "cfo@company.com"}'`


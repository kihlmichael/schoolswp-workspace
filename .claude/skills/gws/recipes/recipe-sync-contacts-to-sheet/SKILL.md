---
name: recipe-sync-contacts-to-sheet
version: 1.0.0
description: |
  Liste l'annuaire Google Contacts (noms, emails, téléphones) et exporte chaque contact en ligne dans un Google Sheets. Pour bâtir un export annuaire exploitable hors Workspace.
  Utilise ce skill quand l'utilisateur dit : "exporte mes contacts dans un Sheets", "sync l'annuaire Google vers une feuille", "transforme mes Contacts en CRM léger", ou pour rapatrier l'annuaire vers Sheets.
  NE PAS utiliser pour : journaliser des deals commerciaux (utiliser recipe-log-deal-update), générer un rapport depuis un Sheets existant (utiliser recipe-generate-report-from-sheet), ou modifier les contacts eux-mêmes (utiliser gws-people).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-people", "gws-sheets"]
---

# Export Google Contacts to Sheets

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-people`, `gws-sheets`

Export Google Contacts directory to a Google Sheets spreadsheet.

## Steps

1. List contacts: `gws people people listDirectoryPeople --params '{"readMask": "names,emailAddresses,phoneNumbers", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' --format json`
2. Create a sheet: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Name", "Email", "Phone"]'`
3. Append each contact row: `gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Jane Doe", "jane@company.com", "+1-555-0100"]'`


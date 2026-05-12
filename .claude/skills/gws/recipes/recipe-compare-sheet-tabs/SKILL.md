---
name: recipe-compare-sheet-tabs
version: 1.0.0
description: |
  Compare deux onglets d'un meme Google Sheet et identifie les differences (lignes ajoutees, supprimees, modifiees, valeurs divergentes par cellule). Recipe gws qui lit les deux tabs et produit un rapport diff structure.
  Utilise ce skill quand l'utilisateur dit : "compare ces deux onglets", "quelles differences entre tab1 et tab2", "diff sheet tabs", "qu'est-ce qui a change entre la version A et B du Sheet", ou colle un Sheet avec deux onglets versionnes.
  NE PAS utiliser pour : comparer deux Sheets distincts (necessite extension custom), comparer deux versions historiques (utiliser revisions Drive), ou auditer un export GSC dans le temps (utiliser `content/audits/` snapshot system schoolsWP).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-sheets"]
---

# Compare Two Google Sheets Tabs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Read data from two tabs in a Google Sheet to compare and identify differences.

## Steps

1. Read the first tab: `gws sheets +read --spreadsheet SHEET_ID --range "January!A1:D"`
2. Read the second tab: `gws sheets +read --spreadsheet SHEET_ID --range "February!A1:D"`
3. Compare the data and identify changes


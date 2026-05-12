---
name: recipe-create-presentation
version: 1.0.0
description: |
  Cree une nouvelle presentation Google Slides vierge avec un titre, recupere son ID, et la partage en ecriture avec l'equipe.
  Utilise ce skill quand l'utilisateur dit : "cree un Google Slides pour la review trimestrielle", "ouvre un nouveau deck Slides partage", "demarre une presentation Google Slides", ou veut un deck Slides initial pret a editer en collab.
  NE PAS utiliser pour : un design HTML brand-strict de slide deck (utiliser external-cc-design en T1), generer des variantes design exploration (utiliser aidesigner-frontend en T0), ou peupler les slides avec un script (utiliser gws-slides direct apres creation).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-slides"]
---

# Create a Google Slides Presentation

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-slides`

Create a new Google Slides presentation and add initial slides.

## Steps

1. Create presentation: `gws slides presentations create --json '{"title": "Quarterly Review Q2"}'`
2. Get the presentation ID from the response
3. Share with team: `gws drive permissions create --params '{"fileId": "PRESENTATION_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`


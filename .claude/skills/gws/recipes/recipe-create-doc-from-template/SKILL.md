---
name: recipe-create-doc-from-template
version: 1.0.0
description: |
  Copie un template Google Docs, injecte le contenu via gws-docs write, puis partage le doc resultant avec les collaborateurs.
  Utilise ce skill quand l'utilisateur dit : "cree un brief depuis le template", "duplique le modele Doc et remplis-le", "genere un Doc a partir du template projet", ou veut industrialiser la production de docs depuis un modele standard.
  NE PAS utiliser pour : creer un Doc vierge sans template (utiliser gws-drive files create + gws-docs), envoyer le contenu d'un Doc par mail (utiliser recipe-draft-email-from-doc), ou partager seulement le lien sans dupliquer (utiliser recipe-email-drive-link).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive", "gws-docs"]
---

# Create a Google Doc from a Template

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`

Copy a Google Docs template, fill in content, and share with collaborators.

## Steps

1. Copy the template: `gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2 Launch"}'`
2. Get the new doc ID from the response
3. Add content: `gws docs +write --document-id NEW_DOC_ID --text '## Project: Q2 Launch

### Objective
Launch the new feature by end of Q2.'`
4. Share with team: `gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`


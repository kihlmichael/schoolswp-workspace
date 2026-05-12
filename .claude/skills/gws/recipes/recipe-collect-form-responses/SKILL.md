---
name: recipe-collect-form-responses
version: 1.0.0
description: |
  Recupere et passe en revue les reponses soumises sur un Google Form, avec rendu en table pour lecture rapide.
  Utilise ce skill quand l'utilisateur dit : "montre les reponses du formulaire", "qui a repondu au form", "recupere les submissions Google Forms", ou veut auditer les retours d'un form existant.
  NE PAS utiliser pour : creer un nouveau formulaire de feedback (utiliser recipe-create-feedback-form), envoyer le lien du form par email (utiliser recipe-create-feedback-form qui combine les deux), ou exporter les reponses en CSV (utiliser gws-forms puis gws-sheets manuellement).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-forms"]
---

# Check Form Responses

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`

Retrieve and review responses from a Google Form.

## Steps

1. List forms: `gws forms forms list` (if you don't have the form ID)
2. Get form details: `gws forms forms get --params '{"formId": "FORM_ID"}'`
3. Get responses: `gws forms forms responses list --params '{"formId": "FORM_ID"}' --format table`


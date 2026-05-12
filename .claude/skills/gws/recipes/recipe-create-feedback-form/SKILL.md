---
name: recipe-create-feedback-form
version: 1.0.0
description: |
  Cree un Google Form de feedback simple et partage le lien responder via Gmail aux destinataires cibles.
  Utilise ce skill quand l'utilisateur dit : "cree un form de feedback et envoie-le", "fais un Google Forms et partage-le par mail", "lance une enquete de satisfaction", ou veut un form leger expedie immediatement par email.
  NE PAS utiliser pour : recuperer les reponses d'un form deja existant (utiliser recipe-collect-form-responses), creer un form complexe avec sections et logique (utiliser gws-forms direct), ou envoyer un email sans form attache (utiliser gws-gmail send direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-forms", "gws-gmail"]
---

# Create and Share a Google Form

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`, `gws-gmail`

Create a Google Form for feedback and share it via Gmail.

## Steps

1. Create form: `gws forms forms create --json '{"info": {"title": "Event Feedback", "documentTitle": "Event Feedback Form"}}'`
2. Get the form URL from the response (responderUri field)
3. Email the form: `gws gmail +send --to attendees@company.com --subject 'Please share your feedback' --body 'Fill out the form: FORM_URL'`


---
name: recipe-forward-labeled-emails
version: 1.0.0
description: |
  Cherche les messages Gmail portant un libellé donné, lit leur contenu, et les transfère vers une autre adresse mail. Utile pour escalader, déléguer ou centraliser les emails étiquetés.
  Utilise ce skill quand l'utilisateur dit : "transfère les mails labellisés X", "forward les emails avec ce libellé à Y", "escalade les emails review au manager", ou pour automatiser un dispatch d'emails étiquetés.
  NE PAS utiliser pour : envoyer un email standard (utiliser gws-gmail directement), créer ou gérer les libellés Gmail (utiliser gws-gmail labels), ou archiver les emails dans Docs (utiliser recipe-save-email-to-doc).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail"]
---

# Forward Labeled Gmail Messages

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Find Gmail messages with a specific label and forward them to another address.

## Steps

1. Find labeled messages: `gws gmail users messages list --params '{"userId": "me", "q": "label:needs-review"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Forward via new email: `gws gmail +send --to manager@company.com --subject 'FW: [Original Subject]' --body 'Forwarding for your review:

[Original Message Body]'`


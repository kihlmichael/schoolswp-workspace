---
name: recipe-draft-email-from-doc
version: 1.0.0
description: |
  Lit le contenu d'un Google Doc existant et l'utilise comme corps de message Gmail envoye au destinataire.
  Utilise ce skill quand l'utilisateur dit : "envoie le contenu de ce Doc par mail", "envoie cette newsletter Doc par Gmail", "transforme ce Doc en email", ou veut deverser un Doc redige dans un mail sortant.
  NE PAS utiliser pour : creer un Doc depuis un template avant envoi (utiliser recipe-create-doc-from-template), partager seulement le lien Drive du Doc sans copier le contenu (utiliser recipe-email-drive-link), ou rediger un email from scratch (utiliser gws-gmail send direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-docs", "gws-gmail"]
---

# Draft a Gmail Message from a Google Doc

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-gmail`

Read content from a Google Doc and use it as the body of a Gmail message.

## Steps

1. Get the document content: `gws docs documents get --params '{"documentId": "DOC_ID"}'`
2. Copy the text from the body content
3. Send the email: `gws gmail +send --to recipient@example.com --subject 'Newsletter Update' --body 'CONTENT_FROM_DOC'`


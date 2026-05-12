---
name: recipe-save-email-to-doc
version: 1.0.0
description: |
  Récupère le contenu d'un message Gmail (sujet, expéditeur, corps) et le sauvegarde dans un nouveau Google Docs pour archivage durable ou référence ultérieure.
  Utilise ce skill quand l'utilisateur dit : "archive cet email en doc", "sauvegarde ce mail important dans Drive", "transforme cet email en référence Docs", ou pour figer un message Gmail hors de la boîte mail.
  NE PAS utiliser pour : sauvegarder les pièces jointes Gmail (utiliser recipe-save-email-attachments), transférer un mail à quelqu'un (utiliser recipe-forward-labeled-emails), ou créer un Docs sans email source (utiliser gws-docs).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail", "gws-docs"]
---

# Save a Gmail Message to Google Docs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-docs`

Save a Gmail message body into a Google Doc for archival or reference.

## Steps

1. Find the message: `gws gmail users messages list --params '{"userId": "me", "q": "subject:important from:boss@company.com"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Create a doc with the content: `gws docs documents create --json '{"title": "Saved Email - Important Update"}'`
4. Write the email body: `gws docs +write --document-id DOC_ID --text 'From: boss@company.com
Subject: Important Update

[EMAIL BODY]'`


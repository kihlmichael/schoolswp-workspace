---
name: recipe-save-email-attachments
version: 1.0.0
description: |
  Cherche les emails Gmail avec pièces jointes selon une requête, télécharge les attachments, puis les uploade dans un dossier Google Drive cible. Pipeline archivage Gmail vers Drive.
  Utilise ce skill quand l'utilisateur dit : "sauvegarde les pièces jointes du client X dans Drive", "archive les attachments de ce thread", "transfère les fichiers email vers Drive", ou pour exfiltrer des PJ vers Drive.
  NE PAS utiliser pour : sauvegarder le corps d'un email en Doc (utiliser recipe-save-email-to-doc), juste lister les emails avec PJ (utiliser gws-gmail), ou uploader un fichier local sans passer par Gmail (utiliser gws-drive upload).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail", "gws-drive"]
---

# Save Gmail Attachments to Google Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-drive`

Find Gmail messages with attachments and save them to a Google Drive folder.

## Steps

1. Search for emails with attachments: `gws gmail users messages list --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' --format table`
2. Get message details: `gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'`
3. Download attachment: `gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MESSAGE_ID", "id": "ATTACHMENT_ID"}'`
4. Upload to Drive folder: `gws drive +upload --file ./attachment.pdf --parent FOLDER_ID`


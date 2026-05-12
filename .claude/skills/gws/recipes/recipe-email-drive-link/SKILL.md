---
name: recipe-email-drive-link
version: 1.0.0
description: |
  Partage un fichier Google Drive avec un destinataire (permission reader/writer) puis envoie le lien Drive par Gmail avec un message.
  Utilise ce skill quand l'utilisateur dit : "envoie le rapport au client par mail", "partage ce Drive et envoie le lien", "donne acces a ce fichier et envoie-le", ou veut un share Drive + email link en un seul flux.
  NE PAS utiliser pour : envoyer le contenu d'un Doc dans le corps du mail (utiliser recipe-draft-email-from-doc), telecharger localement le fichier puis l'attacher (utiliser recipe-bulk-download-folder + gws-gmail), ou creer un Drive Partage entier (utiliser recipe-create-shared-drive).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive", "gws-gmail"]
---

# Email a Google Drive File Link

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-gmail`

Share a Google Drive file and email the link with a message to recipients.

## Steps

1. Find the file: `gws drive files list --params '{"q": "name = '\''Quarterly Report'\''"}'`
2. Share the file: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'`
3. Email the link: `gws gmail +send --to client@example.com --subject 'Quarterly Report' --body 'Hi, please find the report here: https://docs.google.com/document/d/FILE_ID'`


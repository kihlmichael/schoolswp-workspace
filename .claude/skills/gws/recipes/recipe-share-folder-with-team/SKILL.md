---
name: recipe-share-folder-with-team
version: 1.0.0
description: |
  Partage un dossier Google Drive avec une équipe en attribuant des rôles distincts (writer pour les contributeurs, reader pour les stakeholders) puis vérifie la liste des permissions. Onboarding Drive d'un projet.
  Utilise ce skill quand l'utilisateur dit : "partage le dossier projet à l'équipe", "donne accès au dossier Q2 à 5 personnes", "ouvre ce folder Drive en édition pour Y", ou pour poser les permissions initiales d'un dossier projet.
  NE PAS utiliser pour : partager un seul fichier (utiliser recipe-share-doc-and-notify), créer la structure de dossiers (utiliser recipe-organize-drive-folder), ou partager avec des participants d'un événement (utiliser recipe-share-event-materials).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive"]
---

# Share a Google Drive Folder with a Team

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Share a Google Drive folder and all its contents with a list of collaborators.

## Steps

1. Find the folder: `gws drive files list --params '{"q": "name = '\''Project X'\'' and mimeType = '\''application/vnd.google-apps.folder'\''"}'`
2. Share as editor: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "colleague@company.com"}'`
3. Share as viewer: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "stakeholder@company.com"}'`
4. Verify permissions: `gws drive permissions list --params '{"fileId": "FOLDER_ID"}' --format table`


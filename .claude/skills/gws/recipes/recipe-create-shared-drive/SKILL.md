---
name: recipe-create-shared-drive
version: 1.0.0
description: |
  Cree un Drive Partage Google (Shared Drive, ex Team Drive) et ajoute les membres avec les roles appropries (writer, reader, etc).
  Utilise ce skill quand l'utilisateur dit : "cree un Drive Partage pour ce projet", "monte un Shared Drive avec ces personnes", "setup un Team Drive equipe", ou veut un espace Drive partage et non un dossier perso partage.
  NE PAS utiliser pour : partager un fichier individuel par email (utiliser recipe-email-drive-link), telecharger en masse depuis un dossier existant (utiliser recipe-bulk-download-folder), ou creer un simple dossier dans My Drive (utiliser gws-drive files create direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive"]
---

# Create and Configure a Shared Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Shared Drive and add members with appropriate roles.

## Steps

1. Create shared drive: `gws drive drives create --params '{"requestId": "unique-id-123"}' --json '{"name": "Project X"}'`
2. Add a member: `gws drive permissions create --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}' --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}'`
3. List members: `gws drive permissions list --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}'`


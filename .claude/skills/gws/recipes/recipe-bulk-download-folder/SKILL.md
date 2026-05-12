---
name: recipe-bulk-download-folder
version: 1.0.0
description: |
  Liste et telecharge en masse tous les fichiers d'un dossier Google Drive, avec export PDF pour les Google Docs et binaire direct pour les autres.
  Utilise ce skill quand l'utilisateur dit : "telecharge tout le dossier Drive", "backup ce folder Google Drive", "recupere tous les fichiers de ce repertoire", ou veut une copie locale d'une arborescence Drive.
  NE PAS utiliser pour : exporter une seule Sheet en CSV (utiliser recipe-backup-sheet-as-csv), partager un fichier par email (utiliser recipe-email-drive-link), ou creer un Drive Partage (utiliser recipe-create-shared-drive).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive"]
---

# Bulk Download Drive Folder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

List and download all files from a Google Drive folder.

## Steps

1. List files in folder: `gws drive files list --params '{"q": "'\''FOLDER_ID'\'' in parents"}' --format json`
2. Download each file: `gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' -o filename.ext`
3. Export Google Docs as PDF: `gws drive files export --params '{"fileId": "FILE_ID", "mimeType": "application/pdf"}' -o document.pdf`


---
name: recipe-find-large-files
version: 1.0.0
description: |
  Identifie les fichiers Google Drive qui consomment le plus de quota de stockage en listant par taille décroissante. Sortie tableau exploitable pour décider quoi archiver, déplacer ou supprimer.
  Utilise ce skill quand l'utilisateur dit : "trouve les gros fichiers Drive", "qu'est-ce qui prend de la place sur mon Drive", "audit stockage Workspace", ou pour faire le ménage avant un quota plein.
  NE PAS utiliser pour : ranger ou déplacer des fichiers Drive (utiliser recipe-organize-drive-folder), supprimer un fichier précis (utiliser gws-drive directement), ou auditer les permissions de partage (utiliser gws-drive permissions list).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-drive"]
---

# Find Largest Files in Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Identify large Google Drive files consuming storage quota.

## Steps

1. List files sorted by size: `gws drive files list --params '{"orderBy": "quotaBytesUsed desc", "pageSize": 20, "fields": "files(id,name,size,mimeType,owners)"}' --format table`
2. Review the output and identify files to archive or move


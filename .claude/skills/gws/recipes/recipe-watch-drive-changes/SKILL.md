---
name: recipe-watch-drive-changes
version: 1.0.0
description: |
  Crée une subscription Google Workspace Events sur un fichier ou dossier Drive pour recevoir des notifications via Pub/Sub à chaque modification, et gère le renouvellement avant expiration.
  Utilise ce skill quand l'utilisateur dit : "alerte-moi quand ce dossier change", "watch ce fichier Drive", "abonne-toi aux modifs Drive sur X", ou pour mettre en place une surveillance event-driven sur un asset Drive.
  NE PAS utiliser pour : juste lister les changements récents (utiliser gws-drive changes list), notifier après un partage (utiliser recipe-share-doc-and-notify), ou monitorer Gmail ou Calendar (utiliser gws-events sur les autres ressources).
metadata:
  openclaw:
    category: "recipe"
    domain: "engineering"
    requires:
      bins: ["gws"]
      skills: ["gws-events"]
---

# Watch for Drive Changes

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-events`

Subscribe to change notifications on a Google Drive file or folder.

## Steps

1. Create subscription: `gws events subscriptions create --json '{"targetResource": "//drive.googleapis.com/drives/DRIVE_ID", "eventTypes": ["google.workspace.drive.file.v1.updated"], "notificationEndpoint": {"pubsubTopic": "projects/PROJECT/topics/TOPIC"}, "payloadOptions": {"includeResource": true}}'`
2. List active subscriptions: `gws events subscriptions list`
3. Renew before expiry: `gws events +renew --subscription SUBSCRIPTION_ID`


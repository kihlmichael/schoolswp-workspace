---
name: recipe-label-and-archive-emails
version: 1.0.0
description: |
  Applique des libelles Gmail aux messages qui matchent une requête puis les archive. Recipe gws batch pour nettoyer une boite (ex : "from:newsletter@" -> label "Newsletters" + archive).
  Utilise ce skill quand l'utilisateur dit : "labelise et archive les emails de X", "nettoie ma inbox Gmail", "applique le label Y et archive", "tag + archive les messages qui matchent", ou colle une requête Gmail avec une intention de tri massif.
  NE PAS utiliser pour : transferer des emails labelises (utiliser `recipe-forward-labeled-emails`), créer un filtre persistent (utiliser `recipe-create-gmail-filter`), ou trier les emails en mode lecture seule sans archiver (utiliser `gws-gmail-triage`).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail"]
---

# Label and Archive Gmail Threads

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Apply Gmail labels to matching messages and archive them to keep your inbox clean.

## Steps

1. Search for matching emails: `gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com"}' --format table`
2. Apply a label: `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'`
3. Archive (remove from inbox): `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"removeLabelIds": ["INBOX"]}'`


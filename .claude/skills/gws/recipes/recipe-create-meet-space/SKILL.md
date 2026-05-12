---
name: recipe-create-meet-space
version: 1.0.0
description: |
  Cree un espace de reunion Google Meet en accessType OPEN et partage le lien de connexion par Gmail aux participants.
  Utilise ce skill quand l'utilisateur dit : "cree un Meet et envoie le lien", "ouvre une salle Google Meet pour cette reunion", "genere un lien Meet et partage-le", ou veut un Meet expedie immediatement.
  NE PAS utiliser pour : ajouter un Meet a un event Calendar existant (utiliser gws-calendar events patch avec conferenceData), inviter sur un event Calendar deja cree (utiliser recipe-batch-invite-to-event), ou creer un event Calendar standard sans Meet (utiliser gws-calendar insert direct).
metadata:
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins: ["gws"]
      skills: ["gws-meet", "gws-gmail"]
---

# Create a Google Meet Conference

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-meet`, `gws-gmail`

Create a Google Meet meeting space and share the join link.

## Steps

1. Create meeting space: `gws meet spaces create --json '{"config": {"accessType": "OPEN"}}'`
2. Copy the meeting URI from the response
3. Email the link: `gws gmail +send --to team@company.com --subject 'Join the meeting' --body 'Join here: MEETING_URI'`


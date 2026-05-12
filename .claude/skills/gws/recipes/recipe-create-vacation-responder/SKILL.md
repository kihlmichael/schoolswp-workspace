---
name: recipe-create-vacation-responder
version: 1.0.0
description: |
  Active la reponse automatique d'absence Gmail avec un message personnalise, sujet, et options de restriction (contacts, domaine).
  Utilise ce skill quand l'utilisateur dit : "active ma reponse vacances", "mets une auto-reply Gmail jusqu'au X", "configure mon out-of-office", ou veut couper Gmail proprement avant un conge.
  NE PAS utiliser pour : creer un filtre Gmail qui route les mails entrants (utiliser recipe-create-gmail-filter), envoyer un email d'annonce de conge (utiliser gws-gmail send direct), ou desactiver la reponse vacances de maniere recurrente cron (manuel via gws-gmail updateVacation).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail"]
---

# Set Up a Gmail Vacation Responder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Enable a Gmail out-of-office auto-reply with a custom message and date range.

## Steps

1. Enable vacation responder: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": true, "responseSubject": "Out of Office", "responseBodyPlainText": "I am out of the office until Jan 20. For urgent matters, contact backup@company.com.", "restrictToContacts": false, "restrictToDomain": false}'`
2. Verify settings: `gws gmail users settings getVacation --params '{"userId": "me"}'`
3. Disable when back: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": false}'`


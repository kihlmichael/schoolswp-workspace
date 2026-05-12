---
name: recipe-create-gmail-filter
version: 1.0.0
description: |
  Cree un filtre Gmail qui libelle, marque ou categorise automatiquement les messages entrants selon des criteres expediteur/sujet/contenu, avec creation de label si besoin.
  Utilise ce skill quand l'utilisateur dit : "cree un filtre Gmail", "libelle automatiquement les mails de X", "skip inbox pour cet expediteur", ou veut router automatiquement une categorie de mails.
  NE PAS utiliser pour : importer des filtres en masse via XML (utiliser le fichier gmail-filters.xml du projet schoolsWP, voir CLAUDE.md), poser une reponse vacances (utiliser recipe-create-vacation-responder), ou envoyer des emails (utiliser gws-gmail).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail"]
---

# Create a Gmail Filter

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Create a Gmail filter to automatically label, star, or categorize incoming messages.

## Steps

1. List existing labels: `gws gmail users labels list --params '{"userId": "me"}' --format table`
2. Create a new label: `gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Receipts"}'`
3. Create a filter: `gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "receipts@example.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'`
4. Verify filter: `gws gmail users settings filters list --params '{"userId": "me"}' --format table`


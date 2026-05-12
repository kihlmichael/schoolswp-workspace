---
name: recipe-send-team-announcement
version: 1.0.0
description: |
  Envoie une annonce identique sur deux canaux en parallèle : Gmail (mail à la liste de l'équipe) et Google Chat (post dans l'espace Chat dédié). Pour maximiser la visibilité d'un message clé.
  Utilise ce skill quand l'utilisateur dit : "annonce ça à toute l'équipe sur Gmail et Chat", "broadcast le changement de politique partout", "communique la mise à jour cross-canal", ou pour pousser une annonce dual-channel.
  NE PAS utiliser pour : envoyer un email solo (utiliser gws-gmail), poster uniquement dans Chat (utiliser gws-chat), ou notifier après un partage Drive (utiliser recipe-share-doc-and-notify).
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["gws"]
      skills: ["gws-gmail", "gws-chat"]
---

# Announce via Gmail and Google Chat

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-chat`

Send a team announcement via both Gmail and a Google Chat space.

## Steps

1. Send email: `gws gmail +send --to team@company.com --subject 'Important Update' --body 'Please review the attached policy changes.'`
2. Post in Chat: `gws chat +send --space spaces/TEAM_SPACE --text '📢 Important Update: Please check your email for policy changes.'`


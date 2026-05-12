---
name: recipe-review-meet-participants
version: 1.0.0
description: |
  Liste les conférences Google Meet récentes, leurs participants et la durée de chaque session. Pour vérifier la présence effective et le temps passé après une visio.
  Utilise ce skill quand l'utilisateur dit : "qui était présent à la dernière visio", "vérifie l'attendance Meet", "combien de temps Y est resté en réunion", ou pour auditer la participation post-réunion.
  NE PAS utiliser pour : créer ou rejoindre une réunion Meet (utiliser gws-calendar events insert avec conferenceData), récupérer les enregistrements Meet (utiliser gws-meet recordings), ou suivre les RSVPs avant l'événement (utiliser gws-calendar events get).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-meet"]
---

# Review Google Meet Attendance

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-meet`

Review who attended a Google Meet conference and for how long.

## Steps

1. List recent conferences: `gws meet conferenceRecords list --format table`
2. List participants: `gws meet conferenceRecords participants list --params '{"parent": "conferenceRecords/CONFERENCE_ID"}' --format table`
3. Get session details: `gws meet conferenceRecords participants participantSessions list --params '{"parent": "conferenceRecords/CONFERENCE_ID/participants/PARTICIPANT_ID"}' --format table`


---
name: gws-meet
version: 1.0.0
description: |
  Google Meet v2 via la CLI gws : gère conferenceRecords (visios passées), participants, recordings, transcripts, smartNotes, et les spaces Meet. Pour récupérer transcripts ou enregistrements de réunions et les exporter ailleurs.
  Utilise ce skill quand l'utilisateur dit : "récupère le transcript Meet", "list mes réunions Meet", "download recording Meet", "Meet smart notes", ou pour automatiser l'archivage de transcripts vers Drive ou un agent.
  NE PAS utiliser pour : créer une visio (passer par gws-calendar-insert avec conferenceData hangoutsMeet), événements Workspace temps réel (utiliser gws-events-subscribe target meet), ou prep de réunion à venir (utiliser gws-workflow-meeting-prep).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws meet --help"
---

# meet (v2)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws meet <resource> <method> [flags]
```

## API Resources

### conferenceRecords

  - `get` — Gets a conference record by conference ID.
  - `list` — Lists the conference records. By default, ordered by start time and in descending order.
  - `participants` — Operations on the 'participants' resource
  - `recordings` — Operations on the 'recordings' resource
  - `smartNotes` — Operations on the 'smartNotes' resource
  - `transcripts` — Operations on the 'transcripts' resource

### spaces

  - `create` — Creates a space.
  - `endActiveConference` — Ends an active conference (if there's one). For an example, see [End active conference](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#end-active-conference).
  - `get` — Gets details about a meeting space. For an example, see [Get a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#get-meeting-space).
  - `patch` — Updates details about a meeting space. For an example, see [Update a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#update-meeting-space).

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws meet --help

# Inspect a method's required params, types, and defaults
gws schema meet.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.


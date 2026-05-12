---
name: recipe-review-overdue-tasks
version: 1.0.0
description: |
  Liste les Google Tasks non terminées, identifie celles dont la due date est passée, et propose un tri pour rattrapage. Lecture seule : pas de mutation, juste l'audit.
  Utilise ce skill quand l'utilisateur dit : "qu'est-ce que j'ai en retard", "liste mes tâches dépassées", "audit overdue tasks", ou pour faire le point sur les tâches Workspace en retard.
  NE PAS utiliser pour : créer ou modifier une tâche (utiliser gws-tasks directement), planifier de nouveaux blocs sur le calendrier (utiliser recipe-plan-weekly-schedule), ou prioriser des deals commerciaux (utiliser recipe-log-deal-update).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-tasks"]
---

# Review Overdue Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Find Google Tasks that are past due and need attention.

## Steps

1. List task lists: `gws tasks tasklists list --format table`
2. List tasks with status: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}' --format table`
3. Review due dates and prioritize overdue items


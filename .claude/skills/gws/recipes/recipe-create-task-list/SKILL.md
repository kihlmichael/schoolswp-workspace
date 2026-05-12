---
name: recipe-create-task-list
version: 1.0.0
description: |
  Configure une nouvelle liste Google Tasks et y injecte des taches initiales avec titre, notes et dates d'echeance.
  Utilise ce skill quand l'utilisateur dit : "cree une liste Google Tasks", "monte une todo list Tasks pour Q2", "ajoute ces taches dans Google Tasks", ou veut piloter un backlog leger via Tasks Google.
  NE PAS utiliser pour : creer un cours Google Classroom (utiliser recipe-create-classroom-course), gerer le backlog interne projet (utiliser core/tasks/todo.md du projet schoolsWP), ou setup un tracker tabule type Sheets (utiliser recipe-create-expense-tracker comme modele).
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["gws"]
      skills: ["gws-tasks"]
---

# Create a Task List and Add Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Set up a new Google Tasks list with initial tasks.

## Steps

1. Create task list: `gws tasks tasklists insert --json '{"title": "Q2 Goals"}'`
2. Add a task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2024-04-01T00:00:00Z"}'`
3. Add another task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'`
4. List tasks: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table`


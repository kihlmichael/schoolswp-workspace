---
name: concise-planning
description: |
  Transforme une demande en plan unique et actionnable : Approach, Scope (In/Out), 6-10 Action Items atomiques verbe-en-tête, Validation. Une à deux questions max si vraiment bloquant, sinon hypothèses raisonnables. Plan court, pas de prose.
  Utilise ce skill quand l'utilisateur dit : "plan d'action", "planifie cette tâche", "étapes à suivre", "comment implémenter", "donne-moi un plan rapide", ou veut cadrer un changement code avant d'attaquer.
  NE PAS utiliser pour : plan stratégique éditorial schoolsWP (utiliser `radar` agent ou skills SEO), plan multi-étapes long en `core/tasks/plans/` (rédiger directement le markdown), brainstorming créatif (utiliser `superpowers:brainstorming`), ou décomposition en tickets parallélisables (utiliser `planning-and-task-breakdown`).
risk: unknown
source: community
date_added: "2026-02-27"
---

# Concise Planning

## Goal

Turn a user request into a **single, actionable plan** with atomic steps.

## Workflow

### 1. Scan Context

- Read `README.md`, docs, and relevant code files.
- Identify constraints (language, frameworks, tests).

### 2. Minimal Interaction

- Ask **at most 1–2 questions** and only if truly blocking.
- Make reasonable assumptions for non-blocking unknowns.

### 3. Generate Plan

Use the following structure:

- **Approach**: 1-3 sentences on what and why.
- **Scope**: Bullet points for "In" and "Out".
- **Action Items**: A list of 6-10 atomic, ordered tasks (Verb-first).
- **Validation**: At least one item for testing.

## Plan Template

```markdown
# Plan

<High-level approach>

## Scope

- In:
- Out:

## Action Items

[ ] <Step 1: Discovery>
[ ] <Step 2: Implementation>
[ ] <Step 3: Implementation>
[ ] <Step 4: Validation/Testing>
[ ] <Step 5: Rollout/Commit>

## Open Questions

- <Question 1 (max 3)>
```

## Checklist Guidelines

- **Atomic**: Each step should be a single logical unit of work.
- **Verb-first**: "Add...", "Refactor...", "Verify...".
- **Concrete**: Name specific files or modules when possible.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

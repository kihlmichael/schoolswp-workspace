# T10 — Roadmap Finale

## Objectif

Synthétiser toutes les actions en un backlog priorisé pour le trimestre.

## Inputs

- T1 à T9 (tous les outputs)

## Output

- Onglet `T10_ROADMAP`
- Backlog trié par score impact/effort

## Prompt

```
Tâche T10 : Roadmap Finale

Agrège tous les outputs T1-T9 et génère un backlog priorisé :
- Actions techniques (T3)
- Articles à créer (T5+T6)
- Articles à optimiser (T7)
- Liens à ajouter (T8)
- E-E-A-T à compléter (T9)

Score chaque action : impact (1-5) / effort (1-5)
Tri décroissant. Top 20 actions = sprint prioritaire.
```

## Format output

| Action | Type | Impact | Effort | Score | Deadline | Statut |
|--------|------|--------|--------|-------|----------|--------|
| Optimiser /fluentcrm | optimize | 5 | 2 | 2.5 | 2026-04-01 | todo |

## KPIs

- Backlog >= 20 actions
- Top 5 actions exécutables en J30
- 0 action sans deadline

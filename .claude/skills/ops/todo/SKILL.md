---
name: todo
description: |
  Affiche le tableau de bord de mission schoolsWP : lit `core/tasks/todo.md` (mission en cours, plan, étapes) + `core/tasks/lessons.md` (lessons learned), puis propose la prochaine action concrète si une mission est active.
  Utilise ce skill quand l'utilisateur dit : "todo", "mission en cours", "tableau de bord", "prochaine étape", "où j'en suis", ou "résume ma mission".
  NE PAS utiliser pour : créer un plan multi-étapes from scratch (utiliser `planning-and-task-breakdown`), restaurer le contexte d'une session passée (utiliser `context-restore`), ou auditer l'état global du projet (utiliser `workspace-audit`).
---

# /todo — Affiche le tableau de bord de mission

Lis et affiche le contenu de ces deux fichiers :

1. `core/tasks/todo.md` — mission en cours, plan, étapes
2. `core/tasks/lessons.md` — lessons learned

Présente-les clairement en deux sections. Si une mission est en cours, propose la prochaine action concrète à exécuter.

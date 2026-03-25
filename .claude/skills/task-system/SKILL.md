---
name: task-system
description: >
  Système de gestion de tâches complexes pour Claude Code — transforme toute mission
  multi-étapes en workflow guidé à lecture séquentielle stricte via un dossier step/.
  Déclencher dès que la tâche implique plusieurs phases distinctes, un risque d'aller
  trop vite, un besoin de traçabilité, ou une exécution qui mérite d'être cadrée avant
  d'être lancée. Exemples : "construis ce workflow n8n complet", "crée ce système de A à Z",
  "refactor cette architecture", "implémente ce pipeline", "je veux un agent qui fait X".
  Utiliser aussi quand l'utilisateur dit "vas-y" sur une mission complexe sans avoir encore
  cadré le scope. Ce skill impose discovery → scope → architecture → exécution, dans cet
  ordre, sans exception. Ne pas utiliser pour des tâches mono-étape ou des corrections
  ciblées simples.
---

# schoolswp-task-system

Workflow guidé à lecture séquentielle stricte. Une étape à la fois. Pas d'exécution avant cadrage.

---

## Initialisation obligatoire

Avant toute chose, crée la structure suivante :

```
step/
├── 00_plan.md          ← source de vérité, mis à jour à chaque transition
├── 01_discovery.md     ← besoin, inconnues, risques
├── 02_scope.md         ← périmètre exact, inclus/exclus
├── 03_architecture.md  ← structure, ordre, dépendances
├── 04_execution.md     ← exécution de ce qui a été validé
├── 05_validation.md    ← vérification du workflow complet
└── 06_summary.md       ← résumé, décisions, fichiers produits
```

Crée d'abord `step/00_plan.md`. Ne remplis aucun autre fichier avant.

---

## Template step/00_plan.md

```markdown
# Plan d'exécution séquentiel

## Objectif global

[objectif du workflow]

## Ordre obligatoire

1. step/01_discovery.md
2. step/02_scope.md
3. step/03_architecture.md
4. step/04_execution.md
5. step/05_validation.md
6. step/06_summary.md

## Statut

- [ ] 01_discovery.md — todo
- [ ] 02_scope.md — todo
- [ ] 03_architecture.md — todo
- [ ] 04_execution.md — todo
- [ ] 05_validation.md — todo
- [ ] 06_summary.md — todo

## Règles

- une seule étape active (doing) à la fois
- mettre à jour ce fichier après chaque étape
- ne pas exécuter avant 02 + 03 terminés
- ne jamais sauter 01_discovery
```

---

## Contenu attendu par étape

### 01_discovery.md — Jamais sauté

- Reformuler le besoin avec tes propres mots
- Lister les inconnues et ce qu'il faut clarifier avant d'agir
- Identifier les risques et hypothèses
- Ne pas encore proposer de solution

### 02_scope.md

- Périmètre exact : ce qui est inclus, ce qui est exclu
- Niveau de profondeur attendu
- Contraintes techniques ou métier

### 03_architecture.md

- Structure logique de la solution
- Ordre d'exécution et dépendances
- Décisions structurantes (avec justification courte)

### 04_execution.md

- Exécuter uniquement ce qui a été validé dans 01+02+03
- Tracer chaque action importante
- Pas d'improvisation sur le scope ou la structure

### 05_validation.md

- Vérifier que chaque étape a bien été traitée dans l'ordre
- Vérifier la cohérence de bout en bout
- Confirmer que le résultat correspond au scope défini en 02

### 06_summary.md

- Résumé de ce qui a été fait
- Décisions importantes prises
- Fichiers produits et leur rôle
- Points d'attention restants pour la suite

---

## Règle de transition

Après chaque étape :

1. Mettre l'étape en cours à `done` dans `step/00_plan.md`
2. Mettre la suivante à `doing`
3. Toutes les autres restent à `todo`

L'étape active est **toujours la seule en `doing`**.

---

## Interdit

- Exécuter quoi que ce soit avant `02_scope` et `03_architecture` terminés
- Sauter `01_discovery` même si la réponse semble évidente
- Charger plusieurs fichiers step en parallèle
- Produire un résultat sans avoir traversé toutes les étapes dans l'ordre

---

## Démarrage

1. Crée `step/`
2. Crée `step/00_plan.md` avec l'objectif et tous les statuts à `todo`
3. Affiche la structure créée
4. Passe `01_discovery.md` à `doing` et traite-le

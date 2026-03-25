# Sequential Step Workflow — Pattern d'exécution guidée

Pattern pour transformer un prompt monolithique en workflow guidé à lecture séquentielle stricte.

---

## Principe

Un dossier `step/` à la racine. Un fichier par étape. Lecture et traitement un par un.
Le plan `step/00_plan.md` est la source de vérité du workflow — pas un résumé, pas une liste.

---

## Structure obligatoire

```
step/
├── 00_plan.md          ← source de vérité, mis à jour à chaque transition
├── 01_discovery.md     ← reformulation, inconnues, risques
├── 02_scope.md         ← périmètre exact, inclus/exclus
├── 03_architecture.md  ← structure logique, dépendances
├── 04_execution.md     ← exécution contrôlée
├── 05_validation.md    ← vérification du workflow complet
└── 06_summary.md       ← résumé, décisions, fichiers produits
```

---

## Template step/00_plan.md

```markdown
# Plan d'exécution séquentiel

## Objectif global

[objectif du workflow]

## Principe de fonctionnement

Lecture séquentielle stricte des fichiers du dossier `step`.
Chaque étape doit être lue, traitée, puis marquée `done` avant de passer à la suivante.
Aucune étape ne doit être sautée.
Aucun chargement massif de contexte au départ.

## Ordre obligatoire

1. step/01_discovery.md
2. step/02_scope.md
3. step/03_architecture.md
4. step/04_execution.md
5. step/05_validation.md
6. step/06_summary.md

## Statut des étapes

- [ ] step/01_discovery.md — todo
- [ ] step/02_scope.md — todo
- [ ] step/03_architecture.md — todo
- [ ] step/04_execution.md — todo
- [ ] step/05_validation.md — todo
- [ ] step/06_summary.md — todo

## Règles

- lire une seule étape active à la fois
- mettre à jour ce plan après chaque étape
- ne pas exécuter avant discovery + scope + architecture
- garder un flux propre, traçable et vérifiable
```

---

## Contenu attendu par étape

### 01_discovery.md

- reformuler le besoin
- identifier les inconnues
- lister les hypothèses
- détecter les risques
- définir ce qu'il faut comprendre avant d'agir
- ne pas encore exécuter la solution

### 02_scope.md

- périmètre exact
- ce qui est inclus
- ce qui est exclu
- niveau de profondeur verrouillé

### 03_architecture.md

- structure logique du workflow
- ordre d'exécution
- dépendances entre composants

### 04_execution.md

- exécuter uniquement ce qui a été validé
- noter chaque action
- pas d'improvisation majeure

### 05_validation.md

- vérifier le respect du workflow séquentiel
- vérifier la cohérence de bout en bout
- vérifier qu'aucune étape n'a été sautée

### 06_summary.md

- résumé de ce qui a été fait
- décisions importantes
- fichiers produits
- points d'attention restants

---

## Règles absolues

- Jamais tout faire dans un seul fichier
- Jamais lire toutes les étapes d'un coup
- Jamais sauter discovery
- Jamais exécuter avant scope + architecture validés
- Mettre à jour 00_plan.md à chaque transition (todo → doing → done)

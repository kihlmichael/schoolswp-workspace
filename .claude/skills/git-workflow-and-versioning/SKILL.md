---
name: git-workflow-and-versioning
description: |
  Discipline git pour commits atomiques (une chose logique par commit), historique propre, changements reversibles. Trunk-based development, branches courtes 1-3 jours, feature flags plutot que long-lived branches, resolution de conflits, worktrees pour travail parallele. Pattern : implement slice, test, verify, commit, next slice.
  Utilise ce skill quand l'utilisateur dit : "git workflow", "stratégie de branches", "commit discipline", "worktrees", "historique git", "avant de committer", "résolution de conflits git", ou "comment décomposer mes commits".
  NE PAS utiliser pour : conventions de message de commit specifiques projet (voir CLAUDE.md schoolsWP : feat: / fix: / chore: / docs: en anglais), workflow de PR et release schoolsWP (utiliser ship gstack ou pattern existant), ou setup initial git (voir docs runbooks-operationnels.md).
---

# Git Workflow and Versioning

Git est ton filet de securite. Les commits sont des save points, les branches des sandboxes, l'historique de la documentation.

## Principes fondamentaux

### Trunk-Based Development

Garder `main` toujours deployable. Travailler en branches courtes (1-3 jours max).

```
main --o--o--o--o--o--o--o--  (toujours deployable)
        \      /  \    /
         o--o-/    o--/    <- branches courtes (1-3 jours)
```

- Les branches longues sont un cout cache (divergence, conflits).
- Feature flags > branches longues pour du travail incomplet.

### 1. Commit Early, Commit Often

Chaque increment reussi = son propre commit. Pas d'accumulation.

```
Pattern : Implement slice -> Test -> Verify -> Commit -> Next slice
Pas ca : Implementer tout -> Esperer -> Gros commit
```

### 2. Commits atomiques

Chaque commit fait UNE chose logique :

```bash
# Bon : chaque commit est autonome
a1b2c3d feat: add task creation endpoint with validation
d4e5f6g feat: add task creation form component
h7i8j9k feat: connect form to API and add loading state

# Mauvais : tout melange
x1y2z3a feat: add task feature, fix sidebar, update deps
```

### 3. Messages descriptifs

Le message explique le POURQUOI, pas juste le QUOI :

```
# Bon
feat: add email validation to registration endpoint

Prevents invalid formats from reaching the database.
Uses Zod schema validation at route handler level.

# Mauvais
update auth.ts
```

**Format (convention schoolsWP) :**
```
<type>: <description courte>

<corps optionnel expliquant pourquoi>
```

Types : `feat`, `fix`, `refactor`, `test`, `docs`, `chore`

### 4. Separer les concerns

Ne PAS combiner formatting + comportement. Ne PAS combiner refactor + feature.

```bash
# Bon : concerns separes
git commit -m "refactor: extract validation logic to shared utility"
git commit -m "feat: add phone number validation"

# Mauvais : concerns melanges
git commit -m "refactor validation and add phone field"
```

### 5. Sizing des changements

```
~100 lignes  -> Facile a review, facile a revert
~300 lignes  -> Acceptable pour un changement logique unique
~1000 lignes -> Decouper
```

## Strategie de branches (convention schoolsWP)

```
main (toujours deployable)
  |
  +-- feature/task-creation
  +-- fix/pipeline-timeout
  +-- chore/update-deps
```

Nommage : `feature/*`, `fix/*`, `chore/*`, `refactor/*`

## Worktrees pour travail parallele

Pour les agents Claude Code paralleles :

```bash
git worktree add ../project-feature-a feature/task-creation
git worktree add ../project-feature-b feature/user-settings

# Chaque worktree = repertoire separe avec sa propre branche
# Les agents travaillent en parallele sans interference

# Cleanup
git worktree remove ../project-feature-a
```

## Le Save Point Pattern

```
Agent demarre
    |
    +-- Changement
    |   +-- Test passe ? -> Commit -> Continuer
    |   +-- Test echoue ? -> Revert au dernier commit -> Investiguer
    |
    +-- Autre changement
    |   +-- Test passe ? -> Commit -> Continuer
    |   +-- Test echoue ? -> Revert -> Investiguer
    |
    +-- Feature complete -> Historique propre
```

## Resume de changements

Apres toute modification, fournir un resume structure :

```
CHANGEMENTS :
- core/agents-py/mon_agent/agent.py : Ajout validation input
- tests/test_mon_agent.py : Tests pour la validation

PAS TOUCHE (intentionnellement) :
- core/agents-py/autre_agent/ : Meme gap mais hors scope
- base.py : Amelioration possible (tache separee)

POINTS D'ATTENTION :
- Le schema Zod est strict -- rejette les champs extras
```

## Hygiene pre-commit

Avant chaque commit (automatise par hooks schoolsWP) :

```bash
# 1. Verifier le diff
git diff --staged

# 2. Pas de secrets
git diff --staged | grep -i "password\|secret\|api_key\|token"

# 3. Tests
.venv/Scripts/python -m pytest tests/ -v

# 4. Lint
.venv/Scripts/python -m ruff check core/agents-py/
```

Hooks pre-commit schoolsWP : secrets-scan -> ruff lint+format -> pip-audit.

## Git pour le debugging

```bash
# Trouver quel commit a introduit un bug
git bisect start
git bisect bad HEAD
git bisect good <commit-connu-bon>

# Voir les changements recents
git log --oneline -20
git diff HEAD~5..HEAD -- core/agents-py/

# Qui a modifie une ligne specifique
git blame core/agents-py/base.py

# Chercher dans les messages de commit
git log --grep="validation" --oneline
```

## Anti-rationalisations

| Excuse | Realite |
|--------|---------|
| "Je commiterai quand la feature sera finie" | Un gros commit est impossible a review, debug ou revert. |
| "Le message n'a pas d'importance" | Les messages sont de la documentation. Le futur toi en aura besoin. |
| "Je squasherai tout plus tard" | Le squash detruit la narrative de developpement. |
| "Les branches ajoutent du overhead" | Les branches courtes sont gratuites. Les longues sont le probleme. |
| "Je n'ai pas besoin de .gitignore" | Jusqu'a ce que `.env` avec les secrets de prod soit commite. |

## Red Flags

- Gros changements non commites qui s'accumulent
- Messages de commit "fix", "update", "misc"
- Changements de formatting melanges avec du comportement
- Pas de `.gitignore`
- `node_modules/`, `.env` ou artifacts de build commites
- Branches longues divergeant significativement de main
- Force-push sur branches partagees

## Verification

Pour chaque commit :

- [ ] Le commit fait une chose logique
- [ ] Le message explique le pourquoi, suit les conventions de type
- [ ] Tests passent avant de commiter
- [ ] Pas de secrets dans le diff
- [ ] Pas de changements formatting-only melanges avec du comportement
- [ ] `.gitignore` couvre les exclusions standard

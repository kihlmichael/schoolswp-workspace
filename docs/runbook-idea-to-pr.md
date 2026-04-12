# Runbook : De l'idee a la PR mergee

Workflow complet pour transformer une idee (feature, fix, refactor) en PR mergee sur schoolsWP.

Ce runbook couvre le workflow **code** (agents Python, config, tooling). Pour le workflow **editorial** (article, audit, publication WordPress), voir `../../docs/runbook-idee-a-publication.md`.

---

## Vue d'ensemble

4 phases sequentielles — chaque phase produit un livrable qui alimente la suivante.

```
Idee → [1. Contexte] → [2. Plan] → [3. Execution] → [4. Livraison] → PR mergee
```

---

## Phase 1 : Gather Context (5 min)

### Objectif

Rassembler toutes les informations necessaires AVANT de coder.

### Actions

- Lire le `CLAUDE.md` du projet + les rules scoped pertinentes
- Lire `core/tasks/lessons.md` (les 10 lessons documentees)
- Identifier les fichiers impactes (`Grep` / `Glob`)
- Si feature liee a un agent : lire `.claude/rules/python-agents.md`
- Si feature liee a n8n : lire `.claude/rules/n8n-integration.md`
- Si contenu : lire `.claude/rules/branding.md`

### Outils

| Outil | Usage |
|---|---|
| `Grep` / `Glob` | Trouver les fichiers impactes |
| `Read` | Lire le code existant |
| `git log` | Comprendre l'historique recent |
| MCP (n8n, GitHub) | Contexte externe si necessaire |

### Livrable

Brief mental ou note dans le plan : "je modifie X fichiers pour Y raison, les dependances sont Z"

---

## Phase 2 : Analyze & Plan (10 min)

### Objectif

Planifier l'implementation AVANT d'ecrire du code.

### Actions

- Creer un plan avec `/plan` ou mode plan Claude Code
- Lister les modifications fichier par fichier
- Identifier les tests a ecrire/modifier
- Anticiper les breaking changes
- Si complexe : decouper en sous-taches

### Regles

- Pas de code sans plan valide pour les changements > 3 fichiers
- Le plan doit mentionner les tests
- Verifier `safe_read_path` / `safe_write_path` si chemins fichiers impliques (lesson #1)
- Verifier `.gitignore` si nouveaux fichiers sensibles (lesson #2)

### Livrable

Plan valide (affiche ou dans `core/tasks/`)

---

## Phase 3 : Execute (variable)

### Objectif

Implementer le plan, etape par etape.

### Workflow type

1. **Creer la branche**
   ```bash
   git checkout -b feature/nom-feature main
   ```

2. **Coder** — Edit/Write les fichiers identifies dans le plan
   - Hook `ruff-check.sh` auto-execute apres chaque Edit/Write sur `.py`
   - Conventions : PEP 8, kebab-case, line-length 120
   - Venv Windows : toujours utiliser `.venv/Scripts/python` (lesson #5)

3. **Tester**
   ```bash
   .venv/Scripts/python -m pytest tests/ -v
   .venv/Scripts/python -m ruff check core/agents-py/
   ```

4. **Verifier** — relire les changements
   ```bash
   git diff
   ```

### Regles

- Un commit par etape logique (pas un mega-commit)
- Messages conventionnels en anglais : `feat:`, `fix:`, `chore:`, `docs:`
- Ne jamais committer `.env`, `.mcp.json`, ou fichiers avec secrets
- Si un test echoue : diagnostiquer avant de patcher
- Si signature d'agent modifiee : grep tous les appelants (lesson #10)
- Jamais `rm` ou `rm -rf` — utiliser `trash`

### Livrable

Code fonctionnel + tests passants sur la branche feature

---

## Phase 4 : Deliver (5 min)

### Objectif

Packager le travail en PR prete a merger.

### Actions

1. **Stage & commit final**
   ```bash
   git add <fichiers specifiques>
   git commit -m "feat: description concise"
   ```

2. **Push**
   ```bash
   git push -u origin feature/nom-feature
   ```

3. **Creer la PR**
   ```bash
   gh pr create --title "feat: titre court" --body "$(cat <<'EOF'
   ## Summary
   - ...

   ## Test plan
   - [ ] ...
   EOF
   )"
   ```

4. **Self-review**
   - Relire le diff complet
   - Verifier que la CI passe (ruff check + ruff format + pytest)
   - S'assurer qu'aucun secret n'est expose

### CI checks (`.github/workflows/ci.yml`)

| Check | Commande |
|---|---|
| Lint | `ruff check core/agents-py/` |
| Format | `ruff format --check core/agents-py/` |
| Tests | `pytest tests/ -v --cov --cov-report=term-missing` |

Coverage minimum : `fail_under = 40`. Les CLI (`*/cli.py`, `*/brain_lite_cli.py`, `*/__main__.py`) sont exclus.

### Livrable

PR ouverte, CI verte, prete a review/merge

---

## Checklist rapide

- [ ] Context : CLAUDE.md + rules + lessons lues
- [ ] Plan : valide, tests mentionnes
- [ ] Branche : creee depuis `main`
- [ ] Code : conventions respectees, ruff clean
- [ ] Tests : ecrits et passants
- [ ] Secrets : aucun dans le diff
- [ ] Commit : messages conventionnels en anglais
- [ ] PR : titre court, body structure, CI verte

---

## Anti-patterns

| Ne fais pas | Fais plutot |
|---|---|
| Coder sans lire le code existant | Phase 1 d'abord |
| Mega-commit de 500 lignes | Commits atomiques |
| `git add .` ou `git add -A` | `git add <fichiers>` |
| Patcher un test qui echoue | Diagnostiquer la cause racine |
| `--no-verify` pour bypasser les hooks | Fixer le probleme detecte |
| Amender le commit precedent apres erreur | Nouveau commit propre |
| `rm -rf` pour nettoyer | `trash <chemin>` |
| Modifier une signature agent sans verifier les appelants | `Grep` tous les imports d'abord |

---

## Voir aussi

- `../../docs/runbook-idee-a-publication.md` — workflow editorial (idee → article → publication WordPress)
- `../../docs/standards-code.md` — standards de qualite code
- `../../docs/runbooks-operationnels.md` — 12 runbooks operationnels
- `core/tasks/lessons.md` — lessons apprises (10 documentees)
- `.claude/rules/python-agents.md` — architecture agents Python
- `CONTRIBUTING.md` — guidelines de contribution

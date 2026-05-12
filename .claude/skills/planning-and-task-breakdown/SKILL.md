---
name: planning-and-task-breakdown
description: |
  Decomposer le travail en taches atomiques, ordonnees, verifiables, avec criteres d'acceptation explicites. Mode read-only obligatoire pendant la planification (pas de code), mapping des dependances, identification des risques. Sortie : plan, pas du code. Adapte au contexte schoolsWP (agents Python, CLI, system prompts md).
  Utilise ce skill quand l'utilisateur dit : "plan d'action", "decompose cette tache", "par ou commencer", "estime le scope", "planifie cette feature", "task breakdown", "ordre d'implementation", ou pour paralleliser du travail entre agents, sessions, worktrees.
  NE PAS utiliser pour : changement single-file au scope evident, spec deja decoupee en taches definies, implementation directe (utiliser incremental-implementation), brainstorm produit en amont (utiliser superpowers:brainstorming ou office-hours), ou plan d'architecture qui necessite review (utiliser plan-eng-review apres ce skill).
---

# Planning and Task Breakdown

Decomposer le travail en taches petites, verifiables, avec des criteres d'acceptation explicites.

## Quand utiliser

- Tu as un spec/brief et tu dois le decouper en unites implementables
- Une tache semble trop large ou vague pour demarrer
- Le travail doit etre parallelise (agents, sessions, worktrees)
- L'ordre d'implementation n'est pas evident
- Tu dois communiquer le scope a un humain

**Ne PAS utiliser :** changement single-file avec scope evident, ou quand le spec contient deja des taches bien definies.

## Processus de planification

### Etape 1 : Mode lecture seule

Avant d'ecrire du code, operer en mode read-only :

- Lire le spec et les sections pertinentes du codebase
- Identifier les patterns et conventions existants
- Mapper les dependances entre composants
- Noter les risques et inconnues

**NE PAS ecrire de code pendant la planification.** La sortie est un plan, pas du code.

### Etape 2 : Graphe de dependances

Mapper ce qui depend de quoi. Pour schoolsWP, typiquement :

```
Schema / Modele de donnees
    |
    +-- Agent Python (base.py heritage)
    |       |
    |       +-- CLI (cli.py)
    |       |       |
    |       |       +-- Integration pipeline
    |       |
    |       +-- System prompt (.md)
    |
    +-- Tests (test_*.py)
    |
    +-- n8n workflow (si applicable)
```

Implementation bottom-up : fondations d'abord.

### Etape 3 : Decoupage vertical

Construire un chemin complet a la fois, pas couche par couche :

**Mauvais (horizontal) :**
```
Tache 1 : Ecrire tous les agents
Tache 2 : Ecrire tous les CLI
Tache 3 : Ecrire tous les tests
Tache 4 : Tout connecter
```

**Bon (vertical) :**
```
Tache 1 : Agent strategy (agent.py + cli.py + test + prompt)
Tache 2 : Agent writer (agent.py + cli.py + test + prompt)
Tache 3 : Pipeline orchestration (factory + integration test)
Tache 4 : n8n workflow (si applicable)
```

Chaque tranche verticale livre une fonctionnalite testable.

### Etape 4 : Rediger les taches

Chaque tache suit cette structure :

```markdown
## Tache [N] : [Titre court descriptif]

**Description :** Un paragraphe expliquant ce que cette tache accomplit.

**Criteres d'acceptation :**
- [ ] [Condition specifique et testable]
- [ ] [Condition specifique et testable]

**Verification :**
- [ ] Tests passent : `.venv/Scripts/python -m pytest tests/test_xxx.py -v`
- [ ] Lint passe : `.venv/Scripts/python -m ruff check core/agents-py/`
- [ ] Verification manuelle : [description]

**Dependances :** [Numeros de taches prerequises, ou "Aucune"]

**Fichiers concernes :**
- `core/agents-py/mon_agent/agent.py`
- `tests/test_mon_agent.py`

**Scope estime :** [XS: 1 fichier | S: 1-2 | M: 3-5 | L: 5-8 | XL: trop gros, decouper]
```

### Etape 5 : Ordonner et checkpointer

1. Dependances satisfaites (fondations d'abord)
2. Chaque tache laisse le systeme fonctionnel
3. Checkpoints apres chaque 2-3 taches
4. Taches a haut risque en premier (fail fast)

```markdown
## Checkpoint : Apres taches 1-3
- [ ] Tous les tests passent
- [ ] ruff check clean
- [ ] Le pipeline fonctionne de bout en bout
- [ ] Review avant de continuer
```

## Sizing des taches

| Taille | Fichiers | Scope | Exemple schoolsWP |
|--------|----------|-------|-------------------|
| **XS** | 1 | Config ou fonction unique | Ajouter un flag CLI |
| **S** | 1-2 | Un composant ou endpoint | Nouvel agent simple |
| **M** | 3-5 | Une tranche feature | Agent + CLI + test + prompt |
| **L** | 5-8 | Feature multi-composants | Pipeline complet nouveau pilier |
| **XL** | 8+ | **Trop gros -- decouper** | -- |

**Quand decouper davantage :**
- Plus de 3 criteres d'acceptation
- Touche 2+ sous-systemes independants (ex: agents ET n8n)
- Le titre contient "et" (signe de 2 taches)

## Template de plan

```markdown
# Plan : [Nom feature/projet]

## Vue d'ensemble
[Un paragraphe resume]

## Decisions d'architecture
- [Decision 1 + justification]
- [Decision 2 + justification]

## Liste des taches

### Phase 1 : Fondations
- [ ] Tache 1 : ...
- [ ] Tache 2 : ...

### Checkpoint : Fondations
- [ ] Tests passent, lint clean

### Phase 2 : Features principales
- [ ] Tache 3 : ...
- [ ] Tache 4 : ...

### Checkpoint : Features
- [ ] Flow end-to-end fonctionnel

### Phase 3 : Polish
- [ ] Tache 5 : ...

### Checkpoint : Complet
- [ ] Tous les criteres remplis
- [ ] Pret pour review

## Risques et mitigations
| Risque | Impact | Mitigation |
|--------|--------|------------|
| [Risque] | [Haut/Moyen/Bas] | [Strategie] |

## Questions ouvertes
- [Question necessitant un input humain]
```

## Parallelisation

- **Safe a paralleliser :** tranches feature independantes, tests sur code existant, documentation
- **Sequentiel obligatoire :** migrations DB, changements d'etat partage, chaines de dependance
- **Coordination requise :** features partageant un contrat (definir le contrat d'abord)

## Anti-rationalisations

| Excuse | Realite |
|--------|---------|
| "Je verrai en avancant" | C'est comme ca qu'on finit avec du spaghetti et du rework. 10 min de plan sauvent des heures. |
| "Les taches sont evidentes" | Ecris-les quand meme. Les taches explicites revelent les dependances cachees. |
| "Planifier c'est du overhead" | Planifier EST la tache. Implementer sans plan, c'est juste taper. |
| "Je peux tout garder en tete" | Les context windows sont finis. Les plans ecrits survivent aux sessions. |

## Red Flags

- Demarrer l'implementation sans liste de taches ecrite
- Taches qui disent "implementer la feature" sans criteres d'acceptation
- Pas d'etapes de verification dans le plan
- Toutes les taches sont XL
- Pas de checkpoints entre les taches
- Ordre des dependances non considere

## Verification

Avant de commencer l'implementation :

- [ ] Chaque tache a des criteres d'acceptation
- [ ] Chaque tache a une etape de verification
- [ ] Les dependances sont identifiees et ordonnees
- [ ] Aucune tache ne touche plus de ~5 fichiers
- [ ] Des checkpoints existent entre les phases majeures
- [ ] L'humain a review et approuve le plan

---
name: incremental-implementation
description: >
  Livrer les changements en tranches verticales fines. Utilise ce skill pour toute implementation
  touchant plus d'un fichier, quand une tache semble trop grosse pour atterrir en une fois,
  ou quand tu es tente d'ecrire plus de 100 lignes avant de tester. Declenche pour
  "implementer incrementalement", "vertical slice", "livrer par tranches", "feature flag",
  "scope trop gros", "une chose a la fois".
---

# Incremental Implementation

Construire en tranches verticales fines -- implementer un morceau, tester, verifier, puis etendre. Chaque increment laisse le systeme dans un etat fonctionnel et testable.

## Quand utiliser

- Tout changement multi-fichiers
- Construction d'une feature a partir d'un task breakdown
- Refactoring de code existant
- Chaque fois que tu es tente d'ecrire >100 lignes avant de tester

**Ne PAS utiliser :** changements single-file/single-function ou le scope est deja minimal.

## Le cycle d'increment

```
+--------------------------------------+
|                                      |
|   Implement --> Test --> Verify --+   |
|       ^                          |   |
|       +------ Commit <-----------+   |
|               |                      |
|               v                      |
|           Next slice                 |
|                                      |
+--------------------------------------+
```

Pour chaque tranche :
1. **Implementer** le plus petit morceau complet de fonctionnalite
2. **Tester** -- executer la suite de tests (ou ecrire un test si aucun n'existe)
3. **Verifier** -- confirmer que la tranche fonctionne (tests passent, build OK)
4. **Commiter** -- sauvegarder avec un message descriptif
5. **Passer a la tranche suivante**

## Strategies de decoupage

### Tranches verticales (prefere)

Construire un chemin complet a travers le stack :

```
Tranche 1 : Agent strategy (agent.py + cli.py + test + prompt)
    -> Tests passent, l'agent fonctionne en CLI

Tranche 2 : Agent writer (agent.py + cli.py + test + prompt)
    -> Tests passent, l'agent ecrit du contenu

Tranche 3 : Pipeline orchestration (factory + integration)
    -> Tests passent, le pipeline complet fonctionne

Tranche 4 : n8n integration (workflow JSON + test)
    -> Workflow fonctionnel et teste
```

### Contract-First

Quand backend et frontend doivent avancer en parallele :

```
Tranche 0 : Definir le contrat (types, interfaces)
Tranche 1a : Backend contre le contrat + tests API
Tranche 1b : Frontend contre des mock data
Tranche 2 : Integration et test end-to-end
```

### Risk-First

Attaquer le plus risque/incertain en premier :

```
Tranche 1 : Prouver que l'API externe fonctionne (plus haut risque)
Tranche 2 : Construire l'agent dessus
Tranche 3 : Ajouter gestion d'erreurs et fallbacks
```

Si Tranche 1 echoue, on le decouvre avant d'investir dans 2 et 3.

## Regles d'implementation

### Regle 0 : Simplicite d'abord

Avant d'ecrire du code : "Quelle est la chose la plus simple qui pourrait marcher ?"

```
SIMPLICITY CHECK :
X  EventBus generique avec middleware pour une notification
OK Simple appel de fonction

X  Abstract factory pour deux composants similaires
OK Deux composants directs avec utils partagees

X  Config-driven form builder pour trois formulaires
OK Trois composants de formulaire
```

Trois lignes similaires > abstraction prematuree.

### Regle 0.5 : Discipline de scope

Toucher UNIQUEMENT ce que la tache requiert.

NE PAS :
- "Nettoyer" du code adjacent
- Refactorer les imports de fichiers non modifies
- Supprimer des commentaires non compris
- Ajouter des features non dans le spec
- Moderniser la syntaxe de fichiers juste lus

```
REMARQUE MAIS PAS TOUCHE :
- core/agents-py/old_agent/agent.py : import inutilise (hors scope)
- base.py : messages d'erreur ameliorables (tache separee)
-> Creer des taches pour ces points ?
```

### Regle 1 : Une chose a la fois

Chaque increment change UNE chose logique. Pas de concerns melanges.

### Regle 2 : Toujours compilable

Apres chaque increment, le projet doit build et les tests existants doivent passer.

### Regle 3 : Feature flags pour features incompletes

```python
# Feature flag pour travail en cours
ENABLE_NEW_PIPELINE = os.getenv("FEATURE_NEW_PIPELINE", "false") == "true"

if ENABLE_NEW_PIPELINE:
    # Nouveau pipeline
    pass
```

### Regle 4 : Defaults securises

```python
# Safe : desactive par defaut, opt-in
async def run(self, *, include_ner: bool = False, include_serp: bool = False):
    ...
```

### Regle 5 : Rollback-friendly

Chaque increment independamment revertable :
- Changements additifs (nouveaux fichiers, nouvelles fonctions) = faciles a revert
- Modifications de code existant = minimales et ciblees
- Ne pas supprimer et remplacer dans le meme commit -- separer

## Checklist d'increment

Apres chaque increment :

- [ ] Le changement fait une chose et la fait completement
- [ ] Tests existants passent : `.venv/Scripts/python -m pytest tests/ -v`
- [ ] Lint passe : `.venv/Scripts/python -m ruff check core/agents-py/`
- [ ] La nouvelle fonctionnalite fonctionne comme attendu
- [ ] Le changement est commite avec un message descriptif

## Anti-rationalisations

| Excuse | Realite |
|--------|---------|
| "Je testerai tout a la fin" | Les bugs composent. Un bug en tranche 1 rend les tranches 2-5 fausses. |
| "C'est plus rapide de tout faire d'un coup" | Ca SEMBLE plus rapide jusqu'a ce que quelque chose casse et tu ne trouves pas laquelle des 500 lignes l'a cause. |
| "Ces changements sont trop petits pour des commits separes" | Les petits commits sont gratuits. Les gros cachent des bugs. |
| "Ce refactor est assez petit pour etre inclus" | Refactors melanges avec features = plus dur a review et debug. Separer. |

## Red Flags

- Plus de 100 lignes ecrites sans lancer de tests
- Changements non lies dans un seul increment
- "Laisse-moi juste ajouter ca aussi" -- expansion de scope
- Sauter l'etape test/verify pour aller plus vite
- Build ou tests casses entre les increments
- Gros changements non commites qui s'accumulent
- Construire des abstractions avant le 3eme use case
- Toucher des fichiers hors scope "tant qu'on y est"

## Verification

Apres avoir complete tous les increments d'une tache :

- [ ] Chaque increment a ete individuellement teste et commite
- [ ] La suite de tests complete passe
- [ ] Le build est propre
- [ ] La feature fonctionne end-to-end comme specifie
- [ ] Pas de changements non commites restants

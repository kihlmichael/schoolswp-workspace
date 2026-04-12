---
name: code-review-and-quality
description: >
  Review de code multi-axes avant merge. Utilise ce skill avant de fusionner tout changement,
  apres une implementation de feature, quand un autre agent a produit du code, ou pour evaluer
  la qualite du code sur 5 dimensions. Declenche pour "review ce code", "code review",
  "avant de merger", "qualite du code", "revue de code", "review PR".
---

# Code Review and Quality

Review multi-dimensionnelle avec quality gates. Tout changement est review avant merge.

## Standard d'approbation

Approuver un changement quand il ameliore clairement la sante globale du code, meme s'il n'est pas parfait. Le code parfait n'existe pas -- l'objectif est l'amelioration continue.

## Les 5 axes de review

### 1. Correctness

Le code fait-il ce qu'il pretend faire ?

- Correspond au spec/tache ?
- Edge cases geres (null, vide, limites) ?
- Chemins d'erreur geres (pas juste le happy path) ?
- Tests passent ET testent les bonnes choses ?
- Off-by-one, race conditions, inconsistances d'etat ?

### 2. Lisibilite et simplicite

Un autre ingenieur (ou agent) peut-il comprendre sans explication ?

- Noms descriptifs et coherents avec les conventions projet ?
- Flow de controle direct (pas de ternaires imbriquees, callbacks profonds) ?
- Code organise logiquement (code lie groupe, frontieres de modules claires) ?
- Peut etre fait en moins de lignes ? (1000 lignes ou 100 suffisent = echec)
- Les abstractions meritent-elles leur complexite ?
- Dead code : variables no-op, shims de compatibilite, commentaires `// removed` ?

### 3. Architecture

Le changement s'integre-t-il au design du systeme ?

- Suit les patterns existants ou en introduit un nouveau (justifie ?) ?
- Frontieres de modules maintenues ?
- Duplication qui devrait etre partagee ?
- Dependances dans la bonne direction (pas de circulaires) ?
- Niveau d'abstraction approprie ?

### 4. Securite

Le changement introduit-il des vulnerabilites ?

- Input utilisateur valide et assaini ?
- Secrets hors du code, logs et version control ?
- Auth/authz verifie la ou necessaire ?
- Queries SQL parametrees ?
- Sorties encodees (XSS) ?
- Donnees externes traitees comme non fiables ?

**Pour schoolsWP :** verifier `safe_read_path()` / `safe_write_path()` sur tout CLI manipulant des fichiers.

### 5. Performance

- Patterns N+1 ?
- Boucles non bornees ou fetch de donnees sans contrainte ?
- Operations synchrones qui devraient etre async ?
- Pagination manquante sur les endpoints liste ?

## Sizing des changements

```
~100 lignes  -> Bon. Reviewable en une session.
~300 lignes  -> Acceptable si changement logique unique.
~1000 lignes -> Trop gros. Decouper.
```

**Strategies de decoupage :**

| Strategie | Comment | Quand |
|-----------|---------|-------|
| **Stack** | Petit changement, puis le suivant base dessus | Dependances sequentielles |
| **Par groupe de fichiers** | Changements separes par groupe | Concerns transversaux |
| **Horizontal** | Code partage/stubs d'abord, consommateurs ensuite | Architecture en couches |
| **Vertical** | Tranches full-stack plus petites | Feature work |

**Separer refactoring et feature.** Toujours. Un changement qui refactorise ET ajoute du comportement = deux changements.

## Descriptions de changement

**Premiere ligne :** courte, imperative, autonome. "Ajouter validation email au endpoint registration" pas "Ajout de la validation."

**Corps :** Ce qui change et pourquoi. Contexte, decisions, raisonnement non visible dans le code.

**Anti-patterns :** "Fix bug", "Update", "Misc", "Phase 1".

## Processus de review

### Etape 1 : Comprendre le contexte
Avant de regarder le code : quel est l'objectif du changement ?

### Etape 2 : Reviewer les tests d'abord
Les tests revelent l'intention et la couverture.

### Etape 3 : Reviewer l'implementation
Parcourir le code avec les 5 axes en tete.

### Etape 4 : Categoriser les findings

| Prefixe | Signification | Action auteur |
|---------|---------------|---------------|
| *(aucun)* | Changement requis | Doit etre corrige avant merge |
| **Critical:** | Bloque le merge | Vulnerabilite, perte de donnees, fonctionnalite cassee |
| **Nit:** | Mineur, optionnel | L'auteur peut ignorer |
| **Optional:** | Suggestion | A considerer mais pas requis |
| **FYI** | Informatif | Pas d'action -- contexte pour reference |

### Etape 5 : Verifier la verification
- Tests executes ?
- Build reussi ?
- Test manuel fait ?
- Avant/apres pour changements UI ?

## Multi-Model Review

```
Model A ecrit le code
    |
    v
Model B review (correctness + architecture)
    |
    v
Model A adresse le feedback
    |
    v
Humain prend la decision finale
```

## Dead Code Hygiene

Apres refactoring, verifier le code orphelin :
1. Identifier le code devenu inaccessible
2. Le lister explicitement
3. **Demander avant de supprimer**

## Discipline des dependances

Avant d'ajouter une dependance :
1. Le stack existant resout-il le probleme ?
2. Taille de la dependance ?
3. Activement maintenue ?
4. Vulnerabilites connues ? (`pip-audit` / `npm audit`)
5. Licence compatible ?

## Checklist de review

```markdown
## Review : [Titre PR/changement]

### Contexte
- [ ] Je comprends ce que ce changement fait et pourquoi

### Correctness
- [ ] Correspond aux requirements
- [ ] Edge cases geres
- [ ] Chemins d'erreur geres
- [ ] Tests couvrent le changement

### Lisibilite
- [ ] Noms clairs et coherents
- [ ] Logique directe
- [ ] Pas de complexite inutile

### Architecture
- [ ] Suit les patterns existants
- [ ] Pas de couplage ou dependances inutiles
- [ ] Niveau d'abstraction approprie

### Securite
- [ ] Pas de secrets dans le code
- [ ] Input valide aux frontieres
- [ ] Pas de vulnerabilites injection
- [ ] safe_read_path/safe_write_path utilises (si CLI)

### Performance
- [ ] Pas de patterns N+1
- [ ] Pas d'operations non bornees

### Verification
- [ ] Tests passent
- [ ] Build reussi
- [ ] Verification manuelle faite

### Verdict
- [ ] **Approve** -- Pret a merger
- [ ] **Request changes** -- Issues a corriger
```

## Anti-rationalisations

| Excuse | Realite |
|--------|---------|
| "Ca marche, c'est suffisant" | Du code illisible, non securise ou mal architecture cree de la dette qui compose. |
| "Je l'ai ecrit, donc je sais que c'est correct" | Les auteurs sont aveugles a leurs propres hypotheses. |
| "On nettoiera plus tard" | Plus tard n'arrive jamais. La review est le quality gate. |
| "Le code genere par IA est probablement bon" | Le code IA necessite PLUS de scrutin. Il est confiant et plausible, meme quand il est faux. |
| "Les tests passent, donc c'est bon" | Les tests sont necessaires mais pas suffisants. |

## Red Flags

- PR mergees sans review
- Review qui verifie uniquement si les tests passent
- "LGTM" sans preuve de review reelle
- Changements security-sensitive sans review security
- Gros PR "trop gros pour review" (les decouper)
- Bug fixes sans test de regression
- Accepter "je corrigerai plus tard"

## Verification

Apres la review :

- [ ] Toutes les issues Critical resolues
- [ ] Toutes les issues Important resolues ou deferrees avec justification
- [ ] Tests passent
- [ ] Build reussi
- [ ] L'histoire de verification est documentee

---
name: documentation-and-adrs
description: >
  Documenter les decisions, pas juste le code. ADR (Architecture Decision Records), documentation
  inline, API docs. Utilise ce skill pour toute decision architecturale significative, changement
  d'API publique, ou quand le contexte doit survivre aux sessions. Declenche pour "ADR",
  "documenter cette decision", "pourquoi ce choix", "architecture decision record",
  "documenter le why", "decisions d'architecture".
---

# Documentation and ADRs

Documenter les decisions, pas juste le code. La documentation la plus precieuse capture le POURQUOI -- le contexte, les contraintes et les trade-offs qui ont mene a une decision.

## Quand utiliser

- Decision architecturale significative
- Choix entre approches concurrentes
- Ajout ou changement d'API publique
- Feature qui change le comportement utilisateur
- Quand tu te retrouves a expliquer la meme chose plusieurs fois

**Ne PAS utiliser :** code evident, commentaires qui restent ce que le code dit deja, prototypes jetables.

## Architecture Decision Records (ADRs)

Les ADRs capturent le raisonnement derriere les decisions techniques significatives.

### Quand ecrire un ADR

- Choix de framework, lib ou dependance majeure
- Design de modele de donnees ou schema
- Strategie d'authentification
- Architecture API (REST vs GraphQL vs tRPC)
- Choix d'outil de build, hebergement, infra
- Toute decision couteuse a reverser

### Template ADR

Stocker dans `docs/decisions/` avec numerotation sequentielle :

```markdown
# ADR-001: [Titre de la decision]

## Status
Accepted | Superseded by ADR-XXX | Deprecated

## Date
YYYY-MM-DD

## Contexte
[Description du probleme et des contraintes]

## Decision
[Ce qui a ete decide et avec quoi]

## Alternatives considerees

### [Alternative A]
- Pour : ...
- Contre : ...
- Rejetee : [raison]

### [Alternative B]
- Pour : ...
- Contre : ...
- Rejetee : [raison]

## Consequences
- [Impact 1]
- [Impact 2]
- [Risques acceptes]
```

### Exemples schoolsWP

```markdown
# ADR-001: Utiliser Anthropic comme provider LLM principal

## Status
Accepted

## Date
2025-12-01

## Contexte
schoolsWP a besoin d'un provider LLM pour la generation de contenu SEO.
Criteres : qualite redactionnelle FR, API async, cout raisonnable, support tools.

## Decision
Anthropic Claude (claude-sonnet-4-6) via le SDK Python anthropic.
Multi-provider abstraction via providers/ package pour fallback.

## Alternatives considerees
- OpenAI GPT-4o : qualite FR inferieure pour notre use case
- Gemini : API moins mature au moment du choix
- Ollama local : performance insuffisante pour production

## Consequences
- Dependance a ANTHROPIC_API_KEY
- Cout variable selon volume
- Abstraction multi-provider deployee pour migration future
```

### Cycle de vie ADR

```
PROPOSED -> ACCEPTED -> (SUPERSEDED ou DEPRECATED)
```

- **Ne jamais supprimer** les anciens ADRs. Ils capturent le contexte historique.
- Quand une decision change, ecrire un nouvel ADR qui reference et supersede l'ancien.

## Documentation inline

### Quand commenter

Commenter le POURQUOI, pas le QUOI :

```python
# MAUVAIS : redit le code
# Incrementer le compteur de 1
counter += 1

# BON : explique l'intention non evidente
# Rate limit utilise une fenetre glissante -- reset au bord de fenetre,
# pas sur schedule fixe, pour prevenir les burst attacks
if now - window_start > WINDOW_SIZE:
    counter = 0
    window_start = now
```

### Quand NE PAS commenter

```python
# Ne pas commenter le code auto-explicatif
def calculate_total(items: list[CartItem]) -> float:
    return sum(item.price * item.quantity for item in items)

# Ne pas laisser de TODO pour des choses a faire maintenant
# TODO: add error handling  <- Juste l'ajouter

# Ne pas laisser de code commente
# old_implementation = ...  <- Supprimer, git a l'historique
```

### Documenter les gotchas connus

```python
"""
IMPORTANT: Cette fonction doit etre appelee avant le premier appel LLM.
Si appelee apres l'init du client, le model override ne prend pas effet
car le client est deja configure.

Voir ADR-003 pour la justification complete.
"""
def configure_model(model: str) -> None:
    ...
```

## Documentation pour les agents

Consideration speciale pour le contexte des agents IA :

- **CLAUDE.md / rules files** -- Conventions projet pour que les agents les suivent
- **Spec files** -- Garder a jour pour que les agents construisent la bonne chose
- **ADRs** -- Aider les agents a comprendre les decisions passees (evite de re-decider)
- **Gotchas inline** -- Empecher les agents de tomber dans les pieges connus

## Anti-rationalisations

| Excuse | Realite |
|--------|---------|
| "Le code est auto-documentant" | Le code montre QUOI. Il ne montre pas POURQUOI, quelles alternatives ont ete rejetees, ou quelles contraintes s'appliquent. |
| "On documentera quand l'API se stabilise" | Les APIs se stabilisent plus vite quand on les documente. Le doc est le premier test du design. |
| "Personne ne lit les docs" | Les agents si. Les futurs ingenieurs si. Ton toi dans 3 mois si. |
| "Les ADRs sont du overhead" | Un ADR de 10 min previent un debat de 2h sur la meme decision 6 mois plus tard. |
| "Les commentaires deviennent obsoletes" | Les commentaires sur le POURQUOI sont stables. Ceux sur le QUOI deviennent obsoletes -- c'est pourquoi on ecrit seulement les premiers. |

## Red Flags

- Decisions architecturales sans justification ecrite
- APIs publiques sans documentation ou types
- README qui n'explique pas comment lancer le projet
- Code commente au lieu de supprime
- Commentaires TODO la depuis des semaines
- Pas d'ADRs dans un projet avec des choix architecturaux significatifs

## Verification

Apres documentation :

- [ ] ADRs existent pour toutes les decisions architecturales significatives
- [ ] README couvre quick start, commandes et vue d'ensemble architecture
- [ ] Fonctions API ont une documentation parametres/retour
- [ ] Gotchas connus documentes inline la ou ca compte
- [ ] Pas de code commente restant
- [ ] Rules files (CLAUDE.md etc.) sont a jour et precis

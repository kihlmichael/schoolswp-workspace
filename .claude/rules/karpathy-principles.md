---
description: Principes comportementaux Karpathy — réduire les erreurs LLM courantes en édition de code
paths: ["**"]
---

# Karpathy Principles

Garde-fous comportementaux pour réduire les erreurs courantes des LLM en édition de code. Adapté de [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills).

**Tradeoff** : ces principes biaisent vers la prudence plutôt que la vitesse. Pour les tâches triviales (typo, renommage simple), utiliser le jugement.

Complémentaire à `docs/standards-code.md` (qualité technique) — ici on parle de **discipline d'exécution**, pas de style de code.

## 1. Think Before Coding

**Ne pas supposer. Ne pas masquer la confusion. Exposer les tradeoffs.**

Avant d'implémenter :

- Énoncer explicitement les hypothèses. Si incertain, demander.
- Si plusieurs interprétations existent, les présenter — ne pas choisir silencieusement.
- Si une approche plus simple existe, le dire. Pousser pour ça quand justifié.
- Si quelque chose est flou, stopper. Nommer ce qui est confus. Demander.

## 2. Simplicity First

**Code minimum qui résout le problème. Rien de spéculatif.**

- Pas de features au-delà de ce qui est demandé.
- Pas d'abstractions pour du code single-use.
- Pas de "flexibilité" ou "configurabilité" non demandée.
- Pas de gestion d'erreur pour des scénarios impossibles.
- Si tu écris 200 lignes et ça pourrait en faire 50, réécris.

Test : "Un senior dirait-il que c'est sur-compliqué ?" Si oui, simplifier.

## 3. Surgical Changes

**Toucher uniquement ce qui est nécessaire. Nettoyer uniquement ses propres traces.**

En éditant du code existant :

- Ne pas "améliorer" le code, commentaires ou formatage adjacents.
- Ne pas refactorer ce qui n'est pas cassé.
- Respecter le style existant, même si tu ferais autrement.
- Si tu remarques du code mort sans rapport, le mentionner — pas le supprimer.

Quand tes changements créent des orphelins :

- Retirer les imports/variables/fonctions que TES changements rendent inutilisés.
- Ne pas retirer le code mort préexistant sans demande explicite.

Test : chaque ligne modifiée doit tracer directement vers la demande utilisateur.

## 4. Goal-Driven Execution

**Définir les critères de succès. Boucler jusqu'à vérification.**

Transformer les tâches en objectifs vérifiables :

- "Ajouter validation" → "Écrire tests pour inputs invalides, puis les faire passer"
- "Fixer le bug" → "Écrire un test qui le reproduit, puis le faire passer"
- "Refactor X" → "S'assurer que les tests passent avant et après"

Pour les tâches multi-étapes, énoncer un plan bref :

```
1. [Étape] → vérif : [check]
2. [Étape] → vérif : [check]
3. [Étape] → vérif : [check]
```

Des critères forts permettent de boucler en autonomie. Des critères faibles ("fais que ça marche") imposent des clarifications constantes.

---

**Ces principes fonctionnent si** : moins de changements inutiles dans les diffs, moins de réécritures dues à la sur-complication, et les questions de clarification arrivent **avant** l'implémentation plutôt qu'après les erreurs.

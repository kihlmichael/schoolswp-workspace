# Codex Plugin pour Claude Code — Guide d'usage

## Les 3 commandes principales

**`/codex:review`** — Review de code classique
Codex analyse ton code (fichier, diff, ou changements récents) et remonte bugs, problèmes de sécurité, améliorations. À lancer avant un commit important ou sur un fichier sensible.

**`/codex:adversarial-review`** — Review qui challenge
Même principe, mais Codex joue l'avocat du diable : il questionne tes choix de design, propose des alternatives, cherche les angles morts. Utile pour les décisions architecturales.

**`/codex:rescue`** — Déléguer en background
Tu confies une tâche complexe à Codex (investigation d'un bug vicieux, refacto, implémentation). Il bosse en arrière-plan pendant que tu continues avec Claude.

## Gérer les jobs en background

- `/codex:status` — voir les jobs en cours
- `/codex:result` — récupérer le résultat d'un job terminé
- `/codex:cancel` — annuler un job

## Workflow type

1. Tu codes avec Claude
2. Avant de commit → `/codex:review` pour un second avis
3. Si Codex trouve un truc gros → tu demandes à Claude de fixer
4. Pour un bug qui résiste → `/codex:rescue` et Codex creuse en parallèle

## Quand utiliser quoi

| Situation | Commande |
|---|---|
| Vérifier un fichier avant commit | `/codex:review` |
| Valider un choix d'architecture | `/codex:adversarial-review` |
| Débloquer une investigation longue | `/codex:rescue` |
| Double-check feature sensible (auth, paiement) | `/codex:adversarial-review` |

## À savoir

- Codex utilise ta clé API OpenAI (conso = ton compte)
- Le runtime démarre au premier appel (léger délai la 1ère fois)
- Les jobs `rescue` tournent sans bloquer ta session
- Option `--enable-review-gate` (désactivée) forcerait une review avant chaque fin de tâche

## Installation (pour mémoire)

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

Prérequis : Node.js ≥ 18.18 + compte ChatGPT ou clé API OpenAI.

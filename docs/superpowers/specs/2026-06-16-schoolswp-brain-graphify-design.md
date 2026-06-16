# Second cerveau schoolsWP - graphify comme moteur de cartographie

Spec de design - 2026-06-16
Statut : validé (brainstorming), prêt pour plan d'implémentation.

## 1. Contexte & objectif

Construire un "second cerveau" durable et interrogeable pour le repo schoolsWP OS (Python content factory : `core/`, `systems/`, `content/`, `schoolswp-agents/`, `docs/`, `tools/`). Il doit permettre de retrouver et relier les décisions, workflows, contenus et agents schoolsWP, tout en restant maîtrisé en coût, en egress et en automatisation.

graphify (CLI knowledge-graph, package `graphifyy`, déjà installé en 0.8.40) sert de moteur. Le repo possède déjà une mémoire dispersée (obsidian-bridge, `content/decisions/`, `docs/` SOP, `schoolswp-agents/*/memory`, auto-mémoire `~/.claude`).

## 2. Principe directeur

> **graphify n'est pas le cerveau. graphify est le moteur de cartographie du cerveau.**
> La mémoire reste dans les fichiers Markdown existants. graphify sert à relier, explorer, retrouver, expliquer. Le wrapper schoolsWP décide ce qui est indexé, envoyé, validé et journalisé. graphify peut lire et cartographier ; schoolsWP décide.

## 3. Décisions actées

- **Mission** : machinerie (code + agents + config) ET contenu éditorial, dans un seul graphe interrogeable.
- **Backend sémantique** : Gemini (cloud) accepté pour ce cas d'usage. Egress assumé pour le contenu ; le code reste offline.
- **Périmètre** : curé (signal/bruit d'abord), élargissable plus tard si le premier graphe est propre.
- **Fraîcheur** : hybride prudent. Code = maj offline gratuite autorisée ; contenu = jamais ré-indexé sans GO manuel. Aucun hook git, aucun cron au départ.
- **Réconciliation** : index-in-place. `schoolswp-brain/` n'est PAS un nouveau vault : c'est la couche graphe/index/synthèse. La connaissance reste où elle est ; graphify l'indexe via une allowlist, sans migration ni copie.

## 4. Architecture (index-in-place)

`schoolswp-brain/` ne recopie rien. Il contient seulement le nouveau :

```
schoolswp-brain/
├── .graphify/             # sortie brute graphify (graph.json/html, cache, GRAPH_REPORT.md) - GITIGNORED
├── 07_graph/
│   ├── logs/              # journal de chaque refresh (commité, auditable)
│   └── exports/           # vues curées / publiées (callflow, tree, synthèses)
├── tools/graphify-brain/  # le wrapper garde-fou
│   ├── allowlist.yml
│   ├── brain.py
│   ├── md_local_index.py
│   └── tests/
├── 00_inbox/              # capture rapide (si non couvert par obsidian-bridge)
└── 03_synthesis/          # synthèses transversales (net-neuf, zéro doublon)
```

graphify indexe en place, via l'allowlist : `core/`, `tools/` (curé), `docs/`, `content/articles|audits|decisions`, `schoolswp-agents/` (memory + shared + soul), et `obsidian-bridge/` en lecture seule. L'allowlist est le seul endroit qui définit "ce qui est dans le cerveau".

## 5. Le wrapper `tools/graphify-brain/`

### allowlist.yml

Source de vérité unique. Chaque racine déclare son backend, donc son niveau d'egress :

```yaml
roots:
  - { path: core/, type: code, backend: offline }
  - { path: tools/, type: code, backend: offline }
  - { path: docs/, type: content, backend: gemini }
  - { path: content/articles/, type: content, backend: gemini }
  - { path: content/audits/, type: content, backend: gemini }
  - { path: content/decisions/, type: content, backend: gemini }
  - { path: schoolswp-agents/, type: content, backend: gemini }
  - { path: obsidian-bridge/, type: content, backend: gemini } # lecture seule (pont local, pas le vault complet)
exclude: # compilé vers .graphifyignore
  - "**/.env*"
  - "**/*.key"
  - "**/*.pem"
  - ".credentials/**"
  - "**/_drafts/**"
  - "**/_workspace/**"
  - "tmp_*/**"
  - ".tmp-*/**"
  - "node_modules/**"
  - "**/.venv/**"
  - "obsidian-bridge/logs/**"
```

Règle : rien hors allowlist n'entre ; rien marqué `offline` ne sort jamais. Le `backend` d'une racine ne gouverne QUE son markdown : le code (`.py`, `.ps1`, ...) de n'importe quelle racine est TOUJOURS extrait en AST local, jamais envoyé.

### Configuration (env)

```env
SCHOOLSWP_REPO_PATH="D:\VS Code\CLAUDE CODE\projects\schoolswp"
OBSIDIAN_BRIDGE_PATH="D:\VS Code\CLAUDE CODE\projects\schoolswp\obsidian-bridge"
GRAPHIFY_OUTPUT_PATH="D:\VS Code\CLAUDE CODE\projects\schoolswp\schoolswp-brain\.graphify"
```

`obsidian-bridge/` est lu en LECTURE SEULE : graphify ne déplace, ne renomme, ne duplique rien. Toutes les sorties vont dans `GRAPHIFY_OUTPUT_PATH` (gitignored ; graphify y crée un sous-dossier `graphify-out/`). On nomme la source `OBSIDIAN_BRIDGE_PATH` (et non `OBSIDIAN_VAULT_PATH`) car ce dossier est le pont local, pas le vault Obsidian complet.

### Composants

- **brain.py** : le CLI garde-fou (refresh / dry-run / gate / log / query).
- **md_local_index.py** : scan markdown 100% local (titres, `[[liens]]`, `#tags`, frontmatter, fichiers modifiés). Aucun LLM, aucun egress. C'est la "couche contenu structurelle".
- **07_graph/.brain-state.json** : dernier commit indexé (pour le `--changed`).
- **07_graph/logs/** : journal append-only.

## 6. Le flux de refresh

Le cerveau a 3 couches, du plus sûr au plus riche :

| Couche                       | Producteur                  | Egress            | Validation     |
| ---------------------------- | --------------------------- | ----------------- | -------------- |
| Code graph                   | graphify AST (tree-sitter)  | aucun (local)     | auto-OK        |
| Carte contenu (structurelle) | `md_local_index.py`         | aucun (local)     | auto-OK        |
| Graphe contenu (sémantique)  | graphify `--backend gemini` | contenu -> Google | GO obligatoire |

Note importante : la couche structurelle markdown n'est PAS l'extraction sémantique de graphify (qui, elle, exige Gemini). graphify ne touche au markdown qu'au moment du GO Gemini.

### Commandes (les 4 étapes formalisées)

- `brain refresh --local` -> couches 1+2 (code AST + md structurel). Gratuit, zéro egress, aucune confirmation. (étape 2)
- `brain refresh --changed --dry-run` -> n'envoie rien. Affiche : fichiers nouveaux / modifiés, ce qui reste local vs ce qui partirait à Gemini, estimation tokens + coût. (étape 1)
- `brain refresh --gemini` -> rejoue le dry-run, attend le GO explicite (`--yes` ou confirmation tapée), exécute le scan secrets pré-envoi, puis indexe le contenu via Gemini. (étape 3)
- Chaque commande append au log : date, commande, fichiers analysés, fichiers envoyés, modèle, coût estimé, coût réel si dispo, résultat. (étape 4)

## 7. Interroger le cerveau

- CLI (MVP) : `brain query "..."`, `brain explain "X"`, `brain path "A" "B"` -> pass-through vers graphify sur le graphe du cerveau.
- Commande `/brain` Claude : phase 2 (le `.claude/` est protégé pour les outils agent ; ajout manuel par l'utilisateur). Jamais de hook PreToolUse.
- Aucun agent ne consulte le graphe automatiquement : outil interrogé à la demande, pas d'injection auto.

## 8. Sécurité & frontière d'egress

- Opt-in strict : rien n'entre hors allowlist.
- `exclude` compilé vers `.graphifyignore` (secrets, credentials, brouillons, tmp, vendored, fichiers clients).
- Frontière d'egress : le code ne sort jamais (AST offline) ; seul le contenu des racines `gemini` peut sortir, après dry-run + GO. Le dry-run affiche la liste exacte des fichiers qui partiraient.
- Scan secrets pré-envoi (défense en profondeur) : avant tout envoi Gemini, `brain.py` scanne le lot sortant (patterns clés/tokens/emails clients) et avorte si détection.
- Sortie du graphe : `schoolswp-brain/.graphify/` (= `GRAPHIFY_OUTPUT_PATH`) gitignored par défaut (dérive du contenu, reste local). `allowlist.yml` + `07_graph/logs/` sont commités (auditable).

## 9. Périmètre MVP vs plus tard

**MVP (prudent)** : allowlist + compilation `.graphifyignore` · `md_local_index.py` · `brain refresh --local` · `brain refresh --changed --dry-run` (coût + egress + scan secrets) · `brain refresh --gemini` (GO gaté) · log + state · `brain query/explain/path` · premier graphe curé validé signal/bruit.

**Repoussé (après validation MVP + plafond budget)** : hook git · cron/nightly · commande `/brain` · capture du coût réel Gemini · merge multi-repo/submodules · sync Obsidian approfondie · publication auto de la viz.

## 10. Critères de succès (testables)

1. Zéro envoi sans GO : aucune donnée ne part sans `--yes` explicite (test : aucun appel API sans confirmation).
2. Rien hors allowlist, aucun secret n'atteint l'index ou l'egress (tests : compilation allowlist + scan pré-envoi).
3. `--changed` détecte correctement nouveaux/modifiés depuis le dernier commit indexé.
4. Chaque refresh produit une ligne de log complète.
5. `brain refresh --local` tourne 100% offline (test : clés coupées, succès, token cost 0).
6. Le premier graphe curé est assez propre pour être utile (acceptation manuelle : god nodes + communautés contenu cohérents, bruit tolérable).

## 11. Dépendances & risques

- graphify épinglé à 0.8.40 ; backend Gemini via `graphifyy[openai]` + `GEMINI_API_KEY`. Risque de breaking changes graphify entre versions -> pin + test de fumée.
- L'estimation de coût est heuristique (chars/4) ; la capture du coût réel est phase 2.
- graphify n'a aucun dry-run/cost/gate natif -> toute la sécurité vit dans le wrapper.
- Submodules / sous-repos (telegram-claude, ultimate-scraper, fluent-mcp-servers, heygen-skills...) hors graphe unique au départ (merge phase 2).
- Environnement Windows/PowerShell ; `brain.py` en Python cross-platform (venv projet, ruff, pytest, ligne 120).

## 12. Questions ouvertes (à trancher au plan ou plus tard)

- [RÉSOLU 2026-06-16] Source Obsidian = `obsidian-bridge/` (pont local, lecture seule) via `OBSIDIAN_BRIDGE_PATH` ; pas le vault complet. Sortie = `schoolswp-brain/.graphify/` (`GRAPHIFY_OUTPUT_PATH`).
- [RÉSOLU 2026-06-16] Le graphe n'est PAS commité (gitignored sous `.graphify/`).
- Modèle Gemini précis pour graphify (défaut auto vs pin d'un modèle).
- Position finale du wrapper : `schoolswp-brain/tools/graphify-brain/` (auto-contenu, retenu) vs `tools/` racine (convention repo).

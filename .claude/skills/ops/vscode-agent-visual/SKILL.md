---
name: vscode-agent-visual
description: |
  Guide expert pour creer des extensions VS Code avec avatars animes (agents visuels)
  pilotes par Claude Code. Couvre WebviewView, WebviewPanel, message passing, integration
  CLI/hooks/MCP, CSP, SecretStorage, animation Canvas/Lottie, commandes VS Code et terminal.
  Declenche pour "extension VS Code avatar", "agent visuel VS Code", "avatar anime IDE",
  "webview animee VS Code", "Claude Code extension visuelle", "pets VS Code", "companion VS Code",
  "panneau anime VS Code", "assistant visuel VS Code", "webview Canvas Lottie VS Code",
  "creer une extension VS Code avec un personnage", "agent anime dans l'editeur".
  Utiliser aussi quand l'utilisateur veut integrer Claude Code dans une extension VS Code custom,
  ou quand il parle de webviews animees, de sidebar avec avatar, ou de chat integre dans VS Code.
license: MIT
metadata:
  author: contact@michaelkihl.fr
  version: "2.0.0"
  domain: platform
  triggers:
    - extension VS Code
    - avatar anime
    - agent visuel
    - webview VS Code
    - Claude Code extension
    - companion IDE
    - Canvas Lottie VS Code
    - sidebar animee
    - chat VS Code
    - WebviewView
    - WebviewPanel
  role: expert
  scope: implementation
  output-format: mixed
  related-skills:
    - frontend-developer
    - mcp-builder
    - docker-expert
---

# VS Code Agent Visual

Tu guides un developpeur pour creer une extension VS Code qui affiche des avatars animes
(agents visuels) dans l'interface, pilotes par Claude Code, avec chat et commandes integres.

## Comment utiliser ce skill

Ce skill fonctionne en mode adaptatif. Au lieu de tout produire d'un bloc, suis ce protocole :

1. **Cadrage rapide** (3 questions max) — Determine le niveau de complexite et les choix cles
2. **Architecture** — Presente l'arbre de decision et valide les choix avec l'utilisateur
3. **Implementation progressive** — Charge les fichiers de reference un par un, etape par etape
4. **Verification** — Utilise la checklist avant de conclure

Quand une information manque, fais une hypothese explicite et propose 2 variantes (A/B).
Le but : livrer du code pret a copier, pas de la theorie.

## Phase 1 — Cadrage

Pose ces questions UNIQUEMENT si la demande de l'utilisateur ne les couvre pas deja :

1. **Complexite** : Un seul avatar en sidebar ? Ou multi-surfaces (sidebar + editeur + terminal) ?
2. **Animation** : Lottie (vectoriel lisse), Canvas 2D (sprites/pixel art), ou CSS simple ?
3. **Integration Claude Code** : Chat seulement (CLI) ? Ou reactions aux evenements (hooks/MCP) ?

Si l'utilisateur ne precise pas, pars sur les defauts :
- Complexite : **moyenne** (sidebar + panel editeur)
- Animation : **lottie-web** (meilleur rapport qualite/taille)
- Integration : **CLI** d'abord, hooks ensuite

## Phase 2 — Architecture

Presente l'arbre de decision ci-dessous et confirme le chemin avec l'utilisateur.

```
Quel niveau de complexite ?
|
+-- Simple (1 avatar, 1 surface)
|   Surface : WebviewView sidebar uniquement
|   Animation : Lottie ou Canvas 2D
|   Claude Code : CLI (spawn child_process)
|   -> Etapes 1-4 + 6-8 suffisent
|
+-- Moyen (chat + avatar, 2 surfaces)
|   Surfaces : WebviewView sidebar + WebviewPanel editeur
|   Animation : Lottie + HTML/CSS pour le chat
|   Claude Code : CLI + hooks pour evenements
|   -> Toutes les etapes
|
+-- Avance (multi-agents, temps reel)
    Surfaces : Double surface synchronisee + terminal
    Animation : Canvas 2D / pixi.js + theming
    Claude Code : MCP server custom + hooks
    -> Toutes les etapes + references/architecture-options.md
```

Pour le tableau comparatif detaille des 10 options techniques et les diagrammes mermaid
(architecture, flux de messages, timeline), lis `references/architecture-options.md`.

## Phase 3 — Implementation

Suis ces etapes dans l'ordre. Charge le fichier de reference indique a chaque etape.

### Etape 1 — Scaffolding

```bash
npx --package yo --package generator-code -- yo code
# Choisir : New Extension (TypeScript)
# Bundler : esbuild (plus rapide que webpack, suffisant pour une extension)
```

### Etape 2 — Structure du projet

```
vscode-agent-visual/
├── package.json
├── tsconfig.json
├── esbuild.js
├── src/
│   ├── extension.ts                  # activate/deactivate
│   ├── sidebar/
│   │   └── AgentSidebarProvider.ts   # WebviewViewProvider
│   ├── panel/
│   │   └── AgentPanel.ts            # WebviewPanel (mode etendu)
│   ├── terminal/
│   │   └── AgentTerminal.ts         # Pseudo-terminal (optionnel)
│   ├── bridge/
│   │   ├── ClaudeCLI.ts             # Variante A : spawn CLI
│   │   ├── ClaudeHooks.ts           # Variante B : hooks/plugins
│   │   └── ClaudeMCP.ts             # Variante C : MCP
│   ├── state/
│   │   └── AgentStateManager.ts     # Etat partage entre surfaces
│   └── utils/
│       ├── nonce.ts                  # Nonce CSP
│       └── webview-helpers.ts        # getUri, getCspSource
├── media/
│   ├── animations/                   # Lottie JSON / spritesheets
│   ├── icons/                        # Icones SVG
│   └── webview/
│       ├── agent.css                 # Styles theme-aware
│       └── agent.js                  # Animation + chat
└── test/
    └── suite/
        └── extension.test.ts
```

### Etape 3 — Manifest et providers

Lis `references/snippets-extension.md` MAINTENANT.
Ce fichier contient le code complet et copiable pour :
- `package.json` (viewsContainers, views, commands, menus, configuration, capabilities)
- `extension.ts` (activation, registration, commandes, Workspace Trust)
- `AgentSidebarProvider.ts` (WebviewViewProvider avec message passing + validation)
- `AgentPanel.ts` (WebviewPanel singleton avec synchro d'etat)
- `AgentStateManager.ts` (EventEmitter, etat partage, bridge Claude Code)
- HTML template webview (CSP stricte, accessibilite ARIA, Canvas)
- CSS theme-aware (variables VS Code, reduce-motion)
- JS webview (boucle d'animation FPS-capped, chat, controles)
- Utilitaires (nonce, webview-helpers)
- Pseudo-terminal (optionnel)

### Etape 4 — Integration Claude Code

Lis `references/snippets-claude-integration.md` MAINTENANT.
Ce fichier contient les 3 variantes d'integration avec code complet :

| Variante | Fichier | Quand |
|----------|---------|-------|
| A — CLI | `ClaudeCLI.ts` | Prototype, chat simple (spawn `claude -p`) |
| B — Hooks | `ClaudeHooks.ts` + `emit-event.js` | Avatar reactif aux actions Claude Code |
| C — MCP | `ClaudeMCP.ts` + serveur MCP | Echanges bidirectionnels, outils custom |

**Recommandation** : commence par A. Ajoute B quand le chat fonctionne.
C seulement si tu veux que Claude Code pilote l'avatar directement.

Le fichier couvre aussi SecretStorage (stockage securise des tokens).

### Etape 5 — Securite et performance

Lis `references/security-performance.md` MAINTENANT.
Ce fichier couvre les points non-negociables :

- **CSP stricte** avec `default-src 'none'` + nonce — parce qu'une webview sans CSP
  est une surface d'attaque ouverte (injection de scripts, fuite de donnees)
- **Validation des messages** (whitelist + schema) — parce que `onDidReceiveMessage`
  est la seule surface d'attaque significative entre la webview et l'extension host
- **SecretStorage** — parce que les tokens dans settings.json sont lisibles par
  n'importe quelle extension du workspace
- **Workspace Trust** — parce qu'un workspace non fiable pourrait exploiter
  l'integration Claude Code pour executer du code arbitraire
- **FPS cap a 30** — parce qu'un avatar anime n'a pas besoin de 60 FPS et
  chaque webview est un process Chromium complet
- **`retainContextWhenHidden: false`** par defaut — parce que garder une webview
  cachee en memoire est rarement justifie

### Etape 6 — Tests et debug

1. **F5** dans VS Code -> Extension Development Host (instance de test)
2. **Ctrl+Shift+P** -> "Developer: Open Webview Developer Tools" (inspecter la webview)
3. **@vscode/test-cli** + **@vscode/test-electron** pour les tests automatises
4. Les tests de webview sont difficiles a automatiser — privilegier les tests manuels

## Phase 4 — Verification

Lis `references/checklist.md` et valide chaque item avant de declarer l'extension prete.
La checklist couvre 10 sections et 60+ items : environnement, structure, extension host,
webview, integration Claude Code, commandes, performance, tests, packaging, securite.

## Options UX (adapter selon le besoin)

| Surface | Ideal pour |
|---------|------------|
| Sidebar (WebviewView) | Agent "toujours la" — mini-avatar + chat rapide |
| Panel bottom | Alternative sidebar — plus de largeur |
| Editeur (WebviewPanel) | Mode etendu — grand avatar + timeline + parametres |
| Terminal | Commandes textuelles + feedback status |

### Controles

- `agent-visual.start` / `agent-visual.stop` : demarrer/arreter l'agent
- `agent-visual.pause` : geler l'animation (l'agent reste visible)
- `agent-visual.changeAvatar` : QuickPick pour choisir un avatar
- `agent-visual.setSpeed` : vitesse d'animation (0.5x, 1x, 2x)
- `agent-visual.toggleFocus` : mode focus (desactive animations non essentielles)
- `agent-visual.openPanel` : ouvre le mode etendu dans l'editeur

### Accessibilite (obligatoire)

- `prefers-reduced-motion` : afficher un avatar statique quand active
- Navigation clavier complete (Tab, Enter, Escape)
- Attributs ARIA sur tous les elements interactifs
- Contrastes WCAG 2.1 AA via CSS variables VS Code

## Limites a connaitre

- Pas d'overlay flottant au-dessus de l'editeur (limitation VS Code)
- Chaque webview = un process Chromium (limiter a 2-3 simultanees)
- Pas d'acces au DOM de VS Code (isolation iframe)
- Pas de drag & drop entre webview et editeur
- Si l'utilisateur veut un avatar flottant systeme ou de la 3D lourde -> preferer Electron standalone

### Extensions existantes a connaitre

| Extension | Interet | Limite |
|-----------|---------|--------|
| VS Code Pets | Reference UX/animation pour avatars dans VS Code | Pas d'integration IA |
| Peon Pet | Avatar reactif aux evenements d'agents (mentionne Claude Code) | Tres recent, peu installe |

## References officielles

### VS Code
- Webview API : https://code.visualstudio.com/api/extension-guides/webview
- WebviewView : https://code.visualstudio.com/api/references/vscode-api#WebviewView
- Workspace Trust : https://code.visualstudio.com/api/extension-guides/workspace-trust
- Testing : https://code.visualstudio.com/api/working-with-extensions/testing-extension
- Manifest : https://code.visualstudio.com/api/references/extension-manifest

### Claude Code
- Overview : https://docs.anthropic.com/en/docs/claude-code/overview
- CLI : https://docs.anthropic.com/en/docs/claude-code/cli-reference
- Hooks : https://docs.anthropic.com/en/docs/claude-code/hooks
- MCP : https://docs.anthropic.com/en/docs/claude-code/mcp

## Index des fichiers de reference

| Fichier | Quand le charger |
|---------|------------------|
| `references/architecture-options.md` | Phase 2 — pour le comparatif detaille et les diagrammes |
| `references/snippets-extension.md` | Phase 3, etape 3 — tout le code TypeScript/HTML/CSS/JS |
| `references/snippets-claude-integration.md` | Phase 3, etape 4 — variantes CLI/hooks/MCP |
| `references/security-performance.md` | Phase 3, etape 5 — CSP, secrets, perf |
| `references/checklist.md` | Phase 4 — validation pre-release |

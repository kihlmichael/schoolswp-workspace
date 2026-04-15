# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Extension VS Code "Agent Visual" — avatars animés pilotés par Claude Code dans VS Code. Affiche un agent animé dans la sidebar et un panel plein écran, avec chat intégré via Claude CLI.

## Build & Dev

```bash
npm run compile          # build production (esbuild → dist/extension.js)
npm run watch            # dev watch mode (esbuild, pas de minification)
npm run test             # vscode-test (suite dans test/suite/)
```

Build config dans `esbuild.js` : entry `src/extension.ts`, output CommonJS Node18, external `vscode`, sourcemaps activés.

Pour tester l'extension : F5 dans VS Code (launch.json configuré — "Run Extension" lance une Extension Development Host).

## Architecture

```
Extension (extension.ts)
  ├── AgentSidebarProvider  →  Webview sidebar (persistante)
  ├── AgentPanel            →  Webview panel plein écran
  ├── AgentStateManager     →  State centralisé + EventEmitter
  └── ClaudeCLI bridge      →  child_process.spawn("claude -p ...")
          ↕ postMessage IPC
      Webview UI (agent.js + agent.css) → Canvas 2D animation
```

**Communication extension ↔ webview** : protocole `postMessage` bidirectionnel.
- Extension → Webview : `state:init`, `state:update`, `chat:response`, `chat:error`
- Webview → Extension : `ui:ready`, `chat:send`, `animation:control`

**State** : `AgentStateManager` est un singleton EventEmitter. Les providers (sidebar/panel) s'abonnent aux changements et broadcast vers les webviews.

**Claude CLI** : mode non-interactif `claude -p <prompt>`, timeout 120s, CWD = premier workspace folder. Support streaming via `--output-format stream-json`.

**Sécurité webview** : CSP nonce-based (`utils/nonce.ts`), `connect-src 'none'`, pas de dépendances externes dans le webview (vanilla JS + Canvas API).

**Workspace Trust** : mode restreint désactive l'intégration Claude CLI dans les workspaces non-trustés. L'animation reste active en lecture seule.

## Configuration extension

Settings namespace `agentVisual.*` :
- `defaultAvatar` : robot-default, robot-blue, cat-orange, ghost-pixel
- `animationSpeed` : 0.5–2.0
- `enableChat` : toggle chat panel
- `claudeIntegration` : cli | hooks | mcp | none

7 commandes enregistrées : `agentVisual.start/stop/pause/changeAvatar/setSpeed/toggleFocus/openPanel`

## Stack

TypeScript 5.5 (strict, ES2022) — esbuild 0.24 — VS Code API ≥1.98.0 — Canvas 2D pour l'animation — Zéro dépendance runtime (devDependencies uniquement)

## Conventions

- Fichiers kebab-case, 2 espaces indentation
- Commits conventionnels anglais (`feat:`, `fix:`, `chore:`)
- Pas de `rm` — utiliser `trash`
- Toute modification du protocole postMessage doit être synchronisée entre `src/` (TypeScript) et `media/webview/agent.js` (browser context)

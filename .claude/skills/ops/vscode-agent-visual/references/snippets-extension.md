# Snippets Extension VS Code — Code complet

## Table des matieres

1. [package.json (manifest)](#packagejson)
2. [extension.ts (point d'entree)](#extensionts)
3. [AgentSidebarProvider (WebviewView)](#webviewview)
4. [AgentPanel (WebviewPanel)](#webviewpanel)
5. [AgentStateManager (etat partage)](#state-manager)
6. [Webview HTML template](#webview-html)
7. [Webview CSS (theme-aware)](#webview-css)
8. [Webview JS (animation + chat)](#webview-js)
9. [Utilitaires (nonce, URI)](#utilitaires)
10. [AgentTerminal (pseudo-terminal)](#terminal)

---

## package.json {#packagejson}

```json
{
  "name": "vscode-agent-visual",
  "displayName": "Agent Visual",
  "description": "Avatars animes pilotes par Claude Code dans VS Code",
  "version": "0.1.0",
  "publisher": "your-publisher-id",
  "engines": {
    "vscode": "^1.98.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onView:agentVisual.sidebar"
  ],
  "main": "./dist/extension.js",
  "contributes": {
    "viewsContainers": {
      "activitybar": [
        {
          "id": "agent-visual",
          "title": "Agent Visual",
          "icon": "media/icons/agent.svg"
        }
      ]
    },
    "views": {
      "agent-visual": [
        {
          "type": "webview",
          "id": "agentVisual.sidebar",
          "name": "Agent",
          "icon": "media/icons/agent.svg"
        }
      ]
    },
    "commands": [
      {
        "command": "agentVisual.start",
        "title": "Agent Visual: Start",
        "icon": "$(play)"
      },
      {
        "command": "agentVisual.stop",
        "title": "Agent Visual: Stop",
        "icon": "$(debug-stop)"
      },
      {
        "command": "agentVisual.pause",
        "title": "Agent Visual: Pause Animation",
        "icon": "$(debug-pause)"
      },
      {
        "command": "agentVisual.changeAvatar",
        "title": "Agent Visual: Change Avatar"
      },
      {
        "command": "agentVisual.setSpeed",
        "title": "Agent Visual: Set Animation Speed"
      },
      {
        "command": "agentVisual.toggleFocus",
        "title": "Agent Visual: Toggle Focus Mode"
      },
      {
        "command": "agentVisual.openPanel",
        "title": "Agent Visual: Open Extended View",
        "icon": "$(screen-full)"
      }
    ],
    "menus": {
      "view/title": [
        {
          "command": "agentVisual.openPanel",
          "when": "view == agentVisual.sidebar",
          "group": "navigation"
        },
        {
          "command": "agentVisual.pause",
          "when": "view == agentVisual.sidebar",
          "group": "navigation"
        }
      ]
    },
    "configuration": {
      "title": "Agent Visual",
      "properties": {
        "agentVisual.defaultAvatar": {
          "type": "string",
          "default": "robot-default",
          "description": "Avatar par defaut"
        },
        "agentVisual.animationSpeed": {
          "type": "number",
          "default": 1,
          "description": "Vitesse d'animation (0.5 a 2.0)"
        },
        "agentVisual.enableChat": {
          "type": "boolean",
          "default": true,
          "description": "Activer le panneau de chat"
        },
        "agentVisual.claudeIntegration": {
          "type": "string",
          "enum": ["cli", "hooks", "mcp", "none"],
          "default": "cli",
          "description": "Mode d'integration Claude Code"
        }
      }
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "node esbuild.js",
    "watch": "node esbuild.js --watch",
    "test": "vscode-test"
  },
  "devDependencies": {
    "@types/vscode": "^1.98.0",
    "@types/node": "^20.0.0",
    "@vscode/test-cli": "^0.0.10",
    "@vscode/test-electron": "^2.4.0",
    "esbuild": "^0.24.0",
    "typescript": "^5.5.0"
  },
  "dependencies": {}
}
```

## extension.ts {#extensionts}

```typescript
import * as vscode from 'vscode';
import { AgentSidebarProvider } from './sidebar/AgentSidebarProvider';
import { AgentPanel } from './panel/AgentPanel';
import { AgentStateManager } from './state/AgentStateManager';

export function activate(context: vscode.ExtensionContext) {
  const stateManager = new AgentStateManager(context);
  const sidebarProvider = new AgentSidebarProvider(context, stateManager);

  // Register sidebar webview
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider(
      'agentVisual.sidebar',
      sidebarProvider,
      { webviewOptions: { retainContextWhenHidden: false } }
    )
  );

  // Commands
  context.subscriptions.push(
    vscode.commands.registerCommand('agentVisual.start', () => {
      stateManager.setRunning(true);
    }),
    vscode.commands.registerCommand('agentVisual.stop', () => {
      stateManager.setRunning(false);
    }),
    vscode.commands.registerCommand('agentVisual.pause', () => {
      stateManager.togglePause();
    }),
    vscode.commands.registerCommand('agentVisual.changeAvatar', async () => {
      const avatars = stateManager.getAvailableAvatars();
      const picked = await vscode.window.showQuickPick(avatars, {
        placeHolder: 'Choisir un avatar'
      });
      if (picked) {
        stateManager.setAvatar(picked);
      }
    }),
    vscode.commands.registerCommand('agentVisual.setSpeed', async () => {
      const speed = await vscode.window.showQuickPick(
        ['0.5x', '1x', '1.5x', '2x'],
        { placeHolder: 'Vitesse d\'animation' }
      );
      if (speed) {
        stateManager.setSpeed(parseFloat(speed));
      }
    }),
    vscode.commands.registerCommand('agentVisual.toggleFocus', () => {
      stateManager.toggleFocusMode();
    }),
    vscode.commands.registerCommand('agentVisual.openPanel', () => {
      AgentPanel.createOrShow(context, stateManager);
    })
  );

  // Check Workspace Trust
  if (!vscode.workspace.isTrusted) {
    vscode.window.showWarningMessage(
      'Agent Visual: certaines fonctionnalites sont desactivees en mode restreint.'
    );
    stateManager.setRestrictedMode(true);
  }

  context.subscriptions.push(
    vscode.workspace.onDidGrantWorkspaceTrust(() => {
      stateManager.setRestrictedMode(false);
    })
  );
}

export function deactivate() {
  // Cleanup is handled by disposables in context.subscriptions
}
```

## AgentSidebarProvider (WebviewView) {#webviewview}

```typescript
// src/sidebar/AgentSidebarProvider.ts
import * as vscode from 'vscode';
import { AgentStateManager } from '../state/AgentStateManager';
import { getNonce } from '../utils/nonce';
import { getWebviewContent } from '../utils/webview-helpers';

export class AgentSidebarProvider implements vscode.WebviewViewProvider {
  public static readonly viewType = 'agentVisual.sidebar';
  private _view?: vscode.WebviewView;

  constructor(
    private readonly _context: vscode.ExtensionContext,
    private readonly _stateManager: AgentStateManager
  ) {
    // Listen to state changes and forward to webview
    this._stateManager.onDidChangeState((state) => {
      this._view?.webview.postMessage({
        type: 'state:update',
        payload: state
      });
    });
  }

  public resolveWebviewView(
    webviewView: vscode.WebviewView,
    _context: vscode.WebviewViewResolveContext,
    _token: vscode.CancellationToken
  ): void {
    this._view = webviewView;

    webviewView.webview.options = {
      enableScripts: true,
      localResourceRoots: [
        vscode.Uri.joinPath(this._context.extensionUri, 'media'),
        vscode.Uri.joinPath(this._context.extensionUri, 'dist')
      ]
    };

    webviewView.webview.html = getWebviewContent(
      webviewView.webview,
      this._context.extensionUri,
      'sidebar'
    );

    // Handle messages from webview
    webviewView.webview.onDidReceiveMessage(
      (message) => this._handleMessage(message),
      undefined,
      []
    );

    // Send initial state
    webviewView.webview.postMessage({
      type: 'state:init',
      payload: this._stateManager.getState()
    });

    // Cleanup on dispose
    webviewView.onDidDispose(() => {
      this._view = undefined;
    });
  }

  private async _handleMessage(message: { type: string; payload?: unknown }) {
    // SECURITY: validate message type against whitelist
    const allowedTypes = ['chat:send', 'avatar:request', 'animation:control', 'ui:ready'];
    if (!allowedTypes.includes(message.type)) {
      console.warn(`[AgentVisual] Unknown message type: ${message.type}`);
      return;
    }

    switch (message.type) {
      case 'chat:send': {
        const text = message.payload as string;
        if (typeof text !== 'string' || text.length > 10000) {
          return;
        }
        this._stateManager.setChatLoading(true);
        try {
          const response = await this._stateManager.sendToClaudeCode(text);
          this._view?.webview.postMessage({
            type: 'chat:response',
            payload: { text: response, emotion: 'happy' }
          });
        } catch (err) {
          this._view?.webview.postMessage({
            type: 'chat:error',
            payload: { error: (err as Error).message }
          });
        } finally {
          this._stateManager.setChatLoading(false);
        }
        break;
      }
      case 'animation:control': {
        const action = message.payload as { action: string };
        if (action?.action === 'pause') {
          this._stateManager.togglePause();
        }
        break;
      }
      case 'ui:ready': {
        this._view?.webview.postMessage({
          type: 'state:init',
          payload: this._stateManager.getState()
        });
        break;
      }
    }
  }
}
```

## AgentPanel (WebviewPanel) {#webviewpanel}

```typescript
// src/panel/AgentPanel.ts
import * as vscode from 'vscode';
import { AgentStateManager } from '../state/AgentStateManager';
import { getWebviewContent } from '../utils/webview-helpers';

export class AgentPanel {
  public static currentPanel: AgentPanel | undefined;
  private static readonly viewType = 'agentVisual.panel';
  private readonly _panel: vscode.WebviewPanel;
  private _disposables: vscode.Disposable[] = [];

  public static createOrShow(
    context: vscode.ExtensionContext,
    stateManager: AgentStateManager
  ) {
    const column = vscode.window.activeTextEditor
      ? vscode.window.activeTextEditor.viewColumn
      : undefined;

    // If panel already exists, reveal it
    if (AgentPanel.currentPanel) {
      AgentPanel.currentPanel._panel.reveal(column);
      return;
    }

    const panel = vscode.window.createWebviewPanel(
      AgentPanel.viewType,
      'Agent Visual — Mode Etendu',
      column || vscode.ViewColumn.One,
      {
        enableScripts: true,
        localResourceRoots: [
          vscode.Uri.joinPath(context.extensionUri, 'media'),
          vscode.Uri.joinPath(context.extensionUri, 'dist')
        ],
        retainContextWhenHidden: false // Set true ONLY if state is expensive to rebuild
      }
    );

    AgentPanel.currentPanel = new AgentPanel(panel, context, stateManager);
  }

  private constructor(
    panel: vscode.WebviewPanel,
    context: vscode.ExtensionContext,
    private readonly _stateManager: AgentStateManager
  ) {
    this._panel = panel;

    this._panel.webview.html = getWebviewContent(
      this._panel.webview,
      context.extensionUri,
      'panel'
    );

    // Forward state changes
    const stateListener = this._stateManager.onDidChangeState((state) => {
      this._panel.webview.postMessage({
        type: 'state:update',
        payload: state
      });
    });
    this._disposables.push(stateListener);

    // Handle messages (same pattern as sidebar)
    this._panel.webview.onDidReceiveMessage(
      (message) => this._handleMessage(message),
      undefined,
      this._disposables
    );

    // Cleanup
    this._panel.onDidDispose(() => this.dispose(), null, this._disposables);
  }

  private async _handleMessage(message: { type: string; payload?: unknown }) {
    // Same validation as sidebar — consider extracting to shared handler
    const allowedTypes = ['chat:send', 'avatar:request', 'animation:control', 'ui:ready'];
    if (!allowedTypes.includes(message.type)) {
      return;
    }
    // ... same logic as AgentSidebarProvider._handleMessage
  }

  public dispose() {
    AgentPanel.currentPanel = undefined;
    this._panel.dispose();
    while (this._disposables.length) {
      const d = this._disposables.pop();
      d?.dispose();
    }
  }
}
```

## AgentStateManager {#state-manager}

```typescript
// src/state/AgentStateManager.ts
import * as vscode from 'vscode';
import { ClaudeCLI } from '../bridge/ClaudeCLI';

interface AgentState {
  running: boolean;
  paused: boolean;
  avatar: string;
  speed: number;
  focusMode: boolean;
  chatLoading: boolean;
  restrictedMode: boolean;
  lastActivity?: { type: string; detail?: string };
}

export class AgentStateManager {
  private _state: AgentState;
  private _onDidChangeState = new vscode.EventEmitter<AgentState>();
  public readonly onDidChangeState = this._onDidChangeState.event;
  private _claudeBridge: ClaudeCLI;

  constructor(private readonly _context: vscode.ExtensionContext) {
    const config = vscode.workspace.getConfiguration('agentVisual');
    this._state = {
      running: true,
      paused: false,
      avatar: config.get<string>('defaultAvatar', 'robot-default'),
      speed: config.get<number>('animationSpeed', 1),
      focusMode: false,
      chatLoading: false,
      restrictedMode: false
    };
    this._claudeBridge = new ClaudeCLI();
  }

  public getState(): AgentState {
    return { ...this._state };
  }

  public getAvailableAvatars(): string[] {
    // Scan media/animations/ for available avatars
    return ['robot-default', 'robot-blue', 'cat-orange', 'ghost-pixel'];
  }

  public setRunning(running: boolean) {
    this._state.running = running;
    this._emit();
  }

  public togglePause() {
    this._state.paused = !this._state.paused;
    this._emit();
  }

  public setAvatar(avatar: string) {
    this._state.avatar = avatar;
    this._emit();
  }

  public setSpeed(speed: number) {
    this._state.speed = Math.max(0.5, Math.min(2, speed));
    this._emit();
  }

  public toggleFocusMode() {
    this._state.focusMode = !this._state.focusMode;
    this._emit();
  }

  public setChatLoading(loading: boolean) {
    this._state.chatLoading = loading;
    this._emit();
  }

  public setRestrictedMode(restricted: boolean) {
    this._state.restrictedMode = restricted;
    this._emit();
  }

  public async sendToClaudeCode(prompt: string): Promise<string> {
    if (this._state.restrictedMode) {
      throw new Error('Claude Code integration desactivee en mode restreint');
    }
    return this._claudeBridge.send(prompt);
  }

  private _emit() {
    this._onDidChangeState.fire({ ...this._state });
  }
}
```

## Webview HTML template {#webview-html}

```html
<!-- media/webview/agent.html -->
<!-- This is a TEMPLATE — placeholders are replaced by getWebviewContent() -->
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy"
    content="default-src 'none';
             img-src {{cspSource}} data:;
             script-src 'nonce-{{nonce}}';
             style-src {{cspSource}} 'nonce-{{nonce}}';
             font-src {{cspSource}};">
  <link href="{{styleUri}}" rel="stylesheet" nonce="{{nonce}}">
  <title>Agent Visual</title>
</head>
<body data-mode="{{mode}}">
  <div id="agent-container" role="application" aria-label="Agent Visual">

    <!-- Avatar area -->
    <div id="avatar-stage" role="img" aria-label="Avatar anime">
      <canvas id="avatar-canvas" width="200" height="200"></canvas>
      <!-- OR for Lottie: <div id="lottie-container"></div> -->
    </div>

    <!-- Status bar -->
    <div id="status-bar" role="status" aria-live="polite">
      <span id="status-text">Pret</span>
      <span id="status-indicator" class="indicator idle"></span>
    </div>

    <!-- Chat area (if enabled) -->
    <div id="chat-area" role="log" aria-label="Conversation avec l'agent">
      <div id="chat-messages"></div>
      <form id="chat-form" role="search">
        <input
          id="chat-input"
          type="text"
          placeholder="Parle a l'agent..."
          aria-label="Message pour l'agent"
          autocomplete="off"
        >
        <button type="submit" aria-label="Envoyer">
          <span class="codicon codicon-send"></span>
        </button>
      </form>
    </div>

    <!-- Controls -->
    <div id="controls" role="toolbar" aria-label="Controles de l'agent">
      <button id="btn-pause" aria-label="Pause animation" title="Pause">
        <span class="codicon codicon-debug-pause"></span>
      </button>
      <button id="btn-speed" aria-label="Vitesse" title="Vitesse">1x</button>
    </div>
  </div>

  <script nonce="{{nonce}}" src="{{scriptUri}}"></script>
</body>
</html>
```

## Webview CSS (theme-aware) {#webview-css}

```css
/* media/webview/agent.css */

/* Use VS Code CSS variables for theme integration */
:root {
  --agent-bg: var(--vscode-sideBar-background, #1e1e1e);
  --agent-fg: var(--vscode-sideBar-foreground, #cccccc);
  --agent-border: var(--vscode-sideBar-border, #333333);
  --agent-input-bg: var(--vscode-input-background, #3c3c3c);
  --agent-input-fg: var(--vscode-input-foreground, #cccccc);
  --agent-input-border: var(--vscode-input-border, #555555);
  --agent-button-bg: var(--vscode-button-background, #0e639c);
  --agent-button-fg: var(--vscode-button-foreground, #ffffff);
  --agent-accent: var(--vscode-focusBorder, #007fd4);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: var(--agent-bg);
  color: var(--agent-fg);
  font-family: var(--vscode-font-family);
  font-size: var(--vscode-font-size);
  overflow: hidden;
}

#agent-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 8px;
  gap: 8px;
}

/* Avatar stage */
#avatar-stage {
  flex: 0 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 150px;
  max-height: 250px;
  border-radius: 8px;
  background: var(--vscode-editor-background);
  overflow: hidden;
}

#avatar-canvas {
  max-width: 100%;
  max-height: 100%;
  image-rendering: pixelated; /* for pixel art; remove for vector */
}

/* Status bar */
#status-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  font-size: 0.85em;
  opacity: 0.8;
}

.indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.indicator.idle { background: #888; }
.indicator.active { background: #4caf50; }
.indicator.loading { background: #ff9800; animation: pulse 1s infinite; }
.indicator.error { background: #f44336; }

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

/* Chat area */
#chat-area {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  min-height: 0;
  overflow: hidden;
}

#chat-messages {
  flex: 1 1 auto;
  overflow-y: auto;
  padding: 4px;
}

.chat-msg {
  margin-bottom: 8px;
  padding: 6px 10px;
  border-radius: 6px;
  max-width: 90%;
  word-wrap: break-word;
}
.chat-msg.user {
  background: var(--agent-button-bg);
  color: var(--agent-button-fg);
  margin-left: auto;
}
.chat-msg.agent {
  background: var(--agent-input-bg);
  border: 1px solid var(--agent-border);
}

#chat-form {
  display: flex;
  gap: 4px;
  padding-top: 4px;
}

#chat-input {
  flex: 1;
  padding: 6px 10px;
  background: var(--agent-input-bg);
  color: var(--agent-input-fg);
  border: 1px solid var(--agent-input-border);
  border-radius: 4px;
  outline: none;
  font-family: inherit;
  font-size: inherit;
}

#chat-input:focus {
  border-color: var(--agent-accent);
}

#chat-form button {
  padding: 6px 10px;
  background: var(--agent-button-bg);
  color: var(--agent-button-fg);
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* Controls toolbar */
#controls {
  display: flex;
  gap: 4px;
  padding-top: 4px;
  border-top: 1px solid var(--agent-border);
}

#controls button {
  padding: 4px 8px;
  background: transparent;
  color: var(--agent-fg);
  border: 1px solid var(--agent-border);
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85em;
}

#controls button:hover {
  background: var(--agent-input-bg);
}

/* Reduce motion */
@media (prefers-reduced-motion: reduce) {
  #avatar-canvas,
  #lottie-container {
    animation: none !important;
    transition: none !important;
  }
  .indicator.loading {
    animation: none;
    opacity: 0.6;
  }
}

/* Panel mode (larger) */
body[data-mode="panel"] #avatar-stage {
  min-height: 250px;
  max-height: 400px;
}

body[data-mode="panel"] #agent-container {
  max-width: 800px;
  margin: 0 auto;
}
```

## Webview JS (animation + chat) {#webview-js}

```javascript
// media/webview/agent.js
// This script runs INSIDE the webview (browser context)

(function () {
  // Acquire the VS Code API (only callable once per webview)
  const vscode = acquireVsCodeApi();

  // DOM elements
  const canvas = document.getElementById('avatar-canvas');
  const ctx = canvas ? canvas.getContext('2d') : null;
  const statusText = document.getElementById('status-text');
  const statusIndicator = document.getElementById('status-indicator');
  const chatMessages = document.getElementById('chat-messages');
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');
  const btnPause = document.getElementById('btn-pause');
  const btnSpeed = document.getElementById('btn-speed');

  // State
  let state = {
    running: true,
    paused: false,
    avatar: 'robot-default',
    speed: 1,
    focusMode: false,
    chatLoading: false
  };

  // --- Animation loop ---
  const FPS_CAP = 30;
  const FRAME_DURATION = 1000 / FPS_CAP;
  let lastFrameTime = 0;
  let animationFrame = 0;

  function drawFrame(timestamp) {
    if (!state.running) return;
    if (state.paused) {
      requestAnimationFrame(drawFrame);
      return;
    }

    // Check reduce motion preference
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
      drawStaticAvatar();
      return;
    }

    // FPS cap
    const elapsed = timestamp - lastFrameTime;
    if (elapsed < FRAME_DURATION / state.speed) {
      requestAnimationFrame(drawFrame);
      return;
    }
    lastFrameTime = timestamp;
    animationFrame++;

    if (ctx) {
      // Clear
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Simple bouncing circle as placeholder
      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;
      const bounce = Math.sin(animationFrame * 0.05) * 10;

      ctx.beginPath();
      ctx.arc(centerX, centerY + bounce, 40, 0, Math.PI * 2);
      ctx.fillStyle = state.chatLoading ? '#ff9800' : '#4caf50';
      ctx.fill();

      // Eyes
      ctx.fillStyle = '#fff';
      ctx.beginPath();
      ctx.arc(centerX - 12, centerY + bounce - 8, 6, 0, Math.PI * 2);
      ctx.arc(centerX + 12, centerY + bounce - 8, 6, 0, Math.PI * 2);
      ctx.fill();

      // Pupils (follow frame for "alive" look)
      const pupilOffset = Math.sin(animationFrame * 0.02) * 2;
      ctx.fillStyle = '#333';
      ctx.beginPath();
      ctx.arc(centerX - 12 + pupilOffset, centerY + bounce - 8, 3, 0, Math.PI * 2);
      ctx.arc(centerX + 12 + pupilOffset, centerY + bounce - 8, 3, 0, Math.PI * 2);
      ctx.fill();
    }

    requestAnimationFrame(drawFrame);
  }

  function drawStaticAvatar() {
    if (!ctx) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    ctx.beginPath();
    ctx.arc(centerX, centerY, 40, 0, Math.PI * 2);
    ctx.fillStyle = '#4caf50';
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.beginPath();
    ctx.arc(centerX - 12, centerY - 8, 6, 0, Math.PI * 2);
    ctx.arc(centerX + 12, centerY - 8, 6, 0, Math.PI * 2);
    ctx.fill();
  }

  // --- Chat ---
  function addChatMessage(text, sender) {
    if (!chatMessages) return;
    const div = document.createElement('div');
    div.className = `chat-msg ${sender}`;
    div.textContent = text;
    div.setAttribute('role', 'article');
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  if (chatForm) {
    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if (!text) return;
      addChatMessage(text, 'user');
      chatInput.value = '';
      vscode.postMessage({ type: 'chat:send', payload: text });
    });
  }

  // --- Controls ---
  if (btnPause) {
    btnPause.addEventListener('click', () => {
      vscode.postMessage({ type: 'animation:control', payload: { action: 'pause' } });
    });
  }

  // --- Message handling from extension ---
  window.addEventListener('message', (event) => {
    const message = event.data;
    switch (message.type) {
      case 'state:init':
      case 'state:update':
        state = { ...state, ...message.payload };
        updateUI();
        break;
      case 'chat:response':
        addChatMessage(message.payload.text, 'agent');
        break;
      case 'chat:error':
        addChatMessage(`Erreur: ${message.payload.error}`, 'agent');
        break;
      case 'avatar:change':
        state.avatar = message.payload.avatar;
        // Load new animation assets here
        break;
    }
  });

  function updateUI() {
    if (statusText) {
      statusText.textContent = state.chatLoading ? 'Reflexion...'
        : state.paused ? 'En pause'
        : state.running ? 'Actif'
        : 'Arrete';
    }
    if (statusIndicator) {
      statusIndicator.className = 'indicator ' + (
        state.chatLoading ? 'loading'
        : state.running ? 'active'
        : 'idle'
      );
    }
    if (btnSpeed) {
      btnSpeed.textContent = `${state.speed}x`;
    }
  }

  // --- Init ---
  vscode.postMessage({ type: 'ui:ready' });
  requestAnimationFrame(drawFrame);
})();
```

## Utilitaires {#utilitaires}

```typescript
// src/utils/nonce.ts
import * as crypto from 'crypto';

export function getNonce(): string {
  return crypto.randomBytes(16).toString('hex');
}
```

```typescript
// src/utils/webview-helpers.ts
import * as vscode from 'vscode';
import { getNonce } from './nonce';

export function getWebviewContent(
  webview: vscode.Webview,
  extensionUri: vscode.Uri,
  mode: 'sidebar' | 'panel'
): string {
  const nonce = getNonce();
  const cspSource = webview.cspSource;

  // URIs for resources
  const styleUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'media', 'webview', 'agent.css')
  );
  const scriptUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'media', 'webview', 'agent.js')
  );

  return `<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy"
    content="default-src 'none';
             img-src ${cspSource} data:;
             script-src 'nonce-${nonce}';
             style-src ${cspSource} 'nonce-${nonce}';
             font-src ${cspSource};">
  <link href="${styleUri}" rel="stylesheet" nonce="${nonce}">
  <title>Agent Visual</title>
</head>
<body data-mode="${mode}">
  <div id="agent-container" role="application" aria-label="Agent Visual">
    <div id="avatar-stage" role="img" aria-label="Avatar anime">
      <canvas id="avatar-canvas" width="200" height="200"></canvas>
    </div>
    <div id="status-bar" role="status" aria-live="polite">
      <span id="status-text">Pret</span>
      <span id="status-indicator" class="indicator idle"></span>
    </div>
    <div id="chat-area" role="log" aria-label="Conversation">
      <div id="chat-messages"></div>
      <form id="chat-form">
        <input id="chat-input" type="text" placeholder="Parle a l'agent..."
               aria-label="Message" autocomplete="off">
        <button type="submit" aria-label="Envoyer">Envoyer</button>
      </form>
    </div>
    <div id="controls" role="toolbar" aria-label="Controles">
      <button id="btn-pause" aria-label="Pause">Pause</button>
      <button id="btn-speed" aria-label="Vitesse">1x</button>
    </div>
  </div>
  <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
</html>`;
}
```

## AgentTerminal (pseudo-terminal optionnel) {#terminal}

```typescript
// src/terminal/AgentTerminal.ts
import * as vscode from 'vscode';

export class AgentTerminal implements vscode.Pseudoterminal {
  private _writeEmitter = new vscode.EventEmitter<string>();
  onDidWrite: vscode.Event<string> = this._writeEmitter.event;
  private _closeEmitter = new vscode.EventEmitter<number>();
  onDidClose: vscode.Event<number> = this._closeEmitter.event;

  private _buffer = '';

  open(): void {
    this._writeEmitter.fire('Agent Visual Terminal\r\n');
    this._writeEmitter.fire('Tape un message pour parler a l\'agent, ou "exit" pour quitter.\r\n\r\n');
    this._prompt();
  }

  close(): void {
    // Cleanup
  }

  handleInput(data: string): void {
    // Handle character by character (terminal sends raw input)
    if (data === '\r') { // Enter
      this._writeEmitter.fire('\r\n');
      this._processCommand(this._buffer.trim());
      this._buffer = '';
    } else if (data === '\x7f') { // Backspace
      if (this._buffer.length > 0) {
        this._buffer = this._buffer.slice(0, -1);
        this._writeEmitter.fire('\b \b');
      }
    } else if (data === '\x03') { // Ctrl+C
      this._writeEmitter.fire('^C\r\n');
      this._buffer = '';
      this._prompt();
    } else {
      this._buffer += data;
      this._writeEmitter.fire(data);
    }
  }

  private _prompt() {
    this._writeEmitter.fire('\x1b[36magent>\x1b[0m ');
  }

  private async _processCommand(input: string) {
    if (!input) {
      this._prompt();
      return;
    }

    if (input === 'exit' || input === 'quit') {
      this._writeEmitter.fire('Au revoir!\r\n');
      this._closeEmitter.fire(0);
      return;
    }

    if (input === 'status') {
      this._writeEmitter.fire('Agent: actif | Avatar: robot-default | Speed: 1x\r\n');
      this._prompt();
      return;
    }

    // Forward to Claude Code
    this._writeEmitter.fire('\x1b[33mReflexion...\x1b[0m\r\n');
    // TODO: integrate with AgentStateManager.sendToClaudeCode()
    this._writeEmitter.fire('(integration Claude Code a connecter ici)\r\n');
    this._prompt();
  }

  /** Call this to display activity from extension host */
  public writeOutput(text: string) {
    this._writeEmitter.fire(`\x1b[90m${text}\x1b[0m\r\n`);
  }
}

// Registration helper (call from extension.ts)
export function registerAgentTerminal(context: vscode.ExtensionContext): AgentTerminal {
  const terminal = new AgentTerminal();
  const pty = vscode.window.createTerminal({
    name: 'Agent Visual',
    pty: terminal
  });
  context.subscriptions.push({ dispose: () => pty.dispose() });
  return terminal;
}
```

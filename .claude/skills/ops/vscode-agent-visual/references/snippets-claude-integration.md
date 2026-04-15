# Integration Claude Code — 3 Variantes

## Table des matieres

1. [Variante A — CLI (`claude -p`)](#variante-a)
2. [Variante B — Hooks/Plugins](#variante-b)
3. [Variante C — MCP Server](#variante-c)
4. [SecretStorage pour les tokens](#secret-storage)
5. [Choix et migration entre variantes](#migration)

---

## Variante A — CLI (`claude -p`) {#variante-a}

La plus simple. Spawn le CLI Claude Code en subprocess et parse la sortie.

```typescript
// src/bridge/ClaudeCLI.ts
import { spawn } from 'child_process';
import * as vscode from 'vscode';

export class ClaudeCLI {
  private _claudePath: string;

  constructor() {
    // Detect Claude CLI path
    // On most systems, 'claude' is in PATH after npm install -g @anthropic-ai/claude-code
    this._claudePath = 'claude';
  }

  /**
   * Send a prompt to Claude Code CLI and get the response.
   * Uses `claude -p` for non-interactive single-prompt mode.
   */
  public async send(prompt: string): Promise<string> {
    return new Promise((resolve, reject) => {
      const args = [
        '-p', prompt,
        '--output-format', 'text'
      ];

      const proc = spawn(this._claudePath, args, {
        cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath,
        env: { ...process.env },
        shell: true,
        timeout: 120_000 // 2 minutes max
      });

      let stdout = '';
      let stderr = '';

      proc.stdout.on('data', (data: Buffer) => {
        stdout += data.toString();
      });

      proc.stderr.on('data', (data: Buffer) => {
        stderr += data.toString();
      });

      proc.on('close', (code) => {
        if (code === 0) {
          resolve(stdout.trim());
        } else {
          reject(new Error(`Claude CLI exited with code ${code}: ${stderr}`));
        }
      });

      proc.on('error', (err) => {
        reject(new Error(`Failed to spawn Claude CLI: ${err.message}`));
      });
    });
  }

  /**
   * Send a prompt with streaming output (for progressive display).
   * Calls onChunk for each piece of text received.
   */
  public async sendStreaming(
    prompt: string,
    onChunk: (text: string) => void
  ): Promise<string> {
    return new Promise((resolve, reject) => {
      const args = [
        '-p', prompt,
        '--output-format', 'stream-json'
      ];

      const proc = spawn(this._claudePath, args, {
        cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath,
        env: { ...process.env },
        shell: true,
        timeout: 120_000
      });

      let fullResponse = '';
      let buffer = '';

      proc.stdout.on('data', (data: Buffer) => {
        buffer += data.toString();
        // Parse JSON lines
        const lines = buffer.split('\n');
        buffer = lines.pop() || ''; // Keep incomplete line in buffer

        for (const line of lines) {
          if (!line.trim()) continue;
          try {
            const parsed = JSON.parse(line);
            if (parsed.type === 'assistant' && parsed.message?.content) {
              for (const block of parsed.message.content) {
                if (block.type === 'text') {
                  onChunk(block.text);
                  fullResponse += block.text;
                }
              }
            }
          } catch {
            // Not JSON — raw text fallback
            onChunk(line);
            fullResponse += line;
          }
        }
      });

      proc.on('close', (code) => {
        if (code === 0) {
          resolve(fullResponse);
        } else {
          reject(new Error(`Claude CLI streaming error (code ${code})`));
        }
      });

      proc.on('error', (err) => {
        reject(new Error(`Failed to spawn Claude CLI: ${err.message}`));
      });
    });
  }

  /**
   * Check if Claude CLI is available.
   */
  public async isAvailable(): Promise<boolean> {
    return new Promise((resolve) => {
      const proc = spawn(this._claudePath, ['--version'], {
        shell: true,
        timeout: 5000
      });
      proc.on('close', (code) => resolve(code === 0));
      proc.on('error', () => resolve(false));
    });
  }
}
```

### Avantages et limites

- **+** Cross-platform, simple, pas de dependance supplementaire
- **+** Fonctionne des que Claude Code CLI est installe
- **-** Pas d'evenements en temps reel (request/response seulement)
- **-** Chaque appel spawn un process — eviter les appels trop frequents
- **-** Le streaming JSON peut varier entre versions du CLI

---

## Variante B — Hooks/Plugins {#variante-b}

Plus reactive. L'extension ecoute les evenements emis par les hooks Claude Code
et peut animer l'avatar en consequence (edit en cours, test lance, erreur, etc.).

### Configuration des hooks

Les hooks Claude Code se configurent dans `.claude/settings.json` ou les settings globaux.
L'idee : un hook `PostToolUse` ecrit un evenement JSON dans un fichier que l'extension surveille.

```json
// .claude/settings.json (dans le workspace)
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "node .claude/hooks/emit-event.js post-tool-use \"$TOOL_NAME\" \"$FILE_PATH\""
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "node .claude/hooks/emit-event.js notification \"$MESSAGE\""
          }
        ]
      }
    ]
  }
}
```

### Script emetteur d'evenements

```javascript
// .claude/hooks/emit-event.js
// Ecrit un evenement JSON dans un fichier que l'extension VS Code surveille.
const fs = require('fs');
const path = require('path');
const os = require('os');

const eventFile = path.join(os.tmpdir(), 'vscode-agent-visual-events.jsonl');
const [, , eventType, ...args] = process.argv;

const event = {
  timestamp: new Date().toISOString(),
  type: eventType,
  data: args.reduce((acc, arg, i) => {
    acc[`arg${i}`] = arg;
    return acc;
  }, {})
};

fs.appendFileSync(eventFile, JSON.stringify(event) + '\n', 'utf-8');
```

### Consommateur d'evenements cote extension

```typescript
// src/bridge/ClaudeHooks.ts
import * as vscode from 'vscode';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';

interface HookEvent {
  timestamp: string;
  type: string;
  data: Record<string, string>;
}

export class ClaudeHooks implements vscode.Disposable {
  private _watcher?: fs.FSWatcher;
  private _onEvent = new vscode.EventEmitter<HookEvent>();
  public readonly onEvent = this._onEvent.event;
  private _eventFile: string;
  private _lastSize = 0;

  constructor() {
    this._eventFile = path.join(os.tmpdir(), 'vscode-agent-visual-events.jsonl');
  }

  /**
   * Start watching for hook events.
   */
  public start(): void {
    // Ensure file exists
    if (!fs.existsSync(this._eventFile)) {
      fs.writeFileSync(this._eventFile, '', 'utf-8');
    }
    this._lastSize = fs.statSync(this._eventFile).size;

    this._watcher = fs.watch(this._eventFile, (eventType) => {
      if (eventType === 'change') {
        this._readNewEvents();
      }
    });
  }

  private _readNewEvents(): void {
    try {
      const stat = fs.statSync(this._eventFile);
      if (stat.size <= this._lastSize) return;

      // Read only new content
      const fd = fs.openSync(this._eventFile, 'r');
      const buffer = Buffer.alloc(stat.size - this._lastSize);
      fs.readSync(fd, buffer, 0, buffer.length, this._lastSize);
      fs.closeSync(fd);

      this._lastSize = stat.size;

      const lines = buffer.toString('utf-8').trim().split('\n');
      for (const line of lines) {
        if (!line) continue;
        try {
          const event: HookEvent = JSON.parse(line);
          this._onEvent.fire(event);
        } catch {
          // Skip malformed lines
        }
      }
    } catch {
      // File may have been rotated or deleted
    }
  }

  /**
   * Map hook events to avatar emotions/animations.
   */
  public static mapEventToAnimation(event: HookEvent): {
    animation: string;
    emotion: string;
    detail?: string;
  } {
    switch (event.type) {
      case 'post-tool-use':
        const tool = event.data.arg0;
        if (tool === 'Edit' || tool === 'Write') {
          return { animation: 'coding', emotion: 'focused', detail: event.data.arg1 };
        }
        if (tool === 'Bash') {
          return { animation: 'running', emotion: 'excited' };
        }
        if (tool === 'Read' || tool === 'Grep') {
          return { animation: 'reading', emotion: 'curious' };
        }
        return { animation: 'working', emotion: 'neutral' };

      case 'notification':
        return { animation: 'alert', emotion: 'surprised', detail: event.data.arg0 };

      default:
        return { animation: 'idle', emotion: 'neutral' };
    }
  }

  public dispose(): void {
    this._watcher?.close();
    this._onEvent.dispose();
  }
}
```

### Integration dans le StateManager

```typescript
// Ajouter dans AgentStateManager (apres le constructeur) :

// Si mode hooks actif
if (config.get<string>('claudeIntegration') === 'hooks') {
  const hooks = new ClaudeHooks();
  hooks.start();
  hooks.onEvent((event) => {
    const mapped = ClaudeHooks.mapEventToAnimation(event);
    this._state.lastActivity = {
      type: mapped.animation,
      detail: mapped.detail
    };
    this._emit();
  });
}
```

---

## Variante C — MCP Server {#variante-c}

La plus puissante. Un serveur MCP custom expose des outils que Claude Code peut appeler,
et l'extension peut aussi consommer les outils du serveur MCP.

### Serveur MCP minimal (Node.js)

```typescript
// mcp-server/src/index.ts
// Serveur MCP qui expose des outils pour piloter l'agent visuel
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const server = new McpServer({
  name: 'agent-visual-mcp',
  version: '1.0.0'
});

// Tool: notify the avatar of an activity
server.tool(
  'notify_avatar',
  'Notify the visual agent of an activity (coding, testing, thinking, etc.)',
  {
    activity: z.enum(['coding', 'testing', 'thinking', 'reading', 'idle', 'celebrating']),
    detail: z.string().optional(),
    emotion: z.enum(['happy', 'focused', 'curious', 'surprised', 'neutral']).optional()
  },
  async ({ activity, detail, emotion }) => {
    // Write event to shared channel (file, socket, etc.)
    const event = { type: 'avatar:activity', activity, detail, emotion };
    // In production: use IPC, named pipe, or HTTP to reach the extension
    console.error(JSON.stringify(event)); // stderr for logging
    return {
      content: [{ type: 'text', text: `Avatar notified: ${activity}` }]
    };
  }
);

// Tool: send a chat message to appear in the agent's chat panel
server.tool(
  'agent_chat',
  'Send a message to appear in the visual agent chat panel',
  {
    message: z.string(),
    sender: z.enum(['agent', 'system']).optional()
  },
  async ({ message, sender }) => {
    const event = { type: 'chat:inject', text: message, sender: sender || 'agent' };
    console.error(JSON.stringify(event));
    return {
      content: [{ type: 'text', text: 'Message sent to chat panel' }]
    };
  }
);

// Resource: current avatar state
server.resource(
  'avatar-state',
  'agent-visual://state',
  async () => ({
    contents: [{
      uri: 'agent-visual://state',
      mimeType: 'application/json',
      text: JSON.stringify({
        running: true,
        avatar: 'robot-default',
        speed: 1,
        focusMode: false
      })
    }]
  })
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
```

### Configuration MCP dans Claude Code

```json
// .mcp.json (a la racine du workspace)
{
  "mcpServers": {
    "agent-visual": {
      "command": "node",
      "args": ["./mcp-server/dist/index.js"],
      "env": {}
    }
  }
}
```

### Consommateur MCP cote extension

```typescript
// src/bridge/ClaudeMCP.ts
import * as vscode from 'vscode';

/**
 * Consomme les evenements MCP via le meme pattern de fichier JSONL
 * que les hooks, mais les evenements viennent du serveur MCP.
 *
 * Alternative: utiliser un serveur HTTP/WebSocket local pour
 * communication bidirectionnelle directe.
 */
export class ClaudeMCP implements vscode.Disposable {
  private _server?: any; // HTTP server for IPC
  private _onEvent = new vscode.EventEmitter<{ type: string; payload: unknown }>();
  public readonly onEvent = this._onEvent.event;

  /**
   * Start a local HTTP server for MCP -> Extension communication.
   * The MCP server POSTs events to this endpoint.
   */
  public async start(port = 0): Promise<number> {
    const http = await import('http');

    return new Promise((resolve) => {
      this._server = http.createServer((req, res) => {
        if (req.method !== 'POST') {
          res.writeHead(405);
          res.end();
          return;
        }

        let body = '';
        req.on('data', (chunk: string) => { body += chunk; });
        req.on('end', () => {
          try {
            const event = JSON.parse(body);
            this._onEvent.fire(event);
            res.writeHead(200);
            res.end('OK');
          } catch {
            res.writeHead(400);
            res.end('Invalid JSON');
          }
        });
      });

      this._server.listen(port, '127.0.0.1', () => {
        const addr = this._server.address();
        const assignedPort = typeof addr === 'object' ? addr.port : port;
        resolve(assignedPort);
      });
    });
  }

  public dispose(): void {
    this._server?.close();
    this._onEvent.dispose();
  }
}
```

---

## SecretStorage pour les tokens {#secret-storage}

```typescript
// src/utils/secrets.ts
import * as vscode from 'vscode';

const SECRET_KEY_API = 'agentVisual.apiKey';
const SECRET_KEY_MCP_TOKEN = 'agentVisual.mcpToken';

/**
 * Store and retrieve secrets securely.
 * NEVER store API keys in settings.json or globalState.
 */
export class SecretManager {
  constructor(private readonly _secretStorage: vscode.SecretStorage) {}

  async getApiKey(): Promise<string | undefined> {
    return this._secretStorage.get(SECRET_KEY_API);
  }

  async setApiKey(key: string): Promise<void> {
    await this._secretStorage.store(SECRET_KEY_API, key);
  }

  async deleteApiKey(): Promise<void> {
    await this._secretStorage.delete(SECRET_KEY_API);
  }

  async getMcpToken(): Promise<string | undefined> {
    return this._secretStorage.get(SECRET_KEY_MCP_TOKEN);
  }

  async setMcpToken(token: string): Promise<void> {
    await this._secretStorage.store(SECRET_KEY_MCP_TOKEN, token);
  }
}

// Usage in extension.ts:
// const secrets = new SecretManager(context.secrets);
// const key = await secrets.getApiKey();
```

---

## Choix et migration entre variantes {#migration}

### Matrice de decision

| Critere | CLI (A) | Hooks (B) | MCP (C) |
|---------|---------|-----------|---------|
| Complexite setup | 5 min | 30 min | 2-4h |
| Reactivite | Request/response | Evenementiel | Bidirectionnel |
| Streaming | Oui (--stream) | Non natif | Oui (SSE) |
| Cross-platform | Oui | Oui | Oui |
| Offline | Non (API) | Depand | Depand |
| Maintenance | Faible | Moyenne | Elevee |

### Strategie de migration recommandee

```
Phase 1 (prototype) : CLI seul
  -> Valider le concept de chat + avatar
  -> 1-2 jours

Phase 2 (reactivite) : CLI + Hooks
  -> L'avatar reagit aux actions de Claude Code
  -> Le chat reste en CLI
  -> +1 jour

Phase 3 (production) : CLI + Hooks + MCP (optionnel)
  -> MCP pour outils bidirectionnels
  -> Si tu veux que Claude Code puisse piloter l'avatar directement
  -> +2-4 jours
```

Les 3 variantes ne sont pas mutuellement exclusives. Le `AgentStateManager` abstrait
le bridge — on peut utiliser CLI pour le chat et Hooks pour les animations simultanement.

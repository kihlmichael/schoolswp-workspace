#!/usr/bin/env node
/**
 * Launcher pour le MCP n8n-mcp.
 *
 * Pourquoi ce launcher : `N8N_API_KEY` etait hardcode en clair dans le bloc
 * env de .mcp.json (drift detecte 2026-05-13). Claude Code lit `.mcp.json`
 * et expose toute valeur litterale dans `claude mcp list` -> transcript JSONL.
 *
 * Le launcher lit N8N_API_KEY depuis .claude/settings.local.json (gitignored),
 * spawn `npx -y n8n-mcp` avec l'env injecte sur le process enfant -- hors-vue
 * de Claude Code.
 *
 * Usage : node _launch-n8n.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};
const apiKey = settings.N8N_API_KEY;
if (!apiKey) {
  console.error('N8N_API_KEY not found in .claude/settings.local.json');
  process.exit(2);
}

// Windows : depuis Node 20.12+ (CVE-2024-27980), spawn direct d'un .cmd
// (npx.cmd) leve EINVAL. On passe par `cmd.exe /c npx`.
const isWin = process.platform === 'win32';
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', '-y', 'n8n-mcp'] : ['-y', 'n8n-mcp'],
  {
    stdio: 'inherit',
    env: {
      ...process.env,
      MCP_MODE: 'stdio',
      LOG_LEVEL: 'error',
      DISABLE_CONSOLE_OUTPUT: 'true',
      N8N_API_URL: settings.N8N_API_URL || 'https://schoolswp-n8n.wp1.host',
      N8N_API_KEY: apiKey,
    },
  }
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Launcher failed to spawn n8n-mcp:', err);
  process.exit(1);
});

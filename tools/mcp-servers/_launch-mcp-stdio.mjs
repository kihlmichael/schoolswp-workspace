#!/usr/bin/env node
/**
 * Launcher generique pour les MCP stdio avec secrets en env block.
 *
 * Pourquoi : empeche les secrets d'apparaitre dans .mcp.json (en clair ou
 * via substitution ${VAR}), donc d'etre exposes par `claude mcp list` dans
 * les transcripts JSONL. Le launcher lit chaque variable nommee depuis
 * .claude/settings.local.json (gitignored) et spawn `npx -y <pkg>` avec
 * l'env injecte sur le child process -- hors-vue de Claude Code.
 *
 * Usage : node _launch-mcp-stdio.mjs <npm-package> <ENV_VAR_1> [<ENV_VAR_2> ...]
 *
 * Exemples :
 *   node _launch-mcp-stdio.mjs firecrawl-mcp FIRECRAWL_API_KEY
 *   node _launch-mcp-stdio.mjs @automattic/mcp-wordpress-remote@latest WP_API_URL WP_API_USERNAME WP_API_PASSWORD
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const [, , pkg, ...envVars] = process.argv;

if (!pkg || envVars.length === 0) {
  console.error('Usage: node _launch-mcp-stdio.mjs <npm-package> <ENV_VAR_1> [<ENV_VAR_2> ...]');
  process.exit(2);
}

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};

const childEnv = { ...process.env };
for (const name of envVars) {
  const value = settings[name];
  if (!value) {
    console.error(`${name} not found in .claude/settings.local.json`);
    process.exit(2);
  }
  childEnv[name] = value;
}

// Windows : depuis Node 20.12+ (CVE-2024-27980), spawn direct d'un .cmd
// (npx.cmd) leve EINVAL. On passe par `cmd.exe /c npx` -- Node applique
// l'echappement cmd-aware des args (metacaracteres |, &, > preserves),
// sans le risque d'injection de `shell: true`.
const isWin = process.platform === 'win32';
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', '-y', pkg] : ['-y', pkg],
  { stdio: 'inherit', env: childEnv }
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Launcher failed to spawn:', err);
  process.exit(1);
});

#!/usr/bin/env node
/**
 * Launcher pour mcp-discord (bot schoolsWP Orchestrator).
 *
 * Pourquoi ce launcher : Claude Code substitue ${DISCORD_BOT_TOKEN} dans args
 * de .mcp.json à la lecture, ce qui fait fuiter le token à chaque `claude mcp
 * list` (incident 2026-04-29). Le launcher lit le token depuis
 * settings.local.json et spawn mcp-discord avec --config TOKEN — hors-vue.
 *
 * Usage : node _launch-discord.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};
const token = settings.DISCORD_BOT_TOKEN;
if (!token) {
  console.error('DISCORD_BOT_TOKEN not found in .claude/settings.local.json');
  process.exit(2);
}

// Windows : depuis Node 20.12+ (CVE-2024-27980), spawn direct d'un .cmd
// (npx.cmd) leve EINVAL. On passe par `cmd.exe /c npx` -- Node applique
// l'echappement cmd-aware des args (le token peut contenir des metacaracteres).
const isWin = process.platform === 'win32';
const npxArgs = ['-y', 'mcp-discord@1.3.4', '--config', token];
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', ...npxArgs] : npxArgs,
  {
    stdio: 'inherit',
    env: { ...process.env, DISCORD_BOT_TOKEN: token },
  }
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Launcher failed to spawn mcp-discord:', err);
  process.exit(1);
});

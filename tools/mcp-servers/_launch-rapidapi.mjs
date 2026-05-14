#!/usr/bin/env node
/**
 * Launcher pour les 4 MCP RapidAPI (LinkedIn / Twitter / Instagram / YouTube).
 *
 * Pourquoi ce launcher : Claude Code substitue ${VAR} dans le bloc args de
 * .mcp.json en lisant settings.local.json, ce qui fait apparaître la clé en
 * clair à chaque `claude mcp list` (incident sécurité 2026-04-21 et 2026-04-29).
 * Le launcher lit RAPIDAPI_KEY depuis settings.local.json et spawn `mcp-remote`
 * avec la clé en arg — hors-vue de Claude Code.
 *
 * Usage : node _launch-rapidapi.mjs <target>
 *   target : linkedin | twitter | instagram | youtube
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const HOSTS = {
  linkedin: 'linkedin-api8.p.rapidapi.com',
  twitter: 'twitter154.p.rapidapi.com',
  instagram: 'instagram120.p.rapidapi.com',
  youtube: 'youtube138.p.rapidapi.com',
};

const [, , target] = process.argv;
const host = HOSTS[target];
if (!host) {
  console.error(`Usage: node _launch-rapidapi.mjs <target>\n  target: ${Object.keys(HOSTS).join(' | ')}`);
  process.exit(2);
}

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};
const key = settings.RAPIDAPI_KEY;
if (!key) {
  console.error('RAPIDAPI_KEY not found in .claude/settings.local.json');
  process.exit(2);
}

// Windows : depuis Node 20.12+ (CVE-2024-27980), spawn direct d'un .cmd
// (npx.cmd) leve EINVAL. On passe par `cmd.exe /c npx` -- Node applique
// l'echappement cmd-aware des args (la cle peut contenir |, &, etc.).
const isWin = process.platform === 'win32';
const npxArgs = [
  '-y',
  'mcp-remote',
  'https://mcp.rapidapi.com',
  '--header',
  `x-api-host:${host}`,
  '--header',
  `x-api-key:${key}`,
];
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', ...npxArgs] : npxArgs,
  { stdio: 'inherit' }
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Launcher failed to spawn mcp-remote:', err);
  process.exit(1);
});

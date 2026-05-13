#!/usr/bin/env node
/**
 * Launcher pour le MCP ZipWP (mcp-remote).
 *
 * Pourquoi ce launcher : Claude Code substitue ${VAR} dans le bloc args de
 * .mcp.json en lisant settings.local.json, ce qui fait apparaître la clé en
 * clair à chaque `claude mcp list` (incident sécurité 2026-04-21 et 2026-04-29).
 * Le launcher lit ZIPWP_TOKEN depuis settings.local.json et spawn `mcp-remote`
 * avec le header injecté en arg — hors-vue de Claude Code.
 *
 * Usage : node _launch-zipwp.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};
const token = settings.ZIPWP_TOKEN;
if (!token) {
  console.error('ZIPWP_TOKEN not found in .claude/settings.local.json');
  process.exit(2);
}

const child = spawn(
  process.platform === 'win32' ? 'npx.cmd' : 'npx',
  [
    '-y',
    'mcp-remote',
    'https://api.zipwp.com/mcp/zipwp',
    '--header',
    `Authorization:Bearer ${token}`,
  ],
  { stdio: 'inherit' }
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Launcher failed to spawn mcp-remote:', err);
  process.exit(1);
});

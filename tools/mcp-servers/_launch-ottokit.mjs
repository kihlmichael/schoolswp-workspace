#!/usr/bin/env node
/**
 * Launcher OttoKit MCP (HTTP remote via mcp-remote).
 *
 * Pourquoi cette plomberie : l'URL serveur OttoKit embarque le token secret
 * directement dans le path (https://api.ottokit.com/mcp/MCP<token>). La poser
 * en clair dans .mcp.json la ferait fuiter a chaque `claude mcp list` dans les
 * transcripts JSONL (incidents securite 2026-04-21 / 2026-04-29). Le launcher
 * lit OTTOKIT_MCP_URL depuis settings.local.json (gitignored) et spawn
 * mcp-remote avec l'URL passee en arg -- hors-vue de Claude Code.
 *
 * mcp-remote logue l'URL de connexion (donc le token) sur stderr au demarrage.
 * On redirige son stderr vers logs/mcp-ottokit.log (gitignored) au lieu de
 * l'heriter du parent, sinon le token fuite dans les transcripts Claude Code.
 *
 * Setup cote OttoKit (1x) : login -> sidebar MCP -> Create MCP Server ->
 * Manage Tools (ajouter les app-actions voulues) -> copier la Server URL ->
 * la coller dans settings.local.json sous "OTTOKIT_MCP_URL".
 *
 * Usage : node _launch-ottokit.mjs  (lance par Claude Code via .mcp.json)
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');

const settingsPath = path.join(ROOT, '.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};
const url = settings.OTTOKIT_MCP_URL;
if (!url) {
  console.error('OTTOKIT_MCP_URL not found in .claude/settings.local.json');
  process.exit(2);
}

// stderr de mcp-remote logue l'URL (avec le token) en clair au demarrage.
// On le route vers un fichier gitignored au lieu de l'heriter du parent.
const logDir = path.join(ROOT, 'logs');
fs.mkdirSync(logDir, { recursive: true });
const stderrLog = fs.openSync(path.join(logDir, 'mcp-ottokit.log'), 'a');

// Windows : depuis Node 20.12+ (CVE-2024-27980), spawn direct d'un .cmd
// (npx.cmd) leve EINVAL. On passe par `cmd.exe /c npx`.
const isWin = process.platform === 'win32';
const npxArgs = ['-y', 'mcp-remote', url];
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', ...npxArgs] : npxArgs,
  { stdio: ['inherit', 'inherit', stderrLog] },
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('OttoKit launcher failed to spawn mcp-remote:', err);
  process.exit(1);
});

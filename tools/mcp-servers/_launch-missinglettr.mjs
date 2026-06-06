#!/usr/bin/env node
/**
 * Launcher Missinglettr MCP (HTTP remote, Bearer OAuth 2.1).
 *
 * Pourquoi cette plomberie : Missinglettr expose un MCP HTTP qui exige un
 * Bearer OAuth issu de leur flow (DCR + PKCE), mais son serveur retourne
 * HTTP 200 + JSON-RPC error sur les appels non-authentifies au lieu d'un
 * HTTP 401 propre. mcp-remote ne declenche donc jamais son OAuth automatique.
 *
 * Architecture :
 *  1. `missinglettr-oauth-setup.mjs` (a lancer 1x) -> DCR + browser + tokens
 *     caches dans `.credentials/missinglettr-oauth.json` (gitignored, 0o600).
 *  2. Ce launcher lit le cache au demarrage. Si l'access_token est expire
 *     (ou expire dans <120s), il appelle /token grant_type=refresh_token
 *     pour le renouveler avant de lancer mcp-remote.
 *  3. mcp-remote est invoque avec `--header "Authorization:Bearer <token>"`,
 *     stderr redirige vers logs/mcp-missinglettr.log (gitignored) pour
 *     eviter la fuite du token dans les transcripts Claude Code.
 *
 * Usage : node _launch-missinglettr.mjs
 *         (lance par Claude Code via .mcp.json)
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');
const MCP_URL = 'https://mcp.missinglettr-api.com';
const CRED_FILE = path.join(ROOT, '.credentials/missinglettr-oauth.json');
const REFRESH_BUFFER_MS = 120 * 1000;

function die(msg) {
  console.error(`[missinglettr-launcher] ${msg}`);
  process.exit(2);
}

if (!fs.existsSync(CRED_FILE)) {
  die(
    `OAuth tokens missing at ${path.relative(ROOT, CRED_FILE)}\n` +
      `  Run once: node tools/mcp-servers/missinglettr-oauth-setup.mjs`,
  );
}

let creds;
try {
  creds = JSON.parse(fs.readFileSync(CRED_FILE, 'utf8'));
} catch (e) {
  die(`Failed to parse ${path.relative(ROOT, CRED_FILE)}: ${e.message}`);
}

async function refreshIfNeeded() {
  if (creds.expires_at && creds.expires_at - Date.now() > REFRESH_BUFFER_MS) {
    return;
  }
  if (!creds.refresh_token || !creds.client_id) {
    die(
      `Access token expired and no refresh_token in cache.\n` +
        `  Re-run: node tools/mcp-servers/missinglettr-oauth-setup.mjs`,
    );
  }
  const resp = await fetch(`${creds.issuer || MCP_URL}/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'refresh_token',
      refresh_token: creds.refresh_token,
      client_id: creds.client_id,
    }).toString(),
  });
  if (!resp.ok) {
    const body = await resp.text();
    die(
      `Refresh failed: ${resp.status} — ${body.slice(0, 200)}\n` +
        `  Re-run: node tools/mcp-servers/missinglettr-oauth-setup.mjs`,
    );
  }
  const t = await resp.json();
  creds.access_token = t.access_token;
  if (t.refresh_token) creds.refresh_token = t.refresh_token;
  creds.expires_at = Date.now() + ((t.expires_in || 3600) - 60) * 1000;
  creds.saved_at = new Date().toISOString();
  fs.writeFileSync(CRED_FILE, JSON.stringify(creds, null, 2), { mode: 0o600 });
}

await refreshIfNeeded();

const headerArg = `Authorization:Bearer ${creds.access_token}`;

// stderr de mcp-remote logue le header en clair au demarrage.
// On le route vers un fichier gitignored au lieu de l'heriter du parent
// (sinon fuite dans les transcripts JSONL de Claude Code).
const logDir = path.join(ROOT, 'logs');
fs.mkdirSync(logDir, { recursive: true });
const stderrLog = fs.openSync(path.join(logDir, 'mcp-missinglettr.log'), 'a');

const isWin = process.platform === 'win32';
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin
    ? ['/c', 'npx', '-y', 'mcp-remote@latest', MCP_URL, '--header', headerArg]
    : ['-y', 'mcp-remote@latest', MCP_URL, '--header', headerArg],
  { stdio: ['inherit', 'inherit', stderrLog] },
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error('Missinglettr launcher failed to spawn:', err);
  process.exit(1);
});

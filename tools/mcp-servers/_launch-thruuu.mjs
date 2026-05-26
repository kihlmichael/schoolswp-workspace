#!/usr/bin/env node
/**
 * Launcher MCP server thruuu - schoolsWP
 *
 * Pourquoi : Claude Code ne resout pas la syntaxe ${VAR} dans le bloc env de
 * .mcp.json (cf. feedback_mcp_var_substitution.md). Ce launcher lit
 * THRUUU_API_KEY depuis le .env racine du projet, l'injecte dans process.env,
 * puis spawn `uv run --with fastmcp --with httpx fastmcp run server.py`.
 *
 * Pattern aligne sur _launch-dataforseo.mjs (autre MCP a secret cle dans .env).
 */
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseEnvFile(filePath) {
  const out = {};
  if (!fs.existsSync(filePath)) return out;
  const content = fs.readFileSync(filePath, 'utf8');
  for (const rawLine of content.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const m = line.match(/^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$/);
    if (!m) continue;
    let value = m[2];
    const hashIdx = value.indexOf(' #');
    if (hashIdx >= 0 && !value.startsWith('"') && !value.startsWith("'")) {
      value = value.slice(0, hashIdx);
    }
    value = value.trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    out[m[1]] = value;
  }
  return out;
}

const projectRoot = path.resolve(__dirname, '../..');
const envPath = path.join(projectRoot, '.env');
const envFile = parseEnvFile(envPath);
const apiKey = envFile.THRUUU_API_KEY || process.env.THRUUU_API_KEY;

if (!apiKey) {
  console.error(
    `[thruuu-launcher] THRUUU_API_KEY absent.\n` +
      `Cherche dans : ${envPath}\n` +
      `Ajouter THRUUU_API_KEY=... dans le .env racine du projet schoolsWP.`,
  );
  process.exit(2);
}

const serverScript = path.join(projectRoot, 'tools', 'mcp-servers', 'thruuu', 'server.py');
if (!fs.existsSync(serverScript)) {
  console.error(`[thruuu-launcher] server.py introuvable : ${serverScript}`);
  process.exit(2);
}

const child = spawn(
  'uv',
  ['run', '--with', 'fastmcp', '--with', 'httpx', '--with', 'python-dotenv', 'fastmcp', 'run', serverScript],
  {
    cwd: projectRoot,
    env: { ...process.env, THRUUU_API_KEY: apiKey },
    stdio: 'inherit',
    shell: process.platform === 'win32',
  },
);

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error(`[thruuu-launcher] spawn error: ${err.message}`);
  process.exit(2);
});

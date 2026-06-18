#!/usr/bin/env node
/**
 * Launcher MCP server thruuu - schoolsWP
 *
 * Pourquoi : Claude Code ne resout pas la syntaxe ${VAR} dans le bloc env de
 * .mcp.json (cf. feedback_mcp_var_substitution.md). Ce launcher lit
 * THRUUU_API_KEY depuis le .env racine du projet, l'injecte dans process.env,
 * puis spawn le serveur FastMCP via le venv Python projet (.venv/Scripts/python.exe).
 *
 * Historique : version initiale utilisait `uv run --with fastmcp` mais Windows
 * Smart App Control / WDAC bloquait le binaire fastmcp.exe telecharge par uv
 * (os error 4551). Solution : pre-install fastmcp dans le venv projet (binaire
 * trusted) et call direct python server.py (sans wrapper fastmcp CLI).
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

const venvPython = path.join(projectRoot, '.venv', 'Scripts', 'python.exe');
if (!fs.existsSync(venvPython)) {
  console.error(`[thruuu-launcher] venv Python introuvable : ${venvPython}`);
  console.error('Lancer : pip install uv && uv sync depuis projects/schoolswp/');
  process.exit(2);
}

const serverScript = path.join(projectRoot, 'tools', 'mcp-servers', 'thruuu', 'server.py');
if (!fs.existsSync(serverScript)) {
  console.error(`[thruuu-launcher] server.py introuvable : ${serverScript}`);
  process.exit(2);
}

const child = spawn(venvPython, [serverScript], {
  cwd: projectRoot,
  env: { ...process.env, THRUUU_API_KEY: apiKey, PYTHONUNBUFFERED: '1' },
  stdio: 'inherit',
});

child.on('exit', (code) => process.exit(code ?? 0));
child.on('error', (err) => {
  console.error(`[thruuu-launcher] spawn error: ${err.message}`);
  process.exit(2);
});

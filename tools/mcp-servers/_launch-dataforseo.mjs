#!/usr/bin/env node
/**
 * Launcher dataforseo-mcp-server (global npm install).
 *
 * Pourquoi : Claude Code ne résout pas la syntaxe ${VAR} dans le bloc env de
 * .mcp.json (test 2026-04-29 — voir feedback_mcp_var_substitution.md).
 * Ce launcher lit DATAFORSEO_USERNAME/PASSWORD depuis le .env racine du projet
 * schoolsWP (gitignored), set process.env, puis import() dynamiquement le cli
 * ESM du serveur.
 *
 * Pattern in-process aligné sur _launch-fluent.mjs (préserve le pipe
 * STDIN/STDOUT JSON-RPC attendu par Claude Code MCP).
 *
 * Note : la convention secrets MCP du projet est settings.local.json, mais
 * DataForSEO vit historiquement dans .env (cf. variables Python qui consomment
 * aussi DATAFORSEO_USERNAME/PASSWORD côté agents).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

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

const envPath = path.resolve(__dirname, '../../.env');
const envFile = parseEnvFile(envPath);

const username = envFile.DATAFORSEO_USERNAME || process.env.DATAFORSEO_USERNAME;
const password = envFile.DATAFORSEO_PASSWORD || process.env.DATAFORSEO_PASSWORD;

if (!username || !password) {
  console.error(
    `[dataforseo-launcher] DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD absents.\n` +
      `Cherché dans : ${envPath}\n` +
      `Ajouter les deux variables dans le .env racine du projet schoolsWP.`,
  );
  process.exit(2);
}

process.env.DATAFORSEO_USERNAME = username;
process.env.DATAFORSEO_PASSWORD = password;

const npmGlobalRoot = path.join(process.env.APPDATA || '', 'npm', 'node_modules');
const serverEntry = path.join(
  npmGlobalRoot,
  'dataforseo-mcp-server',
  'build',
  'main',
  'main',
  'cli.js',
);

if (!fs.existsSync(serverEntry)) {
  console.error(`[dataforseo-launcher] Binary introuvable : ${serverEntry}`);
  console.error('Réinstaller : npm install -g dataforseo-mcp-server');
  process.exit(2);
}

process.argv = [process.argv[0], serverEntry, ...process.argv.slice(2)];
await import(pathToFileURL(serverEntry).href);

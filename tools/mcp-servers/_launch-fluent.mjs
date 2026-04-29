#!/usr/bin/env node
/**
 * Launcher générique pour les 5 Fluent MCP servers (Carlos Rodera).
 *
 * Pourquoi ce launcher : Claude Code ne résout pas la syntaxe ${VAR} dans le
 * bloc env de .mcp.json (test 2026-04-29 — voir feedback_mcp_var_substitution.md).
 * Ce launcher lit les credentials depuis .claude/settings.local.json (gitignored),
 * set process.env, puis import() dynamiquement le main du serveur (ESM, top-level
 * await — require() échoue avec ERR_REQUIRE_ASYNC_MODULE).
 *
 * Emplacement : versionné dans tools/mcp-servers/ (parent du clone upstream qui
 * est gitignored). Survit à un re-clone du repo upstream.
 *
 * Usage : node _launch-fluent.mjs <PREFIX> <server-dirname> [--mode dynamic]
 *   PREFIX        : FLUENTCRM | FLUENTSUPPORT | FLUENTBOARDS | FLUENTCOMMUNITY | FLUENTAFFILIATE
 *   server-dirname: fluent-crm-mcp | fluent-support-mcp | fluent-boards-mcp | fluent-community-mcp | fluent-affiliate-mcp
 *
 * Référence pour réutilisation avec d'autres MCP servers WP REST natifs :
 * adapter les noms d'env vars (LOOKUP source dans settings.local.json + TARGET
 * names attendues par le serveur cible).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const [, , prefix, serverDir, ...rest] = process.argv;

if (!prefix || !serverDir) {
  console.error('Usage: node _launch-fluent.mjs <PREFIX> <server-dirname> [--mode dynamic]');
  process.exit(2);
}

const settingsPath = path.resolve(__dirname, '../../.claude/settings.local.json');
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};

process.env[`${prefix}_URL`] = 'https://schoolswp.com';
process.env[`${prefix}_USERNAME`] = settings.FLUENTCRM_API_USERNAME;
process.env[`${prefix}_APP_PASSWORD`] = settings.FLUENTCRM_API_PASSWORD;

const serverEntry = path.join(__dirname, 'fluent-mcp-servers', serverDir, 'dist', 'index.js');
process.argv = [process.argv[0], serverEntry, ...rest];

await import(pathToFileURL(serverEntry).href);

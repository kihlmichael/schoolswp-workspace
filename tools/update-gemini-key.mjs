#!/usr/bin/env node
/**
 * Patche .claude/settings.local.json en remplacant la cle GEMINI_API_KEY
 * sans afficher la valeur courante dans le terminal.
 *
 * Usage:
 *   node tools/update-gemini-key.mjs <NEW_KEY>
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const settingsPath = path.resolve(__dirname, '..', '.claude', 'settings.local.json');

const newKey = process.argv[2];
if (!newKey || newKey.length < 20) {
  console.error('Usage: node tools/update-gemini-key.mjs <NEW_KEY>');
  console.error('Cle trop courte ou manquante.');
  process.exit(1);
}

const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));
if (!settings.env) settings.env = {};
const oldLen = (settings.env.GEMINI_API_KEY || '').length;
settings.env.GEMINI_API_KEY = newKey;

fs.writeFileSync(settingsPath, JSON.stringify(settings, null, 2) + '\n', 'utf-8');
console.log(`OK : GEMINI_API_KEY remplacee (${oldLen} -> ${newKey.length} chars).`);
console.log('Test : .venv/Scripts/python tools/generate-hero-fluentcrm.py');

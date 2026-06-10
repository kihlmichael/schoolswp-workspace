#!/usr/bin/env node
/**
 * Patch idempotent du modele Gemini du MCP `nano-banana-mcp`.
 *
 * Pourquoi : nano-banana-mcp@1.0.3 (derniere version publiee, upstream abandonne)
 * hardcode `gemini-2.5-flash-image-preview` dans dist/index.js. Ce modele a ete
 * retire de l'API v1beta -> tous les appels edit_image / generate_image renvoient
 * un 404 NOT_FOUND. Le package n'expose aucune surcharge par env ni par config,
 * donc la seule correction est de remplacer la chaine du modele.
 *
 * Le binaire reel vit dans le cache npx (volatile : un `npm cache clean` le reset).
 * Ce script reapplique le patch a la demande, sur toutes les copies trouvees, et
 * centralise le modele cible (modifiable via NANO_BANANA_MODEL). C'est l'inverse
 * d'un hardcoding disperse : un seul endroit, re-executable.
 *
 * Usage :
 *   node tools/mcp-servers/patch-nano-banana-model.mjs            # modele par defaut
 *   NANO_BANANA_MODEL=gemini-3-pro-image node tools/...           # autre modele
 *
 * Apres patch : recharger le MCP nano-banana (le process en cours garde l'ancien
 * code en memoire) via `/mcp` -> reconnecter, ou redemarrer Claude Code.
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const RETIRED_MODEL = 'gemini-2.5-flash-image-preview';
const TARGET_MODEL = process.env.NANO_BANANA_MODEL || 'gemini-2.5-flash-image';

if (TARGET_MODEL === RETIRED_MODEL) {
  console.error(`TARGET_MODEL is the retired model itself (${RETIRED_MODEL}). Aborting.`);
  process.exit(2);
}

const REL = path.join('node_modules', 'nano-banana-mcp', 'dist', 'index.js');

// Emplacements candidats du binaire nano-banana-mcp.
function candidatePaths() {
  const found = new Set();
  const localAppData = process.env.LOCALAPPDATA || path.join(os.homedir(), 'AppData', 'Local');
  const npxRoot = path.join(localAppData, 'npm-cache', '_npx');
  // Cache npx : un sous-dossier hashe par spec de package.
  try {
    for (const entry of fs.readdirSync(npxRoot, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const p = path.join(npxRoot, entry.name, REL);
      if (fs.existsSync(p)) found.add(p);
    }
  } catch {
    // pas de cache npx : on ignore.
  }
  // node_modules global et local (au cas ou nano-banana-mcp y serait installe).
  const globalRoot = process.env.APPDATA ? path.join(process.env.APPDATA, 'npm', 'node_modules') : null;
  for (const base of [globalRoot, path.resolve('node_modules')]) {
    if (!base) continue;
    const p = path.join(base, 'nano-banana-mcp', 'dist', 'index.js');
    if (fs.existsSync(p)) found.add(p);
  }
  return [...found];
}

const targets = candidatePaths();
if (targets.length === 0) {
  console.error('Aucune copie de nano-banana-mcp/dist/index.js trouvee (cache npx vide ?).');
  console.error('Lance le MCP une fois (pour peupler le cache npx), puis relance ce script.');
  process.exit(1);
}

let totalReplacements = 0;
let filesChanged = 0;
for (const file of targets) {
  const src = fs.readFileSync(file, 'utf8');
  const occurrences = src.split(RETIRED_MODEL).length - 1;
  if (occurrences === 0) {
    console.log(`[deja a jour] ${file} (aucune occurrence de "${RETIRED_MODEL}")`);
    continue;
  }
  const patched = src.split(RETIRED_MODEL).join(TARGET_MODEL);
  fs.writeFileSync(file, patched, 'utf8');
  totalReplacements += occurrences;
  filesChanged += 1;
  console.log(`[patche]      ${file} -> ${occurrences} occurrence(s) "${RETIRED_MODEL}" => "${TARGET_MODEL}"`);
}

console.log('');
console.log(`Modele cible : ${TARGET_MODEL}`);
console.log(`Fichiers modifies : ${filesChanged} | remplacements : ${totalReplacements}`);
if (filesChanged > 0) {
  console.log('Recharge le MCP nano-banana (/mcp -> reconnecter, ou redemarrer Claude Code) pour prise en compte.');
}

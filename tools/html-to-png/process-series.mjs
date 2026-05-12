#!/usr/bin/env node
/**
 * process-series.mjs - orchestrator pour un dossier social-series complet
 *
 * Pour chaque sous-dossier de format détecté dans <series>/, exécute :
 * 1. capture.mjs avec les bonnes dimensions selon le format
 * 2. inject-meta.mjs si seo-meta.yaml présent
 * 3. export-pdf.mjs pour les formats carrousel LinkedIn
 *
 * Format detection auto par nom de dossier :
 *   instagram-feed       -> 1080x1350 (4:5)
 *   instagram-square     -> skip (pointer LinkedIn, pas de slides)
 *   instagram-stories    -> 1080x1920 (9:16) + pattern story-
 *   linkedin-carousel    -> 1080x1080 (1:1) + export-pdf
 *   pinterest-pins       -> 1000x1500 (2:3) + pattern pin-
 *   twitter-card         -> 1600x900 (16:9)
 *   youtube-thumbnail    -> 1280x720 (16:9)
 *   tiktok-cover         -> 1080x1920 (9:16)
 *
 * Usage:
 *   node process-series.mjs content/social-series/<series>
 */

import { readdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, resolve, basename, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));

const FORMAT_PROFILES = {
  'instagram-feed':     { width: 1080, height: 1350, pattern: 'slide-' },
  'instagram-square':   { skip: true, reason: 'pointer LinkedIn (no slides)' },
  'instagram-stories':  { width: 1080, height: 1920, pattern: 'story-' },
  'linkedin-carousel':  { width: 1080, height: 1080, pattern: 'slide-', exportPdf: true },
  'pinterest-pins':     { width: 1000, height: 1500, pattern: 'pin-' },
  'twitter-card':       { width: 1600, height: 900,  pattern: 'slide-' },
  'youtube-thumbnail':  { width: 1280, height: 720,  pattern: 'slide-' },
  'tiktok-cover':       { width: 1080, height: 1920, pattern: 'slide-' },
};

function parseArgs(argv) {
  const args = { positional: [] };
  for (const arg of argv) {
    if (arg.startsWith('--')) {
      const [key, value] = arg.slice(2).split('=');
      args[key] = value === undefined ? true : value;
    } else {
      args.positional.push(arg);
    }
  }
  return args;
}

function runScript(scriptName, scriptArgs) {
  return new Promise((resolveProm, rejectProm) => {
    const scriptPath = join(__dirname, scriptName);
    const proc = spawn('node', [scriptPath, ...scriptArgs], { stdio: 'inherit' });
    proc.on('close', (code) => {
      if (code === 0) resolveProm();
      else rejectProm(new Error(`${scriptName} exited with code ${code}`));
    });
    proc.on('error', rejectProm);
  });
}

const args = parseArgs(process.argv.slice(2));
const seriesPath = args.positional[0];

if (!seriesPath || args.help) {
  console.log(`
process-series.mjs - orchestrator complet pour un dossier social-series

Usage:
  node process-series.mjs <series-directory>

Exemple:
  node process-series.mjs content/social-series/fluentcart-gratuit-vs-pro

Pour chaque format détecté, exécute capture + inject-meta + export-pdf (LinkedIn).
`);
  process.exit(args.help ? 0 : 1);
}

const series = resolve(seriesPath);
if (!existsSync(series)) {
  console.error(`Series directory not found: ${series}`);
  process.exit(1);
}

const seriesName = basename(series);
console.log(`\n🚀 Processing series: ${seriesName}\n`);

const entries = await readdir(series);
const formats = [];

for (const entry of entries) {
  const entryPath = join(series, entry);
  const stats = await stat(entryPath);
  if (!stats.isDirectory()) continue;
  if (entry.startsWith('_')) continue;
  if (!FORMAT_PROFILES[entry]) {
    console.log(`   ⊘  ${entry} - unknown format, skip`);
    continue;
  }
  formats.push(entry);
}

console.log(`Detected formats: ${formats.join(', ')}\n`);

let successCount = 0;
let totalSteps = 0;

for (const format of formats) {
  const profile = FORMAT_PROFILES[format];
  const formatPath = join(series, format);

  console.log(`\n━━━ ${format} ━━━`);

  if (profile.skip) {
    console.log(`   ⊘  ${profile.reason}`);
    continue;
  }

  // 1. Capture
  totalSteps++;
  try {
    await runScript('capture.mjs', [
      formatPath,
      `--width=${profile.width}`,
      `--height=${profile.height}`,
      `--pattern=${profile.pattern}`,
    ]);
    successCount++;
  } catch (err) {
    console.error(`   ✗ capture failed: ${err.message}`);
    continue;
  }

  // 2. Inject metadata if seo-meta.yaml exists
  const metaPath = join(formatPath, 'seo-meta.yaml');
  if (existsSync(metaPath)) {
    totalSteps++;
    try {
      await runScript('inject-meta.mjs', [formatPath]);
      successCount++;
    } catch (err) {
      console.error(`   ✗ inject-meta failed: ${err.message}`);
    }
  } else {
    console.log(`   ⊘  no seo-meta.yaml, skip metadata injection`);
  }

  // 3. Export PDF (LinkedIn carrousel only)
  if (profile.exportPdf) {
    totalSteps++;
    const pdfName = `carrousel-${format}-${seriesName}.pdf`;
    try {
      await runScript('export-pdf.mjs', [
        formatPath,
        `--width=${profile.width}`,
        `--height=${profile.height}`,
        `--pattern=${profile.pattern}`,
        `--output=${pdfName}`,
      ]);
      successCount++;
    } catch (err) {
      console.error(`   ✗ export-pdf failed: ${err.message}`);
    }
  }
}

console.log(`\n✅ Series complete: ${successCount}/${totalSteps} steps OK\n`);

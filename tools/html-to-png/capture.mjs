#!/usr/bin/env node
/**
 * capture.mjs -convert slide-*.html files to PNG
 *
 * Default output: 1080x1350 (Instagram feed 4:5)
 *
 * Usage:
 *   node capture.mjs <directory>                     # Defaults: 1080x1350, deviceScaleFactor=2
 *   node capture.mjs <directory> --width=1080 --height=1080   # Square Instagram
 *   node capture.mjs <directory> --selector=.slide   # Custom element selector (default .slide)
 *   node capture.mjs <directory> --pattern=slide-    # Filename prefix to capture (default slide-)
 *   node capture.mjs <directory> --scale=1           # deviceScaleFactor (default 2 for retina)
 *
 * Output: slide-XX-name.png next to each slide-XX-name.html
 */

import { chromium } from 'playwright';
import { readdir, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, resolve, basename } from 'node:path';
import { pathToFileURL } from 'node:url';

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

const args = parseArgs(process.argv.slice(2));
const targetDir = args.positional[0];

if (!targetDir || args.help) {
  console.log(`
capture.mjs -HTML slides → PNG

Usage:
  node capture.mjs <directory> [options]

Options:
  --width=<n>      Viewport width  (default: 1080)
  --height=<n>     Viewport height (default: 1350 -Instagram feed 4:5)
  --selector=<s>   CSS selector to capture (default: .slide)
  --pattern=<s>    Filename prefix to match (default: slide-)
  --scale=<n>      Device scale factor (default: 2)
  --output=<dir>   Output directory (default: same as input)

Examples:
  node capture.mjs ../content/inspirations/instagram-carrousels/5-erreurs-wp-seo
  node capture.mjs ../some-deck --width=1080 --height=1080 --scale=1
`);
  process.exit(args.help ? 0 : 1);
}

const dir = resolve(targetDir);
if (!existsSync(dir)) {
  console.error(`Directory not found: ${dir}`);
  process.exit(1);
}

const width = parseInt(args.width || '1080', 10);
const height = parseInt(args.height || '1350', 10);
const selector = args.selector || '.slide';
const pattern = args.pattern || 'slide-';
const scale = parseFloat(args.scale || '2');
const outputDir = args.output ? resolve(args.output) : dir;

if (!existsSync(outputDir)) await mkdir(outputDir, { recursive: true });

const files = (await readdir(dir))
  .filter(f => f.startsWith(pattern) && f.endsWith('.html'))
  .sort();

if (files.length === 0) {
  console.error(`No "${pattern}*.html" files in ${dir}`);
  process.exit(1);
}

console.log(`\n📸 Capturing ${files.length} slide(s)`);
console.log(`   Source : ${dir}`);
console.log(`   Output : ${outputDir}`);
console.log(`   Size   : ${width}×${height} @${scale}x\n`);

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width, height },
  deviceScaleFactor: scale,
});
const page = await context.newPage();

let successCount = 0;
const startTime = Date.now();

for (const file of files) {
  const path = join(dir, file);
  const url = pathToFileURL(path).href;
  const out = join(outputDir, file.replace(/\.html$/, '.png'));
  const label = basename(out);

  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);

    const target = await page.$(selector);
    if (target) {
      await target.screenshot({ path: out, omitBackground: false });
    } else {
      await page.screenshot({ path: out, clip: { x: 0, y: 0, width, height } });
    }
    console.log(`   ✓ ${label}`);
    successCount++;
  } catch (err) {
    console.error(`   ✗ ${label} -${err.message}`);
  }
}

await browser.close();

const duration = ((Date.now() - startTime) / 1000).toFixed(1);
console.log(`\n✅ Done -${successCount}/${files.length} slides in ${duration}s\n`);

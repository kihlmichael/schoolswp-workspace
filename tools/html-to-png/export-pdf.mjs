#!/usr/bin/env node
/**
 * export-pdf.mjs - assemble PNG slides into a single PDF
 *
 * Built for LinkedIn document carrousel (PDF upload native).
 * Assembles all `<pattern>-*.png` files in a directory into a single PDF,
 * one image per page.
 *
 * Usage:
 *   node export-pdf.mjs <directory>
 *   node export-pdf.mjs <directory> --width=1080 --height=1080
 *   node export-pdf.mjs <directory> --pattern=slide- --output=carrousel-linkedin.pdf
 *
 * Defaults: 1080x1080 page, pattern "slide-", output "carrousel.pdf" in same dir.
 */

import { PDFDocument } from 'pdf-lib';
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, resolve, basename } from 'node:path';

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
export-pdf.mjs - PNG slides -> single PDF (LinkedIn carrousel ready)

Usage:
  node export-pdf.mjs <directory> [options]

Options:
  --width=<n>      Page width in PDF points (default: 1080)
  --height=<n>     Page height in PDF points (default: 1080)
  --pattern=<s>    PNG filename prefix to match (default: slide-)
  --output=<s>     Output PDF filename (default: carrousel.pdf)

Examples:
  node export-pdf.mjs ../content/inspirations/linkedin-carrousels/5-erreurs-wp-seo
  node export-pdf.mjs ../some-deck --width=1080 --height=1350 --output=insta.pdf
`);
  process.exit(args.help ? 0 : 1);
}

const dir = resolve(targetDir);
if (!existsSync(dir)) {
  console.error(`Directory not found: ${dir}`);
  process.exit(1);
}

const width = parseInt(args.width || '1080', 10);
const height = parseInt(args.height || '1080', 10);
const pattern = args.pattern || 'slide-';
const outputName = args.output || 'carrousel.pdf';
const outputPath = join(dir, outputName);

const files = (await readdir(dir))
  .filter(f => f.startsWith(pattern) && f.endsWith('.png'))
  .sort();

if (files.length === 0) {
  console.error(`No "${pattern}*.png" files in ${dir}`);
  console.error(`Run capture.mjs first to generate the PNG slides.`);
  process.exit(1);
}

console.log(`\n📄 Assembling ${files.length} slide(s) into PDF`);
console.log(`   Source : ${dir}`);
console.log(`   Output : ${outputPath}`);
console.log(`   Page   : ${width}x${height} pt\n`);

const pdf = await PDFDocument.create();
pdf.setTitle(`Carrousel · ${basename(dir)}`);
pdf.setProducer('schoolsWP html-to-png');
pdf.setCreationDate(new Date());

const startTime = Date.now();
for (const file of files) {
  const bytes = await readFile(join(dir, file));
  const img = await pdf.embedPng(bytes);
  const page = pdf.addPage([width, height]);
  page.drawImage(img, { x: 0, y: 0, width, height });
  console.log(`   ✓ ${file}`);
}

await writeFile(outputPath, await pdf.save());

const duration = ((Date.now() - startTime) / 1000).toFixed(1);
const sizeKb = (((await readFile(outputPath)).length / 1024)).toFixed(1);
console.log(`\n✅ Done - ${files.length} pages, ${sizeKb} KB, ${duration}s`);
console.log(`   ${outputPath}\n`);

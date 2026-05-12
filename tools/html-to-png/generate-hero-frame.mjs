#!/usr/bin/env node
/**
 * Wrap l'illustration Gemini carre dans le template hero brand schoolsWP
 * et rend en 1920x1080 (16:9 ratio OG image).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, '..', '..');

const brandDir = path.join(projectRoot, 'content', 'articles', 'fluentcrm-automatisations-indispensables', 'captures-brand');
const templatePath = path.join(brandDir, '_hero-template.html');

const template = fs.readFileSync(templatePath, 'utf-8');

const heroSrcPath = path.join(brandDir, 'hero-fluentcrm-automatisation.png');
const heroSrcUrl = 'file:///' + heroSrcPath.replace(/\\/g, '/');

const html = template
  .replaceAll('__TITLE__', '10 automatisations FluentCRM indispensables')
  .replaceAll('__IMAGE_PATH__', heroSrcUrl);

const slidePath = path.join(brandDir, 'slide-00-hero.html');
fs.writeFileSync(slidePath, html, 'utf-8');
console.log(`✓ slide-00-hero.html`);

console.log(`\n🎬 Lancement capture.mjs sur le hero (1920x1080)...`);

const capture = spawn(
  'node',
  [
    path.join(__dirname, 'capture.mjs'),
    brandDir,
    '--width=1920',
    '--height=1080',
    '--scale=1',
    '--pattern=slide-00-hero',
  ],
  { stdio: 'inherit' }
);

capture.on('exit', (code) => {
  console.log(`\nCapture exited with code ${code}`);
  process.exit(code || 0);
});

#!/usr/bin/env node
/**
 * inject-meta.mjs - injecte les métadonnées SEO dans les PNG via ExifTool
 *
 * Lit un manifest seo-meta.yaml dans le dossier cible, applique les champs
 * XP* (Windows search), XMP-dc (Adobe), IPTC (médias), EXIF (standard) sur
 * chaque PNG. Réutilisable pour tous les visuels schoolsWP.
 *
 * Prérequis : ExifTool installé (par défaut chemin winget user scope Windows).
 *
 * Usage:
 *   node inject-meta.mjs <directory>
 *   node inject-meta.mjs <directory> --meta=seo-meta.yaml --exiftool=/path/to/ExifTool.exe
 *
 * Format seo-meta.yaml attendu :
 *   defaults:
 *     author: Michaël KIHL
 *     copyright: © schoolsWP - Michaël KIHL
 *     url: https://schoolswp.com/article-slug/
 *   images:
 *     - file: slide-01-hook.png
 *       title: Titre court
 *       subject: Sujet/headline
 *       description: Description longue
 *       alt: Alt text accessibility
 *       keywords: [kw1, kw2, kw3]
 */

import { promises as fs } from 'node:fs';
import { existsSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { homedir, tmpdir } from 'node:os';
import yaml from 'yaml';

const execFileAsync = promisify(execFile);

const DEFAULT_EXIFTOOL = join(homedir(), 'AppData', 'Local', 'Programs', 'ExifTool', 'ExifTool.exe');

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
inject-meta.mjs - injecte SEO metadata dans les PNG via ExifTool

Usage:
  node inject-meta.mjs <directory> [options]

Options:
  --meta=<file>       Manifest YAML (default: seo-meta.yaml)
  --exiftool=<path>   ExifTool binary path (default: AppData winget user scope)

Champs supportés par image:
  title       -> XPTitle, XMP-dc:Title, IPTC:ObjectName
  subject     -> XPSubject, IPTC:Headline
  description -> XPComment, XMP-dc:Description, IPTC:Caption-Abstract, EXIF:ImageDescription
  alt         -> XMP-iptcCore:AltTextAccessibility (accessibilité moderne)
  keywords    -> XPKeywords, XMP-dc:Subject, IPTC:Keywords
  author      -> EXIF:Artist, XPAuthor, XMP-dc:Creator, IPTC:By-line
  copyright   -> EXIF:Copyright, XMP-dc:Rights, IPTC:CopyrightNotice
  url         -> XMP-xmpRights:WebStatement
  software    -> EXIF:Software
`);
  process.exit(args.help ? 0 : 1);
}

const dir = resolve(targetDir);
if (!existsSync(dir)) {
  console.error(`Directory not found: ${dir}`);
  process.exit(1);
}

const exiftool = args.exiftool || DEFAULT_EXIFTOOL;
if (!existsSync(exiftool)) {
  console.error(`ExifTool not found at: ${exiftool}`);
  console.error(`Install: winget install OliverBetz.ExifTool`);
  console.error(`Or pass --exiftool=/path/to/ExifTool.exe`);
  process.exit(1);
}

const metaFile = args.meta || 'seo-meta.yaml';
const metaPath = join(dir, metaFile);
if (!existsSync(metaPath)) {
  console.error(`Meta manifest not found: ${metaPath}`);
  process.exit(1);
}

const yamlText = await fs.readFile(metaPath, 'utf8');
const data = yaml.parse(yamlText);
const defaults = data.defaults || {};
const images = data.images || [];

if (images.length === 0) {
  console.error(`No images defined in ${metaPath}`);
  process.exit(1);
}

console.log(`\n🏷️  Injecting metadata into ${images.length} image(s)`);
console.log(`   Source   : ${dir}`);
console.log(`   Manifest : ${metaFile}`);
console.log(`   ExifTool : ${exiftool}\n`);

const startTime = Date.now();
let successCount = 0;

for (const img of images) {
  const merged = { ...defaults, ...img };
  const filePath = join(dir, merged.file);

  if (!existsSync(filePath)) {
    console.log(`   ✗ ${merged.file} - file not found, skip`);
    continue;
  }

  const flags = [
    '-overwrite_original',
    '-charset', 'filename=utf8',
    '-charset', 'iptc=utf8',
    '-charset', 'exif=utf8',
    '-codedcharacterset=utf8',
  ];

  if (merged.title) {
    flags.push(`-XPTitle=${merged.title}`);
    flags.push(`-XMP-dc:Title=${merged.title}`);
    flags.push(`-IPTC:ObjectName=${merged.title}`);
  }

  if (merged.subject) {
    flags.push(`-XPSubject=${merged.subject}`);
    flags.push(`-IPTC:Headline=${merged.subject}`);
  }

  if (merged.description) {
    flags.push(`-XPComment=${merged.description}`);
    flags.push(`-XMP-dc:Description=${merged.description}`);
    flags.push(`-IPTC:Caption-Abstract=${merged.description}`);
    flags.push(`-EXIF:ImageDescription=${merged.description}`);
  }

  if (merged.alt) {
    flags.push(`-XMP-iptcCore:AltTextAccessibility=${merged.alt}`);
  }

  if (Array.isArray(merged.keywords) && merged.keywords.length > 0) {
    flags.push(`-XPKeywords=${merged.keywords.join(';')}`);
    for (const kw of merged.keywords) {
      flags.push(`-XMP-dc:Subject+=${kw}`);
      flags.push(`-IPTC:Keywords+=${kw}`);
    }
  }

  if (merged.author) {
    flags.push(`-EXIF:Artist=${merged.author}`);
    flags.push(`-XPAuthor=${merged.author}`);
    flags.push(`-XMP-dc:Creator=${merged.author}`);
    flags.push(`-IPTC:By-line=${merged.author}`);
  }

  if (merged.copyright) {
    flags.push(`-EXIF:Copyright=${merged.copyright}`);
    flags.push(`-XMP-dc:Rights=${merged.copyright}`);
    flags.push(`-IPTC:CopyrightNotice=${merged.copyright}`);
  }

  if (merged.url) {
    flags.push(`-XMP-xmpRights:WebStatement=${merged.url}`);
  }

  if (merged.software) {
    flags.push(`-EXIF:Software=${merged.software}`);
  }

  flags.push(filePath);

  // Write args to UTF-8 temp file so non-ASCII chars (é, ©, etc.) survive
  // the Windows shell cp1252 conversion when passed as argv.
  const argsFile = join(tmpdir(), `exiftool-args-${Date.now()}-${Math.random().toString(36).slice(2)}.txt`);
  await fs.writeFile(argsFile, flags.join('\n') + '\n', 'utf8');

  try {
    await execFileAsync(exiftool, ['-@', argsFile]);
    console.log(`   ✓ ${merged.file}`);
    successCount++;
  } catch (err) {
    console.error(`   ✗ ${merged.file} - ${err.message}`);
  } finally {
    await fs.unlink(argsFile).catch(() => {});
  }
}

const duration = ((Date.now() - startTime) / 1000).toFixed(1);
console.log(`\n✅ Done - ${successCount}/${images.length} images in ${duration}s\n`);

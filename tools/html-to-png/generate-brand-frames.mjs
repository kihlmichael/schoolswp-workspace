#!/usr/bin/env node
/**
 * Genere des HTML slides brand schoolsWP pour chaque capture raw FluentCRM,
 * puis appelle capture.mjs pour produire les PNG finaux.
 *
 * Usage:
 *   node tools/html-to-png/generate-brand-frames.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, '..', '..');

const rawDir = path.join(projectRoot, 'content', 'articles', 'fluentcrm-automatisations-indispensables', 'captures-raw');
const brandDir = path.join(projectRoot, 'content', 'articles', 'fluentcrm-automatisations-indispensables', 'captures-brand');
const templatePath = path.join(brandDir, '_template.html');

const captures = [
  { file: '01-dashboard.png',                badge: 'Dashboard',         title: 'Le <strong>tableau de bord FluentCRM</strong> : 34 contacts, 17 automatisations actives, 326 tags' },
  { file: '02-automatisations-liste.png',    badge: 'Automatisations',   title: 'Les <strong>19 funnels actifs</strong> sur schoolsWP : welcome multilingue, lead magnet, FluentCRM Pro Discovery' },
  { file: '03-funnel-builder-welcome-fr.png', badge: 'Builder visuel',   title: 'Le <strong>builder welcome series</strong> : trigger Tag Applied → 4 emails alternés avec wait times' },
  { file: '04-contacts-segmentation.png',    badge: 'Contacts',          title: '<strong>Segmentation contacts</strong> : tags lang_fr/en/de + welcome_news_*_e1_sent traçabilité complète' },
  { file: '05-tags-segmentation.png',        badge: 'Étiquettes',        title: '<strong>326 tags FluentCRM</strong> : segmentation linguistique + progression welcome series automatique' },
  { file: '06-campagnes-email.png',          badge: 'Campagnes',         title: 'Les <strong>33 campagnes email</strong> historiques : taux d\'ouverture, clic et revenu attribué' },
  { file: '07-formulaires.png',              badge: 'Formulaires',       title: '<strong>9 formulaires connectés</strong> à FluentCRM via Fluent Forms : newsletter, lead magnet, sondages' },
  { file: '08-sequences-email.png',          badge: 'Séquences',         title: '<strong>13 séquences email</strong> prêtes à attacher à n\'importe quel funnel ou liste de contacts' },
  { file: '09-reglages-menu-complet.png',    badge: 'Réglages',          title: 'Les <strong>16 onglets de configuration</strong> FluentCRM : entreprise, double opt-in, panier abandonné, webhooks' },
  { file: '10-rapports-overview.png',        badge: 'Rapports',          title: '<strong>Rapports avancés</strong> : croissance contacts, envois email, clics et désinscriptions par période' },
  { file: '11-listes-segmentation.png',      badge: 'Listes',            title: 'Les <strong>7 listes schoolsWP</strong> : étudiants, newsletter, clients, prospects, freebies, partenaires, support' },
];

const template = fs.readFileSync(templatePath, 'utf-8');

console.log(`📐 Génération de ${captures.length} slides HTML brand-aligned...`);

for (const cap of captures) {
  const rawPath = path.join(rawDir, cap.file);
  if (!fs.existsSync(rawPath)) {
    console.warn(`  ⚠ Raw not found: ${cap.file}, skip`);
    continue;
  }

  // Use absolute file:// URL for the image so Playwright finds it
  const imgUrl = 'file:///' + rawPath.replace(/\\/g, '/');

  const html = template
    .replaceAll('__TITLE__', cap.title)
    .replaceAll('__BADGE__', cap.badge)
    .replaceAll('__IMAGE_PATH__', imgUrl);

  const slideName = 'slide-' + cap.file.replace('.png', '') + '.html';
  const slidePath = path.join(brandDir, slideName);
  fs.writeFileSync(slidePath, html, 'utf-8');
  console.log(`  ✓ ${slideName}`);
}

console.log(`\n🎬 Lancement capture.mjs sur ${brandDir} (1920x1200, retina 2x)...`);

const capture = spawn(
  'node',
  [
    path.join(__dirname, 'capture.mjs'),
    brandDir,
    '--width=1920',
    '--height=1200',
    '--scale=1',
    '--pattern=slide-',
  ],
  { stdio: 'inherit' }
);

capture.on('exit', (code) => {
  console.log(`\nCapture exited with code ${code}`);
  process.exit(code || 0);
});

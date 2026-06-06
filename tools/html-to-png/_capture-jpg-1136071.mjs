#!/usr/bin/env node
/**
 * _capture-jpg-1136071.mjs - one-shot : capture les 2 illustrations DE en JPG HQ
 * pour l'article DE wie-erstellt-man-blogeintrag (post 1136071, draft).
 */
import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const ASSETS_DIR = resolve(
  'd:/VS Code/CLAUDE CODE/projects/schoolswp/assets/featured-images/post-1136071',
);

const jobs = [
  {
    html: 'slide-01-structure-infographic-de.html',
    out: '01-wordpress-artikel-strukturieren-lesbarkeit.jpg',
    width: 1080,
    height: 3200,
    quality: 92,
  },
  {
    html: 'slide-02-editor-mockup-de.html',
    out: '02-wordpress-beitrag-editor-oberflaeche.jpg',
    width: 1456,
    height: 668,
    quality: 94,
  },
];

const browser = await chromium.launch();
for (const job of jobs) {
  const context = await browser.newContext({
    viewport: { width: job.width, height: job.height },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  await page.goto(pathToFileURL(resolve(ASSETS_DIR, job.html)).href, {
    waitUntil: 'networkidle',
  });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const el = await page.$('.slide');
  await el.screenshot({
    path: resolve(ASSETS_DIR, job.out),
    type: 'jpeg',
    quality: job.quality,
  });
  await context.close();
  console.log(`JPG written: ${job.out}`);
}
await browser.close();

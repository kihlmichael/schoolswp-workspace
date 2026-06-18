#!/usr/bin/env node
/**
 * _capture-jpg-739164.mjs - one-shot : capture les 2 illustrations EN en JPG HQ
 * pour l'article create-blog-post-wordpress (post 739164).
 * Vit ici (à côté de node_modules) ; sort dans assets/featured-images/post-739164/.
 */
import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const ASSETS_DIR = resolve(
  'd:/VS Code/CLAUDE CODE/projects/schoolswp/assets/featured-images/post-739164',
);

const jobs = [
  {
    html: 'slide-01-structure-infographic-en.html',
    out: '01-how-to-structure-wordpress-article-readability.jpg',
    width: 1080,
    height: 3000,
    quality: 92,
  },
  {
    html: 'slide-02-editor-mockup-en.html',
    out: '02-wordpress-post-editor-interface.jpg',
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

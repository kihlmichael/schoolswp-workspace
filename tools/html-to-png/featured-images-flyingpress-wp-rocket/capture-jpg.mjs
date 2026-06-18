#!/usr/bin/env node
import { chromium } from 'playwright';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = resolve(__dirname, 'slide-flyingpress-vs-wp-rocket.html');
const outPath = resolve(__dirname, 'flyingpress-vs-wp-rocket-wordpress-caching.jpg');

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 },
  deviceScaleFactor: 1,
});
const page = await context.newPage();
await page.goto(pathToFileURL(htmlPath).href);
await page.waitForLoadState('networkidle');

const el = await page.$('.slide');
await el.screenshot({ path: outPath, type: 'jpeg', quality: 92 });

await browser.close();
console.log('JPG written:', outPath);

#!/usr/bin/env node
// One-off: capture slide-*.html via an explicit Chromium executablePath
// (works around a Playwright bundled-revision mismatch). Same selector/dims logic as capture.mjs.
import { chromium } from 'playwright';
import { readdir } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const EXEC =
  process.env.PW_EXEC ||
  'C:/Users/conta/AppData/Local/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-win64/chrome-headless-shell.exe';

const args = {};
for (const a of process.argv.slice(2)) {
  if (a.startsWith('--')) {
    const [k, v] = a.slice(2).split('=');
    args[k] = v === undefined ? true : v;
  } else {
    args.dir = a;
  }
}

const dir = resolve(args.dir);
const width = parseInt(args.width || '480', 10);
const height = parseInt(args.height || '480', 10);
const scale = parseFloat(args.scale || '2');
const selector = args.selector || '.slide';

const files = (await readdir(dir)).filter((f) => f.startsWith('slide-') && f.endsWith('.html')).sort();

const browser = await chromium.launch({ executablePath: EXEC });
const ctx = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: scale });
const page = await ctx.newPage();

for (const f of files) {
  const url = pathToFileURL(join(dir, f)).href;
  const out = join(dir, f.replace(/\.html$/, '.png'));
  await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const t = await page.$(selector);
  if (t) await t.screenshot({ path: out, omitBackground: false });
  else await page.screenshot({ path: out, clip: { x: 0, y: 0, width, height } });
  console.log('OK ' + out);
}

await browser.close();
console.log('done ' + files.length);

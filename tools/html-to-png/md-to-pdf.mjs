#!/usr/bin/env node
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { marked } from 'marked';
import { chromium } from 'playwright';

const [, , inputArg, outputArg] = process.argv;
if (!inputArg || !outputArg) {
  console.error('Usage: node md-to-pdf.mjs <input.md> <output.pdf>');
  process.exit(1);
}

const inputPath = resolve(inputArg);
const outputPath = resolve(outputArg);

let md = readFileSync(inputPath, 'utf8');

let title = 'Document';
let frontmatter = {};
if (md.startsWith('---')) {
  const end = md.indexOf('\n---', 3);
  if (end !== -1) {
    const fmRaw = md.slice(3, end).trim();
    md = md.slice(end + 4).trim();
    for (const line of fmRaw.split('\n')) {
      const m = line.match(/^([\w_-]+):\s*(.*)$/);
      if (m) frontmatter[m[1]] = m[2].trim();
    }
    if (frontmatter.title) title = frontmatter.title;
  }
}

const bodyHtml = marked.parse(md, { gfm: true, breaks: false });

const css = `
@page {
  size: A4;
  margin: 22mm 18mm 22mm 18mm;
  @bottom-center {
    content: counter(page) ' / ' counter(pages);
    font-family: 'Roboto', sans-serif;
    font-size: 9pt;
    color: #888;
  }
}
* { box-sizing: border-box; }
html, body {
  font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #12111F;
  background: #ffffff;
  margin: 0;
  padding: 0;
}
.cover {
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  height: 100vh;
  padding: 0;
}
.cover .accent {
  width: 60px;
  height: 6px;
  background: #00D400;
  margin-bottom: 28px;
}
.cover h1 {
  font-family: 'Nunito Sans', sans-serif;
  font-size: 34pt;
  line-height: 1.1;
  font-weight: 700;
  margin: 0 0 18px 0;
  color: #12111F;
  border: none;
}
.cover .subtitle {
  font-size: 13pt;
  color: #555;
  margin-bottom: 36px;
  max-width: 80%;
}
.cover .meta {
  font-size: 10pt;
  color: #888;
  border-top: 1px solid #ddd;
  padding-top: 14px;
  width: 100%;
}
.cover .meta strong { color: #12111F; font-weight: 600; }
h1, h2, h3, h4 {
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 700;
  color: #12111F;
  line-height: 1.25;
  break-after: avoid-page;
}
h1 {
  font-size: 22pt;
  margin-top: 28pt;
  margin-bottom: 12pt;
  padding-bottom: 8pt;
  border-bottom: 2px solid #00D400;
}
h2 {
  font-size: 15pt;
  margin-top: 22pt;
  margin-bottom: 8pt;
  color: #00A100;
}
h3 {
  font-size: 12pt;
  margin-top: 16pt;
  margin-bottom: 6pt;
}
h4 {
  font-size: 11pt;
  margin-top: 12pt;
  margin-bottom: 4pt;
  color: #555;
}
p {
  margin: 0 0 9pt 0;
}
ul, ol {
  margin: 0 0 10pt 0;
  padding-left: 20pt;
}
li {
  margin-bottom: 3pt;
}
li > ul, li > ol {
  margin-top: 3pt;
  margin-bottom: 3pt;
}
strong { color: #12111F; font-weight: 700; }
em { font-style: italic; color: #444; }
code {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 9pt;
  background: #F4F5F7;
  padding: 1pt 4pt;
  border-radius: 3pt;
  color: #00A100;
}
pre {
  background: #F4F5F7;
  border-left: 3px solid #00D400;
  padding: 10pt 12pt;
  font-size: 9pt;
  line-height: 1.45;
  overflow-x: auto;
  border-radius: 4pt;
  page-break-inside: avoid;
  margin: 10pt 0;
}
pre code {
  background: transparent;
  padding: 0;
  color: #12111F;
}
blockquote {
  border-left: 3px solid #E668D4;
  background: #FAFBFD;
  padding: 8pt 14pt;
  margin: 10pt 0;
  color: #444;
  font-style: normal;
  border-radius: 0 4pt 4pt 0;
  page-break-inside: avoid;
}
blockquote p { margin: 0; }
hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 18pt 0;
}
a {
  color: #00A100;
  text-decoration: none;
  border-bottom: 1px solid rgba(0, 161, 0, 0.3);
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 10pt 0;
  font-size: 9.5pt;
}
th, td {
  border: 1px solid #ddd;
  padding: 6pt 8pt;
  text-align: left;
}
th {
  background: #F4F5F7;
  font-weight: 700;
  color: #12111F;
}
`;

const today = new Date().toISOString().slice(0, 10);
const version = frontmatter.version || '';
const lastUpdated = frontmatter.last_updated || today;

const html = `<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>${title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>${css}</style>
</head>
<body>
  <section class="cover">
    <div class="accent"></div>
    <h1>${title}</h1>
    <div class="subtitle">WordPress. Clair. Structuré. Utile.</div>
    <div class="meta">
      <p><strong>Auteur</strong> : Michaël KIHL — schoolsWP</p>
      ${version ? `<p><strong>Version</strong> : ${version}</p>` : ''}
      <p><strong>Dernière mise à jour</strong> : ${lastUpdated}</p>
    </div>
  </section>
  ${bodyHtml}
</body>
</html>`;

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();

await page.setContent(html, { waitUntil: 'networkidle' });

await page.pdf({
  path: outputPath,
  format: 'A4',
  printBackground: true,
  margin: { top: '22mm', bottom: '22mm', left: '18mm', right: '18mm' },
  displayHeaderFooter: false,
});

await browser.close();

console.log(outputPath);

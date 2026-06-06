// One-shot: rasterize an SVG to a transparent PNG via Chromium (Playwright).
// Usage: node _svg-to-png.mjs <src.svg> <out.png> [width] [height]
import { chromium } from "playwright";
import { readFileSync } from "fs";

const [, , SRC, OUT, wArg, hArg] = process.argv;
const W = parseInt(wArg || "900", 10);
const H = parseInt(hArg || "192", 10);

const svg = readFileSync(SRC, "utf8");
const html = `<!doctype html><html><head><meta charset="utf-8">
<style>*{margin:0;padding:0}html,body{background:transparent}
svg{display:block;width:${W}px;height:${H}px}</style></head>
<body>${svg}</body></html>`;

const browser = await chromium.launch({ channel: "chrome" });
const page = await browser.newPage({
  viewport: { width: W, height: H },
  deviceScaleFactor: 1,
});
await page.setContent(html, { waitUntil: "networkidle" });
const el = await page.$("svg");
await el.screenshot({ path: OUT, omitBackground: true });
await browser.close();
console.log("OK ->", OUT, `${W}x${H}`);

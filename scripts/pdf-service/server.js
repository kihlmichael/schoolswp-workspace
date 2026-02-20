'use strict';

/**
 * schoolsWP PDF Service
 * Convertit du HTML en PDF via Playwright/Chromium
 *
 * POST /generate  { html: string, options?: { format, margin, ... } }
 * GET  /health    → { status: "ok", version, uptime }
 */

const express  = require('express');
const { chromium } = require('playwright');

const app  = express();
const PORT = process.env.PORT || 3001;

app.use(express.json({ limit: '15mb' }));

// ── Health check ──────────────────────────────────────────────────────────
app.get('/health', (_req, res) => {
  res.json({
    status: 'ok',
    service: 'schoolswp-pdf-service',
    version: '1.0.0',
    uptime: Math.round(process.uptime())
  });
});

// ── PDF generation ────────────────────────────────────────────────────────
app.post('/generate', async (req, res) => {
  const startedAt = Date.now();
  const { html, options = {} } = req.body;

  if (!html || typeof html !== 'string') {
    return res.status(400).json({ error: 'Missing or invalid html field' });
  }

  let browser;
  try {
    browser = await chromium.launch({
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--disable-gpu'
      ]
    });

    const page = await browser.newPage();

    // Charger les Google Fonts si nécessaire (réseau disponible)
    await page.setContent(html, { waitUntil: 'networkidle', timeout: 20000 });

    const pdfBuffer = await page.pdf({
      format:          options.format          || 'A4',
      printBackground: options.printBackground ?? true,
      margin: options.margin || {
        top:    '0mm',
        right:  '0mm',
        bottom: '0mm',
        left:   '0mm'
      },
      displayHeaderFooter: false
    });

    await browser.close();

    const elapsed = Date.now() - startedAt;
    console.log(`[pdf-service] PDF generated — ${pdfBuffer.length} bytes in ${elapsed}ms`);

    res.set({
      'Content-Type':        'application/pdf',
      'Content-Length':      pdfBuffer.length,
      'X-Generation-Time-Ms': elapsed
    });
    return res.send(pdfBuffer);

  } catch (err) {
    if (browser) await browser.close().catch(() => {});
    console.error('[pdf-service] Error:', err.message);
    return res.status(500).json({ error: err.message });
  }
});

// ── Start ─────────────────────────────────────────────────────────────────
app.listen(PORT, '0.0.0.0', () => {
  console.log(`[pdf-service] Listening on port ${PORT}`);
});

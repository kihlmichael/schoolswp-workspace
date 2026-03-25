# ── schoolsWP PDF Service — Playwright/Chromium (optimized) ──────────────
# Multi-stage: deps → runtime (Chromium only, non-root, ~800 MB vs ~2 GB)

# ── Stage 1: Install dependencies ────────────────────────────────────────
FROM node:18-slim AS deps

WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --omit=dev && npm cache clean --force

# ── Stage 2: Production runtime ──────────────────────────────────────────
FROM node:18-slim AS runtime

# Install only Chromium + minimal deps (skip Firefox/WebKit)
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      wget \
      ca-certificates \
      fonts-liberation \
      fonts-noto-color-emoji \
      libasound2 \
      libatk-bridge2.0-0 \
      libatk1.0-0 \
      libcups2 \
      libdbus-1-3 \
      libdrm2 \
      libgbm1 \
      libgtk-3-0 \
      libnspr4 \
      libnss3 \
      libxcomposite1 \
      libxdamage1 \
      libxfixes3 \
      libxrandr2 \
      libxss1 \
      xdg-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy deps from build stage
COPY --from=deps /app/node_modules ./node_modules

# Install Chromium only (not Firefox/WebKit — saves ~1 GB)
RUN npx playwright install chromium

# Copy source
COPY package.json server.js ./

# Non-root user
RUN groupadd -g 1001 pdfservice && \
    useradd -u 1001 -g pdfservice -s /bin/false -M pdfservice && \
    chown -R pdfservice:pdfservice /app /ms-playwright

USER 1001

EXPOSE 3001

HEALTHCHECK --interval=20s --timeout=10s --start-period=30s --retries=3 \
  CMD wget -qO- http://localhost:3001/health || exit 1

# Graceful shutdown: Node receives SIGTERM directly (no shell wrapper)
CMD ["node", "server.js"]

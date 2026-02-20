# ── schoolsWP PDF Service — Playwright/Chromium ───────────────────────────
FROM mcr.microsoft.com/playwright:v1.44.0-jammy

WORKDIR /app

# Dépendances Node
COPY package.json .
RUN npm install --omit=dev

# Code source
COPY server.js .

# Playwright télécharge Chromium lors du npm install via postinstall.
# Forcer si nécessaire :
# RUN npx playwright install chromium

EXPOSE 3001

# Healthcheck intégré
HEALTHCHECK --interval=20s --timeout=10s --start-period=30s --retries=3 \
  CMD wget -qO- http://localhost:3001/health || exit 1

CMD ["node", "server.js"]

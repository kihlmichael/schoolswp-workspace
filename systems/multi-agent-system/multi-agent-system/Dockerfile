# ── schoolsWP Multi-Agent System — FastAPI/Uvicorn (optimized) ───────────
# Multi-stage: deps → runtime (non-root, healthcheck, minimal image)

# ── Stage 1: Build & install dependencies ────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build tools
RUN pip install --no-cache-dir hatchling

# Install deps from pyproject.toml (single source of truth)
COPY pyproject.toml .
RUN pip install --no-cache-dir --prefix=/install \
    "anthropic>=0.40.0" \
    "fastapi>=0.115.0" \
    "uvicorn[standard]>=0.32.0" \
    "sse-starlette>=2.1.0" \
    "aiosqlite>=0.20.0" \
    "pydantic>=2.10.0" \
    "python-dotenv>=1.0.0" \
    "httpx>=0.27.0"

# Install package itself (no deps, already installed above)
COPY . .
RUN pip install --no-cache-dir --no-deps --prefix=/install .

# ── Stage 2: Production runtime ──────────────────────────────────────────
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Create non-root user
RUN groupadd -g 1001 appuser && \
    useradd -u 1001 -g appuser -s /bin/false -M appuser && \
    mkdir -p /app/data/decisions && \
    chown -R appuser:appuser /app

# Copy source (api + packages only — what hatch builds)
COPY --chown=appuser:appuser api/ ./api/
COPY --chown=appuser:appuser packages/ ./packages/
COPY --chown=appuser:appuser pyproject.toml ./

USER 1001

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
  CMD python -c "import urllib.request, sys; urllib.request.urlopen('http://localhost:8000/health') or sys.exit(1)"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

# Étape 1 : installer les dépendances en premier (layer cache Docker)
# Si seul pyproject.toml change → pas de re-download des packages
COPY pyproject.toml .
RUN pip install --no-cache-dir hatchling \
    "anthropic>=0.40.0" \
    "fastapi>=0.115.0" \
    "uvicorn[standard]>=0.32.0" \
    "sse-starlette>=2.1.0" \
    "aiosqlite>=0.20.0" \
    "pydantic>=2.10.0" \
    "python-dotenv>=1.0.0" \
    "httpx>=0.27.0"

# Étape 2 : copier le source et installer le package (sans re-télécharger les deps)
COPY . .
RUN pip install --no-cache-dir --no-deps .

# Répertoire de données (surchargé par le volume en prod)
RUN mkdir -p data/decisions

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

#!/usr/bin/env bash
# setup.sh — Script d'onboarding schoolsWP OS
# Automatise la configuration initiale sur une nouvelle machine ou un clone frais.
# Fonctionne sous Windows + Git Bash, Linux et macOS.

set -euo pipefail

# --- Couleurs ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

ok()      { echo -e "  ${GREEN}[OK]${NC} $1"; }
warn()    { echo -e "  ${YELLOW}[WARN]${NC} $1"; }
err()     { echo -e "  ${RED}[ERREUR]${NC} $1"; }
info()    { echo -e "  ${CYAN}[INFO]${NC} $1"; }
section() { echo -e "\n${BOLD}==> $1${NC}"; }

# --- Trouver la racine du projet ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BOLD}"
echo "  schoolsWP OS — Script d'installation"
echo "  ======================================"
echo -e "${NC}"
info "Racine du projet : $PROJECT_ROOT"

# --- Compteurs ---
ERRORS=0
WARNINGS=0

# =============================================================================
# 1. Prerequis
# =============================================================================
section "1/5 — Verification des prerequis"

# Python
if command -v python3 &>/dev/null; then
  PY_VERSION=$(python3 --version 2>&1)
  ok "Python trouve : $PY_VERSION"
elif command -v python &>/dev/null; then
  PY_VERSION=$(python --version 2>&1)
  ok "Python trouve : $PY_VERSION"
else
  err "Python non trouve (python3 ou python requis, >= 3.11)"
  ERRORS=$((ERRORS + 1))
fi

# uv
if command -v uv &>/dev/null; then
  UV_VERSION=$(uv --version 2>&1)
  ok "uv trouve : $UV_VERSION"
else
  warn "uv non trouve — installation recommandee : pip install uv"
  WARNINGS=$((WARNINGS + 1))
fi

# Node / npm
if command -v node &>/dev/null; then
  NODE_VERSION=$(node --version 2>&1)
  ok "Node.js trouve : $NODE_VERSION"
else
  warn "Node.js non trouve (optionnel, pour les deps JS)"
  WARNINGS=$((WARNINGS + 1))
fi

if command -v npm &>/dev/null; then
  NPM_VERSION=$(npm --version 2>&1)
  ok "npm trouve : $NPM_VERSION"
else
  warn "npm non trouve (optionnel)"
  WARNINGS=$((WARNINGS + 1))
fi

# Git
if command -v git &>/dev/null; then
  GIT_VERSION=$(git --version 2>&1)
  ok "Git trouve : $GIT_VERSION"
else
  err "Git non trouve"
  ERRORS=$((ERRORS + 1))
fi

# =============================================================================
# 2. Fichiers de configuration
# =============================================================================
section "2/5 — Copie des fichiers de configuration"

if [ -f ".env" ]; then
  ok ".env existe deja"
else
  if [ -f ".env.example" ]; then
    cp .env.example .env
    ok ".env cree depuis .env.example"
    warn "Pense a remplir les cles API dans .env (ANTHROPIC_API_KEY, etc.)"
    WARNINGS=$((WARNINGS + 1))
  else
    err ".env.example introuvable — impossible de creer .env"
    ERRORS=$((ERRORS + 1))
  fi
fi

if [ -f ".mcp.json" ]; then
  ok ".mcp.json existe deja"
else
  if [ -f ".mcp.json.example" ]; then
    cp .mcp.json.example .mcp.json
    ok ".mcp.json cree depuis .mcp.json.example"
    warn "Pense a remplir les cles API MCP dans .mcp.json"
    WARNINGS=$((WARNINGS + 1))
  else
    err ".mcp.json.example introuvable — impossible de creer .mcp.json"
    ERRORS=$((ERRORS + 1))
  fi
fi

# =============================================================================
# 3. Installation des dependances Python
# =============================================================================
section "3/5 — Installation des dependances Python (uv sync)"

if command -v uv &>/dev/null; then
  if uv sync 2>&1; then
    ok "Dependances Python installees via uv sync"
  else
    err "uv sync a echoue"
    ERRORS=$((ERRORS + 1))
  fi
else
  warn "uv absent — dependances Python non installees"
  info "Installe uv puis relance : pip install uv && uv sync"
  WARNINGS=$((WARNINGS + 1))
fi

# JS deps (optionnel)
if [ -f "package.json" ] && command -v npm &>/dev/null; then
  info "Installation des dependances JS (npm install)..."
  if npm install 2>&1; then
    ok "Dependances JS installees"
  else
    warn "npm install a echoue (optionnel, non bloquant)"
    WARNINGS=$((WARNINGS + 1))
  fi
else
  info "Pas de package.json ou npm absent — deps JS ignorees"
fi

# =============================================================================
# 4. Verification (ruff + pytest)
# =============================================================================
section "4/5 — Verification du code (lint + tests)"

VENV_PYTHON=".venv/Scripts/python"
if [ ! -f "$VENV_PYTHON" ]; then
  # Fallback Linux/macOS
  VENV_PYTHON=".venv/bin/python"
fi

if [ -f "$VENV_PYTHON" ]; then
  # Ruff check
  info "Lancement de ruff check..."
  if "$VENV_PYTHON" -m ruff check core/agents-py/ 2>&1; then
    ok "ruff check : aucun probleme detecte"
  else
    warn "ruff check a signale des problemes (voir ci-dessus)"
    WARNINGS=$((WARNINGS + 1))
  fi

  # Pytest
  info "Lancement de pytest..."
  if "$VENV_PYTHON" -m pytest tests/ -v --tb=short 2>&1; then
    ok "pytest : tous les tests passent"
  else
    warn "pytest a signale des echecs (voir ci-dessus)"
    WARNINGS=$((WARNINGS + 1))
  fi
else
  warn "Venv introuvable ($VENV_PYTHON) — verification impossible"
  info "Lance d'abord uv sync pour creer le venv"
  WARNINGS=$((WARNINGS + 1))
fi

# =============================================================================
# 5. Resume
# =============================================================================
section "5/5 — Resume"

echo ""
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
  echo -e "  ${GREEN}${BOLD}Installation terminee sans probleme !${NC}"
elif [ $ERRORS -eq 0 ]; then
  echo -e "  ${YELLOW}${BOLD}Installation terminee avec $WARNINGS avertissement(s).${NC}"
else
  echo -e "  ${RED}${BOLD}Installation terminee avec $ERRORS erreur(s) et $WARNINGS avertissement(s).${NC}"
fi

echo ""
info "Actions manuelles restantes :"
echo -e "  ${CYAN}1.${NC} Remplir les cles API dans ${BOLD}.env${NC} (ANTHROPIC_API_KEY obligatoire)"
echo -e "  ${CYAN}2.${NC} Remplir les cles API MCP dans ${BOLD}.mcp.json${NC} (n8n, rapidapi, etc.)"
echo -e "  ${CYAN}3.${NC} (Optionnel) Installer pre-commit : pip install pre-commit && pre-commit install"
echo ""

# Toujours sortir 0 — les erreurs sont informatives, pas bloquantes
exit 0

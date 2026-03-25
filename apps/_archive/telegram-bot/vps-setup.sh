#!/usr/bin/env bash
# Script de setup VPS pour ccpa-telegram (schoolsWP)
# À lancer une seule fois sur le VPS en tant que root ou sudo

set -e

echo "=== Setup Claude Code Telegram Bot — schoolsWP ==="

# 1. Mise à jour système
apt update && apt upgrade -y

# 2. Node.js 22 (via NodeSource)
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs git

echo "Node.js: $(node --version)"
echo "npm: $(npm --version)"

# 3. pm2 (gestionnaire de processus)
npm install -g pm2

# 4. Claude Code CLI
npm install -g @anthropic-ai/claude-code

echo ""
echo "=== Installation terminée ==="
echo "Prochaine étape : cloner le repo et configurer .env"
echo "  git clone <ton-repo> ~/workspace"
echo "  cd ~/workspace/telegram-bot"
echo "  cp .env.example .env && nano .env"
echo "  pm2 start ecosystem.config.js"

#!/usr/bin/env bash
# Démarre le tunnel serveo.net avec la clé SSH dédiée.
# URL stable : https://e30e381f3da968b4-172-94-66-9.serveousercontent.com
#
# Usage :
#   bash scripts/start-tunnel.sh          # en avant-plan (Ctrl+C pour arrêter)
#   bash scripts/start-tunnel.sh &        # en arrière-plan

set -e

KEY="$HOME/.ssh/serveo_agents"
LOCAL_PORT="${API_PORT:-8000}"
TUNNEL_URL="https://schoolswp-agents.serveo.net"
SUBDOMAIN="schoolswp-agents"

if [ ! -f "$KEY" ]; then
  echo "[tunnel] Clé SSH introuvable : $KEY"
  echo "[tunnel] Génère-la avec : ssh-keygen -t ed25519 -f $KEY -N \"\""
  exit 1
fi

echo "[tunnel] Démarrage du tunnel serveo → localhost:$LOCAL_PORT"
echo "[tunnel] URL publique : $TUNNEL_URL"
echo "[tunnel] Appuie sur Ctrl+C pour arrêter."

exec ssh \
  -o StrictHostKeyChecking=no \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -i "$KEY" \
  -R "${SUBDOMAIN}:80:localhost:$LOCAL_PORT" \
  serveo.net

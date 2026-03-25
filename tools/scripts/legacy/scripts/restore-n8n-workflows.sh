#!/bin/bash
# Restore n8n workflows from Git backup
# Usage: ./restore-n8n-workflows.sh [workflow-file.json]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

if [ -f "$PROJECT_ROOT/.env" ]; then
    export $(grep -v '^#' "$PROJECT_ROOT/.env" | xargs)
fi

N8N_HOST="${N8N_HOST:-http://localhost:5678}"
N8N_API_KEY="${N8N_API_KEY}"
BACKUP_DIR="$PROJECT_ROOT/workflows"

if [ -z "$N8N_API_KEY" ]; then
    echo "ERROR: N8N_API_KEY not set"
    exit 1
fi

if [ -n "$1" ]; then
    workflows=("$1")
else
    workflows=("$BACKUP_DIR"/*.json)
fi

echo "Restoring workflows to $N8N_HOST..."

for workflow_file in "${workflows[@]}"; do
    if [ -f "$workflow_file" ]; then
        echo "  Importing $(basename "$workflow_file")..."

        curl -s -X POST "${N8N_HOST}/api/v1/workflows" \
          -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
          -H "Content-Type: application/json" \
          -d "@$workflow_file" > /dev/null

        echo "    ✓ Imported"
    fi
done

echo "✓ Restoration completed"

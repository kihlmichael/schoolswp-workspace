#!/bin/bash
# n8n Health Check Script
# Returns 0 if healthy, 1 if unhealthy

N8N_HOST="${N8N_HOST:-http://localhost:5678}"

if curl -sf "${N8N_HOST}/healthz" > /dev/null; then
    echo "✓ n8n is healthy"
    exit 0
else
    echo "✗ n8n is unhealthy"
    exit 1
fi

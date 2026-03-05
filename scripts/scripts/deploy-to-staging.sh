#!/bin/bash
# Deploy workflows to staging
# Usage: ./deploy-to-staging.sh

set -e

echo "🚀 Deploying to Staging"
echo "======================="
echo ""

# Set staging environment
export NODE_ENV=staging
export N8N_HOST="${N8N_STAGING_HOST:-http://staging.n8n.local:5678}"

# Run health check
./scripts/health-check.sh || {
    echo "ERROR: Staging n8n is not healthy, aborting deployment"
    exit 1
}

# Restore workflows
./scripts/restore-n8n-workflows.sh

echo ""
echo "✓ Staging deployment completed"
echo "✓ Please test in staging before deploying to production"

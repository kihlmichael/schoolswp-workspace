#!/bin/bash
# Deploy workflows to production
# Usage: ./deploy-to-production.sh

set -e

echo "🚀 Deploying to Production"
echo "=========================="
echo ""

# Confirmation
read -p "Are you sure you want to deploy to PRODUCTION? (yes/NO) " -r
if [[ ! $REPLY =~ ^yes$ ]]; then
    echo "Deployment cancelled"
    exit 0
fi

# Run health check
./scripts/health-check.sh || {
    echo "ERROR: n8n is not healthy, aborting deployment"
    exit 1
}

# Run tests if available
if [ -f "./scripts/run-tests.sh" ]; then
    ./scripts/run-tests.sh || {
        echo "ERROR: Tests failed, aborting deployment"
        exit 1
    }
fi

# Restore workflows
./scripts/restore-n8n-workflows.sh

echo ""
echo "✓ Deployment completed successfully"
echo "✓ Please verify workflows in n8n UI"

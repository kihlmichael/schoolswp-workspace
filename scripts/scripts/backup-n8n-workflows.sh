#!/bin/bash
#==============================================================================
# n8n Workflow Backup Script
#==============================================================================
# Purpose: Automated backup of n8n workflows to Git repository
# Usage: ./backup-n8n-workflows.sh
# Cron: 0 2 * * * (daily at 2 AM)
# Author: n8n Framework
# Version: 1.0.0
#==============================================================================

set -e  # Exit on error

#------------------------------------------------------------------------------
# CONFIGURATION
#------------------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Load environment variables
if [ -f "$PROJECT_ROOT/.env" ]; then
    export $(grep -v '^#' "$PROJECT_ROOT/.env" | xargs)
fi

# n8n Configuration
N8N_HOST="${N8N_HOST:-http://localhost:5678}"
N8N_API_KEY="${N8N_API_KEY}"

# Backup Configuration
BACKUP_DIR="$PROJECT_ROOT/workflows"
GIT_REPO="$PROJECT_ROOT"
LOG_FILE="$PROJECT_ROOT/logs/backup-$(date +%Y%m%d).log"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1" | tee -a "$LOG_FILE"
}

#------------------------------------------------------------------------------
# PREFLIGHT CHECKS
#------------------------------------------------------------------------------

log "Starting n8n workflow backup..."

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    log_error "jq is not installed. Please install jq first."
    log_error "Install: sudo apt-get install jq (Ubuntu/Debian) or brew install jq (Mac)"
    exit 1
fi

# Check API key
if [ -z "$N8N_API_KEY" ]; then
    log_error "N8N_API_KEY is not set"
    log_error "Please set N8N_API_KEY in .env file or environment variable"
    exit 1
fi

# Create backup directory
mkdir -p "$BACKUP_DIR"
mkdir -p "$(dirname "$LOG_FILE")"

log "Configuration:"
log "  n8n Host: $N8N_HOST"
log "  Backup Directory: $BACKUP_DIR"
log "  Git Repository: $GIT_REPO"

#------------------------------------------------------------------------------
# CHECK N8N AVAILABILITY
#------------------------------------------------------------------------------

log "Checking n8n availability..."

if ! curl -sf "${N8N_HOST}/healthz" > /dev/null; then
    log_error "n8n is not responding at $N8N_HOST"
    log_error "Please ensure n8n is running"
    exit 1
fi

log_success "n8n is available"

#------------------------------------------------------------------------------
# EXPORT WORKFLOWS
#------------------------------------------------------------------------------

log "Exporting workflows from n8n..."

# Fetch all workflows
RESPONSE=$(curl -s -X GET "${N8N_HOST}/api/v1/workflows" \
  -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
  -H "Accept: application/json")

# Check if request was successful
if [ -z "$RESPONSE" ]; then
    log_error "Failed to fetch workflows from n8n API"
    exit 1
fi

# Parse workflows
WORKFLOW_COUNT=$(echo "$RESPONSE" | jq -r '.data | length' 2>/dev/null || echo "0")

if [ "$WORKFLOW_COUNT" -eq "0" ]; then
    log_warning "No workflows found in n8n"
    exit 0
fi

log "Found $WORKFLOW_COUNT workflows"

# Export each workflow
EXPORTED_COUNT=0
FAILED_COUNT=0

echo "$RESPONSE" | jq -c '.data[]' | while read -r workflow; do
    # Extract workflow details
    ID=$(echo "$workflow" | jq -r '.id')
    NAME=$(echo "$workflow" | jq -r '.name')
    ACTIVE=$(echo "$workflow" | jq -r '.active')

    # Sanitize filename (remove special characters)
    FILENAME=$(echo "$NAME" | sed 's/[^a-zA-Z0-9-]/_/g' | sed 's/__*/_/g')
    FILEPATH="$BACKUP_DIR/${FILENAME}_${ID}.json"

    log "  Exporting: $NAME (ID: $ID)"

    # Sanitize credentials (replace with placeholders)
    SANITIZED=$(echo "$workflow" | jq 'walk(
        if type == "object" then
            if has("credentials") then
                .credentials = "{{CREDENTIAL_PLACEHOLDER}}"
            else
                .
            end
        else
            .
        end
    )')

    # Save workflow to file
    echo "$SANITIZED" | jq '.' > "$FILEPATH" 2>/dev/null

    if [ $? -eq 0 ]; then
        log_success "    ✓ Exported: ${FILENAME}_${ID}.json"
        ((EXPORTED_COUNT++))
    else
        log_error "    ✗ Failed to export: $NAME"
        ((FAILED_COUNT++))
    fi
done

# Wait for subshell to complete
wait

log_success "Export completed: $EXPORTED_COUNT workflows exported, $FAILED_COUNT failed"

#------------------------------------------------------------------------------
# GIT OPERATIONS
#------------------------------------------------------------------------------

log "Committing changes to Git..."

cd "$GIT_REPO"

# Configure Git if not configured
if [ -z "$(git config user.name)" ]; then
    git config user.name "n8n Backup Bot"
fi

if [ -z "$(git config user.email)" ]; then
    git config user.email "backup@n8n.local"
fi

# Add workflows to Git
git add workflows/*.json

# Check if there are changes
if git diff --staged --quiet; then
    log "No changes detected, skipping commit"
else
    # Get list of changed files
    CHANGED_FILES=$(git diff --staged --name-status | head -5)

    # Create commit
    COMMIT_MESSAGE="Automated workflow backup: $(date '+%Y-%m-%d %H:%M:%S')

Workflows exported: $EXPORTED_COUNT
Changes:
$(echo "$CHANGED_FILES" | sed 's/^/  /')

Generated by: n8n-framework backup script"

    git commit -m "$COMMIT_MESSAGE"

    log_success "Changes committed to Git"

    # Push to remote (if configured)
    if git remote -v | grep -q 'origin'; then
        log "Pushing to remote repository..."

        if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
            log_success "Successfully pushed to remote"
        else
            log_error "Failed to push to remote (non-fatal)"
        fi
    else
        log_warning "No remote repository configured, skipping push"
    fi
fi

#------------------------------------------------------------------------------
# CLEANUP OLD LOGS
#------------------------------------------------------------------------------

log "Cleaning up old logs (keeping last 30 days)..."

find "$PROJECT_ROOT/logs" -name "backup-*.log" -mtime +30 -delete 2>/dev/null || true

#------------------------------------------------------------------------------
# SUMMARY
#------------------------------------------------------------------------------

log_success "============================================"
log_success "BACKUP COMPLETED SUCCESSFULLY"
log_success "============================================"
log_success "Workflows exported: $EXPORTED_COUNT"
log_success "Failed exports: $FAILED_COUNT"
log_success "Backup location: $BACKUP_DIR"
log_success "Log file: $LOG_FILE"
log_success "============================================"

exit 0

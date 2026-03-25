#!/bin/bash
#==============================================================================
# n8n Environment Setup Script
#==============================================================================
# Purpose: Complete automated setup of n8n environment
# Usage: ./setup-n8n-environment.sh [dev|staging|prod]
# Author: n8n Framework
# Version: 1.0.0
#==============================================================================

set -e  # Exit on error
set -u  # Exit on undefined variable

#------------------------------------------------------------------------------
# CONFIGURATION
#------------------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
ENV_TYPE="${1:-dev}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_command() {
    if ! command -v $1 &> /dev/null; then
        log_error "$1 is not installed. Please install it first."
        exit 1
    fi
}

generate_secure_key() {
    openssl rand -base64 32
}

generate_hex_key() {
    openssl rand -hex 32
}

#------------------------------------------------------------------------------
# PRE-FLIGHT CHECKS
#------------------------------------------------------------------------------

log_info "Starting n8n environment setup for: $ENV_TYPE"
echo ""

log_info "Checking dependencies..."
check_command "node"
check_command "npm"
check_command "openssl"
check_command "git"

NODE_VERSION=$(node --version)
NPM_VERSION=$(npm --version)

log_success "Node.js version: $NODE_VERSION"
log_success "npm version: $NPM_VERSION"
echo ""

#------------------------------------------------------------------------------
# VALIDATE ENVIRONMENT TYPE
#------------------------------------------------------------------------------

if [[ ! "$ENV_TYPE" =~ ^(dev|staging|prod)$ ]]; then
    log_error "Invalid environment type: $ENV_TYPE"
    echo "Usage: $0 [dev|staging|prod]"
    exit 1
fi

log_info "Setting up $ENV_TYPE environment"
echo ""

#------------------------------------------------------------------------------
# INSTALL N8N
#------------------------------------------------------------------------------

log_info "Installing n8n globally..."
npm install -g n8n@2.4.8

if [ $? -eq 0 ]; then
    log_success "n8n installed successfully"
    N8N_VERSION=$(n8n --version 2>&1 || echo "unknown")
    log_info "n8n version: $N8N_VERSION"
else
    log_error "Failed to install n8n"
    exit 1
fi

echo ""

#------------------------------------------------------------------------------
# INSTALL MCP COMMUNITY NODE
#------------------------------------------------------------------------------

log_info "Installing n8n-nodes-mcp community package..."
npm install -g n8n-nodes-mcp@0.1.37

if [ $? -eq 0 ]; then
    log_success "n8n-nodes-mcp installed successfully"
else
    log_warning "Failed to install n8n-nodes-mcp (optional)"
fi

echo ""

#------------------------------------------------------------------------------
# GENERATE ENCRYPTION KEYS
#------------------------------------------------------------------------------

log_info "Generating encryption keys..."

N8N_ENCRYPTION_KEY=$(generate_secure_key)
N8N_API_KEY=$(generate_hex_key)
N8N_JWTSECRET=$(generate_secure_key)
BASIC_AUTH_PASSWORD=$(generate_secure_key | tr -d '/+=' | cut -c1-20)
GRAFANA_PASSWORD=$(generate_secure_key | tr -d '/+=' | cut -c1-20)

log_success "Encryption keys generated"
echo ""

#------------------------------------------------------------------------------
# CREATE .env FILE
#------------------------------------------------------------------------------

ENV_FILE="$PROJECT_ROOT/.env"

if [ -f "$ENV_FILE" ]; then
    log_warning ".env file already exists"
    read -p "Do you want to overwrite it? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Skipping .env creation"
    else
        log_info "Creating .env file..."
        create_env_file
    fi
else
    log_info "Creating .env file..."
    create_env_file
fi

echo ""

#------------------------------------------------------------------------------
# CREATE ENV FILE FUNCTION
#------------------------------------------------------------------------------

create_env_file() {
    cat > "$ENV_FILE" << EOF
# n8n Environment Configuration - Generated on $(date)
# Environment: $ENV_TYPE

# Core Configuration
N8N_ENCRYPTION_KEY=$N8N_ENCRYPTION_KEY
N8N_HOST=localhost
N8N_PORT=5678
N8N_PROTOCOL=http
N8N_EDITOR_BASE_URL=http://localhost:5678

# Authentication
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD
N8N_JWTSECRET=$N8N_JWTSECRET

# Database
DB_TYPE=postgresdb
DB_POSTGRESDB_HOST=localhost
DB_POSTGRESDB_PORT=5432
DB_POSTGRESDB_DATABASE=n8n_$ENV_TYPE
DB_POSTGRESDB_USER=n8n_user
DB_POSTGRESDB_PASSWORD=CHANGE_THIS_PASSWORD

# Community Packages
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
N8N_COMMUNITY_PACKAGES_ENABLED=true

# Logging
N8N_LOG_LEVEL=info
N8N_LOG_OUTPUT=console

# Performance
EXECUTIONS_PROCESS=main
EXECUTIONS_TIMEOUT=300
EXECUTIONS_TIMEOUT_MAX=3600

# Metrics
N8N_METRICS=true
N8N_METRICS_PREFIX=n8n_

# API
N8N_API_ENABLED=true
N8N_API_KEY=$N8N_API_KEY

# MCP Integration
MCP_OTTOKIT_ENDPOINT=
MCP_FIRECRAWL_API_KEY=
MCP_PABBLY_ENDPOINT=
MCP_DATAFORSEO_LOGIN=
MCP_DATAFORSEO_PASSWORD=

# Monitoring
GRAFANA_ADMIN_PASSWORD=$GRAFANA_PASSWORD

# Environment
NODE_ENV=$ENV_TYPE
DEPLOYMENT_ENVIRONMENT=$ENV_TYPE
DEPLOYMENT_VERSION=1.0.0
EOF

    chmod 600 "$ENV_FILE"
    log_success ".env file created at: $ENV_FILE"
}

#------------------------------------------------------------------------------
# DISPLAY CREDENTIALS
#------------------------------------------------------------------------------

log_info "============================================"
log_info "IMPORTANT CREDENTIALS - SAVE THESE SECURELY"
log_info "============================================"
echo ""
echo -e "${GREEN}N8N_ENCRYPTION_KEY:${NC} $N8N_ENCRYPTION_KEY"
echo -e "${GREEN}N8N_API_KEY:${NC} $N8N_API_KEY"
echo -e "${GREEN}Basic Auth User:${NC} admin"
echo -e "${GREEN}Basic Auth Password:${NC} $BASIC_AUTH_PASSWORD"
echo -e "${GREEN}Grafana Admin Password:${NC} $GRAFANA_PASSWORD"
echo ""
log_warning "Store these credentials in a secure password manager!"
echo ""

#------------------------------------------------------------------------------
# CREATE DIRECTORIES
#------------------------------------------------------------------------------

log_info "Creating project directories..."

mkdir -p "$PROJECT_ROOT/.n8n"
mkdir -p "$PROJECT_ROOT/logs"
mkdir -p "$PROJECT_ROOT/systems/workflows/workflows/examples"
mkdir -p "$PROJECT_ROOT/scripts"
mkdir -p "$PROJECT_ROOT/config/grafana-dashboards"
mkdir -p "$PROJECT_ROOT/docs"

log_success "Directories created"
echo ""

#------------------------------------------------------------------------------
# CREATE DATABASE (if PostgreSQL is available)
#------------------------------------------------------------------------------

if command -v psql &> /dev/null; then
    log_info "PostgreSQL detected. Do you want to create the database?"
    read -p "Create database? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_info "Creating database n8n_$ENV_TYPE..."
        createdb "n8n_$ENV_TYPE" 2>/dev/null || log_warning "Database may already exist"

        psql -d "n8n_$ENV_TYPE" -c "
        CREATE TABLE IF NOT EXISTS error_logs (
            id SERIAL PRIMARY KEY,
            workflow_id TEXT,
            workflow_name TEXT,
            execution_id TEXT,
            node_name TEXT,
            error_message TEXT,
            severity TEXT,
            environment TEXT,
            timestamp TIMESTAMP,
            error_data JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        " 2>/dev/null && log_success "Database and error_logs table created"
    fi
else
    log_warning "PostgreSQL not found. You'll need to set up the database manually."
fi

echo ""

#------------------------------------------------------------------------------
# INITIALIZE GIT (if not already initialized)
#------------------------------------------------------------------------------

if [ ! -d "$PROJECT_ROOT/.git" ]; then
    log_info "Initializing Git repository..."
    cd "$PROJECT_ROOT"
    git init
    log_success "Git repository initialized"
else
    log_info "Git repository already exists"
fi

echo ""

#------------------------------------------------------------------------------
# FINAL INSTRUCTIONS
#------------------------------------------------------------------------------

log_success "============================================"
log_success "n8n ENVIRONMENT SETUP COMPLETE!"
log_success "============================================"
echo ""
log_info "Next steps:"
echo ""
echo "  1. Review and update .env file with your specific configuration"
echo "  2. Configure MCP endpoints in .env if using MCP servers"
echo "  3. Start n8n:"
echo -e "     ${GREEN}n8n start${NC}"
echo ""
echo "  4. Access n8n web interface:"
echo -e "     ${GREEN}http://localhost:5678${NC}"
echo ""
echo "  5. Login with:"
echo -e "     Username: ${GREEN}admin${NC}"
echo -e "     Password: ${GREEN}$BASIC_AUTH_PASSWORD${NC}"
echo ""
echo "  6. Import the error workflow:"
echo -e "     ${GREEN}Import systems/workflows/workflows/error-workflow-centralized.json${NC}"
echo ""
log_info "For more information, see README.md"
echo ""

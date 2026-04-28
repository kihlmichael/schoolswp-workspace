#!/usr/bin/env bash
# Common helpers for claude-config-backup scripts.
# Tar-only (no rsync dependency) pour compat Git Bash Windows.

set -euo pipefail

WORKSPACE_SRC="${CLAUDE_WORKSPACE_SRC:-/d/VS Code/CLAUDE CODE/.claude}"
USER_SRC="${CLAUDE_USER_SRC:-$HOME/.claude}"
SYNC_DIR="$HOME/claude-config-sync"
BACKUP_DIR_DEFAULT="$HOME/claude-config-backups"

# Exclude patterns (tar --exclude syntax, glob).
# Keep in sync with "Secrets exclus" section of SKILL.md.
EXCLUDES=(
  # Env files (tout ce qui ressemble de près ou de loin à .env)
  ".env"
  ".env.local"
  ".env.*"
  "*.env"
  "*.env.local"
  "secrets.env"
  "secrets*"
  "*secrets*"
  # MCP/Claude config locaux
  ".mcp.json"
  "settings.local.json"
  ".claude.json.backup"
  # Keys / certs
  "*.key"
  "*.pem"
  "*.p12"
  "*.pfx"
  # Tokens (tous patterns)
  "*.token"
  "*token*.json"
  "token.json"
  "*_token.json"
  "*-token.json"
  "*oauth*"
  "*_oauth*"
  "refresh_token*"
  # Credentials
  "credentials.json"
  ".credentials.json"
  "*credentials*"
  "client_secret*.json"
  "service-account*.json"
  "gcloud*.json"
  # Autres
  "projects"
  "node_modules"
  ".DS_Store"
  "Thumbs.db"
  ".git"
)

die() { echo "ERROR: $*" >&2; exit 1; }
info() { echo ">> $*"; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Commande requise manquante : $1"
}

tar_excludes() {
  local out=()
  for pat in "${EXCLUDES[@]}"; do
    out+=(--exclude="$pat")
  done
  printf '%s\n' "${out[@]}"
}

load_backupignore() {
  local dir="$1"
  local f="$dir/.backupignore"
  [[ -f "$f" ]] || return 0
  while IFS= read -r line; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    EXCLUDES+=("$line")
  done < "$f"
}

HAS_WORKSPACE=0
HAS_USER=0

check_sources() {
  if [[ -d "$WORKSPACE_SRC" ]]; then
    HAS_WORKSPACE=1
    info "Workspace source: $WORKSPACE_SRC"
  else
    info "Workspace absent ($WORKSPACE_SRC) — skippé"
  fi
  if [[ -d "$USER_SRC" ]]; then
    HAS_USER=1
    info "User source: $USER_SRC"
  else
    info "User absent ($USER_SRC) — skippé"
  fi
  [[ $HAS_WORKSPACE -eq 1 || $HAS_USER -eq 1 ]] || die "Aucune source trouvée. Définis CLAUDE_WORKSPACE_SRC ou CLAUDE_USER_SRC."
}

# Copy src/ contents into dst/, applying EXCLUDES via tar-pipe (no rsync).
# Preserves perms, deletes nothing from dst (caller must clean if --delete semantics needed).
tar_copy() {
  local src="$1" dst="$2"
  mkdir -p "$dst"
  mapfile -t EXCL < <(tar_excludes)
  tar -C "$src" -cf - "${EXCL[@]}" . | tar -C "$dst" -xf -
}

# Mirror src/ into dst/ (empties dst first, then copies with excludes).
tar_mirror() {
  local src="$1" dst="$2"
  if [[ -d "$dst" ]]; then
    # Wipe contents but keep the directory itself (safer than rm -rf on the dir).
    find "$dst" -mindepth 1 -delete
  else
    mkdir -p "$dst"
  fi
  tar_copy "$src" "$dst"
}

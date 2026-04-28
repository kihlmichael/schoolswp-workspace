#!/usr/bin/env bash
# Backup config Claude Code : git push et/ou archive .tar.gz horodatée.
# Usage : bash backup.sh [--git] [--archive] [--branch <name>] [--out <dir>]
# Défaut branch : pc-maison (override via $CLAUDE_BACKUP_BRANCH ou --branch)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

DO_GIT=0
DO_ARCHIVE=0
OUT_DIR="$BACKUP_DIR_DEFAULT"
BRANCH="${CLAUDE_BACKUP_BRANCH:-pc-maison}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --git) DO_GIT=1; shift ;;
    --archive) DO_ARCHIVE=1; shift ;;
    --branch) BRANCH="$2"; shift 2 ;;
    --out) OUT_DIR="$2"; shift 2 ;;
    -h|--help) sed -n '2,4p' "$0"; exit 0 ;;
    *) die "Flag inconnu : $1" ;;
  esac
done

[[ $DO_GIT -eq 1 || $DO_ARCHIVE -eq 1 ]] || die "Précise --git et/ou --archive"

require_cmd tar
check_sources
load_backupignore "$WORKSPACE_SRC"
load_backupignore "$USER_SRC"

TS="$(date +%Y%m%d-%H%M%S)"

if [[ $DO_ARCHIVE -eq 1 ]]; then
  mkdir -p "$OUT_DIR"
  ARCHIVE="$OUT_DIR/claude-config-$TS.tar.gz"
  info "Création archive : $ARCHIVE"

  STAGE="$(mktemp -d)"
  trap 'rm -rf "$STAGE"' EXIT
  TAR_DIRS=()
  [[ $HAS_WORKSPACE -eq 1 ]] && tar_copy "$WORKSPACE_SRC" "$STAGE/workspace" && TAR_DIRS+=("workspace")
  [[ $HAS_USER -eq 1 ]] && tar_copy "$USER_SRC" "$STAGE/user" && TAR_DIRS+=("user")
  tar -czf "$ARCHIVE" -C "$STAGE" "${TAR_DIRS[@]}"
  info "Archive OK ($(du -h "$ARCHIVE" | cut -f1))"
fi

if [[ $DO_GIT -eq 1 ]]; then
  require_cmd git
  [[ -d "$SYNC_DIR/.git" ]] || die "$SYNC_DIR n'est pas un repo git — lance init.sh d'abord"

  cd "$SYNC_DIR"
  info "Fetch origin"
  git fetch origin --quiet

  # Checkout ou crée la branche locale
  if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    info "Checkout branche existante : $BRANCH"
    git checkout "$BRANCH" --quiet
    git pull --ff-only --quiet || info "(pull ff-only a échoué — branche divergente, on continue)"
  elif git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
    info "Checkout branche distante : $BRANCH"
    git checkout -b "$BRANCH" "origin/$BRANCH" --quiet
  else
    info "Création nouvelle branche : $BRANCH (depuis HEAD actuel)"
    git checkout -b "$BRANCH" --quiet
  fi

  if [[ $HAS_WORKSPACE -eq 1 ]]; then
    info "Sync workspace → $SYNC_DIR/workspace/"
    tar_mirror "$WORKSPACE_SRC" "$SYNC_DIR/workspace"
  fi
  if [[ $HAS_USER -eq 1 ]]; then
    info "Sync user → $SYNC_DIR/user/"
    tar_mirror "$USER_SRC" "$SYNC_DIR/user"
  fi

  if [[ -n "$(git status --porcelain)" ]]; then
    git add .
    git -c user.email="${GIT_AUTHOR_EMAIL:-contact@michaelkihl.fr}" \
        -c user.name="${GIT_AUTHOR_NAME:-Michael KIHL}" \
        commit -m "chore: backup $TS [$BRANCH]"
    info "Push origin $BRANCH"
    git push -u origin "$BRANCH"
  else
    info "Aucun changement à commiter sur $BRANCH."
  fi
fi

info "Backup terminé."

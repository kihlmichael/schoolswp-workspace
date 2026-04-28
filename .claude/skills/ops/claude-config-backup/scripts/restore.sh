#!/usr/bin/env bash
# Restore config Claude Code depuis git ou archive.
# Usage :
#   bash restore.sh --git <repo-url> [--branch <name>] [--dry-run]
#   bash restore.sh --archive <file.tar.gz> [--dry-run]
#   bash restore.sh --local [--branch <name>] [--dry-run]
# Défaut branch : main (l'état canonique fusionné)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

MODE=""
SRC_ARG=""
DRY_RUN=0
BRANCH="${CLAUDE_RESTORE_BRANCH:-main}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --git) MODE=git; SRC_ARG="$2"; shift 2 ;;
    --archive) MODE=archive; SRC_ARG="$2"; shift 2 ;;
    --local) MODE=local; shift ;;
    --branch) BRANCH="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) sed -n '2,7p' "$0"; exit 0 ;;
    *) die "Flag inconnu : $1" ;;
  esac
done

[[ -n "$MODE" ]] || die "Précise --git <url>, --archive <file>, ou --local"
require_cmd tar

STAGE=""
TMPSTAGE=""
cleanup() { [[ -n "$TMPSTAGE" && -d "$TMPSTAGE" ]] && rm -rf "$TMPSTAGE"; }
trap cleanup EXIT

case "$MODE" in
  git)
    require_cmd git
    [[ -n "$SRC_ARG" ]] || die "URL du repo requise"
    if [[ -d "$SYNC_DIR/.git" ]]; then
      info "Repo de sync déjà présent : fetch"
      (cd "$SYNC_DIR" && git fetch origin --quiet)
    else
      info "Clone $SRC_ARG → $SYNC_DIR"
      git clone "$SRC_ARG" "$SYNC_DIR"
    fi
    info "Checkout branche : $BRANCH"
    (cd "$SYNC_DIR" && git checkout "$BRANCH" --quiet && git pull --ff-only --quiet 2>/dev/null || true)
    STAGE="$SYNC_DIR"
    ;;
  local)
    [[ -d "$SYNC_DIR" ]] || die "$SYNC_DIR absent — utilise --git ou --archive"
    info "Checkout branche locale : $BRANCH"
    (cd "$SYNC_DIR" && git checkout "$BRANCH" --quiet)
    STAGE="$SYNC_DIR"
    ;;
  archive)
    [[ -f "$SRC_ARG" ]] || die "Archive introuvable : $SRC_ARG"
    TMPSTAGE="$(mktemp -d)"
    STAGE="$TMPSTAGE"
    info "Extraction → $STAGE"
    tar -xzf "$SRC_ARG" -C "$STAGE"
    ;;
esac

[[ -d "$STAGE/workspace" ]] || die "Structure invalide : $STAGE/workspace absent"
[[ -d "$STAGE/user" ]] || die "Structure invalide : $STAGE/user absent"

restore_one() {
  local src="$1" dst="$2"
  info "Restore $dst"
  if [[ $DRY_RUN -eq 1 ]]; then
    (cd "$src" && find . -type f | head -50 | sed 's|^\./|  + |')
    local total
    total=$(cd "$src" && find . -type f | wc -l)
    info "  ... $total fichiers seraient copiés (preview 50 max)"
  else
    mkdir -p "$dst"
    tar -C "$src" -cf - . | tar -C "$dst" -xf -
  fi
}

[[ $DRY_RUN -eq 1 ]] && info "MODE DRY-RUN — aucune écriture"

restore_one "$STAGE/workspace" "$WORKSPACE_SRC"
restore_one "$STAGE/user" "$USER_SRC"

info "Restore terminé."
[[ $DRY_RUN -eq 0 ]] && info "Redémarre Claude Code pour recharger skills/settings."

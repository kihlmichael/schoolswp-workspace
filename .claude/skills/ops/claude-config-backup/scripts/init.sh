#!/usr/bin/env bash
# Setup initial du repo git privé pour sync claude-config.
# Usage : bash init.sh <github-user> <repo-name>

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

[[ $# -eq 2 ]] || die "Usage: $0 <github-user> <repo-name>"
GH_USER="$1"
REPO_NAME="$2"

require_cmd git
require_cmd tar
check_sources

if [[ -d "$SYNC_DIR/.git" ]]; then
  die "$SYNC_DIR existe déjà avec un repo git. Supprime-le (via 'trash') ou utilise backup.sh --git."
fi

info "Création du dossier de sync : $SYNC_DIR"
mkdir -p "$SYNC_DIR"

info "Écriture du .gitignore sécurisé"
cat > "$SYNC_DIR/.gitignore" <<'EOF'
# Secrets — NE JAMAIS commiter
.env
.env.local
.env.*
!.env.example
.mcp.json
settings.local.json
*.key
*.pem
*.token
credentials.json

# OS/IDE junk
.DS_Store
Thumbs.db
node_modules/
EOF

info "Copie initiale workspace → $SYNC_DIR/workspace/"
tar_mirror "$WORKSPACE_SRC" "$SYNC_DIR/workspace"

info "Copie initiale user → $SYNC_DIR/user/"
tar_mirror "$USER_SRC" "$SYNC_DIR/user"

info "Init git"
cd "$SYNC_DIR"
git init -b main >/dev/null
git add .
git -c user.email="${GIT_AUTHOR_EMAIL:-contact@michaelkihl.fr}" \
    -c user.name="${GIT_AUTHOR_NAME:-Michael KIHL}" \
    commit -m "chore: initial claude config snapshot" >/dev/null

if command -v gh >/dev/null 2>&1; then
  info "Création du repo GitHub privé via gh CLI"
  gh repo create "$GH_USER/$REPO_NAME" --private --source=. --remote=origin --push
else
  info "gh CLI absent — crée le repo manuellement sur github.com puis :"
  echo "    cd $SYNC_DIR"
  echo "    git remote add origin git@github.com:$GH_USER/$REPO_NAME.git"
  echo "    git push -u origin main"
fi

info "Init terminé. Prochain backup : bash backup.sh --git"

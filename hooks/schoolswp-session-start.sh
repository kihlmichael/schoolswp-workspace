#!/bin/bash
# ~/.claude/hooks/schoolswp-session-start.sh
# Hook SessionStart — Charge automatiquement le contexte schoolsWP
# 
# Ce script s'exécute à chaque démarrage/reprise de session Claude Code.
# Il injecte le contexte projet dans la conversation via additionalContext.

# --- Fonctions utilitaires ---

get_git_context() {
  if git rev-parse --is-inside-work-tree &>/dev/null; then
    local branch=$(git branch --show-current 2>/dev/null || echo "detached")
    local status=$(git status --short 2>/dev/null | head -10)
    local recent_commits=$(git log --oneline -5 2>/dev/null)
    echo "## Git"
    echo "Branche : $branch"
    if [ -n "$status" ]; then
      echo "Fichiers modifiés :"
      echo "$status"
    else
      echo "Working tree propre."
    fi
    echo ""
    echo "Derniers commits :"
    echo "$recent_commits"
  fi
}

get_editorial_calendar() {
  # Cherche un fichier de calendrier éditorial dans le projet
  local cal_files=(
    ".claude/tasks/session-current.md"
    "content/calendar.md"
    "editorial-calendar.md"
    ".claude/editorial-calendar.md"
  )
  for f in "${cal_files[@]}"; do
    if [ -f "$f" ]; then
      echo "## Calendrier éditorial"
      head -30 "$f"
      echo ""
      return
    fi
  done
}

get_active_cocons() {
  # Cherche les cocons sémantiques en cours
  if [ -d "content/cocons" ] || [ -d "cocons" ]; then
    local cocon_dir="content/cocons"
    [ -d "cocons" ] && cocon_dir="cocons"
    echo "## Cocons sémantiques actifs"
    find "$cocon_dir" -name "*.md" -maxdepth 2 2>/dev/null | head -15
    echo ""
  fi
}

get_pending_tasks() {
  # Cherche les tâches en cours
  if [ -f ".claude/tasks/session-current.md" ]; then
    echo "## Tâches en cours"
    cat ".claude/tasks/session-current.md" | head -20
    echo ""
  fi
}

# --- Construction du contexte ---

context=""

# Toujours rappeler l'identité
context+="## Projet : schoolsWP\n"
context+="Mission : WordPress. Clair. Structuré. Utile.\n"
context+="Cible : freelances, créateurs, formateurs, entrepreneurs.\n"
context+="Écriture : schoolsWP (toujours cette casse exacte).\n\n"

# Contexte Git
git_ctx=$(get_git_context)
if [ -n "$git_ctx" ]; then
  context+="$git_ctx\n\n"
fi

# Calendrier éditorial
cal_ctx=$(get_editorial_calendar)
if [ -n "$cal_ctx" ]; then
  context+="$cal_ctx\n\n"
fi

# Cocons actifs
cocon_ctx=$(get_active_cocons)
if [ -n "$cocon_ctx" ]; then
  context+="$cocon_ctx\n\n"
fi

# Tâches en cours
task_ctx=$(get_pending_tasks)
if [ -n "$task_ctx" ]; then
  context+="$task_ctx\n\n"
fi

# Date du jour
context+="## Date : $(date '+%A %d %B %Y')\n"

# --- Output JSON pour Claude Code ---
# additionalContext est injecté dans le contexte de la conversation

echo "{\"additionalContext\": \"$(echo -e "$context" | sed 's/"/\\"/g' | tr '\n' ' ')\"}"

exit 0

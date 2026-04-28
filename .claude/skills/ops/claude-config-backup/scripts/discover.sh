#!/usr/bin/env bash
# Discover : scanne les disques Windows pour trouver tous les dossiers .claude
# et identifie workspace vs user config.
# Usage : bash discover.sh

set -uo pipefail  # pas de -e : on veut continuer même si un find échoue

echo "================================================================"
echo "  Claude Config Discovery — scan des dossiers .claude"
echo "================================================================"
echo ""

# 1. Détection du dossier utilisateur (toujours présent)
echo "## 1. Dossier utilisateur (global)"
echo ""
USER_HOME_CLAUDE="$HOME/.claude"
if [[ -d "$USER_HOME_CLAUDE" ]]; then
  SIZE=$(du -sh "$USER_HOME_CLAUDE" 2>/dev/null | cut -f1)
  NB_SKILLS=$(find "$USER_HOME_CLAUDE/skills" -maxdepth 3 -name "SKILL.md" 2>/dev/null | wc -l)
  echo "  ✅ $USER_HOME_CLAUDE ($SIZE, $NB_SKILLS skills)"
else
  echo "  ❌ $USER_HOME_CLAUDE n'existe pas"
fi
echo ""

# 2. Scan des disques pour trouver d'autres .claude
echo "## 2. Scan des disques (C:, D:, E:) — peut prendre 1-2 min..."
echo ""

FOUND=()
for DRIVE in /c /d /e /f; do
  [[ -d "$DRIVE" ]] || continue
  echo "  Scan $DRIVE ..."
  while IFS= read -r dir; do
    # Ignore les node_modules, .git, AppData Roaming/Local cache, etc.
    case "$dir" in
      */node_modules/*) continue ;;
      */.git/*) continue ;;
      */AppData/Local/*) continue ;;
      */AppData/Roaming/*) continue ;;
      */\$Recycle.Bin/*) continue ;;
      */Windows/*) continue ;;
    esac
    FOUND+=("$dir")
  done < <(find "$DRIVE" -maxdepth 8 -type d -name ".claude" 2>/dev/null)
done
echo ""

# 3. Classification
echo "## 3. Classification des dossiers trouvés"
echo ""

if [[ ${#FOUND[@]} -eq 0 ]]; then
  echo "  (aucun dossier .claude trouvé hors du dossier utilisateur)"
  echo ""
else
  echo "  Légende :"
  echo "    [USER]      → dossier utilisateur global"
  echo "    [WORKSPACE] → workspace VS Code (contient skills/ + settings.json)"
  echo "    [PROJECT]   → .claude d'un projet (dans un dossier avec package.json/pyproject.toml)"
  echo "    [OTHER]     → autre (à vérifier manuellement)"
  echo ""

  for dir in "${FOUND[@]}"; do
    # Skip le user home déjà traité
    [[ "$dir" == "$USER_HOME_CLAUDE" ]] && continue

    PARENT="$(dirname "$dir")"
    SIZE=$(du -sh "$dir" 2>/dev/null | cut -f1)
    NB_SKILLS=$(find "$dir/skills" -maxdepth 3 -name "SKILL.md" 2>/dev/null | wc -l)
    HAS_SETTINGS=$([[ -f "$dir/settings.json" ]] && echo "settings.json" || echo "")
    HAS_AGENTS=$([[ -d "$dir/agents" ]] && echo "agents/" || echo "")
    HAS_COMMANDS=$([[ -d "$dir/commands" ]] && echo "commands/" || echo "")

    # Classification heuristique
    if [[ -f "$PARENT/package.json" || -f "$PARENT/pyproject.toml" || -f "$PARENT/CLAUDE.md" ]]; then
      TYPE="[PROJECT]"
    elif [[ -d "$dir/skills" && "$NB_SKILLS" -gt 0 ]]; then
      TYPE="[WORKSPACE]"
    else
      TYPE="[OTHER]"
    fi

    echo "  $TYPE $dir"
    echo "     taille: $SIZE | skills: $NB_SKILLS | contenu: $HAS_SETTINGS $HAS_AGENTS $HAS_COMMANDS"
    echo ""
  done
fi

# 4. Recommandation
echo "================================================================"
echo "## Recommandation"
echo "================================================================"
echo ""
echo "Colle le résultat ci-dessus dans ta conversation Claude Code."
echo "On va t'aider à choisir quel dossier sauvegarder en priorité."
echo ""
echo "Points clés à noter :"
echo "  • Le dossier [USER] est TOUJOURS sauvegardé (automatique)."
echo "  • Le dossier [WORKSPACE] est celui à pointer dans le script de backup."
echo "  • Les dossiers [PROJECT] appartiennent à un projet git — à gérer séparément."
echo ""

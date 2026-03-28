#!/usr/bin/env bash
# Hook PostToolUse — Lance ruff sur les fichiers Python édités
# Exécuté après Edit ou Write sur un fichier .py

INPUT=$(cat)
FILE=$(echo "$INPUT" | python -c "
import sys, json
try:
    d = json.loads(sys.stdin.read())
    ti = d.get('tool_input', {})
    # Edit tool: file_path
    # Write tool: file_path
    print(ti.get('file_path', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# Vérifier que c'est un fichier Python
if [[ "$FILE" != *.py ]]; then
    exit 0
fi

# Vérifier que le fichier existe
if [[ ! -f "$FILE" ]]; then
    exit 0
fi

# Lancer ruff depuis le répertoire schoolswp
SCHOOLSWP="d:/VS Code/CLAUDE CODE/projects/schoolswp"
RUFF="$SCHOOLSWP/.venv/Scripts/python"

if [[ ! -f "$RUFF" ]]; then
    exit 0
fi

RESULT=$("$RUFF" -m ruff check "$FILE" 2>&1)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "⚠ ruff — problèmes détectés dans $FILE :"
    echo "$RESULT"
    # Exit 1 = avertissement (n'interrompt pas, informe Claude)
    exit 1
fi

exit 0

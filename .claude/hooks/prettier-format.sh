#!/usr/bin/env bash
# Hook PostToolUse — Lance Prettier sur les fichiers modifiés par Claude

INPUT=$(cat)
FILE=$(echo "$INPUT" | python -c "
import sys, json
try:
    d = json.loads(sys.stdin.read())
    ti = d.get('tool_input', {})
    print(ti.get('file_path', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# Extensions supportées par Prettier
PRETTIER_EXTS=".js .jsx .ts .tsx .json .css .scss .html .md .yaml .yml .graphql .gql"

# Vérifier que le fichier est renseigné
if [[ -z "$FILE" ]]; then
    exit 0
fi

# Vérifier que le fichier existe
if [[ ! -f "$FILE" ]]; then
    exit 0
fi

# Vérifier l'extension
EXT=".${FILE##*.}"
if [[ ! " $PRETTIER_EXTS " =~ " $EXT " ]]; then
    exit 0
fi

# Lancer Prettier
RESULT=$(npx prettier --write "$FILE" 2>&1)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "⚠ prettier — erreur sur $FILE :"
    echo "$RESULT"
    exit 1
fi

exit 0

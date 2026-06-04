#!/bin/bash
# Hook: PreToolUse - Block dangerous actions
# Exit 0 = allow, Exit 2 = block (stderr message shown to Claude)
#
# Place in: .claude/hooks/dangerous-actions-blocker.sh
# Register in: .claude/settings.json under PreToolUse event

# Auto-detect jq via winget on Windows if not already in PATH
command -v jq >/dev/null 2>&1 || { for p in "$HOME"/AppData/Local/Microsoft/WinGet/Packages/jqlang.jq*; do [ -d "$p" ] && export PATH="$p:$PATH" && break; done; }

set -e

# Read JSON from stdin
INPUT=$(cat)

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input // empty')

# === BASH: Dangerous commands ===
if [[ "$TOOL_NAME" == "Bash" ]]; then
    COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')

    # Dangerous patterns
    DANGEROUS_PATTERNS=(
        "rm -rf /"
        "rm -rf ~"
        "rm -rf \$HOME"
        "dd if="
        "mkfs"
        ":(){:|:&};:"          # Fork bomb
        "> /dev/sda"
        "chmod -R 777 /"
        "chown -R"
        "sudo rm"
        "DROP DATABASE"
        "DROP TABLE"
        "--no-preserve-root"
    )

    for pattern in "${DANGEROUS_PATTERNS[@]}"; do
        if [[ "$COMMAND" == *"$pattern"* ]]; then
            echo "BLOCKED: Dangerous command detected: '$pattern'" >&2
            exit 2
        fi
    done

    # Block force push to main/master
    if echo "$COMMAND" | grep -qE "git push.*(-f|--force).*(main|master)"; then
        echo "BLOCKED: Force push to main/master is forbidden" >&2
        exit 2
    fi

    # Block npm publish without confirmation
    if echo "$COMMAND" | grep -qE "npm publish|pnpm publish|yarn publish"; then
        echo "BLOCKED: Package publication requires manual confirmation" >&2
        exit 2
    fi

    # Check for potential secrets in command
    SECRET_PATTERNS=(
        "password="
        "secret="
        "api_key="
        "apikey="
        "token="
        "aws_access_key"
        "aws_secret"
        "private_key"
    )

    for pattern in "${SECRET_PATTERNS[@]}"; do
        if echo "$COMMAND" | grep -qi "$pattern"; then
            echo "BLOCKED: Potential secret detected in command: '$pattern'" >&2
            exit 2
        fi
    done
fi

# === EDIT/WRITE: Sensitive files ===
if [[ "$TOOL_NAME" == "Edit" || "$TOOL_NAME" == "Write" ]]; then
    FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.file_path // empty')

    # Protected files
    PROTECTED_FILES=(
        ".env"
        ".env.local"
        ".env.production"
        ".env.development"
        "credentials.json"
        "serviceAccountKey.json"
        "id_rsa"
        "id_ed25519"
        "id_ecdsa"
        ".npmrc"
        ".pypirc"
        "secrets.yml"
        "secrets.yaml"
    )

    FILENAME=$(basename "$FILE_PATH")
    for protected in "${PROTECTED_FILES[@]}"; do
        if [[ "$FILENAME" == "$protected" ]]; then
            echo "BLOCKED: Editing sensitive file '$FILENAME' is forbidden" >&2
            exit 2
        fi
    done

    # Normalize a path for cross-platform comparison:
    #  - backslashes -> forward slashes
    #  - leading Windows drive "X:/..." -> git-bash "/x/..." (drive lowercased)
    # Without this, on Windows the harness sends "C:\Users\..." while the
    # allowed prefixes are git-bash style ("/c/Users/..."), so they never match
    # and edits to ~/.claude (memory, plans, settings) get wrongly blocked.
    normpath() {
        local p="${1//\\//}"
        if [[ "$p" =~ ^([A-Za-z]):/(.*)$ ]]; then
            local drive="${BASH_REMATCH[1],,}"
            p="/${drive}/${BASH_REMATCH[2]}"
        fi
        printf '%s' "$p"
    }

    # Block editing outside project (with configurable exceptions)
    PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
    CLAUDE_HOME="${HOME}/.claude"

    # Allowed paths (configurable via environment variable)
    # Format: colon-separated paths - e.g., ALLOWED_PATHS="/custom/path:/other/path"
    EXTRA_ALLOWED="${ALLOWED_PATHS:-}"

    NORM_FILE=$(normpath "$FILE_PATH")

    # Check if path is allowed
    is_allowed=false

    # Current project
    [[ "$NORM_FILE" == "$(normpath "$PROJECT_DIR")"* ]] && is_allowed=true

    # Claude Code directory (~/.claude/) - plans, logs, settings
    [[ "$NORM_FILE" == "$(normpath "$CLAUDE_HOME")"* ]] && is_allowed=true

    # Temporary files
    [[ "$NORM_FILE" == "/tmp"* ]] && is_allowed=true

    # Additional configured paths. Normalize drive letters first
    # (X:/ -> /x/) so the ':' separator is unambiguous next to Windows
    # drive colons, then split.
    if [[ -n "$EXTRA_ALLOWED" ]]; then
        EXTRA_NORM="${EXTRA_ALLOWED//\\//}"
        EXTRA_NORM=$(printf '%s' "$EXTRA_NORM" | sed -E 's#(^|:)([A-Za-z]):/#\1/\L\2/#g')
        IFS=':' read -ra EXTRA_PATHS <<< "$EXTRA_NORM"
        for allowed_path in "${EXTRA_PATHS[@]}"; do
            [[ -n "$allowed_path" && "$NORM_FILE" == "$allowed_path"* ]] && is_allowed=true
        done
    fi

    if [[ "$is_allowed" == "false" ]]; then
        echo "BLOCKED: Editing outside project is forbidden: $FILE_PATH" >&2
        echo "Allowed paths: $PROJECT_DIR, $CLAUDE_HOME, /tmp" >&2
        [[ -n "$EXTRA_ALLOWED" ]] && echo "Additional allowed: $EXTRA_ALLOWED" >&2
        exit 2
    fi
fi

# === DELETE: Always warn ===
if [[ "$TOOL_NAME" == "Bash" ]]; then
    COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')
    if echo "$COMMAND" | grep -qE "rm -r|rmdir|unlink"; then
        # Warning but not blocking (exit 0)
        echo '{"systemMessage": "Warning: File deletion detected. Verify this is intentional."}'
    fi
fi

# Allow by default
exit 0

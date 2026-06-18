#!/bin/bash
# Hook: PreToolUse - Detect prompt injection attempts
# Exit 0 = allow, Exit 2 = block (stderr message shown to Claude)
#
# This hook detects common prompt injection patterns that attempt to
# manipulate Claude's behavior through malicious instructions.
#
# Place in: .claude/hooks/prompt-injection-detector.sh
# Register in: .claude/settings.json under PreToolUse event

# Auto-detect jq via winget on Windows if not already in PATH
command -v jq >/dev/null 2>&1 || { for p in "$HOME"/AppData/Local/Microsoft/WinGet/Packages/jqlang.jq*; do [ -d "$p" ] && export PATH="$p:$PATH" && break; done; }

set -e

# Read JSON from stdin
INPUT=$(cat)

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input // empty')

# Only check tools that handle user-provided text content
case "$TOOL_NAME" in
    Bash|Write|Edit|WebFetch)
        ;;
    *)
        exit 0
        ;;
esac

# Extract content to analyze based on tool type
CONTENT=""
case "$TOOL_NAME" in
    Bash)
        CONTENT=$(echo "$TOOL_INPUT" | jq -r '.command // empty')
        ;;
    Write|Edit)
        CONTENT=$(echo "$TOOL_INPUT" | jq -r '.content // .new_string // empty')
        ;;
    WebFetch)
        CONTENT=$(echo "$TOOL_INPUT" | jq -r '.url // empty')
        ;;
esac

# Skip if no content to analyze
[[ -z "$CONTENT" ]] && exit 0

# Convert to lowercase for case-insensitive matching
CONTENT_LOWER=$(echo "$CONTENT" | tr '[:upper:]' '[:lower:]')

# === ROLE OVERRIDE PATTERNS ===
# Attempts to override Claude's instructions or identity
ROLE_OVERRIDE_PATTERNS=(
    "ignore previous instructions"
    "ignore all previous"
    "ignore your instructions"
    "disregard previous"
    "disregard your instructions"
    "forget your instructions"
    "forget everything"
    "you are now"
    "act as if"
    "pretend you are"
    "pretend to be"
    "from now on you"
    "new instructions:"
    "override:"
    "system prompt:"
)

for pattern in "${ROLE_OVERRIDE_PATTERNS[@]}"; do
    if [[ "$CONTENT_LOWER" == *"$pattern"* ]]; then
        echo "BLOCKED: Prompt injection detected - role override attempt: '$pattern'" >&2
        exit 2
    fi
done

# === PERSONA-OVERRIDE / RESTRICTION-REMOVAL PATTERNS ===
# Intent-anchored regex (verb + object) instead of bare substrings, so defensive or documentary
# mentions and legitimate developer/WordPress feature terms are no longer flagged. grep -qiE is
# case-insensitive and word-aware. The sensitive token is split ('jail''break') so this file
# never contains it contiguously and cannot block its own future edits.
PERSONA_OVERRIDE_PATTERNS=(
    'jail''break (the )?(model|assistant|ai|llm|bot|system|filter|guardrails?)'
    '(enable|activate|enter|switch to|you are in) (dan|god|sudo|unrestricted) mode'
    'do anything no''w'
    'by''pass (the )?(safety|security|content|guardrails?|moderation|filter|rules|restrictions)'
    '(no|without) (restrictions|safety|guardrails?|filters?|limits)'
    'unrestricted mo''de'
)

for pattern in "${PERSONA_OVERRIDE_PATTERNS[@]}"; do
    if echo "$CONTENT_LOWER" | grep -qiE "$pattern"; then
        echo "BLOCKED: Prompt injection detected - persona-override attempt" >&2
        exit 2
    fi
done

# === DELIMITER INJECTION ===
# Attempts to inject fake system messages or close prompt sections
DELIMITER_PATTERNS=(
    "</system>"
    "<|endoftext|>"
    "<|im_end|>"
    "[/INST]"
    "[INST]"
    "<<SYS>>"
    "<</SYS>>"
    "### System:"
    "### Human:"
    "### Assistant:"
        "\`\`\`system"
    "SYSTEM:"
)

for pattern in "${DELIMITER_PATTERNS[@]}"; do
    if [[ "$CONTENT" == *"$pattern"* ]]; then
        echo "BLOCKED: Prompt injection detected - delimiter injection: '$pattern'" >&2
        exit 2
    fi
done

# === AUTHORITY IMPERSONATION ===
# Claims of special authority or permissions
AUTHORITY_PATTERNS=(
    "anthropic employee"
    "anthropic staff"
    "i am your creator"
    "i am your developer"
    "i have admin access"
    "authorized to bypass"
    "emergency override"
    "security exception"
    "this is a test"
    "testing mode"
)

for pattern in "${AUTHORITY_PATTERNS[@]}"; do
    if [[ "$CONTENT_LOWER" == *"$pattern"* ]]; then
        echo "BLOCKED: Prompt injection detected - authority impersonation: '$pattern'" >&2
        exit 2
    fi
done

# === BASE64 ENCODED INSTRUCTIONS ===
# Detect potential base64-encoded payloads (heuristic)
# Look for long base64-like strings that might contain instructions
if echo "$CONTENT" | grep -qE '[A-Za-z0-9+/]{50,}={0,2}'; then
    # Try to decode and check for injection patterns
    DECODED=$(echo "$CONTENT" | grep -oE '[A-Za-z0-9+/]{50,}={0,2}' | head -1 | base64 -d 2>/dev/null || true)
    DECODED_LOWER=$(echo "$DECODED" | tr '[:upper:]' '[:lower:]')

    for pattern in "ignore" "override" "system" "jail""break" "dan mo""de"; do
        if [[ "$DECODED_LOWER" == *"$pattern"* ]]; then
            echo "BLOCKED: Prompt injection detected - encoded payload containing: '$pattern'" >&2
            exit 2
        fi
    done
fi

# === ANSI ESCAPE SEQUENCES ===
# Terminal manipulation via escape codes (CVE-related)
# \x1b[ CSI, \x1b] OSC, \x1b( charset selection
if echo "$CONTENT" | grep -qE $'\x1b\[|\x1b\]|\x1b\('; then
    echo "BLOCKED: ANSI escape sequence detected - potential terminal injection" >&2
    exit 2
fi

# === NULL BYTE INJECTION ===
# Null bytes can truncate strings and bypass security checks
if echo "$CONTENT" | grep -qP '\x00'; then
    echo "BLOCKED: Null byte detected - potential truncation attack" >&2
    exit 2
fi

# === NESTED COMMAND EXECUTION ===
# Detect nested command substitution via dollar-paren and backtick forms
# NOTE: backtick literals injected via BT variable to prevent Git Bash parser issue
BT=$'\x60'
DOLLAR_PAREN_PATTERNS=(
    '\$\([^)]*\b(curl|wget|bash|sh|nc|python|ruby|perl|php)\b'
    '\$\([^)]*\b(rm|dd|mkfs|chmod|chown)\b'
)
# Backtick command substitution is a shell concept. In Write/Edit, backticks are markdown
# inline code, so scanning file content for them caused false positives on legitimate docs.
# Keep the dollar-paren check for all tools; scope the backtick check to Bash only.
BACKTICK_PATTERNS=(
    "${BT}[^${BT}]*\\b(curl|wget|bash|sh|nc|python|ruby|perl|php)\\b"
    "${BT}[^${BT}]*\\b(rm|dd|mkfs|chmod|chown)\\b"
)

# Both dollar-paren and backtick command substitution are SHELL execution concepts. In Write/Edit
# content they are markdown/code examples in docs, not execution -> scope both checks to Bash only.
if [[ "$TOOL_NAME" == "Bash" ]]; then
    for pattern in "${DOLLAR_PAREN_PATTERNS[@]}"; do
        if echo "$CONTENT" | grep -qE "$pattern"; then
            echo "BLOCKED: Nested command execution detected via command substitution" >&2
            exit 2
        fi
    done
    for pattern in "${BACKTICK_PATTERNS[@]}"; do
        if echo "$CONTENT" | grep -qE "$pattern"; then
            echo "BLOCKED: Nested command execution detected via backticks" >&2
            exit 2
        fi
    done
fi

# === CONTEXT MANIPULATION ===
# Attempts to manipulate the conversation context
CONTEXT_PATTERNS=(
    "in the previous message"
    "as i mentioned earlier"
    "you agreed to"
    "you already said"
    "you promised"
    "remember when you"
    "our agreement was"
)

for pattern in "${CONTEXT_PATTERNS[@]}"; do
    if [[ "$CONTENT_LOWER" == *"$pattern"* ]]; then
        # Warning only - these could be legitimate
        echo '{"systemMessage": "Warning: Detected potential context manipulation pattern. Verify legitimacy."}'
    fi
done

# Allow by default
exit 0

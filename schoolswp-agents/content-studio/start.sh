#!/usr/bin/env bash
# ============================================
#  Content Studio — schoolsWP Agent
#  Lance Claude Code avec le channel Telegram
# ============================================

AGENT_DIR="D:/VS Code/CLAUDE CODE/projects/schoolswp/schoolswp-agents/content-studio"
export TELEGRAM_STATE_DIR="${AGENT_DIR}/.claude/channels/telegram"

cd "$AGENT_DIR" || exit 1

claude --dangerously-skip-permissions --channels plugin:telegram@claude-plugins-official

@echo off
REM ============================================
REM  Content Studio — schoolsWP Agent
REM  Lance Claude Code avec le channel Telegram
REM ============================================

set AGENT_DIR=D:\VS Code\CLAUDE CODE\projects\schoolswp\schoolswp-agents\content-studio
set TELEGRAM_STATE_DIR=%AGENT_DIR%\.claude\channels\telegram

cd /d "%AGENT_DIR%"

claude --dangerously-skip-permissions --channels plugin:telegram@claude-plugins-official

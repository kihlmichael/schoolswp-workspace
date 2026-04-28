#!/bin/sh
export PATH="$HOME/.local/bin:/usr/bin:/bin"
echo "=== status ==="
voice-mode status 2>&1 | head -60
echo ""
echo "=== service --help ==="
voice-mode service --help 2>&1 | head -40

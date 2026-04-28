#!/bin/sh
echo "=== .bashrc lines with OPENAI (key redacted) ==="
grep -n "OPENAI" /root/.bashrc | sed 's/=.*/=<redacted>/'
echo ""
echo "=== Is it exported via 'export'? ==="
grep -c "^export OPENAI_API_KEY" /root/.bashrc
echo ""
echo "=== Test: does sourcing .bashrc via bash propagate it? ==="
bash -c 'source /root/.bashrc > /dev/null 2>&1; if [ -n "$OPENAI_API_KEY" ]; then echo "OPENAI_API_KEY is set (len=${#OPENAI_API_KEY})"; else echo "OPENAI_API_KEY NOT set"; fi'
echo ""
echo "=== Launcher shebang ==="
head -3 /root/start-voicemode.sh

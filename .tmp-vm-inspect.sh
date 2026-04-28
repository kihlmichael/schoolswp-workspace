#!/bin/sh
echo "=== start-voicemode.sh ==="
cat /root/start-voicemode.sh 2>&1
echo ""
echo "=== OPENAI in voicemode.env ==="
grep -c "^OPENAI_API_KEY=" /root/.voicemode/voicemode.env 2>/dev/null || echo 0
echo ""
echo "=== OPENAI in /root/.bashrc / .profile ==="
grep -l "OPENAI_API_KEY" /root/.bashrc /root/.profile /root/.bash_profile 2>/dev/null

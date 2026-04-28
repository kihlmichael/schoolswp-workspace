#!/bin/sh
export PATH="$HOME/.local/bin:/usr/bin:/bin"
echo "=== voicemode log files ==="
ls -lat /root/.voicemode/logs/ 2>/dev/null | head -10
echo ""
echo "=== latest voicemode.log tail ==="
find /root/.voicemode/logs -name "*.log" -type f -printf "%T@ %p\n" | sort -n | tail -3 | awk '{print $2}' | while read f; do
  echo "--- $f ---"
  tail -40 "$f"
done
echo ""
echo "=== latest event log (structured) ==="
find /root/.voicemode/logs/events -type f -printf "%T@ %p\n" 2>/dev/null | sort -n | tail -1 | awk '{print $2}' | while read f; do
  echo "--- $f ---"
  tail -30 "$f"
done

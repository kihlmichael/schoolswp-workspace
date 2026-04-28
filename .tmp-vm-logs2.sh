#!/bin/sh
echo "=== Latest converse events (last 30) ==="
find /root/.voicemode/logs/events -type f -printf "%T@ %p\n" 2>/dev/null | sort -n | tail -1 | awk '{print $2}' | while read f; do
  tail -30 "$f"
done
echo ""
echo "=== Source state LIVE while parecord warms it up ==="
(parecord --rate=16000 --channels=1 --format=s16le /tmp/warm.raw >/dev/null 2>&1) &
sleep 0.3
pactl list short sources
sleep 0.5
kill %1 2>/dev/null
wait 2>/dev/null
echo ""
echo "=== Source state after (should go SUSPENDED again) ==="
sleep 0.5
pactl list short sources

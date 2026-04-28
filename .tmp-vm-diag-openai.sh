#!/bin/sh
set -a
. /root/.voicemode/voicemode.env
set +a

echo "=== Key shape check (no value leak) ==="
if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "KEY=MISSING"
else
  echo "KEY=present len=${#OPENAI_API_KEY}"
  # First 3 + last 3 to see if it's wrapped in quotes or has hidden chars
  FIRST=$(printf '%s' "$OPENAI_API_KEY" | head -c 3)
  LAST=$(printf '%s' "$OPENAI_API_KEY" | tail -c 3)
  echo "PREFIX3=$FIRST (should be 'sk-' usually)"
  echo "SUFFIX3=...$LAST"
  # Check for quotes or CR
  printf '%s' "$OPENAI_API_KEY" | od -c | tail -2
fi

echo ""
echo "=== Minimal TTS curl to OpenAI (returns HTTP code + first 200 bytes body) ==="
curl -s -o /tmp/tts-out.mp3 -w "HTTP_CODE=%{http_code}\nSIZE=%{size_download}\n" \
  -X POST https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"tts-1","input":"bonjour","voice":"alloy","response_format":"mp3"}'
echo "=== body (if error, JSON) ==="
head -c 300 /tmp/tts-out.mp3 2>/dev/null; echo ""
file /tmp/tts-out.mp3 2>/dev/null || true

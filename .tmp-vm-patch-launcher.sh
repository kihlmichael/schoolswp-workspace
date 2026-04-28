#!/bin/sh
set -eu
TARGET=/root/start-voicemode.sh
BACKUP=/root/start-voicemode.sh.bak

if [ ! -f "$BACKUP" ]; then
  cp "$TARGET" "$BACKUP"
  echo "backup_created=$BACKUP"
else
  echo "backup_exists=$BACKUP"
fi

cat > "$TARGET" <<'EOF'
#!/bin/bash
# source bashrc (best effort; may return early for non-interactive shells)
source /root/.bashrc 2>/dev/null || true
# unconditionally load voicemode env (export all assignments)
if [ -f /root/.voicemode/voicemode.env ]; then
  set -a
  . /root/.voicemode/voicemode.env
  set +a
fi
exec /root/.local/bin/voicemode
EOF
chmod +x "$TARGET"

echo "=== new launcher ==="
cat "$TARGET"

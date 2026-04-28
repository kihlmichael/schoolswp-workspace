#!/bin/sh
echo "=== WSLg runtime dir ==="
ls -la /mnt/wslg/runtime-dir/pulse/ 2>/dev/null || echo "NO_WSLG_PULSE"
echo ""
echo "=== Env XDG_RUNTIME_DIR / PULSE ==="
echo "XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR"
echo "PULSE_SERVER=$PULSE_SERVER"
echo ""
echo "=== ALSA devices ==="
cat /proc/asound/cards 2>/dev/null || echo "NO_ALSA_CARDS"
aplay -l 2>&1 | head -10
echo ""
echo "=== pactl availability ==="
which pactl
pactl info 2>&1 | head -10
echo ""
echo "=== is pipewire/pulseaudio client installed ==="
dpkg -l 2>/dev/null | grep -E "pulseaudio|pipewire|wslg" | head -5

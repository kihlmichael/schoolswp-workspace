#!/bin/sh
echo "=== All pulse sources ==="
pactl list short sources 2>&1
echo ""
echo "=== ALSA cards ==="
cat /proc/asound/cards 2>/dev/null || echo "no /proc/asound/cards"
echo ""
echo "=== Python sounddevice enum (what voicemode sees) ==="
/root/.local/share/uv/tools/voice-mode/bin/python3 -c "
import sounddevice as sd
print('default_input_device:', sd.default.device)
print('---devices---')
for i, d in enumerate(sd.query_devices()):
    mark = ' <-- default' if i == sd.default.device[0] else ''
    print(f'[{i}] {d[\"name\"]} ch_in={d[\"max_input_channels\"]} sr={d[\"default_samplerate\"]:.0f}{mark}')
print('---hostapis---')
for i, h in enumerate(sd.query_hostapis()):
    print(f'[{i}] {h[\"name\"]} default_in={h[\"default_input_device\"]}')
" 2>&1

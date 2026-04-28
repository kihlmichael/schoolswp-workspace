#!/bin/sh
echo "=== Pulse sources (input devices = micros) ==="
pactl list short sources 2>&1
echo ""
echo "=== Pulse default source ==="
pactl info 2>&1 | grep -i "default source"
echo ""
echo "=== OPENAI_API_KEY available to shell ==="
set -a
. /root/.voicemode/voicemode.env 2>/dev/null
set +a
test -n "$OPENAI_API_KEY" && echo "OPENAI key ready" || echo "OPENAI key MISSING"
echo ""
echo "=== Record 3s from default source, see if any audio captured ==="
parecord --channels=1 --rate=16000 --format=s16le /tmp/mictest.raw 2>&1 &
PID=$!
sleep 3
kill $PID 2>/dev/null
ls -la /tmp/mictest.raw 2>/dev/null
echo "bytes captured: $(stat -c%s /tmp/mictest.raw 2>/dev/null)"
# compute RMS amplitude to see if silence
python3 -c "
import struct
with open('/tmp/mictest.raw','rb') as f:
    data = f.read()
n = len(data) // 2
if n == 0:
    print('EMPTY')
else:
    samples = struct.unpack('<%dh' % n, data[:n*2])
    rms = (sum(s*s for s in samples) / n) ** 0.5
    peak = max(abs(s) for s in samples)
    print(f'samples={n} rms={rms:.1f} peak={peak} (rms>500 = non-silent)')
" 2>&1

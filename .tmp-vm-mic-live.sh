#!/bin/sh
echo ">>> Parle FORT maintenant, compte jusqu'a 5 (4 secondes)..."
parecord --channels=1 --rate=16000 --format=s16le /tmp/live.raw &
PID=$!
sleep 4
kill $PID 2>/dev/null
wait $PID 2>/dev/null
echo ""
echo "=== Analyse ==="
python3 -c "
import struct
with open('/tmp/live.raw','rb') as f:
    data = f.read()
n = len(data) // 2
samples = struct.unpack('<%dh' % n, data[:n*2])
rms = (sum(s*s for s in samples) / n) ** 0.5 if n else 0
peak = max(abs(s) for s in samples) if n else 0
print(f'samples={n} duration={n/16000:.1f}s rms={rms:.0f} peak={peak}')
print('>>> rms < 100: silence. rms 100-500: bruit ambiant. rms > 500: voix OK <<<')
"

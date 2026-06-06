import sys
src = sys.argv[1]
prefix = sys.argv[2]
chunk_size = 18000
with open(src, 'r', encoding='ascii') as f:
    data = f.read()
n = 0
for i in range(0, len(data), chunk_size):
    with open(f"{prefix}.{n:02d}", 'w', encoding='ascii', newline='') as out:
        out.write(data[i:i+chunk_size])
    n += 1
print(f"{n} chunks, total {len(data)} chars")

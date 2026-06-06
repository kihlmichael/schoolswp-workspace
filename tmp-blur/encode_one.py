import base64, sys
with open(sys.argv[1], 'rb') as f:
    print(base64.b64encode(f.read()).decode('ascii'), end='')

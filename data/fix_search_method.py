"""
Fix Rechercher Images:
- searchMethod → 'query' (raw Drive API query, not name search)
- Update folder IDs (01_A faire / 02_Terminé)
"""
import sys, json, urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8')

with open('.mcp.json') as f:
    cfg = json.load(f)
srv = cfg['mcpServers']['n8n-mcp']['env']
BASE = srv['N8N_API_URL'].rstrip('/')
KEY  = srv['N8N_API_KEY']
HEADERS = {
    'X-N8N-API-KEY': KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

def api(method, path, body=None):
    data = json.dumps(body, ensure_ascii=False).encode('utf-8') if body else None
    req = urllib.request.Request(f'{BASE}{path}', data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f'ERROR {e.code}: {e.read().decode()[:400]}'); return None

wf = api('GET', '/api/v1/workflows/nmXNUqXgmKVcrjsJ')
nodes = wf['nodes']
node_map = {n['name']: i for i, n in enumerate(nodes)}

# ── 1. Fix Rechercher Images — search method + query ──────────────────────────
idx = node_map['Rechercher Images']
nodes[idx]['parameters'] = {
    "resource": "fileFolder",
    "searchMethod": "query",         # use raw Drive API query (not name search)
    "queryString": '="{{ $json.sourceFolderId }}" in parents and mimeType contains \'image/\' and trashed = false',
    "returnAll": True,               # get all images, no limit
    "filter": {},
    "options": {}
}
print('  [OK] Rechercher Images: searchMethod=query, returnAll=true')

# ── 2. Update Configuration folder IDs ───────────────────────────────────────
idx = node_map['Configuration']
for a in nodes[idx]['parameters']['assignments']['assignments']:
    if a['name'] == 'sourceFolderId':
        a['value'] = '1beNcu0IOEFgPksNZKKKI8hGgsANLyIaY'   # 01_A faire
    elif a['name'] == 'destinationFolderId':
        a['value'] = '1Z_faJJyjNvwpK6eSTytbu0cKQ8Ijkflb'   # 02_Terminé
print('  [OK] Configuration: sourceFolderId=01_A faire, destinationFolderId=02_Terminé')

# ── 3. Push ───────────────────────────────────────────────────────────────────
SETTINGS_OK = {
    'executionOrder', 'callerPolicy', 'saveManualExecutions', 'errorWorkflow',
    'timezone', 'saveDataSuccessExecution', 'saveDataErrorExecution',
    'saveExecutionProgress', 'executionTimeout'
}
body = {
    'name': wf['name'],
    'nodes': nodes,
    'connections': wf['connections'],
    'settings': {k: v for k, v in wf.get('settings', {}).items() if k in SETTINGS_OK},
    'staticData': wf.get('staticData')
}
r = api('PUT', '/api/v1/workflows/nmXNUqXgmKVcrjsJ', body)
print('OK' if r else 'FAILED')

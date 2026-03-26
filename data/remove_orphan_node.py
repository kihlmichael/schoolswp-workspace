"""Remove orphaned Traiter par Batch node."""
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
before = len(wf['nodes'])

# Remove Traiter par Batch
wf['nodes'] = [n for n in wf['nodes'] if n['name'] != 'Traiter par Batch']
print(f'  Nodes: {before} → {len(wf["nodes"])}')

SETTINGS_OK = {
    'executionOrder', 'callerPolicy', 'saveManualExecutions', 'errorWorkflow',
    'timezone', 'saveDataSuccessExecution', 'saveDataErrorExecution',
    'saveExecutionProgress', 'executionTimeout'
}
body = {
    'name': wf['name'],
    'nodes': wf['nodes'],
    'connections': wf['connections'],
    'settings': {k: v for k, v in wf.get('settings', {}).items() if k in SETTINGS_OK},
    'staticData': wf.get('staticData')
}
r = api('PUT', '/api/v1/workflows/nmXNUqXgmKVcrjsJ', body)
print('OK' if r else 'FAILED')

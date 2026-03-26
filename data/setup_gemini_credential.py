"""
Create Gemini credential in n8n + update Analyser avec Gemini node to use it.
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
    data = json.dumps(body, ensure_ascii=False).encode() if body else None
    req = urllib.request.Request(f'{BASE}{path}', data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f'  {method} {path} → {e.code}: {err[:300]}')
        return None

# ── 1. Create credential — try different data shapes ─────────────────────────
GEMINI_KEY = 'AIzaSyAb8-0N3EOn_T27-L6bB9sEeRu88JcRUX0'
CRED_ID = None

# Try googlePalmApi with host
r = api('POST', '/api/v1/credentials', {
    'name': 'Gemini_Production_API',
    'type': 'googlePalmApi',
    'data': {
        'apiKey': GEMINI_KEY,
        'host': 'https://generativelanguage.googleapis.com'
    }
})
if r and r.get('id'):
    CRED_ID = r['id']
    print(f'[OK] Credential created: id={CRED_ID}, name={r["name"]}')

if not CRED_ID:
    # Fallback: httpHeaderAuth — sends key as Authorization header
    r = api('POST', '/api/v1/credentials', {
        'name': 'Gemini_Production_API',
        'type': 'httpHeaderAuth',
        'data': {
            'name': 'x-goog-api-key',
            'value': GEMINI_KEY
        }
    })
    if r and r.get('id'):
        CRED_ID = r['id']
        print(f'[OK] Credential httpHeaderAuth created: id={CRED_ID}')

if not CRED_ID:
    print('Could not create credential — will update node to use header auth inline')

# ── 2. Update Analyser avec Gemini node ──────────────────────────────────────
wf = api('GET', '/api/v1/workflows/nmXNUqXgmKVcrjsJ')
nodes = wf['nodes']
node_map = {n['name']: i for i, n in enumerate(nodes)}
idx = node_map['Analyser avec Gemini']

if CRED_ID:
    # Use the credential
    cred_type = r.get('type', 'httpHeaderAuth')
    nodes[idx]['parameters'] = {
        'method': 'POST',
        'url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
        'authentication': 'predefinedCredentialType',
        'nodeCredentialType': cred_type,
        'sendBody': True,
        'specifyBody': 'json',
        'jsonBody': '={{ JSON.stringify($json.geminiBody) }}',
        'options': {}
    }
    nodes[idx]['credentials'] = {
        cred_type: {'id': CRED_ID, 'name': 'Gemini_Production_API'}
    }
    print(f'[OK] Node updated to use credential {cred_type}')
else:
    # Fallback: keep query param but use header instead (more secure)
    nodes[idx]['parameters'] = {
        'method': 'POST',
        'url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
        'sendHeaders': True,
        'headerParameters': {
            'parameters': [
                {'name': 'x-goog-api-key', 'value': GEMINI_KEY}
            ]
        },
        'sendBody': True,
        'specifyBody': 'json',
        'jsonBody': '={{ JSON.stringify($json.geminiBody) }}',
        'options': {}
    }
    print('[OK] Node updated to use x-goog-api-key header (no credential)')

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
r2 = api('PUT', '/api/v1/workflows/nmXNUqXgmKVcrjsJ', body)
print('Workflow OK' if r2 else 'Workflow FAILED')

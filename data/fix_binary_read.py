"""
Fix Construire Requête Gemini:
- Use $helpers.getBinaryDataBuffer() to read filesystem-stored binary (n8n binaryDataMode=filesystem)
- item.binary.data.data = 'filesystem-v2' reference, not actual base64
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

# Updated code: use $helpers.getBinaryDataBuffer() for filesystem binary mode
new_code = r"""// Préparer les données pour l'appel Gemini Vision
// n8n binaryDataMode=filesystem : item.binary.data.data = référence 'filesystem-v2'
// Solution : $helpers.getBinaryDataBuffer() lit le fichier depuis le disque
const results = [];

const prompt = [
  'Analyse cette photo de vacances.',
  'Retourne UNIQUEMENT un objet JSON valide (sans bloc markdown ni texte avant/après) avec ces propriétés exactes :',
  '- city : string ou null (nom du lieu/ville reconnaissable)',
  '- city_confidence : "high", "medium" ou "low"',
  '- landmark : string ou null (monument ou lieu identifiable)',
  '- scene_description : string (description brève)',
  '- quality : objet avec sharpness, composition, lighting, visual_interest, overall (entiers 1-10)',
  '- is_duplicate_candidate : boolean',
  '- is_blurry : boolean',
  '- suggested_filename : string sans extension ni espace (ex: Paris_TourEiffel_Coucher_Soleil)'
].join(' ');

for (const item of items) {
  let imageBase64 = '';
  let mimeType = 'image/jpeg';

  if (item.binary && item.binary.data) {
    mimeType = item.binary.data.mimeType || 'image/jpeg';
    try {
      // Works for both filesystem and memory binary modes
      const buffer = await $helpers.getBinaryDataBuffer(item, 'data');
      imageBase64 = buffer.toString('base64');
    } catch (e) {
      // Last-resort fallback: memory mode where .data is already base64
      const raw = item.binary.data.data;
      if (typeof raw === 'string' && !raw.startsWith('filesystem')) {
        imageBase64 = raw;
      }
    }
  }

  results.push({
    json: {
      fileId: item.json.id || '',
      fileName: item.json.name || '',
      geminiBody: {
        contents: [{
          parts: [
            { text: prompt },
            { inline_data: { mime_type: mimeType, data: imageBase64 } }
          ]
        }]
      }
    }
  });
}

return results;"""

idx = node_map['Construire Requête Gemini']
nodes[idx]['parameters']['jsCode'] = new_code
print('  [OK] Construire Requête Gemini: using $helpers.getBinaryDataBuffer()')

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

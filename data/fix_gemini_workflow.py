"""
Fix workflow nmXNUqXgmKVcrjsJ — [Offline] Gemini: Organisateur Photos Vacances
Corrections :
1. Rename to [InDev]
2. Fix Rechercher Images queryString
3. Add "Construire Requête Gemini" Code node (extract base64 + metadata)
4. Replace Analyser avec Gemini (LangChain) → HTTP Request (Gemini Vision API)
5. Add "Fusionner Métadonnées" Merge node (combine file metadata + Gemini response)
6. Update Parser Analyse to read merged data
7. Fix Copier Meilleures Photos (add destination folderId)
8. Fix connections: remove splitInBatches from chain, wire up new nodes
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
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f'  ERROR {method} {path} → {e.code}: {err[:600]}')
        return None

# ── Fetch ─────────────────────────────────────────────────────────────────────
wf = api('GET', '/api/v1/workflows/nmXNUqXgmKVcrjsJ')
if not wf:
    print('Failed to fetch workflow'); sys.exit(1)

nodes = wf['nodes']
connections = wf['connections']
node_map = {n['name']: i for i, n in enumerate(nodes)}
print(f'Fetched: {wf["name"]}  ({len(nodes)} nodes)')

# ── 1. Rename to [InDev] ──────────────────────────────────────────────────────
wf['name'] = '[InDev] Google Drive > Gemini: Organisateur Photos Vacances'

# ── 2. Fix queryString in Rechercher Images ───────────────────────────────────
idx = node_map['Rechercher Images']
nodes[idx]['parameters']['queryString'] = \
    '="{{ $json.sourceFolderId }}" in parents and mimeType contains \'image/\''
print('  [OK] Rechercher Images queryString fixed')

# ── 3. Replace Analyser avec Gemini → HTTP Request ────────────────────────────
idx = node_map['Analyser avec Gemini']
nodes[idx] = {
    "parameters": {
        "method": "POST",
        "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        "sendQuery": True,
        "queryParameters": {
            "parameters": [
                {"name": "key", "value": "={{ $vars.GEMINI_API_KEY }}"}
            ]
        },
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify($json.geminiBody) }}",
        "options": {}
    },
    "id": "59f08225-916b-4662-9679-f0806d7d3d8c",
    "name": "Analyser avec Gemini",
    "type": "n8n-nodes-base.httpRequest",
    "typeVersion": 4.2,
    "position": [-416, 0]
}
print('  [OK] Analyser avec Gemini → HTTP Request (Gemini Vision API)')

# ── 4. Update Parser Analyse code ─────────────────────────────────────────────
idx = node_map['Parser Analyse']
nodes[idx]['parameters']['jsCode'] = r"""// Parser la réponse Gemini et préparer les données
// Note : les données fusionnées contiennent fileId/fileName (du Code node)
//        + candidates[] (de la réponse HTTP Gemini)
const results = [];

for (const item of items) {
  const data = item.json;
  let analysis;

  try {
    // Extraire le texte de la réponse Gemini HTTP API
    let responseText = '';
    if (data.candidates && data.candidates[0] &&
        data.candidates[0].content && data.candidates[0].content.parts &&
        data.candidates[0].content.parts[0]) {
      responseText = data.candidates[0].content.parts[0].text || '';
    } else if (data.text) {
      responseText = data.text;
    } else if (data.output) {
      responseText = data.output;
    }

    // Nettoyer les éventuels blocs markdown
    responseText = responseText.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
    analysis = JSON.parse(responseText);
  } catch (e) {
    analysis = {
      city: null,
      city_confidence: 'low',
      landmark: null,
      scene_description: 'unknown',
      quality: { sharpness: 5, composition: 5, lighting: 5, visual_interest: 5, overall: 5 },
      is_duplicate_candidate: false,
      is_blurry: false,
      suggested_filename: 'Photo_Non_Identifiee'
    };
  }

  // Score qualité 0-100
  const qualityScore = analysis.quality
    ? (analysis.quality.sharpness + analysis.quality.composition +
       analysis.quality.lighting + analysis.quality.visual_interest +
       analysis.quality.overall) * 2
    : 50;

  const city = analysis.city || 'Non_Classe';
  const descriptor = analysis.suggested_filename || (city + '_Photo');
  const timestamp = Date.now();
  const finalFilename = descriptor + '_' + timestamp.toString().slice(-6);

  const shouldKeep = !analysis.is_blurry && qualityScore >= 40;

  results.push({
    json: {
      originalId: data.fileId || data.id || '',
      originalName: data.fileName || data.name || '',
      city: city,
      cityConfidence: analysis.city_confidence,
      landmark: analysis.landmark,
      sceneDescription: analysis.scene_description,
      qualityScore: qualityScore,
      qualityDetails: analysis.quality,
      isBlurry: analysis.is_blurry,
      isDuplicateCandidate: analysis.is_duplicate_candidate,
      suggestedFilename: finalFilename,
      shouldKeep: shouldKeep,
      analysisRaw: analysis
    }
  });
}

return results;"""
print('  [OK] Parser Analyse code updated')

# ── 5. Fix Copier Meilleures Photos — add destinationFolderId ─────────────────
idx = node_map['Copier Meilleures Photos']
nodes[idx]['parameters']['driveId'] = {"__rl": True, "mode": "list", "value": "My Drive"}
nodes[idx]['parameters']['folderId'] = {"__rl": True, "mode": "id", "value": "={{ $json.destinationFolderId }}"}
print('  [OK] Copier Meilleures Photos folderId added')

# ── 6. Add "Construire Requête Gemini" Code node ──────────────────────────────
code_construire = {
    "parameters": {
        "jsCode": r"""// Extraire les métadonnées + image base64 pour l'appel Gemini Vision
return items.map(item => {
  const binaryField = item.binary && item.binary.data ? item.binary.data : null;
  let imageBase64 = '';
  let mimeType = 'image/jpeg';

  if (binaryField) {
    mimeType = binaryField.mimeType || 'image/jpeg';
    if (Buffer.isBuffer(binaryField.data)) {
      imageBase64 = binaryField.data.toString('base64');
    } else if (typeof binaryField.data === 'string') {
      imageBase64 = binaryField.data;
    }
  }

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

  return {
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
  };
});"""
    },
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "name": "Construire Requête Gemini",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [-640, 0]
}

# ── 7. Add "Fusionner Métadonnées" Merge node ─────────────────────────────────
merge_metadata = {
    "parameters": {
        "mode": "combine",
        "combineBy": "combineByPosition",
        "options": {}
    },
    "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "name": "Fusionner Métadonnées",
    "type": "n8n-nodes-base.merge",
    "typeVersion": 3.1,
    "position": [-192, 0]
}

nodes.append(code_construire)
nodes.append(merge_metadata)
print('  [OK] Added: Construire Requête Gemini + Fusionner Métadonnées')

# ── 8. Rebuild connections ────────────────────────────────────────────────────

# Rechercher Images → Télécharger Image (was → Traiter par Batch)
connections['Rechercher Images']['main'][0] = [
    {"node": "Télécharger Image", "type": "main", "index": 0}
]

# Télécharger Image → Construire Requête Gemini
connections['Télécharger Image'] = {
    "main": [[
        {"node": "Construire Requête Gemini", "type": "main", "index": 0}
    ]]
}

# Construire Requête Gemini → Analyser avec Gemini  +  → Fusionner Métadonnées (input 1)
connections['Construire Requête Gemini'] = {
    "main": [[
        {"node": "Analyser avec Gemini", "type": "main", "index": 0},
        {"node": "Fusionner Métadonnées", "type": "main", "index": 1}
    ]]
}

# Analyser avec Gemini → Fusionner Métadonnées (input 0)
connections['Analyser avec Gemini'] = {
    "main": [[
        {"node": "Fusionner Métadonnées", "type": "main", "index": 0}
    ]]
}

# Fusionner Métadonnées → Parser Analyse
connections['Fusionner Métadonnées'] = {
    "main": [[
        {"node": "Parser Analyse", "type": "main", "index": 0}
    ]]
}

# Orphan Traiter par Batch (remove its outgoing connections, keep the node)
connections.pop('Traiter par Batch', None)

print('  [OK] Connections updated')

# ── 9. PUT the workflow ───────────────────────────────────────────────────────
SETTINGS_OK = {
    'executionOrder', 'callerPolicy', 'saveManualExecutions', 'errorWorkflow',
    'timezone', 'saveDataSuccessExecution', 'saveDataErrorExecution',
    'saveExecutionProgress', 'executionTimeout'
}
body = {
    'name': wf['name'],
    'nodes': nodes,
    'connections': connections,
    'settings': {k: v for k, v in wf.get('settings', {}).items() if k in SETTINGS_OK},
    'staticData': wf.get('staticData')
}

print('\nPushing workflow...')
result = api('PUT', '/api/v1/workflows/nmXNUqXgmKVcrjsJ', body)
if result:
    print(f'\n=== SUCCESS ===')
    print(f'  Name    : {result.get("name")}')
    print(f'  Version : {result.get("versionId")}')
    print(f'  Nodes   : {len(result.get("nodes", []))}')
else:
    print('\n=== FAILED ===')

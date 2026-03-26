"""
n8n Workflows — Nomenclature + Tags
Renames 3 workflows non-conformes + crée et assigne les tags sur les 56.
"""
import sys, json, urllib.request, urllib.error, time
sys.stdout.reconfigure(encoding='utf-8')

# ── Config ──────────────────────────────────────────────────────────────────
with open('.mcp.json') as f:
    cfg = json.load(f)
srv = cfg['mcpServers']['n8n-mcp']['env']
BASE = srv['N8N_API_URL'].rstrip('/')
KEY  = srv['N8N_API_KEY']
HEADERS = {'X-N8N-API-KEY': KEY, 'Accept': 'application/json',
           'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}

def api(method, path, body=None):
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(f'{BASE}{path}', data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f'  !! {method} {path} → {e.code}: {e.read().decode()[:200]}')
        return None

# ── 1. Renames ────────────────────────────────────────────────────────────
RENAMES = {
    '6utQzJcmXQczrHag': '[Prod] Claude > Google Sheets: Skills Registry Sync',
    'sLsPkcU3faV727dM': '[InDev] YouTube > Kie.ai: Thumbnail Generator',
    'iXR2tvSfd5L9zE2t': '[Prod] Schedule > n8n: Workflows Backup',
}

print('=== 1. RENAMES ===')
for wid, new_name in RENAMES.items():
    wf = api('GET', f'/api/v1/workflows/{wid}')
    if not wf:
        continue
    old_name = wf['name']
    wf['name'] = new_name
    # PUT requires the full workflow object
    result = api('PUT', f'/api/v1/workflows/{wid}', wf)
    status = 'OK' if result else 'FAIL'
    print(f'  [{status}] {old_name[:50]}')
    print(f'        → {new_name}')
    time.sleep(0.3)

# ── 2. Create tags ────────────────────────────────────────────────────────
TAGS_TO_CREATE = [
    'google-drive', 'seo', 'content', 'social', 'wordpress',
    'agents', 'infra', 'youtube',
    'scheduled', 'webhook', 'manual',
    'schoolswp',
]

print('\n=== 2. TAGS ===')
existing = api('GET', '/api/v1/tags?limit=100') or {}
tag_map = {t['name']: t['id'] for t in existing.get('data', [])}

for tag_name in TAGS_TO_CREATE:
    if tag_name in tag_map:
        print(f'  [exists] {tag_name} → {tag_map[tag_name]}')
    else:
        result = api('POST', '/api/v1/tags', {'name': tag_name})
        if result:
            tag_map[tag_name] = result['id']
            print(f'  [created] {tag_name} → {result["id"]}')
        time.sleep(0.2)

print(f'\nTag map: {json.dumps(tag_map, indent=2)}')

# ── 3. Assign tags ────────────────────────────────────────────────────────
# wf_id → [tag_names]
WF_TAGS = {
    # PROD actifs
    '9bbCZznrXCD9fdz9': ['google-drive', 'agents', 'schoolswp', 'webhook'],     # Auto README New Folder
    'CDuKpLL7E6LuaWNT': ['google-drive', 'agents', 'schoolswp', 'webhook'],     # Hub Sync README
    'J3bOLPqUQg28VVVR': ['seo', 'infra', 'schoolswp', 'scheduled'],             # Thruuu Token Health
    '5jsmzak1wDosjDEy': ['infra', 'schoolswp', 'webhook'],                      # Telegram Auth Alert
    '6utQzJcmXQczrHag': ['agents', 'schoolswp', 'scheduled'],                   # Skills Registry (renamed)
    'iXR2tvSfd5L9zE2t': ['infra', 'schoolswp', 'scheduled'],                    # n8n Backup (renamed)

    # STAGING
    'DcbnlLoedzX2lVIJ': ['wordpress', 'content', 'seo', 'schoolswp', 'webhook'], # WP > Sheets Sync
    'MveNwfDlvVYYZTwz': ['google-drive', 'schoolswp', 'webhook'],                # Migration structure

    # INDEV — Google Drive
    'PkFO7Of9BrMfl8Ed': ['google-drive', 'schoolswp', 'webhook'],               # Auto-Rename on Move
    '5kqNhwathbPqLL9l': ['google-drive', 'schoolswp', 'manual'],                # Drive Audit
    'RhQO6SxIy7eJs7Bd': ['google-drive', 'schoolswp', 'webhook'],               # Migration Niveau 2
    'Vk43iCD851XyGJq9': ['google-drive', 'schoolswp', 'manual'],                # Migration arborescence

    # INDEV — SEO
    'xEkwRNNw9Mm2BUxq': ['seo', 'schoolswp', 'manual'],                         # SEO Maillage Interne
    'MyzvSuY5ZeqNemKB': ['seo', 'schoolswp', 'scheduled'],                      # GSC Rapport quotidien
    'Im1Khan3gJwhJkuu': ['seo', 'schoolswp', 'webhook'],                        # Thruuu Monitoring Results
    'YfP0L8Mc46GyjbsK': ['wordpress', 'social', 'schoolswp', 'scheduled'],      # RSS Plugin Monitor

    # INDEV — Content / Agents
    '15l8YimrlFeRxZL5': ['content', 'schoolswp', 'webhook'],                    # Content Ops Pipeline
    'DuA0mTknpwxl3n7t': ['content', 'schoolswp', 'manual'],                     # RAG Base de Connaissances
    'zcm7RCjuWyyYS9zM': ['content', 'schoolswp', 'manual'],                     # Email Extractor
    'WocLwnUAZPaZFitG': ['agents', 'schoolswp', 'webhook'],                     # Orchestrator Callback
    'uqH7WJf6y8f1AgAr': ['agents', 'schoolswp', 'webhook'],                     # Orchestrator Trigger
    'krF2AcxO9sXBimLI': ['agents', 'schoolswp', 'webhook'],                     # Claude Skills Audit Sync
    '3JE0YzrhoiusJZ6T': ['seo', 'agents', 'schoolswp', 'webhook'],              # GEO Architect Bulk Fill
    'P4riSkL0azBX7rJg': ['seo', 'agents', 'schoolswp', 'webhook'],              # GEO Architect AIO Pipeline
    '5LRZoMPjOvGtvLsr': ['agents', 'schoolswp', 'webhook'],                     # schoolsWP Brain
    'nV3pipGTnwZq7zCz': ['infra', 'schoolswp'],                                 # Global Error Handler

    # INDEV — Social / YouTube
    'mOARMmejMqpWVav2': ['social', 'schoolswp', 'manual'],                      # Créer post LinkedIn
    'rfywaXMGBoKQReln': ['social', 'schoolswp', 'manual'],                      # LinkedIn Carousel
    'DvpBgumVBQ4GxN55': ['social', 'youtube', 'schoolswp', 'scheduled'],        # Shorts Auto-Post (1)
    'g7JMn5A9uiXqgdgI': ['social', 'youtube', 'schoolswp', 'scheduled'],        # Shorts Auto-Post (2)
    'RCrxLczqjF95kVV8': ['social', 'schoolswp', 'scheduled'],                   # Social Stats
    'ls46UbBJJuZCobfI': ['youtube', 'seo', 'schoolswp', 'manual'],              # YouTube Analyse WP
    'sLsPkcU3faV727dM': ['youtube', 'schoolswp', 'manual'],                      # Thumbnail Generator (renamed)
    'esMrVGG182Wa0bxr': ['social', 'youtube', 'schoolswp', 'manual'],           # Setup Shorts CMS
    'aW9LzUdmykugYzea': ['social', 'youtube', 'schoolswp', 'manual'],           # Create Shorts CMS Sheet

    # INDEV — WordPress
    'xxm6wDQpIL4NCk4s': ['wordpress', 'schoolswp', 'webhook'],                  # SecuPress Discord

    # OFFLINE — Templates
    'FVt4dadONosJBgQQ': ['social', 'manual'],                                   # Abyssale > Blotato
    'nqZCiTjpWnTbmr0o': ['social', 'youtube', 'manual'],                        # Image > NanoBanana
    'gfOOdgck46toZsiK': ['social', 'youtube', 'manual'],                        # NanoBanana > Blotato
    'MoIYzZ5Sh0NkQZnl': ['youtube', 'social', 'manual'],                        # YouTube > Blotato

    # OFFLINE — Gemini / Maps
    'L7kTqgSDrdwSShxQ': ['google-drive', 'manual'],                             # Gemini Photos (1)
    'YHC6gRUN0yliUnN5': ['google-drive', 'manual'],                             # Gemini Photos (2)
    'nmXNUqXgmKVcrjsJ': ['google-drive', 'manual'],                             # Gemini Photos (3)
    'l1bkufQrDjkdPHkq': ['seo', 'manual'],                                      # Google Maps Reviews
    'McG5eQhjEEvOKdKj': ['infra', 'manual'],                                    # Bright Data MCP
    '2ZaeawddHVOQuapx': ['infra', 'manual'],                                    # Bright Data Unlocker
}

print('\n=== 3. TAG ASSIGNMENTS ===')
ok = fail = skip = 0
for wf_id, tag_names in WF_TAGS.items():
    tag_ids = []
    missing = []
    for tn in tag_names:
        if tn in tag_map:
            tag_ids.append({'id': tag_map[tn]})
        else:
            missing.append(tn)
    if missing:
        print(f'  [SKIP] {wf_id} — tags manquants: {missing}')
        skip += 1
        continue
    result = api('PUT', f'/api/v1/workflows/{wf_id}/tags', tag_ids)
    if result is not None:
        print(f'  [OK] {wf_id} → {tag_names}')
        ok += 1
    else:
        fail += 1
    time.sleep(0.2)

print(f'\n=== RÉSULTAT ===')
print(f'  Tags assignés : {ok}')
print(f'  Erreurs       : {fail}')
print(f'  Ignorés       : {skip}')
print(f'\n  ForDeletion à supprimer manuellement :')
print(f'    u47SqEoOLfJpM4MM — Claude Skills Audit Sync (doublon)')
print(f'    VJ6U2tOkpXjXt6ed — Thruuu Monitoring (doublon)')
print(f'\n  Incohérence statut/activité à corriger :')
print(f'    RhQO6SxIy7eJs7Bd — marqué [Offline] mais ACTIF')

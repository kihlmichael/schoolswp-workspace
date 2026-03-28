# Workspace Hygiene Report — 2026-03-25

## Etat general

**14 fichiers** detectes dans la categorie "Patch files et scripts residuels" :
- 8 `patch_*.py` a la racine
- 1 `fix_*.py` a la racine
- 5 `fix_*.py` dans `data/`
- 0 fichiers `.patch`

Tous ces scripts sont des one-shot executes via l'API REST n8n pour patcher des workflows. Aucun n'est importe ou appele par un autre module. Ils sont mentionnes dans `.claude/rules/tools-services.md` comme "scripts one-shot a la racine — ne pas relancer sans verifier". Les fichiers racine (`patch_*.py` + `fix_workflow.py`) sont dans `.gitignore`. Les fichiers `data/fix_*.py` ne le sont pas.

**Probleme de securite** : tous les scripts racine (`patch_*.py` + `fix_workflow.py`) contiennent une cle API n8n hardcodee en clair. Les scripts `data/fix_*.py` lisent la cle depuis `.mcp.json` (correct). Ce fait renforce la decision d'archiver plutot que de laisser trainer.

## Patch files et scripts residuels

### Racine — workflow `PkFO7Of9BrMfl8Ed` (Auto-Rename on Move)

Ces 8 patch + 1 fix forment une sequence chronologique de debug sur le workflow n8n "[InDev] Auto-Rename on Move". Chaque script corrige un probleme specifique du precedent. Ils sont tous appliques et obsoletes.

| Fichier | Localisation | Action proposee | Raison |
|---------|-------------|-----------------|--------|
| `patch_extract_convention.py` | racine | archive | Patch initial — remplace regex literal par `new RegExp()` dans le node "Extract Convention". Documente le contexte du workflow Drive rename. |
| `patch_staticdata.py` | racine | archive | Evolution — passe les donnees via `$workflow.staticData` entre Code nodes. Documente 5 nodes patches simultanement. |
| `patch_merge_conv.py` | racine | archive | Ajoute un node Merge pour combiner convention + fichiers. Code le plus complexe de la serie, documente le rewiring complet. |
| `patch_set_convention.py` | racine | archive | Remplace le Merge par un Set node (plus simple). Documente le changement d'architecture. |
| `patch_fix_setnode.py` | racine | trash | Micro-correction du Set node (mode `manual` + champ `files`). Minimal, pas de docstring, entierement supersede par les patches suivants. |
| `patch_claude_body.py` | racine | trash | Corrige `specifyBody` + `jsonBody` sur le node Claude. Tres court, pas de docstring, correction ponctuelle sans contexte. |
| `patch_file_context.py` | racine | archive | Ajoute le node "Add File Context" (Set node entre Generate New Name et Extract New Filename). Documente le rewiring avec la branche error. |
| `patch_error_node.py` | racine | trash | Corrige le node "Collect Error Info" (retire `.item.json.name`). Minimal, sans docstring, correction syntaxique pure. |
| `fix_workflow.py` | racine | archive | Le plus gros script (262 lignes). Restructuration complete du workflow : renommage de 5 nodes, ajout de 3 nodes, rewiring integral. Reference dans `.claude/rules/tools-services.md`. |

### `data/` — workflow `nmXNUqXgmKVcrjsJ` (Gemini Organisateur Photos)

Ces 5 fix forment une sequence de debug sur le workflow "[InDev] Google Drive > Gemini: Organisateur Photos Vacances". Chaque script a une docstring et lit la cle API depuis `.mcp.json` (pattern plus propre).

| Fichier | Localisation | Action proposee | Raison |
|---------|-------------|-----------------|--------|
| `fix_gemini_workflow.py` | `data/` | archive | Script principal (301 lignes) — restructuration complete du workflow Gemini. Docstring detaillee (8 corrections listees). Ajoute des nodes, remplace LangChain par HTTP Request. Reference active du workflow. |
| `fix_drive_query.py` | `data/` | trash | Corrige `queryString` — retire `mimeType contains` (cru invalide). Supersede immediatement par `fix_mime_query.py` qui restaure le filtre. |
| `fix_mime_query.py` | `data/` | trash | Restaure `mimeType contains 'image/'`. Correction qui annule `fix_drive_query.py`. Les deux ensemble = zero changement net. |
| `fix_search_method.py` | `data/` | archive | Corrige `searchMethod` -> `query` + met a jour les folder IDs. Docstring claire, contient des IDs de dossiers Drive reels. |
| `fix_binary_read.py` | `data/` | archive | Corrige la lecture binaire filesystem (`$helpers.getBinaryDataBuffer()`). Docstring detaillee, solution non triviale au probleme `binaryDataMode=filesystem`. |

## Plan d'action resume

1. Creer `_archive/patches/` si necessaire
2. **Archiver 9 fichiers** vers `_archive/patches/` :
   - `patch_extract_convention.py`
   - `patch_staticdata.py`
   - `patch_merge_conv.py`
   - `patch_set_convention.py`
   - `patch_file_context.py`
   - `fix_workflow.py`
   - `data/fix_gemini_workflow.py`
   - `data/fix_search_method.py`
   - `data/fix_binary_read.py`
3. **Trasher 5 fichiers** :
   - `patch_fix_setnode.py` (micro-correction supersedee)
   - `patch_claude_body.py` (micro-correction supersedee)
   - `patch_error_node.py` (correction syntaxique minimale)
   - `data/fix_drive_query.py` (annule par fix_mime_query)
   - `data/fix_mime_query.py` (annule fix_drive_query — les deux s'annulent)
4. Mettre a jour `.claude/rules/tools-services.md` pour retirer la mention des scripts racine (apres archivage)
5. Ajouter `data/fix_*.py` dans `.gitignore` (actuellement non couvert)

**Attente validation avant execution.**

# Audit : fichiers patch_*.py et fix_*.py

**Date** : 2026-03-25
**Scope** : `d:/VS Code/CLAUDE CODE/projects/schoolswp/`
**Fichiers trouves** : 14 (8 patch, 6 fix)
**Statut git** : non-tracked (`.gitignore` contient `patch_*.py` et `fix_workflow.py`)

---

## Synthese

Tous ces fichiers sont des **scripts one-shot de patching n8n** : ils appellent l'API n8n pour modifier des workflows en production via PUT. Ils contiennent des **cles API n8n en clair** (JWT). Aucun n'est un module reutilisable. Aucun n'est importe par un autre fichier du projet.

Ils se regroupent en deux chantiers distincts :

| Chantier | Workflow cible | Fichiers |
|---|---|---|
| **A** -- Auto-Rename on Move | `PkFO7Of9BrMfl8Ed` | 8 fichiers racine |
| **B** -- Gemini Organisateur Photos | `nmXNUqXgmKVcrjsJ` | 6 fichiers (`data/` + racine) |

---

## Detail par fichier

### Chantier A -- Workflow "[InDev] Auto-Rename on Move" (8 fichiers)

Ces 8 fichiers representent les iterations successives du debug d'un meme workflow n8n. Chaque fichier est une etape qui corrige ou remplace le patch precedent.

| # | Fichier | Lignes | Role | Supersede par |
|---|---------|--------|------|--------------|
| 1 | `patch_extract_convention.py` | 70 | Remplace regex literal par `new RegExp()` dans le node "Extract Convention" | #2 |
| 2 | `patch_staticdata.py` | 149 | Refactoring complet : stocke convention/folderId dans `$workflow.staticData` pour 4 nodes | #3 |
| 3 | `patch_merge_conv.py` | 178 | Retire staticData, ajoute un node Merge pour combiner convention + fichiers | #4 |
| 4 | `patch_set_convention.py` | 101 | Remplace le Merge par un Set node "Add Convention Fields" (plus simple) | #5 |
| 5 | `patch_fix_setnode.py` | 69 | Corrige le mode du Set node (v3.4 : `mode: "manual"`) | -- |
| 6 | `patch_claude_body.py` | 48 | Corrige le node "Generate New Name" : `specifyBody: "json"` + `JSON.parse()` | -- |
| 7 | `patch_file_context.py` | 116 | Ajoute le node "Add File Context" entre Claude et Extract New Filename | -- |
| 8 | `patch_error_node.py` | 55 | Corrige le node "Collect Error Info" (retire `.item.json.name` qui causait SyntaxError) | -- |

**Conclusion** : les fichiers 1-4 forment une chaine de supersession (#1 -> #2 -> #3 -> #4). Tous les 8 ont deja ete executes et appliques au workflow.

### Chantier B -- Workflow "[InDev] Gemini: Organisateur Photos Vacances" (6 fichiers)

| # | Fichier | Lignes | Role | Supersede par |
|---|---------|--------|------|--------------|
| 1 | `fix_workflow.py` | 301 | Refactoring massif du workflow Gemini (rename, queryString, nouveau node Code + Merge, rewire complet) | -- |
| 2 | `data/fix_gemini_workflow.py` | 301 | **Doublon exact fonctionnel** de `fix_workflow.py` (meme workflow ID, meme logique) -- probablement une copie deplacee | -- |
| 3 | `data/fix_drive_query.py` | 51 | Corrige le queryString de "Rechercher Images" : retire `mimeType contains` (considere invalide) | #4 |
| 4 | `data/fix_mime_query.py` | 55 | Annule #3 : restaure `mimeType contains 'image/'` (en fait valide dans Drive API) | -- |
| 5 | `data/fix_search_method.py` | 69 | Change `searchMethod` en `query`, met a jour les folder IDs (01_A faire / 02_Termine) | -- |
| 6 | `data/fix_binary_read.py` | 107 | Corrige "Construire Requete Gemini" : utilise `$helpers.getBinaryDataBuffer()` pour le mode filesystem | -- |

**Conclusion** : #3 est rendu obsolete par #4 (qui l'annule). `fix_workflow.py` et `data/fix_gemini_workflow.py` sont probablement des doublons.

---

## Problemes de securite

**Tous les fichiers du chantier A contiennent une cle API n8n en clair** (JWT hardcode ligne 4). Meme si `.gitignore` les exclut du depot, ils restent sur le disque. Les fichiers du chantier B lisent la cle depuis `.mcp.json` (plus propre).

---

## Recommandation

| Action | Fichiers | Justification |
|--------|----------|---------------|
| **Supprimer** (`trash`) | `patch_extract_convention.py` | Supersede par `patch_staticdata.py` |
| **Supprimer** (`trash`) | `patch_staticdata.py` | Supersede par `patch_merge_conv.py` |
| **Supprimer** (`trash`) | `patch_merge_conv.py` | Supersede par `patch_set_convention.py` |
| **Supprimer** (`trash`) | `patch_set_convention.py` | Supersede par `patch_fix_setnode.py` |
| **Supprimer** (`trash`) | `patch_fix_setnode.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `patch_claude_body.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `patch_file_context.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `patch_error_node.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `data/fix_drive_query.py` | Annule par `fix_mime_query.py` |
| **Supprimer** (`trash`) | `data/fix_gemini_workflow.py` | Doublon de `fix_workflow.py` |
| **Supprimer** (`trash`) | `fix_workflow.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `data/fix_mime_query.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `data/fix_search_method.py` | Applique, one-shot |
| **Supprimer** (`trash`) | `data/fix_binary_read.py` | Applique, one-shot |

**Verdict : les 14 fichiers peuvent etre supprimes.** Ce sont tous des scripts one-shot deja appliques aux workflows n8n. Aucun n'a de valeur de reference (la verite est dans les workflows n8n eux-memes). Les 8 fichiers du chantier A contiennent en plus une cle API en clair qui ne devrait pas trainer sur le disque.

### Commande de nettoyage (a executer manuellement)

```bash
cd "d:/VS Code/CLAUDE CODE/projects/schoolswp"
trash patch_extract_convention.py patch_staticdata.py patch_merge_conv.py patch_set_convention.py patch_fix_setnode.py patch_claude_body.py patch_file_context.py patch_error_node.py fix_workflow.py
trash data/fix_gemini_workflow.py data/fix_drive_query.py data/fix_mime_query.py data/fix_search_method.py data/fix_binary_read.py
```

### Suggestion preventive

Pour eviter la proliferation future, ajouter un dossier `_patches/` (gitignored) pour centraliser ce type de scripts temporaires, ou mieux : utiliser le MCP n8n (`mcp__n8n-mcp__n8n_update_partial_workflow`) au lieu de scripts Python ad hoc.

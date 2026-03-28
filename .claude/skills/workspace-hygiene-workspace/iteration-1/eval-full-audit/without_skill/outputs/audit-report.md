# Audit workspace schoolsWP -- 2026-03-25

## Resume executif

Le workspace presente un niveau de bruit significatif. Les principaux problemes : scripts jetables a la racine, fichiers orphelins, repertoire data/ melange (scripts + donnees), 40 Mo de skills archives, dossiers vides, credentials versionnees, et node_modules imbriques non-gitignored.

**Score hygiene estime : 5/10**

---

## 1. Fichiers orphelins a la racine du projet

La racine du projet contient 14 fichiers qui ne devraient pas etre la :

| Fichier | Taille | Probleme |
|---------|--------|----------|
| download.html | 0 octets | Fichier vide, aucune utilite |
| 2026-03-21_youtube_welcome-to-tutor-lms-academy.md | 2 Ko | Contenu egare |
| sync-colors.ps1 | 4 Ko | Script PowerShell non-tracked |
| fix_workflow.py | 11 Ko | Script one-shot |
| patch_claude_body.py | 1.8 Ko | Script one-shot |
| patch_error_node.py | 2 Ko | Script one-shot |
| patch_extract_convention.py | 2.6 Ko | Script one-shot |
| patch_file_context.py | 4 Ko | Script one-shot |
| patch_fix_setnode.py | 2.5 Ko | Script one-shot |
| patch_merge_conv.py | 7 Ko | Script one-shot |
| patch_set_convention.py | 3.6 Ko | Script one-shot |
| patch_staticdata.py | 6.5 Ko | Script one-shot |
| ccpa.config.json | 189 octets | Template config Telegram |
| skills-lock.json | 18 Ko | Fichier lock skills hors dossier |

**Action suggeree** : Deplacer scripts dans tools/scripts/archive/. Supprimer download.html.

---

## 2. data/ -- melange scripts et donnees

9 scripts Python dans data/ :
- data/build_volumes_csv.py
- data/fix_binary_read.py
- data/fix_drive_query.py
- data/fix_gemini_workflow.py
- data/fix_mime_query.py
- data/fix_search_method.py
- data/n8n_organize.py
- data/remove_orphan_node.py
- data/setup_gemini_credential.py

**Action** : Deplacer vers tools/scripts/.

---

## 3. temp-n8n-skills/ -- vide

Dossier vide. **Supprimer.**

---

## 4. .firecrawl/ -- 6.7 Mo cache

53 fichiers FluentCRM. **Ajouter au .gitignore.**

---

## 5. Skills : 290 entrees + 40 Mo archives

15 dossiers dans .archived-workspace-variants/ (40 Mo).
Fichiers .tmp et .log a nettoyer.

---

## 6. Credentials/tokens sur disque

4 fichiers token/credentials dans tools/scripts/.
Couverts par .gitignore mais presents physiquement.

---

## 7. node_modules imbriques dans apps/

4 dossiers + 1 venv POC. Ajouter apps/**/node_modules/ au .gitignore.

---

## 8. Legacy nesting excessif

tools/legacy/tools/ et tools/scripts/legacy/scripts/ a aplatir.
14 scripts setup-notion-*.js a archiver.

---

## 9-10. data/output/ et data/reports/ desorganises

Nesting excessif, doublons report/reports, dossier root-output vague.

---

## 11-13. Apify JSON, __pycache__, .gitignore

Apify v1-v5 a archiver. __pycache__ a nettoyer. .gitignore incomplet.

---

## Priorites

### Haute
1. Supprimer download.html et temp-n8n-skills/
2. Deplacer scripts racine dans tools/scripts/archive/
3. Ajouter .firecrawl/ et apps/**/node_modules/ au .gitignore

### Moyenne
4. Deplacer 9 scripts de data/ vers tools/scripts/
5. Aplatir legacy dirs
6. Reorganiser data/output/ et data/reports/

### Basse
7. Archiver .archived-workspace-variants/ (40 Mo)
8. Nettoyer Apify JSON, .tmp, .log, __pycache__
9. Verifier tokens pas git-tracked

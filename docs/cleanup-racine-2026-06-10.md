# Plan de nettoyage de la racine - 2026-06-10

Document de traçabilité. **Aucune suppression n'est effectuée par ce plan.** Il classe les
fichiers de la racine en 3 catégories et fournit les commandes prêtes à l'emploi, à exécuter
**uniquement après validation humaine**.

## Règles de sécurité appliquées

- Aucune suppression directe (`rm`, `rm -rf`, `sudo`) - voir `CLAUDE.md` racine workspace.
- Fichiers **tracked** : retrait via `git rm` -> toujours récupérables depuis l'historique git.
- Fichiers **ignored / untracked** : absents de git -> **doivent passer par la Corbeille Windows**
  (Explorer, ou snippet PowerShell `SendToRecycleBin` ci-dessous), jamais `Remove-Item` brut.
- **Ne pas toucher** : `.env`, `.mcp.json`, les dépôts git imbriqués (voir section Hors scope).

## Correctif .gitignore - DÉJÀ APPLIQUÉ (non destructif)

Ajouté dans la section « Local scratch / sandbox / one-shot probes » (root-ancré, pour coller
à la convention existante `/tmp-*.py`, `/*.txt`, `/test-yt.md`) :

```gitignore
/.tmp-*        # fichiers/dossiers temporaires à point initial, non couverts par /tmp-*.py
/scan.json     # dump volumineux régénérable (~24 Mo)
/*_post.json   # dumps de posts WP régénérables via tools/scripts/
```

Vérifié : `de_post.json` / `fr_post.json` sont des dumps tirés de l'API WordPress (régénérables
via `tools/scripts/backup_wp_to_drive.py` et `wp_audit_de_polylang_lang.py`), et aucun autre
`*_post.json` n'est tracké dans le repo.

---

## 1. À GARDER (source, config, gouvernance, entrypoints)

- **Config / build** (tracked) : `.editorconfig`, `.gitattributes`, `.gitignore`,
  `.pre-commit-config.yaml`, `.env.example`, `.mcp.json.example`, `.nano-banana-config.json`,
  `pyproject.toml`, `uv.lock`, `insforge.toml`, `skills-lock.json`
- **Config locale** (ignored, ne pas toucher) : `.env`, `.mcp.json`, `.coverage`
- **Gouvernance / docs** (tracked) : `CLAUDE.md`, `AGENTS.md`, `README.md`, `README-IA.md`,
  `CHANGELOG.md`, `CONTRIBUTING.md`
- **Entrypoints** (tracked) : `brain.bat`, `brain-lite.bat`, `planner.bat`, `publisher.bat`,
  `setup.bat`, `audit.ps1`
- **Worktree** : `.worktreeinclude` - référencé dans CLAUDE.md mais actuellement **untracked**
  -> à committer plutôt qu'à laisser flotter.

**À garder mais à vérifier** (rôle pas 100 % certain) : `package.json` + `package-lock.json`
(node racine), `settings.json` (résidu possible, la config Claude Code vit dans `.claude/`),
`ccpa.config.json`, `sync-colors.ps1`, `AVATAR-MICHAEL.md`, `AVATAR-USER.md`,
`.mcp.json.fluent` (config alternative tracked - confirmer avant tout retrait).

---

## 2. À DÉPLACER EN ARCHIVE (valeur potentielle, mais pas à la racine)

| Fichiers                                                                                                                                                                                                                                             | Statut    | Destination                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------- |
| `n8n-workflow-sync-blog.json`, `-simple.json`, `-fr-active.json`                                                                                                                                                                                     | tracked   | `systems/workflows/workflows/`                                  |
| `n8n-workflow-sync-translations.json`                                                                                                                                                                                                                | untracked | `systems/workflows/workflows/` (move manuel + `git add`)        |
| 7 transcripts `2026-03-2*_youtube_*.md`                                                                                                                                                                                                              | tracked   | `_archive/racine-2026-06-10/youtube-transcripts/`               |
| `landing-stanza.html`, `acces-protege.html`                                                                                                                                                                                                          | tracked   | `landing-pages/`                                                |
| `DNS_BASELINE_michaelkihl-fr_20260410.md`, `gmail-filters.xml`, `schoolsWP/Guide-commandes-schoolsWP-MCP-RANK-SEO.md`                                                                                                                                | tracked   | `docs/`                                                         |
| Brouillons `.tmp-*` (9) : `.tmp-draft-2967212-clean.md`, `.tmp-fluentcart-leadmagnet.md` / `-drive.md` / `.pdf`, `.tmp-fluentcart-brief-v04.md`, `.tmp-fcvswoo-gutenberg.html` / `-v2.html`, `.tmp-faq-kadence.html`, `.tmp-faq-original-block.html` | tracked   | `_archive/racine-2026-06-10/drafts/`                            |
| `slide-01..11-*.png` (deck, 11)                                                                                                                                                                                                                      | tracked   | `_archive/racine-2026-06-10/slides/`                            |
| `sync-blog.py`                                                                                                                                                                                                                                       | tracked   | À vérifier vs `scripts/n8n_sync_blog/` puis archiver si doublon |

---

## 3. À ENVOYER À LA CORBEILLE (jetable / régénérable / vide)

- **Gros poids** : `scan.json` (24 Mo, tracked).
- **Vides / marqueurs** : `0`, `Priorite`, `download.html` (tracked) ; `gws_debug_stdout.log` (ignored).
- **Logs debug** (ignored) : `gws_debug_stderr.log`, `gws_debug_stdout.log`.
- **Dumps texte scratch** : `kw_check.txt` (tracked) ; `col_0.txt`, `col_1.txt`, `callout.txt`,
  `first40.txt`, `orig_sample.txt`, `sc_block.txt`, `toc_ctx.txt`, `wp_raw_now.txt` (ignored).
- **Dumps de posts WP** (régénérables) : `de_post.json`, `fr_post.json` (untracked) ;
  `de_post.txt`, `de_post_content.txt`, `fr_post.txt`, `latest_de_post.txt` (ignored).
  ATTENTION : datés du 09/06 - confirmer qu'aucune tâche en cours ne s'appuie dessus.
- **Scripts one-shot n8n** (ignored) : `patch_claude_body.py`, `patch_error_node.py`,
  `patch_extract_convention.py`, `patch_file_context.py`, `patch_fix_setnode.py`,
  `patch_merge_conv.py`, `patch_set_convention.py`, `patch_staticdata.py`, `fix_workflow.py`.
- **Runners loose** : `run_mcp_action.mjs` (tracked), `run_get_post.mjs` (untracked).
- **Scripts/data `.tmp-*` jetables** (tracked, 27) : `.tmp-vm-*.sh` (12), `.tmp-gws-*.py` (4),
  `.tmp-find-docx.py`, `.tmp-find-draft.py`, `.tmp-test-gemini-key.py`, `.tmp-test-sheet.py`,
  `.tmp-build-fcvswoo.py`, `.tmp-assemble-fcvswoo.py`, `.tmp-parse-thruuu.py`,
  `.tmp-prep-sources-baseline.py`, `.tmp-upload-pdf-media.py`,
  `.tmp-fluentcart-finalize-uploads.py`, `.tmp-ninja-data.json`.
- **Captures d'itération** (tracked) : `iter1-screenshot.png`..`iter4-screenshot.png`.
- **Captures design** (tracked) : `aidesigner-hero-desktop.png`, `ccdesign-hero-desktop.png`,
  `tweak-accent-magenta.png`.
- **Backups MCP redondants** (ignored) : `.mcp.backup.json`, `.mcp.json.bak`
  (NB : ce sont des backups, PAS le `.mcp.json` live - celui-ci reste intouché).
- **Divers** : `update_form_5.php` (patch form one-shot, tracked), `test-yt.md` (ignored).

---

## Hors scope - NE PAS toucher

Dépôts git imbriqués (marqués `m` dans `git status`, sans `.gitmodules`) :
`tmp_fluentboards_dev_doc`, `agents/telegram-claude`, `antigravity/heygen-skills`,
`tools/ultimate-scraper`.

## Annexe - dossiers à traiter ensuite (hors périmètre « fichiers »)

Scrapes de doc temporaires (candidats Corbeille/archive) : `.tmp-fluentcart-doc-customer/`,
`.tmp-fluentcart-doc-dev/`, `.tmp-fluentcart-transcripts/`, `.tmp-gsc-npm/`, `.tmp-qrgen/`,
`tmp_fluentboards_doc_customer/`, `tmp_fluentboards_doc_dev/`, `tmp_fluentforms_doc_customer/`,
`tmp_rankmath_enrichment/`, `tmp-samaritain-img/`, `tmp-blur/`.
Dirs de travail (souvent gitignored) : `scratch/`, `sandbox-workspace/`, `runs/`, `input/`,
`output/`, `reports/`.

---

# COMMANDES PRÊTES (NE PAS EXÉCUTER SANS VALIDATION)

## A. git mv - fichiers tracked à archiver

```bash
# Créer les dossiers d'archive (non destructif)
mkdir -p _archive/racine-2026-06-10/youtube-transcripts
mkdir -p _archive/racine-2026-06-10/drafts
mkdir -p _archive/racine-2026-06-10/slides

# n8n workflows -> systems/workflows/workflows/
git mv n8n-workflow-sync-blog.json systems/workflows/workflows/
git mv n8n-workflow-sync-blog-simple.json systems/workflows/workflows/
git mv n8n-workflow-sync-blog-fr-active.json systems/workflows/workflows/

# Transcripts YouTube
git mv 2026-03-21_youtube_welcome-to-tutor-lms-academy.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_9-steps-seo-friendly-website-rank-math.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_complete-rank-math-tutorial-2026.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_how-to-add-remove-schema-rank-math.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_rank-math-seo-tutorial-2025-matt.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_schema-data-guide-rank-math.md _archive/racine-2026-06-10/youtube-transcripts/
git mv 2026-03-28_youtube_technical-seo-sitemap-robots-schema-rank-math.md _archive/racine-2026-06-10/youtube-transcripts/

# Landing pages
git mv landing-stanza.html landing-pages/
git mv acces-protege.html landing-pages/

# Docs de référence
git mv DNS_BASELINE_michaelkihl-fr_20260410.md docs/
git mv gmail-filters.xml docs/
git mv schoolsWP/Guide-commandes-schoolsWP-MCP-RANK-SEO.md docs/

# Brouillons de contenu .tmp-*
git mv .tmp-draft-2967212-clean.md _archive/racine-2026-06-10/drafts/
git mv .tmp-fluentcart-leadmagnet.md _archive/racine-2026-06-10/drafts/
git mv .tmp-fluentcart-leadmagnet-drive.md _archive/racine-2026-06-10/drafts/
git mv .tmp-fluentcart-leadmagnet.pdf _archive/racine-2026-06-10/drafts/
git mv .tmp-fluentcart-brief-v04.md _archive/racine-2026-06-10/drafts/
git mv .tmp-fcvswoo-gutenberg.html _archive/racine-2026-06-10/drafts/
git mv .tmp-fcvswoo-gutenberg-v2.html _archive/racine-2026-06-10/drafts/
git mv .tmp-faq-kadence.html _archive/racine-2026-06-10/drafts/
git mv .tmp-faq-original-block.html _archive/racine-2026-06-10/drafts/

# Slides (deck)
git mv slide-01-title.png _archive/racine-2026-06-10/slides/
git mv slide-02-agenda.png _archive/racine-2026-06-10/slides/
git mv slide-03-step01.png _archive/racine-2026-06-10/slides/
git mv slide-04-step02.png _archive/racine-2026-06-10/slides/
git mv slide-05-breaker.png _archive/racine-2026-06-10/slides/
git mv slide-06-step03.png _archive/racine-2026-06-10/slides/
git mv slide-07-step04.png _archive/racine-2026-06-10/slides/
git mv slide-08-step05.png _archive/racine-2026-06-10/slides/
git mv slide-09-step06.png _archive/racine-2026-06-10/slides/
git mv slide-10-recap.png _archive/racine-2026-06-10/slides/
git mv slide-11-cta.png _archive/racine-2026-06-10/slides/

# Untracked à archiver (move manuel puis git add)
#   n8n-workflow-sync-translations.json -> systems/workflows/workflows/
# À VÉRIFIER avant archivage : sync-blog.py (doublon possible de scripts/n8n_sync_blog/)
```

## B. git rm - fichiers tracked vraiment jetables (récupérables via historique)

```bash
git rm scan.json
git rm 0 Priorite download.html
git rm kw_check.txt
git rm run_mcp_action.mjs
git rm update_form_5.php
git rm iter1-screenshot.png iter2-screenshot.png iter3-screenshot.png iter4-screenshot.png
git rm aidesigner-hero-desktop.png ccdesign-hero-desktop.png tweak-accent-magenta.png

# .tmp-* scripts/data jetables (tracked)
git rm .tmp-vm-audio.sh .tmp-vm-devices.sh .tmp-vm-diag-openai.sh .tmp-vm-envcheck.sh \
       .tmp-vm-help.sh .tmp-vm-inspect.sh .tmp-vm-logs.sh .tmp-vm-logs2.sh \
       .tmp-vm-mic-live.sh .tmp-vm-mic.sh .tmp-vm-patch-launcher.sh .tmp-vm-status.sh
git rm .tmp-gws-update-brief.py .tmp-gws-update-md.py .tmp-gws-upload-leadmagnet.py .tmp-gws-upload-scripts.py
git rm .tmp-find-docx.py .tmp-find-draft.py
git rm .tmp-test-gemini-key.py .tmp-test-sheet.py
git rm .tmp-build-fcvswoo.py .tmp-assemble-fcvswoo.py
git rm .tmp-parse-thruuu.py .tmp-prep-sources-baseline.py .tmp-upload-pdf-media.py .tmp-fluentcart-finalize-uploads.py
git rm .tmp-ninja-data.json
```

> Variante « ceinture + bretelles » si tu veux que la copie physique parte aussi à la Corbeille :
> `git rm --cached <fichier>` (dé-suivi, garde le fichier), puis envoi manuel à la Corbeille.

## C. Fichiers ignored / untracked -> Corbeille Windows (manuel)

Ces fichiers ne sont **pas** dans git : pas de `git rm`. Suppression **via Explorer** (préféré)
ou via le snippet PowerShell `SendToRecycleBin` ci-dessous.

```
gws_debug_stderr.log
gws_debug_stdout.log
col_0.txt
col_1.txt
callout.txt
first40.txt
orig_sample.txt
sc_block.txt
toc_ctx.txt
wp_raw_now.txt
de_post.json
de_post.txt
de_post_content.txt
fr_post.json
fr_post.txt
latest_de_post.txt
patch_claude_body.py
patch_error_node.py
patch_extract_convention.py
patch_file_context.py
patch_fix_setnode.py
patch_merge_conv.py
patch_set_convention.py
patch_staticdata.py
fix_workflow.py
run_get_post.mjs
test-yt.md
.mcp.backup.json
.mcp.json.bak
```

Snippet PowerShell (envoie réellement à la Corbeille, pas une suppression définitive) -
à lancer depuis la racine du projet, **après validation** :

```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
$files = @(
  'gws_debug_stderr.log','gws_debug_stdout.log','col_0.txt','col_1.txt','callout.txt',
  'first40.txt','orig_sample.txt','sc_block.txt','toc_ctx.txt','wp_raw_now.txt',
  'de_post.json','de_post.txt','de_post_content.txt','fr_post.json','fr_post.txt','latest_de_post.txt',
  'patch_claude_body.py','patch_error_node.py','patch_extract_convention.py','patch_file_context.py',
  'patch_fix_setnode.py','patch_merge_conv.py','patch_set_convention.py','patch_staticdata.py','fix_workflow.py',
  'run_get_post.mjs','test-yt.md','.mcp.backup.json','.mcp.json.bak'
)
foreach ($f in $files) {
  if (Test-Path $f) {
    [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(
      (Resolve-Path $f), 'OnlyErrorDialogs', 'SendToRecycleBin')
  }
}
```

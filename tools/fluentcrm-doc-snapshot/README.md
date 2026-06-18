# fluentcrm-doc-snapshot

Snapshot mensuel de docs.fluentcrm.com vers un dossier Google Drive. Idempotent par defaut. Zero consommation API Anthropic. Pense pour tourner en cron local ou manuellement.

Cible canonique : sous-dossier `2026-05-15_snapshot` du dossier Drive `02 - Documentation officielle` (id `10eqbhKRkEeVCkzdrUDK1noVfMk25U6i1`). A chaque snapshot mensuel, creer un nouveau sous-dossier date plutot qu'ecraser, pour conserver l'historique.

## Setup

```powershell
cd "d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\fluentcrm-doc-snapshot"
..\..\.venv\Scripts\python -m pip install -r requirements.txt
```

Variables d'environnement (lues depuis `.env` racine projet ou `.env` local) :

- `FIRECRAWL_API_KEY` : cle Firecrawl, deja presente dans `.env` racine projet, partagee avec les agents Python.
- `GDRIVE_CREDENTIALS_PATH` : optionnel, chemin vers `drive_credentials.json`. Par defaut le script cherche `./drive_credentials.json` dans le dossier du tool.

OAuth Google Drive (une seule fois) :

1. Aller sur https://console.cloud.google.com/apis/credentials
2. Creer un OAuth client de type "Desktop app", scope `https://www.googleapis.com/auth/drive.file`.
3. Telecharger le JSON, le poser a `tools/fluentcrm-doc-snapshot/drive_credentials.json` (gitignored).
4. Premier run : le script ouvre le navigateur, tu valides ton compte Google. Le token est sauve dans `drive_token.json` (gitignored).

## Usage

Mode par defaut, idempotent : ne touche pas aux slugs deja presents.

```powershell
..\..\.venv\Scripts\python snapshot.py --folder-id 1_4Y7-t2j9jmMRsfz4ybygIiDVBde3Y-l
```

Completer la session du 2026-05-15 (les 63 manquants seront uploades, les 95 presents preserves) :

```powershell
..\..\.venv\Scripts\python snapshot.py --folder-id 1_4Y7-t2j9jmMRsfz4ybygIiDVBde3Y-l --target-date 2026-05-15
```

Re-scrape cible sur un slug ou un groupe (utile pour les pages condensees par les sous-agents). Liste a passer en virgule-separee :

```powershell
..\..\.venv\Scripts\python snapshot.py --folder-id <id> --mode full --only mcp-for-ai-agents,setting-up-campaign,advanced-filter
```

Snapshot mensuel propre : creer d'abord le sous-dossier date dans Drive UI, puis lancer en `missing` mode dessus :

```powershell
..\..\.venv\Scripts\python snapshot.py --folder-id <new_id> --mode missing
```

Mode `delta` (re-scrape mais ne re-uploade que si le contenu a change, base sur md5 du markdown final) :

```powershell
..\..\.venv\Scripts\python snapshot.py --folder-id <id> --mode delta
```

## Sortie

- `manifest.json` : historique des runs + etat par slug (file_id Drive, hash md5, scraped_at, uploaded_at). Utile pour audit ou detection de drift entre snapshots.
- `snapshot.log` : log detaille du dernier run (rotation manuelle, pas auto).
- Codes de sortie : `0` succes, `1` partiel (echecs presents dans manifest), `2` setup error.

## Cron mensuel (suggestion)

Sous Windows Task Scheduler, declencher le 1er de chaque mois :

```powershell
$today = Get-Date -Format yyyy-MM-dd
cd 'd:\VS Code\CLAUDE CODE\projects\schoolswp\tools\fluentcrm-doc-snapshot'
..\..\.venv\Scripts\python snapshot.py --folder-id NEW_MONTHLY_FOLDER_ID --target-date $today
```

A chaque run, creer manuellement le sous-dossier date en amont, ou etendre le script pour qu'il le cree tout seul (pas implemente volontairement pour rester explicite sur le quoi-creer-ou).

## Pourquoi ce tool

Le scraping initial du 2026-05-15 a ete fait par 3 sous-agents Claude Code en parallele. Deux ont plante a mi-course sur "monthly usage limit" Anthropic. Conclusion : un job bulk-scrape ne doit pas dependre du quota Anthropic. Ce tool consomme uniquement Firecrawl (pay-per-scrape, ~10 EUR pour 1000 pages) et Drive API (gratuit dans les quotas standards).

## Limites connues

- Firecrawl peut renvoyer un markdown vide pour des pages JS-heavy. Le script retry une fois avec `waitFor: 6000`. Si toujours vide, log l'echec et continue.
- L'auth OAuth desktop expire apres 7 jours en mode test ; si ton OAuth client n'est pas en mode "Production", il faut re-valider le token periodiquement. Documente cote Google : https://support.google.com/cloud/answer/10311615
- Le mode `delta` compare le md5 du markdown final (frontmatter inclus avec `scraped_at`). Donc un run meme date ne re-uploade pas ; un run nouvelle date avec contenu identique re-uploade quand meme (le frontmatter change). Solution simple : changer `target_date` seulement quand on veut reellement marquer un nouveau snapshot.

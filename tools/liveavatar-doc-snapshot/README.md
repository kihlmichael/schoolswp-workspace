# liveavatar-doc-snapshot

Snapshot de la documentation officielle LiveAvatar (`docs.liveavatar.com`, plateforme HeyGen d'avatars video IA temps reel) vers du Markdown propre par page. Zero consommation API Anthropic. Pense pour un cron mensuel local (Windows Task Scheduler).

## Methode

LiveAvatar tourne sous Mintlify, qui expose pour chaque page une variante Markdown native (`<page>.md`, source byte-perfect, plus propre que defuddle ou firecrawl), plus `/sitemap.xml`, `/llms.txt`, `/llms-full.txt`, `/openapi.json`. Le script decouvre les pages via le sitemap (plus quelques pages extra referencees dans `llms.txt`), recupere chaque `.md`, et ecrit en miroir de l'arborescence URL avec un frontmatter `source-brute`. Deux pages embarquant du contenu externe (master-faq sur Notion, socials/x) sont stubbees.

## Usage

```powershell
cd "d:\VS Code\CLAUDE CODE\projects\schoolswp"
# scrape vers tools/liveavatar-doc-snapshot/snapshots/<today>/
.venv\Scripts\python tools\liveavatar-doc-snapshot\snapshot.py

# date / dossier custom
.venv\Scripts\python tools\liveavatar-doc-snapshot\snapshot.py --date 2026-07-01 --out chemin\sortie

# miroir vers Google Drive (via gws ; pointe --parent sur un dossier neuf pour eviter les doublons)
.venv\Scripts\python tools\liveavatar-doc-snapshot\upload_to_drive.py --src snapshots\2026-07-01 --parent <drive_folder_id> --name 2026-07-01
```

## Cron mensuel (Windows Task Scheduler)

`run-monthly.ps1` orchestre le scrape (et, avec `-UploadDrive`, le miroir vers un sous-dossier date sous le dossier Drive LiveAvatar pour garder l'historique sans ecraser la copie courante).

Tache enregistree le 2026-06-05 :

```powershell
schtasks /create /tn "schoolsWP - LiveAvatar doc snapshot (mensuel)" `
  /tr "powershell -NoProfile -ExecutionPolicy Bypass -File \"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\liveavatar-doc-snapshot\run-monthly.ps1\"" `
  /sc monthly /d 1 /st 09:00 /f
```

Le 1er de chaque mois a 9h. Sortie journalisee dans `logs/run-<date>.log`. Pour activer le miroir Drive, editer l'action de la tache pour ajouter `-UploadDrive`.

## Transport vault

Le transport vers le vault Obsidian (`08_sources/services-saas/liveavatar/`) reste **manuel** (arbitrage humain, SOP passerelle). Le cron ne touche pas au vault.

## Reference

Memoire interne projet : `reference_liveavatar_docs_snapshot`. Methode reutilisable pour toute doc Mintlify (changer `BASE` dans `snapshot.py`).

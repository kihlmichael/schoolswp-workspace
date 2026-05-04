# Cheatsheet wp-media-upload

Pour un nouvel article, demande juste a Claude : "upload les images de l article X"

Il scaffold, genere les metadonnees, lance l upload. Tu n as rien a retenir.

## Si tu veux piloter toi-meme

Depuis projects\schoolswp\tools\wp-media-upload\ :

    python cli.py env-check
    python cli.py init --article <slug>
    python cli.py list --article <slug>
    python cli.py upload --article <slug> --dry-run
    python cli.py upload --article <slug>

Interpreteur complet si besoin :
D:\VS Code\CLAUDE CODE\projects\schoolswp\.venv\Scripts\python.exe

## Structure par article

- inbox\<slug>\ : tu deposes tes JPEG + manifest.yaml ici
- processed\<slug>\ : ou le tool deplace apres upload
- backup\<slug>\ : master copies automatiques (fichiers originaux preserves)
- logs\uploads.log : trace de toutes les operations

## Regles de nommage

- Pas de date dans le nom de fichier (pas de -2026, -avril)
- Pas de mention schoolswp dans le nom (le domaine le contient deja)
- Prefixe 01-, 02- OK en local (strippe automatiquement a l upload WP)

## Panne

- 401 : verifie les env vars WP
- 404 article : post en draft, mets en publish ou utilise un id publie
- ExifTool not found : installe via winget OliverBetz.ExifTool ou utilise --no-exif

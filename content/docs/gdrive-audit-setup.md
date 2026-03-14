# Guide de setup — Google Drive Audit

## Pre-requis

- Python 3.10+
- Un compte Google avec acces au Drive a auditer
- Acces a Google Cloud Console

## Etape 1 : Creer un projet Google Cloud

1. Va sur [console.cloud.google.com](https://console.cloud.google.com/)
2. Clique **Nouveau projet** → nom : `schoolswp-drive-audit`
3. Selectionne ce projet

## Etape 2 : Activer l'API Google Drive

1. Menu hamburger → **API et services** → **Bibliotheque**
2. Cherche "Google Drive API"
3. Clique **Activer**

## Etape 3 : Configurer l'ecran de consentement OAuth

1. **API et services** → **Ecran de consentement OAuth**
2. Type : **Externe** (meme si c'est pour toi seul)
3. Remplis :
   - Nom de l'application : `Drive Audit schoolsWP`
   - Email d'assistance : ton email
   - Coordonnees du developpeur : ton email
4. **Enregistrer et continuer**
5. Scopes : clique **Ajouter ou supprimer des champs d'application**
   - Cherche `drive.metadata.readonly`
   - Coche-le → **Mettre a jour**
6. **Enregistrer et continuer**
7. Utilisateurs de test : clique **Ajouter des utilisateurs** → entre ton email Google
8. **Enregistrer et continuer** → **Retour au tableau de bord**

## Etape 4 : Creer les identifiants OAuth

1. **API et services** → **Identifiants**
2. **Creer des identifiants** → **ID client OAuth**
3. Type d'application : **Application de bureau**
4. Nom : `drive-audit-desktop`
5. **Creer**
6. Telecharge le fichier JSON
7. Renomme-le en `credentials-gdrive-audit.json`
8. Place-le dans le dossier `scripts/`

> IMPORTANT : ce fichier contient des secrets. Il est deja dans .gitignore.
> Ne le commite JAMAIS.

## Etape 5 : Installer les dependances Python

```bash
cd scripts/
pip install -r requirements-gdrive-audit.txt
```

Ou avec un venv (recommande) :

```bash
cd scripts/
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements-gdrive-audit.txt
```

## Etape 6 : Lancer l'audit

```bash
cd scripts/
python gdrive-audit.py
```

Au premier lancement :
1. Un navigateur s'ouvre automatiquement
2. Connecte-toi avec ton compte Google
3. Autorise l'application (scope : metadata readonly)
4. Le token est sauvegarde localement dans `token-gdrive-audit.json`
5. L'audit demarre automatiquement

### Options

```bash
# Auditer un sous-dossier specifique
python gdrive-audit.py --folder-id 1AbCdEfGhIjKlMnOpQrStUvWxYz

# Limiter la profondeur
python gdrive-audit.py --max-depth 5

# Changer le dossier de sortie
python gdrive-audit.py --output-dir ../output/mon-audit
```

## Etape 7 : Verifier les resultats

Les fichiers sont generes dans `output/gdrive-audit/` :

| Fichier | Contenu |
|---------|---------|
| `inventory.csv` | Inventaire complet (id, nom, chemin, type, taille, date) |
| `naming_issues.csv` | Problemes de nommage detectes avec severite |
| `duplicates_suspects.csv` | Fichiers potentiellement dupliques |
| `depth_report.csv` | Analyse de profondeur par dossier |
| `audit_summary.json` | Resume global (stats, top problemes, flags) |

## Securite

- Le scope `drive.metadata.readonly` ne permet QUE de lire les metadonnees
- Aucun contenu de fichier n'est lu ou telecharge
- Aucun fichier n'est modifie, deplace ou supprime
- Le token expire et peut etre revoque a tout moment dans [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
- Supprime `token-gdrive-audit.json` pour forcer une re-authentification

## Duree estimee

| Volume Drive | Temps approximatif |
|---|---|
| < 1 000 fichiers | < 1 min |
| 1 000 – 5 000 | 1-3 min |
| 5 000 – 20 000 | 3-10 min |
| > 20 000 | 10-30 min |

Le script affiche la progression tous les 500 elements.

## Depannage

### "credentials-gdrive-audit.json introuvable"
→ Verifie que le fichier est bien dans le meme dossier que le script

### "Access Not Configured" / "API not enabled"
→ Retourne dans Google Cloud Console et verifie que l'API Google Drive est activee

### "Error 403: access_denied"
→ Verifie que ton email est dans la liste des "Utilisateurs de test" de l'ecran de consentement

### Token expire
→ Supprime `token-gdrive-audit.json` et relance le script

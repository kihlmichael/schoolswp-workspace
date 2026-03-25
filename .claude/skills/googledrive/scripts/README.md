# Scripts Google Drive - schoolsWP

## Prérequis

### 1. Installation des dépendances

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 2. Configuration OAuth Google Cloud

#### Étape 1 : Créer un projet Google Cloud

1. Va sur [Google Cloud Console](https://console.cloud.google.com/)
2. Clique sur "Sélectionner un projet" → "Nouveau projet"
3. Nom : `schoolsWP-Drive-Audit`
4. Clique "Créer"

#### Étape 2 : Activer l'API Google Drive

1. Menu ☰ → "API et services" → "Bibliothèque"
2. Recherche "Google Drive API"
3. Clique dessus → "Activer"

#### Étape 3 : Configurer l'écran de consentement OAuth

1. Menu ☰ → "API et services" → "Écran de consentement OAuth"
2. Type d'utilisateur : **Externe** (ou Interne si G Suite)
3. Remplis :
   - Nom de l'application : `schoolsWP Drive Audit`
   - Email d'assistance : ton email
   - Email du développeur : ton email
4. Scopes : ajoute `.../auth/drive.metadata.readonly`
5. Utilisateurs test : ajoute ton email

#### Étape 4 : Créer les identifiants OAuth

1. Menu ☰ → "API et services" → "Identifiants"
2. "Créer des identifiants" → "ID client OAuth"
3. Type d'application : **Application de bureau**
4. Nom : `schoolsWP Audit CLI`
5. Télécharge le JSON
6. **Renomme-le en `credentials.json`**
7. Place-le dans le dossier `scripts/`

### 3. Structure des fichiers

```
scripts/
├── audit_drive.py      # Script principal
├── credentials.json    # ← À créer (OAuth)
├── token.json          # ← Généré automatiquement
└── README.md           # Ce fichier
```

---

## Utilisation

### Audit complet (dry-run)

```bash
cd .claude/skills/08_GoogleDrive/scripts
python audit_drive.py
```

### Audit d'un dossier spécifique

```bash
# Trouver l'ID du dossier dans l'URL Google Drive
# https://drive.google.com/drive/folders/ABC123...
python audit_drive.py --folder-id ABC123...
```

### Limiter la profondeur

```bash
python audit_drive.py --max-depth 5
```

### Personnaliser le nom de sortie

```bash
python audit_drive.py --output mon_audit
```

---

## Fichiers générés

| Fichier | Contenu |
|---------|---------|
| `audit_drive_YYYYMMDD_HHMMSS.json` | Rapport complet (stats, problèmes, recommandations) |
| `audit_drive_YYYYMMDD_HHMMSS_items.csv` | Liste de tous les fichiers/dossiers |
| `audit_drive_YYYYMMDD_HHMMSS_issues.csv` | Liste des problèmes détectés |

---

## Scopes utilisés

| Scope | Permission |
|-------|------------|
| `drive.metadata.readonly` | Lecture des métadonnées uniquement |

**Aucune permission d'écriture, modification ou suppression.**

---

## Problèmes détectés

| Catégorie | Description |
|-----------|-------------|
| `profondeur_excessive` | Arborescence trop profonde (> 6 niveaux) |
| `caracteres_interdits` | Caractères spéciaux problématiques |
| `nom_trop_long` | Noms > 100 caractères |
| `versioning_chaotique` | `_final`, `_v2`, `copie`, etc. |
| `espaces_parasites` | Espaces en début/fin de nom |
| `espaces_multiples` | Plusieurs espaces consécutifs |
| `noms_generiques` | `nouveau`, `test`, `sans titre`, etc. |
| `doublons_potentiels` | Fichiers similaires |
| `melange_langues` | FR/EN dans un même nom |

---

## Sécurité

- Le script n'a **aucune permission d'écriture**
- Mode **dry-run par défaut** : aucune modification possible
- Token stocké localement (`token.json`)
- Pour révoquer l'accès : [Google Security](https://myaccount.google.com/permissions)

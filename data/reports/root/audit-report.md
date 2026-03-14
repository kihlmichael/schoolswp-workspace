# Audit de Code - CLAUDE CODE Workspace

**Date :** 2026-02-04
**Langage principal :** Python, Markdown
**Fichiers analysés :** 95 (6 Python, 79 Markdown, 10 JSON)
**Score de santé :** 82/100

---

## Résumé exécutif

| Catégorie | Total | P0 | P1 | P2 |
|-----------|-------|----|----|----|
| Duplication | 2 | 0 | 2 | 0 |
| TODO/FIXME | 0 | 0 | 0 | 0 |
| Patterns | 0 | 0 | 0 | 0 |
| Dépendances | 1 | 0 | 0 | 1 |
| **Total** | **3** | **0** | **2** | **1** |

### Score de santé : 82/100

Interprétation : **Bonne santé** (70-89)

Le workspace est bien organisé avec une structure de skills cohérente.

---

## Action immédiate recommandée

> **Créer `google_drive_common.py`** pour éliminer 240 lignes de code dupliqué dans les scripts Google Drive.
>
> **Impact :** -11% de code Python, maintenance OAuth centralisée, risque d'incohérence éliminé.
>
> **Effort :** 2 heures

---

## Axe principal d'amélioration : Refactoring Google Drive Scripts

Les 4 scripts de gestion Google Drive présentent une **duplication significative** qui représente le principal levier d'amélioration de ce workspace.

### Vue d'ensemble de la duplication

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CODE DUPLIQUÉ (240 lignes)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────┐│
│  │ audit_drive.py  │  │ migrate_phase1  │  │ migrate_phase2  │  │ phase3  ││
│  │     502 L       │  │     339 L       │  │     362 L       │  │  448 L  ││
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  └────┬────┘│
│           │                    │                    │                │     │
│           ▼                    ▼                    ▼                ▼     │
│  ┌────────────────────────────────────────────────────────────────────────┐│
│  │  BLOCS IDENTIQUES RÉPÉTÉS 4 FOIS :                                     ││
│  │  • Hack encodage UTF-8 (5 lignes)                                      ││
│  │  • Imports Google API (13 lignes)                                      ││
│  │  • Configuration SCOPES/TOKEN/CREDENTIALS (5 lignes)                   ││
│  │  • Méthode authenticate() (~25 lignes)                                 ││
│  │  • Messages d'erreur OAuth (~10 lignes)                                ││
│  │                                                            Total: ~60L ││
│  └────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│  60 lignes × 4 fichiers = 240 lignes dupliquées (11% du code Python)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Findings Importants (P1)

### [DUP-001] Blocs d'initialisation dupliqués

**Fichiers concernés :**
| Fichier | Lignes | Bloc dupliqué |
|---------|--------|---------------|
| [audit_drive.py](.claude/skills/08_GoogleDrive/scripts/audit_drive.py#L1-L41) | 1-41 | Imports + Config |
| [migrate_phase1.py](.claude/skills/08_GoogleDrive/scripts/migrate_phase1.py#L1-L41) | 1-41 | Imports + Config |
| [migrate_phase2_doublons.py](.claude/skills/08_GoogleDrive/scripts/migrate_phase2_doublons.py#L1-L41) | 1-41 | Imports + Config |
| [migrate_phase3_structure.py](.claude/skills/08_GoogleDrive/scripts/migrate_phase3_structure.py#L1-L41) | 1-41 | Imports + Config |

**Extrait du code dupliqué :**

```python
# === BLOC 1 : Hack encodage (L1-5) - IDENTIQUE dans les 4 fichiers ===
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# === BLOC 2 : Imports Google API (L23-35) - IDENTIQUE ===
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# === BLOC 3 : Configuration (L37-41) - QUASI-IDENTIQUE ===
SCOPES = ['https://www.googleapis.com/auth/drive']  # ou .metadata.readonly
TOKEN_FILE = 'token_write.json'                      # ou token.json
CREDENTIALS_FILE = 'credentials.json'
```

---

### [DUP-002] Méthode authenticate() dupliquée

**Comparaison côte à côte :**

| audit_drive.py (L88-118) | migrate_phase1.py (L127-150) |
|--------------------------|------------------------------|
| `def authenticate(self):` | `def authenticate(self):` |
| `creds = None` | `creds = None` |
| `if os.path.exists(TOKEN_FILE):` | `if os.path.exists(TOKEN_FILE):` |
| `creds = Credentials.from_authorized_user_file(...)` | `creds = Credentials.from_authorized_user_file(...)` |
| ... (25 lignes similaires) | ... (25 lignes similaires) |

**Seules différences :** Les messages d'erreur et le print de confirmation.

---

## Solution recommandée : Module commun

### Architecture cible

```
.claude/skills/08_GoogleDrive/scripts/
├── google_drive_common.py    # NOUVEAU - Module partagé
├── audit_drive.py            # Simplifié (import du module)
├── migrate_phase1.py         # Simplifié
├── migrate_phase2_doublons.py
└── migrate_phase3_structure.py
```

### Implémentation proposée

**Fichier à créer : `google_drive_common.py`**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Common - Module partagé schoolsWP
==============================================
Centralise l'authentification et la configuration pour tous les scripts Drive.
"""

import sys
import io
import os

# Fix encodage Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Google API imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# === CONFIGURATION CENTRALISÉE ===
CREDENTIALS_FILE = 'credentials.json'
TOKEN_READ_FILE = 'token.json'
TOKEN_WRITE_FILE = 'token_write.json'

SCOPES_READ = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES_WRITE = ['https://www.googleapis.com/auth/drive']


def get_drive_service(write_access: bool = False, verbose: bool = True):
    """
    Obtient un service Google Drive authentifié.

    Args:
        write_access: True pour permissions d'écriture, False pour lecture seule
        verbose: Afficher les messages de progression

    Returns:
        Service Google Drive ou None si échec
    """
    scopes = SCOPES_WRITE if write_access else SCOPES_READ
    token_file = TOKEN_WRITE_FILE if write_access else TOKEN_READ_FILE
    creds = None

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"\n❌ ERREUR: Fichier '{CREDENTIALS_FILE}' introuvable.")
                print("\n📋 Instructions:")
                print("1. Va sur https://console.cloud.google.com/")
                print("2. Crée un projet ou sélectionne un existant")
                print("3. Active l'API Google Drive")
                print("4. Crée des identifiants OAuth 2.0 (Application de bureau)")
                print(f"5. Télécharge le JSON et renomme-le '{CREDENTIALS_FILE}'")
                print(f"6. Place-le dans: {os.getcwd()}")
                return None

            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, scopes)
            creds = flow.run_local_server(port=0)

        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    if verbose:
        mode = "ÉCRITURE" if write_access else "LECTURE SEULE"
        print(f"✅ Authentification réussie (mode {mode})")

    return service


# Export des erreurs pour gestion dans les scripts
__all__ = [
    'get_drive_service',
    'HttpError',
    'SCOPES_READ',
    'SCOPES_WRITE',
    'CREDENTIALS_FILE',
]
```

### Refactoring des scripts existants

**AVANT (audit_drive.py) - 41 lignes d'initialisation :**
```python
#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(...)
# ... 35 autres lignes ...
```

**APRÈS (audit_drive.py) - 3 lignes :**
```python
#!/usr/bin/env python3
"""Google Drive Audit Script - schoolsWP"""
from google_drive_common import get_drive_service, HttpError

class DriveAuditor:
    def __init__(self, max_depth=None):
        self.service = get_drive_service(write_access=False)
        # ... reste du code métier ...
```

### Gains attendus

| Métrique | Avant | Après | Gain |
|----------|-------|-------|------|
| Lignes dupliquées | 240 | 0 | -100% |
| Points de maintenance OAuth | 4 | 1 | -75% |
| Risque d'incohérence | Élevé | Nul | ✓ |

### Plan d'exécution

```
[ ] 1. Créer google_drive_common.py (30 min)
[ ] 2. Tester l'authentification isolément (15 min)
[ ] 3. Refactorer audit_drive.py (20 min)
[ ] 4. Refactorer migrate_phase1.py (20 min)
[ ] 5. Refactorer migrate_phase2_doublons.py (20 min)
[ ] 6. Refactorer migrate_phase3_structure.py (20 min)
[ ] 7. Tests de non-régression (15 min)
```

**Effort total estimé : 2h**

---

## Findings Mineurs (P2)

### [DEP-001] Dépendance fpdf utilisée une seule fois

**Fichier :** [skills_list.py](skills_list.py)
**Package :** `fpdf` (FPDF2)

**Détails :** Le fichier `skills_list.py` est un script one-shot pour générer un PDF de la liste des skills. Il utilise `fpdf` qui n'est pas déclaré dans un fichier de dépendances.

**Impact :** Mineur - script utilitaire ponctuel.

**Recommandation :**
1. Ajouter un commentaire en en-tête :
```python
# Prérequis: pip install fpdf2
```
2. Ou déplacer dans un dossier `scripts/` avec un requirements.txt dédié

**Effort estimé :** 10min

---

## Statistiques détaillées

### Structure du projet

| Composant | Compte |
|-----------|--------|
| Skills (.claude/skills/) | 17 |
| Fichiers Python | 6 |
| Fichiers Markdown | 79 |
| Workflows n8n (.json) | 4 |
| Lignes de code Python | 2,190 |

### Répartition des fichiers Python

| Fichier | Lignes | Rôle |
|---------|--------|------|
| audit_drive.py | 502 | Audit Google Drive |
| migrate_phase3_structure.py | 448 | Migration Phase 3 |
| bot.py | 437 | Bot Telegram PoC |
| migrate_phase2_doublons.py | 362 | Migration Phase 2 |
| migrate_phase1.py | 339 | Migration Phase 1 |
| skills_list.py | 102 | Génération PDF |

### TODO/FIXME

- **Total trouvés dans le code source :** 0
- **Faux positif ignoré :** 1 (XXX dans documentation comme placeholder)

### Patterns de nommage

| Catégorie | Convention | Cohérence |
|-----------|------------|-----------|
| Fichiers Python | snake_case | 100% |
| Dossiers skills | NN_NomSkill | 100% |
| Fichiers Markdown | kebab-case / UPPERCASE | 95% |
| Classes Python | PascalCase | 100% |
| Fonctions Python | snake_case | 100% |

### Dépendances

**claude-telegram-poc/requirements.txt :**
- python-telegram-bot>=21.0
- mistune>=3.0
- python-dotenv>=1.0

**Scripts Google Drive (non déclarées formellement) :**
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

**skills_list.py :**
- fpdf2

---

## Prochaines actions recommandées

### Priorité 1 : Refactoring Google Drive (ce mois)

**Objectif :** Éliminer 240 lignes de code dupliqué et centraliser la maintenance OAuth.

| Étape | Action | Effort | Fichier |
|-------|--------|--------|---------|
| 1 | Créer le module commun | 30 min | `google_drive_common.py` |
| 2 | Tester authentification | 15 min | - |
| 3 | Refactorer audit_drive.py | 20 min | `audit_drive.py` |
| 4 | Refactorer migrate_phase1.py | 20 min | `migrate_phase1.py` |
| 5 | Refactorer migrate_phase2_doublons.py | 20 min | `migrate_phase2_doublons.py` |
| 6 | Refactorer migrate_phase3_structure.py | 20 min | `migrate_phase3_structure.py` |
| 7 | Tests de non-régression | 15 min | - |

**Total : 2h**

### Priorité 2 : Documentation (backlog)

- [ ] Ajouter commentaire de prérequis dans `skills_list.py`
- [ ] Créer `requirements.txt` pour les scripts Google Drive :
  ```
  google-api-python-client>=2.0
  google-auth-httplib2>=0.1
  google-auth-oauthlib>=1.0
  ```

---

## Points positifs

- **Organisation des skills excellente** : Structure cohérente avec préfixes numériques
- **Documentation complète** : Chaque skill a un SKILL.md bien structuré
- **Aucun TODO oublié** : Le code source ne contient pas de dette technique non trackée
- **Conventions de nommage respectées** : 100% de cohérence sur Python, 95%+ sur Markdown
- **Séparation claire des responsabilités** : Chaque script a un rôle défini

---

**Audit généré par Code Audit Skill**
**Date :** 2026-02-04 12:30

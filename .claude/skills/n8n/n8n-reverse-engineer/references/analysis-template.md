# Template d'analyse et plan de reproduction

Ce fichier est le template de sortie pour le skill `n8n-reverse-engineer`.
Remplir chaque section en remplacant les placeholders par les donnees reelles.
Ne pas supprimer de section — si une section est sans objet, ecrire "N/A — [raison]".

---

## PHASE 1 — ANALYSE

### 1. Resume executif

- **Ce que fait l'automatisation** : [description en 2-3 phrases]
- **Point d'entree** : [trigger exact — webhook, schedule, Telegram, etc.]
- **Resultat final** : [ce qui est produit/envoye/cree]
- **Services externes** : [liste des APIs/services utilises]
- **Parcours complet** : [resume du flux en une phrase]

### 2. Inventaire des workflows et fichiers

| Chemin | Type | Nom workflow/script | Role suppose | Statut | Raison classification | Preuve |
|--------|------|---------------------|-------------|--------|----------------------|--------|
| `path/file.json` | Export n8n | Nom du workflow | Role | production / secondaire / template / test / archive / incertain | Indices observes | confirme / probable / incertain |

### 3. Cartographie du pipeline

Pour chaque etape du pipeline reel, dans l'ordre d'execution :

#### Etape N — [Nom descriptif]

- **Source** : [noeud ou fichier qui prouve ce comportement]
- **Entree** : [donnees recues]
- **Traitement** : [ce qui est fait]
- **Sortie** : [donnees produites]
- **Dependances** : [services, credentials, sub-workflows]
- **Preuve** : confirme / probable / incertain
- **Notes** : [commentaires utiles]

### 4. Analyse noeud par noeud

Pour chaque workflow pertinent :

#### Workflow : "[Nom du workflow]"

**Trigger** : [type et configuration]

| # | Noeud | Type | Role | Expressions cles | Variables produites | Variables consommees | Preuve |
|---|-------|------|------|------------------|--------------------|--------------------|--------|
| 1 | Nom | Type n8n | Ce qu'il fait | `={{ $json.field }}` | `fieldName` | `inputField` | confirme |

**Prompts extraits** (citer textuellement) :

```
[Prompt systeme exact tel que trouve dans le noeud]
```

```
[Prompt utilisateur exact tel que trouve dans le noeud]
```

**Code embarque** (noeuds Code) :

```javascript
// Noeud: "Nom du noeud Code"
// [code exact copie du JSON]
```

**Decisions conditionnelles** :

| Noeud IF/Switch | Condition | Branche true | Branche false |
|----------------|-----------|-------------|--------------|
| Nom | `{{ condition }}` | → Noeud X | → Noeud Y |

**Appels HTTP** :

| Noeud | Methode | URL | Headers | Body | Auth |
|-------|---------|-----|---------|------|------|
| Nom | GET/POST | `https://...` | `{ ... }` | `{ ... }` | credential-name |

**Points de fragilite** :

- [liste des risques identifies]

### 5. Dependances externes

| Service | Usage exact | Auth | Donnees envoyees | Donnees recues | Variable .env | Preuve |
|---------|------------|------|-----------------|---------------|--------------|--------|
| Telegram Bot API | Recevoir messages + envoyer reponses | Bot Token | message text | message_id | `TELEGRAM_BOT_TOKEN` | confirme |

### 6. Entrees, sorties et schemas

**Entree principale** :

```json
{
  "description": "Format du message/payload d'entree",
  "fields": {
    "field_name": "type — description"
  }
}
```

**Champs intermediaires importants** :

| Champ | Cree par | Consomme par | Type | Description |
|-------|---------|-------------|------|-------------|
| `field` | Noeud X | Noeud Y | string | Description |

**Sortie principale** :

```
[Format exact de la sortie — texte, JSON, message, fichier]
```

**Champs non confirmes** :

- [liste des champs dont l'existence ou le format est incertain]

### 7. Prompts, templates et logique redactionnelle

Pour chaque prompt trouve :

#### Prompt [N] — [Noeud source]

- **Type** : systeme / utilisateur / template
- **Texte exact** :

```
[texte integral sans reformulation]
```

- **Variables injectees** : `{{ variable1 }}`, `{{ variable2 }}`
- **Contraintes de sortie** : [format impose, longueur, langue, ton]
- **Variantes** : [si plusieurs versions existent, laquelle est active et pourquoi]

### 8. Ambiguites, trous et risques

#### Bloquants

| Element | Pourquoi c'est ambigu | Ce qui manque | Impact | Action requise |
|---------|----------------------|--------------|--------|---------------|
| ... | ... | ... | ... | ... |

#### Importants

| Element | Pourquoi c'est ambigu | Ce qui manque | Impact | Action requise |
|---------|----------------------|--------------|--------|---------------|
| ... | ... | ... | ... | ... |

#### Mineurs

| Element | Pourquoi c'est ambigu | Ce qui manque | Impact | Action requise |
|---------|----------------------|--------------|--------|---------------|
| ... | ... | ... | ... | ... |

---

## PHASE 2 — PLAN DE REPRODUCTION

### 9. Strategie de reproduction

| Categorie | Elements | Approche |
|-----------|---------|----------|
| A l'identique | [prompts, formats de sortie, logique metier] | Copie fidele |
| n8n → Python | [appels API, transformations, code embarque] | Script Python equivalent |
| Declaratif | [credentials, config, setup] | Documentation dans SKILL.md |
| A confirmer | [elements incertains] | Marque comme placeholder |

### 10. Structure cible du Skill

```
skill-name/
├── SKILL.md                 # Instructions de reproduction
├── scripts/
│   ├── main_pipeline.py     # Pipeline principal
│   ├── [other_scripts].py   # Scripts specifiques
│   └── requirements.txt     # Dependances Python
├── prompts/
│   ├── system-prompt-1.md   # Prompt systeme extrait
│   └── user-prompt-1.md     # Prompt utilisateur extrait
├── references/
│   └── [docs].md            # Documentation, schemas
├── examples/
│   └── sample-output.md     # Exemple de sortie attendue
└── .env                     # Placeholders secrets
```

### 11. Mapping original → reproduction

| Etape/noeud original | Comportement observe | Composant cible | Fichier cible | Statut | Justification |
|---------------------|---------------------|----------------|--------------|--------|--------------|
| Telegram Trigger | Recoit message utilisateur | Entree CLI / webhook | `scripts/main_pipeline.py` | identique | Meme format d'entree |

### 12. Scripts Python necessaires

Pour chaque script :

#### `scripts/[nom].py`

- **Role** : [description]
- **Arguments** : `--arg1 value` (type, obligatoire/optionnel)
- **Sortie** : [format et destination]
- **Dependances Python** : `requests`, `anthropic`, etc.
- **Variables .env** : `API_KEY`, `TOKEN`
- **Remplace** : [noeud(s) n8n original(aux)]

### 13. Variables d'environnement

| Variable | Role | Obligatoire | Placeholder | Source originale |
|----------|------|-------------|-------------|-----------------|
| `TELEGRAM_BOT_TOKEN` | Auth Telegram Bot API | oui | `__A_REMPLIR__` | credential "telegram-bot" |

### 14. Plan d'implementation sequentiel

| Ordre | Objectif | Fichiers | Dependances | Risque | Critere de validation |
|-------|---------|---------|-------------|--------|----------------------|
| 1 | Creer structure + .env | Dossier skill | Aucune | Faible | Structure existe |
| 2 | Extraire prompts | `prompts/*.md` | Phase 1 validee | Faible | Prompts identiques au JSON |
| 3 | ... | ... | ... | ... | ... |

### 15. Criteres d'acceptation

- [ ] Un input equivalent au trigger original produit la sortie attendue
- [ ] Les prompts sont identiques a ceux extraits du JSON (diff = 0)
- [ ] Aucune cle sensible en dur dans le code
- [ ] Chaque appel API externe est fonctionnel avec les bons credentials
- [ ] Le pipeline respecte l'ordre de traitement original
- [ ] Les formats de sortie matchent ceux du workflow n8n
- [ ] Les zones incertaines sont documentees, pas devinées

---

## PHASE 3 — PROCHAINE ETAPE

### 16. Prochaine etape recommandee

[Indiquer precisement ce qu'il faut faire pour passer a l'implementation.
Lister les decisions en attente, les confirmations necessaires, les risques a lever.]

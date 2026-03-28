---
name: code-audit
description: |
  Détecte la dette technique, le code dupliqué, les patterns inconsistants et les dépendances
  inutiles dans un dépôt, puis génère un rapport actionnable. Déclenche pour "auditer le code",
  "dette technique", "code dupliqué", "dead code", "dépendances inutilisées", "scanner les TODO",
  "qualité du code", "candidats au refactoring".
---

# Code Audit & Technical Debt Scanner

Détecte la dette technique, le code dupliqué, les patterns inconsistants et les dépendances inutiles dans un dépôt, puis génère un rapport actionnable.

## Objectifs

- Identifier le code dupliqué avec précision (textuel et structurel)
- Recenser les marqueurs de dette technique (TODO, FIXME, HACK, XXX)
- Détecter les incohérences de patterns (nommage, architecture, style)
- Lister les dépendances déclarées mais non utilisées
- Produire un rapport priorisé avec preuves et recommandations concrètes

## Non-objectifs

- Corriger automatiquement le code (la skill propose, ne modifie pas)
- Remplacer les outils spécialisés (linters, SonarQube) mais les compléter
- Analyser la performance runtime ou les vulnérabilités de sécurité
- Générer des tests automatiquement

## Inputs

| Input              | Required | Default         | Description                                                   |
| ------------------ | -------- | --------------- | ------------------------------------------------------------- |
| `repo_path`        | Yes      | `.`             | Chemin du dépôt à analyser                                    |
| `language`         | No       | `auto`          | Langage : auto, javascript, typescript, python, java, go, php |
| `severity_level`   | No       | `balanced`      | Niveau : strict, balanced, lenient                            |
| `exclude_patterns` | No       | Voir ci-dessous | Patterns à ignorer                                            |

### Exclusions par défaut

```yaml
directories:
  - node_modules
  - vendor
  - dist
  - build
  - __pycache__
  - .git
  - coverage
  - .venv

files:
  - "*.min.js"
  - "*.bundle.js"
  - "*.spec.*"
  - "*.test.*"
  - "*.d.ts"
  - "*.map"
  - "package-lock.json"
  - "yarn.lock"
```

### Configuration avancée

```yaml
config:
  duplication:
    min_tokens: 50 # Minimum de tokens pour détecter duplication
    similarity_threshold: 85 # % de similarité (0-100)
  todo:
    keywords: ["TODO", "FIXME", "HACK", "XXX", "NOTE"]
    age_threshold_days: 90 # Considéré "ancien" après X jours
  dependencies:
    check_unused: true
  patterns:
    check_naming: true
    check_architecture: true
    check_error_handling: true
```

## Workflow

```
Démarrer
    │
    ▼
┌─────────────────────────────┐
│ 1. Détecter langage &       │
│    structure du projet      │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ 2. Indexer fichiers sources │
│    (exclure patterns)       │
└─────────────────────────────┘
    │
    ├──────────────────────────────────────┐
    │                                      │
    ▼                                      ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ 3a. Analyser    │  │ 3b. Scanner     │  │ 3c. Vérifier    │  │ 3d. Auditer     │
│ duplication     │  │ TODO/FIXME      │  │ patterns        │  │ dépendances     │
└─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────────┘
    │                    │                    │                    │
    └────────────────────┴────────────────────┴────────────────────┘
                                │
                                ▼
                    ┌─────────────────────────────┐
                    │ 4. Consolider findings      │
                    └─────────────────────────────┘
                                │
                                ▼
                    ┌─────────────────────────────┐
                    │ 5. Prioriser P0/P1/P2       │
                    └─────────────────────────────┘
                                │
                                ▼
                    ┌─────────────────────────────┐
                    │ 6. Générer rapport          │
                    │    (MD + JSON)              │
                    └─────────────────────────────┘
                                │
                                ▼
                              Fin
```

## Procedure

### Règles anti-hallucination

1. Cite TOUJOURS fichier + ligne pour chaque finding
2. Si tu ne trouves pas d'info : écris "Info manquante" ou pose 1 question (max 3)
3. N'invente JAMAIS de contenu de fichier
4. Utilise bash pour lire les fichiers réels
5. Base-toi sur les sorties d'outils réels (grep, find, npx depcheck, etc.)

### Étape 1 : Préparation

Détecter le langage et la structure du projet :

```bash
# Lister structure racine
ls -la [repo_path]

# Détecter package manager / langage
cat package.json || cat pyproject.toml || cat pom.xml || cat go.mod || cat composer.json

# Compter les fichiers source
find [repo_path] -type f \( -name "*.ts" -o -name "*.js" -o -name "*.py" -o -name "*.java" -o -name "*.go" -o -name "*.php" \) | wc -l
```

Si le niveau de sévérité n'est pas spécifié, utiliser `balanced`.

### Étape 2 : Analyse de duplication

Référence : [references/duplication-analysis.md](references/duplication-analysis.md)

```bash
# Méthode 1 : jscpd (si Node.js disponible)
npx jscpd src/ --min-tokens 50 --format json --output ./jscpd-report.json
cat jscpd-report.json

# Méthode 2 : Fallback avec hash de fichiers
find src/ -name "*.ts" -exec md5sum {} \; | sort | uniq -d -w 32
```

### Étape 3 : Détection TODO/FIXME

Référence : [references/todo-detection.md](references/todo-detection.md)

```bash
# Scanner tous les marqueurs
grep -rn 'TODO\|FIXME\|HACK\|XXX' src/ --include="*.ts" --include="*.js" --include="*.py"

# Dater avec git blame
git log --all --format="%H %ai" -- $(grep -rl "TODO" src/ | head -5)
```

### Étape 4 : Patterns inconsistants

Référence : [references/pattern-consistency.md](references/pattern-consistency.md)

```bash
# Nommage des fichiers
find src/ -type f | grep -E '(camelCase|snake_case)' | sort

# Architecture des dossiers
ls -R src/ | grep -E '(controller|service|helper|util)'

# Linting existant
npx eslint src/ --format json > eslint.json || echo "Pas d'ESLint configuré"
```

### Étape 5 : Dépendances inutilisées

Référence : [references/dependency-audit.md](references/dependency-audit.md)

```bash
# Node.js
npx depcheck --json

# Python
pip-autoremove --list

# Analyser les imports manuellement
grep -rh "^import\|^from\|require(" src/ | sort -u
```

### Étape 6 : Génération du rapport

1. Regrouper les findings par catégorie
2. Assigner sévérité P0/P1/P2 selon les critères ci-dessous
3. Calculer le health_score
4. Générer `audit-report.md` (format lisible)
5. Générer `audit.json` (format machine)

Référence : [assets/report-templates.md](assets/report-templates.md)

## Sévérités & Priorisation

### Niveaux de priorité

**P0 - Critique** : Impact immédiat sur maintenance/qualité

- Code dupliqué >90% similarité sur >50 lignes
- TODO critique >180 jours
- Patterns bloquant collaboration (conventions critiques)
- Dépendances inutilisées >5MB

**P1 - Important** : Impact moyen-terme

- Duplication 80-90% ou 20-50 lignes
- TODO 90-180 jours
- Incohérences répétées (>5 occurrences)
- Dépendances 1-5MB

**P2 - Mineur** : Amélioration qualité

- Duplication <80% ou <20 lignes
- TODO <90 jours
- Incohérences isolées (<5)
- Dépendances <1MB

### Seuils par niveau de sévérité

| Paramètre                | Strict | Balanced | Lenient |
| ------------------------ | ------ | -------- | ------- |
| min_tokens (duplication) | 30     | 50       | 80      |
| similarity_threshold     | 80%    | 85%      | 90%     |
| min_lines                | 5      | 8        | 12      |
| age_threshold (TODO)     | 30j    | 90j      | 180j    |

### Scoring de santé (0-100)

```
health_score = 100 - (P0_count * 10) - (P1_count * 3) - (P2_count * 1)
```

Plafonné entre 0 et 100.

**Interprétation :**

- 90-100 : Excellente santé
- 70-89 : Bonne santé
- 50-69 : Attention requise
- 0-49 : Intervention urgente

## Output Format

### Markdown (audit-report.md)

```markdown
# Audit de Code - [Nom du projet]

**Date :** [date]
**Langage principal :** [langage]
**Fichiers analysés :** [count]
**Score de santé :** [score]/100

## Findings Critiques (P0)

[Liste avec fichier:ligne, description, recommandation]

## Findings Importants (P1)

[Liste]

## Findings Mineurs (P2)

[Liste]

## Résumé

- Duplication : XX occurrences
- TODO : XX (XX anciens)
- Patterns : XX incohérences
- Dépendances : XX inutilisées
```

### JSON (audit.json)

```json
{
  "metadata": {
    "date": "2025-02-04T10:30:00Z",
    "repo_path": "./projet",
    "language": "typescript",
    "files_analyzed": 247,
    "health_score": 68
  },
  "findings": [
    {
      "id": "DUP-001",
      "category": "duplication",
      "severity": "P0",
      "title": "Code dupliqué détecté",
      "files": ["src/auth/login.ts", "src/auth/register.ts"],
      "lines": [
        [45, 78],
        [52, 85]
      ],
      "similarity": 92,
      "impact": "Maintenance difficile, risque d'incohérence",
      "recommendation": "Extraire la logique commune",
      "effort": "2h"
    }
  ],
  "summary": {
    "duplication": { "count": 12, "p0": 3, "p1": 7, "p2": 2 },
    "todo": { "count": 45, "old": 18, "recent": 27 },
    "patterns": { "count": 8, "p0": 1, "p1": 5, "p2": 2 },
    "dependencies": { "unused": 6, "size_impact_mb": 2.4 }
  }
}
```

## Gestion des erreurs

| Situation                        | Action                                       |
| -------------------------------- | -------------------------------------------- |
| Commande échoue                  | Log l'erreur, continuer avec autres analyses |
| Dépôt trop gros (>1000 fichiers) | Proposer de limiter le scope                 |
| Langage non supporté             | Analyse générique (grep, find)               |
| Outil manquant (jscpd, depcheck) | Utiliser méthode fallback                    |

## Stratégies anti-faux positifs

**Duplication :**

- Ignorer code généré (headers `@generated`)
- Exclure boilerplate inévitable (tests patterns)
- Valider que les blocs ont une vraie logique métier

**TODO :**

- Ignorer TODO dans documentation (README, docs/)
- Ignorer TODO accompagné d'un numéro d'issue (#123)
- Filtrer TODO dans code commenté

**Patterns :**

- Permettre exceptions documentées (`@eslint-disable`)
- Valider incohérence sur minimum 3 occurrences

**Dépendances :**

- Exclure dev dependencies si mode production
- Vérifier usages indirects (peer dependencies, types)

## Utilisation

### Commande directe

```
/code-audit [repo_path]
/code-audit . --severity strict
/code-audit src/ --language typescript --exclude "*.test.ts"
```

### Invocation contextuelle

L'utilisateur dit :

- "Audite ce dépôt" → Exécute le workflow complet
- "Trouve le code dupliqué" → Focus sur duplication
- "Liste les TODO" → Focus sur TODO/FIXME
- "Quelles dépendances sont inutilisées ?" → Focus sur dependencies

## Related Skills

- `06_Dev` pour les corrections WordPress
- `n8n-validation-expert` pour valider les workflows n8n

---

**Code Audit** — Détecte la dette technique, génère des rapports actionnables.

# Report Templates

Templates de sortie pour les rapports d'audit de code.

## Markdown Report (audit-report.md)

```markdown
# Audit de Code - [Nom du projet]

**Date :** [YYYY-MM-DD]
**Langage principal :** [TypeScript | JavaScript | Python | Java | Go | PHP]
**Fichiers analysés :** [nombre]
**Score de santé :** [0-100]/100

---

## Résumé exécutif

| Catégorie | Total | P0 | P1 | P2 |
|-----------|-------|----|----|----|
| Duplication | XX | X | X | X |
| TODO/FIXME | XX | X | X | X |
| Patterns | XX | X | X | X |
| Dépendances | XX | X | X | X |
| **Total** | **XX** | **X** | **X** | **X** |

### Score de santé : [SCORE]/100

- 90-100 : Excellente santé
- 70-89 : Bonne santé
- 50-69 : Attention requise
- 0-49 : Intervention urgente

---

## Findings Critiques (P0)

### [DUP-001] Code dupliqué détecté

**Fichiers :**
- `[path/to/file1.ts]` (L[start]-[end])
- `[path/to/file2.ts]` (L[start]-[end])

**Similarité :** [XX]%
**Lignes :** [XX]

**Impact :** [Description de l'impact]

**Recommandation :**
1. [Action 1]
2. [Action 2]
3. [Action 3]

**Effort estimé :** [Xh]

---

### [TODO-001] TODO critique ancien

**Fichier :** `[path/to/file.ts]` (L[line])
**Contenu :** `// [TODO content]`
**Âge :** [XXX] jours (ajouté le [YYYY-MM-DD])

**Impact :** [Description de l'impact]

**Recommandation :**
1. [Action 1]
2. [Action 2]

**Effort estimé :** [Xh]

---

## Findings Importants (P1)

### [PAT-001] Incohérence de nommage

**Détails :**
- [X] fichiers utilisent `[pattern1]`
- [X] fichiers utilisent `[pattern2]`

**Fichiers concernés :**
- `[file1]`
- `[file2]`
- `[file3]`

**Convention recommandée :** [pattern1]

**Recommandation :**
1. [Action 1]
2. [Action 2]

**Effort estimé :** [Xh]

---

### [DEP-001] Dépendance inutilisée

**Package :** `[package-name]` (v[version])
**Type :** [runtime | dev]
**Taille :** [X.X] MB

**Recommandation :**
```bash
npm uninstall [package-name]
```

**Effort estimé :** [Xmin]

---

## Findings Mineurs (P2)

| ID | Catégorie | Description | Fichier | Effort |
|----|-----------|-------------|---------|--------|
| [ID] | [cat] | [desc] | [file] | [Xh] |
| [ID] | [cat] | [desc] | [file] | [Xh] |
| [ID] | [cat] | [desc] | [file] | [Xh] |

---

## Statistiques détaillées

### Duplication

- **Blocs dupliqués :** [X]
- **Lignes totales dupliquées :** [X]
- **Pourcentage du codebase :** [X]%
- **Fichiers les plus concernés :**
  1. `[file1]` - [X] duplications
  2. `[file2]` - [X] duplications

### TODO/FIXME

| Type | Total | <90j | 90-180j | >180j |
|------|-------|------|---------|-------|
| TODO | X | X | X | X |
| FIXME | X | X | X | X |
| HACK | X | X | X | X |
| XXX | X | X | X | X |

### Patterns

- **Nommage fichiers :** [X]% cohérent
- **Architecture :** [by-feature | by-type | hybrid]
- **Violations ESLint :** [X]

### Dépendances

- **Inutilisées :** [X] ([X.X] MB)
- **Manquantes :** [X]
- **Outdated :** [X]

---

## Prochaines actions recommandées

### Priorité 1 (cette semaine)
- [ ] [Action P0]
- [ ] [Action P0]

### Priorité 2 (ce mois)
- [ ] [Action P1]
- [ ] [Action P1]

### Priorité 3 (backlog)
- [ ] [Action P2]
- [ ] [Action P2]

---

**Audit généré par Code Audit Skill**
**Date :** [YYYY-MM-DD HH:MM]
```

---

## JSON Report (audit.json)

```json
{
  "metadata": {
    "date": "2025-02-04T10:30:00Z",
    "repo_path": "./projet",
    "language": "typescript",
    "files_analyzed": 247,
    "lines_analyzed": 15420,
    "health_score": 68,
    "severity_level": "balanced",
    "excluded_patterns": [
      "node_modules",
      "dist",
      "*.test.ts"
    ]
  },
  "findings": [
    {
      "id": "DUP-001",
      "category": "duplication",
      "severity": "P0",
      "title": "Code dupliqué détecté",
      "description": "Logique de validation identique dans deux fichiers",
      "files": [
        {
          "path": "src/auth/login.ts",
          "start_line": 45,
          "end_line": 78
        },
        {
          "path": "src/auth/register.ts",
          "start_line": 52,
          "end_line": 85
        }
      ],
      "metrics": {
        "similarity": 92,
        "lines": 33,
        "tokens": 156
      },
      "impact": "Maintenance difficile, risque d'incohérence lors de modifications",
      "recommendation": "Extraire la logique commune dans src/auth/validators.ts",
      "effort_hours": 2,
      "tags": ["auth", "validation"]
    },
    {
      "id": "TODO-001",
      "category": "todo",
      "severity": "P1",
      "title": "TODO ancien non traité",
      "description": "TODO: Implémenter retry logic",
      "files": [
        {
          "path": "src/payment/stripe.ts",
          "line": 124
        }
      ],
      "metrics": {
        "age_days": 145,
        "created_date": "2024-09-12",
        "commit": "abc123"
      },
      "has_issue_link": false,
      "impact": "Fiabilité des paiements compromise",
      "recommendation": "Créer issue GitHub et implémenter ou supprimer",
      "effort_hours": 4,
      "tags": ["payment", "reliability"]
    },
    {
      "id": "PAT-001",
      "category": "pattern",
      "severity": "P1",
      "title": "Incohérence de nommage de fichiers",
      "description": "Mix de camelCase et snake_case",
      "files": [
        {
          "path": "src/utils/string_utils.ts",
          "convention": "snake_case"
        },
        {
          "path": "src/helpers/dateHelper.ts",
          "convention": "camelCase"
        }
      ],
      "metrics": {
        "camelCase_count": 45,
        "snake_case_count": 3,
        "kebab_case_count": 0
      },
      "impact": "Confusion, maintenance difficile",
      "recommendation": "Standardiser sur camelCase, renommer les 3 fichiers",
      "effort_hours": 2,
      "tags": ["naming", "convention"]
    },
    {
      "id": "DEP-001",
      "category": "dependency",
      "severity": "P1",
      "title": "Dépendance inutilisée",
      "description": "Package lodash non utilisé dans le code",
      "packages": [
        {
          "name": "lodash",
          "version": "4.17.21",
          "type": "runtime",
          "size_mb": 1.4
        }
      ],
      "impact": "Bundle size inutile, surface d'attaque élargie",
      "recommendation": "npm uninstall lodash",
      "effort_hours": 0.25,
      "tags": ["cleanup", "bundle-size"]
    }
  ],
  "summary": {
    "total_findings": 15,
    "by_severity": {
      "P0": 2,
      "P1": 8,
      "P2": 5
    },
    "duplication": {
      "count": 5,
      "total_lines": 245,
      "percentage": 1.6,
      "by_severity": { "P0": 1, "P1": 3, "P2": 1 }
    },
    "todo": {
      "count": 45,
      "by_type": {
        "TODO": 30,
        "FIXME": 10,
        "HACK": 3,
        "XXX": 2
      },
      "by_age": {
        "recent": 27,
        "old": 12,
        "critical": 6
      },
      "with_issues": 8,
      "without_issues": 37,
      "by_severity": { "P0": 0, "P1": 3, "P2": 2 }
    },
    "patterns": {
      "count": 3,
      "naming_consistency": 94,
      "architecture_type": "by-feature",
      "by_severity": { "P0": 0, "P1": 2, "P2": 1 }
    },
    "dependencies": {
      "unused_count": 6,
      "unused_size_mb": 8.4,
      "missing_count": 0,
      "outdated_count": 12,
      "by_severity": { "P0": 1, "P1": 0, "P2": 1 }
    },
    "estimated_effort_hours": 24
  },
  "recommendations": {
    "priority_1": [
      {
        "action": "Supprimer moment.js inutilisé",
        "finding_ids": ["DEP-002"],
        "effort_hours": 0.5
      },
      {
        "action": "Extraire validateurs dupliqués",
        "finding_ids": ["DUP-001"],
        "effort_hours": 2
      }
    ],
    "priority_2": [
      {
        "action": "Traiter TODO critiques",
        "finding_ids": ["TODO-001", "TODO-002", "TODO-003"],
        "effort_hours": 12
      }
    ],
    "priority_3": [
      {
        "action": "Standardiser nommage fichiers",
        "finding_ids": ["PAT-001"],
        "effort_hours": 3
      }
    ]
  }
}
```

---

## CSV Export (findings.csv)

Pour import dans Excel/Google Sheets :

```csv
id,category,severity,title,file,line_start,line_end,impact,recommendation,effort_hours,date_found
DUP-001,duplication,P0,"Code dupliqué",src/auth/login.ts,45,78,"Maintenance difficile","Extraire dans validators.ts",2,2025-02-04
DUP-001,duplication,P0,"Code dupliqué",src/auth/register.ts,52,85,"Maintenance difficile","Extraire dans validators.ts",2,2025-02-04
TODO-001,todo,P1,"TODO ancien",src/payment/stripe.ts,124,124,"Fiabilité paiements","Créer issue GitHub",4,2025-02-04
PAT-001,pattern,P1,"Nommage inconsistant",src/utils/string_utils.ts,,,,"Renommer en camelCase",2,2025-02-04
DEP-001,dependency,P1,"Dépendance inutilisée",package.json,,,"Bundle size","npm uninstall lodash",0.25,2025-02-04
```

---

## Génération des rapports

### Script de génération

```bash
#!/bin/bash
# generate-audit-report.sh

PROJECT_NAME=$(basename $(pwd))
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

OUTPUT_DIR="./audit-reports"
mkdir -p "$OUTPUT_DIR"

# Générer les fichiers
echo "Generating audit reports for $PROJECT_NAME..."

# Les contenus sont générés par Claude pendant l'audit
# et écrits dans ces fichiers :

# - $OUTPUT_DIR/audit-report_$TIMESTAMP.md
# - $OUTPUT_DIR/audit_$TIMESTAMP.json
# - $OUTPUT_DIR/findings_$TIMESTAMP.csv

echo "Reports generated in $OUTPUT_DIR/"
```

### Nommage des fichiers

```
audit-reports/
├── audit-report_20250204_103000.md
├── audit_20250204_103000.json
└── findings_20250204_103000.csv
```

---

## Personnalisation

### Variables à remplacer

| Variable | Description |
|----------|-------------|
| `[Nom du projet]` | Nom du dépôt ou projet |
| `[YYYY-MM-DD]` | Date de l'audit |
| `[XX]` | Valeur numérique |
| `[path/to/file.ts]` | Chemin relatif du fichier |
| `[L[start]-[end]]` | Numéros de lignes |

### Sections optionnelles

Selon le scope de l'audit, certaines sections peuvent être omises :

- `--no-duplication` : Omettre section duplication
- `--no-todo` : Omettre section TODO
- `--no-patterns` : Omettre section patterns
- `--no-deps` : Omettre section dépendances

---

Retour à [SKILL.md](../SKILL.md)

# Pattern Consistency Procedure

Détecter les incohérences de patterns (nommage, architecture, style).

## Types d'incohérences

### 1. Nommage

| Élément | Convention attendue | Exemple |
|---------|---------------------|---------|
| Fichiers | kebab-case ou camelCase | `user-service.ts` / `userService.ts` |
| Classes | PascalCase | `UserController` |
| Fonctions | camelCase | `getUserById` |
| Constantes | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| Variables | camelCase | `userName` |
| Interfaces | PascalCase (avec I préfixe optionnel) | `IUserService` / `UserService` |

### 2. Architecture

| Pattern | Description |
|---------|-------------|
| Par feature | `/features/auth/`, `/features/payment/` |
| Par type | `/controllers/`, `/services/`, `/models/` |
| Hybride | Feature-first avec sous-dossiers par type |

### 3. Style de code

| Aspect | Variations |
|--------|------------|
| Error handling | try-catch vs return Error vs Result type |
| Async | Callbacks vs Promises vs async/await |
| Imports | Named vs Default exports |
| State | Mutable vs Immutable |

## Commandes de détection

### Nommage des fichiers

```bash
# Lister tous les fichiers source
find src/ -type f -name "*.ts" -o -name "*.js" | sort

# Détecter snake_case dans un projet camelCase
find src/ -type f | grep -E '_[a-z]' | grep -v node_modules

# Détecter camelCase dans un projet kebab-case
find src/ -type f | grep -E '[a-z][A-Z]' | grep -v node_modules

# Compter les conventions utilisées
find src/ -type f -name "*.ts" | while read f; do
  basename "$f"
done | grep -E '^[a-z]+(-[a-z]+)+\.ts$' | wc -l  # kebab-case

find src/ -type f -name "*.ts" | while read f; do
  basename "$f"
done | grep -E '^[a-z]+([A-Z][a-z]+)*\.ts$' | wc -l  # camelCase
```

### Architecture des dossiers

```bash
# Lister la structure de premier niveau
ls -d src/*/ 2>/dev/null | head -20

# Détecter pattern "par type"
ls -d src/*/ | grep -E '(controller|service|model|util|helper|middleware)s?$'

# Détecter pattern "par feature"
ls -d src/*/ | grep -E '(auth|user|payment|order|product)'

# Compter fichiers par pattern
echo "Controllers:" && find src/ -name "*controller*" -o -name "*Controller*" | wc -l
echo "Services:" && find src/ -name "*service*" -o -name "*Service*" | wc -l
echo "Models:" && find src/ -name "*model*" -o -name "*Model*" | wc -l
```

### Conventions de code

```bash
# Détecter usage de console.log (vs logger)
grep -rn 'console.log\|console.error' src/ --include="*.ts" --include="*.js" | wc -l

# Compter try-catch vs .catch()
echo "try-catch:" && grep -rn 'try\s*{' src/ | wc -l
echo ".catch():" && grep -rn '\.catch(' src/ | wc -l

# Exports default vs named
echo "Default exports:" && grep -rn 'export default' src/ | wc -l
echo "Named exports:" && grep -rn 'export {' src/ | wc -l
echo "Export const/function:" && grep -rn 'export const\|export function\|export class' src/ | wc -l
```

### ESLint existant

```bash
# Vérifier si ESLint est configuré
cat .eslintrc.json 2>/dev/null || cat .eslintrc.js 2>/dev/null || cat .eslintrc 2>/dev/null

# Exécuter ESLint pour trouver les violations
npx eslint src/ --format json 2>/dev/null

# Compter violations par règle
npx eslint src/ --format json 2>/dev/null | jq '[.[] | .messages[] | .ruleId] | group_by(.) | map({rule: .[0], count: length}) | sort_by(-.count)'
```

## Classification des findings

### P0 - Critique

- Conventions contradictoires dans le même fichier
- Nommage qui cause des bugs (casse sensible)
- Architecture empêchant la collaboration

### P1 - Important

- Incohérence répétée (>5 occurrences)
- Convention majoritaire non respectée (>20% déviation)
- Patterns mixtes dans le même module

### P2 - Mineur

- Incohérences isolées (<5 occurrences)
- Fichiers legacy en cours de migration
- Variations acceptables (kebab vs camelCase pour fichiers)

## Faux positifs à ignorer

1. **Code tiers** : node_modules, vendor
2. **Fichiers de config** : Conventions imposées (.eslintrc, tsconfig)
3. **Code généré** : Types générés, migrations
4. **Conventions documentées** : Exceptions explicites dans CONTRIBUTING.md
5. **Migration en cours** : Fichiers marqués pour refactoring

## Template de finding

```markdown
**[PAT-XXX]** Incohérence de nommage

**Détails :**
- 12 fichiers utilisent `camelCase.ts`
- 8 fichiers utilisent `kebab-case.ts`

**Fichiers concernés :**
- `user_service.ts` (snake_case - minoritaire)
- `orderService.ts` (camelCase - majoritaire)
- `payment-handler.ts` (kebab-case - minoritaire)

**Convention recommandée :** camelCase (majorité actuelle)

**Impact :** Confusion, imports incorrects possibles, maintenance difficile.

**Recommandation :**
1. Choisir standard : `camelCase.ts` (convention TS/JS courante)
2. Renommer les 8 fichiers non conformes
3. Documenter dans `CONTRIBUTING.md`
4. Ajouter règle ESLint : `unicorn/filename-case`

**Effort estimé :** 3h + validation CI
```

## Rapport pattern

### Format de sortie

```json
{
  "patterns": {
    "naming": {
      "files": {
        "camelCase": 45,
        "kebab-case": 12,
        "snake_case": 3
      },
      "majority": "camelCase",
      "deviations": ["src/utils/string_utils.ts", "src/helpers/date-helper.ts"]
    },
    "architecture": {
      "type": "by-feature",
      "consistency": 85,
      "violations": ["/src/helpers/", "/src/utils/"]
    },
    "code_style": {
      "error_handling": { "try-catch": 45, "promise-catch": 12 },
      "exports": { "named": 120, "default": 8 },
      "logging": { "console": 15, "logger": 45 }
    }
  },
  "findings": [
    {
      "id": "PAT-001",
      "category": "naming",
      "severity": "P1",
      "description": "File naming inconsistency",
      "details": "3 files use snake_case in a camelCase project",
      "files": ["string_utils.ts", "date_helper.ts", "api_client.ts"]
    }
  ]
}
```

## Bonnes pratiques

### Configuration ESLint recommandée

```json
{
  "rules": {
    "@typescript-eslint/naming-convention": [
      "error",
      { "selector": "default", "format": ["camelCase"] },
      { "selector": "variable", "format": ["camelCase", "UPPER_CASE"] },
      { "selector": "typeLike", "format": ["PascalCase"] }
    ],
    "unicorn/filename-case": ["error", { "case": "camelCase" }]
  }
}
```

### Documentation des conventions

Créer un fichier `CONTRIBUTING.md` ou `CONVENTIONS.md` :

```markdown
# Code Conventions

## Nommage
- Fichiers : camelCase.ts
- Classes : PascalCase
- Fonctions/variables : camelCase
- Constantes : UPPER_SNAKE_CASE

## Architecture
- Structure par feature : /src/features/{feature}/
- Sous-dossiers : /components, /hooks, /services

## Exceptions autorisées
- Fichiers de config : lowercase (tsconfig.json)
- Tests : {name}.test.ts ou {name}.spec.ts
```

---

Retour à [SKILL.md](../SKILL.md)

# Dependency Audit Procedure

Identifier les dépendances déclarées mais non utilisées.

## Par écosystème

### Node.js / JavaScript / TypeScript

#### Outil principal : depcheck

```bash
# Installation
npm install -g depcheck

# Analyse basique
npx depcheck

# Format JSON pour traitement
npx depcheck --json > depcheck-report.json

# Options utiles
npx depcheck --ignores="@types/*,eslint*" --skip-missing
```

**Lecture du rapport :**

```json
{
  "dependencies": ["lodash", "moment"],     // Non utilisées
  "devDependencies": ["jest"],               // Non utilisées (dev)
  "missing": {"axios": ["src/api.ts"]},      // Utilisées mais non déclarées
  "invalidFiles": {},
  "invalidDirs": {}
}
```

#### Analyse manuelle des imports

```bash
# Lister toutes les dépendances déclarées
cat package.json | jq '.dependencies | keys[]'
cat package.json | jq '.devDependencies | keys[]'

# Lister tous les imports utilisés
grep -roh "from ['\"][^'\"]*['\"]" src/ | sort -u | sed "s/from ['\"]//;s/['\"]$//"
grep -roh "require(['\"][^'\"]*['\"])" src/ | sort -u

# Comparer (manuel)
```

### Python

#### Outil : pip-autoremove

```bash
# Installation
pip install pip-autoremove

# Lister candidates à supprimer
pip-autoremove --list

# Désinstaller (interactif)
pip-autoremove <package>
```

#### Analyse manuelle

```bash
# Lister dépendances déclarées
cat requirements.txt | grep -v '^#' | cut -d'=' -f1

# Ou depuis pyproject.toml
cat pyproject.toml | grep -A 100 '\[project.dependencies\]'

# Lister imports utilisés
grep -roh '^import \w\+\|^from \w\+' src/ | sort -u | awk '{print $2}'

# Outil : pipreqs (génère requirements depuis imports réels)
pip install pipreqs
pipreqs src/ --print
```

#### Outil : pip-audit (sécurité)

```bash
pip install pip-audit
pip-audit
```

### Java (Maven)

```bash
# Analyse des dépendances inutilisées
mvn dependency:analyze

# Rapport détaillé
mvn dependency:analyze -DoutputXML=true

# Arbre de dépendances
mvn dependency:tree
```

### PHP (Composer)

```bash
# Lister dépendances
composer show --direct

# Analyser (outil tiers)
composer require --dev icanhazstring/composer-unused
composer unused
```

### Go

```bash
# Modules inutilisés
go mod tidy -v 2>&1 | grep "unused"

# Lister dépendances
go list -m all
```

## Classification des findings

### Par taille

| Taille | Sévérité | Action |
|--------|----------|--------|
| >5 MB | P0 | Supprimer immédiatement |
| 1-5 MB | P1 | Planifier suppression |
| <1 MB | P2 | Supprimer quand possible |

### Par type

| Type | Impact |
|------|--------|
| Runtime dependency inutilisée | Bundle size, surface d'attaque |
| Dev dependency inutilisée | CI/CD plus lent, confusion |
| Peer dependency manquante | Bugs potentiels |
| Type definition inutilisée | Minimal (dev only) |

## Faux positifs à ignorer

1. **Dépendances implicites**
   - Peer dependencies
   - Plugins (webpack, babel, eslint)
   - Dépendances de build non importées

2. **Types TypeScript**
   - `@types/*` souvent détectés comme inutilisés
   - Nécessaires pour compilation

3. **CLI tools**
   - Scripts npm sans import
   - Outils de dev (prettier, husky)

4. **Polyfills et shims**
   - core-js, regenerator-runtime
   - Importés mais pas explicitement utilisés

### Exclusions recommandées

```bash
# depcheck avec exclusions
npx depcheck --ignores="@types/*,eslint*,prettier,husky,lint-staged,typescript,jest,@babel/*,webpack*"
```

## Template de finding

```markdown
**[DEP-XXX]** Dépendance inutilisée

**Package :** `lodash` (v4.17.21)
**Type :** runtime dependency
**Taille :** 1.4 MB (unpacked)
**Dernière utilisation :** Aucune trace dans src/

**Impact :**
- Bundle size inutile (+1.4 MB)
- Surface d'attaque sécurité élargie
- Maintenance des mises à jour inutile

**Vérification :**
```bash
grep -r "lodash\|_\." src/  # Aucun résultat
```

**Recommandation :**
```bash
npm uninstall lodash
npm test  # Vérifier que les tests passent
```

**Effort estimé :** 15min
```

## Rapport dépendances

### Format de sortie

```json
{
  "dependencies": {
    "unused": [
      {
        "name": "lodash",
        "version": "4.17.21",
        "type": "runtime",
        "size_mb": 1.4,
        "severity": "P1"
      },
      {
        "name": "moment",
        "version": "2.29.4",
        "type": "runtime",
        "size_mb": 4.2,
        "severity": "P0"
      }
    ],
    "missing": [
      {
        "name": "axios",
        "usedIn": ["src/api/client.ts", "src/services/http.ts"]
      }
    ],
    "outdated": [
      {
        "name": "react",
        "current": "17.0.2",
        "latest": "18.2.0"
      }
    ]
  },
  "summary": {
    "total_unused": 6,
    "total_size_mb": 8.4,
    "security_advisories": 2
  }
}
```

## Commandes utiles

### Taille des dépendances

```bash
# Taille de node_modules
du -sh node_modules/

# Taille par package (top 20)
du -sh node_modules/*/ | sort -rh | head -20

# Package spécifique
du -sh node_modules/lodash/

# Avec npm
npm ls --all | wc -l  # Nombre total
```

### Vérification de sécurité

```bash
# npm audit
npm audit --json

# yarn audit
yarn audit --json

# Snyk (plus complet)
npx snyk test
```

### Mise à jour

```bash
# Packages outdated
npm outdated

# Mise à jour interactive
npx npm-check-updates -i

# Mise à jour sécurité uniquement
npm audit fix
```

## Bonnes pratiques

### Nettoyage régulier

1. Exécuter `depcheck` mensuellement
2. Vérifier avant chaque release
3. Automatiser dans CI/CD

### Remplacement de gros packages

| Package lourd | Alternative légère |
|---------------|-------------------|
| moment (4.2 MB) | date-fns (tree-shakeable) |
| lodash (1.4 MB) | lodash-es (tree-shakeable) |
| axios (0.4 MB) | fetch natif |

### Script de nettoyage

```bash
#!/bin/bash
# clean-deps.sh

echo "=== Analyzing unused dependencies ==="
npx depcheck --json > /tmp/depcheck.json

unused=$(cat /tmp/depcheck.json | jq -r '.dependencies[]')
if [ -n "$unused" ]; then
  echo "Unused dependencies found:"
  echo "$unused"
  read -p "Remove all? (y/n) " confirm
  if [ "$confirm" = "y" ]; then
    echo "$unused" | xargs npm uninstall
  fi
else
  echo "No unused dependencies found!"
fi
```

---

Retour à [SKILL.md](../SKILL.md)

# Duplication Analysis Procedure

Détection du code dupliqué dans un dépôt.

## Méthodes de détection

### Méthode 1 : JSCPD (JavaScript/TypeScript)

Outil recommandé pour les projets Node.js.

```bash
# Installation si nécessaire
npm install -g jscpd

# Analyse avec rapport JSON
npx jscpd [path] --min-tokens 50 --format json --output ./jscpd-report.json

# Options courantes
--min-tokens 50       # Minimum de tokens (default: 50)
--min-lines 5         # Minimum de lignes
--threshold 0         # Seuil de pourcentage global accepté
--ignore "**/*.test.*,**/node_modules/**"
```

**Lecture du rapport :**

```json
{
  "duplicates": [
    {
      "firstFile": { "name": "src/auth/login.ts", "start": 45, "end": 78 },
      "secondFile": { "name": "src/auth/register.ts", "start": 52, "end": 85 },
      "lines": 33,
      "tokens": 156
    }
  ],
  "statistics": {
    "total": { "lines": 5000, "tokens": 25000 },
    "duplicated": { "lines": 500, "tokens": 2500 },
    "percentage": 10
  }
}
```

### Méthode 2 : PMD CPD (Multi-langage)

Fonctionne avec Java, Python, PHP, Go, etc.

```bash
# Télécharger PMD
# https://pmd.github.io/

# Exécution
pmd cpd --minimum-tokens 50 --dir src/ --language java --format json
```

### Méthode 3 : Fallback manuel (grep + hash)

Quand aucun outil n'est disponible.

```bash
# Identifier fichiers avec contenu similaire (hash)
find src/ -name "*.ts" -exec md5sum {} \; | sort | uniq -d -w 32

# Rechercher patterns répétés
grep -roh '\bfunction\s\+\w\+\s*([^)]*)\s*{[^}]*}' src/ | sort | uniq -c | sort -rn | head -20
```

## Seuils par niveau

| Paramètre | Strict | Balanced | Lenient |
|-----------|--------|----------|---------|
| min_tokens | 30 | 50 | 80 |
| similarity_threshold | 80% | 85% | 90% |
| min_lines | 5 | 8 | 12 |

## Classification des findings

### P0 - Critique
- Similarité >90%
- Plus de 50 lignes dupliquées
- Logique métier critique

### P1 - Important
- Similarité 80-90%
- Entre 20 et 50 lignes
- Code fonctionnel répété

### P2 - Mineur
- Similarité <80%
- Moins de 20 lignes
- Boilerplate acceptable

## Faux positifs à ignorer

1. **Code généré** : Fichiers avec header `@generated`
2. **Tests** : Patterns de tests similaires (describe, it, expect)
3. **Configuration** : Fichiers de config répétitifs
4. **Imports** : Blocs d'imports identiques
5. **Constantes** : Déclarations de constantes similaires

## Template de finding

```markdown
**[DUP-XXX]** Code dupliqué détecté

**Fichiers :**
- `src/auth/login.ts` (L45-78)
- `src/auth/register.ts` (L52-85)

**Similarité :** 92%
**Lignes :** 33

**Impact :** Maintenance difficile, risque de bugs asymétriques lors de modifications.

**Recommandation :**
1. Créer `src/auth/validators.ts`
2. Extraire la fonction `validateCredentials()`
3. Importer dans les deux fichiers

**Code suggéré :**
```typescript
// src/auth/validators.ts
export function validateCredentials(email: string, password: string): boolean {
  // Logique commune extraite
}
```

**Effort estimé :** 1-2h
```

## Commandes de diagnostic

```bash
# Compter le pourcentage de duplication global
npx jscpd src/ --reporters console

# Visualiser les duplications (HTML)
npx jscpd src/ --format html --output ./duplication-report/

# Exclure certains fichiers
npx jscpd src/ --ignore "**/*.test.ts,**/*.spec.ts,**/index.ts"
```

## Bonnes pratiques de refactoring

### Extraction de fonction

```typescript
// AVANT (dupliqué dans 2 fichiers)
const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!regex.test(email)) {
  throw new Error("Invalid email");
}

// APRÈS (centralisé)
// src/utils/validators.ts
export const isValidEmail = (email: string): boolean => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
};

export const validateEmail = (email: string): void => {
  if (!isValidEmail(email)) {
    throw new Error("Invalid email");
  }
};
```

### Extraction de classe

Pour logique plus complexe, créer une classe ou un module dédié.

### Factory pattern

Pour création d'objets similaires répétée.

---

Retour à [SKILL.md](../SKILL.md)

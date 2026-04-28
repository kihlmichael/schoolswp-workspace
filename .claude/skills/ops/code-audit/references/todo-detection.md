# TODO Detection Procedure

Scanner et classifier les marqueurs de dette technique (TODO, FIXME, HACK, XXX).

## Mots-clés recherchés

| Keyword | Signification | Priorité typique |
|---------|---------------|------------------|
| `TODO` | Fonctionnalité à implémenter | P2 (récent) → P1 (ancien) |
| `FIXME` | Bug connu à corriger | P1 → P0 |
| `HACK` | Solution temporaire/contournement | P1 |
| `XXX` | Attention requise / code dangereux | P0 |
| `NOTE` | Information contextuelle | Info |
| `OPTIMIZE` | Performance à améliorer | P2 |
| `REFACTOR` | Code à restructurer | P2 |

## Commandes de scan

### Scan basique

```bash
# Tous les marqueurs
grep -rn 'TODO\|FIXME\|HACK\|XXX\|NOTE' src/ --include="*.ts" --include="*.js" --include="*.py"

# Avec contexte (2 lignes avant/après)
grep -rn -C 2 'TODO\|FIXME\|HACK\|XXX' src/

# Compter par type
grep -roh 'TODO\|FIXME\|HACK\|XXX' src/ | sort | uniq -c | sort -rn
```

### Datation avec Git

```bash
# Trouver l'âge d'un TODO spécifique
git blame -L <line>,<line> <file> | awk '{print $1, $3, $4}'

# Lister les fichiers contenant des TODO avec leur date de dernière modification
git log --all --format="%H %ai" -- $(grep -rl "TODO" src/)

# TODO les plus anciens (commits)
for file in $(grep -rl "TODO" src/); do
  echo "=== $file ==="
  git log -1 --format="%ai" -- "$file"
done
```

### Scan avancé

```bash
# TODO avec numéro d'issue GitHub (à ignorer)
grep -rn 'TODO(#[0-9]\+)' src/

# TODO sans issue associée (à traiter)
grep -rn 'TODO' src/ | grep -v 'TODO(#[0-9]\+)'

# TODO dans le code actif (exclure commenté)
grep -rn '^\s*//\s*TODO\|^\s*#\s*TODO\|^\s*\*\s*TODO' src/
```

## Classification par âge

| Âge | Strict | Balanced | Lenient |
|-----|--------|----------|---------|
| Récent | <30j | <90j | <180j |
| Ancien | 30-90j | 90-180j | 180-365j |
| Critique | >90j | >180j | >365j |

### Script de datation

```bash
#!/bin/bash
# date-todos.sh

for file in $(grep -rl "TODO\|FIXME" src/); do
  while IFS=: read -r line_num content; do
    commit=$(git blame -L "$line_num,$line_num" "$file" 2>/dev/null | awk '{print $1}')
    if [ -n "$commit" ] && [ "$commit" != "00000000" ]; then
      date=$(git show -s --format=%ai "$commit" 2>/dev/null)
      echo "$file:$line_num | $date | $content"
    fi
  done < <(grep -n "TODO\|FIXME" "$file")
done
```

## Faux positifs à ignorer

1. **Documentation** : TODO dans README.md, docs/, CHANGELOG
2. **Avec issue** : `TODO(#123)` ou `TODO @issue/123`
3. **Code commenté** : Blocs de code désactivés contenant TODO
4. **Dépendances** : node_modules, vendor, etc.
5. **Tests** : TODO dans fichiers de test (parfois acceptables)

### Pattern d'exclusion

```bash
# Exclure documentation et tests
grep -rn 'TODO\|FIXME' src/ \
  --exclude-dir=docs \
  --exclude-dir=__tests__ \
  --exclude="*.md" \
  --exclude="*.test.*"
```

## Template de finding

```markdown
**[TODO-XXX]** TODO ancien non traité

**Fichier :** `src/payment/stripe.ts` (L124)
**Contenu :** `// TODO: Implémenter retry logic pour les erreurs réseau`
**Âge :** 145 jours (ajouté le 2024-09-12)
**Commit :** abc123

**Impact :** Fiabilité des paiements compromise en cas d'erreur réseau.

**Recommandation :**
1. Créer issue GitHub : "Implémenter retry logic Stripe"
2. Modifier le commentaire : `// TODO(#456): Retry logic`
3. OU implémenter directement si prioritaire

**Code suggéré :**
```typescript
async function processPayment(amount: number, retries = 3): Promise<PaymentResult> {
  for (let i = 0; i < retries; i++) {
    try {
      return await stripe.charges.create({ amount });
    } catch (error) {
      if (i === retries - 1) throw error;
      await delay(1000 * Math.pow(2, i)); // Exponential backoff
    }
  }
}
```

**Effort estimé :** 4h
```

## Rapport par catégorie

### Format de sortie

```json
{
  "todos": [
    {
      "id": "TODO-001",
      "type": "TODO",
      "file": "src/auth/login.ts",
      "line": 45,
      "content": "TODO: Add password strength validation",
      "date": "2024-06-15",
      "age_days": 234,
      "has_issue": false,
      "severity": "P1"
    }
  ],
  "summary": {
    "total": 45,
    "by_type": { "TODO": 30, "FIXME": 10, "HACK": 3, "XXX": 2 },
    "by_age": { "recent": 27, "old": 12, "critical": 6 },
    "with_issues": 8,
    "without_issues": 37
  }
}
```

## Bonnes pratiques

### Format de TODO recommandé

```typescript
// TODO(#123): Description courte
// @author: john.doe
// @date: 2024-01-15
// @priority: high
```

### Workflow de traitement

1. **Triage** : Identifier TODO sans issue
2. **Créer issues** : Pour chaque TODO important
3. **Lier** : Ajouter référence `(#xxx)` au TODO
4. **Planifier** : Intégrer dans sprints
5. **Résoudre** : Implémenter et supprimer TODO

---

Retour à [SKILL.md](../SKILL.md)

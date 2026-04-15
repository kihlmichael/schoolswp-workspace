#!/bin/bash
# verify-consolidation.sh — Vérifie l'état de consolidation du workspace schoolsWP
# Usage : bash scripts/verify-consolidation.sh

set -e

echo "=== Vérification de consolidation — schoolsWP ==="
echo ""

ERRORS=0
WARNINGS=0

# 1. Vérifier l'absence de chemins skills dupliqués
echo "1. Chemins skills dupliqués..."
if [ -d ".agent/skills" ] || [ -d ".agents/skills" ]; then
    echo "   ❌ ERREUR : Chemins skills dupliqués détectés"
    [ -d ".agent/skills" ] && echo "      → .agent/skills/ existe"
    [ -d ".agents/skills" ] && echo "      → .agents/skills/ existe"
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Aucun doublon détecté"
fi

# 2. Vérifier l'absence de fichiers patch à la racine
echo "2. Fichiers temporaires à la racine..."
PATCH_FILES=$(find . -maxdepth 1 -name "patch_*" -o -name "temp_*" -o -name "backup_*" 2>/dev/null | head -10)
if [ -n "$PATCH_FILES" ]; then
    echo "   ❌ ERREUR : Fichiers temporaires à la racine"
    echo "$PATCH_FILES" | while read f; do echo "      → $f"; done
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Racine propre"
fi

# 3. Vérifier que .claude/skills/ existe
echo "3. Dossier skills officiel..."
if [ -d ".claude/skills" ]; then
    SKILL_COUNT=$(ls -d .claude/skills/*/ 2>/dev/null | wc -l)
    echo "   ✅ .claude/skills/ existe ($SKILL_COUNT skills)"
else
    echo "   ⚠️  AVERTISSEMENT : .claude/skills/ n'existe pas encore"
    WARNINGS=$((WARNINGS + 1))
fi

# 4. Vérifier que docs/lessons.md existe
echo "4. Journal des leçons..."
if [ -f "docs/lessons.md" ]; then
    LESSON_COUNT=$(grep -c "^## " docs/lessons.md 2>/dev/null || echo "0")
    echo "   ✅ docs/lessons.md existe ($LESSON_COUNT entrées)"
else
    echo "   ⚠️  AVERTISSEMENT : docs/lessons.md n'existe pas"
    WARNINGS=$((WARNINGS + 1))
fi

# 5. Vérifier que le CHANGELOG existe
echo "5. CHANGELOG..."
if [ -f "docs/CHANGELOG.md" ] || [ -f "CHANGELOG.md" ]; then
    echo "   ✅ CHANGELOG trouvé"
else
    echo "   ⚠️  AVERTISSEMENT : Pas de CHANGELOG"
    WARNINGS=$((WARNINGS + 1))
fi

# 6. Vérifier la structure data/
echo "6. Structure data/..."
if [ -d "data" ]; then
    SUBDIRS=0
    [ -d "data/raw" ] && SUBDIRS=$((SUBDIRS + 1))
    [ -d "data/processed" ] && SUBDIRS=$((SUBDIRS + 1))
    [ -d "data/exports" ] && SUBDIRS=$((SUBDIRS + 1))
    if [ $SUBDIRS -eq 3 ]; then
        echo "   ✅ Structure data/ complète"
    else
        echo "   ⚠️  AVERTISSEMENT : Structure data/ incomplète ($SUBDIRS/3 sous-dossiers)"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "   ⚠️  AVERTISSEMENT : Pas de dossier data/"
    WARNINGS=$((WARNINGS + 1))
fi

# 7. Vérifier les tags git
echo "7. Tags git..."
if git rev-parse --git-dir > /dev/null 2>&1; then
    TAG_COUNT=$(git tag -l "v*" 2>/dev/null | wc -l)
    LATEST_TAG=$(git tag -l "v*" --sort=-v:refname 2>/dev/null | head -1)
    if [ $TAG_COUNT -gt 0 ]; then
        echo "   ✅ $TAG_COUNT tag(s) trouvé(s) — dernier : $LATEST_TAG"
    else
        echo "   ⚠️  AVERTISSEMENT : Aucun tag sémantique"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "   ⚠️  AVERTISSEMENT : Pas un dépôt git"
    WARNINGS=$((WARNINGS + 1))
fi

# 8. Vérifier les tests
echo "8. Tests..."
if [ -d "tests" ]; then
    TEST_COUNT=$(find tests/ -name "test_*.py" 2>/dev/null | wc -l)
    echo "   ✅ Dossier tests/ existe ($TEST_COUNT fichiers de test)"
else
    echo "   ⚠️  AVERTISSEMENT : Pas de dossier tests/"
    WARNINGS=$((WARNINGS + 1))
fi

# Résumé
echo ""
echo "=== Résumé ==="
echo "Erreurs  : $ERRORS"
echo "Avertissements : $WARNINGS"
echo ""

if [ $ERRORS -gt 0 ]; then
    echo "❌ Le workspace nécessite des corrections urgentes."
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo "⚠️  Le workspace est fonctionnel mais peut être amélioré."
    exit 0
else
    echo "✅ Le workspace est en bon état !"
    exit 0
fi

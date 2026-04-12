#!/bin/bash
# cleanup-workspace.sh — Nettoie les fichiers temporaires du workspace schoolsWP
# Usage : bash scripts/cleanup-workspace.sh [--dry-run]
# --dry-run : affiche ce qui serait fait sans rien supprimer

set -e

DRY_RUN=false
if [ "$1" = "--dry-run" ]; then
    DRY_RUN=true
    echo "=== Mode dry-run : aucune modification ne sera faite ==="
    echo ""
fi

ARCHIVE_DIR="_archive/$(date +%Y-%m-%d)_cleanup"
MOVED=0

echo "=== Nettoyage du workspace — schoolsWP ==="
echo ""

# 1. Fichiers patch à la racine
echo "1. Recherche de fichiers temporaires à la racine..."
TEMP_FILES=$(find . -maxdepth 1 \( -name "patch_*" -o -name "temp_*" -o -name "backup_*" -o -name "tmp_*" \) 2>/dev/null)

if [ -n "$TEMP_FILES" ]; then
    echo "   Fichiers trouvés :"
    echo "$TEMP_FILES" | while read f; do echo "      → $f"; done

    if [ "$DRY_RUN" = false ]; then
        mkdir -p "$ARCHIVE_DIR"
        echo "$TEMP_FILES" | while read f; do
            mv "$f" "$ARCHIVE_DIR/"
            MOVED=$((MOVED + 1))
        done
        echo "   ✅ Déplacés dans $ARCHIVE_DIR/"
    else
        echo "   [dry-run] Seraient déplacés dans $ARCHIVE_DIR/"
    fi
else
    echo "   ✅ Aucun fichier temporaire trouvé"
fi

# 2. Chemins skills dupliqués
echo ""
echo "2. Recherche de chemins skills dupliqués..."
for DIR in ".agent/skills" ".agents/skills"; do
    if [ -d "$DIR" ]; then
        echo "   Trouvé : $DIR"
        if [ "$DRY_RUN" = false ]; then
            # Vérifier si contenu existe dans .claude/skills/
            if [ -d ".claude/skills" ]; then
                echo "   ⚠️  Vérifie manuellement que le contenu est migré vers .claude/skills/"
                echo "   Suppression de $DIR..."
                rm -rf "$DIR"
                echo "   ✅ Supprimé"
            else
                echo "   ⚠️  .claude/skills/ n'existe pas. Migration nécessaire avant suppression."
            fi
        else
            echo "   [dry-run] Serait supprimé après migration"
        fi
    fi
done

# 3. Fichiers __pycache__
echo ""
echo "3. Nettoyage des __pycache__..."
CACHE_COUNT=$(find . -type d -name "__pycache__" 2>/dev/null | wc -l)
if [ $CACHE_COUNT -gt 0 ]; then
    echo "   $CACHE_COUNT dossier(s) __pycache__ trouvé(s)"
    if [ "$DRY_RUN" = false ]; then
        find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        echo "   ✅ Supprimés"
    else
        echo "   [dry-run] Seraient supprimés"
    fi
else
    echo "   ✅ Aucun cache trouvé"
fi

# 4. Fichiers .pyc isolés
echo ""
echo "4. Nettoyage des .pyc isolés..."
PYC_COUNT=$(find . -name "*.pyc" -not -path "./__pycache__/*" 2>/dev/null | wc -l)
if [ $PYC_COUNT -gt 0 ]; then
    echo "   $PYC_COUNT fichier(s) .pyc trouvé(s)"
    if [ "$DRY_RUN" = false ]; then
        find . -name "*.pyc" -delete 2>/dev/null || true
        echo "   ✅ Supprimés"
    else
        echo "   [dry-run] Seraient supprimés"
    fi
else
    echo "   ✅ Aucun .pyc isolé"
fi

# Résumé
echo ""
echo "=== Nettoyage terminé ==="
if [ "$DRY_RUN" = true ]; then
    echo "Mode dry-run : aucune modification effectuée."
    echo "Relancez sans --dry-run pour appliquer les changements."
fi

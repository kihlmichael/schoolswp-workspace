# Debug Pipeline Agent

Diagnostic systématique d'un pipeline agent schoolsWP qui échoue.

## Cible
Pipeline ou agent : $ARGUMENTS

## Protocole (dans l'ordre)
1. **Reproduire** — Lancer la commande exacte, capturer l'erreur complète
2. **Localiser** — Identifier le fichier et la ligne de l'erreur (traceback)
3. **Contexte** — Lire le code autour de l'erreur + les dépendances importées
4. **Cause racine** — Identifier pourquoi (pas juste quoi)
5. **Fix** — Proposer la correction minimale
6. **Vérifier** — Relancer le pipeline, confirmer le fix
7. **Lesson** — Si le bug est systémique, ajouter dans core/tasks/lessons.md

## Règles
- Ne pas deviner : toujours lire le code avant de proposer un fix
- Vérifier safe_read_path / safe_write_path si le bug touche des chemins
- Vérifier le venv Windows (.venv/Scripts/python) si ImportError

# Plan d'action – Organisation Google Drive schoolsWP

## Phase 1 : Préparation (étapes 1-4)

### Étape 1 – Sauvegarde de sécurité
- Créer un dossier `_BACKUP_2026-02-07` à la racine du Drive
- Y copier (pas déplacer) l'intégralité du dossier source actuel
- Vérifier que la copie est complète (compter les fichiers)

### Étape 2 – Créer l'arborescence cible
- Exécuter le script `02_apps-script-structure.js`
- Vérifier que tous les dossiers sont créés (38 dossiers attendus)
- Ajouter les sous-dossiers de statut (01_DRAFT, 02_VALIDÉ, 03_LIVE, 99_ARCHIVES) dans chaque sous-catégorie de 02_TEMPLATES et 03_PROMPTS

### Étape 3 – Inventaire de l'existant
- Exécuter le script d'audit (`03_apps-script-audit.js`)
- Générer la liste complète des fichiers existants avec : nom, chemin, date de création, date de modif, type MIME
- Sauvegarder l'inventaire dans un Google Sheet temporaire

### Étape 4 – Analyser l'inventaire
- Détecter les doublons (même nom ou contenu similaire)
- Détecter les fichiers sans date dans le nom
- Détecter les fichiers avec mauvais séparateurs (underscore, tiret court au lieu de tiret long)
- Détecter les fichiers mal rangés (email one-shot dans monetisation, etc.)
- Classer chaque anomalie par sévérité : Critique / Moyen / Mineur

## Phase 2 : Dry-Run (étapes 5-7)

### Étape 5 – Mapping automatique
- Pour chaque fichier, proposer :
  - Nouveau nom (format : `AAAA-MM-JJ – Sujet – Type – Usage – Infos.ext`)
  - Nouveau chemin (dossier cible dans l'arborescence)
  - Niveau de confiance (80%+ = auto, <80% = "À valider")

### Étape 6 – Générer le tableau de mapping
- Exporter dans un Google Sheet : Ancien nom | Ancien chemin | Nouveau nom | Nouveau chemin | Confiance | Action
- Actions possibles : RENAME, MOVE, RENAME+MOVE, ARCHIVE, DOUBLON, À_VALIDER

### Étape 7 – Validation humaine
- Partager le tableau de mapping avec Michaël
- Attendre validation des lignes "À valider"
- Confirmer les doublons à archiver

## Phase 3 : Exécution (étapes 8-12)

### Étape 8 – Renommer les fichiers
- Appliquer les renommages validés (confiance 80%+ ou validés manuellement)
- Logger chaque opération (ancien nom → nouveau nom)

### Étape 9 – Déplacer les fichiers
- Déplacer vers les dossiers cibles
- Logger chaque déplacement (ancien chemin → nouveau chemin)

### Étape 10 – Archiver les doublons
- Déplacer les doublons confirmés vers 99_ARCHIVES
- Ne jamais supprimer définitivement

### Étape 11 – Créer les raccourcis
- Pour les fichiers accessibles depuis plusieurs endroits, créer des raccourcis Drive (pas de copies)
- Ex : un template email utilisé aussi en monétisation → fichier dans TEMPLATES, raccourci dans MONETISATION

### Étape 12 – Générer l'Index Global
- Créer le fichier d'index dans 01_ADMIN/01_Regles-et-Index
- Remplir avec tous les fichiers migrés
- Champs : Nom | Lien | Catégorie | Statut | Dernière MAJ | Notes

## Phase 4 : Finalisation (étapes 13-16)

### Étape 13 – Vérification post-migration
- Compter les fichiers source vs fichiers migrés
- Vérifier qu'aucun fichier n'a été perdu
- Vérifier la cohérence des noms (regex de validation)

### Étape 14 – Nettoyage
- Supprimer le dossier source vide (si tous les fichiers ont été déplacés)
- Conserver _BACKUP pendant 30 jours minimum

### Étape 15 – Rapport final
- Générer le rapport avec métriques
- Lister les exceptions et recommandations

### Étape 16 – Documentation de maintenance
- Documenter la procédure pour les nouveaux fichiers
- Créer une checklist rapide "Où ranger mon fichier ?"
- Optionnel : automatiser l'index via trigger Google Apps Script

## Checklist rapide post-migration

- [ ] Arborescence créée (38+ dossiers)
- [ ] Tous les fichiers renommés selon convention
- [ ] Tous les fichiers dans le bon dossier
- [ ] Doublons archivés
- [ ] Index global à jour
- [ ] Raccourcis créés si nécessaire
- [ ] Backup vérifié
- [ ] Rapport final produit

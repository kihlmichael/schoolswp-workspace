# Mode d'emploi – schoolsWP Drive Organizer v2.0

## Prérequis

- Un compte Google avec accès au Drive cible
- Accès à [Google Apps Script](https://script.google.com)
- 10-15 minutes pour l'exécution complète

---

## Étape 1 : Créer le projet Apps Script

1. Ouvrir **https://script.google.com**
2. Cliquer **Nouveau projet**
3. Renommer le projet : `schoolsWP Drive Organizer`

## Étape 2 : Ajouter les scripts

### Fichier 1 : Structure (Code.gs)
1. Dans l'éditeur, le fichier `Code.gs` existe déjà
2. **Supprimer tout le contenu** par défaut
3. **Coller le contenu** de `02_apps-script-structure.js`
4. `PARENT_FOLDER_ID` est déjà à `null` (racine du Drive) – modifier si besoin

### Fichier 2 : Audit & Migration (AuditMigration.gs)
1. Cliquer **+** à côté de "Fichiers" puis **Script**
2. Nommer le fichier : `AuditMigration`
3. **Coller le contenu** de `03_apps-script-audit.js`
4. La configuration est déjà faite :
   - `SOURCE_FOLDER_ID` = `1O_GbYXkAnnsix1Gowuv7EuvXL5qRdS_N` (ton dossier)
   - `TARGET_ROOT_ID` = `null` (recherche auto de PROMPTS_schoolsWP)

### Activer le service Drive API (pour les raccourcis)
1. Dans le menu gauche, cliquer **Services** (icône +)
2. Chercher **Drive API**
3. Cliquer **Ajouter**

---

## Étape 3 : Exécution (dans l'ordre STRICT !)

### 3a. Créer l'arborescence
1. Sélectionner la fonction **`createFullStructure`** dans le menu déroulant
2. Cliquer **Exécuter** (bouton lecture)
3. **Autoriser l'accès** au Drive quand demandé :
   - Cliquer "Examiner les autorisations"
   - Choisir ton compte Google
   - Cliquer "Autoriser"
4. Vérifier les logs : **Affichage puis Journaux d'exécution**
5. Vérifier dans le Drive que l'arborescence est créée

### 3b. Vérifier (optionnel)
1. Sélectionner **`verifyStructure`**
2. Exécuter pour lister tous les dossiers et fichiers

### 3c. Auditer les fichiers existants
1. Sélectionner **`runAudit`**
2. Exécuter
3. Lire les logs – le rapport détaille :
   - Fichiers sans date, mauvais séparateurs, sans type/usage
   - Extensions non standard
   - **Fichiers Email/CRM mal rangés** (avec la destination correcte)
   - Doublons vs variantes légitimes (V1/V2/FR/EN)

### 3d. Générer le mapping (DRY-RUN)
1. Sélectionner **`generateMapping`**
2. Exécuter
3. Un **Google Sheet** `schoolsWP – Mapping Migration` est créé automatiquement
4. Ouvrir le Sheet et vérifier chaque onglet :
   - **Mapping** : tableau complet (12 colonnes)
   - **Doublons** : groupes avec distinction vrais doublons vs variantes
   - **Email-CRM** : onglet dédié à la classification anti-fourre-tout
   - **Résumé** : métriques globales et sévérités

### 3e. Valider le mapping (OBLIGATOIRE avant migration)
1. Dans le Sheet, onglet **Mapping** :
   - Colonne K **"Validé ?"** : mettre **OUI** pour chaque ligne approuvée
   - Les lignes confiance >= 80% ont déjà "OUI" pré-rempli
   - Les lignes en **rouge** (confiance < 80%) = "À_VALIDER"
   - Les lignes en **orange** (sévérité CRITIQUE) = attention particulière
   - Tu peux **modifier** le "Nouveau nom proposé" ou "Nouveau chemin" directement dans le Sheet
2. Onglet **Email-CRM** : vérifier que la classification est correcte
   - Template réutilisable => 02_TEMPLATES/02_Email_CRM_FluentCRM
   - Prompt one-shot daté => 03_PROMPTS/02_Email_CRM
   - Séquence monétisation => 05_MONETISATION/04_Sequences_Email
3. Ne PAS mettre "OUI" sur les lignes dont tu n'es pas sûr

### 3f. Exécuter la migration
1. **IMPORTANT : Vérifier que le Sheet est validé !**
2. Sélectionner **`executeMigration`**
3. Exécuter
4. Un backup automatique est créé : `_BACKUP_YYYY-MM-DD` dans PROMPTS_schoolsWP
5. Seules les lignes avec OUI en colonne K sont traitées
6. Vérifier les logs pour le rapport de migration

### 3g. Générer l'index global
1. Sélectionner **`generateGlobalIndex`**
2. Exécuter
3. Deux formats sont générés :
   - **Google Sheet** `schoolsWP – Index Global` (filtrable, triable)
   - **Fichier .md** miroir dans `01_ADMIN/01_Regles-et-Index`

### 3h. Créer les raccourcis (optionnel)
1. Modifier la fonction `createAllShortcuts` avec tes IDs de fichiers
2. Syntaxe : `createShortcut_("ID_FICHIER", "ID_DOSSIER_CIBLE");`
3. Exécuter **`createAllShortcuts`**

---

## Étape 4 : Automatiser l'index (optionnel)

Pour régénérer l'index automatiquement chaque semaine :

1. Dans Apps Script : **Déclencheurs** (icône horloge à gauche)
2. Cliquer **Ajouter un déclencheur**
3. Configurer :
   - Fonction : `generateGlobalIndex`
   - Source : Programmé
   - Basé sur l'heure
   - Hebdomadaire
   - Jour : Lundi
   - Heure : 8h-9h
4. Sauvegarder

---

## Dépannage

### "Autorisation requise"
Normal à la première exécution. Accepter les permissions.

### "Dossier non trouvé"
Vérifier que l'ID du dossier est correct (copié depuis l'URL du Drive).
Pour ton dossier : `1O_GbYXkAnnsix1Gowuv7EuvXL5qRdS_N`

### "Dépassement du temps d'exécution" (6 min)
Si beaucoup de fichiers (500+), le script peut timeout.
Solution : dans `runAudit()`, ajouter un compteur et reprendre manuellement.

### "Drive API non trouvé"
Activer le service Drive API (Étape 2, dernière section).

### Le Sheet de mapping est vide
Exécuter `runAudit()` AVANT `generateMapping()`.

### "PropertiesService quota exceeded"
Si plus de 500 fichiers, les données dépassent le quota.
Le script v2 chunke automatiquement, mais si l'erreur persiste :
relancer `runAudit()` qui écrasera les anciennes données.

---

## Ordre d'exécution résumé

```
1. createFullStructure()     --> Crée les 38+ dossiers
2. verifyStructure()         --> Vérifie (optionnel)
3. runAudit()                --> Inventorie + détecte anomalies
4. generateMapping()         --> Sheet dry-run (4 onglets)
5. [VALIDATION HUMAINE]      --> Vérifier le Sheet !
6. executeMigration()        --> Renomme/déplace (safe, backup auto)
7. generateGlobalIndex()     --> Index Sheet + miroir .md
8. createAllShortcuts()      --> Raccourcis Drive (optionnel)
```

---

## Règles Email/CRM anti-fourre-tout (rappel)

| Type de fichier | Destination |
|----------------|-------------|
| Template Email réutilisable | `02_TEMPLATES/02_Email_CRM_FluentCRM` |
| Prompt Email one-shot daté | `03_PROMPTS/02_Email_CRM` |
| Séquence email monétisation (lancement/promo/evergreen) | `05_MONETISATION/04_Sequences_Email` |

L'onglet **Email-CRM** du Sheet de mapping affiche la classification de chaque fichier email détecté.

---

*schoolsWP Drive Organizer v2.0 – Michaël KIHL*

---
name: workspace-hygiene
description: "Audit, nettoyage et maintenance structurelle de workspaces de développement. Utilise ce skill dès que l'utilisateur mentionne : nettoyage de projet, doublons, fichiers résiduels, fichiers temporaires, audit de workspace, dette structurelle, organisation de repo, fichiers .patch, fichiers orphelins, réduction de bruit, ou demande de ranger/trier/nettoyer un dossier de travail. Déclenche aussi quand l'utilisateur dit 'c'est le bordel', 'faut ranger', 'trop de fichiers', 'je sais plus ce qui sert', 'audit', 'hygiène', ou toute variante exprimant un besoin de clarté structurelle dans un projet. Fonctionne en deux modes : AUDIT (analyse sans modification) et APPLY (exécution d'un plan validé). Ne supprime jamais définitivement — utilise toujours _trash/ et _archive/."
---

# Workspace Hygiene Manager

Skill de maintenance structurelle pour workspaces de développement solo-founder.

Objectif : réduire le bruit, détecter les doublons, classer les composants ambigus, préserver les sources de vérité et proposer un nettoyage sûr, réversible et traçable.

---

## Deux modes d'opération

Ce skill fonctionne exclusivement en deux modes séquentiels. Ne jamais mélanger les deux dans une même passe.

### Mode AUDIT

Analyse le workspace. Ne modifie rien. Produit un rapport structuré.

### Mode APPLY

Exécute un plan validé par l'utilisateur. Toute action est réversible.

Si l'utilisateur ne précise pas le mode, démarrer en mode AUDIT par défaut.

---

## Mode AUDIT — Instructions

### Étape 1 : Reconnaissance du workspace

Commencer par cartographier la structure :

```bash
# Vue d'ensemble (2 niveaux, sans node_modules ni .git)
find . -maxdepth 2 -not -path './.git/*' -not -path '*/node_modules/*' | head -200

# Taille des dossiers principaux
du -sh */ 2>/dev/null | sort -rh | head -20

# Fichiers récents (modifiés dans les 7 derniers jours)
find . -maxdepth 3 -type f -mtime -7 -not -path './.git/*' -not -path '*/node_modules/*' | head -50

# Fichiers anciens (non modifiés depuis 90+ jours)
find . -maxdepth 3 -type f -mtime +90 -not -path './.git/*' -not -path '*/node_modules/*' | head -50
```

### Étape 2 : Détection des signaux

Chercher ces catégories de signaux, dans cet ordre de priorité :

**Signaux forts (décision rapide possible) :**
- Fichiers nommés `patch_*.py`, `fix_*.py`, `tmp_*.py`, `debug_*.py`, `test_*.py` (hors dossier tests/)
- Fichiers `.patch`, `.rej`, `.orig`
- Dossiers `__pycache__/`, `.cache/`, `dist/`, `build/` non référencés dans un script de build
- Fichiers `*.bak`, `*.old`, `*_copy.*`, `* (1).*`, `* (2).*`
- Fichiers `*.log`, `*.tmp` à la racine

**Signaux moyens (investigation requise) :**
- Dossiers avec noms similaires (ex: `config/` et `configs/`, `utils/` et `helpers/`)
- Fichiers README ou CHANGELOG multiples à différents niveaux
- Dossiers `_archive/`, `old/`, `backup/`, `deprecated/` déjà existants
- Scripts jamais référencés dans aucun workflow, Makefile, CI ou documentation

**Signaux faibles (ne pas décider seul) :**
- Dossiers volumineux dont le rôle n'est pas évident
- Fichiers de configuration pour des outils non détectés dans le projet
- Composants dont la date de modification est ancienne mais qui pourraient être des références stables

### Étape 3 : Vérification des références

Avant de classer un élément, vérifier s'il est référencé quelque part :

```bash
# Chercher les références à un fichier ou dossier suspect
grep -r "nom_du_fichier" --include="*.md" --include="*.py" --include="*.sh" --include="*.yml" --include="*.yaml" --include="*.json" --include="*.toml" --include="Makefile" . 2>/dev/null

# Chercher les imports Python
grep -r "from.*nom_module\|import.*nom_module" --include="*.py" . 2>/dev/null

# Vérifier .gitignore
grep "nom_du_fichier\|nom_du_dossier" .gitignore 2>/dev/null
```

Ne jamais décider qu'un composant est inactif uniquement à partir de sa date de modification. Toujours croiser avec les références dans docs, scripts, workflows, imports et fichiers de configuration.

### Étape 4 : Classification

Chaque élément détecté reçoit un classement parmi quatre catégories :

| Classement | Signification | Action en mode APPLY |
|---|---|---|
| `keep` | Actif, référencé, utile | Aucune action |
| `archive` | Historique, potentiellement utile, non actif | Déplacer dans `_archive/` |
| `trash` | Résiduel, temporaire, non référencé | Déplacer dans `_trash/` |
| `review_required` | Ambiguïté forte, décision humaine nécessaire | Aucune action automatique |

Règles de classement :
- Un fichier `.patch` va en `archive` par défaut (sous-dossier `_archive/patches/`)
- Un fichier `tmp_*.py` non référencé va en `trash`
- Un dossier volumineux sans références claires va en `review_required`
- En cas de doublons exacts, garder la copie canonique (celle référencée ou à l'emplacement le plus logique), l'autre va en `trash`
- En cas de doublons partiels, classer en `review_required`

### Étape 5 : Rapport d'audit

Structurer le rapport exactement ainsi :

```markdown
# Audit Workspace — [nom du projet]
Date : [date ISO]

## 1. Résumé exécutif
- Nombre total d'éléments analysés
- Répartition : X keep / X archive / X trash / X review_required
- Estimation de l'espace récupérable
- Niveau de bruit structurel : faible / modéré / élevé

## 2. Éléments détectés

### trash (suppression sûre)
| Fichier/Dossier | Raison | Taille |
|---|---|---|
| `tmp_fix.py` | Fichier temporaire, aucune référence | 2.1 KB |

### archive (conservation historique)
| Fichier/Dossier | Raison | Destination |
|---|---|---|
| `migration_v1.patch` | Patch appliqué, valeur historique | `_archive/patches/` |

### review_required (décision humaine)
| Fichier/Dossier | Raison | Question pour l'utilisateur |
|---|---|---|
| `old_config/` | Dossier de 12 MB, rôle incertain | Ce dossier sert-il encore ? |

### keep (aucune action)
| Fichier/Dossier | Raison |
|---|---|
| `SKILL.md` | Source de vérité du skill principal |

## 3. Plan proposé
- Liste numérotée des actions à exécuter en mode APPLY
- Chaque action indique : source → destination
- Les actions `review_required` sont listées mais marquées [EN ATTENTE]

## 4. Points sensibles
- Éléments nécessitant une attention particulière
- Risques identifiés
- Questions ouvertes pour l'utilisateur
```

---

## Mode APPLY — Instructions

### Pré-requis

Ne jamais passer en mode APPLY sans un plan validé explicitement par l'utilisateur. Si l'utilisateur dit "applique" sans avoir validé un plan d'audit, rappeler qu'un audit est nécessaire d'abord.

### Étape 1 : Création de la structure de sécurité

```bash
# Créer les dossiers de destination s'ils n'existent pas
mkdir -p _trash
mkdir -p _archive/patches
mkdir -p _archive/old_configs
mkdir -p _archive/deprecated

# Horodater le nettoyage
echo "Nettoyage exécuté le $(date -Iseconds)" > _trash/.cleanup-log
echo "Archivage exécuté le $(date -Iseconds)" > _archive/.cleanup-log
```

### Étape 2 : Exécution des actions non ambiguës

Exécuter uniquement les éléments classés `trash` ou `archive` dans le plan validé. Ne jamais toucher aux éléments `review_required` sauf si l'utilisateur a donné une réponse explicite.

```bash
# Exemple : déplacer un fichier temporaire vers _trash
mv tmp_fix.py _trash/

# Exemple : archiver un patch
mv migration_v1.patch _archive/patches/

# Exemple : archiver un dossier entier
mv old_config/ _archive/old_configs/
```

### Étape 3 : Vérifications post-exécution

```bash
# Vérifier que rien n'est cassé (si un linter ou test existe)
# Adapter selon le projet
python -m py_compile main.py 2>&1 || echo "ERREUR DE COMPILATION"

# Lister le contenu de _trash et _archive pour confirmation
echo "=== CONTENU _trash ===" && ls -la _trash/
echo "=== CONTENU _archive ===" && find _archive/ -type f
```

### Étape 4 : Rapport d'exécution

Structurer le rapport exactement ainsi :

```markdown
# Rapport d'exécution — [nom du projet]
Date : [date ISO]

## 1. Actions exécutées
| # | Action | Source | Destination | Statut |
|---|---|---|---|---|
| 1 | trash | `tmp_fix.py` | `_trash/tmp_fix.py` | OK |
| 2 | archive | `migration_v1.patch` | `_archive/patches/migration_v1.patch` | OK |

## 2. État final
- Éléments déplacés vers _trash : X
- Éléments archivés : X
- Éléments review_required restants : X
- Espace libéré (hors _trash) : 0 (tout est récupérable)
- Tests/compilation : OK / KO

## 3. Journal synthétique
- Résumé des décisions prises
- Éléments review_required en attente de décision
- Prochaine action recommandée (ex : vider _trash après 7 jours si aucun problème)
```

---

## Règles impératives

Ces règles s'appliquent dans les deux modes, sans exception.

1. **Pas de suppression définitive.** Tout passe par `_trash/` ou `_archive/`. L'utilisateur décide quand vider.

2. **Pas de décision basée uniquement sur la date.** La date de modification seule ne suffit jamais à classer un élément. Toujours croiser avec les références (imports, docs, scripts, CI, workflows).

3. **Pas de symlink automatique.** Ne jamais créer de liens symboliques pour "simplifier". Les symlinks créent de la dette invisible.

4. **Pas de fusion automatique.** Si deux dossiers sont des copies exactes, garder le canonique et déplacer l'autre. Ne pas fusionner le contenu de deux dossiers différents.

5. **Pas de modification de .gitignore** sauf si le plan validé le prévoit explicitement et que l'utilisateur a confirmé.

6. **review_required = on ne touche pas.** En cas de doute, toujours classer en `review_required` et poser la question à l'utilisateur.

7. **Un seul source de vérité.** Si un doublon est détecté, identifier la version canonique (la plus référencée, la mieux placée) et archiver ou supprimer l'autre.

8. **Traçabilité totale.** Chaque action doit apparaître dans le rapport. Aucune modification silencieuse.

---

## Patterns de nommage à détecter

### Fichiers temporaires (-> trash par défaut si non référencés)

```
tmp_*.py, fix_*.py, debug_*.py, hack_*.py
*.bak, *.old, *.orig, *.rej
*_copy.*, * (1).*, * (2).*
*.tmp, *.log (à la racine)
.DS_Store, Thumbs.db, desktop.ini
```

### Fichiers historiques (-> archive par défaut)

```
*.patch
CHANGELOG.old, README.old
deprecated/*, old/*, backup/*
```

### Dossiers de build/cache (-> trash si non référencés dans un script de build)

```
__pycache__/, .cache/, .pytest_cache/
dist/, build/, *.egg-info/
node_modules/ (si pas de package.json)
.next/, .nuxt/ (si pas de framework correspondant)
```

---

## Exemples d'invocation

**Exemple 1 — Audit simple**

```
Utilisateur : "Fais un audit de ce workspace, y'a du bruit partout"
-> Déclencher le mode AUDIT
-> Scanner la structure, détecter les signaux, produire le rapport complet
```

**Exemple 2 — Audit ciblé**

```
Utilisateur : "Regarde le dossier scripts/, je suis sûr qu'il y a des fichiers morts"
-> Mode AUDIT limité au dossier scripts/
-> Vérifier les références de chaque script dans le reste du projet
-> Rapport ciblé
```

**Exemple 3 — Application d'un plan**

```
Utilisateur : "OK, le plan me va. Applique tout sauf le point 4."
-> Mode APPLY
-> Exécuter toutes les actions sauf le point 4
-> Rapport d'exécution
```

**Exemple 4 — Demande ambiguë**

```
Utilisateur : "Nettoie ce repo"
-> Répondre : "Je commence par un audit pour identifier ce qui peut être nettoyé.
   Je ne modifierai rien avant ta validation. C'est parti."
-> Lancer le mode AUDIT
```

**Exemple 5 — Doublons**

```
Utilisateur : "J'ai l'impression d'avoir deux fois le même dossier config"
-> Mode AUDIT ciblé sur les dossiers de configuration
-> Comparer les contenus (diff ou hash)
-> Identifier la version canonique
-> Proposer un plan
```

---

## Checklist d'exécution

### Avant l'audit

- [ ] Identifier le répertoire racine du workspace
- [ ] Vérifier s'il existe un `.gitignore`, un `Makefile`, un `CI config`, un `README`
- [ ] Vérifier s'il existe déjà un `_archive/` ou `_trash/` (nettoyages précédents)
- [ ] Demander à l'utilisateur s'il y a des dossiers ou fichiers à ne jamais toucher

### Pendant l'audit

- [ ] Scanner la structure complète (2-3 niveaux)
- [ ] Mesurer la taille des dossiers principaux
- [ ] Détecter les fichiers temporaires, patches, doublons
- [ ] Vérifier les références de chaque élément suspect
- [ ] Classer chaque élément : keep / archive / trash / review_required
- [ ] Ne jamais classer un élément sans avoir vérifié ses références

### Après l'audit

- [ ] Produire le rapport structuré complet (4 sections)
- [ ] Lister clairement les éléments `review_required` avec des questions précises
- [ ] Proposer un plan numéroté d'actions
- [ ] Attendre la validation explicite de l'utilisateur

### Pendant l'application

- [ ] Créer `_trash/` et `_archive/` avec horodatage
- [ ] Exécuter uniquement les actions validées
- [ ] Ne pas toucher aux éléments `review_required` non résolus
- [ ] Vérifier la compilation ou les tests après exécution
- [ ] Produire le rapport d'exécution complet (3 sections)

### Après l'application

- [ ] Confirmer que tout est récupérable
- [ ] Suggérer un délai avant de vider `_trash/` (7 jours recommandés)
- [ ] Proposer d'ajouter `_trash/` au `.gitignore` si pertinent (avec validation)

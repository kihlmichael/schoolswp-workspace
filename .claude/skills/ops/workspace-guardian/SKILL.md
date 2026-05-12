---
name: workspace-guardian
description: |
  Encode les règles de gouvernance du workspace schoolsWP : anti-duplication stricte (un seul chemin `.claude/skills/`), gouvernance Git (conventional commits, branches feature/fix/chore, tags semantiques), seuils de qualite (30 % couverture mini, tests par agent), anti-accumulation (pas de patch_*.py / temp_* / backup_* a la racine), capitalisation des lecons apres incident, checklist pre-deploiement. Sert de référence pour chaque decision structurelle. Principe directeur : "Construire moins, consolider plus, livrer mieux."
  Utilise ce skill quand l'utilisateur dit : "règles workspace", "gouvernance schoolsWP", "ou je dois mettre ce fichier", "convention de nommage", "guardian", "puis-je créer ce dossier", "checklist pre-deploiement", "format commit", "règle de structure", ou avant toute decision structurelle (creation de fichier/dossier, commit, merge, deploiement).
  NE PAS utiliser pour : exécuter concretement les actions de cleanup (utiliser `consolidation-ops`), trancher une question editoriale (utiliser `branding` ou `BRAND_RULES.md`), ecrire les règles d'un sub-projet (chaque sub-CLAUDE.md gere son scope), ou debugguer un incident en cours (utiliser le skill technique du domaine).
---

# Workspace Guardian — Skill de gouvernance schoolsWP

## Objectif

Ce skill encode les règles de gouvernance du workspace schoolsWP.
Il sert de référence pour chaque décision structurelle, chaque commit, chaque déploiement.

Principe directeur : **"Construire moins, consolider plus, livrer mieux."**

---

## Quand utiliser ce skill

- Avant de créer un nouveau fichier ou dossier
- Avant chaque commit ou merge
- Avant de déployer quoi que ce soit
- Après un incident ou un bug en production
- Pour auditer l'état du workspace

---

## 1. Anti-duplication stricte

### Règle : un seul chemin pour les skills

Le chemin officiel est `.claude/skills/`. Point final.

Si tu trouves un dossier `.agent/skills/` ou `.agents/skills/`, c'est un doublon. Il doit être supprimé après vérification que son contenu a été migré.

### Checklist avant création

1. Le fichier existe-t-il déjà ailleurs dans le projet ?
2. Une fonctionnalité similaire est-elle déjà couverte ?
3. Le nom suit-il la convention kebab-case ?

### Structure autorisée

```
.claude/
├── skills/
│   ├── workspace-guardian/
│   ├── consolidation-ops/
│   └── [autres-skills]/
└── settings.json
```

---

## 2. Gouvernance Git

### Branches

| Branche | Rôle | Règle |
|---------|------|-------|
| `main` | Stable, déployable | Jamais de commit direct. Merge uniquement via PR. |
| `feature/*` | Développement | Une branche par fonctionnalité. Nommage : `feature/nom-explicite` |
| `fix/*` | Corrections | Pour les bugfixes urgents. Nommage : `fix/description-courte` |
| `chore/*` | Maintenance | Nettoyage, refactoring, docs. Nommage : `chore/description` |

### Commits conventionnels

Format obligatoire :

```
type(scope): description courte

Corps optionnel pour le contexte.
```

Types autorisés : `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `style`.

Exemples :
- `feat(agents): ajouter agent de synchronisation WordPress`
- `fix(crm): corriger le mapping des champs FluentCRM`
- `chore(workspace): archiver les fichiers patch obsolètes`

### Tags sémantiques

Format : `vMAJEUR.MINEUR.PATCH`

- **MAJEUR** : changement breaking ou refonte complète
- **MINEUR** : nouvelle fonctionnalité rétro-compatible
- **PATCH** : correction de bug ou ajustement mineur

Règle : chaque merge sur `main` doit être taggé.

---

## 3. Seuils de qualité

### Tests

| Critère | Seuil minimum | Cible |
|---------|---------------|-------|
| Couverture code critique | 30% | 60% |
| Tests par agent | 1 minimum | 3+ |
| Tests d'intégration | 1 par workflow | 2+ |

"Code critique" = tout ce qui touche aux agents, aux API, aux données utilisateur.

### Pre-commit hooks

Obligatoires :
1. **Linting** : vérification syntaxe Python/JS
2. **Tests unitaires** : les tests existants doivent passer
3. **Format** : vérification du formatage (black, prettier)

Configuration dans `.pre-commit-config.yaml` à la racine.

### Revue de code

Avant chaque merge sur `main` :
- Au moins un test ajouté ou mis à jour
- Pas de `TODO` non documenté
- Pas de secrets ou credentials dans le code

---

## 4. Anti-accumulation

### Fichiers interdits à la racine

Ces patterns ne doivent **jamais** exister à la racine du projet :

- `patch_*.py` → déplacer dans `scripts/patches/` ou supprimer
- `test_*.py` isolés → déplacer dans `tests/`
- `temp_*`, `tmp_*` → supprimer
- `backup_*` → archiver ou supprimer

### Apps squelettes

Une app sans contenu réel (juste un `__init__.py` et un `models.py` vide) doit être :
1. Archivée dans `_archive/` avec la date
2. Documentée dans le CHANGELOG
3. Supprimée du code actif

### Structure data/

```
data/
├── raw/          # Données brutes, jamais modifiées
├── processed/    # Données transformées
├── exports/      # Fichiers de sortie
└── README.md     # Description du contenu
```

---

## 5. Capitalisation des leçons

### Quand écrire une leçon

Après chaque :
- Bug en production
- Incident technique
- Décision architecturale importante
- Erreur évitée de justesse

### Format obligatoire

Utilise le template `templates/lesson-entry.md` :

```markdown
## [Date] — Titre de la leçon

**Contexte :** Qu'est-ce qui s'est passé ?
**Impact :** Quel effet sur le projet ?
**Cause racine :** Pourquoi c'est arrivé ?
**Action corrective :** Qu'est-ce qu'on a fait ?
**Prévention :** Comment éviter que ça se reproduise ?
```

Fichier cible : `docs/lessons.md` à la racine du projet.

---

## 6. Déploiement

### Documentation obligatoire

Chaque déploiement doit avoir un playbook dans `docs/deploy-to-wordpress.md`.

Contenu minimum :
1. Prérequis (versions, accès, credentials)
2. Étapes pas à pas
3. Vérifications post-déploiement
4. Procédure de rollback

### Checklist pré-déploiement

- [ ] Tous les tests passent
- [ ] Le CHANGELOG est à jour
- [ ] Le tag de version est créé
- [ ] Le playbook est relu
- [ ] Le backup de la base est fait

---

## 7. Monitoring et visibilité des agents

### Chaque agent doit avoir

1. Un fichier `README.md` dans son dossier
2. Un log de ses actions (même minimal)
3. Un test de contrat d'interface
4. Une entrée dans `docs/agents-registry.md`

### Format du registre

```markdown
| Agent | Rôle | Statut | Dernière mise à jour |
|-------|------|--------|---------------------|
| sync-wp | Synchronisation WordPress | Actif | 2026-03-20 |
| crm-bridge | Pont FluentCRM | En dev | 2026-03-15 |
```

---

## 8. Résumé des règles

| Domaine | Règle clé |
|---------|-----------|
| Structure | Un seul chemin : `.claude/skills/` |
| Git | Conventional commits + tags sémantiques |
| Qualité | 30% couverture minimum, 1 test par agent |
| Propreté | Pas de fichiers orphelins à la racine |
| Leçons | `lessons.md` obligatoire après incident |
| Déploiement | Playbook documenté + checklist |
| Agents | Registre + README + test par agent |

---

## Fichiers de référence

- `references/governance-rules.md` : règles détaillées
- `references/quality-thresholds.md` : seuils de qualité
- `templates/lesson-entry.md` : template de leçon
- `templates/changelog-entry.md` : template d'entrée CHANGELOG

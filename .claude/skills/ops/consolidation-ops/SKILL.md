# Consolidation Ops — Playbooks d'exécution schoolsWP

## Objectif

Ce skill contient les playbooks concrets pour consolider le workspace schoolsWP.
4 playbooks, 18 actions, priorisés par urgence et impact.

Chaque action est vérifiable. Pas de théorie, que du concret.

---

## Vue d'ensemble

| Playbook | Horizon | Durée estimée | Actions |
|----------|---------|---------------|---------|
| 1. Quick Wins | Cette semaine | ~1h | 5 actions |
| 2. Qualité | Ce mois | ~3h | 4 actions |
| 3. Documentation | Ce mois | ~2h | 4 actions |
| 4. Architecture | Ce trimestre | ~5h | 5 actions |

---

## Playbook 1 — Quick Wins (cette semaine, ~1h)

### Action 1.1 : Merger les branches et taguer v0.1.0

**Pourquoi :** Stabiliser `main` comme source de vérité.

**Étapes :**
1. Vérifier l'état des branches : `git branch -a`
2. Identifier les branches à merger (feature terminées)
3. Merger chaque branche : `git merge feature/nom --no-ff`
4. Résoudre les conflits si nécessaire
5. Taguer : `git tag -a v0.1.0 -m "chore: consolidation initiale du workspace"`
6. Pousser : `git push origin main --tags`

**Vérification :** `git log --oneline --graph -10` montre un historique propre.

### Action 1.2 : Supprimer .agent/skills/ (doublon)

**Pourquoi :** Un seul chemin autorisé : `.claude/skills/`.

**Étapes :**
1. Vérifier le contenu de `.agent/skills/` (s'il existe)
2. Comparer avec `.claude/skills/` — migrer ce qui manque
3. Supprimer : `rm -rf .agent/skills/`
4. Supprimer aussi `.agents/skills/` si présent
5. Commiter : `chore(structure): supprimer chemins skills dupliqués`

**Vérification :** `find . -path "*.agent*skills*" -type d` ne retourne rien.

### Action 1.3 : Archiver les fichiers patch et temporaires

**Pourquoi :** La racine doit rester propre.

**Étapes :**
1. Lister : `find . -maxdepth 1 -name "patch_*" -o -name "temp_*" -o -name "backup_*"`
2. Créer `_archive/2026-03-24_cleanup/`
3. Déplacer les fichiers identifiés
4. Commiter : `chore(cleanup): archiver fichiers temporaires racine`

**Vérification :** `ls *.py` à la racine ne montre que les fichiers légitimes.

### Action 1.4 : Archiver les apps squelettes

**Pourquoi :** Une app vide encombre et crée de la confusion.

**Étapes :**
1. Identifier les apps avec seulement `__init__.py` et `models.py` vide
2. Déplacer dans `_archive/2026-03-24_apps-squelettes/`
3. Documenter dans le CHANGELOG
4. Commiter : `chore(apps): archiver applications squelettes`

**Vérification :** Chaque app restante a du code fonctionnel.

### Action 1.5 : Initialiser docs/lessons.md

**Pourquoi :** Capitaliser les leçons dès maintenant.

**Étapes :**
1. Créer `docs/lessons.md` avec le header
2. Ajouter la première leçon : "Pourquoi on consolide"
3. Commiter : `docs: initialiser le journal des leçons`

**Template :**
```markdown
# Journal des leçons — schoolsWP

> Chaque erreur est une leçon. Chaque leçon rend le projet plus solide.

---

## 2026-03-24 — Consolidation initiale du workspace

**Contexte :** Le workspace a grandi organiquement avec des doublons,
des fichiers temporaires à la racine et des apps vides.

**Impact :** Confusion sur la structure, risque d'erreurs.

**Cause racine :** Pas de règles de gouvernance dès le départ.

**Action corrective :** Mise en place des skills workspace-guardian
et consolidation-ops.

**Prévention :** Suivre les règles de governance-rules.md.

**Tags :** `structure`, `gouvernance`
```

**Vérification :** Le fichier existe et contient au moins une entrée.

---

## Playbook 2 — Qualité (ce mois, ~3h)

### Action 2.1 : Créer les tests contrat d'interface

**Pourquoi :** Chaque agent doit avoir un test minimum.

**Étapes :**
1. Lister tous les agents dans `agents/`
2. Pour chaque agent, créer `tests/test_[agent].py`
3. Écrire un test de contrat : l'agent démarre, accepte un input, retourne un output valide
4. Commiter : `test(agents): ajouter tests contrat interface`

**Template de test :**
```python
"""Test contrat d'interface pour l'agent [nom]."""

def test_agent_initialisation():
    """L'agent doit s'initialiser sans erreur."""
    from agents.[nom] import Agent
    agent = Agent()
    assert agent is not None

def test_agent_contrat():
    """L'agent doit accepter un input et retourner un output valide."""
    from agents.[nom] import Agent
    agent = Agent()
    result = agent.run(input_data={"test": True})
    assert result is not None
    assert "status" in result
```

**Vérification :** `pytest tests/ -v` passe sans erreur.

### Action 2.2 : Configurer le coverage report

**Pourquoi :** Mesurer pour améliorer.

**Étapes :**
1. Installer : `pip install pytest-cov`
2. Ajouter dans `pyproject.toml` ou `setup.cfg` :
   ```ini
   [tool:pytest]
   addopts = --cov=agents --cov-report=html --cov-report=term
   ```
3. Lancer : `pytest --cov`
4. Vérifier que la couverture du code critique est >= 30%

**Vérification :** Le rapport HTML est généré dans `htmlcov/`.

### Action 2.3 : Créer le CHANGELOG

**Pourquoi :** Tracer l'historique des changements.

**Étapes :**
1. Créer `docs/CHANGELOG.md`
2. Documenter les versions existantes (même rétroactivement)
3. Utiliser le format Keep a Changelog
4. Commiter : `docs: initialiser le CHANGELOG`

**Vérification :** Le fichier existe avec au moins une entrée de version.

### Action 2.4 : Configurer GitHub Actions CI

**Pourquoi :** Automatiser la vérification de qualité.

**Étapes :**
1. Créer `.github/workflows/ci.yml`
2. Utiliser le template dans `templates/ci-workflow.yml`
3. Configurer : lint + tests sur chaque push et PR
4. Commiter : `ci: ajouter workflow GitHub Actions`

**Vérification :** Le workflow se déclenche sur le prochain push.

---

## Playbook 3 — Documentation (ce mois, ~2h)

### Action 3.1 : Créer deploy-to-wordpress.md

**Pourquoi :** Le déploiement doit être reproductible.

**Étapes :**
1. Créer `docs/deploy-to-wordpress.md`
2. Utiliser le template dans `templates/deploy-playbook.md`
3. Documenter chaque étape du processus actuel
4. Ajouter la checklist pré-déploiement
5. Commiter : `docs: ajouter playbook de déploiement WordPress`

**Vérification :** Un nouveau contributeur peut déployer en suivant le doc.

### Action 3.2 : Structurer le dossier data/

**Pourquoi :** Les données doivent être organisées et documentées.

**Étapes :**
1. Créer `data/raw/`, `data/processed/`, `data/exports/`
2. Déplacer les fichiers existants dans le bon sous-dossier
3. Créer `data/README.md` décrivant la structure
4. Commiter : `chore(data): structurer le dossier data`

**Vérification :** Chaque fichier dans `data/` est dans le bon sous-dossier.

### Action 3.3 : Auditer et nettoyer .claude/

**Pourquoi :** Le dossier de configuration doit être minimal et propre.

**Étapes :**
1. Lister tout dans `.claude/`
2. Vérifier que chaque fichier a une raison d'être
3. Supprimer les fichiers obsolètes
4. Documenter la structure dans un README
5. Commiter : `chore(.claude): audit et nettoyage configuration`

**Vérification :** Pas de fichier sans utilité dans `.claude/`.

### Action 3.4 : Créer le registre des agents

**Pourquoi :** Savoir quels agents existent et leur état.

**Étapes :**
1. Créer `docs/agents-registry.md`
2. Lister chaque agent avec : nom, rôle, statut, date de dernière mise à jour
3. Commiter : `docs: créer le registre des agents`

**Vérification :** Chaque agent du dossier `agents/` a une entrée dans le registre.

---

## Playbook 4 — Architecture (ce trimestre, ~5h)

### Action 4.1 : Refactoring des agents

**Pourquoi :** Les agents doivent suivre une interface commune.

**Étapes :**
1. Définir l'interface commune (BaseAgent)
2. Refactoriser chaque agent pour hériter de BaseAgent
3. Mettre à jour les tests
4. Commiter : `refactor(agents): interface commune BaseAgent`

### Action 4.2 : Créer un Dockerfile

**Pourquoi :** Environnement reproductible pour le développement et le déploiement.

**Étapes :**
1. Créer `Dockerfile` à la racine
2. Configurer Python + dépendances
3. Ajouter `docker-compose.yml` si nécessaire
4. Tester le build : `docker build -t schoolswp .`
5. Commiter : `ci(docker): ajouter Dockerfile`

### Action 4.3 : Monitoring des agents

**Pourquoi :** Savoir si les agents fonctionnent correctement en production.

**Étapes :**
1. Ajouter un système de logging structuré (JSON)
2. Créer un dashboard de santé (même simple en CLI)
3. Alertes sur les erreurs critiques
4. Commiter : `feat(monitoring): logging structuré et dashboard santé`

### Action 4.4 : Tags sémantiques automatisés

**Pourquoi :** Automatiser le versioning pour éviter les oublis.

**Étapes :**
1. Configurer un outil comme `python-semantic-release` ou `standard-version`
2. Lier au workflow CI
3. Tester sur une branche de test
4. Commiter : `ci(release): automatiser les tags sémantiques`

### Action 4.5 : Gouvernance complète

**Pourquoi :** Formaliser les règles pour l'équipe et les contributeurs.

**Étapes :**
1. Créer `CONTRIBUTING.md` à la racine
2. Documenter : setup local, conventions, processus de PR
3. Créer `CODEOWNERS` si pertinent
4. Commiter : `docs: ajouter guide de contribution`

---

## Suivi des actions

Utilise `references/action-tracker.md` pour suivre l'avancement.

Format :
```
| # | Action | Statut | Date |
|---|--------|--------|------|
| 1.1 | Merger + tag v0.1.0 | [ ] | — |
| 1.2 | Supprimer .agent/skills/ | [ ] | — |
```

Mettre à jour après chaque action terminée.

---

## Scripts utilitaires

- `scripts/verify-consolidation.sh` : vérifie l'état du workspace
- `scripts/cleanup-workspace.sh` : nettoie les fichiers temporaires

---

## Règle d'or

> Chaque action doit laisser le workspace dans un meilleur état qu'avant.
> Si tu n'es pas sûr, consulte le skill workspace-guardian.

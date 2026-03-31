# Diagnostic strategique — Workspace schoolsWP

**Date** : 2026-03-24
**Type** : Audit CTO fractional + auditeur technique + consultant productivite
**Sujet** : Organisation, execution, architecture du workspace schoolsWP

---

## Verdict global

Systeme de production editoriale pilote par IA dans le top 1% pour un solo-dev. 28 agents Python, 374 skills, 56 system prompts, 14 workflows n8n, 7 apps. Architecture solide, documentation exemplaire, securite au-dessus de la moyenne.

**Mais** : systeme devenu trop dense pour rester fluide. Pas de filet de securite automatise (ni CI, ni tests suffisants, ni release formalisee). Complexite qui coute plus en charge mentale qu'elle ne rapporte en productivite.

> "Tu as un moteur de F1 dans un garage sans alarme, sans controle technique, et avec des pieces de rechange empilees partout."

---

## Ce qui est solide

- **Architecture agent** : 28 agents Python, BaseContentAgent, async, CLI-ready, retour Markdown
- **Documentation** : CLAUDE.md a 3 niveaux, brand rules (26 regles), style guide, methode (6 frameworks)
- **Securite** : pentest, STRIDE, RGPD, path traversal, pre-commit hooks, Dependabot
- **Outillage Claude Code** : 286+ skills, hooks, rules scopees, MCP integre
- **Separation des concerns** : arborescence de premier niveau lisible

---

## Ce qui ralentit ou fragilise

1. **Bruit structurel eleve** — 374 skills, 7 apps (3 squelettes), 8 patch files, data/ non organise, doublons
2. **Zero filet de securite automatise** — Pas de CI/CD, 5 tests pour 19 500 lignes, pas de coverage
3. **Git fragile** — Branche unique, pas de main, pas de tags, pas de CHANGELOG
4. **Deploiement implicite** — Chemin article → publication WP dans la tete, pas dans le systeme
5. **Agents trop similaires** — 28 agents avec patterns repetes, __init__.py de 718 lignes
6. **Apps zombies** — 3 squelettes, apps/ pese 5.6 GB (88% du projet)
7. **Lessons non capitalisees** — lessons.md vide apres 39 commits et 2 pentests
8. **Repo disproportionne** — ~15 GB dont 5.6 GB node_modules

---

## 8 faiblesses majeures (par priorite)

### 1. Absence totale de CI/CD [CRITIQUE]

| | |
|---|---|
| **Constat** | Aucun pipeline GitHub Actions. Pre-commit hooks = seule barriere |
| **Impact** | Chaque commit est un acte de foi. Regressions invisibles |
| **Action** | Workflow minimal : ruff check + pytest + pip-audit sur chaque push (15 min) |

### 2. Couverture de tests quasi inexistante [CRITIQUE]

| | |
|---|---|
| **Constat** | 5 fichiers de tests pour 19 500 lignes. < 1% de couverture |
| **Impact** | Impossible de savoir si un refactoring casse quelque chose |
| **Action** | 1 test par agent (contrat d'interface). Commencer par les 3 pipelines principaux |

### 3. Git sans baseline stable [HAUTE]

| | |
|---|---|
| **Constat** | 39 commits sur chore/workspace-setup. Pas de main, tags, CHANGELOG |
| **Impact** | Aucun point de retour fiable. Rollback impossible proprement |
| **Action** | Merger dans main. Proteger. Tag v0.1.0. Convention feature/ |

### 4. Duplication skills .agent/ vs .agents/ [HAUTE]

| | |
|---|---|
| **Constat** | 93 skills identiques dans 2 dossiers. 186 fichiers en double |
| **Impact** | Bruit cognitif, risque de divergence, desorientation |
| **Action** | Choisir un emplacement canonique. Supprimer l'autre. Documenter |

### 5. Deploiement non documente [HAUTE]

| | |
|---|---|
| **Constat** | Chemin article → publication WP non formalise |
| **Impact** | Perte de temps a la reprise. Impossible a deleguer |
| **Action** | Playbook deploy-to-wordpress.md dans core/playbooks/ |

### 6. Agents trop homogenes sans factorisation [MOYENNE]

| | |
|---|---|
| **Constat** | 28 agents, patterns repetes, __init__.py 718 lignes |
| **Impact** | Bug fix replique sur 28 fichiers. Cout lineaire |
| **Action** | Extraire patterns communs : decorateur CLI, wrapper API, registre dynamique |

### 7. Apps zombies et poids mort [MOYENNE]

| | |
|---|---|
| **Constat** | 3 squelettes inactifs, 8 patch files, apps/ = 5.6 GB |
| **Impact** | Bruit visuel/cognitif, repo lourd, fausse impression de complexite |
| **Action** | Archiver squelettes, supprimer patch files, verifier .gitignore |

### 8. data/ non structure [FAIBLE]

| | |
|---|---|
| **Constat** | CSV, JSON debug, rapports melanges (27 MB) |
| **Action** | Sous-dossiers : data/reports/, data/exports/, data/debug/, data/youtube/ |

---

## Ce qui doit etre simplifie, fusionne, archive ou supprime

| Action | Element | Raison |
|--------|---------|--------|
| SUPPRIMER | .agent/skills/ (93 skills) | Doublon exact. Zero valeur, 100% bruit |
| SUPPRIMER | 8 patch_*.py / fix_*.py | Dette residuelle a la racine |
| ARCHIVER | apps/elearning/ | Squelette inactif |
| ARCHIVER | apps/video-marketing/ | Squelette inactif |
| ARCHIVER | apps/claude-telegram-poc/ | POC a cote de telegram-bot/ |
| FUSIONNER | CLAUDE DESKTOP/ dans schoolsWP | gws-cli et notebooklm-cli sont des outils du projet |
| SIMPLIFIER | core/agents-py/__init__.py | 718 lignes → registre dynamique |
| SIMPLIFIER | .claude/ (546 MB) | Auditer et supprimer les variants obsoletes |
| STRUCTURER | data/ (27 MB) | Sous-dossiers thematiques + purge debug |

---

## Ce qui manque pour passer de puissant a robuste

1. **Filet de securite automatise** — CI/CD + tests + coverage report
2. **Strategie de release** — Tags git, CHANGELOG auto, releases GitHub
3. **Monitoring des agents** — Prometheus + Grafana (references mais pas deployes)
4. **Conteneurisation** — Dockerfile pour les agents Python
5. **Capitalisation des erreurs** — lessons.md rempli
6. **Gouvernance structurelle** — Regles anti-duplication, seuils skills, nettoyage periodique

---

## Top 5 actions a plus fort ROI

| # | Action | Duree | Impact |
|---|--------|-------|--------|
| 1 | Creer main + tag v0.1.0 | 10 min | Baseline stable |
| 2 | GitHub Actions minimal (ruff + pytest + pip-audit) | 15 min | Qualite automatisee |
| 3 | Supprimer .agent/skills/ + patch files | 5 min | -186 fichiers parasites |
| 4 | Tests contrat d'interface sur 3 pipelines | 2h | ~30% couverture code critique |
| 5 | Remplir lessons.md + playbook deploy-to-wordpress | 30 min | Memoire operationnelle externalisee |

---

## Plan d'action en 3 horizons

### Cette semaine (~1h total)

1. Merger dans main, proteger, tag v0.1.0 (10 min)
2. Supprimer .agent/skills/ via git rm (5 min)
3. Supprimer/archiver les 8 patch files (5 min)
4. Archiver les 3 apps squelettes dans _archive/ (10 min)
5. Remplir lessons.md — 10 premieres lecons (20 min)
6. Creer workflow GitHub Actions minimal (15 min)

### Ce mois-ci

7. Tests contrat d'interface : content_factory, article_pipeline, publish_ready (2h)
8. Playbook deploy-to-wordpress.md (30 min)
9. Structurer data/ en sous-dossiers + purge (30 min)
10. Auditer .claude/ (546 MB) et supprimer variants obsoletes (1h)
11. Coverage report dans le CI (pytest-cov) (15 min)
12. CHANGELOG.md + convention de commits (30 min)

### Ce trimestre

13. Refactoring agents : extraire patterns communs (4h)
14. Dockerfile pour les agents Python (2h)
15. Monitoring : connecter logs a Grafana/Prometheus (3h)
16. Strategie de release : tags semantiques + CHANGELOG auto (1h)
17. Consolider CLAUDE DESKTOP/ : integrer gws-cli et notebooklm-cli dans tools/ (1h)
18. Regles de gouvernance structurelle (1h)

---

## Conclusion strategique

> **Arreter de construire. Commencer a consolider. Simplifier ce qui peut l'etre. Supprimer ce qui ne sert plus. Automatiser la qualite, pas seulement la production.**

Le plan de cette semaine = ~1h de travail pour un ROI considerable : baseline Git stable, CI fonctionnel, 186 fichiers parasites en moins, capitalisation formelle des lecons.

> "Construire moins, consolider plus, livrer mieux."

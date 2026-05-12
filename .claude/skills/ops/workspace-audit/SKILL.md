---
name: workspace-audit
description: |
  Audit complet et reproductible du workspace `D:\VS Code` + projet schoolsWP en 7 phases. Produit un rapport Markdown avec métriques, scores de maturité, bloc metadata JSON, et comparaison automatisée avec l'audit précédent.
  Utilise ce skill quand l'utilisateur dit : "audit workspace", "bilan schoolsWP", "état des lieux", "diagnostic", "health check", "où en est le projet", "montre-moi les métriques", ou "qu'est-ce qui a changé".
  NE PAS utiliser pour : nettoyer concrètement les doublons et fichiers résiduels (utiliser `workspace-hygiene`), auditer le code Python (utiliser `audit-codebase` ou `code-review-and-quality`), ou auditer la sécurité (utiliser `cso` ou `security-auditor`).
---

# Workspace Audit — schoolsWP

Audit complet, reproductible et comparable du workspace `D:\VS Code` et du projet schoolsWP.
Chaque audit produit un rapport Markdown avec un bloc metadata JSON en fin de fichier,
permettant des comparaisons automatisees entre audits successifs.

## Quand utiliser ce skill

- Bilan periodique (hebdomadaire, mensuel, trimestriel)
- Avant/apres un chantier majeur (migration, refactor, ajout d'agents)
- Pour identifier les progres et les regressions
- Pour prioriser les prochaines actions

## Processus d'audit

L'audit se deroule en 7 phases sequentielles. Chaque phase collecte des donnees factuelles
avant toute interpretation. Ne jamais inventer de chiffres — si une mesure echoue, le noter
explicitement dans le rapport.

### Phase 1 — Cartographie du workspace

Explorer `D:\VS Code/` au premier niveau et identifier :
- Les dossiers principaux (CLAUDE CODE, CLAUDE DESKTOP, GEMINI, GEMINI PRO, etc.)
- Leur role probable et leur niveau d'activite (actif, ponctuel, inactif, archive)
- Les fichiers structurants a la racine (scripts, docs, config)

Commandes cles :
```bash
ls -la "d:/VS Code/"
ls -la "d:/VS Code/CLAUDE CODE/"
```

### Phase 2 — Metriques schoolsWP

Collecter les metriques suivantes depuis `d:/VS Code/CLAUDE CODE/projects/schoolswp/` :

**Code et agents**
```bash
# Nombre d'agents Python
find core/agents-py -maxdepth 1 -type d | grep -v __pycache__ | grep -v "^core/agents-py$" | wc -l

# Lignes de code agents
find core/agents-py -name "*.py" -type f | xargs wc -l 2>/dev/null | tail -1

# CLIs disponibles
find core/agents-py -name "cli.py" -type f | wc -l

# System prompts
find core/agents-md -name "*.md" -type f | wc -l
```

**Skills**
```bash
# Skills projet
find .claude/skills -maxdepth 1 -type d | wc -l

# Skills workspace
find "d:/VS Code/CLAUDE CODE/.claude/skills" -maxdepth 1 -type d | wc -l

# Skills legacy (.agents)
find .agents/skills -maxdepth 1 -type d 2>/dev/null | wc -l
```

**Contenu**
```bash
find content/articles -name "*.md" -type f 2>/dev/null | wc -l
find content/pages -name "*.md" -type f 2>/dev/null | wc -l
find systems/workflows -name "*.json" -type f 2>/dev/null | wc -l
```

**Tests**
```bash
find tests -name "*.py" -type f | wc -l
```

**Git**
```bash
git log --oneline --all | wc -l
git branch -a
git log --oneline -5
```

**Tailles** (peut timeout sur gros dossiers — noter "N/A" si echec)
```bash
du -sh core/ content/ systems/ tools/ infra/ data/ apps/ tests/ .claude/ 2>/dev/null
```

### Phase 3 — Inventaire detaille

Lister :
- Les 28+ agents Python (module + fonction)
- Les sous-applications dans apps/ (nom + stack + maturite)
- Les workflows n8n exportes
- Les formations dans content/formations/
- Les documents strategiques dans .claude/docs/
- Les slash commands dans .claude/commands/
- Les serveurs MCP actifs

### Phase 4 — Audit securite

Verifier la presence et l'etat de :
- Protection path traversal dans base.py (`safe_read_path`, `safe_write_path`)
- `.gitignore` fortress (secrets, .env, .mcp.json, tokens, patch files)
- Pre-commit hooks (secrets-scan, ruff, pip-audit)
- Dependabot (pip + npm)
- Rapports pentest dans systems/security/
- Documents GDPR/compliance

### Phase 5 — Evaluation de maturite

Evaluer chaque dimension sur 10 en se basant sur des criteres objectifs :

| Dimension | Criteres |
|---|---|
| **Structure** | Separation des concerns, conventions documentees, arborescence coherente |
| **Outillage IA** | Nombre d'agents, skills, MCP, pipelines, couverture fonctionnelle |
| **Documentation** | CLAUDE.md, brand rules, READMEs, lessons.md rempli ou non |
| **Securite** | Pentest, STRIDE, GDPR, path traversal, gitignore, pre-commit |
| **Maintenabilite** | Code propre (ruff), DRY, patterns agents, refactoring |
| **Testabilite** | Nombre de tests vs nombre d'agents, couverture estimee |
| **CI/CD** | GitHub Actions, deploy automatise, validation sur push |
| **Deploiement** | Docker, workflow de mise en production, reproductibilite |
| **Scalabilite** | Architecture extensible, orchestration, monitoring |

**Score global** = moyenne arithmetique des 9 scores.

Bareme indicatif :
- 9-10 : Exemplaire, rien a changer
- 7-8 : Solide, ameliorations mineures
- 5-6 : Fonctionnel, ameliorations significatives a planifier
- 3-4 : Lacunaire, action requise
- 1-2 : Absent ou critique

### Phase 6 — Risques et recommandations

Identifier les risques par severite (Haute, Moyenne, Faible) en se basant sur les
observations factuelles des phases precedentes.

Formuler des recommandations en 3 horizons :
- **Court terme** (cette semaine) — quick wins, hygiene
- **Moyen terme** (ce mois) — ameliorations structurantes
- **Long terme** (ce trimestre) — investissements strategiques

### Phase 7 — Comparaison avec l'audit precedent

Chercher le dernier audit dans `data/audits/` :
```bash
ls -t data/audits/*_workspace-audit.md 2>/dev/null | head -1
```

Si un audit precedent existe, extraire son bloc `metadata` JSON et comparer :
- Delta sur chaque metrique (agents, skills, tests, commits, tailles)
- Delta sur chaque score de maturite
- Risques resolus vs nouveaux risques
- Recommandations completees vs restantes

Presenter la comparaison sous forme de tableau avec fleches (hausse/baisse/stable).

## Format du rapport

Le rapport DOIT suivre cette structure exacte pour garantir la comparabilite :

```markdown
# Audit Workspace — YYYY-MM-DD

**Date** : YYYY-MM-DD
**Branche** : [branche active]
**Commits** : [nombre total]
**Auditeur** : [modele Claude utilise]

---

## Resume executif
[3-5 phrases]

## 1. Cartographie D:\VS Code
[Tableau des dossiers]

## 2. schoolsWP — Metriques cles
[Tableau des metriques]

### Tailles des repertoires
[Tableau des tailles]

## 3. Les N agents Python
[Tableau module + fonction]

## 4. Sous-applications (apps/)
[Tableau app + stack + maturite]

## 5. Automatisations n8n
[Liste workflows + instance]

## 6. Securite
[Tableau element + statut]

## 7. Configuration VS Code
[Synthese settings + extensions]

## 8. Evaluation de maturite
[Tableau 9 dimensions + score + commentaire]
**Score global** : X.X / 10

## 9. Risques identifies
[Tableau risque + severite]

## 10. Recommandations
### Court terme
### Moyen terme
### Long terme

## 11. Comparaison avec audit precedent
[Si disponible : tableau de deltas]
[Si premier audit : "Premier audit — pas de comparaison disponible."]

## Metadata audit
```json
{
  "date": "YYYY-MM-DD",
  "version": "1.0",
  "branch": "...",
  "commits_count": N,
  "agents_count": N,
  "agents_lines": N,
  "system_prompts_count": N,
  "skills_count_project": N,
  "skills_count_workspace": N,
  "skills_count_total_unique": N,
  "tests_count": N,
  "articles_count": N,
  "pages_count": N,
  "workflows_count": N,
  "apps_count": N,
  "mcp_servers_count": N,
  "maturity_structure": N,
  "maturity_ai_tooling": N,
  "maturity_documentation": N,
  "maturity_security": N,
  "maturity_maintainability": N,
  "maturity_testability": N,
  "maturity_ci_cd": N,
  "maturity_deployment": N,
  "maturity_scalability": N,
  "maturity_score": N.N,
  "top_risks": ["...", "...", "..."],
  "size_core_mb": N,
  "size_content_mb": N,
  "size_systems_mb": N,
  "size_tools_mb": N,
  "size_apps_mb": N,
  "size_data_mb": N,
  "size_claude_mb": N,
  "size_tests_mb": N
}
```
```

## Sauvegarde

Sauvegarder le rapport dans :
```
data/audits/YYYY-MM-DD_workspace-audit.md
```

Convention de nommage : `YYYY-MM-DD_workspace-audit.md` (date ISO du jour de l'audit).

## Parallelisation

Pour accelerer l'audit, lancer en parallele via des agents :
1. **Agent Workspace** — Phase 1 (cartographie D:\VS Code)
2. **Agent schoolsWP** — Phases 2-3 (metriques + inventaire detaille)
3. **Agent Config** — Phases 4 + config VS Code (securite + settings)

Puis consolider les resultats pour les phases 5-7 (maturite, risques, comparaison).

## Regles

- Ne jamais inventer de chiffres — si une commande echoue, noter "N/A (timeout)" ou "N/A (non trouve)"
- Distinguer faits observes / interpretations / recommandations
- Utiliser le tutoiement (convention schoolsWP)
- Ne pas ajouter d'emojis sauf demande explicite
- Le bloc metadata JSON doit etre parseable — pas de commentaires dans le JSON
- Garder le meme schema JSON entre audits pour permettre les comparaisons automatisees

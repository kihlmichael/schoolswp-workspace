# schoolsWP Lessons Learned

Erreurs commises, causes racines identifiées et règles établies pour ne pas les répéter.

---

## Lesson #1 — Path traversal non protégé sur tous les CLIs

**Date** : 2026-03-15
**Contexte** : Pentest session 1

**Erreur** : Les 28 agents CLI acceptaient des chemins fichiers arbitraires (`--file`, `--output`) sans validation. Un utilisateur pouvait lire/écrire hors du répertoire de travail (ex: `--file ../../etc/passwd`).

**Cause racine** : Aucune validation de chemin dans le contrat `BaseContentAgent`. Chaque CLI faisait confiance à l'input utilisateur.

**Fix** : `safe_read_path()` et `safe_write_path()` ajoutés dans `base.py` — vérifient que le chemin résolu est sous `Path.cwd()`. Déployé sur les 28 CLIs en 2 commits (744cc9d, d562abf).

**Règle** : Tout nouveau CLI utilisant des chemins fichiers DOIT passer par `safe_read_path` / `safe_write_path`. Tests dans `test_base.py`.

---

## Lesson #2 — Secrets committés avant le gitignore fortress

**Date** : 2026-03-14
**Contexte** : Audit sécurité

**Erreur** : `ccpa.config.json` et des tokens se retrouvaient dans l'historique git. Le `.gitignore` initial ne couvrait pas assez de patterns.

**Cause racine** : `.gitignore` trop minimaliste au départ — seuls `.env` et `node_modules` étaient exclus. Pas de scan automatique.

**Fix** : Gitignore "fortress" (b5beaa3) + pre-commit hook `secrets-scan` qui détecte les patterns de clés/tokens avant chaque commit.

**Règle** : Toujours vérifier `.gitignore` avant d'ajouter un nouveau type de fichier sensible. Le hook `secrets-scan` est la dernière barrière — ne jamais le bypass sans justification documentée.

---

## Lesson #3 — Workflows n8n obsolètes accumulés

**Date** : 2026-03-15
**Contexte** : Nettoyage post-audit

**Erreur** : 8 fichiers JSON de workflows n8n obsolètes traînaient dans `systems/workflows/`. Confusion sur ce qui était actif vs legacy.

**Cause racine** : Pas de convention de nommage avec statut (`[Prod]`, `[Offline]`, `[ForDeletion]`) au début du projet. Les exports étaient juste copiés sans tri.

**Fix** : Suppression des 8 fichiers (b8ab0b5 → 211dc34). Convention de nommage avec tags de statut ajoutée dans CONTRIBUTING.md.

**Règle** : Tout workflow exporté doit porter un tag de statut dans son nom. Un workflow `[Offline]` depuis plus de 30 jours → `[ForDeletion]`.

---

## Lesson #4 — Pas de CI/CD — les hooks sont la seule barrière [RESOLVED]

**Date** : 2026-03-24
**Contexte** : Audit workspace
**Résolu** : CI ajouté dans `.github/workflows/ci.yml` — ruff check + ruff format + pytest avec coverage (fail_under=40%). Voir section "CI (GitHub Actions)" dans CLAUDE.md.

**Erreur initiale** : Aucune GitHub Action configurée. Toute la qualité reposait sur les pre-commit hooks locaux (`secrets-scan` + `ruff` + `pip-audit`). Si un dev les bypass (`--no-verify`), rien ne rattrapait.

**Cause racine** : Projet solo, priorisation de la production de contenu sur l'infra CI/CD.

**Règle** : Accepté comme dette technique connue. Mitigation : `--no-verify` interdit sauf hook cassé (documenter pourquoi dans le commit). À réévaluer quand le projet aura des contributeurs externes.

---

## Lesson #5 — Venv Windows + Bash = activation qui ne persiste pas

**Date** : 2026-02-10
**Contexte** : Setup initial

**Erreur** : `source .venv/Scripts/activate` dans Claude Code Bash ne persiste pas entre les commandes. Les scripts échouaient silencieusement en utilisant le Python système.

**Cause racine** : Chaque commande Bash dans Claude Code est un sous-shell indépendant. L'activation d'un venv modifie des variables d'environnement qui disparaissent.

**Fix** : Utiliser le chemin complet `.venv/Scripts/python` partout. Documenté dans CLAUDE.md.

**Règle** : Ne jamais compter sur `activate` dans un contexte non-interactif. Toujours `.venv/Scripts/python -m ...`.

---

## Lesson #6 — Commits multiples pour un même changement logique

**Date** : 2026-03-15
**Contexte** : Session sécurité

**Erreur** : L'audit sécurité 5 volets a généré 4 commits quasi-identiques (5c277ed → 312375d) + les corrections OWASP en 6 commits séparés. L'historique est bruyant.

**Cause racine** : Changements trop gros pour un seul commit, mais découpés par batch technique (fichiers) plutôt que par changement logique.

**Fix** : Documenté les conventions dans CONTRIBUTING.md — commits atomiques par changement logique, pas par batch de fichiers.

**Règle** : Un changement logique = un commit. Si c'est trop gros, découper par fonctionnalité (ex: "path traversal agents 1-14" puis "agents 15-28"), pas par nombre de fichiers.

---

## Lesson #7 — brain.bat référence un venv legacy inexistant

**Date** : 2026-03-05
**Contexte** : Tentative d'exécution pipeline

**Erreur** : `brain.bat` et `brain-lite.bat` pointent vers `tools/scripts/legacy/scripts/.venv/` qui n'existe plus. Les commandes échouent silencieusement.

**Cause racine** : Migration vers le root venv (`.venv/`) sans mise à jour des wrappers batch.

**Règle** : Documenté dans CLAUDE.md comme workaround. Les .bat restent comme raccourcis historiques — utiliser `.venv/Scripts/python -m agents.content_factory.cli ...` directement.

---

## Lesson #8 — 374 skills = bruit, pas signal

**Date** : 2026-03-24
**Contexte** : Audit workspace

**Erreur** : 374 skills Claude Code enregistrés (281 projet + 50 workspace + 43 legacy). Beaucoup sont des doublons ou des variations mineures. Le temps de sélection du bon skill ralentit l'exécution.

**Cause racine** : Création de skills sans vérifier l'existant. Pas de revue périodique ni de déduplication.

**Règle** : Avant de créer un skill, vérifier l'INDEX et le registry. Audit mensuel des skills (prochain : avril 2026). Objectif : réduire à <150 skills uniques.

---

## Lesson #9 — BrainLiteAgent manquant = import cassé silencieux

**Date** : 2026-03-25
**Contexte** : Tests E2E pipelines

**Erreur** : `content_factory/agent.py` importait `BrainLiteAgent` depuis `brain_lite_cli.py`, mais la classe n'existait pas. L'`__init__.py` de content_factory re-exportait ce module, donc tout import du package crashait avec `ImportError`.

**Cause racine** : Refactoring du CLI brain-lite qui a supprimé/déplacé la classe sans mettre à jour les imports. Aucun test ne couvrait le pipeline complet.

**Fix** : Classe `BrainLiteAgent` créée dans `brain_lite_cli.py` — wrapper stratégique qui retourne un dict `{topic, angle, audience, roi_ok}` en un appel LLM.

**Règle** : Tout nouveau pipeline doit avoir au minimum un test E2E mocké qui valide la chaîne d'imports et l'orchestration.

---

## Lesson #10 — Signatures d'agents incohérentes entre pipeline et sous-agents

**Date** : 2026-03-25
**Contexte** : Tests E2E pipelines

**Erreur** : `pipeline.py` appelait `SeoAuditorAgent.run(content=...)` et `ClusterArchitectAgent.run(keyword=..., pillar=...)` — mais les signatures réelles étaient `article=` et `thematique=, objectif=`. Crash systématique à l'exécution.

**Cause racine** : Les agents ont été refactorisés indépendamment du pipeline qui les orchestre. Pas de contrat typé entre orchestrateur et sous-agents.

**Fix** : Corrigé `pipeline.py` : `content=` → `article=`, `keyword=/pillar=` → `thematique=/objectif=`. Import `SeoEditorAgent` déplacé dans le `try` block.

**Règle** : Si tu changes la signature `run()` d'un agent, chercher tous les appelants avec `grep "AgentName" core/agents-py/` et mettre à jour.

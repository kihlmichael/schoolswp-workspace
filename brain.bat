@echo off
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REM  schoolsWP Brain — Content Factory
REM  Stratégie → Article → Audit 4 modules → Cluster sémantique
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REM
REM  MODE GÉNÉRATION (depuis mot-clé) :
REM    brain.bat --keyword "lms wordpress rentable" --intent décisionnelle --pillar LMS
REM    brain.bat --keyword "fluentcrm avis" --intent informationnelle --pillar CRM
REM    brain.bat --keyword "tutor lms vs learndash" --intent comparative --pillar LMS --include-ner
REM
REM  MODE AUDIT (article existant) :
REM    brain.bat --file content/articles/lms-pilier/v3.md --kw "lms wordpress" --intent décisionnelle
REM    brain.bat --file content/articles/crm/fluentcrm.md --kw "fluentcrm wordpress" --pillar CRM
REM
REM  OPTIONS :
REM    --keyword      Mot-clé principal → mode génération (requis en génération)
REM    --file         Fichier markdown → mode audit seul
REM    --kw           Mot-clé pour mode audit (requis avec --file)
REM    --intent       informationnelle | comparative | décisionnelle
REM    --pillar       SEO | LMS | CRM | Performance | Automatisation
REM    --objective    email | affiliation | formation | offre
REM    --include-serp Simulation SERP Top 5 (+~2 min, mode génération)
REM    --include-ner  Enrichissement NER sémantique (+~1-2 min, mode génération)
REM    --no-links     Désactive le maillage interne
REM    --no-cluster   Désactive le plan cluster
REM    --force        Forcer même si ROI faible
REM    --save-dir     Dossier de sauvegarde (auto si absent)
REM    --model        Modèle Claude (défaut: claude-sonnet-4-6)
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

cd /d "%~dp0"
tools\scripts\legacy\scripts\.venv\Scripts\python -m agents.content_factory.cli %*

@echo off
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REM  Brain Lite — schoolsWP Content Machine
REM  Workflow 5 étapes : Brain → Writer → Audit → LLM → Maillage
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REM
REM  Usage :
REM    brain-lite.bat --keyword "lms wordpress rentable" --intent décisionnelle
REM    brain-lite.bat --keyword "fluentcrm vs activecampaign" --intent comparative --pilier crm
REM    brain-lite.bat --keyword "tutor lms avis" --intent informationnelle --save-dir content/articles/lms/
REM
REM  Options complètes :
REM    --keyword      Mot-clé principal (requis)
REM    --intent       informationnelle | comparative | décisionnelle (requis)
REM    --pilier       seo | lms | crm | performance | automatisation | ecommerce (optionnel)
REM    --save-dir     Dossier de sauvegarde (auto si absent)
REM    --output       Fichier de sortie principal (optionnel)
REM    --force        Forcer la production même si ROI faible
REM    --model        Modèle Claude (défaut: claude-sonnet-4-6)
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

cd /d "%~dp0"
.venv\Scripts\python -m agents.article_pipeline.brain_lite_cli %*

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
setlocal enabledelayedexpansion

REM ─── Capture start time (secondes depuis minuit) ─────────────────
for /f "tokens=1-4 delims=:.," %%a in ("!TIME!") do set /a _START=((%%a*3600)+(%%b*60)+%%c)

REM ─── Extraction des args pour la notif (keyword, pillar, intent) ─
set "_KW="
set "_PILLAR="
set "_INTENT="
set "_NEXT="
for %%A in (%*) do (
  if defined _NEXT (
    if "!_NEXT!"=="kw" set "_KW=%%~A"
    if "!_NEXT!"=="pillar" set "_PILLAR=%%~A"
    if "!_NEXT!"=="intent" set "_INTENT=%%~A"
    set "_NEXT="
  ) else (
    if "%%~A"=="--keyword" set "_NEXT=kw"
    if "%%~A"=="--kw" set "_NEXT=kw"
    if "%%~A"=="--pillar" set "_NEXT=pillar"
    if "%%~A"=="--intent" set "_NEXT=intent"
  )
)

.venv\Scripts\python -m agents.content_factory.cli %*
set _EXIT=!ERRORLEVEL!

REM ─── Compute duration + status ───────────────────────────────────
for /f "tokens=1-4 delims=:.," %%a in ("!TIME!") do set /a _END=((%%a*3600)+(%%b*60)+%%c)
set /a _DUR=!_END!-!_START!
if !_DUR! lss 0 set /a _DUR=!_DUR!+86400
if !_EXIT! equ 0 (set _STATUS=ok) else (set _STATUS=fail)

REM ─── Notif Discord + Telegram (skip silencieux si creds absents) ─
.venv\Scripts\python tools\scripts\notify-brain-done.py ^
  --keyword "!_KW!" --pillar "!_PILLAR!" --intent "!_INTENT!" ^
  --status !_STATUS! --duration !_DUR! --exit-code !_EXIT! 2>nul

endlocal & exit /b %_EXIT%

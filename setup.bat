@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul 2>&1

REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REM  schoolsWP — Setup nouveau PC
REM  Installe toutes les dépendances et configure l'environnement
REM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

cd /d "%~dp0"

echo.
echo ══════════════════════════════════════════════════════════════
echo   schoolsWP — Setup nouveau PC
echo ══════════════════════════════════════════════════════════════
echo.

set ERRORS=0
set WARNINGS=0

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 1 — Vérification des prérequis système
REM ──────────────────────────────────────────────────────────────
echo [1/6] Vérification des prérequis système...
echo.

REM Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   [MANQUANT] Python n'est pas installé ou pas dans le PATH
    echo              Télécharger : https://www.python.org/downloads/
    echo              Cocher "Add Python to PATH" lors de l'installation
    set /A ERRORS+=1
) else (
    for /f "tokens=*" %%v in ('python --version 2^>^&1') do echo   [OK] %%v
)

REM Node.js
node --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   [MANQUANT] Node.js n'est pas installé
    echo              Télécharger : https://nodejs.org/ (LTS)
    set /A ERRORS+=1
) else (
    for /f "tokens=*" %%v in ('node --version 2^>^&1') do echo   [OK] Node.js %%v
)

REM npm
npm --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   [MANQUANT] npm non disponible (inclus avec Node.js)
    set /A ERRORS+=1
) else (
    for /f "tokens=*" %%v in ('npm --version 2^>^&1') do echo   [OK] npm %%v
)

REM Git
git --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   [MANQUANT] Git n'est pas installé
    echo              Télécharger : https://git-scm.com/download/win
    set /A ERRORS+=1
) else (
    for /f "tokens=*" %%v in ('git --version 2^>^&1') do echo   [OK] %%v
)

REM Docker
docker --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   [AVERTISSEMENT] Docker Desktop non détecté
    echo                   Requis pour n8n local : https://www.docker.com/products/docker-desktop/
    set /A WARNINGS+=1
) else (
    for /f "tokens=*" %%v in ('docker --version 2^>^&1') do echo   [OK] %%v
)

echo.

if %ERRORS% GTR 0 (
    echo   !! %ERRORS% prérequis manquants — installer les programmes ci-dessus puis relancer ce script
    echo.
    pause
    exit /b 1
)

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 2 — Python : uv + dépendances
REM ──────────────────────────────────────────────────────────────
echo [2/6] Installation des dépendances Python...
echo.

REM Installer uv si absent
uv --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   Installation de uv...
    pip install uv --quiet
    if %ERRORLEVEL% NEQ 0 (
        echo   [ERREUR] Impossible d'installer uv
        set /A ERRORS+=1
        goto step3
    )
    echo   [OK] uv installé
) else (
    for /f "tokens=*" %%v in ('uv --version 2^>^&1') do echo   [OK] uv déjà installé (%%v)
)

REM Synchroniser les dépendances Python
echo   Synchronisation des dépendances Python (uv sync)...
uv sync --quiet
if %ERRORLEVEL% NEQ 0 (
    echo   [ERREUR] uv sync a échoué — vérifier pyproject.toml
    set /A ERRORS+=1
) else (
    echo   [OK] Dépendances Python installées (.venv prêt)
)

:step3
echo.

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 3 — JavaScript : npm install
REM ──────────────────────────────────────────────────────────────
echo [3/6] Installation des dépendances JavaScript...
echo.

if exist "package.json" (
    echo   npm install en cours...
    npm install --silent
    if %ERRORLEVEL% NEQ 0 (
        echo   [ERREUR] npm install a échoué
        set /A ERRORS+=1
    ) else (
        echo   [OK] Dépendances JS installées (node_modules/)
    )
) else (
    echo   [SKIP] Pas de package.json à la racine
)

REM MCP serveurs globaux (n8n-mcp, firecrawl-mcp, etc.)
echo   Installation des serveurs MCP globaux...
npm install -g n8n-mcp --silent >nul 2>&1
npm install -g firecrawl-mcp --silent >nul 2>&1
npm install -g actors-mcp-server --silent >nul 2>&1
npm install -g wisewand-mcp --silent >nul 2>&1
npm install -g dataforseo-mcp-server --silent >nul 2>&1
npm install -g mcp-remote --silent >nul 2>&1
echo   [OK] Serveurs MCP npm installés

echo.

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 4 — Fichiers de configuration
REM ──────────────────────────────────────────────────────────────
echo [4/6] Configuration des fichiers d'environnement...
echo.

REM .env
if not exist ".env" (
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo   [OK] .env créé depuis .env.example
        echo   !! A REMPLIR : ANTHROPIC_API_KEY dans .env
    ) else (
        echo   [AVERTISSEMENT] .env.example introuvable
        set /A WARNINGS+=1
    )
) else (
    echo   [OK] .env existe déjà
)

REM .mcp.json
if not exist ".mcp.json" (
    if exist ".mcp.json.example" (
        copy ".mcp.json.example" ".mcp.json" >nul
        echo   [OK] .mcp.json créé depuis .mcp.json.example
        echo   !! A REMPLIR : clés API dans .mcp.json
    ) else (
        echo   [AVERTISSEMENT] .mcp.json.example introuvable
        set /A WARNINGS+=1
    )
) else (
    echo   [OK] .mcp.json existe déjà
)

REM Patch chemin GitHub MCP (C:/Users/micha → utilisateur courant)
if exist ".mcp.json" (
    set CURRENT_USER=%USERNAME%
    REM Remplacer l'ancien chemin utilisateur si nécessaire
    powershell -Command "(Get-Content '.mcp.json') -replace 'C:/Users/micha/', 'C:/Users/%USERNAME%/' | Set-Content '.mcp.json'" >nul 2>&1
    echo   [OK] Chemin GitHub MCP adapté pour l'utilisateur %USERNAME%
)

echo.

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 5 — Pre-commit hooks
REM ──────────────────────────────────────────────────────────────
echo [5/6] Installation des hooks pre-commit...
echo.

pre-commit --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo   Installation de pre-commit...
    pip install pre-commit --quiet
)

if exist ".pre-commit-config.yaml" (
    pre-commit install --quiet
    if %ERRORLEVEL% NEQ 0 (
        echo   [AVERTISSEMENT] pre-commit install a échoué (pas bloquant)
        set /A WARNINGS+=1
    ) else (
        echo   [OK] Hooks git pre-commit installés
    )
) else (
    echo   [SKIP] .pre-commit-config.yaml introuvable
)

echo.

REM ──────────────────────────────────────────────────────────────
REM  ÉTAPE 6 — Vérification finale
REM ──────────────────────────────────────────────────────────────
echo [6/6] Vérification finale...
echo.

REM Tester que Python et les agents fonctionnent
if exist ".venv\Scripts\python.exe" (
    .venv\Scripts\python -c "import anthropic; import dotenv; print('  [OK] anthropic + dotenv importables')" 2>nul
    if %ERRORLEVEL% NEQ 0 (
        echo   [AVERTISSEMENT] Certaines dépendances Python non importables
        set /A WARNINGS+=1
    )
) else (
    echo   [AVERTISSEMENT] .venv non trouvé — uv sync n'a peut-être pas fonctionné
    set /A WARNINGS+=1
)

REM Vérifier que ANTHROPIC_API_KEY est renseignée dans .env
if exist ".env" (
    findstr /C:"ANTHROPIC_API_KEY=your-anthropic" ".env" >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo   [!!] ANTHROPIC_API_KEY non configurée dans .env — les agents ne fonctionneront pas
        set /A WARNINGS+=1
    ) else (
        findstr /C:"ANTHROPIC_API_KEY=" ".env" >nul 2>&1
        if %ERRORLEVEL% EQU 0 (
            echo   [OK] ANTHROPIC_API_KEY présente dans .env
        )
    )
)

echo.

REM ──────────────────────────────────────────────────────────────
REM  RÉSUMÉ
REM ──────────────────────────────────────────────────────────────
echo ══════════════════════════════════════════════════════════════
if %ERRORS% EQU 0 (
    if %WARNINGS% EQU 0 (
        echo   Setup terminé avec succès !
    ) else (
        echo   Setup terminé avec %WARNINGS% avertissement(s) à corriger
    )
) else (
    echo   Setup incomplet — %ERRORS% erreur(s), %WARNINGS% avertissement(s)
)
echo ══════════════════════════════════════════════════════════════
echo.
echo   Actions manuelles restantes :
echo.
echo   1. Remplir les clés API dans .env :
echo      - ANTHROPIC_API_KEY  (obligatoire)
echo      - FIRECRAWL_API_KEY, RAPIDAPI_KEY, APIFY_API_TOKEN...
echo.
echo   2. Remplir les clés dans .mcp.json :
echo      - N8N_API_KEY, WP_API_PASSWORD, etc.
echo.
echo   3. Adapter le chemin GitHub MCP dans .mcp.json :
echo      Ligne "github" -> verifier C:/Users/%USERNAME%/.claude/mcp-github.sh
echo      (copier mcp-github.sh depuis l'ancien PC si nécessaire)
echo.
echo   4. [Optionnel] Lancer n8n local :
echo      docker compose -f systems/n8n/docker-compose.yml up -d
echo.
echo   5. Tester le pipeline :
echo      brain.bat --keyword "lms wordpress" --intent informationnelle --pillar LMS
echo.
echo ══════════════════════════════════════════════════════════════
echo.
pause
endlocal

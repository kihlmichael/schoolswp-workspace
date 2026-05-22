#Requires -Version 7
# ============================================================================
# memory-lint-launcher.ps1
# Lance le lint de la memoire interne schoolsWP, bride a 1x/jour.
# Invocable a la main, ou via la tache planifiee "schoolsWP Memory Lint".
#
# Design : le run Claude headless n'ecrit jamais dans le dossier memoire
# (traite comme sensible par le harness). Il ecrit ses resultats dans un
# dossier de staging cote projet ; ce launcher applique ensuite les
# ecritures dans le dossier memoire.
# ============================================================================

$ErrorActionPreference = 'Stop'

# --- Chemins ---
# tools/scripts/ -> racine projet (deux niveaux au-dessus)
$ProjectRoot  = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$MemoryDir    = 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory'
$ProcedureDoc = Join-Path $ProjectRoot 'obsidian-bridge\SOP-memory-lint.md'
$EnvFile      = Join-Path $ProjectRoot '.env'
$StagingDir   = Join-Path $PSScriptRoot '.lint-staging'
$ApplyDir     = Join-Path $StagingDir 'apply'
$StampFile    = Join-Path $MemoryDir '.last-lint'
$ResultFile   = Join-Path $MemoryDir '.lint-result.txt'
$LogMdFile    = Join-Path $MemoryDir 'LOG.md'
$LauncherLog  = Join-Path $MemoryDir '.lint-launcher.log'

function Write-LauncherLog([string]$msg) {
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ss'
    Add-Content -Path $LauncherLog -Value "$ts | $msg" -Encoding utf8
}

# --- Throttle : un seul run par jour ---
$today = Get-Date -Format 'yyyy-MM-dd'
if (Test-Path $StampFile) {
    if ((Get-Content $StampFile -Raw).Trim() -eq $today) {
        Write-LauncherLog 'skip : deja lance aujourd hui'
        exit 0
    }
}

# --- Pre-requis : claude sur le PATH ---
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-LauncherLog 'ERREUR : claude introuvable sur le PATH (pas de stamp, retry au prochain logon)'
    exit 1
}

# --- Pre-requis : procedure de lint presente ---
if (-not (Test-Path $ProcedureDoc)) {
    Write-LauncherLog "ERREUR : procedure introuvable : $ProcedureDoc"
    exit 1
}

# --- Webhook Discord depuis .env (le launcher poste ; Claude ne lit jamais .env) ---
$webhook = ''
if (Test-Path $EnvFile) {
    $line = Get-Content $EnvFile | Where-Object { $_ -match '^\s*DISCORD_ROUTINES_WEBHOOK\s*=' } | Select-Object -First 1
    if ($line) {
        $webhook = ($line -replace '^\s*DISCORD_ROUTINES_WEBHOOK\s*=', '').Trim().Trim('"')
    }
}

# --- Staging propre avant le run ---
if (Test-Path $StagingDir) { Remove-Item $StagingDir -Recurse -Force }
New-Item -ItemType Directory -Path $ApplyDir -Force | Out-Null

# --- Run du lint via Claude Code headless ---
# acceptEdits : le run ecrit uniquement dans le staging (cote projet, non
# sensible). Il lit le dossier memoire via --add-dir mais ne l'ecrit jamais ;
# c'est ce launcher qui applique les ecritures dans le dossier memoire.
$prompt = @"
Execute le lint de la memoire interne schoolsWP.
Suis STRICTEMENT la procedure decrite dans : $ProcedureDoc
Le dossier de la memoire interne (lecture seule pour toi) est : $MemoryDir
Le dossier de staging ou ecrire tous tes resultats est : $StagingDir
"@

Write-LauncherLog 'lancement du lint'
Push-Location $ProjectRoot
try {
    & claude -p $prompt --add-dir $MemoryDir --permission-mode acceptEdits
    $exitCode = $LASTEXITCODE
} finally {
    Pop-Location
}

if ($exitCode -ne 0) {
    Write-LauncherLog "ERREUR : lint sorti en code $exitCode (pas de stamp, retry au prochain logon)"
    exit $exitCode
}

# --- Verification : le lint a-t-il produit ses fichiers de staging ? ---
# Un headless qui sort en code 0 sans staging = echec silencieux.
$stagedLog    = Join-Path $StagingDir 'log-entry.md'
$stagedResult = Join-Path $StagingDir 'result.txt'
if ((-not (Test-Path $stagedLog)) -or (-not (Test-Path $stagedResult))) {
    Write-LauncherLog 'ERREUR : staging incomplet apres un run en code 0 (lint non persiste, pas de stamp, retry au prochain logon)'
    exit 1
}

# --- Application des ecritures dans le dossier memoire ---
# 1. Auto-fix : chaque fichier de staging/apply/ ecrase son homologue memoire.
$applied = 0
foreach ($f in Get-ChildItem -Path $ApplyDir -File) {
    Copy-Item -Path $f.FullName -Destination (Join-Path $MemoryDir $f.Name) -Force
    $applied++
}
# 2. Journal : ligne vide de separation puis entree LOG.md.
Add-Content -Path $LogMdFile -Value '' -Encoding utf8
Add-Content -Path $LogMdFile -Value (Get-Content $stagedLog -Raw).TrimEnd() -Encoding utf8
# 3. Fichier resultat.
Copy-Item -Path $stagedResult -Destination $ResultFile -Force
Write-LauncherLog "ecritures appliquees ($applied auto-fix)"

# --- Succes : ecrire le stamp de throttle ---
Set-Content -Path $StampFile -Value $today -Encoding utf8 -NoNewline

# --- Notification Discord si flags ---
$result = (Get-Content $ResultFile -Raw).Trim()
if ($webhook -and $result -and ($result -ne 'clean')) {
    if ($result.Length -gt 1900) { $result = $result.Substring(0, 1900) + ' [...]' }
    try {
        $body = @{ content = $result } | ConvertTo-Json -Compress
        Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json' -Body $body | Out-Null
        Write-LauncherLog 'notification Discord envoyee'
    } catch {
        $errMsg = $_.Exception.Message
        Write-LauncherLog "ERREUR notification Discord : $errMsg"
    }
}

Write-LauncherLog 'lint termine OK'
exit 0

#Requires -Version 7
# ============================================================================
# memory-normalize-launcher.ps1
# Lance le script de normalisation du frontmatter de la memoire interne
# schoolsWP. Idempotent : aucune ecriture si pas de drift.
#
# Trigger via la tache planifiee "schoolsWP Memory Normalize" (Weekly Monday 9h).
# ============================================================================

$ErrorActionPreference = 'Stop'

# --- Chemins ---
$ProjectRoot  = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$Script       = Join-Path $ProjectRoot 'tools\scripts\memory-normalize-frontmatter.py'
$Venv         = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
$MemoryDir    = 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory'
$EnvFile      = Join-Path $ProjectRoot '.env'
$LauncherLog  = Join-Path $MemoryDir '.normalize-launcher.log'

function Write-LauncherLog([string]$msg) {
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ss'
    Add-Content -Path $LauncherLog -Value "$ts | $msg" -Encoding utf8
}

# --- Pre-requis ---
if (-not (Test-Path $Venv)) {
    Write-LauncherLog "ERREUR : venv Python introuvable ($Venv)"
    exit 1
}
if (-not (Test-Path $Script)) {
    Write-LauncherLog "ERREUR : script de normalisation introuvable ($Script)"
    exit 1
}

# --- Webhook Discord depuis .env (le launcher poste ; Python ne lit jamais .env) ---
$webhook = ''
if (Test-Path $EnvFile) {
    $line = Get-Content $EnvFile | Where-Object { $_ -match '^\s*DISCORD_ROUTINES_WEBHOOK\s*=' } | Select-Object -First 1
    if ($line) {
        $webhook = ($line -replace '^\s*DISCORD_ROUTINES_WEBHOOK\s*=', '').Trim().Trim('"<>')
    }
}

# --- Run du script en mode --apply (idempotent : 0 ecriture si pas de drift) ---
Write-LauncherLog 'lancement normalisation'
Push-Location $ProjectRoot
try {
    $output = & $Venv $Script --apply 2>&1
    $exitCode = $LASTEXITCODE
} finally {
    Pop-Location
}
$outputStr = ($output | Out-String)

if ($exitCode -ne 0) {
    Write-LauncherLog "ECHEC : exit code $exitCode"
    if ($webhook) {
        try {
            $body = @{ content = "Normalisation memoire schoolsWP : ECHEC (exit $exitCode). Voir .normalize-launcher.log." } | ConvertTo-Json -Compress
            Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json' -Body $body | Out-Null
        } catch {}
    }
    exit $exitCode
}

# --- Parse la sortie pour detecter le drift effectif ---
$driftCount = 0
if ($outputStr -match 'Changements de .name:.\s*:\s*(\d+)') {
    $driftCount = [int]$Matches[1]
}
$wikiCount = 0
if ($outputStr -match '(\d+) wikilinks mis') {
    $wikiCount = [int]$Matches[1]
}

Write-LauncherLog "OK : $driftCount renomages, $wikiCount wikilinks"

# --- Notification Discord uniquement si drift detecte (signal, pas de bruit) ---
if ($webhook -and ($driftCount -gt 0 -or $wikiCount -gt 0)) {
    try {
        $msg = "Normalisation memoire schoolsWP : $driftCount fichiers renommes, $wikiCount wikilinks reroutes. Drift corrige."
        $body = @{ content = $msg } | ConvertTo-Json -Compress
        Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json' -Body $body | Out-Null
        Write-LauncherLog 'notification Discord envoyee'
    } catch {
        $errMsg = $_.Exception.Message
        Write-LauncherLog "ERREUR notification Discord : $errMsg"
    }
}

exit 0

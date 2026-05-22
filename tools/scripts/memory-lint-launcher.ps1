#Requires -Version 7
# ============================================================================
# memory-lint-launcher.ps1
# Lance le lint de la memoire interne schoolsWP, bride a 1x/jour.
# Invocable a la main, ou via la tache planifiee "schoolsWP Memory Lint".
# ============================================================================

$ErrorActionPreference = 'Stop'

# --- Chemins ---
# tools/scripts/ -> racine projet (deux niveaux au-dessus)
$ProjectRoot  = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$MemoryDir    = 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory'
$ProcedureDoc = Join-Path $ProjectRoot 'obsidian-bridge\SOP-memory-lint.md'
$EnvFile      = Join-Path $ProjectRoot '.env'
$StampFile    = Join-Path $MemoryDir '.last-lint'
$ResultFile   = Join-Path $MemoryDir '.lint-result.txt'
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

# --- Run du lint via Claude Code headless ---
# acceptEdits : auto-accepte les editions de fichiers ; le lint ne fait
# que des editions (pas de commande systeme, pas de web), donc aucun blocage interactif.
Remove-Item $ResultFile -ErrorAction SilentlyContinue
$prompt = @"
Execute le lint de la memoire interne schoolsWP.
Suis STRICTEMENT la procedure decrite dans : $ProcedureDoc
Le dossier de la memoire interne est : $MemoryDir
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

# --- Succes : ecrire le stamp de throttle ---
Set-Content -Path $StampFile -Value $today -Encoding utf8 -NoNewline

# --- Notification Discord si flags ---
if ((Test-Path $ResultFile) -and $webhook) {
    $result = (Get-Content $ResultFile -Raw).Trim()
    if ($result -and $result -ne 'clean') {
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
}

Write-LauncherLog 'lint termine OK'
exit 0

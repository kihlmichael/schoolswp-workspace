#Requires -Version 7
# ============================================================================
# healthcheck-telegram-agents.ps1
# Check local fiable de https://telegram-agents.wp1.host/health.
#
# Pourquoi local : la routine cloud claude.ai (trig_018QJMcvsFnQMzE2FT4tEPvp)
# echoue parfois a resoudre le domaine (passe derriere Cloudflare) depuis le
# proxy d'egress du sandbox -> faux positifs. Ce check tourne sur la machine de
# Michael, qui joint l'URL sans souci, et alerte sur Discord #alerts.
#
# Aucun run Claude : simple HTTP + retry + notif webhook.
# Lancement manuel : pwsh -NoProfile -File tools/scripts/healthcheck-telegram-agents.ps1
# Planifie : tache "schoolsWP Telegram Healthcheck" (voir register-* plus bas).
#
# Codes de sortie : 0 = service sain (silencieux). 1 = service KO (alerte
# envoyee). 2 = check non concluant cote local (erreur reseau de CETTE machine,
# alerte "non concluant" envoyee, sans conseiller de Deploy Now).
# ============================================================================

$ErrorActionPreference = 'Stop'

# --- Chemins : tools/scripts/ -> racine projet (deux niveaux au-dessus) ---
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$EnvFile     = Join-Path $ProjectRoot '.env'
$TgClaudeEnv = Join-Path $ProjectRoot 'agents\telegram-claude\.env'
$LogDir      = Join-Path $ProjectRoot 'logs'
$LogFile     = Join-Path $LogDir 'healthcheck-telegram-agents.log'

$HealthUrl   = 'https://telegram-agents.wp1.host/health'
# Porte de test : override d'URL pour valider le chemin d'alerte sans toucher la prod.
if ($env:HEALTHCHECK_URL_OVERRIDE) { $HealthUrl = $env:HEALTHCHECK_URL_OVERRIDE }
$RequiredAgents = @('studio', 'radar', 'flow', 'pulse')
$MaxAttempts = 3
$RetryDelaySec = 5
$TimeoutSec  = 15

if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }

function Write-Log([string]$msg) {
    $ts = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    Add-Content -Path $LogFile -Value "$ts | $msg" -Encoding utf8
}

# --- Webhook Discord depuis .env (jamais logge, jamais affiche) ---
function Get-EnvValue([string]$path, [string]$key) {
    if (-not (Test-Path $path)) { return '' }
    $line = Get-Content $path | Where-Object { $_ -match "^\s*$key\s*=" } | Select-Object -First 1
    if (-not $line) { return '' }
    return ($line -replace "^\s*$key\s*=", '').Trim().Trim('"').Trim("'")
}

# Canal Discord : webhook #alerts (POST pur, independant du token bot).
$webhook = Get-EnvValue $EnvFile 'DISCORD_ROUTINES_WEBHOOK'
# Canal Telegram : token bot (cascade tg-claude < .env) + chat_id du destinataire.
$tgToken = Get-EnvValue $EnvFile 'TELEGRAM_NOTIF_TOKEN'
if (-not $tgToken) { $tgToken = Get-EnvValue $TgClaudeEnv 'TELEGRAM_TOKEN_STUDIO' }
$tgChat = Get-EnvValue $EnvFile 'TELEGRAM_HEALTHCHECK_CHAT_ID'
if (-not $tgChat) { $tgChat = Get-EnvValue $EnvFile 'TELEGRAM_NOTIF_CHAT_ID' }

function Send-DiscordAlert([string]$content) {
    if (-not $webhook) {
        Write-Log 'Discord skip : DISCORD_ROUTINES_WEBHOOK absent du .env'
        return
    }
    if ($content.Length -gt 1900) { $content = $content.Substring(0, 1900) + ' [...]' }
    try {
        $body = @{ content = $content } | ConvertTo-Json -Compress
        Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json' -Body $body | Out-Null
        Write-Log 'alerte Discord envoyee'
    } catch {
        Write-Log "ERREUR envoi Discord : $($_.Exception.Message)"
    }
}

function Send-TelegramAlert([string]$text) {
    if (-not $tgToken -or -not $tgChat) {
        Write-Log 'Telegram skip : token ou chat_id absent'
        return
    }
    if ($text.Length -gt 3900) { $text = $text.Substring(0, 3900) + ' [...]' }
    try {
        $body = @{ chat_id = $tgChat; text = $text; disable_web_page_preview = $true } | ConvertTo-Json -Compress
        $uri = "https://api.telegram.org/bot$tgToken/sendMessage"
        Invoke-RestMethod -Uri $uri -Method Post -ContentType 'application/json' -Body $body | Out-Null
        Write-Log 'alerte Telegram envoyee'
    } catch {
        Write-Log "ERREUR envoi Telegram : $($_.Exception.Message)"
    }
}

# Fan-out : envoie sur tous les canaux configures (chacun skip silencieux si absent).
function Send-Alert([string]$content) {
    Send-DiscordAlert $content
    Send-TelegramAlert $content
}

# --- Tentatives ---
$httpCode = $null
$bodyText = ''
$netError = ''

for ($i = 1; $i -le $MaxAttempts; $i++) {
    try {
        $resp = Invoke-WebRequest -Uri $HealthUrl -TimeoutSec $TimeoutSec -SkipHttpErrorCheck -MaximumRedirection 5
        $httpCode = [int]$resp.StatusCode
        $bodyText = [string]$resp.Content
        $netError = ''
        Write-Log "tentative $i : HTTP $httpCode"
        if ($httpCode -eq 200) { break }
    } catch {
        # Erreur reseau de CETTE machine (DNS, connexion refusee, timeout dur)
        $httpCode = $null
        $bodyText = ''
        $netError = $_.Exception.Message
        Write-Log "tentative $i : erreur reseau locale : $netError"
    }
    if ($i -lt $MaxAttempts) { Start-Sleep -Seconds $RetryDelaySec }
}

$nowUtc = (Get-Date).ToUniversalTime().ToString('yyyy-MM-dd HH:mm:ss \U\T\C')

# --- Classification ---
# A. HEALTHY : 200 + status ok + tous les agents requis presents
if ($httpCode -eq 200) {
    $statusOk = $bodyText -match '"status"\s*:\s*"ok"'
    $missing = $RequiredAgents | Where-Object { $bodyText -notmatch [regex]::Escape("`"$_`"") }
    if ($statusOk -and -not $missing) {
        Write-Log 'OK telegram-agents healthy'
        exit 0
    }
    # C. SERVICE_DOWN : le service repond, mais mal (status pas ok ou agents manquants)
    $reason = if (-not $statusOk) { 'champ status != ok' } else { "agents manquants : $($missing -join ', ')" }
    $excerpt = if ($bodyText.Length -gt 400) { $bodyText.Substring(0, 400) + '…' } else { $bodyText }
    $msg = @"
🚨 **telegram-agents DOWN** — healthcheck local KO
Date : $nowUtc
Code HTTP : 200 mais reponse invalide ($reason)
Reponse : ``$excerpt``
Action : xCloud (https://app.xcloud.host) → app telegram_agents → **Deploy Now**.
Si Deploy Now casse sur ecosystem.config.cjs : Run Custom Command →
``cd /home/telegram_agents/files && pm2 start ecosystem.config.cjs --only telegram-agents && pm2 save``
"@
    Send-Alert $msg
    Write-Log "SERVICE_DOWN (200 invalide : $reason)"
    exit 1
}

# C. SERVICE_DOWN : on a une vraie reponse HTTP du service mais code != 200
if ($null -ne $httpCode) {
    $excerpt = if ($bodyText.Length -gt 400) { $bodyText.Substring(0, 400) + '…' } else { $bodyText }
    $msg = @"
🚨 **telegram-agents DOWN** — healthcheck local KO
Date : $nowUtc
Code HTTP : $httpCode (apres $MaxAttempts tentatives)
Reponse : ``$excerpt``
Action : xCloud (https://app.xcloud.host) → app telegram_agents → **Deploy Now**.
Si Deploy Now casse sur ecosystem.config.cjs : Run Custom Command →
``cd /home/telegram_agents/files && pm2 start ecosystem.config.cjs --only telegram-agents && pm2 save``
"@
    Send-Alert $msg
    Write-Log "SERVICE_DOWN (HTTP $httpCode)"
    exit 1
}

# B. CHECKER_UNREACHABLE : aucune reponse HTTP, erreur reseau de cette machine
$msg = @"
ℹ️ **Healthcheck telegram-agents NON CONCLUANT** (reseau local)
Date : $nowUtc
Aucune reponse HTTP apres $MaxAttempts tentatives. Erreur reseau de la machine de check (DNS/connexion), PAS une panne confirmee du service. **NE PAS** lancer de Deploy Now sur cette seule base.
Erreur : ``$netError``
Verif manuelle : ouvre $HealthUrl dans un navigateur. Si 200 + status ok → ignorer.
"@
Send-DiscordAlert $msg
Write-Log "CHECKER_UNREACHABLE : $netError"
exit 2

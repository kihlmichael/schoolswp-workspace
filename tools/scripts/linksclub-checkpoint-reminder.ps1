#Requires -Version 5.1
# ============================================================================
# linksclub-checkpoint-reminder.ps1
# Poste un rappel Discord (#alerts) a chaque checkpoint de la campagne
# Linksclub liens forum (juin -> oct 2026).
#
# Le rappel invite Michael a lancer la mesure d'impact EN SESSION.
# Ce script ne collecte AUCUNE donnee (pas de GSC, pas d'Ubersuggest) : il
# poste uniquement le rappel.
#
# Invocation :
#   - a la main : pwsh -File linksclub-checkpoint-reminder.ps1 [-Test]
#   - via la tache planifiee "schoolsWP Linksclub Checkpoint"
#     (15 du mois, 09h, juillet -> novembre 2026, rattrapage si PC eteint)
#
# Secret : le webhook est lu depuis .env au runtime (jamais commite, jamais
# expose dans un transcript). Meme pattern que memory-lint-launcher.ps1.
# ============================================================================

param([switch]$Test)

$ErrorActionPreference = 'Stop'

# --- Chemins : tools/scripts/ -> racine projet (deux niveaux au-dessus) ---
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$EnvFile     = Join-Path $ProjectRoot '.env'
$TrackerRel  = 'content/audits/_campaigns/linksclub-forum-2026-06.md'
$LogFile     = Join-Path $PSScriptRoot 'linksclub-checkpoint-reminder.log'

function Write-Log([string]$msg) {
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ss'
    Add-Content -Path $LogFile -Value "$ts | $msg" -Encoding utf8
}

# --- Webhook Discord depuis .env (Claude ne lit jamais .env ; ce script si) ---
$webhook = ''
if (Test-Path $EnvFile) {
    $line = Get-Content $EnvFile | Where-Object { $_ -match '^\s*DISCORD_ROUTINES_WEBHOOK\s*=' } | Select-Object -First 1
    if ($line) {
        $webhook = ($line -replace '^\s*DISCORD_ROUTINES_WEBHOOK\s*=', '').Trim().Trim('"')
    }
}
if (-not $webhook) {
    Write-Log 'ERREUR : DISCORD_ROUTINES_WEBHOOK introuvable dans .env (pas de post)'
    exit 1
}

# --- Construction du message (single-quote here-string + -f : backticks et
#     accents sont litteraux, pas d'echappement PowerShell a gerer) ---
$fr     = [System.Globalization.CultureInfo]::GetCultureInfo('fr-FR')
$mois   = (Get-Date).ToString('MMMM yyyy', $fr)
$prefix = if ($Test) { '[TEST] ' } else { '' }

$template = @'
{0}**Checkpoint campagne Linksclub forum - {1}**
Lance la mesure d'impact EN SESSION (GSC + Ubersuggest sur les 3 pages cibles) puis remplis le tableau de checkpoints dans `{2}`.

Baseline (2026-06-04) a comparer :
- Accueil : 8 clics / pos 3,4
- apprendre-wordpress-autonomie : 2 clics / pos 25,5
- fluentcrm-automations-indispensables : 1 clic / pos 16,3
- 90 domaines referents (Ubersuggest)
'@
$message = $template -f $prefix, $mois, $TrackerRel

# --- Garde-fou limite Discord (2000 chars, headroom) ---
if ($message.Length -gt 1900) { $message = $message.Substring(0, 1900) + ' [...]' }

# --- POST (corps encode UTF-8 explicite pour preserver les accents) ---
# TLS 1.2 force pour Windows PowerShell 5.1 (Discord refuse TLS < 1.2).
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    $body  = @{ content = $message } | ConvertTo-Json -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($body)
    Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json; charset=utf-8' -Body $bytes | Out-Null
    Write-Log "rappel poste ($mois)$(if ($Test) { ' [test]' })"
} catch {
    Write-Log "ERREUR post Discord : $($_.Exception.Message)"
    exit 1
}

exit 0

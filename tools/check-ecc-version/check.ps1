# ECC version watcher
# Detecte la sortie de affaan-m/everything-claude-code version 2 GA (transition rc -> GA).
# Output : rapport Markdown + POST Discord webhook si GA detectee.
#
# Usage :
#   .\check.ps1                                                # check silent, sortie console
#   .\check.ps1 -ReportFile "report.md"                        # ecrit le rapport dans un fichier
#   .\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..."  # POST si GA detectee
#
# Pre-requis : git CLI dans le PATH, acces lecture clone ECC dans projects/everything-claude-code/
#
# Critere GA : VERSION matche ^v?\d+\.\d+\.\d+$ (3 nombres sans suffixe pre-release)
# OU un tag de release dans le repo matche ce pattern.

param(
    [Parameter(Mandatory=$false)]
    [string]$EccRepoDir = "d:\VS Code\CLAUDE CODE\projects\everything-claude-code",

    [Parameter(Mandatory=$false)]
    [string]$WebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$N8nWebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$ReportFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$BaselineFile = $null
)

$ErrorActionPreference = "Stop"
$DateRun = (Get-Date -Format "yyyy-MM-dd HH:mm")

# Fallback env var pour WebhookUrl si pas passe en parametre
# Variable user persistante DISCORD_SCHOOLSWP_ROUTINES_URL (set via [Environment]::SetEnvironmentVariable)
if (-not $WebhookUrl -and $env:DISCORD_SCHOOLSWP_ROUTINES_URL) {
    $WebhookUrl = $env:DISCORD_SCHOOLSWP_ROUTINES_URL
}
if (-not $N8nWebhookUrl -and $env:N8N_ECC_VERSION_WATCHER_URL) {
    $N8nWebhookUrl = $env:N8N_ECC_VERSION_WATCHER_URL
}

if (-not (Test-Path $EccRepoDir)) {
    Write-Error "ECC repo dir introuvable : $EccRepoDir"
    exit 1
}

# Resolution baseline
$Baseline = @{
    version = "2.0.0-rc.1"
    commit = "1e8c7e7"
    set_at = "2026-05-24"
}
if (-not $BaselineFile) {
    $BaselineFile = Join-Path $PSScriptRoot ".baseline.json"
}
if (Test-Path $BaselineFile) {
    $baselineData = Get-Content $BaselineFile -Raw | ConvertFrom-Json
    $Baseline.version = $baselineData.version
    $Baseline.commit = $baselineData.commit
    $Baseline.set_at = $baselineData.set_at
}

# 1. git fetch silencieux
Push-Location $EccRepoDir
Write-Host "=== ECC version watcher - $DateRun ==="
Write-Host "Repo : $EccRepoDir"
Write-Host "Baseline : v$($Baseline.version) (set $($Baseline.set_at))"

try {
    git fetch origin --quiet 2>&1 | Out-Null
} catch {
    Write-Warning "git fetch echoue : $_"
}

# 2. Lecture VERSION sur origin/HEAD (pas local HEAD, pour eviter dependance pull)
$versionPath = "VERSION"
$version = $null
try {
    $version = (git show origin/HEAD:$versionPath 2>$null).Trim()
} catch {
    # Fallback local
    if (Test-Path $versionPath) {
        $version = (Get-Content $versionPath -Raw).Trim()
    }
}

if (-not $version) {
    Write-Error "Impossible de lire VERSION dans le repo"
    Pop-Location
    exit 1
}

# 3. Tags releases sur origin
$tags = @(git tag --list --sort=-creatordate)
$commitsAhead = (git log --oneline HEAD..origin/HEAD 2>$null | Measure-Object -Line).Lines

# 4. Detection GA
$gaPattern = '^v?\d+\.\d+\.\d+$'
$versionIsGa = $version -match $gaPattern
$gaTags = @($tags | Where-Object { $_ -match $gaPattern })
$gaDetected = $versionIsGa -or ($gaTags.Count -gt 0)

$versionChanged = ($version -ne $Baseline.version)

Pop-Location

# 5. Rapport
$report = "# ECC version watcher - $DateRun" + [char]10 + [char]10
$report += "- **VERSION origin/HEAD** : $version" + [char]10
$report += "- **Baseline** : $($Baseline.version) (set $($Baseline.set_at))" + [char]10
$report += "- **Version changee depuis baseline** : $versionChanged" + [char]10
$report += "- **Tags GA detectes** : $($gaTags -join ', ')" + [char]10
$report += "- **Commits ahead** : $commitsAhead" + [char]10
$report += "- **GA detected** : $gaDetected" + [char]10 + [char]10

if ($gaDetected) {
    $report += "## ECC version 2 GA est sortie." + [char]10 + [char]10
    $report += "Action : lancer la passe 3 ECC en suivant 05_sop/SOP-cherry-pick-depots-tiers-claude-code.md (vault Obsidian)." + [char]10
} elseif ($versionChanged) {
    $report += "## Version a change mais pas encore GA." + [char]10 + [char]10
    $report += "VERSION : $($Baseline.version) -> $version. Probable nouvelle rc ou pre-release." + [char]10
    $report += "Pas d'action requise. Mise a jour de la baseline possible si le changement est durable." + [char]10
} else {
    $report += "Pas de changement detecte. ECC toujours en $version (rc, pas GA)." + [char]10
}

Write-Host ""
Write-Host $report

if ($ReportFile) {
    Set-Content -Path $ReportFile -Value $report -Encoding UTF8
    Write-Host "Rapport ecrit : $ReportFile"
}

# 6. Discord webhook si fourni ET GA detectee
if ($WebhookUrl -and $gaDetected) {
    $discordMsg = ":rocket: **ECC version 2 GA detectee** - $DateRun" + [char]10 + [char]10
    $discordMsg += "VERSION origin/HEAD : ``$version``" + [char]10
    if ($gaTags.Count -gt 0) {
        $discordMsg += "Tag GA : ``$($gaTags -join ', ')``" + [char]10
    }
    $discordMsg += [char]10 + "Action : lancer passe 3 ECC via la SOP cherry-pick (05_sop dans le vault)."

    $payload = @{ content = $discordMsg } | ConvertTo-Json -Compress
    try {
        Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body $payload -ContentType "application/json"
        Write-Host "Discord webhook : POST OK"
    } catch {
        Write-Warning "Discord webhook : echec POST - $_"
    }
}

# 7. n8n webhook si fourni (structure complete pour orchestration)
if ($N8nWebhookUrl) {
    $n8nPayload = @{
        date = $DateRun
        source = "ecc-version-watcher"
        version_current = $version
        version_baseline = $Baseline.version
        version_changed = $versionChanged
        ga_tags = $gaTags
        ga_detected = $gaDetected
        commits_ahead = $commitsAhead
    } | ConvertTo-Json -Depth 5 -Compress

    try {
        Invoke-RestMethod -Uri $N8nWebhookUrl -Method Post -Body $n8nPayload -ContentType "application/json" | Out-Null
        Write-Host "n8n webhook : POST OK"
    } catch {
        Write-Warning "n8n webhook : echec POST - $_"
    }
}

# Exit codes : 0 si OK et pas de changement, 2 si GA detectee, 3 si version changee sans GA
if ($gaDetected) { exit 2 }
if ($versionChanged) { exit 3 }
exit 0

# HyperFrames launch watcher
# Detecte un nouveau commit sur un dossier d'un repo GitHub public (par defaut
# heygen-com/hyperframes-launches, path texture-launch-video).
# Output : rapport Markdown + POST Discord webhook si nouveau commit detecte.
#
# Usage :
#   .\check.ps1                                                # check silent, sortie console
#   .\check.ps1 -ReportFile "report.md"                        # ecrit le rapport dans un fichier
#   .\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..."  # POST si nouveau commit
#   .\check.ps1 -Repo "owner/repo" -Path "sous/dossier"        # surveiller un autre repo/dossier
#
# Pre-requis : acces reseau a api.github.com. Aucun clone local requis.
#
# Critere : le SHA du dernier commit touchant -Path differe du SHA baseline.
#
# Note securite : ce script ne lit JAMAIS GITHUB_TOKEN depuis l'environnement
# (cf. memoire feedback_github_token_env_override : la var ecrase le keyring gh).
# L'API publique non authentifiee (60 req/h) suffit pour un poll hebdo. Pour plus
# de marge de rate-limit, passer un token explicite via -GithubToken.

param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "heygen-com/hyperframes-launches",

    [Parameter(Mandatory=$false)]
    [string]$Path = "texture-launch-video",

    [Parameter(Mandatory=$false)]
    [string]$WebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$N8nWebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$ReportFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$BaselineFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$GithubToken = $null
)

$ErrorActionPreference = "Stop"
$DateRun = (Get-Date -Format "yyyy-MM-dd HH:mm")

# Fallback env var pour les webhooks (jamais GITHUB_TOKEN, voir entete)
if (-not $WebhookUrl -and $env:DISCORD_SCHOOLSWP_ROUTINES_URL) {
    $WebhookUrl = $env:DISCORD_SCHOOLSWP_ROUTINES_URL
}
if (-not $N8nWebhookUrl -and $env:N8N_HYPERFRAMES_WATCHER_URL) {
    $N8nWebhookUrl = $env:N8N_HYPERFRAMES_WATCHER_URL
}

# Resolution baseline
$Baseline = @{
    sha = ""
    date = ""
    set_at = ""
}
if (-not $BaselineFile) {
    $BaselineFile = Join-Path $PSScriptRoot ".baseline.json"
}
if (Test-Path $BaselineFile) {
    $baselineData = Get-Content $BaselineFile -Raw | ConvertFrom-Json
    $Baseline.sha = $baselineData.sha
    $Baseline.date = $baselineData.date
    $Baseline.set_at = $baselineData.set_at
}

Write-Host "=== HyperFrames launch watcher - $DateRun ==="
Write-Host "Repo : $Repo"
Write-Host "Path : $Path"
Write-Host "Baseline SHA : $($Baseline.sha) (set $($Baseline.set_at))"

# 1. Appel API GitHub : dernier commit touchant le path
$headers = @{
    "User-Agent" = "schoolswp-hyperframes-watcher"
    "Accept"     = "application/vnd.github+json"
}
if ($GithubToken) {
    $headers["Authorization"] = "Bearer $GithubToken"
}

$encodedPath = [uri]::EscapeDataString($Path)
$apiUrl = "https://api.github.com/repos/$Repo/commits?path=$encodedPath&per_page=1"

$commit = $null
try {
    $resp = Invoke-RestMethod -Uri $apiUrl -Headers $headers -Method Get
    if ($resp -and $resp.Count -gt 0) {
        $commit = $resp[0]
    }
} catch {
    Write-Error "Appel API GitHub echoue : $($_.Exception.Message)"
    exit 1
}

if (-not $commit) {
    Write-Error "Aucun commit trouve pour $Repo path $Path (path inexistant ou repo prive ?)"
    exit 1
}

# 2. Extraction des champs
$shaFull   = $commit.sha
$shaShort  = $shaFull.Substring(0, 12)
$commitMsg = ($commit.commit.message -split "`n")[0]
$author    = $commit.commit.author.name
$commitDate = $commit.commit.committer.date
$htmlUrl   = $commit.html_url

# 3. Detection changement
$changed = ($shaShort -ne $Baseline.sha)

# 4. Rapport
$report = "# HyperFrames launch watcher - $DateRun" + [char]10 + [char]10
$report += "- **Repo** : $Repo" + [char]10
$report += "- **Path** : $Path" + [char]10
$report += "- **Dernier commit SHA** : $shaShort" + [char]10
$report += "- **Date commit** : $commitDate" + [char]10
$report += "- **Auteur** : $author" + [char]10
$report += "- **Message** : $commitMsg" + [char]10
$report += "- **Baseline SHA** : $($Baseline.sha) (set $($Baseline.set_at))" + [char]10
$report += "- **Nouveau commit detecte** : $changed" + [char]10 + [char]10

if ($changed) {
    $report += "## Nouveau commit detecte sur $Path." + [char]10 + [char]10
    $report += "Lien : $htmlUrl" + [char]10
    $report += "Action : verifier le contenu. Mettre a jour .baseline.json (sha + date) une fois pris en compte." + [char]10
} else {
    $report += "Pas de changement. Dernier commit toujours $shaShort." + [char]10
}

Write-Host ""
Write-Host $report

if ($ReportFile) {
    Set-Content -Path $ReportFile -Value $report -Encoding UTF8
    Write-Host "Rapport ecrit : $ReportFile"
}

# 5. Discord webhook si fourni ET nouveau commit
if ($WebhookUrl -and $changed) {
    $discordMsg = ":satellite: **Nouveau commit hyperframes-launches** - $DateRun" + [char]10 + [char]10
    $discordMsg += "Path : ``$Path``" + [char]10
    $discordMsg += "SHA : ``$shaShort`` ($commitDate)" + [char]10
    $discordMsg += "Auteur : $author" + [char]10
    $discordMsg += "Message : $commitMsg" + [char]10
    $discordMsg += [char]10 + $htmlUrl

    $payload = @{ content = $discordMsg } | ConvertTo-Json -Compress
    try {
        Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body $payload -ContentType "application/json"
        Write-Host "Discord webhook : POST OK"
    } catch {
        Write-Warning "Discord webhook : echec POST - $_"
    }
}

# 6. n8n webhook si fourni (structure complete pour orchestration)
if ($N8nWebhookUrl) {
    $n8nPayload = @{
        date          = $DateRun
        source        = "hyperframes-launch-watcher"
        repo          = $Repo
        path          = $Path
        sha_current   = $shaShort
        sha_baseline  = $Baseline.sha
        commit_date   = $commitDate
        author        = $author
        message       = $commitMsg
        html_url      = $htmlUrl
        changed       = $changed
    } | ConvertTo-Json -Depth 5 -Compress

    try {
        Invoke-RestMethod -Uri $N8nWebhookUrl -Method Post -Body $n8nPayload -ContentType "application/json" | Out-Null
        Write-Host "n8n webhook : POST OK"
    } catch {
        Write-Warning "n8n webhook : echec POST - $_"
    }
}

# Exit codes : 0 si pas de changement, 2 si nouveau commit detecte
if ($changed) { exit 2 }
exit 0

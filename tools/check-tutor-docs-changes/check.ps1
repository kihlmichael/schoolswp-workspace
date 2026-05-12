# Tutor LMS docs change watcher
# Compare le content_hash actuel des pages docs.themeum.com avec le hash baseline du vault.
# Output : rapport Markdown + POST Discord webhook optionnel si changements detectes.
#
# Usage local :
#   .\check.ps1 -VaultDocsDir "D:\path\to\vault\tutor-lms\docs"      # path obligatoire si pas dans env
#   .\check.ps1 -Limit 5                                              # test rapide sur 5 fichiers
#   .\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..."   # POST si changement
#   .\check.ps1 -ReportFile "report.md"                               # ecrit le rapport dans un fichier
#
# Path vault par defaut lu depuis env var VAULT_TUTOR_DOCS_DIR (evite emojis dans le code).
#
# Pre-requis : defuddle CLI installe global (npm), acces lecture vault.

param(
    [Parameter(Mandatory=$false)]
    [int]$Limit = 0,

    [Parameter(Mandatory=$false)]
    [string]$WebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$N8nWebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$ReportFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$VaultDocsDir = $null
)

$ErrorActionPreference = "Stop"
$DateRun = (Get-Date -Format "yyyy-MM-dd HH:mm")

# Resolution path vault
if (-not $VaultDocsDir) {
    $VaultDocsDir = $env:VAULT_TUTOR_DOCS_DIR
}
if (-not $VaultDocsDir) {
    Write-Error "VaultDocsDir requis : passer en parametre OU definir env var VAULT_TUTOR_DOCS_DIR. Path attendu vers le dossier docs/ du plugin tutor-lms dans le vault Obsidian."
    exit 1
}
if (-not (Test-Path $VaultDocsDir)) {
    Write-Error "Vault docs dir introuvable : $VaultDocsDir"
    exit 1
}

function Get-FrontmatterField {
    param([string]$Content, [string]$Field)
    $pattern = "(?m)^${Field}:\s*(.+)$"
    $match = [regex]::Match($Content, $pattern)
    if ($match.Success) { return $match.Groups[1].Value.Trim().Trim('"') }
    return $null
}

function Get-ContentHash {
    param([string]$Content)
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Content)
    $hash = [System.Security.Cryptography.MD5]::Create().ComputeHash($bytes)
    return ([BitConverter]::ToString($hash) -replace '-', '').Substring(0, 10).ToLower()
}

# Replication exacte de la logique scrape-themeum-docs.ps1 v3 pour hash comparable
function Test-IsIndexPage {
    param([string]$Content)
    $svgPattern = '^\!\[\]\(https?://[^\)]*tutor-1\.svg\)'
    if ($Content -match $svgPattern) { return $true }
    $linkPattern = '\[[^\]]+\]\(https?://'
    $linksCount = ([regex]::Matches($Content, $linkPattern)).Count
    if ($linksCount -ge 20 -and ($linksCount * 60) -gt $Content.Length) { return $true }
    return $false
}

# 1. Lecture du vault : extraire (url, content_hash, is_index_page) pour tous les .md
Write-Host "=== Lecture vault docs ==="
Write-Host "Path : $VaultDocsDir"
$vaultEntries = @()
$files = Get-ChildItem $VaultDocsDir -Filter "*.md"
foreach ($f in $files) {
    $head = (Get-Content $f.FullName -TotalCount 25) -join "`n"
    $url = Get-FrontmatterField -Content $head -Field "url"
    $hash = Get-FrontmatterField -Content $head -Field "content_hash"
    $isIdx = Get-FrontmatterField -Content $head -Field "is_index_page"

    if ($url -and $hash) {
        $vaultEntries += [PSCustomObject]@{
            File = $f.Name
            Url = $url
            VaultHash = $hash
            IsIndex = ($isIdx -eq "true")
        }
    }
}

# Filtre : on watch que les pages content (skip stubs)
$toCheck = $vaultEntries | Where-Object { -not $_.IsIndex }
Write-Host "Vault total : $($vaultEntries.Count) fichiers"
Write-Host "Watch list (non-stub) : $($toCheck.Count) fichiers"

if ($Limit -gt 0) {
    $toCheck = $toCheck | Select-Object -First $Limit
    Write-Host "Limit applique : $($toCheck.Count) fichiers"
}
Write-Host ""

# 2. Re-fetch + recompute hash + compare
Write-Host "=== Verification des pages ==="
$results = @()
$errors = 0
$idx = 0
foreach ($entry in $toCheck) {
    $idx++
    Write-Host "[$idx/$($toCheck.Count)] $($entry.Url)"

    try {
        $tmpFile = [System.IO.Path]::GetTempFileName() + ".md"
        & defuddle parse $entry.Url -m -o $tmpFile 2>$null | Out-Null

        if (-not (Test-Path $tmpFile)) {
            Write-Warning "  Echec scrape"
            $errors++
            continue
        }

        $content = Get-Content $tmpFile -Raw -Encoding UTF8
        Remove-Item $tmpFile -Force

        if ([string]::IsNullOrWhiteSpace($content)) {
            Write-Warning "  Content vide"
            $errors++
            continue
        }

        # Replication is_index detection
        if (Test-IsIndexPage -Content $content) {
            $stub = "Cette page est l'index de la section. Le contenu reel est reparti dans les sous-pages enfants." + [char]10 + [char]10 + "Voir l'arborescence dans le menu source : <" + $entry.Url + ">" + [char]10 + [char]10 + "Les sous-pages sont scrapees individuellement (voir index-documentation.md pour la liste complete)." + [char]10
            $content = $stub
        }

        $newHash = Get-ContentHash -Content $content
        $changed = ($newHash -ne $entry.VaultHash)

        $results += [PSCustomObject]@{
            File = $entry.File
            Url = $entry.Url
            VaultHash = $entry.VaultHash
            NewHash = $newHash
            Changed = $changed
        }

        if ($changed) {
            Write-Host "  CHANGE detecte : $($entry.VaultHash) -> $newHash" -ForegroundColor Yellow
        }
    } catch {
        Write-Warning "  Erreur : $_"
        $errors++
    }
}

# 3. Rapport Markdown
$changedItems = $results | Where-Object { $_.Changed }
$report = "# Tutor LMS docs change watcher - $DateRun" + [char]10 + [char]10
$report += "- **Pages verifiees** : $($results.Count) / $($toCheck.Count)" + [char]10
$report += "- **Erreurs scrape** : $errors" + [char]10
$report += "- **Changements detectes** : $($changedItems.Count)" + [char]10 + [char]10

if ($changedItems.Count -gt 0) {
    $report += "## Pages modifiees" + [char]10 + [char]10
    $report += "| Fichier vault | URL | Vault hash | New hash |" + [char]10
    $report += "|---|---|---|---|" + [char]10
    foreach ($c in $changedItems) {
        $report += "| $($c.File) | $($c.Url) | $($c.VaultHash) | $($c.NewHash) |" + [char]10
    }
    $report += [char]10 + "**Action recommandee** : re-scrape ces pages via scrape-themeum-docs.ps1 pour produire un nouveau outbox transport." + [char]10
} else {
    $report += "Aucun changement detecte. Le corpus vault Tutor LMS est a jour." + [char]10
}

Write-Host ""
Write-Host "=== Rapport ==="
Write-Host $report

if ($ReportFile) {
    Set-Content -Path $ReportFile -Value $report -Encoding UTF8
    Write-Host "Rapport ecrit : $ReportFile"
}

# 4. Discord webhook si fourni ET changements detectes
if ($WebhookUrl -and $changedItems.Count -gt 0) {
    $discordMsg = ":warning: **Tutor LMS docs change watcher** - $($changedItems.Count) page(s) modifiee(s) detectee(s) le $DateRun." + [char]10 + [char]10
    foreach ($c in $changedItems | Select-Object -First 5) {
        $discordMsg += "- $($c.Url)" + [char]10
    }
    if ($changedItems.Count -gt 5) {
        $discordMsg += "- ... et $($changedItems.Count - 5) autre(s)" + [char]10
    }
    $discordMsg += [char]10 + "Voir le rapport complet pour la liste exhaustive."

    $payload = @{ content = $discordMsg } | ConvertTo-Json -Compress
    try {
        Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body $payload -ContentType "application/json"
        Write-Host "Discord webhook : POST OK"
    } catch {
        Write-Warning "Discord webhook : echec POST - $_"
    }
}

# 5. n8n webhook si fourni (POST JSON structure complete pour orchestration)
if ($N8nWebhookUrl) {
    $changedArray = @()
    foreach ($c in $changedItems) {
        $changedArray += @{
            file = $c.File
            url = $c.Url
            old_hash = $c.VaultHash
            new_hash = $c.NewHash
        }
    }

    $n8nPayload = @{
        date = $DateRun
        source = "tutor-lms-docs-watcher"
        checked = $results.Count
        errors = $errors
        changes_count = $changedItems.Count
        changed_pages = $changedArray
    } | ConvertTo-Json -Depth 5 -Compress

    try {
        Invoke-RestMethod -Uri $N8nWebhookUrl -Method Post -Body $n8nPayload -ContentType "application/json" | Out-Null
        Write-Host "n8n webhook : POST OK"
    } catch {
        Write-Warning "n8n webhook : echec POST - $_"
    }
}

# Exit code : 0 si OK, 1 si erreurs scrape, 2 si changements detectes (utile pour cron)
if ($errors -gt 0) { exit 1 }
if ($changedItems.Count -gt 0) { exit 2 }
exit 0

# FluentCart Checkout Login watcher
# Surveille le repo public PineDigitalCo/fluentcart-checkout-login (mini-plugin
# communautaire "vibe-coded" qui ajoute un login dans le checkout FluentCart).
# Detecte : nouveaux commits, modif du ZIP, sources hors ZIP, releases, modif README,
# changement de version, changelog, issues/PR, changements PHP/JS/CSS, et mentions
# login/checkout/REST/securite/compatibilite dans les messages de commit.
#
# Output : snapshot baseline JSON + rapport Markdown (6 sections) + POST Discord/n8n
#          si changement significatif. Historique append-only.
#
# Usage :
#   .\check.ps1                                   # check, compare a la baseline
#   .\check.ps1 -ReportFile "reports\latest.md"   # ecrit le rapport
#   .\check.ps1 -DeepScan                          # telecharge le ZIP + audit code automatique
#   .\check.ps1 -UpdateBaseline                    # fige l'etat courant comme nouvelle baseline
#   .\check.ps1 -Init                              # (re)capture la baseline sans diff
#
# Pre-requis : acces reseau a api.github.com. Aucun clone local requis.
#
# Note securite : ce script ne lit JAMAIS GITHUB_TOKEN depuis l'environnement
# (cf. memoire feedback_github_token_env_override : la var ecrase le keyring gh).
# L'API publique non authentifiee (60 req/h) suffit pour un poll hebdo. Pour plus
# de marge de rate-limit, passer un token explicite via -GithubToken.
# Compatible PowerShell 5.1 (Task Scheduler) et 7+.

param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "PineDigitalCo/fluentcart-checkout-login",

    [Parameter(Mandatory=$false)]
    [string]$WebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$N8nWebhookUrl = $null,

    [Parameter(Mandatory=$false)]
    [string]$ReportFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$BaselineFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$HistoryFile = $null,

    [Parameter(Mandatory=$false)]
    [string]$GithubToken = $null,

    [Parameter(Mandatory=$false)]
    [switch]$DeepScan,

    [Parameter(Mandatory=$false)]
    [switch]$UpdateBaseline,

    [Parameter(Mandatory=$false)]
    [switch]$Init
)

$ErrorActionPreference = "Stop"
$DateRun = (Get-Date -Format "yyyy-MM-dd HH:mm")
$Today   = (Get-Date -Format "yyyy-MM-dd")
$NL = [char]10

# Fallback env var pour les webhooks (jamais GITHUB_TOKEN, voir entete)
if (-not $WebhookUrl -and $env:DISCORD_SCHOOLSWP_ROUTINES_URL) {
    $WebhookUrl = $env:DISCORD_SCHOOLSWP_ROUTINES_URL
}
if (-not $N8nWebhookUrl -and $env:N8N_FLUENTCART_CHECKOUT_LOGIN_WATCHER_URL) {
    $N8nWebhookUrl = $env:N8N_FLUENTCART_CHECKOUT_LOGIN_WATCHER_URL
}

if (-not $BaselineFile) { $BaselineFile = Join-Path $PSScriptRoot ".baseline.json" }
if (-not $HistoryFile)  { $HistoryFile  = Join-Path $PSScriptRoot "history.md" }

# ----------------------------------------------------------------------------
# Helper appel API GitHub
# ----------------------------------------------------------------------------
$ghHeaders = @{
    "User-Agent" = "schoolswp-fct-checkout-login-watcher"
    "Accept"     = "application/vnd.github+json"
}
if ($GithubToken) { $ghHeaders["Authorization"] = "Bearer $GithubToken" }

function Invoke-GH($url) {
    try {
        return Invoke-RestMethod -Uri $url -Headers $ghHeaders -Method Get
    } catch {
        Write-Warning "API GitHub : echec sur $url -> $($_.Exception.Message)"
        return $null
    }
}

function Get-RawFile($branch, $path) {
    $u = "https://raw.githubusercontent.com/$Repo/$branch/$path"
    try {
        return Invoke-RestMethod -Uri $u -Headers @{ "User-Agent" = $ghHeaders["User-Agent"] } -Method Get
    } catch {
        return $null
    }
}

Write-Host "=== FluentCart Checkout Login watcher - $DateRun ==="
Write-Host "Repo : $Repo"

# ----------------------------------------------------------------------------
# 1. Fetch etat courant
# ----------------------------------------------------------------------------
$repoInfo = Invoke-GH "https://api.github.com/repos/$Repo"
if (-not $repoInfo) {
    Write-Error "Impossible de lire les infos du repo (prive, renomme, ou rate-limit ?)."
    exit 1
}
$branch = $repoInfo.default_branch

$treeResp = Invoke-GH "https://api.github.com/repos/$Repo/git/trees/$branch`?recursive=1"
if (-not $treeResp) {
    Write-Error "Impossible de lire l'arbre des fichiers."
    exit 1
}

$commits  = Invoke-GH "https://api.github.com/repos/$Repo/commits?per_page=20"
$releases = Invoke-GH "https://api.github.com/repos/$Repo/releases"
$issues   = Invoke-GH "https://api.github.com/repos/$Repo/issues?state=all&per_page=30"

# --- Tree : map path -> sha + resume types ---
$tree = [ordered]@{}
$summary = @{ php = 0; js = 0; css = 0; zip = @(); total = 0 }
$readmePath = $null
$hasChangelog = $false
$hasLicenseFile = $false
foreach ($node in $treeResp.tree) {
    if ($node.type -ne "blob") { continue }
    $p = $node.path
    $tree[$p] = $node.sha
    $summary.total++
    $lower = $p.ToLower()
    if ($lower -match '\.php$')  { $summary.php++ }
    if ($lower -match '\.js$')   { $summary.js++ }
    if ($lower -match '\.css$')  { $summary.css++ }
    if ($lower -match '\.zip$')  { $summary.zip += $p }
    if ($lower -match '(^|/)readme\.txt$' -or $lower -match '(^|/)readme\.md$') { if (-not $readmePath) { $readmePath = $p } }
    if ($lower -match 'changelog') { $hasChangelog = $true }
    if ($lower -match '(^|/)license' -or $lower -match '(^|/)licence') { $hasLicenseFile = $true }
}
# Source hors ZIP = au moins un .php/.js/.css trace directement dans le repo (pas dans un ZIP)
$summary.source_outside_zip = (($summary.php + $summary.js + $summary.css) -gt 0)

# --- Version depuis le readme (Stable tag) ---
$versionReadme = $null
if ($readmePath) {
    $readmeRaw = Get-RawFile $branch $readmePath
    if ($readmeRaw) {
        $m = [regex]::Match($readmeRaw, '(?im)^\s*Stable tag:\s*(.+?)\s*$')
        if ($m.Success) { $versionReadme = $m.Groups[1].Value.Trim() }
    }
}

# --- Commits ---
$latestCommit = $null
if ($commits -and $commits.Count -gt 0) {
    $c = $commits[0]
    $latestCommit = [ordered]@{
        sha     = $c.sha
        date    = $c.commit.committer.date
        message = ($c.commit.message -split "`n")[0]
    }
}

# --- Releases / issues ---
$releaseCount = 0; $latestRelease = $null
if ($releases) { $releaseCount = $releases.Count; if ($releaseCount -gt 0) { $latestRelease = $releases[0].tag_name } }
$openIssuePr = $repoInfo.open_issues_count   # GitHub compte issues + PR ouvertes

# --- Snapshot courant ---
$readmeSha = $null
if ($readmePath -and $tree.Contains($readmePath)) { $readmeSha = $tree[$readmePath] }

$cur = [ordered]@{
    repo                 = $Repo
    set_at               = $Today
    default_branch       = $branch
    pushed_at            = $repoInfo.pushed_at
    latest_commit        = $latestCommit
    release_count        = $releaseCount
    latest_release       = $latestRelease
    open_issues_pr_count = $openIssuePr
    readme_path          = $readmePath
    readme_sha           = $readmeSha
    version_readme        = $versionReadme
    has_changelog        = $hasChangelog
    has_license_file     = $hasLicenseFile
    tree                 = $tree
    tree_summary         = $summary
}

# ----------------------------------------------------------------------------
# 2. Mode Init / premiere execution : capture baseline, pas de diff
# ----------------------------------------------------------------------------
$baselineExists = Test-Path $BaselineFile
if ($Init -or -not $baselineExists) {
    $cur.set_by = "Init/premiere execution"
    $cur | ConvertTo-Json -Depth 12 | Set-Content -Path $BaselineFile -Encoding UTF8
    Write-Host "Baseline capturee : $BaselineFile"
    Write-Host "  version_readme=$versionReadme  latest_commit=$($latestCommit.sha.Substring(0,10))  fichiers=$($summary.total)"
    if ($ReportFile) {
        $initR = "# FluentCart Checkout Login watcher - $DateRun$NL$NL"
        $initR += "Baseline initialisee. Aucun diff lors de cette execution.$NL$NL"
        $initR += "- Repo : $Repo$NL- Version readme : $versionReadme$NL- Dernier commit : $($latestCommit.sha.Substring(0,10)) ($($latestCommit.date))$NL- Fichiers traces : $($summary.total)$NL"
        $dir = Split-Path $ReportFile -Parent
        if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
        Set-Content -Path $ReportFile -Value $initR -Encoding UTF8
        Write-Host "Rapport initial ecrit : $ReportFile"
    }
    exit 0
}

# ----------------------------------------------------------------------------
# 3. Diff contre la baseline
# ----------------------------------------------------------------------------
$base = Get-Content $BaselineFile -Raw | ConvertFrom-Json
Write-Host "Baseline : version_readme=$($base.version_readme)  commit=$($base.latest_commit.sha.Substring(0,10))  (set $($base.set_at))"

$changes = New-Object System.Collections.Generic.List[string]
$flags   = New-Object System.Collections.Generic.List[string]   # categories pour scoring/keywords

# 3a. Commit
$newCommit = ($latestCommit -and $latestCommit.sha -ne $base.latest_commit.sha)
if ($newCommit) {
    $changes.Add("Nouveau commit HEAD : $($base.latest_commit.sha.Substring(0,10)) -> $($latestCommit.sha.Substring(0,10)) ($($latestCommit.message))")
    $flags.Add("commit")
}

# 3b. pushed_at (push sans changement de HEAD = branche/tag)
if ($repoInfo.pushed_at -ne $base.pushed_at -and -not $newCommit) {
    $changes.Add("Activite de push detectee (pushed_at change) sans changement de HEAD : branche ou tag pousse ?")
    $flags.Add("push")
}

# 3c. Releases
if ($releaseCount -ne $base.release_count) {
    $changes.Add("Releases : $($base.release_count) -> $releaseCount (derniere : $latestRelease)")
    $flags.Add("release")
}

# 3d. Version readme
if ($versionReadme -ne $base.version_readme) {
    $changes.Add("Version readme (Stable tag) : $($base.version_readme) -> $versionReadme")
    $flags.Add("version")
}

# 3e. README
if ($readmeSha -ne $base.readme_sha) {
    $changes.Add("README modifie ($($base.readme_path) -> $readmePath, sha change)")
    $flags.Add("readme")
}

# 3f. Changelog apparu
if ($hasChangelog -and -not $base.has_changelog) {
    $changes.Add("Un changelog est apparu dans le repo")
    $flags.Add("changelog")
}

# 3g. Issues / PR
if ($openIssuePr -ne $base.open_issues_pr_count) {
    $changes.Add("Issues/PR ouvertes : $($base.open_issues_pr_count) -> $openIssuePr")
    $flags.Add("issues")
}

# 3h. Diff de l'arbre des fichiers (ajouts / suppressions / modifs)
$baseTree = @{}
foreach ($prop in $base.tree.PSObject.Properties) { $baseTree[$prop.Name] = $prop.Value }
$added = @(); $removed = @(); $modified = @()
foreach ($k in $tree.Keys) {
    if (-not $baseTree.ContainsKey($k)) { $added += $k }
    elseif ($baseTree[$k] -ne $tree[$k]) { $modified += $k }
}
foreach ($k in $baseTree.Keys) { if (-not $tree.Contains($k)) { $removed += $k } }

if ($added.Count -gt 0)    { $changes.Add("Fichiers ajoutes : $($added -join ', ')"); $flags.Add("files_added") }
if ($removed.Count -gt 0)  { $changes.Add("Fichiers supprimes : $($removed -join ', ')"); $flags.Add("files_removed") }
if ($modified.Count -gt 0) { $changes.Add("Fichiers modifies : $($modified -join ', ')"); $flags.Add("files_modified") }

# Sources hors ZIP apparues
if ($summary.source_outside_zip -and -not $base.tree_summary.source_outside_zip) {
    $changes.Add("Des fichiers source (PHP/JS/CSS) apparaissent maintenant HORS du ZIP")
    $flags.Add("source_outside_zip")
}
# ZIP touche
$zipTouched = @($added + $modified + $removed) | Where-Object { $_ -match '\.zip$' }
if ($zipTouched.Count -gt 0) { $flags.Add("zip") }

# 3i. Scan mots-cles sur les messages des nouveaux commits
$kwMap = [ordered]@{
    "login"         = 'login|connexion|sign[- ]?in'
    "checkout"      = 'checkout'
    "rest_api"      = 'rest|api|endpoint|nonce'
    "securite"      = 'secur|vuln|xss|csrf|sanitiz|escap|injection|nonce'
    "compatibilite" = 'compat|fluentcart|fluent cart|breaking|deprecat'
    "fix"           = '\bfix|bug|hotfix|patch'
}
$newMessages = New-Object System.Collections.Generic.List[string]
if ($commits) {
    foreach ($c in $commits) {
        if ($c.sha -eq $base.latest_commit.sha) { break }
        $newMessages.Add(($c.commit.message -split "`n")[0])
    }
}
$kwHits = [ordered]@{}
$allNewMsg = ($newMessages -join " " ).ToLower()
foreach ($kw in $kwMap.Keys) {
    if ($allNewMsg -match $kwMap[$kw]) { $kwHits[$kw] = $true; $flags.Add("kw:$kw") }
}

$hasChanges = ($changes.Count -gt 0)

# ----------------------------------------------------------------------------
# 4. Deep scan optionnel : telecharge le ZIP + audit code automatique
# ----------------------------------------------------------------------------
$deepReport = $null
if ($DeepScan) {
    $deepReport = New-Object System.Collections.Generic.List[string]
    $deepReport.Add("## Audit technique automatique (deep scan)")
    $deepReport.Add("")
    $tmp = Join-Path $env:TEMP ("fct-watcher-deepscan-" + ([guid]::NewGuid().ToString("N").Substring(0,8)))
    New-Item -ItemType Directory -Path $tmp -Force | Out-Null
    try {
        # localise le(s) ZIP(s) dans l'arbre
        $zipPaths = @($tree.Keys | Where-Object { $_ -match '\.zip$' })
        $srcFiles = @()
        foreach ($zp in $zipPaths) {
            $zipLocal = Join-Path $tmp ("pkg-" + ([IO.Path]::GetFileName($zp)))
            $zurl = "https://raw.githubusercontent.com/$Repo/$branch/$zp"
            Invoke-WebRequest -Uri $zurl -Headers @{ "User-Agent" = $ghHeaders["User-Agent"] } -OutFile $zipLocal
            $ex = Join-Path $tmp ("ex-" + ([IO.Path]::GetFileNameWithoutExtension($zp)))
            Expand-Archive -Path $zipLocal -DestinationPath $ex -Force
            $srcFiles += Get-ChildItem $ex -Recurse -File | Where-Object { $_.Extension -match '\.(php|js|css)$' }
            $deepReport.Add("ZIP ``$zp`` extrait : $((Get-ChildItem $ex -Recurse -File).Count) fichiers.")
        }
        # sources tracees hors ZIP
        foreach ($k in $tree.Keys) {
            if ($k -match '\.(php|js)$') {
                $raw = Get-RawFile $branch $k
                if ($raw) {
                    $f = Join-Path $tmp ($k -replace '[\\/]', '_')
                    Set-Content -Path $f -Value $raw -Encoding UTF8
                    $srcFiles += Get-Item $f
                }
            }
        }
        $deepReport.Add("")

        # patterns dangereux PHP/JS
        $dangerPatterns = @(
            'eval\s*\(', 'base64_decode\s*\(', 'shell_exec\s*\(', '\bexec\s*\(',
            '\bsystem\s*\(', 'passthru\s*\(', 'popen\s*\(', 'proc_open\s*\(',
            'file_put_contents\s*\(', '\bfwrite\s*\(', '\bfopen\s*\(', 'curl_exec\s*\(',
            'wp_remote_(get|post|request)\s*\(', 'create_function\s*\(', 'assert\s*\(',
            'new\s+Function\s*\(', 'document\.write', '\.innerHTML\s*=', '\batob\s*\('
        )
        $danger = New-Object System.Collections.Generic.List[string]
        $externalUrls = New-Object System.Collections.Generic.List[string]
        foreach ($sf in ($srcFiles | Sort-Object FullName -Unique)) {
            $content = Get-Content $sf.FullName -Raw
            foreach ($pat in $dangerPatterns) {
                $mm = [regex]::Matches($content, $pat)
                if ($mm.Count -gt 0) { $danger.Add("$($sf.Name) : motif ``$pat`` x$($mm.Count)") }
            }
            foreach ($um in [regex]::Matches($content, 'https?://[^\s"''`)]+')) {
                $u = $um.Value
                if ($u -notmatch 'gnu\.org|w3\.org|schema\.org|wordpress\.org') { $externalUrls.Add("$($sf.Name) : $u") }
            }
        }

        # marqueurs de couplage FluentCart
        $allSrc = ""
        foreach ($sf in ($srcFiles | Sort-Object FullName -Unique)) { $allSrc += (Get-Content $sf.FullName -Raw) + "`n" }
        $coupling = [ordered]@{
            "window.fluentcart_checkout_info" = ($allSrc -match 'fluentcart_checkout_info')
            "handle JS fct-checkout"          = ($allSrc -match "fct-checkout")
            "endpoint REST /user/login"       = ($allSrc -match '/user/login')
            "header X-WP-Nonce"               = ($allSrc -match 'X-WP-Nonce')
        }
        $escCount = ([regex]::Matches($allSrc, 'esc_(html|attr|url)')).Count

        $deepReport.Add("**Fonctions dangereuses (eval/base64_decode/shell_exec/ecriture fichier/appel externe) :**")
        if ($danger.Count -eq 0) { $deepReport.Add("- Aucune detectee.") } else { foreach ($d in $danger) { $deepReport.Add("- $d") } }
        $deepReport.Add("")
        $deepReport.Add("**URLs externes en dur :**")
        if ($externalUrls.Count -eq 0) { $deepReport.Add("- Aucune.") } else { foreach ($u in $externalUrls) { $deepReport.Add("- $u") } }
        $deepReport.Add("")
        $deepReport.Add("**Marqueurs de couplage FluentCart :**")
        foreach ($k in $coupling.Keys) { $deepReport.Add("- $k : $($coupling[$k])") }
        $deepReport.Add("")
        $deepReport.Add("**Echappement PHP (occurrences esc_html/esc_attr/esc_url) :** $escCount")
        if ($danger.Count -gt 0) { $flags.Add("danger_code") }
    } catch {
        $deepReport.Add("Deep scan en echec : $($_.Exception.Message)")
    } finally {
        if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
    }
}

# ----------------------------------------------------------------------------
# 5. Scoring du risque + recommandation
# ----------------------------------------------------------------------------
$risk = "faible"
$reco = "continuer a surveiller"

if ($flags -contains "danger_code" -or $flags -contains "kw:securite") {
    $risk = "eleve"; $reco = "auditer"
} elseif ($flags -contains "source_outside_zip" -or $flags -contains "zip" -or $flags -contains "files_modified" -or $flags -contains "kw:rest_api") {
    $risk = "moyen"; $reco = "auditer"
} elseif ($flags -contains "release" -or $flags -contains "version" -or $flags -contains "changelog") {
    $risk = "moyen"; $reco = "tester en staging"
} elseif ($flags -contains "commit" -or $flags -contains "files_added") {
    $risk = "faible-a-moyen"; $reco = "tester en staging"
} elseif (-not $hasChanges) {
    $risk = "nul"; $reco = "ignorer"
}

# ----------------------------------------------------------------------------
# 6. Rapport Markdown
# ----------------------------------------------------------------------------
$R = New-Object System.Collections.Generic.List[string]
$R.Add("# FluentCart Checkout Login watcher - $DateRun")
$R.Add("")
$R.Add("- **Repo** : $Repo")
$R.Add("- **Dernier commit** : $($latestCommit.sha.Substring(0,10)) - $($latestCommit.message) ($($latestCommit.date))")
$R.Add("- **Version readme** : $versionReadme (baseline : $($base.version_readme))")
$R.Add("- **Releases** : $releaseCount  |  **Issues/PR ouvertes** : $openIssuePr  |  **Fichiers** : $($summary.total)")
$R.Add("- **Changement detecte** : $hasChanges")
$R.Add("")

if (-not $hasChanges) {
    $R.Add("Aucun changement depuis la baseline ($($base.set_at)). Repo stable.")
} else {
    # 1. Ce qui a change
    $R.Add("## 1. Ce qui a change")
    $R.Add("")
    foreach ($ch in $changes) { $R.Add("- $ch") }
    if ($newMessages.Count -gt 0) {
        $R.Add("")
        $R.Add("Nouveaux messages de commit :")
        foreach ($m in $newMessages) { $R.Add("  - $m") }
    }
    if ($kwHits.Keys.Count -gt 0) {
        $R.Add("")
        $R.Add("Mots-cles detectes dans les commits : " + (($kwHits.Keys) -join ", "))
    }
    $R.Add("")

    # 2. Pourquoi c'est important
    $R.Add("## 2. Pourquoi c'est important")
    $R.Add("")
    if ($flags -contains "release")            { $R.Add("- Premiere release / nouvelle release : signal de maturite (versionnage, distribution propre hors ZIP brut).") }
    if ($flags -contains "version")            { $R.Add("- La version a bouge : nouvelle iteration du plugin, a re-tester.") }
    if ($flags -contains "source_outside_zip") { $R.Add("- Les sources sortent du ZIP : le code devient lisible/auditable directement sur GitHub (gros plus pour la revue).") }
    if ($flags -contains "zip")                { $R.Add("- Le ZIP a change : le binaire distribue a ete remplace, contenu a re-inspecter.") }
    if ($flags -contains "changelog")          { $R.Add("- Apparition d'un changelog : meilleure tracabilite des evolutions.") }
    if ($flags -contains "kw:securite")        { $R.Add("- Un commit mentionne la securite : potentiellement un correctif ou une faille, prioritaire.") }
    if ($flags -contains "kw:rest_api")        { $R.Add("- Un commit touche l'API REST / le nonce : coeur du mecanisme de login, risque de regression.") }
    if ($flags -contains "issues")             { $R.Add("- Mouvement sur les issues/PR : retours communautaires ou contributions, indicateur d'activite et de fiabilite.") }
    if ($changes.Count -gt 0 -and ($R[$R.Count-1] -eq "## 2. Pourquoi c'est important" -or $R[$R.Count-1] -eq "")) { $R.Add("- Activite sur un repo jusqu'ici fige : le plugin evolue, re-evaluer sa maturite.") }
    $R.Add("")

    # 3. Impact potentiel FluentCart
    $R.Add("## 3. Impact potentiel sur FluentCart")
    $R.Add("")
    $R.Add("- Si le code a change, revalider les points de couplage : dependance a ``window.fluentcart_checkout_info`` (rest.url + rest.nonce), handle JS ``fct-checkout``, action ``fluent_cart/before_checkout_page_start``, endpoint ``{rest.url}/user/login``.")
    $R.Add("- Verifier la conservation du panier apres reload (le plugin fait window.location.reload, la persistance du panier reste a la charge de FluentCart).")
    $R.Add("- Verifier l'absence de conflit DOM avec le checkout (le plugin rend hors du root [data-fluent-cart-checkout-page] et evite les classes fct_*).")
    $R.Add("")

    # 4. Impact potentiel schoolsWP
    $R.Add("## 4. Impact potentiel pour schoolsWP")
    $R.Add("")
    $R.Add("- FluentCart est dans la stack (checkout formations). Un login invite fiable sur le checkout reduit les frictions de commande pour les clients existants.")
    $R.Add("- Angle editorial : sujet concret 'combler un manque de FluentCart', interessant pour un article/tutoriel si le plugin devient fiable.")
    $R.Add("- Tant que maturite faible : usage staging uniquement, jamais en production sans audit.")
    $R.Add("")

    # 5. Niveau de risque
    $R.Add("## 5. Niveau de risque")
    $R.Add("")
    $R.Add("- **Risque evalue ce run** : $risk")
    $R.Add("- Rappel baseline : maturite 3/10, risque maintenance 7/10 (couplage fort aux internes FluentCart, vibe-coded, pas de tests/CI).")
    $R.Add("")

    # 6. Recommandation
    $R.Add("## 6. Recommandation")
    $R.Add("")
    $R.Add("**$($reco.ToUpper())**")
    $R.Add("")
    $R.Add("Options : ignorer | continuer a surveiller | tester en staging | auditer | integrer.")
    $R.Add("Ne jamais considerer ce plugin pret pour la production sans audit prealable.")
}

if ($deepReport) {
    $R.Add("")
    foreach ($l in $deepReport) { $R.Add($l) }
}

$report = ($R -join $NL) + $NL
Write-Host ""
Write-Host $report

if ($ReportFile) {
    $dir = Split-Path $ReportFile -Parent
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    Set-Content -Path $ReportFile -Value $report -Encoding UTF8
    Write-Host "Rapport ecrit : $ReportFile"
}

# ----------------------------------------------------------------------------
# 7. Historique append-only (si changement)
# ----------------------------------------------------------------------------
if ($hasChanges) {
    if (-not (Test-Path $HistoryFile)) {
        Set-Content -Path $HistoryFile -Value ("# Historique des changements - $Repo" + $NL) -Encoding UTF8
    }
    $entry = "$NL## $DateRun - risque $risk - reco $reco$NL"
    foreach ($ch in $changes) { $entry += "- $ch$NL" }
    Add-Content -Path $HistoryFile -Value $entry -Encoding UTF8
    Write-Host "Historique mis a jour : $HistoryFile"
}

# ----------------------------------------------------------------------------
# 8. Notifications Discord / n8n (si changement significatif)
# ----------------------------------------------------------------------------
if ($WebhookUrl -and $hasChanges) {
    $msg = ":satellite: **FluentCart Checkout Login - changement detecte** - $DateRun" + $NL
    $msg += "Repo : <https://github.com/$Repo>" + $NL
    $msg += "Risque : **$risk**  |  Reco : **$reco**" + $NL + $NL
    $n = 0
    foreach ($ch in $changes) { if ($n -lt 8) { $msg += "- $ch" + $NL; $n++ } }
    if ($changes.Count -gt 8) { $msg += "- (+$($changes.Count - 8) autres, voir rapport)" + $NL }
    if ($msg.Length -gt 1900) { $msg = $msg.Substring(0, 1900) + $NL + "[...]" }
    $payload = @{ content = $msg } | ConvertTo-Json -Compress
    try {
        Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body $payload -ContentType "application/json" | Out-Null
        Write-Host "Discord webhook : POST OK"
    } catch {
        Write-Warning "Discord webhook : echec POST - $_"
    }
}

if ($N8nWebhookUrl) {
    $n8nPayload = @{
        date                 = $DateRun
        source               = "fluentcart-checkout-login-watcher"
        repo                 = $Repo
        has_changes          = $hasChanges
        risk                 = $risk
        reco                 = $reco
        flags                = @($flags)
        changes              = @($changes)
        version_readme       = $versionReadme
        version_baseline     = $base.version_readme
        latest_commit_sha    = $latestCommit.sha
        release_count        = $releaseCount
        open_issues_pr_count = $openIssuePr
    } | ConvertTo-Json -Depth 6 -Compress
    try {
        Invoke-RestMethod -Uri $N8nWebhookUrl -Method Post -Body $n8nPayload -ContentType "application/json" | Out-Null
        Write-Host "n8n webhook : POST OK"
    } catch {
        Write-Warning "n8n webhook : echec POST - $_"
    }
}

# ----------------------------------------------------------------------------
# 9. Mise a jour baseline (sur demande explicite uniquement)
# ----------------------------------------------------------------------------
if ($UpdateBaseline) {
    $cur.set_by = "UpdateBaseline $DateRun"
    $cur | ConvertTo-Json -Depth 12 | Set-Content -Path $BaselineFile -Encoding UTF8
    Write-Host "Baseline mise a jour : $BaselineFile"
}

# Exit codes : 0 aucun changement, 2 changement detecte, 1 erreur API (plus haut)
if ($hasChanges) { exit 2 }
exit 0

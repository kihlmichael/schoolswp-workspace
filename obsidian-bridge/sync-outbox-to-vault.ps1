#Requires -Version 7
# ============================================================================
# sync-outbox-to-vault.ps1   (Passerelle Obsidian schoolsWP - Phase 2)
#
# Synchronise les memos techniques produits par Claude Code vers le vault
# Obsidian schoolsWP, en sens unique :
#   obsidian-bridge/outbox-to-obsidian/*.md  ->  vault .../outbox-depuis-claude/
#
# - Idempotent : ne transporte que les drafts absents du vault (skip par nom).
# - Conserve une copie locale (miroir) dans outbox-to-obsidian/_archive/deja-transportes/
#   gardee indefiniment, evolutive (re-generee a chaque passe d'index).
# - Regenere l'index versionne cote repo + le MOC cote vault.
# - Journalise dans obsidian-bridge/logs/sync.log.
#
# Usage :
#   pwsh ./sync-outbox-to-vault.ps1            # synchronise
#   pwsh ./sync-outbox-to-vault.ps1 -DryRun    # simulation, n'ecrit rien
#
# Aucune suppression : les drafts transportes sont DEPLACES vers le miroir local,
# jamais supprimes. Le vault reste l'autorite finale (on n'ecrase jamais une note
# vault deja presente).
# ============================================================================
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'

# --- Chemins cote projet ---
$BridgeDir = $PSScriptRoot
$OutboxDir = Join-Path $BridgeDir 'outbox-to-obsidian'
$MirrorDir = Join-Path (Join-Path $OutboxDir '_archive') 'deja-transportes'
$LogsDir   = Join-Path $BridgeDir 'logs'
$RepoIndex = Join-Path $BridgeDir 'INDEX-memos-techniques.md'
$EnvFile   = Join-Path (Split-Path $BridgeDir -Parent) '.env'

# --- Chemins cote vault (espaces + accents + emoji : toujours -LiteralPath) ---
$VaultBridge = 'D:\MES SITES\' + [System.Char]::ConvertFromUtf32(0x1F4CB) + ' SCHOOLSWP.COM\12_Obsidian\schoolsWP\00_systeme\claude-code-bridge'
$VaultOutbox = Join-Path $VaultBridge 'outbox-depuis-claude'
$VaultMoc    = Join-Path $VaultBridge 'MOC-memos-techniques.md'

$logFile = Join-Path $LogsDir 'sync.log'
function Log([string]$m) {
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ss'
    if (-not $DryRun) { Add-Content -LiteralPath $logFile -Value "$ts | $m" -Encoding utf8 }
    Write-Host "$ts | $m"
}

# --- Pre-requis : vault accessible ---
if (-not (Test-Path -LiteralPath $VaultBridge)) {
    Log "ERREUR : passerelle vault introuvable ($VaultBridge) - abandon (vault non monte ?)"
    exit 1
}
foreach ($d in @($MirrorDir, $LogsDir, $VaultOutbox)) {
    if (-not (Test-Path -LiteralPath $d)) { New-Item -ItemType Directory -Force -Path $d | Out-Null }
}

# --- Index des noms deja presents dans le vault ---
$vaultHas = @{}
Get-ChildItem -LiteralPath $VaultOutbox -Filter *.md -File -ErrorAction SilentlyContinue |
    ForEach-Object { $vaultHas[$_.Name] = $true }

# --- 1. Transport des drafts en attente (racine outbox, hors fichiers _*) ---
$pending = Get-ChildItem -LiteralPath $OutboxDir -Filter *.md -File | Where-Object { $_.Name -notlike '_*' }
$nTransport = 0
foreach ($f in $pending) {
    $dst = Join-Path $VaultOutbox $f.Name
    if (-not $vaultHas.ContainsKey($f.Name)) {
        if ($DryRun) { Log "DRY transport -> vault : $($f.Name)" }
        else { Copy-Item -LiteralPath $f.FullName -Destination $dst -Force; Log "transport -> vault : $($f.Name)" }
        $nTransport++
    }
    # la copie locale rejoint le miroir (gardee), qu'elle ait ete transportee ou deja presente
    if (-not $DryRun) { Move-Item -LiteralPath $f.FullName -Destination (Join-Path $MirrorDir $f.Name) -Force }
}

# --- 2. Regeneration des index a partir du miroir (= memos synchronises) ---
$memos = Get-ChildItem -LiteralPath $MirrorDir -Filter *.md -File |
    Where-Object { $_.Name -notlike '_*' } | Sort-Object Name
$groups = [ordered]@{}
foreach ($m in $memos) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($m.Name)
    $parts = $base -split '_'
    $date = $parts[0]
    if ($parts.Count -ge 3) { $type = $parts[1]; $title = ($parts[2..($parts.Count - 1)] -join '_') }
    elseif ($parts.Count -eq 2) { $type = 'divers'; $title = $parts[1] }
    else { $type = 'divers'; $title = $base }
    if (-not $groups.Contains($type)) { $groups[$type] = New-Object System.Collections.ArrayList }
    [void]$groups[$type].Add([pscustomobject]@{ Date = $date; Title = $title; Name = $base })
}
$sortedTypes = $groups.Keys | Sort-Object
$today = Get-Date -Format 'yyyy-MM-dd'

# Index versionne cote repo (liste lisible, sans wikilink)
$repo = New-Object System.Text.StringBuilder
[void]$repo.AppendLine('# Index des memos techniques schoolsWP (passerelle Obsidian)')
[void]$repo.AppendLine('')
[void]$repo.AppendLine('Genere automatiquement par `sync-outbox-to-vault.ps1` (re-genere a chaque synchro). Ne pas editer a la main.')
[void]$repo.AppendLine('')
[void]$repo.AppendLine("$($memos.Count) memos synchronises vers le vault Obsidian (``00_systeme/claude-code-bridge/outbox-depuis-claude/``). Copies locales : ``outbox-to-obsidian/_archive/deja-transportes/``. Navigation Obsidian : ``MOC-memos-techniques.md`` dans le vault.")
[void]$repo.AppendLine('')
foreach ($t in $sortedTypes) {
    [void]$repo.AppendLine("## $t ($($groups[$t].Count))")
    [void]$repo.AppendLine('')
    foreach ($it in ($groups[$t] | Sort-Object Date -Descending)) {
        [void]$repo.AppendLine("- $($it.Date) - $($it.Title -replace '-', ' ')")
    }
    [void]$repo.AppendLine('')
}

# MOC cote vault (wikilinks Obsidian)
$moc = New-Object System.Text.StringBuilder
[void]$moc.AppendLine('# MOC - Memos techniques schoolsWP (depuis Claude Code)')
[void]$moc.AppendLine('')
[void]$moc.AppendLine("Carte de contenu generee le $today par la passerelle (``sync-outbox-to-vault.ps1``). $($memos.Count) notes, $($sortedTypes.Count) categories.")
[void]$moc.AppendLine('')
foreach ($t in $sortedTypes) {
    [void]$moc.AppendLine("## $t")
    [void]$moc.AppendLine('')
    foreach ($it in ($groups[$t] | Sort-Object Date -Descending)) {
        [void]$moc.AppendLine("- [[$($it.Name)]]")
    }
    [void]$moc.AppendLine('')
}

if ($DryRun) {
    Log "DRY index repo : $RepoIndex"
    Log "DRY MOC vault  : $VaultMoc"
}
else {
    Set-Content -LiteralPath $RepoIndex -Value $repo.ToString() -Encoding utf8
    Set-Content -LiteralPath $VaultMoc -Value $moc.ToString() -Encoding utf8
    Log "index repo + MOC vault regeneres"
}

$suffix = if ($DryRun) { ' [DRY-RUN]' } else { '' }
Log "sync terminee : $nTransport transportes, $($memos.Count) memos indexes, $($sortedTypes.Count) categories$suffix"

# --- 3. Notification Discord optionnelle (si des memos ont ete transportes) ---
if (-not $DryRun -and $nTransport -gt 0 -and (Test-Path -LiteralPath $EnvFile)) {
    $line = Get-Content -LiteralPath $EnvFile | Where-Object { $_ -match '^\s*DISCORD_ROUTINES_WEBHOOK\s*=' } | Select-Object -First 1
    if ($line) {
        $hook = ($line -replace '^\s*DISCORD_ROUTINES_WEBHOOK\s*=', '').Trim().Trim('"')
        if ($hook) {
            try {
                $msg = "Passerelle Obsidian schoolsWP : $nTransport memo(s) synchronise(s) vers le vault. Total indexe : $($memos.Count)."
                $body = @{ content = $msg } | ConvertTo-Json -Compress
                Invoke-RestMethod -Uri $hook -Method Post -ContentType 'application/json' -Body $body | Out-Null
                Log 'notification Discord envoyee'
            }
            catch { Log "ERREUR notification Discord : $($_.Exception.Message)" }
        }
    }
}
exit 0

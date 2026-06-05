<#
.SYNOPSIS
  Promotion d'un draft passerelle (outbox-to-obsidian) vers une zone stable du vault
  Obsidian schoolsWP, avec backup, entree log.md (section 6) + ligne de grille (section 5),
  et verification. Encode la procedure manuelle de la SOP passerelle (exception 8.4).

.DESCRIPTION
  Ecrit dans le vault via PowerShell car les outils Write/Edit sont restreints au perimetre
  projet. A n'utiliser qu'apres validation L0 explicite de Michael (le script ne demande rien).
  Operations additives uniquement : nouveau fichier en zone stable (jamais d'ecrasement),
  append de l'entree log, ajout d'une ligne de grille. Backup du log.md avant edition.

.PARAMETER DraftPath
  Chemin du draft source (relatif a obsidian-bridge/ ou absolu).
.PARAMETER TargetZone
  Zone stable cible du vault, ex : 05_sop, 06_decisions, 03_synthesis.
.PARAMETER TargetName
  Nom du fichier cible dans la zone, ex : SOP-mon-sujet.md.
.PARAMETER SetFields
  Table de champs frontmatter scalaires a poser/mettre a jour sur le fichier promu
  (ex : @{status='sop-stable'; validated_by='Michael KIHL'; date_validation='2026-06-05'}).
.PARAMETER Trace
  Copie aussi le draft dans 00_systeme/claude-code-bridge/outbox-depuis-claude/.
.PARAMETER WhatIf
  Dry-run : montre le fichier cible, l'entree log et la ligne de grille sans rien ecrire.

.EXAMPLE
  ./promote-to-vault.ps1 -DraftPath outbox-to-obsidian/2026-06-05_sop_x.md -TargetZone 05_sop `
    -TargetName SOP-x.md -Type ajout -Title "SOP X" -Action "..." -Reason "..." `
    -Validation "oui (Michael L0 2026-06-05)" -SetFields @{status='sop-stable'} -WhatIf
#>
param(
  [Parameter(Mandatory)][string]$DraftPath,
  [Parameter(Mandatory)][string]$TargetZone,
  [Parameter(Mandatory)][string]$TargetName,
  [Parameter(Mandatory)][ValidateSet('ajout','modification','decision','correction','synthese','validation_memoire','lint','archive')][string]$Type,
  [Parameter(Mandatory)][string]$Title,
  [Parameter(Mandatory)][string]$Action,
  [Parameter(Mandatory)][string]$Reason,
  [Parameter(Mandatory)][string]$Validation,
  [string]$Author = 'Claude Code (production) + Michael (validation L0)',
  [string[]]$Notes = @(),
  [hashtable]$SetFields = @{},
  [string]$Date = (Get-Date -Format 'yyyy-MM-dd'),
  [string]$VaultRoot = 'D:\MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP',
  [string]$ProjectBridge = 'D:\VS Code\CLAUDE CODE\projects\schoolswp\obsidian-bridge',
  [switch]$Trace,
  [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
$BT = [char]0x60   # literal backtick for markdown inline-code, built without escaping

function Resolve-Draft([string]$p) {
  if (Test-Path -LiteralPath $p) { return (Resolve-Path -LiteralPath $p).Path }
  $alt = Join-Path $ProjectBridge $p
  if (Test-Path -LiteralPath $alt) { return (Resolve-Path -LiteralPath $alt).Path }
  throw "Draft introuvable : $p"
}

$draftFull = Resolve-Draft $DraftPath
$zoneDir   = Join-Path $VaultRoot $TargetZone
$target    = Join-Path $zoneDir $TargetName
$log       = Join-Path $VaultRoot 'log.md'

if (-not (Test-Path -LiteralPath $zoneDir)) { throw "Zone cible inexistante (ouverture de zone = decision a part) : $zoneDir" }
if (Test-Path -LiteralPath $target)         { throw "Cible deja presente, pas d'ecrasement : $target" }
if (-not (Test-Path -LiteralPath $log))     { throw "log.md introuvable : $log" }

# --- contenu du fichier promu (pose eventuelle de champs frontmatter) ---
$content = Get-Content -LiteralPath $draftFull -Raw
foreach ($k in $SetFields.Keys) {
  $v = [string]$SetFields[$k]
  $rxKey = '(?m)^' + [regex]::Escape($k) + ':.*$'
  if ([regex]::IsMatch($content, $rxKey)) {
    $content = [regex]::Replace($content, $rxKey, ($k + ': ' + $v))
  } else {
    $content = [regex]::Replace($content, '(?s)^(---\r?\n)', ('${1}' + $k + ': ' + $v + "`n"), 1)
  }
}

# --- entree log (section 6, append) ---
$cibleRef = $BT + $TargetZone + '/' + $TargetName + $BT
$entry  = "### [$Date] $Type | $Title`n`n"
$entry += "- **Auteur** : $Author`n"
$entry += "- **Cible** : $cibleRef`n"
$entry += "- **Action** : $Action`n"
$entry += "- **Raison** : $Reason`n"
$entry += "- **Validation** : $Validation`n"
if ($Notes.Count -gt 0) {
  $entry += "- **Notes** :`n"
  foreach ($n in $Notes) { $entry += "  - $n`n" }
}
$entry += "`n---`n"

# --- ligne de grille (section 5) ---
$gridRow = "| $Date | $Type | $TargetZone/$TargetName | $Author | $Validation |"

if ($WhatIf) {
  Write-Output "[DRY-RUN] promotion :"
  Write-Output "  draft  : $draftFull"
  Write-Output "  cible  : $target"
  Write-Output "  trace  : $([bool]$Trace)"
  Write-Output "--- entree log ---"
  Write-Output $entry
  Write-Output "--- ligne grille ---"
  Write-Output $gridRow
  return
}

# --- backup log.md ---
$stamp  = (Get-Date -Format 'yyyyMMdd-HHmmss')
$backup = Join-Path $ProjectBridge ("logs/_vault-log-backup-$stamp.md")
Copy-Item -LiteralPath $log -Destination $backup -Force

# --- fichier promu ---
Set-Content -LiteralPath $target -Value $content -NoNewline -Encoding utf8

# --- trace optionnelle ---
if ($Trace) {
  $traceDir = Join-Path $VaultRoot '00_systeme\claude-code-bridge\outbox-depuis-claude'
  if (Test-Path -LiteralPath $traceDir) {
    Copy-Item -LiteralPath $draftFull -Destination (Join-Path $traceDir (Split-Path $draftFull -Leaf)) -Force
  }
}

# --- edition log.md : ligne grille (section 5) + entree (append section 6) ---
$raw   = Get-Content -LiteralPath $log -Raw
$eol   = if ($raw -match "`r`n") { "`r`n" } else { "`n" }
$lines = $raw -split "`r`n|`n"

# insert grille : derniere ligne commencant par '|' avant la note '> Cette grille'
$noteIdx = -1
for ($i = 0; $i -lt $lines.Count; $i++) { if ($lines[$i] -match '^>\s*Cette grille') { $noteIdx = $i; break } }
if ($noteIdx -lt 0) { throw "Marqueur de fin de grille introuvable (> Cette grille). Edition annulee, backup : $backup" }
$lastRow = -1
for ($i = $noteIdx; $i -ge 0; $i--) { if ($lines[$i] -match '^\|') { $lastRow = $i; break } }
if ($lastRow -lt 0) { throw "Aucune ligne de grille trouvee. Edition annulee, backup : $backup" }

$spliced = @()
$spliced += $lines[0..$lastRow]
$spliced += $gridRow
$spliced += $lines[($lastRow + 1)..($lines.Count - 1)]
$raw = ($spliced -join $eol)

# append entree en fin de fichier (les entrees recentes vivent a la fin)
$entryEol = ($entry -replace "`r`n", "`n")
if ($eol -eq "`r`n") { $entryEol = $entryEol -replace "`n", "`r`n" }
if (-not $raw.EndsWith($eol)) { $raw += $eol }
$raw += $eol + $entryEol

Set-Content -LiteralPath $log -Value $raw -NoNewline -Encoding utf8

# --- verification ---
$after = Get-Content -LiteralPath $log -Raw
$okGrid  = $after -match ('(?m)^\| ' + [regex]::Escape($Date) + ' \| ' + [regex]::Escape($Type) + ' \| ' + [regex]::Escape("$TargetZone/$TargetName"))
$okEntry = $after -match ('(?m)^### \[' + [regex]::Escape($Date) + '\] ' + [regex]::Escape($Type) + ' \| ' + [regex]::Escape($Title))
$okFile  = Test-Path -LiteralPath $target
Write-Output "fichier promu present : $okFile -> $target"
Write-Output "ligne grille ajoutee  : $okGrid"
Write-Output "entree log ajoutee    : $okEntry"
Write-Output "backup log.md         : $backup"
if (-not ($okFile -and $okGrid -and $okEntry)) {
  Write-Output "ATTENTION : une verification a echoue. Restaurer log.md depuis le backup si besoin."
  exit 1
}
Write-Output "OK : promotion $TargetZone/$TargetName terminee."

<#
.SYNOPSIS
  Re-scrape mensuel de la documentation LiveAvatar (cron via Windows Task Scheduler).

.DESCRIPTION
  Lance snapshot.py vers snapshots/<date>/, journalise la sortie dans logs/run-<date>.log.
  Avec -UploadDrive, miroir aussi le snapshot vers un sous-dossier date sous le dossier Drive
  LiveAvatar (history, pas d'ecrasement de la copie courante).
  Le transport vers le vault Obsidian reste manuel (arbitrage humain, SOP passerelle).

.PARAMETER UploadDrive
  Si present, uploade le snapshot du mois vers Drive LiveAvatar/_snapshot-<date>/.

.PARAMETER Date
  Date stamp YYYY-MM-DD (defaut : aujourd'hui).

.EXAMPLE
  ./run-monthly.ps1
  ./run-monthly.ps1 -UploadDrive
#>
param(
  [switch]$UploadDrive,
  [string]$Date = (Get-Date -Format 'yyyy-MM-dd'),
  [string]$LiveAvatarDriveFolderId = '1XPwXJUT1va9Q7G3AaXkUCb8EzlZTudQT'
)
$ErrorActionPreference = 'Stop'
$ToolDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = (Resolve-Path (Join-Path $ToolDir '..\..')).Path
$Python = Join-Path $ProjectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $Python)) { $Python = 'python' }

$logDir = Join-Path $ToolDir 'logs'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "run-$Date.log"
$snapDir = Join-Path $ToolDir "snapshots\$Date"

"=== LiveAvatar doc snapshot - $Date ===" | Tee-Object -FilePath $logFile
"Python : $Python" | Tee-Object -FilePath $logFile -Append

& $Python (Join-Path $ToolDir 'snapshot.py') --date $Date --out $snapDir 2>&1 | Tee-Object -FilePath $logFile -Append
if ($LASTEXITCODE -ne 0) { "ECHEC snapshot (exit $LASTEXITCODE)" | Tee-Object -FilePath $logFile -Append; exit 1 }

if ($UploadDrive) {
  "--- Upload Drive (history) ---" | Tee-Object -FilePath $logFile -Append
  & $Python (Join-Path $ToolDir 'upload_to_drive.py') --src $snapDir --parent $LiveAvatarDriveFolderId --name "_snapshot-$Date" 2>&1 | Tee-Object -FilePath $logFile -Append
  if ($LASTEXITCODE -ne 0) { "ECHEC upload Drive (exit $LASTEXITCODE)" | Tee-Object -FilePath $logFile -Append; exit 1 }
}

"OK : snapshot $Date termine ($snapDir)" | Tee-Object -FilePath $logFile -Append

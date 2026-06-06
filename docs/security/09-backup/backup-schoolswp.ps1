# backup-schoolswp.ps1
# Nightly backup via restic to Backblaze B2.
# Usage:
#   - Manual:   .\backup-schoolswp.ps1
#   - DryRun:   .\backup-schoolswp.ps1 -DryRun
#   - From Task Scheduler: see backup-schoolswp-task.ps1
#
# Requires env vars set in calling session (see load-backup-secrets.ps1):
#   - B2_ACCOUNT_ID
#   - B2_ACCOUNT_KEY
#   - RESTIC_REPOSITORY
#   - RESTIC_PASSWORD

param(
    [switch]$DryRun = $false,
    [switch]$SkipForget = $false,
    [switch]$SkipCheck = $false
)

$ErrorActionPreference = "Stop"

# === Configuration ===
$ProjectRoot   = "D:\VS Code\CLAUDE CODE\projects\schoolswp"
$ObsidianVault = "D:\MES SITES\SCHOOLSWP.COM\12_Obsidian\schoolsWP"
$N8nSnapshotDir = "$ProjectRoot\docs\security\09-backup"  # contains n8n-snapshot-YYYY-MM-DD/
$LogDir        = "$ProjectRoot\logs"

# Hostname tag for snapshots (lets you distinguish if you backup from multiple machines later)
$HostTag = $env:COMPUTERNAME

# Retention policy
$KeepDaily   = 7
$KeepWeekly  = 4
$KeepMonthly = 6

# === Pre-flight: verify env vars ===
$required = @("B2_ACCOUNT_ID", "B2_ACCOUNT_KEY", "RESTIC_REPOSITORY", "RESTIC_PASSWORD")
foreach ($v in $required) {
    if (-not (Test-Path "env:$v")) {
        Write-Host "ERROR: env var $v not set." -ForegroundColor Red
        Write-Host "Load secrets first: . .\load-backup-secrets.ps1"
        exit 1
    }
}

# === Pre-flight: verify restic + paths ===
if (-not (Get-Command restic -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: restic not in PATH. Install via: winget install restic.restic" -ForegroundColor Red
    exit 2
}

foreach ($p in @($ProjectRoot, $ObsidianVault, $N8nSnapshotDir)) {
    if (-not (Test-Path $p)) {
        Write-Host "ERROR: path missing: $p" -ForegroundColor Red
        exit 3
    }
}

# === Log setup ===
$DateTag = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$LogFile = Join-Path $LogDir "restic-backup-$DateTag.log"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
function Log {
    param([string]$msg)
    $line = "[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $msg
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

# === Excludes (project repo) ===
$RepoExcludes = @(
    "--exclude=.venv",
    "--exclude=node_modules",
    "--exclude=_archive",
    "--exclude=.next",
    "--exclude=dist",
    "--exclude=build",
    "--exclude=target",
    "--exclude=.pytest_cache",
    "--exclude=.mypy_cache",
    "--exclude=.ruff_cache",
    "--exclude=__pycache__",
    "--exclude=logs/*.log",
    "--exclude=.coverage",
    "--exclude=coverage.xml",
    "--exclude=tools/wp-media-upload/.cache",
    "--exclude=.claude/worktrees"
)

# === Run backups ===
Log "=== restic backup START (host=$HostTag) ==="
Log "Repo: $env:RESTIC_REPOSITORY"
Log "DryRun: $DryRun | SkipForget: $SkipForget | SkipCheck: $SkipCheck"

$DryFlag = if ($DryRun) { @("--dry-run") } else { @() }

# Backup 1 : project repo
Log ""
Log "--- [1/3] BACKUP repo schoolswp ---"
$args = @("backup", $ProjectRoot) + $RepoExcludes + @("--tag", "repo", "--tag", $HostTag) + $DryFlag
& restic @args 2>&1 | Tee-Object -Append -FilePath $LogFile
if ($LASTEXITCODE -ne 0) {
    Log "ERROR: restic backup repo failed (exit $LASTEXITCODE)"
    exit 10
}

# Backup 2 : Obsidian vault
Log ""
Log "--- [2/3] BACKUP vault Obsidian ---"
$VaultExcludes = @(
    "--exclude=.obsidian/workspace*.json",
    "--exclude=.obsidian/cache",
    "--exclude=.trash"
)
$args = @("backup", $ObsidianVault) + $VaultExcludes + @("--tag", "vault-obsidian", "--tag", $HostTag) + $DryFlag
& restic @args 2>&1 | Tee-Object -Append -FilePath $LogFile
if ($LASTEXITCODE -ne 0) {
    Log "ERROR: restic backup vault failed (exit $LASTEXITCODE)"
    exit 11
}

# Backup 3 : n8n snapshots folder (all dated subfolders inside)
Log ""
Log "--- [3/3] BACKUP n8n snapshots ---"
$N8nFolders = Get-ChildItem $N8nSnapshotDir -Directory -Filter "n8n-snapshot-*"
if ($N8nFolders.Count -eq 0) {
    Log "WARN: no n8n-snapshot-* folder found in $N8nSnapshotDir (run _export_n8n_workflows.py first)"
} else {
    foreach ($folder in $N8nFolders) {
        Log "  including: $($folder.Name)"
    }
    $args = @("backup", $N8nSnapshotDir) +
            @("--exclude=*.py", "--exclude=__pycache__", "--exclude=*.md") +
            @("--tag", "n8n-snapshot", "--tag", $HostTag) + $DryFlag
    & restic @args 2>&1 | Tee-Object -Append -FilePath $LogFile
    if ($LASTEXITCODE -ne 0) {
        Log "ERROR: restic backup n8n failed (exit $LASTEXITCODE)"
        exit 12
    }
}

# === Forget (apply retention) ===
if (-not $SkipForget -and -not $DryRun) {
    Log ""
    Log "--- forget + prune (retention: daily=$KeepDaily weekly=$KeepWeekly monthly=$KeepMonthly) ---"
    & restic forget `
        --keep-daily $KeepDaily `
        --keep-weekly $KeepWeekly `
        --keep-monthly $KeepMonthly `
        --prune 2>&1 | Tee-Object -Append -FilePath $LogFile
    if ($LASTEXITCODE -ne 0) {
        Log "WARN: restic forget/prune exit $LASTEXITCODE (non-blocking)"
    }
}

# === Integrity check ===
if (-not $SkipCheck -and -not $DryRun) {
    Log ""
    Log "--- restic check (integrity, may be slow on large repos) ---"
    & restic check 2>&1 | Tee-Object -Append -FilePath $LogFile
    if ($LASTEXITCODE -ne 0) {
        Log "ERROR: restic check failed (exit $LASTEXITCODE) - REPO INTEGRITY ISSUE"
        exit 20
    }
}

# === Summary ===
Log ""
Log "--- snapshots list (last 5) ---"
& restic snapshots --compact --last 5 2>&1 | Tee-Object -Append -FilePath $LogFile

Log ""
Log "=== restic backup DONE ==="
Log "Log file: $LogFile"

Write-Host ""
Write-Host "Backup terminé avec succès. Log: $LogFile" -ForegroundColor Green

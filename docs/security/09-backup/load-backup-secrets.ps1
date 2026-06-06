# load-backup-secrets.ps1
# Charge les credentials restic + B2 dans la session PowerShell courante.
# Usage: . .\load-backup-secrets.ps1  (note le point devant pour dot-source)
#
# Lit les valeurs depuis %USERPROFILE%\.schoolswp-backup-secrets.ps1
# qui DOIT etre chmod 600 equivalent (NTFS perms restrictifs) et JAMAIS commit en git.
#
# Le fichier .schoolswp-backup-secrets.ps1 doit contenir uniquement :
#   $env:B2_ACCOUNT_ID = "..."
#   $env:B2_ACCOUNT_KEY = "..."
#   $env:RESTIC_REPOSITORY = "b2:schoolswp-backups-2026"
#   $env:RESTIC_PASSWORD = "..."

$SecretsFile = Join-Path $env:USERPROFILE ".schoolswp-backup-secrets.ps1"

if (-not (Test-Path $SecretsFile)) {
    Write-Host "ERROR: secrets file not found: $SecretsFile" -ForegroundColor Red
    Write-Host ""
    Write-Host "Cree le fichier avec ce contenu (remplace les valeurs):" -ForegroundColor Yellow
    Write-Host ""
    Write-Host '  $env:B2_ACCOUNT_ID = "<keyID from 1Password>"'
    Write-Host '  $env:B2_ACCOUNT_KEY = "<applicationKey from 1Password>"'
    Write-Host '  $env:RESTIC_REPOSITORY = "b2:schoolswp-backups-2026"'
    Write-Host '  $env:RESTIC_PASSWORD = "<32-char random from 1Password>"'
    Write-Host ""
    Write-Host "Puis restreins les permissions NTFS:" -ForegroundColor Yellow
    Write-Host '  icacls "$env:USERPROFILE\.schoolswp-backup-secrets.ps1" /inheritance:r /grant:r "$env:USERNAME:F"'
    return $false
}

# Verifie les permissions NTFS (que conta soit le seul ayant FullControl)
$acl = Get-Acl $SecretsFile
$nonOwnerAccess = $acl.Access | Where-Object {
    ($_.IdentityReference -notlike "*$env:USERNAME*") -and
    ($_.IdentityReference -notlike "*SYSTEM*") -and
    ($_.IdentityReference -notlike "*Administrateurs*") -and
    ($_.IdentityReference -notlike "*Administrators*")
}
if ($nonOwnerAccess) {
    Write-Host "WARN: secrets file has permissions for other users:" -ForegroundColor Yellow
    $nonOwnerAccess | Format-Table IdentityReference, FileSystemRights, AccessControlType
    Write-Host "Fix avec:" -ForegroundColor Yellow
    Write-Host "  icacls `"$SecretsFile`" /inheritance:r /grant:r `"$env:USERNAME`:F`""
}

# Charge les variables
. $SecretsFile

# Verifie que les 4 vars sont bien set
$required = @("B2_ACCOUNT_ID", "B2_ACCOUNT_KEY", "RESTIC_REPOSITORY", "RESTIC_PASSWORD")
$missing = @()
foreach ($v in $required) {
    if (-not (Test-Path "env:$v")) {
        $missing += $v
    }
}
if ($missing.Count -gt 0) {
    Write-Host "ERROR: missing vars after sourcing: $($missing -join ', ')" -ForegroundColor Red
    return $false
}

Write-Host "OK: backup secrets loaded (RESTIC_REPOSITORY=$env:RESTIC_REPOSITORY)" -ForegroundColor Green
return $true

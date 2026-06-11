#Requires -Version 7
# ============================================================================
# register-sync-task.ps1
# Enregistre (ou met a jour) la tache planifiee Windows "schoolsWP Obsidian Sync"
# qui lance sync-outbox-to-vault.ps1 : au logon + tous les jours a 13:00.
#
# Compte courant, LogonType Interactive, RunLevel Limited : aucune elevation
# requise (meme schema que la tache "schoolsWP Memory Lint").
#
#   pwsh ./register-sync-task.ps1            # enregistre / met a jour
#   pwsh ./register-sync-task.ps1 -Remove    # supprime la tache
# ============================================================================
param([switch]$Remove)
$ErrorActionPreference = 'Stop'

$TaskName = 'schoolsWP Obsidian Sync'

if ($Remove) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    "Tache '$TaskName' supprimee."
    return
}

$Script = Join-Path $PSScriptRoot 'sync-outbox-to-vault.ps1'
if (-not (Test-Path -LiteralPath $Script)) { throw "Script introuvable : $Script" }
$pwsh = (Get-Command pwsh -ErrorAction Stop).Source

$action = New-ScheduledTaskAction -Execute $pwsh -Argument "-NoProfile -ExecutionPolicy RemoteSigned -File `"$Script`""
$trigLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$trigDaily = New-ScheduledTaskTrigger -Daily -At '13:00'
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger @($trigLogon, $trigDaily) `
    -Principal $principal -Settings $settings -Force `
    -Description 'Synchronise les memos techniques schoolsWP (outbox-to-obsidian) vers le vault Obsidian + regenere les index. Voir obsidian-bridge/sync-outbox-to-vault.ps1' | Out-Null

"Tache '$TaskName' enregistree (logon + quotidien 13:00)."
Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State

#Requires -Version 7
# ============================================================================
# install-memory-normalize-task.ps1
# Enregistre (ou met a jour) la tache planifiee Windows
# "schoolsWP Memory Normalize".
# Trigger : Weekly Monday 9h00 (heure locale). Relancer ce script pour
# reinstaller apres modification.
# ============================================================================

$ErrorActionPreference = 'Stop'

$TaskName = 'schoolsWP Memory Normalize'
$Launcher = Join-Path $PSScriptRoot 'memory-normalize-launcher.ps1'

if (-not (Test-Path $Launcher)) {
    throw "Launcher introuvable : $Launcher"
}

$pwshPath  = (Get-Command pwsh).Source
$taskArgs  = '-NoProfile -ExecutionPolicy RemoteSigned -File "' + $Launcher + '"'
$action    = New-ScheduledTaskAction -Execute $pwshPath -Argument $taskArgs
$trigger   = New-ScheduledTaskTrigger -Weekly -WeeksInterval 1 -DaysOfWeek Monday -At '9:00am'
$timeLimit = New-TimeSpan -Minutes 5
$settings  = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit $timeLimit
$descText  = 'Normalisation hebdo (lundi 9h) du frontmatter de la memoire interne schoolsWP. Idempotent. Notification Discord si drift corrige.'

Register-ScheduledTask -TaskName $TaskName -Force -Action $action -Trigger $trigger -Settings $settings -Description $descText | Out-Null

Write-Host "Tache '$TaskName' enregistree (trigger Weekly Monday 9am)."
Write-Host "Verifier : Get-ScheduledTask -TaskName '$TaskName'"
Write-Host "Lancer manuellement : Start-ScheduledTask -TaskName '$TaskName'"

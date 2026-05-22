#Requires -Version 7
# ============================================================================
# install-memory-lint-task.ps1
# Enregistre (ou met a jour) la tache planifiee Windows "schoolsWP Memory Lint".
# Trigger : AtLogOn. Relancer ce script pour reinstaller apres modification.
# ============================================================================

$ErrorActionPreference = 'Stop'

$TaskName = 'schoolsWP Memory Lint'
$Launcher = Join-Path $PSScriptRoot 'memory-lint-launcher.ps1'

if (-not (Test-Path $Launcher)) {
    throw "Launcher introuvable : $Launcher"
}

$pwshPath  = (Get-Command pwsh).Source
$taskArgs  = '-NoProfile -ExecutionPolicy RemoteSigned -File "' + $Launcher + '"'
$action    = New-ScheduledTaskAction -Execute $pwshPath -Argument $taskArgs
$trigger   = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$timeLimit = New-TimeSpan -Minutes 30
$settings  = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit $timeLimit
$descText  = 'Lint de la memoire interne schoolsWP (bride a 1x/jour par le launcher).'

Register-ScheduledTask -TaskName $TaskName -Force -Action $action -Trigger $trigger -Settings $settings -Description $descText | Out-Null

Write-Host "Tache '$TaskName' enregistree (trigger AtLogOn)."
Write-Host "Verifier : Get-ScheduledTask -TaskName '$TaskName'"

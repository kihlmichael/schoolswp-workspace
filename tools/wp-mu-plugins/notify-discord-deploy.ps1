# notify-discord-deploy.ps1
#
# Notification Discord post-deploy d'un mu-plugin schoolsWP.
# Pousse une ligne dans le channel #alerts via le webhook schoolsWP-Routines.
#
# Usage :
#   .\notify-discord-deploy.ps1 -PluginName "schoolswp-affiliate-cloaks" -Version "1.1.1" -PhpFile "schoolswp-affiliate-cloaks.php"
#
# Prerequis :
#   - Variable d'env DISCORD_SCHOOLSWP_ROUTINES_URL definie (HKCU\Environment)
#     ou parametre -WebhookUrl explicite.
#   - Le PhpFile doit exister localement (pour calcul SHA-256 de tracabilite).
#
# Référence mémoire : reference_discord_webhook_routines

param(
    [Parameter(Mandatory=$true)]
    [string]$PluginName,

    [Parameter(Mandatory=$true)]
    [string]$Version,

    [Parameter(Mandatory=$false)]
    [string]$PhpFile = "",

    [Parameter(Mandatory=$false)]
    [string]$WebhookUrl = $env:DISCORD_SCHOOLSWP_ROUTINES_URL,

    [Parameter(Mandatory=$false)]
    [string]$Status = "success"
)

if ([string]::IsNullOrWhiteSpace($WebhookUrl)) {
    Write-Error "Webhook URL absente. Definir DISCORD_SCHOOLSWP_ROUTINES_URL ou passer -WebhookUrl."
    exit 1
}

$sha256 = "n/a"
if (-not [string]::IsNullOrWhiteSpace($PhpFile) -and (Test-Path $PhpFile)) {
    $hash = Get-FileHash $PhpFile -Algorithm SHA256
    $sha256 = $hash.Hash.Substring(0, 12).ToLower()
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"

$emoji = if ($Status -eq "success") { ":ship:" } else { ":warning:" }

$message = "$emoji **mu-plugin pushed** : ``$PluginName`` v$Version`n" +
           "SHA-256 (12) : ``$sha256```n" +
           "Timestamp : $timestamp`n" +
           "Status : $Status"

$payload = @{
    content = $message
} | ConvertTo-Json -Compress

try {
    $response = Invoke-RestMethod -Uri $WebhookUrl -Method Post -ContentType "application/json" -Body $payload
    Write-Output "Notification Discord envoyee : $PluginName v$Version (sha $sha256)"
    exit 0
} catch {
    Write-Error "Echec notification Discord : $_"
    exit 2
}

# ECC version watcher

Surveille la sortie de affaan-m/everything-claude-code **version 2 GA** pour declencher la passe 3 cherry-pick (cf. 05_sop/SOP-cherry-pick-depots-tiers-claude-code.md dans le vault Obsidian).

## Pourquoi

ECC publie 53 skills, 12 agents et 8 commands nouveaux toutes les 5 semaines. La passe 2 du 2026-05-24 a etabli le baseline a 2.0.0-rc.1. Quand ECC v2 passera GA (tag de release sans suffixe rc, ou VERSION matching un pattern 3 nombres sans pre-release), il faut lancer la passe 3 sur le delta accumule.

Pattern calque sur tools/check-tutor-docs-changes/.

## Usage

```powershell
.\check.ps1                                                  : check silent
.\check.ps1 -ReportFile "report-2026-XX.md"                  : avec rapport ecrit
.\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..." : alerte Discord si GA (override env var)
.\check.ps1 -N8nWebhookUrl "https://schoolswp-n8n.wp1.host/webhook/ecc-version-watcher"
```

Path repo par defaut : d:\VS Code\CLAUDE CODE\projects\everything-claude-code (modifiable via -EccRepoDir).

Baseline par defaut lue depuis .baseline.json dans le meme dossier.

**Fallback env var (recommande)** : si -WebhookUrl n'est pas fourni, le script lit automatiquement la variable d'environnement user DISCORD_SCHOOLSWP_ROUTINES_URL. Idem pour -N8nWebhookUrl avec N8N_ECC_VERSION_WATCHER_URL. Cela evite de stocker l'URL en clair dans les arguments de la tache planifiee.

## Stockage URL Discord (a faire une seule fois)

Le webhook Discord schoolsWP-Routines (channel #alerts) est stocke en variable d'environnement user persistante dans le registry Windows HKCU. Une fois set, l'URL est disponible pour toutes les sessions PowerShell et toutes les taches planifiees, sans avoir a la retaper ni la commiter en clair.

```powershell
$url = Read-Host "URL Discord webhook schoolsWP-Routines"
[Environment]::SetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", $url, "User")
Remove-Variable url
```

Le Read-Host saisit l'URL dans la console (pas dans la commande ni l'historique git). SetEnvironmentVariable persiste dans HKCU\Environment.

Verification dans une nouvelle session PowerShell :

```powershell
[Environment]::GetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", "User").Length
```

Doit retourner ~120 (longueur typique d'une URL Discord webhook).

Pour recharger dans la session courante apres set (sinon il faut redemarrer PowerShell) :

```powershell
$env:DISCORD_SCHOOLSWP_ROUTINES_URL = [Environment]::GetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", "User")
```

Pour revoquer / changer l'URL (par exemple apres rotation du webhook cote Discord) :

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", $null, "User")
```

Puis re-set avec la nouvelle URL.

## Comportement

1. Le script lance un git fetch origin silencieux sur le clone ECC local.
2. Lecture du fichier VERSION sur origin/HEAD (pas le local HEAD, pour eviter la dependance pull).
3. Liste des tags via git tag list trie par date de creation.
4. Detection GA : VERSION ou tag matchant un pattern 3 nombres sans suffixe pre-release type rc, beta, alpha.
5. Comparaison version actuelle vs baseline.
6. Output rapport Markdown plus POST Discord/n8n si GA detectee.

## Exit codes

- 0 : OK, aucun changement de version
- 2 : GA detectee (action requise)
- 3 : Version a change mais pas GA (probable nouvelle rc, mise a jour de baseline possible)

## Frequence recommandee

**Hebdomadaire** (lundi 10h Paris). ECC sort une rc ou GA toutes les 1 a 3 semaines, hebdo capture le signal sans bruit excessif.

## Cron Windows Task Scheduler

Pre-requis : env var user DISCORD_SCHOOLSWP_ROUTINES_URL deja stockee (voir section Stockage URL Discord plus haut). La tache planifiee ne contient pas l'URL en clair, c'est le script qui la recupere via env var au moment du run.

Creation via Register-ScheduledTask (PowerShell-natif, gere les paths avec espaces correctement, plus propre que schtasks) :

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Unrestricted -NoProfile -File `"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-ecc-version\check.ps1`" -ReportFile `"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-ecc-version\reports\ecc-version-watch.md`""

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 10am

$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd -RunOnlyIfNetworkAvailable

Register-ScheduledTask -TaskName "ECC version watcher hebdo" -Action $action -Trigger $trigger -Settings $settings -Force
```

Verification :

```powershell
Get-ScheduledTask -TaskName "ECC version watcher hebdo" | Get-ScheduledTaskInfo
```

Test immediat :

```powershell
Start-ScheduledTask -TaskName "ECC version watcher hebdo"
Start-Sleep -Seconds 8
Get-ScheduledTaskInfo -TaskName "ECC version watcher hebdo" | Select-Object LastRunTime, LastTaskResult, NextRunTime
```

LastTaskResult egal 0 : succes. NextRunTime : prochain lundi 10h.

Suppression si besoin :

```powershell
Unregister-ScheduledTask -TaskName "ECC version watcher hebdo" -Confirm:$false
```

URL Discord du channel #alerts (webhook schoolsWP-Routines) : stockee dans env var user DISCORD_SCHOOLSWP_ROUTINES_URL (voir section Stockage plus haut). Memoire interne reference_discord_webhook_routines documente le pattern Discord general (URL non stockee dans le repo pour securite).

## Quand GA est detectee

1. Discord push une alerte dans le channel #alerts.
2. Tu ouvres 05_sop/SOP-cherry-pick-depots-tiers-claude-code.md dans le vault Obsidian.
3. Tu lances la passe 3 selon la procedure (clone update, audit delegue, matrice KEEP/ADAPT/REJECT, validation L0, import gut YAML, lockfile, memoire interne, synthese passerelle).
4. Une fois la passe 3 close, tu mets a jour .baseline.json avec la nouvelle version (ex 2.0.0 GA, et le commit hash correspondant).

## Mise a jour de la baseline

Si la version passe d'une rc a une autre (par exemple 2.0.0-rc.1 vers 2.0.0-rc.2) et que tu veux mettre a jour le baseline pour ne plus voir l'alerte exit code 3 :

```json
{
  "version": "2.0.0-rc.2",
  "commit": "<nouveau hash>",
  "set_at": "<date>",
  "set_by": "<contexte>",
  "ga_target_quarter": "2026-Q3"
}
```

## Limites connues

- Pas de re-pull automatique du clone si GA detectee (manuel : git pull puis lancer la passe 3).
- Pas de tracking des hooks ou MCP configurations ajoutes a ECC (hors perimetre cherry-pick selon la SOP 05_sop).
- Webhook Discord stocke en clair dans les parametres Task Scheduler. Pour secret durable, utiliser env var Windows ou stockage chiffre.

## Wrap n8n (optionnel)

Le pattern tutor-docs-watcher inclut un wrap n8n pour orchestrer Discord plus Sheets log plus Telegram depuis un workflow centralise. Si tu veux la meme chose pour ECC :

1. Cloner le workflow np4OG9UGDCGWaK4H (tutor-lms-docs-watcher) dans n8n.
2. Renommer en [InDev] Webhook vers Discord : ECC Version Watcher.
3. Modifier l'endpoint webhook vers ecc-version-watcher.
4. Adapter le node IF : filtrer sur ga_detected egal true ou version_changed egal true.
5. Reconstruire l'embed Discord avec les champs adaptes (version actuelle, baseline, ga_tags).

Pas urgent : le POST Discord direct depuis check.ps1 suffit pour le MVP.

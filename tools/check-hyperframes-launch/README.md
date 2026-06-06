# HyperFrames launch watcher

Surveille un dossier d'un repo GitHub public et alerte quand un **nouveau commit** y apparait. Cible par defaut : `heygen-com/hyperframes-launches`, path `texture-launch-video`.

## Pourquoi

Le repo `hyperframes-launches` heberge les launches HyperFrames (HeyGen). Le dossier `texture-launch-video` correspond a un launch suivi. Ce watcher detecte tout nouveau commit touchant ce path pour ne pas rater une mise a jour.

Pattern calque sur `tools/check-ecc-version/` et `tools/check-tutor-docs-changes/`. Difference : pas de clone local, on tape directement l'API GitHub publique.

## Usage

```powershell
.\check.ps1                                                    # check silent
.\check.ps1 -ReportFile "reports\hyperframes-launch-watch.md"  # avec rapport ecrit
.\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..." # alerte Discord (override env var)
.\check.ps1 -Repo "owner/repo" -Path "sous/dossier"            # surveiller un autre repo/dossier
```

Baseline par defaut lue depuis `.baseline.json` dans le meme dossier.

**Fallback env var (recommande)** : si `-WebhookUrl` n'est pas fourni, le script lit automatiquement la variable d'environnement user `DISCORD_SCHOOLSWP_ROUTINES_URL` (le meme webhook #alerts que les autres watchers). Idem pour `-N8nWebhookUrl` avec `N8N_HYPERFRAMES_WATCHER_URL`. Cela evite de stocker l'URL en clair dans la tache planifiee.

L'URL Discord est deja stockee (mise en place pour le watcher ECC). Si besoin de la (re)stocker, voir `tools/check-ecc-version/README.md` section "Stockage URL Discord".

## Securite — pas de GITHUB_TOKEN

Le script ne lit **jamais** `GITHUB_TOKEN` depuis l'environnement (cf. memoire interne `feedback_github_token_env_override` : cette var ecrase le keyring `gh`). L'API publique non authentifiee plafonne a 60 req/h, largement suffisant pour un poll hebdo. Pour plus de marge de rate-limit, passer un token explicite via `-GithubToken` (jamais via env var).

## Comportement

1. GET `https://api.github.com/repos/<repo>/commits?path=<path>&per_page=1` : dernier commit touchant le path.
2. Extraction SHA (court 12), date, auteur, message, lien html.
3. Comparaison SHA vs baseline.
4. Output rapport Markdown + POST Discord/n8n si nouveau commit.

## Exit codes

- 0 : OK, aucun nouveau commit
- 1 : erreur (API injoignable, path inexistant, repo prive)
- 2 : nouveau commit detecte (action requise)

## Frequence recommandee

**Hebdomadaire** (lundi 10h Paris), aligne sur les autres watchers. Si le launch est actif et que tu veux reagir plus vite, passer a quotidien — l'API publique encaisse sans probleme.

## Wrap n8n (Sheet log + Telegram) — ACTIF

Workflow n8n `[Prod] Webhook > Sheets+Telegram: HyperFrames Launch Watcher` (id `NsGg0qKZhkVN3PKV`, actif).

A chaque run, le PS1 POST son payload vers le webhook `https://schoolswp-n8n.wp1.host/webhook/hyperframes-launch-watcher` (URL dans l'env var user `N8N_HYPERFRAMES_WATCHER_URL`). Le workflow :

1. **Log Google Sheet** (chaque run, heartbeat + trace) : [schoolsWP - HyperFrames Launch Watch Log](https://docs.google.com/spreadsheets/d/1DEbxpxCtI5SF6usNIAH-ibMfQ7w_eapOkg_hbzeIeqI/edit). Colonnes : checked_at, repo, path, sha_current, sha_baseline, changed, commit_date, author, message, html_url.
2. **Telegram** (seulement si `changed=true`) : alerte sur le chat `1020689775` via le bot `schoolswp_yt_bot` (meme canal que les alertes infra n8n).

**Repartition des canaux** : Discord reste gere en direct par le PS1 (POST `DISCORD_SCHOOLSWP_ROUTINES_URL`, pas de secret dans n8n). n8n ajoute Sheet + Telegram. Le log Sheet est independant d'un echec Telegram (la reponse webhook part apres le log).

Le wrap est automatique des que `N8N_HYPERFRAMES_WATCHER_URL` est dans l'env (deja pose). Pour desactiver le wrap sans toucher au reste : retirer l'env var, ou desactiver le workflow n8n.

## Cron Windows Task Scheduler

Pre-requis : env var user `DISCORD_SCHOOLSWP_ROUTINES_URL` deja stockee (faite pour le watcher ECC).

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Unrestricted -NoProfile -File `"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-hyperframes-launch\check.ps1`" -ReportFile `"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-hyperframes-launch\reports\hyperframes-launch-watch.md`""

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 10am

$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd -RunOnlyIfNetworkAvailable

Register-ScheduledTask -TaskName "HyperFrames launch watcher hebdo" -Action $action -Trigger $trigger -Settings $settings -Force
```

Verification :

```powershell
Get-ScheduledTask -TaskName "HyperFrames launch watcher hebdo" | Get-ScheduledTaskInfo
```

Test immediat :

```powershell
Start-ScheduledTask -TaskName "HyperFrames launch watcher hebdo"
Start-Sleep -Seconds 8
Get-ScheduledTaskInfo -TaskName "HyperFrames launch watcher hebdo" | Select-Object LastRunTime, LastTaskResult, NextRunTime
```

`LastTaskResult` egal 0 : succes (pas de nouveau commit). 2 : nouveau commit (normal, l'alerte Discord est partie).

Suppression si besoin :

```powershell
Unregister-ScheduledTask -TaskName "HyperFrames launch watcher hebdo" -Confirm:$false
```

## Mise a jour de la baseline

Quand un nouveau commit est detecte et pris en compte, mettre a jour `.baseline.json` (`sha` + `date` + `set_at`) avec le commit le plus recent, sinon l'alerte se redeclenche a chaque run.

## Limites connues

- Surveille uniquement le dernier commit touchant le path (pas l'historique complet entre deux runs). Si plusieurs commits tombent entre deux checks, seul le plus recent est rapporte — le lien GitHub permet de voir le delta complet.
- Pas de detection de suppression du dossier (si le path disparait, exit 1 "aucun commit trouve").
- Repo prive non supporte sans `-GithubToken`.

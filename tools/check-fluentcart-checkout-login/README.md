# FluentCart Checkout Login watcher

Surveille le repo public **PineDigitalCo/fluentcart-checkout-login**, un mini-plugin communautaire qui ajoute un login dans le checkout FluentCart. Plugin "vibe-coded", immature : pas de release, pas de tests, pas de CI. Le but de ce watcher est de detecter toute evolution importante et de signaler si le plugin devient plus fiable, plus risque, plus interessant a tester, ou pertinent pour un contenu schoolsWP.

Pattern calque sur tools/check-hyperframes-launch/ (API GitHub publique, aucun clone local).

## Ce qui est surveille

- Nouveaux commits (SHA HEAD) et activite de push
- Modification du ZIP distribue (hash blob)
- Apparition de fichiers source hors ZIP (PHP / JS / CSS traces directement)
- Publication de releases et de tags
- Modification du README et changement de version (Stable tag readme + header en deep scan)
- Apparition d'un changelog
- Mouvement sur les issues et PR
- Ajouts / suppressions / modifications de fichiers
- Mots-cles dans les messages de commit : login, checkout, REST/API/nonce, securite, compatibilite, fix
- En deep scan : fonctions dangereuses, URLs externes en dur, marqueurs de couplage FluentCart, echappement

## Fichiers du dossier

| Fichier        | Role                                                               |
| -------------- | ------------------------------------------------------------------ |
| check.ps1      | Le watcher (compatible PowerShell 5.1 et 7+)                       |
| .baseline.json | Etat fige, compare a chaque run                                    |
| fiche-repo.md  | Fiche d'evaluation du plugin (scorecard, checklist technique)      |
| history.md     | Historique append-only, une entree par changement detecte          |
| reports/       | Rapports Markdown 6 sections, ecrits a chaque run avec -ReportFile |

## Usage

```powershell
.\check.ps1                                              # check, compare a la baseline (exit 2 si changement)
.\check.ps1 -ReportFile "reports\2026-XX-XX.md"          # ecrit le rapport
.\check.ps1 -DeepScan                                     # telecharge le ZIP, audit code automatique
.\check.ps1 -DeepScan -ReportFile "reports\audit.md"      # audit complet ecrit
.\check.ps1 -UpdateBaseline                               # fige l'etat courant comme nouvelle baseline (apres prise en compte)
.\check.ps1 -Init                                         # (re)capture la baseline sans diff
```

Repo par defaut : PineDigitalCo/fluentcart-checkout-login (modifiable via -Repo).

**Fallback env var (recommande)** : si -WebhookUrl n'est pas fourni, le script lit automatiquement la variable d'environnement user DISCORD_SCHOOLSWP_ROUTINES_URL. Idem pour -N8nWebhookUrl avec N8N_FLUENTCART_CHECKOUT_LOGIN_WATCHER_URL. Cela evite de stocker l'URL en clair dans les arguments de la tache planifiee.

## Stockage URL Discord (a faire une seule fois, deja en place sur cette machine)

Le webhook Discord schoolsWP-Routines (channel #alerts) est stocke en variable d'environnement user persistante (registry HKCU). Une fois set, l'URL est disponible pour toutes les sessions PowerShell et toutes les taches planifiees, sans la retaper ni la commiter.

```powershell
$url = Read-Host "URL Discord webhook schoolsWP-Routines"
[Environment]::SetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", $url, "User")
Remove-Variable url
```

Le Read-Host saisit l'URL dans la console (pas dans la commande ni l'historique git). Verification dans une nouvelle session :

```powershell
[Environment]::GetEnvironmentVariable("DISCORD_SCHOOLSWP_ROUTINES_URL", "User").Length
```

Cette var est partagee avec les autres watchers schoolsWP (ECC, HyperFrames). Pas besoin de la re-set si elle existe deja.

## Exit codes

- 0 : OK, aucun changement depuis la baseline
- 2 : changement detecte (rapport + alerte Discord si webhook present)
- 1 : erreur API (repo prive, renomme, ou rate-limit)

## Comportement

1. Lit l'etat courant via l'API GitHub : infos repo, arbre des fichiers (recursif), commits, releases, issues/PR, et la version depuis le readme brut.
2. Compare a .baseline.json sur toutes les dimensions surveillees.
3. Scanne les messages des nouveaux commits pour les mots-cles sensibles.
4. Optionnel (-DeepScan) : telecharge le ZIP, l'extrait en temp, et audite le code (fonctions dangereuses, URLs externes, couplage FluentCart, echappement). Le temp est nettoye en fin de run.
5. Produit un rapport Markdown en 6 sections (ce qui a change, pourquoi c'est important, impact FluentCart, impact schoolsWP, niveau de risque, recommandation).
6. Note l'evenement dans history.md et POST une alerte Discord/n8n si changement.

La baseline n'est PAS mise a jour automatiquement : un changement continue d'alerter tant que tu ne fais pas -UpdateBaseline. C'est volontaire (tracabilite, pas d'oubli).

## Scoring du risque (heuristique automatique)

| Declencheur                                                   | Risque         | Reco par defaut   |
| ------------------------------------------------------------- | -------------- | ----------------- |
| Fonction dangereuse detectee ou commit "securite"             | eleve          | auditer           |
| Sources hors ZIP, ZIP modifie, fichiers modifies, commit REST | moyen          | auditer           |
| Release, changement de version, changelog                     | moyen          | tester en staging |
| Nouveau commit ou fichiers ajoutes                            | faible-a-moyen | tester en staging |
| Aucun changement                                              | nul            | ignorer           |

Le scoring est indicatif. Ne jamais considerer ce plugin pret pour la production sans audit, quel que soit le score.

## Frequence recommandee

**Hebdomadaire** (lundi 10h Paris). Le repo est jeune et peut rester dormant ou repartir d'un coup. Hebdo capture le signal sans bruit. Passer en quotidien si une vague d'activite demarre.

## Cron Windows Task Scheduler

Pre-requis : env var user DISCORD_SCHOOLSWP_ROUTINES_URL deja stockee (voir plus haut). La tache ne contient pas l'URL en clair.

```powershell
$base = "d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-fluentcart-checkout-login"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Unrestricted -NoProfile -File `"$base\check.ps1`" -ReportFile `"$base\reports\latest.md`""
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 10am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd -RunOnlyIfNetworkAvailable
Register-ScheduledTask -TaskName "FluentCart Checkout Login watcher hebdo" -Action $action -Trigger $trigger -Settings $settings -Force
```

Verification et test immediat :

```powershell
Get-ScheduledTask -TaskName "FluentCart Checkout Login watcher hebdo" | Get-ScheduledTaskInfo
Start-ScheduledTask -TaskName "FluentCart Checkout Login watcher hebdo"
```

LastTaskResult 0 = succes (aucun changement). Le watcher ecrit le rapport meme sans changement ; en cas de changement, exit 2 et alerte Discord.

Suppression :

```powershell
Unregister-ScheduledTask -TaskName "FluentCart Checkout Login watcher hebdo" -Confirm:$false
```

## Quand un changement est detecte

1. Discord push une alerte dans #alerts avec le resume et la reco.
2. Lire le rapport dans reports/ (6 sections).
3. Si code touche : relancer avec -DeepScan pour l'audit automatique, et/ou auditer manuellement / tester en staging.
4. Mettre a jour fiche-repo.md si l'evaluation change (maturite, risque).
5. Une fois le changement pris en compte, refixer la reference : .\check.ps1 -UpdateBaseline

## Limites connues

- Le poll non authentifie est limite a 60 req/h (largement suffisant pour un run hebdo, ~6 appels par run, ~10 en deep scan).
- Le deep scan telecharge et extrait le ZIP a chaque appel : a reserver aux runs ou un changement de code est suspecte.
- Pas de Telegram natif dans le script (le bot token .env local renvoie 401, cf. memoire). Discord webhook est le canal fiable. Telegram reste un fallback manuel si besoin.

## Wrap n8n (optionnel)

Comme les watchers ECC et tutor-docs, on peut router via n8n (Sheets log + multi-canal). Le script POST deja un payload JSON complet sur -N8nWebhookUrl si fourni (champs : date, repo, has_changes, risk, reco, flags, changes, versions, sha, counts). Pas necessaire pour le MVP : le POST Discord direct suffit.

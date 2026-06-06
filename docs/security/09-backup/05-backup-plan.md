# Etape 5 - Plan backup non-negociable

> Date : 2026-05-12. Objectif : garantir qu on peut tout restaurer avant tout hardening.
> Strategie : 3-2-1 (3 copies, 2 supports, 1 hors site).
> Estimation totale : 2-3 heures (en grande partie attente Backblaze + WP Umbrella).

---

## Resume

5 cibles a sauvegarder, 3 deja partiellement couvertes :

| Cible | Couverture actuelle | A ajouter |
|---|---|---|
| WP schoolswp.com | WP Umbrella (v2.23.0) + WPvivid (v0.9.126) actifs cote WP | 2e copie restic vers Backblaze B2 (hors-site chiffree) |
| WP michaelkihl.fr | xCloud snapshot natif | restic vers Backblaze (hors-site) |
| n8n workflows | Workflow [Prod] Schedule > n8n: Workflows Backup vers Drive (mais jwt hardcoded - finding etape 3) | Export local hebdo + restic (deja exporte aujourd hui dans `n8n-snapshot-2026-05-12/`) |
| Vault Obsidian | Aucun backup actif | restic vers Backblaze (1er point critique) |
| Repo schoolswp (Git) | GitHub origin (private) | Mirror Backblaze hebdo (defense-in-depth) |

**Couverture actuelle** : WP a 2 copies (Umbrella + WPvivid), mais toutes 2 sur le meme serveur EasyHoster. Si l hebergeur tombe ou se fait compromettre, les 2 copies tombent ensemble.

**Gap critique** : aucun backup hors-site chiffre. La strategie 3-2-1 n est pas remplie.

---

## Inventaire actuel

### Outils installes

| Outil | Etat | Version |
|---|---|---|
| WP Umbrella plugin | Actif sur schoolswp.com | 2.23.0 |
| WPvivid plugin | Actif sur schoolswp.com + michaelkihl.fr | 0.9.126 |
| xCloud snapshots | Auto cote provider | (managed) |
| Workflow n8n backup | Actif (jwt hardcoded a fixer) | id iXR2tvSfd5L9zE2t |
| restic | **NON installe** (winget v0.18.1 dispo) | - |
| Docker Desktop | Running | 29.4.2 (pour restore drill n8n) |
| WSL2 Ubuntu 24.04 | Disponible | (pour CLI Unix-style si necessaire) |
| WordPress Studio MCP | Connecte, 0 site local pour le moment | - |
| Backblaze B2 compte | **NON cree** | - |

### Snapshot baseline genere aujourd hui

`docs/security/09-backup/n8n-snapshot-2026-05-12/` :
- 65 workflows JSON (1.5 MB total)
- 1 fichier `_credentials-metadata.json` (metadata uniquement, valeurs chiffrees par n8n non exportables)
- 1 fichier `_manifest.json`

C est le **baseline n8n**. Le restore = n8n UI > import JSON par workflow + recreation credentials manuelle (les valeurs chiffrees ne peuvent pas etre exportees via REST API, by design).

---

## Plan d execution

### Phase A - Setup outillage (10 min, manuel)

Actions a faire toi-meme via PowerShell elevée :

```
winget install restic.restic
winget install --id Backblaze.Client (optionnel, GUI B2)
```

Verification :
```
restic version
```

Doit afficher `restic 0.18.1` ou plus recent.

### Phase B - Creation compte Backblaze B2 (15 min, manuel)

1. Ouvre https://www.backblaze.com/sign-up/cloud-storage
2. Cree un compte gratuit (10 GB stockage offert)
3. Une fois connecte, **Buckets > Create a Bucket** :
    - Bucket Name : `schoolswp-backups-2026` (doit etre unique globalement, ajoute suffixe si pris)
    - Files in Bucket are : `Private`
    - Default Encryption : `Enable` (server-side)
    - Object Lock : `Disable` (pour pouvoir purger les vieux backups)
4. **Account > Application Keys > Add a New Application Key** :
    - Name : `restic-schoolswp-2026-05`
    - Allow access to : `Selected Bucket` -> ton bucket
    - Type of Access : `Read and Write`
    - File name prefix : laisse vide (acces complet au bucket)
    - Duration : laisse vide (no expiration, tu rotateras quand tu veux)
5. **Copie keyID et applicationKey** dans 1Password vault sous "backblaze_b2_restic"
6. Note aussi le **Bucket region** (`s3.us-west-002` par ex) et le **Bucket name**

### Phase C - Initialisation restic (10 min, semi-automatique)

Dans PowerShell, charge les credentials B2 dans tes env vars (NE PAS les coller en clair dans un terminal interactif, utilise 1Password CLI ou tape les valeurs apres `=`).

```powershell
$env:B2_ACCOUNT_ID = "<keyID from 1Password>"
$env:B2_ACCOUNT_KEY = "<applicationKey from 1Password>"
$env:RESTIC_REPOSITORY = "b2:schoolswp-backups-2026"
$env:RESTIC_PASSWORD = "<random 32 chars, stocker AUSSI dans 1Password>"
```

**ATTENTION** : `RESTIC_PASSWORD` est la cle qui chiffre les backups cote restic. Si tu la perds, **tu ne peux pas restaurer**. Stocke-la dans 1Password vault "schoolswp-backups" sous "restic_password" + imprime sur papier.

Initialise le repo :

```powershell
restic init
```

Cette commande creee la structure dans B2. Output attendu : `created restic repository <id> at b2:schoolswp-backups-2026`.

Verifie avec :

```powershell
restic snapshots
```

(Vide pour l instant, mais doit afficher la liste sans erreur.)

### Phase D - Premier backup baseline (30-60 min selon connexion, automatique)

Reviens me dire "OK restic init OK" et je generera un script `backup-schoolswp.ps1` qui fait :

1. `restic backup` du repo `projects/schoolswp/` (en excluant `.venv`, `node_modules`, `_archive`, `.next`, `logs/*.log`)
2. `restic backup` du vault Obsidian `D:/MES SITES/SCHOOLSWP.COM/12_Obsidian/schoolsWP/`
3. `restic backup` du snapshot n8n `docs/security/09-backup/n8n-snapshot-YYYY-MM-DD/`
4. `restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6` (politique de retention)
5. `restic check` (verification integrite)

Le script ecrira son log dans `logs/restic-backup-YYYY-MM-DD.log`.

### Phase E - Restore drill (45 min, critique)

3 drills en parallele :

**Drill 1 : Workflow n8n** (le plus rapide, 10 min)

- Demarre un n8n local via Docker :
    ```
    docker run -d --rm -p 5678:5678 -e N8N_ENCRYPTION_KEY=test-only-do-not-use n8nio/n8n:latest
    ```
- Ouvre http://localhost:5678 dans le navigateur, cree l admin local
- Import un workflow depuis `n8n-snapshot-2026-05-12/iXR2tvSfd5L9zE2t__Prod--Schedule---n8n--Workflows-Backup.json`
- Verifier qu il s ouvre, que les nodes sont visibles, que les references credentials existent (mais sont vides = normal)
- Note le temps de restore total dans `RESTORE-RUNBOOK.md`
- Stop le container quand fini : `docker stop $(docker ps -q --filter ancestor=n8nio/n8n:latest)`

**Drill 2 : Repo Git** (1 min)

- Clone depuis le mirror Backblaze local restic vers un dossier `/tmp/restore-test/`
- Verifie que le `.git/` est OK et que les derniers 3 commits sont presents
- Note le temps

**Drill 3 : WP schoolswp.com** (30 min)

C est le drill le plus complexe. Procedure :

1. Telecharge le dernier backup WP Umbrella depuis https://app.wp-umbrella.com (ou WPvivid via wp-admin > WPvivid Backup > Backups List > Download)
2. Le fichier resultant est typiquement un `.zip` ou un `.wpress` (export All-in-One)
3. Via Claude Code : `mcp__wordpress-studio__site_create` nom "schoolsWP-drill-2026-05-12"
4. Tu obtiens un site WordPress local fraichement installe
5. Installe le plugin "All-in-One WP Migration" via le site local
6. Import le fichier `.wpress` telecharge a l etape 1
7. Verifie via `mcp__wordpress-studio__take_screenshot` sur le frontend
8. Test login admin
9. Verifie via WP-CLI :
    ```
    wp option get blogname        # doit retourner "schoolsWP"
    wp post list --post_type=post --posts_per_page=3
    wp db query "SELECT COUNT(*) FROM wp_fc_subscribers"   # FluentCRM contacts
    ```
10. Note le temps total + tout probleme dans `RESTORE-RUNBOOK.md`
11. Supprime le site drill : `mcp__wordpress-studio__site_delete`

### Phase F - Automatisation (15 min, manuel)

Une fois le premier backup + drill OK, configure le scheduling :

```powershell
# Cree une tache planifiee Windows pour backup nightly a 3h00
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument '-NoProfile -File "D:\VS Code\CLAUDE CODE\projects\schoolswp\docs\security\09-backup\backup-schoolswp.ps1"'
$trigger = New-ScheduledTaskTrigger -Daily -At "03:00"
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType S4U
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -RunOnlyIfNetworkAvailable
Register-ScheduledTask -TaskName "schoolswp-restic-backup-nightly" -Action $action -Trigger $trigger -Principal $principal -Settings $settings
```

Pour le drill restore mensuel automatique : a definir plus tard (etape 14 du briefing - calendrier de maintenance).

---

## Politique de retention

Cible : equilibre cout B2 (0.005 $/GB/mois) + fenetre de restore.

```
--keep-daily 7      (1 backup par jour pour les 7 derniers jours)
--keep-weekly 4     (1 backup par semaine pour les 4 dernieres semaines)
--keep-monthly 6    (1 backup par mois pour les 6 derniers mois)
```

Total = 17 snapshots conserves. Si chaque snapshot mute ~500 MB (uploads + DB), cout B2 = ~50 GB * 0.005 = **0.25 $/mois**.

---

## Politique de chiffrement

- **restic** chiffre en AES-256 cote client. La cle `RESTIC_PASSWORD` est dans 1Password.
- **B2** chiffre cote serveur (server-side encryption activee a la creation du bucket).
- **Double chiffrement** : double protection en cas de fuite B2.

---

## Cle de chiffrement : 3 lieux

`RESTIC_PASSWORD` doit etre disponible meme si :
- ton PC brule
- ton 1Password compte est lock-out
- B2 est down

Stocke-la a 3 endroits :

1. **1Password vault "schoolswp-backups"** (principal)
2. **Papier imprime, range dans un coffre physique ou dans un dossier "important" chez toi** (secondaire, offline)
3. **Coffre fort 1Password emergency kit** (si tu as un compte famille 1Password, sinon skip)

Note : meme strategie pour la cle `N8N_ENCRYPTION_KEY` et toute autre cle maitre.

---

## Checklist de validation finale

Avant de passer a l etape 6 du briefing, coche :

- [ ] restic installe (winget) et `restic version` repond OK
- [ ] Compte Backblaze B2 cree avec bucket prive + encryption
- [ ] Application key restic-only cree (R/W, scope bucket)
- [ ] Credentials B2 + RESTIC_PASSWORD dans 1Password
- [ ] RESTIC_PASSWORD aussi sur papier
- [ ] `restic init` reussi, `restic snapshots` repond sans erreur
- [ ] Premier backup baseline run a passe (vault Obsidian + repo schoolswp + n8n snapshot)
- [ ] Drill restore workflow n8n via Docker = OK
- [ ] Drill restore WP schoolswp.com via WordPress Studio = OK
- [ ] Drill restore repo Git via restic = OK
- [ ] `RESTORE-RUNBOOK.md` ecrit avec les temps mesures
- [ ] `RESTORE-RUNBOOK.md` imprime sur papier
- [ ] Tache planifiee Windows pour backup nightly = active
- [ ] Calendrier drill restore mensuel = a definir etape 14

---

## Suite

Une fois validee, on passe a l etape 6 (WP users + admin access) et l etape 7 (Cloudflare + n8n derriere Access).

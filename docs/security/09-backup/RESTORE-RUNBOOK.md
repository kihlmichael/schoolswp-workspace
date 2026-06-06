# RESTORE-RUNBOOK schoolsWP

> A LIRE QUAND TOUT BRULE. Ecrit pour etre suivi alors que tu es stresse a 3h du matin.
> Imprime aussi sur PAPIER. Range a 3 endroits : repo, 1Password vault, dossier physique.
> Derniere mise a jour : 2026-05-12.

---

## Pre-requis (5 min)

Avant TOUT restore, recupere ces 3 valeurs depuis 1Password vault schoolswp-backups :

| Variable | Description |
|---|---|
| B2_ACCOUNT_ID | keyID Backblaze pour l acces restic |
| B2_ACCOUNT_KEY | applicationKey Backblaze |
| RESTIC_PASSWORD | passphrase qui dechiffre les backups |

Si 1Password est inaccessible : la valeur RESTIC_PASSWORD est aussi sur papier dans un coffre physique chez toi. Les B2 credentials sont visibles dans https://secure.backblaze.com/app_keys.htm (connecte-toi a B2 avec ton compte email).

---

## Scenario 1 : Restore complet WP schoolswp.com

**Quand l utiliser** : site compromis, base de donnees corrompue, hebergeur tombe, ou apres incident GDPR.

**Temps estime** : 30-90 min selon taille DB + uploads.

### Option A (recommandee) : restore via WP Umbrella

1. Va sur https://app.wp-umbrella.com (login compte abonnement)
2. Selectionne schoolswp.com dans la liste des sites
3. Backups > selectionne le dernier point de restauration valide (voir colonne Status Success)
4. Clique Restore
5. Suivre l interface WP Umbrella qui handle tout (DB + files + theme + plugins)
6. Verification post-restore (cf section Validation plus bas)

Si WP Umbrella ne marche pas (compte expire, plugin desactive cote WP, ou backup corrompu) : passer a Option B.

### Option B : restore via WPvivid

1. Connecte-toi au panel EasyHoster pour ton compte schoolswp.com
2. cPanel > File Manager > navigue vers wp-content/wpvivid_backup/
3. Cherche le fichier .wpvivid_xxxxx.tar ou .zip le plus recent
4. Telecharge-le sur ton PC
5. Si le site est down, reinstalle WordPress propre sur le meme domaine via EasyHoster > Auto Installer (saute la creation d admin, on va restaurer)
6. Active le plugin WPvivid Backup
7. WPvivid > Upload > upload le fichier telecharge
8. Restore

### Option C : restore via Backblaze B2 (si WP Umbrella + WPvivid tous deux indisponibles)

Le backup B2 ne contient PAS le WP entier (DB + files + uploads + plugins). Il contient uniquement le repo Git + vault Obsidian + n8n workflows. Donc on ne peut PAS restaurer le WP schoolswp.com depuis B2 seul.

Action : ouvre un ticket support EasyHoster + WP Umbrella. Demande copie sauvegarde la plus recente disponible cote provider.

### Validation post-restore WP

Verifications dans wp-admin :

- Login admin : OK ?
- Frontend : page d accueil charge sans erreur ?
- 3 articles aleatoires : OK ?
- FluentCRM > Contacts : nb contacts > 0 ?
- FluentCart > Orders : nb commandes recentes > 0 ?
- Aucun message d erreur dans wp-admin > Tools > Site Health ?

Si tu as WP-CLI sur le serveur (commandes a copier-coller) :

    wp option get blogname
    wp post list --post_type=post --posts_per_page=3
    wp db query "SELECT COUNT(*) FROM wp_fc_subscribers"
    wp plugin list --status=active --field=name

Plugin count doit etre ~54.

---

## Scenario 2 : Restore workflow n8n

**Quand l utiliser** : un workflow specifique a ete supprime, modifie par erreur, ou tu veux verifier qu un workflow exporte le mois dernier reste loadable.

**Temps estime** : 5 min par workflow.

1. Identifie le workflow voulu dans le snapshot (cf n8n-snapshot-YYYY-MM-DD/ dans le repo)
2. Ouvre le fichier JSON correspondant (nom = id__safe-name.json)
3. Va sur https://schoolswp-n8n.wp1.host/workflows (ou ton instance n8n)
4. Import from File (icone en haut a droite) > selectionne le JSON
5. Le workflow est importe avec un nouvel ID (l ancien si conflit reste)
6. Recree les credentials manuellement via l UI n8n (les valeurs chiffrees ne sont pas exportees dans le JSON)
7. Active le workflow si necessaire

### Restore complet de tous les workflows (apres crash n8n)

Si la base n8n est totalement perdue, restore tous les 65 workflows via le script PowerShell :

    $snapshot = "D:\VS Code\CLAUDE CODE\projects\schoolswp\docs\security\09-backup\n8n-snapshot-2026-05-12"
    $apiUrl = "https://schoolswp-n8n.wp1.host"
    $apiKey = "<from 1Password n8n_api_key_mcp>"

    Get-ChildItem "$snapshot\*.json" | Where-Object { $_.Name -notlike "_*" } | ForEach-Object {
        $body = Get-Content $_.FullName -Raw
        Invoke-RestMethod -Method POST -Uri "$apiUrl/api/v1/workflows" `
            -Headers @{ "X-N8N-API-KEY" = $apiKey } `
            -ContentType "application/json" -Body $body
        Write-Output "Imported: $($_.BaseName)"
    }

Important : les workflows sont importes comme NEW (nouveaux IDs), pas comme update des existants. Si tu restaures sur une instance qui a deja certains workflows, tu auras des doublons. Verifie d abord.

---

## Scenario 3 : Restore vault Obsidian

**Quand l utiliser** : le fichier vault Obsidian a ete corrompu, supprime, ou ton PC a brule.

**Temps estime** : 15 min.

1. Sur le nouveau poste, installe Obsidian (https://obsidian.md)
2. Charge les env restic dans PowerShell :

        $env:B2_ACCOUNT_ID = "<from 1Password>"
        $env:B2_ACCOUNT_KEY = "<from 1Password>"
        $env:RESTIC_REPOSITORY = "b2:schoolswp-backups-2026"
        $env:RESTIC_PASSWORD = "<from 1Password>"

3. Liste les snapshots disponibles :

        restic snapshots --path "D:/MES SITES/SCHOOLSWP.COM/12_Obsidian/schoolsWP"

4. Restore le snapshot voulu (par exemple le plus recent) :

        restic restore latest --target "D:/restore-obsidian-test"

5. Ouvre Obsidian, Open folder as vault > selectionne D:/restore-obsidian-test/.../schoolswp
6. Verifie : claude.md, index.md, log.md a la racine du vault sont presents
7. Une fois OK, deplace le restore vers le path final D:/MES SITES/SCHOOLSWP.COM/12_Obsidian/schoolsWP/

---

## Scenario 4 : Restore repo Git schoolswp

**Quand l utiliser** : repo local corrompu, GitHub down, ou tu travailles sur un nouveau PC.

**Temps estime** : 5 min si GitHub OK, 20 min via B2.

### Option A : GitHub origin

    git clone https://github.com/kihlmichael/schoolswp.git
    cd schoolswp

Tu auras besoin de t authentifier via gh CLI ou PAT.

### Option B : restore via Backblaze (si GitHub indisponible)

Charge env restic comme scenario 3 step 2, puis :

    restic snapshots --path "D:/VS Code/CLAUDE CODE/projects/schoolswp"
    restic restore <snapshot-id> --target "D:/restore-schoolswp"

Le .git est inclus dans le backup, donc tu peux re-initier le push vers un nouveau remote si GitHub reste inaccessible :

    cd D:/restore-schoolswp/projects/schoolswp
    git remote -v
    git remote set-url origin <new-remote-url>

---

## Scenario 5 : Compromis VPS / hebergeur

**Quand l utiliser** : tu suspectes une intrusion sur schoolswp.com ou xCloud apps.

**Temps estime** : 1-2 heures pour confinement, plus restore selon scenario 1-4.

### Etapes immediates (premieres 15 min)

1. Couper l acces public :
   - schoolswp.com : Cloudflare > Security > Under Attack mode (challenge JS pour tout visiteur)
   - n8n : Cloudflare Access deny all si configure, sinon WP Umbrella > Site Status > Pause
2. Garder une session SSH/cPanel ouverte (ne pas tout fermer)
3. Snapshot disque cote provider :
   - EasyHoster : ticket support en URGENT pour demander snapshot immediat
   - xCloud : Dashboard > Servers > Backup Now (sinon snapshot)
4. NE PAS REBOOT (perte de la RAM = perte de preuves)
5. Pas de modification des fichiers avant le snapshot

### Investigation (30 min)

- WP : verifier wp_users (utilisateurs ajoutes ?), wp_options (backdoor ?), wp-content/uploads/ (php files ?)
- Logs : EasyHoster access.log + error.log dernieres 24h
- WP Umbrella > Activity feed (login admins recents)
- Comparer plugins/themes avec le manifest etape 2 (02-wp-inventory-schoolswp.md)

### Restore propre (selon decouvertes)

- Si la compromission date de moins de 7j : restore WP via Option A (WP Umbrella point pre-compromis)
- Si datant > 7j : restore + audit manuel ligne a ligne du WP
- Rotation immediate de TOUS les Application Passwords (cf liste etape 2)
- Rotation de TOUS les secrets MCP touchant schoolswp.com (FluentCRM, WP_API_PASSWORD, etc.)

---

## Temps mesures (drill du 2026-05-12)

A remplir lors du premier drill effectif :

| Scenario | Temps measure | Date drill |
|---|---|---|
| Restore workflow n8n (1 unite) | ?? | ?? |
| Restore tous workflows n8n (65) | ?? | ?? |
| Restore vault Obsidian | ?? | ?? |
| Restore repo Git via B2 | ?? | ?? |
| Restore WP via WP Umbrella | ?? | ?? |
| Restore WP via WordPress Studio (drill local) | ?? | ?? |

---

## Maintenance du runbook

A revisiter :

- Apres chaque incident (mettre a jour avec les decouvertes)
- Apres chaque drill mensuel (mettre a jour les temps + procedures changees)
- Apres tout changement majeur (nouveau plugin critique, nouveau backup target, etc.)

## Numeros d urgence

- EasyHoster support : https://www.easyhoster.com/support/ (ticket urgent)
- xCloud support : cherche dans 1Password ou la dashboard
- Cloudflare support : https://dash.cloudflare.com/?to=/:account/support
- Backblaze support : https://www.backblaze.com/help.html
- Anthropic security : security@anthropic.com (incident clef leak)
- Stripe support : compte FluentCart connecte
- Registrar AFNIC (.fr) ou ICANN (.com) pour michaelkihl.fr / schoolswp.com

---

## Si tu ne te souviens de rien d autre

Recupere d abord :

1. RESTIC_PASSWORD (1Password ou papier)
2. Acces 1Password (master password ou recovery code)
3. Acces GitHub (gh auth status, ou recovery codes 2FA)

Le reste est restorable depuis ces 3 acces.

# Adoption ciblée du pattern LLM Wiki — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Corriger les 4 écarts entre le pattern LLM Wiki de Karpathy et l'infrastructure schoolsWP (passerelle Obsidian + mémoire interne), via une routine de lint locale, une carte de propagation, un réflexe de capitalisation et un journal chronologique de la mémoire.

**Architecture:** Cinq blocs. (1) Dégonflage immédiat de `MEMORY.md` sous le plafond de chargement. (2) Journal `LOG.md` de la mémoire interne. (3) Routine de lint : un run Claude Code headless déclenché au logon Windows par un launcher PowerShell bridé à 1×/jour, piloté par un doc de procédure ; le launcher (pas Claude) lit le webhook `.env`, poste sur Discord et écrit le stamp de throttle. (4) SOP passerelle v1.2 (carte de propagation + cas d'usage 3). (5) Synchronisation doc (`CLAUDE.md`, `README.md`).

**Tech Stack:** Markdown, PowerShell 7, Windows Task Scheduler, Claude Code headless (`claude -p`), webhook Discord.

**Spec de référence:** [docs/superpowers/specs/2026-05-22-adoption-pattern-llm-wiki-design.md](../specs/2026-05-22-adoption-pattern-llm-wiki-design.md)

**Raffinement vs spec §3.3:** la spec plaçait le POST Discord dans le run Claude. Le plan le déplace dans le launcher PowerShell. Le run de lint tourne en `--permission-mode acceptEdits` : il ne fait que des éditions de fichiers, jamais de commande système, donc il ne peut pas poster lui-même sur Discord sans se bloquer sur une demande de permission. L'intention de la spec est préservée : notification Discord uniquement s'il y a des flags, webhook lu depuis `.env`, Claude ne lit jamais `.env`.

---

## Note sur le style de ce plan

Ce chantier est du travail documentaire et infrastructure, pas du code testable par pytest. Les étapes suivent le motif **créer/modifier → vérifier** avec commandes exactes et sortie attendue, et non le cycle TDD test-rouge/test-vert. Le projet n'utilise pas Pester ; aucune dépendance de test n'est ajoutée.

## Structure des fichiers

| Fichier | Responsabilité | Versionné |
| --- | --- | --- |
| `<memory>/MEMORY.md` | Index de la mémoire interne (dégonflé + directive `LOG.md`) | Non |
| `<memory>/LOG.md` | Journal chronologique append-only de la mémoire interne | Non |
| `obsidian-bridge/SOP-claude-obsidian-bridge.md` | SOP passerelle v1.2 (carte de propagation, cas d'usage 3) | Oui |
| `obsidian-bridge/SOP-memory-lint.md` | Procédure suivie par le run de lint headless | Oui |
| `tools/scripts/memory-lint-launcher.ps1` | Launcher : throttle, lecture webhook, run Claude, POST Discord | Oui |
| `tools/scripts/install-memory-lint-task.ps1` | Enregistre la tâche planifiée Windows | Oui |
| `obsidian-bridge/README.md` | Doc passerelle (bump version, mention du nouveau SOP) | Oui |
| `CLAUDE.md` | Réflexes passerelle + mention de la routine de lint | Oui |
| `.env.example` | Placeholder `DISCORD_ROUTINES_WEBHOOK` | Oui |

`<memory>` désigne `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory`.

---

## Task 1: Mémoire interne — dégonfler `MEMORY.md` + créer `LOG.md`

Couvre spec §3.1 et §3.2. **Fichiers hors dépôt git : aucun commit pour cette tâche.**

**Files:**
- Modify: `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\MEMORY.md`
- Create: `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\LOG.md`

- [ ] **Step 1: Mesurer la taille actuelle de `MEMORY.md`**

Run :
```powershell
(Get-Item 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\MEMORY.md').Length
```
Attendu : une valeur supérieure à 24986 (au-dessus du plafond de chargement ~24,4 Ko). Noter la valeur.

- [ ] **Step 2: Dégonfler l'index sous 23000 octets**

Règles de dégonflage, à appliquer dans l'ordre :

1. Pour chaque ligne d'index dont la longueur totale dépasse 200 caractères : raccourcir le hook (le texte après le séparateur ` - `) sous ~120 caractères. **Ne jamais modifier la portion `[Titre](fichier.md)`** : le pointeur et le titre restent intacts.
2. Si le fichier dépasse encore 23000 octets : raccourcir les hooks les plus longs restants. Le détail retiré du hook doit déjà figurer (ou être ajouté) dans le corps du fichier topic correspondant, jamais perdu.
3. Ne supprimer aucune ligne d'index, ne supprimer aucun fichier topic.

- [ ] **Step 3: Vérifier la taille après dégonflage**

Run :
```powershell
(Get-Item 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\MEMORY.md').Length
```
Attendu : valeur inférieure à 23000.

- [ ] **Step 4: Ajouter la directive `LOG.md` à l'en-tête de `MEMORY.md`**

Remplacer le bloc d'en-tête. Ancien texte :
```text
> Index des mémoires. Une ligne par fichier topic, hook court : le détail vit dans les fichiers topic, pas ici.
> Plafond de chargement ~24 Ko. Garder chaque ligne brève. Au-delà de ~190 entrées, repenser la structure de l'index.
```
Nouveau texte :
```text
> Index des mémoires. Une ligne par fichier topic, hook court : le détail vit dans les fichiers topic, pas ici.
> Plafond de chargement ~24 Ko. Garder chaque ligne brève. Au-delà de ~190 entrées, repenser la structure de l'index.
> Journal chronologique : LOG.md (même dossier). Appender une entrée à chaque création, mise à jour ou suppression de mémoire. Format : ## [YYYY-MM-DD] type | résumé.
```

- [ ] **Step 5: Créer `LOG.md`**

Créer `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\LOG.md` avec ce contenu exact :
```text
# LOG — Mémoire interne schoolsWP

Journal chronologique append-only de la mémoire interne. Une entrée par création, mise à jour ou suppression de mémoire, et par run de lint.

Format : ## [YYYY-MM-DD] type | résumé — type vaut ingest, update, delete ou lint.
Append-only strict : ne jamais modifier ni supprimer une entrée passée.

## [2026-05-22] lint | initialisation du journal

Création de LOG.md dans le cadre de l'adoption du pattern LLM Wiki (écart 4). Dégonflage simultané de MEMORY.md sous le plafond de chargement (écart 1, passage de lint manuel initial).
```

- [ ] **Step 6: Vérifier**

Run :
```powershell
Test-Path 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\LOG.md'
Select-String -Path 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\MEMORY.md' -Pattern 'Journal chronologique'
```
Attendu : `True`, puis une ligne de correspondance pour la directive. Pas de commit (fichiers hors dépôt).

---

## Task 2: SOP passerelle v1.2 — carte de propagation + cas d'usage 3

Couvre spec §3.4 et §3.5 (volet SOP).

**Files:**
- Modify: `obsidian-bridge/SOP-claude-obsidian-bridge.md`

- [ ] **Step 1: Bumper le frontmatter**

Ancien texte :
```text
version: 1.1
date_creation: 2026-05-04
date_maj: 2026-05-05
```
Nouveau texte :
```text
version: 1.2
date_creation: 2026-05-04
date_maj: 2026-05-22
```

- [ ] **Step 2: Ajouter l'étape carte de propagation dans le cas d'usage 2**

Dans la section `## 3. Cas d'usage 2`, remplacer la liste de procédure. Ancien texte :
```text
1. Claude Code écrit le draft dans `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_type_titre.md`.
2. Le draft utilise le frontmatter standard et un template (`templates/synthese.md`, `templates/decision.md`).
3. Tu (Michaël) relis et arbitres.
4. Si validé, tu copies le fichier dans `00_systeme/claude-code-bridge/outbox-depuis-claude/` du vault.
5. Si tu décides de le promouvoir en zone stable :
```
Nouveau texte :
```text
1. Claude Code écrit le draft dans `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_type_titre.md`.
2. Le draft utilise le frontmatter standard et un template (`templates/synthese.md`, `templates/decision.md`).
3. Claude Code lit `index.md` à la racine du vault (lecture autorisée, cf. section 7) et ajoute au draft une section finale `## Carte de propagation` : d'après l'index, les pages du vault liées au sujet, les pages potentiellement contredites, les pages à mettre à jour si le draft est promu. Si l'index ne permet pas de conclure, l'indiquer explicitement plutôt que d'inventer.
4. Tu (Michaël) relis et arbitres.
5. Si validé, tu copies le fichier dans `00_systeme/claude-code-bridge/outbox-depuis-claude/` du vault.
6. Si tu décides de le promouvoir en zone stable :
```

- [ ] **Step 3: Insérer le cas d'usage 3**

Juste avant la ligne `## 4. Nommage des fichiers transitants`, insérer cette section :
```text
## 3bis. Cas d'usage 3 - capitaliser une analyse de session

Claude Code produit en session une analyse stratégique réutilisable (confrontation, comparaison, arbitrage, synthèse de recherche). Sans capture, elle disparaît dans l'historique de chat.

Procédure :

1. Quand une analyse de ce type est produite, Claude Code propose de la capitaliser.
2. Si tu acceptes, Claude Code écrit l'analyse dans `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_type_titre.md` (type `note` ou `synthese`), avec frontmatter standard.
3. Le draft suit ensuite le cas d'usage 2 à partir de l'étape 3 (carte de propagation, relecture, promotion éventuelle).

Critère de déclenchement : l'analyse a une valeur au-delà de la session courante. Une réponse ponctuelle à une question opérationnelle ne se capitalise pas.

```

- [ ] **Step 4: Vérifier**

Run :
```powershell
Select-String -Path 'obsidian-bridge\SOP-claude-obsidian-bridge.md' -Pattern 'version: 1.2','Carte de propagation','3bis. Cas'
```
Attendu : trois lignes de correspondance.

- [ ] **Step 5: Commit**

```text
git add obsidian-bridge/SOP-claude-obsidian-bridge.md
git commit -m "docs(obsidian-bridge): SOP v1.2 with propagation map and capitalization use case"
```

---

## Task 3: Procédure de lint — `SOP-memory-lint.md`

Couvre spec §3.3 (le doc de procédure que suit le run headless).

**Files:**
- Create: `obsidian-bridge/SOP-memory-lint.md`

- [ ] **Step 1: Créer le doc de procédure**

Créer `obsidian-bridge/SOP-memory-lint.md` avec ce contenu exact :
```text
---
name: SOP - Lint de la mémoire interne schoolsWP
owner: Michaël KIHL
project: schoolsWP
version: 1.0
date_creation: 2026-05-22
status: actif
---

# SOP - Lint de la mémoire interne schoolsWP

Procédure suivie par le run Claude Code headless déclenché par tools/scripts/memory-lint-launcher.ps1. Adoption de l'opération « lint » du pattern LLM Wiki (écart 1).

## 1. Rôle

Contrôle de santé périodique de la mémoire interne Claude Code et des dossiers de transit de la passerelle Obsidian. Auto-corrige le mécanique sans risque, signale le reste.

## 2. Cibles

- Le dossier de la mémoire interne (chemin absolu fourni dans le prompt de lancement). Contient MEMORY.md, LOG.md et les fichiers topic.
- obsidian-bridge/outbox-to-obsidian/ : drafts en attente de transport vers le vault.
- obsidian-bridge/logs/ : journaux quotidiens de la passerelle.

## 3. Loi de sécurité

- Aucune suppression de contenu. Jamais supprimer un fichier topic ni vider une mémoire. Au maximum : raccourcir une ligne d'index, déporter du détail.
- LOG.md append-only. Ne jamais modifier une entrée passée.
- Tout ce qui demande un arbitrage (contradiction, péremption) est SIGNALÉ, jamais corrigé d'office.

## 4. Checklist

### 4.1 Auto-fix (mécanique, sans risque)

| Contrôle | Correction |
| --- | --- |
| MEMORY.md dépasse ~24 Ko (plafond de chargement) | Raccourcir les lignes d'index les plus longues, déporter le détail dans le fichier topic correspondant. Viser ~22 Ko. |
| Ligne d'index de MEMORY.md au-dessus de ~200 caractères | Raccourcir le hook, sans toucher la portion titre et lien. |
| Fichier topic présent dans le dossier mémoire mais absent de l'index MEMORY.md | Ajouter la ligne d'index (titre, lien, hook court). |

### 4.2 Signalement seul (arbitrage Michaël requis)

| Contrôle | Action |
| --- | --- |
| Ligne d'index de MEMORY.md pointant vers un fichier topic inexistant | Flag. |
| Fichier topic sans frontmatter complet (name, description, metadata.type) | Flag. |
| Lien wikilink non résolu dans un topic | Compter et flag (un wikilink non résolu est admis, il marque du travail futur). |
| Deux mémoires en contradiction apparente | Flag, citer les deux fichiers. |
| Mémoire potentiellement périmée (référence un fichier ou flag disparu, TODO probablement clos) | Flag. |
| Draft dans outbox-to-obsidian/ non transporté depuis plus de 14 jours | Flag. |

## 5. Procédure

1. Lire MEMORY.md et lister les fichiers topic du dossier mémoire.
2. Dérouler la checklist 4.1, appliquer les auto-fix.
3. Dérouler la checklist 4.2, collecter les flags.
4. Appender une entrée dans LOG.md (cf. section 6).
5. Écrire le fichier résultat .lint-result.txt dans le dossier mémoire (cf. section 7).

## 6. Entrée LOG.md

Toujours appender, même quand le lint est propre.

En-tête : ## [YYYY-MM-DD] lint | propre, ou ## [YYYY-MM-DD] lint | N fixes, M flags.

Quand il y a des fixes ou des flags, détailler dans le corps, une puce par élément. Exemple :

    ## [2026-05-22] lint | 2 fixes, 1 flag

    - fix : MEMORY.md ramené de 25,2 à 22,0 Ko (8 lignes d'index raccourcies)
    - fix : ajout de l'entrée d'index pour reference_xyz.md (topic orphelin)
    - flag : project_abc.md et project_def.md se contredisent sur un sujet

## 7. Fichier résultat .lint-result.txt

Écrire dans le dossier mémoire. Lu par le launcher pour décider de la notification Discord.

- Si aucun flag : écrire exactement le mot clean (les auto-fix seuls, sans flag, ne déclenchent pas de notification).
- Si au moins un flag : écrire un résumé court (moins de 1900 caractères) destiné à Discord, commençant par « Lint mémoire schoolsWP : » et listant les flags.
```

- [ ] **Step 2: Vérifier**

Run :
```powershell
Select-String -Path 'obsidian-bridge\SOP-memory-lint.md' -Pattern 'Loi de sécurité','Auto-fix','lint-result.txt'
```
Attendu : au moins trois lignes de correspondance.

- [ ] **Step 3: Commit**

```text
git add obsidian-bridge/SOP-memory-lint.md
git commit -m "feat(memory-lint): add lint procedure document"
```

---

## Task 4: Launcher — `.env.example` + `memory-lint-launcher.ps1`

Couvre spec §3.3 (le launcher et la clé webhook).

**Files:**
- Modify: `.env.example`
- Create: `tools/scripts/memory-lint-launcher.ps1`

- [ ] **Step 1: Ajouter la clé webhook dans `.env.example`**

À la toute fin de `.env.example`, après la dernière ligne (le bloc `FLUENTBOARDS`), ajouter :
```text

# ----------------------------------------------------------------------------
# DISCORD ROUTINES — webhook schoolsWP-Routines (channel #alerts)
# ----------------------------------------------------------------------------
# Webhook utilisé par les routines locales (ex : lint de la mémoire interne).
# Discord, paramètres du canal #alerts, Intégrations, Webhooks, copier l'URL.
# Optionnel : si vide, la notification est skippée silencieusement.
DISCORD_ROUTINES_WEBHOOK=
```

- [ ] **Step 2: Créer le launcher**

Créer `tools/scripts/memory-lint-launcher.ps1` avec ce contenu exact :
```powershell
#Requires -Version 7
# ============================================================================
# memory-lint-launcher.ps1
# Lance le lint de la memoire interne schoolsWP, bride a 1x/jour.
# Invocable a la main, ou via la tache planifiee "schoolsWP Memory Lint".
# ============================================================================

$ErrorActionPreference = 'Stop'

# --- Chemins ---
# tools/scripts/ -> racine projet (deux niveaux au-dessus)
$ProjectRoot  = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$MemoryDir    = 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory'
$ProcedureDoc = Join-Path $ProjectRoot 'obsidian-bridge\SOP-memory-lint.md'
$EnvFile      = Join-Path $ProjectRoot '.env'
$StampFile    = Join-Path $MemoryDir '.last-lint'
$ResultFile   = Join-Path $MemoryDir '.lint-result.txt'
$LauncherLog  = Join-Path $MemoryDir '.lint-launcher.log'

function Write-LauncherLog([string]$msg) {
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ss'
    Add-Content -Path $LauncherLog -Value "$ts | $msg" -Encoding utf8
}

# --- Throttle : un seul run par jour ---
$today = Get-Date -Format 'yyyy-MM-dd'
if (Test-Path $StampFile) {
    if ((Get-Content $StampFile -Raw).Trim() -eq $today) {
        Write-LauncherLog 'skip : deja lance aujourd hui'
        exit 0
    }
}

# --- Pre-requis : claude sur le PATH ---
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-LauncherLog 'ERREUR : claude introuvable sur le PATH (pas de stamp, retry au prochain logon)'
    exit 1
}

# --- Pre-requis : procedure de lint presente ---
if (-not (Test-Path $ProcedureDoc)) {
    Write-LauncherLog "ERREUR : procedure introuvable : $ProcedureDoc"
    exit 1
}

# --- Webhook Discord depuis .env (le launcher poste ; Claude ne lit jamais .env) ---
$webhook = ''
if (Test-Path $EnvFile) {
    $line = Get-Content $EnvFile | Where-Object { $_ -match '^\s*DISCORD_ROUTINES_WEBHOOK\s*=' } | Select-Object -First 1
    if ($line) {
        $webhook = ($line -replace '^\s*DISCORD_ROUTINES_WEBHOOK\s*=', '').Trim().Trim('"')
    }
}

# --- Run du lint via Claude Code headless ---
# acceptEdits : auto-accepte les editions de fichiers ; le lint ne fait
# que des editions (pas de commande systeme, pas de web), donc aucun blocage interactif.
Remove-Item $ResultFile -ErrorAction SilentlyContinue
$prompt = @"
Execute le lint de la memoire interne schoolsWP.
Suis STRICTEMENT la procedure decrite dans : $ProcedureDoc
Le dossier de la memoire interne est : $MemoryDir
"@

Write-LauncherLog 'lancement du lint'
Push-Location $ProjectRoot
try {
    & claude -p $prompt --add-dir $MemoryDir --permission-mode acceptEdits
    $exitCode = $LASTEXITCODE
} finally {
    Pop-Location
}

if ($exitCode -ne 0) {
    Write-LauncherLog "ERREUR : lint sorti en code $exitCode (pas de stamp, retry au prochain logon)"
    exit $exitCode
}

# --- Succes : ecrire le stamp de throttle ---
Set-Content -Path $StampFile -Value $today -Encoding utf8 -NoNewline

# --- Notification Discord si flags ---
if ((Test-Path $ResultFile) -and $webhook) {
    $result = (Get-Content $ResultFile -Raw).Trim()
    if ($result -and $result -ne 'clean') {
        if ($result.Length -gt 1900) { $result = $result.Substring(0, 1900) + ' [...]' }
        try {
            $body = @{ content = $result } | ConvertTo-Json -Compress
            Invoke-RestMethod -Uri $webhook -Method Post -ContentType 'application/json' -Body $body | Out-Null
            Write-LauncherLog 'notification Discord envoyee'
        } catch {
            $errMsg = $_.Exception.Message
            Write-LauncherLog "ERREUR notification Discord : $errMsg"
        }
    }
}

Write-LauncherLog 'lint termine OK'
exit 0
```

- [ ] **Step 3: Vérifier la syntaxe du launcher**

Run :
```powershell
$null = [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path 'tools\scripts\memory-lint-launcher.ps1'), [ref]$null, [ref]$null); if ($?) { 'OK syntaxe' }
```
Attendu : `OK syntaxe`.

- [ ] **Step 4: Vérifier `.env.example`**

Run :
```powershell
Select-String -Path '.env.example' -Pattern 'DISCORD_ROUTINES_WEBHOOK'
```
Attendu : une ligne de correspondance.

- [ ] **Step 5: Commit**

```text
git add .env.example tools/scripts/memory-lint-launcher.ps1
git commit -m "feat(memory-lint): add throttled launcher and webhook env key"
```

---

## Task 5: Installeur de tâche planifiée — `install-memory-lint-task.ps1`

Couvre spec §3.3 (enregistrement de la tâche Windows).

**Files:**
- Create: `tools/scripts/install-memory-lint-task.ps1`

- [ ] **Step 1: Créer l'installeur**

Créer `tools/scripts/install-memory-lint-task.ps1` avec ce contenu exact :
```powershell
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
```

- [ ] **Step 2: Vérifier la syntaxe de l'installeur**

Run :
```powershell
$null = [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path 'tools\scripts\install-memory-lint-task.ps1'), [ref]$null, [ref]$null); if ($?) { 'OK syntaxe' }
```
Attendu : `OK syntaxe`.

- [ ] **Step 3: Commit**

```text
git add tools/scripts/install-memory-lint-task.ps1
git commit -m "feat(memory-lint): add scheduled task installer"
```

---

## Task 6: Synchronisation doc — `CLAUDE.md` + `README.md`

Couvre spec §3.5 (volet `CLAUDE.md`) et §6 (mise à jour doc). À faire après la Task 5 : `CLAUDE.md` mentionne la routine qui doit exister.

**Files:**
- Modify: `CLAUDE.md`
- Modify: `obsidian-bridge/README.md`

- [ ] **Step 1: Ajouter les réflexes passerelle dans `CLAUDE.md`**

Dans la section `## Passerelle Obsidian`, juste avant la ligne qui commence par `**Procédure complète**`, insérer :
```text
**Réflexes passerelle** :

- Toute synthèse produite vers `outbox-to-obsidian/` inclut une section `## Carte de propagation` fondée sur l'`index.md` du vault (SOP cas d'usage 2).
- Toute analyse stratégique réutilisable produite en session est proposée à la capitalisation via `outbox-to-obsidian/` (SOP cas d'usage 3).
- La mémoire interne et les dossiers passerelle sont contrôlés par la routine de lint locale (`tools/scripts/memory-lint-launcher.ps1`, déclenchée au logon, bridée à 1×/jour). Procédure : `obsidian-bridge/SOP-memory-lint.md`.

```

- [ ] **Step 2: Mettre à jour la ligne de version SOP dans `CLAUDE.md`**

Ancien texte :
```text
**Procédure complète** : [obsidian-bridge/SOP-claude-obsidian-bridge.md](obsidian-bridge/SOP-claude-obsidian-bridge.md) (v1.1, MAJ 2026-05-05 avec exception 8.2 et 8.3).
```
Nouveau texte :
```text
**Procédure complète** : [obsidian-bridge/SOP-claude-obsidian-bridge.md](obsidian-bridge/SOP-claude-obsidian-bridge.md) (v1.2, MAJ 2026-05-22 : carte de propagation et cas d'usage 3).
```

- [ ] **Step 3: Mettre à jour la note Workspace Hygiene sur `MEMORY.md`**

Dans la section `## Workspace Hygiene`, remplacer la note sur la mémoire interne. Ancien texte :
```text
**Mémoire interne Claude Code** : le fichier MEMORY.md du workspace `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\` dépasse le plafond de chargement de 24,4 KB (25,2 KB) et est tronqué — des entrées d'index ne sont plus lues. À assainir : raccourcir les lignes d'index sous ~200 chars et déporter le détail dans les fichiers topic.
```
Nouveau texte :
```text
**Mémoire interne Claude Code** : `MEMORY.md` (dans `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\`) a été dégonflé sous le plafond de chargement et est maintenu par la routine de lint locale (cf. section Passerelle Obsidian). Le journal chronologique vit dans `LOG.md` du même dossier.
```

- [ ] **Step 4: Mettre à jour `obsidian-bridge/README.md`**

Bumper le frontmatter. Ancien texte :
```text
version: 1.0
date_creation: 2026-05-04
phase: 1
```
Nouveau texte :
```text
version: 1.1
date_creation: 2026-05-04
phase: 1
```

Puis, dans le bloc `## 3. Structure`, ajouter la ligne du nouveau SOP. Ancien texte :
```text
├── SOP-claude-obsidian-bridge.md   (versionné)
├── .gitignore                      (versionné)
```
Nouveau texte :
```text
├── SOP-claude-obsidian-bridge.md   (versionné)
├── SOP-memory-lint.md              (versionné)
├── .gitignore                      (versionné)
```

Puis, dans la section `## 6. Documentation associée`, après la ligne `Procédure complète`, ajouter :
```text
- Procédure de lint mémoire : [SOP-memory-lint.md](SOP-memory-lint.md)
```

- [ ] **Step 5: Vérifier**

Run :
```powershell
Select-String -Path 'CLAUDE.md' -Pattern 'Réflexes passerelle','SOP-memory-lint','MAJ 2026-05-22'
Select-String -Path 'obsidian-bridge\README.md' -Pattern 'version: 1.1','SOP-memory-lint.md'
```
Attendu : trois correspondances pour `CLAUDE.md`, deux pour `README.md`.

- [ ] **Step 6: Commit**

```text
git add CLAUDE.md obsidian-bridge/README.md
git commit -m "docs: wire memory lint routine into CLAUDE.md and bridge README"
```

---

## Task 7: Installation + run de validation

Recette d'acceptation. **Aucun commit** : cette tâche exécute des scripts, elle ne modifie pas de fichier du dépôt.

**Files:** aucun (exécution et vérification).

- [ ] **Step 1: Renseigner le webhook dans `.env` (manuel, Michaël)**

Dans le fichier `.env` local (non versionné), renseigner `DISCORD_ROUTINES_WEBHOOK` avec l'URL du webhook `schoolsWP-Routines` (channel `#alerts`). Si la clé reste vide, la notification Discord sera simplement skippée et le reste du lint fonctionnera.

- [ ] **Step 2: Installer la tâche planifiée**

Run :
```powershell
pwsh -NoProfile -ExecutionPolicy RemoteSigned -File tools\scripts\install-memory-lint-task.ps1
```
Attendu : `Tache 'schoolsWP Memory Lint' enregistree (trigger AtLogOn).`

- [ ] **Step 3: Vérifier que la tâche existe**

Run :
```powershell
Get-ScheduledTask -TaskName 'schoolsWP Memory Lint' | Select-Object TaskName, State
```
Attendu : une ligne avec `TaskName = schoolsWP Memory Lint` et `State = Ready`.

- [ ] **Step 4: Premier run manuel du lint**

Supprimer un éventuel stamp résiduel puis lancer le launcher :
```powershell
Remove-Item 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\.last-lint' -ErrorAction SilentlyContinue
pwsh -NoProfile -ExecutionPolicy RemoteSigned -File tools\scripts\memory-lint-launcher.ps1
```
Attendu : le script se termine sans se bloquer. Vérifier le code de sortie :
```powershell
$LASTEXITCODE
```
Attendu : `0`.

- [ ] **Step 5: Vérifier les effets du lint**

Run :
```powershell
$m = 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory'
Get-Content (Join-Path $m '.last-lint')
Get-Content (Join-Path $m 'LOG.md') -Tail 12
Get-Content (Join-Path $m '.lint-launcher.log') -Tail 5
```
Attendu : `.last-lint` contient la date du jour ; `LOG.md` se termine par une nouvelle entrée `## [date] lint | ...` ; le log launcher se termine par `lint termine OK`.

- [ ] **Step 6: Vérifier le throttle**

Relancer immédiatement le launcher :
```powershell
pwsh -NoProfile -ExecutionPolicy RemoteSigned -File tools\scripts\memory-lint-launcher.ps1
Get-Content 'C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\.lint-launcher.log' -Tail 1
```
Attendu : la dernière ligne du log est `skip : deja lance aujourd hui` (aucun second run le même jour).

- [ ] **Step 7: Vérifier la notification Discord (conditionnel)**

Si `DISCORD_ROUTINES_WEBHOOK` est renseigné dans `.env` et que le run de l'étape 4 a produit des flags (`.lint-result.txt` différent du mot `clean`), vérifier qu'un message est apparu dans le channel Discord `#alerts`. Si `.lint-result.txt` vaut `clean` ou si la clé est vide, aucune notification n'est attendue : c'est le comportement correct.

---

## Self-Review

**1. Couverture de la spec :**

- Spec §3.1 (dégonfler `MEMORY.md`) : Task 1, steps 1 à 3. Couvert.
- Spec §3.2 (`LOG.md` + directive) : Task 1, steps 4 à 6. Couvert.
- Spec §3.3 (routine de lint) : Task 3 (procédure), Task 4 (launcher + `.env.example`), Task 5 (installeur), Task 7 (installation + recette). Couvert.
- Spec §3.4 (carte de propagation) : Task 2, step 2. Couvert.
- Spec §3.5 (réflexe de capitalisation) : Task 2, step 3 (SOP) + Task 6, step 1 (réflexe `CLAUDE.md`). Couvert.
- Spec §6 (inventaire fichiers) : tous les fichiers créés/modifiés apparaissent dans une tâche. Couvert.
- Spec §7 (séquencement) : l'ordre des tâches respecte §3.1+§3.2 puis §3.4+§3.5 puis §3.3, à un raffinement près. La Task 3 (procédure de lint) précède la Task 6 (sync doc) parce que `CLAUDE.md` et `README.md` doivent référencer des fichiers déjà créés.

**2. Placeholders :** aucun `TBD` ni `TODO`. Le seuil « 14 jours » est explicite, le seuil de taille `MEMORY.md` est chiffré (23000 octets), le contenu complet des deux scripts et des trois documents est inline.

**3. Cohérence des types et noms :** `DISCORD_ROUTINES_WEBHOOK`, `memory-lint-launcher.ps1`, `install-memory-lint-task.ps1`, `SOP-memory-lint.md`, la tâche `schoolsWP Memory Lint`, les fichiers `.last-lint`, `.lint-result.txt` et `.lint-launcher.log` sont nommés de façon identique d'une tâche à l'autre. Le format d'entrée `LOG.md` est identique entre Task 1 (création), la directive `MEMORY.md` et le SOP de lint (Task 3, section 6).

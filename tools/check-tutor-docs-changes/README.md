# Tutor LMS docs change watcher

Surveille les changements sur `docs.themeum.com/tutor-lms/` en comparant les hashes MD5 des pages avec ceux stockés dans le vault Obsidian schoolsWP (sprint corpus 2026-05-04).

## Pourquoi

Les 164 pages docs Tutor LMS scrapées dans le vault sont une référence stratégique pour :

- Production des 7 pillars SEO Tier 1 (Native eCommerce, migrations, abonnements, etc.)
- Décisions stack FluentBoards (FluentCart vs Native eCommerce)
- Mapping FluentCRM emails (37 triggers)
- Customisation Kadence + Tutor

**Si Themeum modifie une page** (nouvelle feature, breaking change, deprecation comme Zoom JWT 2023), le corpus vault devient périmé. Le watcher détecte ça pour déclencher un re-scrape ciblé.

## Usage

```powershell
# Path vault via env var (recommande)
$env:VAULT_TUTOR_DOCS_DIR = "D:\path\to\vault\08_sources\plugins-wordpress\tutor-lms\docs"

# Test rapide sur 5 pages
.\check.ps1 -Limit 5

# Verification complete (154 pages non-stub, ~5-8 min)
.\check.ps1

# Avec rapport ecrit
.\check.ps1 -ReportFile "report-2026-XX-XX.md"

# Avec alerte Discord webhook si changements
.\check.ps1 -WebhookUrl "https://discord.com/api/webhooks/..."
```

Path vault peut aussi etre passe en parametre direct si emoji-free :

```powershell
.\check.ps1 -VaultDocsDir "D:\path\to\docs"
```

## Comportement

1. Lit les 164 .md du vault, extrait `url` + `content_hash` du frontmatter.
2. Filtre les 10 pages `is_index_page: true` (stubs, hash basé sur menu auto-généré).
3. Reste : 154 pages content à surveiller.
4. Pour chaque, refetch via `defuddle parse url -m -o tmp.md`, recompute MD5 first 10 chars.
5. Compare avec le hash vault.
6. Output rapport Markdown + POST Discord si webhook fourni ET changements détectés.

**Logique de stub identique au scrape v3** : la fonction `Test-IsIndexPage` détecte si le content scrape est un dump de menu Themeum (signature `tutor-1.svg` ou ratio liens/content > 50 %), auquel cas le content est remplacé par le même stub que le scrape original avant calcul du hash, ce qui rend la comparaison fiable.

## Exit codes

- **0** : OK, aucun changement
- **1** : erreurs scrape sur certaines URLs
- **2** : changements détectés (utile pour cron qui agit selon code)

## Fréquence recommandée

**Mensuel** (1er du mois). Tutor LMS publie ~1-2 pages doc par mois, parfois moins. Plus fréquent = bruit pour rien.

## Cron / routine

3 options pour automatiser :

### Option A - Windows Task Scheduler (local, simple)

```text
Action : powershell.exe
Arguments : -ExecutionPolicy Unrestricted -File "d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\check-tutor-docs-changes\check.ps1" -ReportFile "d:\reports\tutor-watch.md"
Trigger : Mensuel, 1er du mois 09:00
```

### Option B - Skill schedule (remote, demande accès vault depuis box remote)

Pas applicable en l'état car le vault est local D:\. Devrait synchroniser le vault ailleurs.

### Option C - Manuel post-sprint

Exécuter à la main 1 fois par mois après revue du corpus. Acceptable pour MVP.

## Sortie type

```markdown
# Tutor LMS docs change watcher - 2026-XX-XX HH:MM

- **Pages verifiees** : 154 / 154
- **Erreurs scrape** : 0
- **Changements detectes** : 2

## Pages modifiees

| Fichier vault | URL | Vault hash | New hash |
|---|---|---|---|
| 2026-05-04_tutor-lms-doc_08-native-ecommerce_overview.md | https://... | abc123 | def456 |
| 2026-05-04_tutor-lms-doc_15-divers_content-bank.md | https://... | xyz789 | uvw012 |

**Action recommandee** : re-scrape ces pages via scrape-themeum-docs.ps1 pour produire un nouveau outbox transport.
```

## Limites connues

- Pas de re-scrape automatique si changement détecté (manuel via `scrape-themeum-docs.ps1`).
- Pas de tracking des nouvelles pages ajoutées (uniquement diff sur les 154 existantes). Pour détecter ajouts, re-fetcher la liste racine `docs.themeum.com/tutor-lms/`.
- Webhook Discord stocké en clair dans le paramètre. Pour secret durable, utiliser env var ou .credentials.

## Extensions futures possibles

- Mode `--auto-rescrape` qui déclenche `scrape-themeum-docs.ps1` sur les URLs modifiées
- Mode `--detect-new` qui re-fetche la liste racine et compare avec le vault
- Export JSON state pour Sheets dashboard (cohérence avec `reference_routine_plugins_snapshot.md`)

## Wrap n8n (déployé 2026-05-05)

Le check.ps1 peut POSTer son rapport JSON à un workflow n8n qui orchestre les notifs (Discord, Sheets log, Telegram, etc.) sans modifier le script.

### Workflow déployé

- **ID** : `np4OG9UGDCGWaK4H`
- **Nom** : `[InDev] Webhook > Discord: Tutor LMS Docs Watcher`
- **Endpoint** : `https://schoolswp-n8n.wp1.host/webhook/tutor-lms-docs-watcher`
- **5 nodes** : Webhook receiver → IF changes_count > 0 → Build Discord embed → POST Discord webhook → Respond OK
- **Statut** : inactive par défaut (à activer après config Discord URL)

### Configuration côté n8n (à faire 1 fois)

1. Ouvrir le workflow dans `https://schoolswp-n8n.wp1.host`
2. Cliquer sur le node **POST Discord webhook**
3. Remplacer `REPLACE_WITH_DISCORD_WEBHOOK_URL` par ton URL Discord (channel #alerts ou équivalent)
4. Sauvegarder
5. Activer le workflow (toggle Active en haut à droite)

### Usage côté PS1

```powershell
.\check.ps1 -N8nWebhookUrl "https://schoolswp-n8n.wp1.host/webhook/tutor-lms-docs-watcher"
```

Le PS1 POSTe un payload JSON :

```json
{
  "date": "2026-XX-XX HH:MM",
  "source": "tutor-lms-docs-watcher",
  "checked": 154,
  "errors": 0,
  "changes_count": 2,
  "changed_pages": [
    {
      "file": "...",
      "url": "https://docs.themeum.com/...",
      "old_hash": "abc123",
      "new_hash": "def456"
    }
  ]
}
```

n8n filtre via IF (changes_count > 0), construit un embed Discord riche (titre + liste 5 premières URLs + footer stats), POSTe au webhook Discord configuré.

### Avantages du wrap n8n

- **Centralisation** : toutes les routines schoolsWP visibles dans le hub n8n
- **Modularité** : changer la destination notif (Discord → Telegram → Sheets log → multi) sans toucher au PS1
- **Historique** : n8n stocke les exécutions (debug, trends, audit)
- **Enrichissement futur** : ajouter Sheets append pour graph mensuel, Notion log, etc.

### Cron / déclenchement

Le PS1 reste lancé localement (vault `D:\` non accessible depuis n8n cloud). Options :

- **Manuel** : exécution mensuelle après revue corpus
- **Windows Task Scheduler** : 1er du mois 9h, action = `powershell.exe -File check.ps1 -N8nWebhookUrl "..."`
- **NemoClaw / box remote** : non applicable tant que vault local

### Combo recommandé

```powershell
# Cron Windows mensuel (Task Scheduler 1er du mois 9h)
$env:VAULT_TUTOR_DOCS_DIR = "D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\08_sources\plugins-wordpress\tutor-lms\docs"
.\check.ps1 -N8nWebhookUrl "https://schoolswp-n8n.wp1.host/webhook/tutor-lms-docs-watcher" -ReportFile "d:\reports\tutor-watch-$(Get-Date -Format 'yyyyMM').md"
```

Si changements → Discord alerte (via n8n) + rapport Markdown local archivé.


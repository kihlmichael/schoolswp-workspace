# SOP — Pinterest Pipeline schoolsWP

> Automatisation de la creation et publication de pins Pinterest via Canva + Claude Code.
> Version : 1.0 | Date : 2026-04-03 | Auteur : Michael KIHL
> Source de verite operationnelle. Toute modification passe par ce fichier.

---

## 1. Objectif

Produire et publier 20-50 pins Pinterest par semaine pour schoolsWP, avec :
- Claude Code comme orchestrateur technique
- Canva comme moteur de visuels (2 chemins : Enterprise Autofill OU assiste)
- Pinterest API v5 pour la publication
- JSON versionne comme source d'etat
- Validation humaine obligatoire avant publication

Cadence cible : ~2h/semaine en regime de croisiere.

---

## 2. Architecture

```
Source contenu (articles schoolsWP)
   |
   v
Claude Code genere le brief
   |
   v
pins_queue.json (source d'etat)
   |
   +---> Chemin A : Canva Enterprise Autofill (si dispo)
   |         |
   +---> Chemin B : Canva assiste (MCP export/generation + validation humaine)
   |
   v
Export image (PNG 1000x1500)
   |
   v
Validation humaine (#2)
   |
   v
Upload media Pinterest (POST /media)
   |
   v
Creation Pin (POST /pins)
   |
   v
Validation humaine (#3) OU auto-publish si pre-approuve
   |
   v
Sync analytics Pinterest
   |
   v
Rapport / iteration
```

### Briques techniques

| Brique | Outil | Methode |
| --- | --- | --- |
| Source contenu | Google Sheets (articles schoolsWP) | Sheet `schoolswp-urls-fr-post` (ID: `11hA3JhbL6qxQhIAA_MT58NKs978-iZLU6rglCib30Aw`) |
| Generation brief | Claude Code (Claude Sonnet) | Prompt structure → JSON brief |
| Visuel Canva (A) | Canva Connect API — Autofill | `list-brand-templates` → `create-autofill-job` → `get-autofill-job` |
| Visuel Canva (B) | Canva MCP | `generate-design` / `generate-design-structured` + `export-design` |
| Export image | Canva API/MCP | `export-design` (PNG, async, URL expire 24h) |
| Publication | Pinterest API v5 | `POST /media` → upload → `POST /pins` |
| Analytics | Pinterest API v5 | `GET /pins/{id}/analytics` + `GET /user_account/analytics/top_pins` |
| Orchestration | Claude Code | Hooks + MCP + scripts |
| Etat | `pins_queue.json` | JSON versionne dans le repo |

---

## 3. Machine d'etat (stricte)

```
idea
  → brief_generated
    → brief_approved          ← VALIDATION HUMAINE #1
      → design_generated
        → design_approved     ← VALIDATION HUMAINE #2
          → exported
            → publish_approved ← VALIDATION HUMAINE #3
              → published
                → analytics_synced
                  → archived
```

**Regles absolues :**
- Aucun script ne peut sauter un etat
- `publish_approved` = `true` obligatoire avant toute publication
- `content_hash` recalcule a chaque modification — detecte les modifications non validees
- Un pin `published` ne peut jamais revenir a `design_generated` directement
- Tout changement d'etat est logue dans `logs/state-transitions.log`

### Mapping avec les statuts Pinterest Strategy System

| Machine d'etat (technique) | Statut editorial (Sheets) |
| --- | --- |
| `idea` | Idee |
| `brief_generated` / `brief_approved` | Brief |
| `design_generated` / `design_approved` | En creation / A valider |
| `exported` / `publish_approved` | Planifie |
| `published` | Publie |
| `archived` | Archive |

---

## 4. Arborescence fichiers

```
systems/pinterest-pipeline/
  SOP.md                      ← ce fichier
  CLAUDE.md                   ← regles Claude Code pour ce sous-systeme
  README.md                   ← (non cree — inutile, SOP suffit)
  /data
    pins_queue.json           ← file de production (source d'etat)
    boards.json               ← mapping board_key → board_id Pinterest
    templates.json            ← mapping template_key → canva_template_id
  /schemas
    pin.schema.json           ← JSON Schema de validation
  /briefs
    YYYY-MM-DD-pin-XXX.json   ← brief fige par pin
  /exports
    pin-XXX.png               ← image exportee prete a publier
  /analytics
    YYYY-MM-DD.json           ← snapshot analytics quotidien
  /logs
    state-transitions.log     ← log des transitions d'etat
    publish.log               ← log des publications Pinterest
  /src
    state.py                  ← machine d'etat + transitions
    brief.py                  ← generation de briefs via Claude
    canva.py                  ← interactions Canva (MCP ou API)
    pinterest.py              ← upload media + creation pin + analytics
    validate.py               ← validation JSON + regles metier
    analytics.py              ← sync + snapshots analytics
```

---

## 5. Schema JSON — Pin

```json
{
  "id": "pin-001",
  "source_type": "article",
  "source_id": "post-123",
  "source_url": "https://schoolswp.com/article-slug",
  "title": "Titre Pinterest (40-100 car.)",
  "description": "Description SEO Pinterest (150-300 car.)",
  "alt_text": "Description image pour accessibilite",
  "overlay_text": "Texte sur le visuel (3-7 mots)",
  "destination_url": "https://schoolswp.com/landing",
  "board_key": "seo-wordpress",
  "board_id": null,
  "template_key": "pin-v1-a",
  "canva_mode": "assisted",
  "canva_template_id": null,
  "canva_design_id": null,
  "export_format": "png",
  "image_path": null,
  "status": "idea",
  "brief_approved": false,
  "design_approved": false,
  "publish_approved": false,
  "published_pin_id": null,
  "analytics_last_sync_at": null,
  "content_hash": null,
  "pillar": "SEO",
  "keyword_primary": "rank math wordpress",
  "keywords_secondary": ["plugin SEO", "optimiser SEO WordPress"],
  "pin_id_editorial": "PIN-SEO-001",
  "angle": "tutoriel pas a pas",
  "cta": "Decouvre le guide complet sur schoolsWP.com",
  "created_at": "2026-04-03T10:00:00Z",
  "updated_at": "2026-04-03T10:00:00Z"
}
```

### Champs critiques (ne jamais omettre)

| Champ | Pourquoi |
| --- | --- |
| `status` | Gouverne le workflow — bloque les actions prematurees |
| `publish_approved` | Gate de securite — aucune publication sans `true` |
| `content_hash` | Detecte les modifications non validees (SHA-256 du brief) |
| `published_pin_id` | Anti-doublon — verifie avant publication |
| `board_key` + `board_id` | Routing — `board_key` humain, `board_id` technique |

---

## 6. Design specs (visuels)

Source : memoire projet + brand rules schoolsWP.

| Spec | Valeur |
| --- | --- |
| Format | 1000x1500 px (ratio 2:3) |
| Marge | 50 px |
| Zone texte | Tiers superieur |
| Couleur accent | `#00D400` (barres, CTA, soulignements — jamais en fond plein) |
| Couleur secondaire | `#00A100` |
| Couleur accent rose | `#E668D4` |
| Fond sombre | `#12111F` |
| Fond clair | `#FAFBFD` |
| Typo titres | Montserrat Bold (Canva) / Nunito Sans Bold 700 (web) |
| Typo corps | Open Sans (Canva) / Roboto Regular 400 (web) |
| Taille min texte | 30pt |
| Headline | 3-7 mots, chiffres dans les titres (CTR+) |

---

## 7. Boards Pinterest schoolsWP

10 boards definis. Mapping `board_key` → nom Pinterest :

| board_key | Nom Pinterest | Pilier |
| --- | --- | --- |
| `wordpress-guides` | WordPress : guides et bonnes pratiques | WordPress |
| `seo-wordpress` | SEO WordPress : guides et optimisation | SEO |
| `lms-wordpress` | LMS WordPress : creer et vendre des formations en ligne | LMS |
| `crm-email` | CRM et email marketing WordPress | CRM |
| `automatisation` | Automatisation WordPress : workflows et gain de temps | Automatisation |
| `plugins` | Plugins WordPress : tests, avis et comparatifs | Plugins |
| `ecommerce` | E-commerce WordPress : WooCommerce et vente en ligne | Ecommerce |
| `freelance` | Freelance et business WordPress | Freelance |
| `strategie-contenu` | Strategie de contenu WordPress : calendrier editorial et clusters SEO | Formation |
| `coulisses` | schoolsWP Coulisses : behind the scenes | Coulisses |

Les `board_id` Pinterest sont a remplir dans `data/boards.json` apres creation du compte.

---

## 8. Workflow V1 (7 jours — hybride assiste)

### Jour 1 — Fondations Canva + Pinterest

- [ ] Creer 3 templates Canva fixes (tutoriel, comparatif, listicle) au format 1000x1500
- [ ] Appliquer les design specs (couleurs, typo, zones texte)
- [ ] Creer les 10 boards Pinterest avec descriptions SEO (copier depuis pinterest-strategy-system.md)
- [ ] Remplir `data/boards.json` avec les `board_id` reels
- [ ] Remplir `data/templates.json` avec les IDs Canva

### Jour 2 — Etat et validation

- [ ] Creer `data/pins_queue.json` (vide, structure validee)
- [ ] Creer `schemas/pin.schema.json` (JSON Schema)
- [ ] Coder `src/state.py` (machine d'etat + transitions + logs)
- [ ] Coder `src/validate.py` (validation JSON + regles metier)

### Jour 3 — Generation de briefs

- [ ] Coder `src/brief.py` (Claude genere : title, description, alt_text, overlay_text, board_key, template_key, keywords)
- [ ] Prompt systeme contraint (pas de "creatif libre", output JSON strict)
- [ ] Tester sur 5 articles existants
- [ ] Valider manuellement les 5 briefs

### Jour 4 — Canva (chemin B assiste)

- [ ] Tester Canva MCP : `generate-design` avec prompt + `export-design`
- [ ] Si MCP OK : integrer dans `src/canva.py`
- [ ] Si MCP KO : workflow manuel (Claude prepare brief → humain ouvre Canva → exporte)
- [ ] Tester `export-design` : format PNG, telecharger avant expiration 24h, stocker dans `/exports`

### Jour 5 — Pinterest API

- [ ] Coder `src/pinterest.py` :
  - `register_media_upload()` — POST /media
  - `upload_media_file()` — upload image
  - `create_pin()` — POST /pins avec board_id, title, description, alt_text, media_source
- [ ] Tester en sandbox Pinterest (mode test)
- [ ] Verifier : mapping board OK, pas de doublon, lien correct

### Jour 6 — Analytics

- [ ] Coder `src/analytics.py` :
  - `fetch_pin_analytics(pin_id)` — GET /pins/{id}/analytics
  - `fetch_top_pins()` — GET /user_account/analytics/top_pins
  - `snapshot_daily()` — sauvegarde dans `/analytics/YYYY-MM-DD.json`
- [ ] Planifier un snapshot quotidien

### Jour 7 — Tests complets

- [ ] 5 runs complets en sandbox : brief → design → export → upload → publish
- [ ] Verifier : zero doublon, zero publish sans validation, export OK, mapping board OK
- [ ] Verifier rollback : annuler un pin a chaque etape
- [ ] Documenter les bugs/ajustements dans les logs

---

## 9. Workflow V2 (avec Canva Enterprise — si disponible)

### Pipeline industrialise

```
list-brand-templates
  → get-brand-template-dataset
    → create-autofill-job (variables : overlay_text, cta, url, pilier)
      → poll get-autofill-job (async)
        → export-design (PNG 1000x1500)
          → upload media Pinterest
            → create pin
              → sync analytics
```

### Ajouts V2

- [ ] Scoring automatique des templates gagnants (engagement rate par template)
- [ ] A/B test overlay_text (2 variantes par pin, mesure apres 7 jours)
- [ ] Board routing automatique (pilier → board via `boards.json`)
- [ ] Generation de variantes 1:many (1 article → 5 pins, angles differents)
- [ ] Rapport hebdo : pins a recycler / a booster / templates sous-performants
- [ ] Integration n8n workflow V3 existant (ID: `RQZnUp6C1qC82Q7K`) pour le scheduling

### Ce qu'on ne fait PAS en V2

- Auto-publication sans garde-fou
- Navigateur headless
- Dependance sur features Canva en preview (`get-design-pages` = preview)
- Multi-outils caches dans 12 SaaS

---

## 10. Hooks Claude Code

### SessionStart

Injecter les regles du pipeline :
- Jamais publier si `publish_approved !== true`
- Jamais ecraser un export existant sans bump de version
- Toujours valider le JSON avant action reseau

### PreToolUse

Matcher sur : `Bash`, `mcp__claude_ai_Canva__.*`, futur `mcp__pinterest__.*`

Actions :
- Bloquer tout publish sans validation
- Bloquer toute suppression de fichiers dans `/exports` ou `/data`
- Verifier que le pin est dans l'etat correct avant toute action API

### PostToolUse

Apres `Edit|Write` sur des fichiers du pipeline :
- Validation JSON automatique
- Recalcul du `content_hash`
- Check de coherence machine d'etat

---

## 11. Validations humaines (3 gates)

### Gate 1 — Apres brief (`brief_generated` → `brief_approved`)

Valider :
- [ ] Angle editorial pertinent
- [ ] Overlay text clair et impactant (3-7 mots)
- [ ] URL destination correcte
- [ ] Board cible coherent avec le pilier
- [ ] Template adapte au type de contenu

### Gate 2 — Apres design (`design_generated` → `design_approved`)

Valider :
- [ ] Hierarchie visuelle : titre lisible en premier
- [ ] Lisibilite mobile (texte > 30pt, contraste OK)
- [ ] Coherence branding schoolsWP (couleurs, typo, ton)
- [ ] Absence erreur typo sur le visuel
- [ ] Marge 50px respectee

### Gate 3 — Avant publication (`exported` → `publish_approved`)

Valider :
- [ ] Description SEO complete (150-300 car., mot-cle en premiere phrase)
- [ ] Alt text renseigne
- [ ] Lien destination fonctionnel (pas de 404)
- [ ] Board final confirme
- [ ] Absence de doublon (verifier `published_pin_id` + `content_hash`)

---

## 12. Garde-fous et fallbacks

### Garde-fous

| Garde-fou | Implementation |
| --- | --- |
| Anti-doublon | Verrou sur `source_id` + `template_key` + `content_hash` |
| Anti-publish sauvage | `publish_approved = true` obligatoire |
| Traçabilite | Log de chaque transition d'etat |
| Export local | Image telechargee et stockee AVANT publication |
| Mode dry_run | Flag `--dry-run` sur tous les scripts (simule sans publier) |
| Retry limite | Max 2 retries par etape reseau |
| Hash de contenu | SHA-256 recalcule a chaque modification |

### Fallbacks

| Situation | Fallback |
| --- | --- |
| Pas de Canva Enterprise | V1 hybride assistee (chemin B) |
| Export Canva KO | Pin reste `design_approved`, jamais `publish_approved` |
| Pinterest API KO | Image conservee, erreur loguee, pas de re-publication sans check |
| MCP indisponible | Scripts REST directs |
| Rate limit Pinterest | Queue avec backoff exponentiel |

---

## 13. Integration avec l'ecosysteme existant

### n8n Workflow V3 (ID: RQZnUp6C1qC82Q7K)

Le workflow n8n existant genere deja les copies de pins (5 variations par article) et les logue dans Google Sheets. Ce pipeline Claude Code se branche en aval :
- n8n genere les copies → Sheet `Copie Pins` (ID: `1YSoa-...`)
- Claude Code lit les copies, genere les briefs structures, orchestre Canva + Pinterest

### Google Drive

Dossier Pinterest (ID: `1D10mjPHE_PEab5ajRUq7spoY4gleTSEY`) — synchronise avec les 7 tableaux Sheets du Pinterest Strategy System.

### Google Sheets (7 tableaux)

| Tableau | Role dans le pipeline |
| --- | --- |
| A. Profil & Positionnement | Reference (pas de MAJ auto) |
| B. Suivi des Boards | Sync `boards.json` → Sheet |
| C. Suivi des Pins | Sync `pins_queue.json` → Sheet |
| D. Calendrier editorial | Input : dates de publication |
| E. SEO & Mots-cles | Input : keywords pour les briefs |
| F. Performances / KPI | Output : analytics Pinterest |
| G. Backlog d'idees | Input : idees a transformer en briefs |

---

## 14. Prerequis techniques

### Canva

- [ ] Integration Canva Developer configuree (Developer Portal)
- [ ] MFA active sur le compte Canva
- [ ] Canva MCP connecte dans `.mcp.json` (deja configure dans le workspace)
- [ ] Plan Canva Pro minimum (export qualite + resize)
- [ ] Si Enterprise : acces Autofill + Brand Templates

### Pinterest

- [ ] App Pinterest creee (Developer Portal)
- [ ] OAuth 2.0 configure (authorization code flow)
- [ ] Scopes : `boards:read`, `boards:write`, `pins:read`, `pins:write`, `user_accounts:read`
- [ ] Access token + refresh token stockes dans `.env` (jamais versionnes)
- [ ] Sandbox active pour les tests

### Claude Code

- [ ] MCP Canva operationnel
- [ ] Hooks configures dans `.claude/settings.json`
- [ ] `.env` avec `PINTEREST_ACCESS_TOKEN`, `PINTEREST_REFRESH_TOKEN`, `CANVA_API_KEY`

---

## 15. Budget mensuel

| Poste | Cout |
| --- | --- |
| Canva Pro | 13 EUR/mois |
| Tailwind Advanced (optionnel) | 20 EUR/mois |
| Placid (optionnel, 500 rendus) | 15 EUR/mois |
| Pinterest API | Gratuit |
| Claude Code | Inclus dans l'abonnement |
| **Total** | **33-48 EUR/mois** |

---

## 16. Checklist d'implementation par priorite

### Priorite 1 — Tout de suite

- [ ] Creer 3 templates Canva fixes (1000x1500)
- [ ] Creer les 10 boards Pinterest
- [ ] Definir `pins_queue.json` + JSON Schema
- [ ] Coder la machine d'etat (`state.py`)
- [ ] Ajouter les 3 validations humaines
- [ ] Coder les scripts Pinterest (`pinterest.py`)
- [ ] 3 runs complets en sandbox

### Priorite 2 — Semaine 2

- [ ] Brancher Canva MCP (ou Autofill si Enterprise)
- [ ] Ajouter export automatique
- [ ] Ajouter snapshots analytics quotidiens
- [ ] Ajouter hooks Claude Code
- [ ] Ajouter mode `--dry-run`

### Priorite 3 — Semaine 3+

- [ ] Scoring des performances par template
- [ ] Variantes automatiques (1 article → 5 pins)
- [ ] Reporting hebdo automatise
- [ ] Routing automatique par board/template
- [ ] Integration calendrier editorial Sheets

---

## 17. Limites connues

| Limite | Impact |
| --- | --- |
| Autofill Canva = Enterprise only | Pas de remplissage auto de Brand Templates en solo |
| URL export Canva expire en 24h | Telecharger et stocker immediatement |
| Elements premium Canva | Export peut echouer avec `license_required` |
| Designs vides via API = supprimes apres 7j | Ne pas creer de designs "placeholder" |
| Canva MCP = auth par utilisateur, pas org | Ne pas batir sur un faux compte partage |
| `get-design-pages` = preview | Ne pas mettre au coeur du systeme |
| Pinterest rate limits | Respecter les quotas, backoff exponentiel |

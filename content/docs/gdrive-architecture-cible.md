# Google Drive — Architecture cible schoolsWP

> Document de reference pour la reorganisation du Drive.
> Statut : EN ATTENTE DE VALIDATION
> Date : 2026-02-10

---

## PHASE 2 — Architecture cible

### 2.1 Arborescence racine (6 dossiers)

```
My Drive/
├── 00_Inbox/                          # Point d'entree unique — tout nouveau contenu arrive ici
├── 01_Projets/                        # Tous les projets actifs (1 sous-dossier = 1 projet)
│   ├── schoolsWP/                     # Projet principal (detail section 2.3)
│   └── Mon-Mini-Electro/             # Autre projet (backup WP)
├── 02_Ressources/                     # Outils, methodes, templates transverses (pas projet-specifique)
├── 03_Admin/                          # Admin personnelle : identite, banque, assurances, impots, contrats
├── 04_Personnel/                      # Photos, medical, documents prives
└── 99_Archives/                       # Tout ce qui est cloture, ancien, ou inactif
```

| Dossier | Logique |
|---------|---------|
| `00_Inbox` | Zone tampon unique. Tout nouveau fichier/scan/telechargement va ici. Trie hebdomadaire. |
| `01_Projets` | 1 sous-dossier par projet. Template standard applique a chacun. |
| `02_Ressources` | Outils, methodes, checklists, formations — utilise par TOUS les projets. |
| `03_Admin` | Strictement admin perso. Sous-dossiers par type (identite, banque, factures, impots, contrats, assurances). |
| `04_Personnel` | Photos, medical, documents prives. Isole du pro. |
| `99_Archives` | Projets finis, anciennes versions, backups. Prefixe date de cloture. |

### 2.2 Template projet duplicable

Chaque projet suit cette structure standard :

```
[Nom-Projet]/
├── 00_README                          # Fichier Google Doc : objectif, liens cles, conventions
├── 01_Strategie/                      # Roadmap, positionnement, objectifs, etude de marche
├── 02_Contenu/                        # Tout contenu publie ou a publier
│   ├── 01_Blog/                       # Articles, brouillons, publies
│   ├── 02_Newsletter/                 # Editions, templates, listes
│   ├── 03_YouTube/                    # Scripts, descriptions, metadata
│   └── 04_Reseaux-Sociaux/           # Posts LinkedIn, Facebook, etc.
├── 03_SEO/                            # Audits, mots-cles, suivi positions, clusters
├── 04_Assets/                         # Tout fichier visuel ou de design
│   ├── 01_Branding/                   # Logo, charte, couleurs, fonts
│   ├── 02_Thumbnails/                 # Miniatures YouTube/blog
│   ├── 03_Illustrations/             # Images creees ou achetees
│   ├── 04_Covers/                     # Couvertures articles/episodes
│   └── 05_Sources-Design/            # Fichiers Canva, Figma, PSD editables
├── 05_Marketing/                      # Vente, monetisation, publicite
│   ├── 01_Affiliation/                # Programmes, fiches, stats
│   ├── 02_Publicite/                  # Campagnes ads, copies, visuels
│   └── 03_Partenariats/              # Briefs, contrats, echanges
├── 06_Technique/                      # WordPress, hosting, plugins, configs
├── 07_Automatisation/                 # n8n, scripts, workflows, integrations
├── 08_IA-et-Prompts/                  # Prompts, templates IA, outils LLM
│   ├── 01_Prompts/                    # Prompts classes par usage
│   └── 02_Templates/                  # Templates structurels
├── 09_Veille/                         # Concurrence, inspirations, benchmarks
├── 10_Analytics/                      # KPI, rapports, dashboards, exports
└── 99_Archive/                        # Contenus inactifs du projet
```

### 2.3 Focus schoolsWP — Mapping des orphelins

Tous les dossiers orphelins actuels sont absorbes dans la structure schoolsWP :

| Dossier orphelin actuel | Destination cible | Action |
|---|---|---|
| `blog/` | `01_Projets/schoolsWP/02_Contenu/01_Blog` | Fusionner |
| `newsletter/` | `01_Projets/schoolsWP/02_Contenu/02_Newsletter` | Fusionner |
| `linkedin/` | `01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/LinkedIn` | Deplacer |
| `facebook/` | `01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/Facebook` | Deplacer |
| `medias/` | `01_Projets/schoolsWP/04_Assets` | Fusionner |
| `branding/` | `01_Projets/schoolsWP/04_Assets/01_Branding` | Fusionner |
| `templates/` | `01_Projets/schoolsWP/08_IA-et-Prompts/02_Templates` | Fusionner |
| `concurrence/` | `01_Projets/schoolsWP/09_Veille` | Deplacer |
| `automatisation/` | `01_Projets/schoolsWP/07_Automatisation` | Fusionner |
| `wordpress/` | `01_Projets/schoolsWP/06_Technique` | Fusionner |
| `ia_llm_seo/` | `01_Projets/schoolsWP/08_IA-et-Prompts` | Fusionner |
| `outils/` | `02_Ressources/Outils` | Deplacer (transverse) |
| `PROMPTS_schoolsWP/` | `01_Projets/schoolsWP/08_IA-et-Prompts` | Fusionner |
| `MEDICALE/` | `04_Personnel/Medical` | Deplacer |
| `_BACKUP_DRIVE_2026-02-09` | `99_Archives/2026-02-09_Backup-Drive` | Deplacer |

### 2.4 Mapping des systemes existants vers la cible

#### Systeme A (MAJUSCULES) → Cible

| Ancien | Nouveau | Notes |
|---|---|---|
| `00_START-HERE/` | Supprime | Contenu redistribue (conventions → 00_README de chaque projet) |
| `01_ADMIN/` | `03_Admin/` | Garder les sous-dossiers actuels (01_Identite → 06_Impots) |
| `02_PROJETS/` | `01_Projets/` | Renommer + conserver le contenu |
| `03_RESSOURCES/` | `02_Ressources/` | Fusionner + nettoyer les doublons internes |
| `04_ASSETS/` | Redistribuer | → `01_Projets/schoolsWP/04_Assets` (c'est du schoolsWP) |
| `05_CLIENTS/` | `01_Projets/` ou `99_Archives/` | Evaluer : clients actifs → projet, sinon archive |
| `06_CONTENUS/` | `01_Projets/schoolsWP/02_Contenu` | C'est du contenu schoolsWP |
| `07_personnel/` | `04_Personnel/` | Renommer |
| `99_ARCHIVES/` | `99_Archives/` | Garder |

#### Systeme B (minuscules vides) → Supprimer

Tous les dossiers du systeme B sont **vides** (0 enfant). Ils representent une tentative de reorganisation non aboutie.

| A supprimer |
|---|
| `00_boite_de_reception` |
| `01_projets_actifs` |
| `02_ressources_transverses` |
| `03_contenus` |
| `04_admin_legal` |
| `05_formations` |
| `06_archive` |

#### Doublons internes 03_RESSOURCES → Nettoyer

| Dossier avec contenu | Dossier vide (doublon) | Action |
|---|---|---|
| `03_Prompts-IA` | `03_Prompts_IA` | Supprimer le vide |
| `04_Methodes` | `04_Methodes_ et _Formations` | Supprimer le vide |
| `05_Outils-Documentation` (97 enfants) | `05_Outils_ et _Docs_Techniques` | Supprimer le vide |

### 2.5 Fichiers volants a la racine → Redistribuer

| Fichier | Destination |
|---|---|
| `schoolsWP – Index Global` (Sheet) | `01_Projets/schoolsWP/00_README/` |
| `schoolsWP – Mapping Migration` (Sheet) | `99_Archives/2026-02-09_Backup-Drive/` |
| `schoolsWP – Full Drive Index` (Sheet) | `99_Archives/2026-02-09_Backup-Drive/` |
| `schoolsWP – Full Drive Mapping` (Sheet) | `99_Archives/2026-02-09_Backup-Drive/` |
| `schoolsWP – Archive Migration` (Sheet) | `99_Archives/2026-02-09_Backup-Drive/` |
| `schoolsWP Drive Organizer` (Script) | `99_Archives/2026-02-09_Backup-Drive/` |
| `_schoolsWP_audit_data.json` | `99_Archives/2026-02-09_Backup-Drive/` |
| `schoolsWP-linkedin-reboot.md` (Doc) | `01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/LinkedIn/` |
| `Guide ultime pour vendre des sites web` (Doc) | `01_Projets/schoolsWP/05_Marketing/` |
| `https://schoolswp.com/-Performance...` (Sheet) | `01_Projets/schoolsWP/10_Analytics/` + renommer |
| `Adobe Scan 05 fevr. 2026.pdf` | `00_Inbox/` (a trier manuellement) |
| `Suivi Affilies Plugins (RSS-Promos)` (Sheet) | `01_Projets/schoolsWP/05_Marketing/01_Affiliation/` |
| `schoolsWP - YouTube Competitor Analysis` (Sheet) | `01_Projets/schoolsWP/09_Veille/` |
| `PROJET PSE LOGIFARE.pdf` | `00_Inbox/` (a trier — pas schoolsWP) |
| `Avocat - January 21, 2026...mp3` | `04_Personnel/` ou `00_Inbox/` |
| `2026-01-20 – BuddyBoss – Affiliation` (Doc) | `01_Projets/schoolsWP/05_Marketing/01_Affiliation/` |

---

## PHASE 3 — Regles de nommage

### 3.1 Convention dossiers

```
Format : XX_Nom-Du-Dossier
```

| Regle | Detail |
|---|---|
| Prefixe | 2 chiffres + underscore : `01_`, `02_`, ..., `99_` |
| Separateur | Tiret `-` entre les mots |
| Casse | Premiere lettre majuscule par mot (Title-Case) : `01_Contenu-Blog` |
| Accents | INTERDITS — `Strategie` pas `Stratégie` |
| Espaces | INTERDITS — utiliser le tiret |
| Caracteres speciaux | INTERDITS — pas de `#`, `&`, `()`, emojis |
| "Divers" / "Temp" / "Nouveau dossier" | INTERDITS — nommer explicitement |
| Langue | Francais (sauf termes techniques universels : SEO, CRM, API, LLM) |

### 3.2 Convention fichiers

```
Format : YYYY-MM-DD_Sujet_Type_v01_STATUS.ext
```

| Segment | Valeurs | Obligatoire |
|---|---|---|
| Date | `YYYY-MM-DD` (ISO 8601) | Oui |
| Sujet | Description courte en kebab-case : `analyse-seo-homepage` | Oui |
| Type | `Article`, `Sheet`, `Brief`, `Facture`, `Contrat`, `Script`, `Thumbnail`, `Export`, `Prompt`, `Rapport`, `Crea` | Oui |
| Version | `v01`, `v02`, `v03`... | Si applicable |
| Status | `DRAFT`, `REVIEW`, `APPROVED`, `FINAL` | Si applicable |
| Extension | `.pdf`, `.png`, `.mp4`, etc. (Google Docs n'en ont pas) | Auto |

**Separateur** : underscore `_` entre les segments, tiret `-` a l'interieur d'un segment.

### 3.3 10 exemples concrets

| # | Nom actuel (fictif/reel) | Nom corrige |
|---|---|---|
| 1 | `Guide ultime pour vendre des sites web` | `2026-02-08_Vendre-sites-web_Article_v01_DRAFT` |
| 2 | `Suivi Affiliés Plugins (RSS-Promos)` | `2026-01-31_Suivi-affilies-plugins_Sheet` |
| 3 | `schoolsWP - YouTube Competitor Analysis` | `2026-01-31_YouTube-competitor-analysis_Sheet` |
| 4 | `Adobe Scan 05 févr. 2026.pdf` | `2026-02-05_Scan-document_Export.pdf` |
| 5 | `2026-01-20 – BuddyBoss – Affiliation – Fiches` | `2026-01-20_BuddyBoss-affiliation_Brief` |
| 6 | `https://schoolswp.com/-Performance-on-Search-2026-02-06` | `2026-02-06_GSC-performance-search_Rapport` |
| 7 | `Avocat - January 21, 2026-esv2-90p-bg-10p.mp3` | `2026-01-21_Avocat-enregistrement_Audio.mp3` |
| 8 | `PROJET PSE LOGIFARE.pdf` | `2026-01-27_PSE-Logifare_Contrat.pdf` |
| 9 | (Thumbnail YouTube) `thumb_final_v3_LAST.png` | `2026-02-10_Performance-WP_Thumbnail_v03_FINAL.png` |
| 10 | (Prompt IA) `prompt seo structure mega ok.md` | `2026-01-15_Structure-SEO_Prompt_v01_APPROVED` |

### 3.4 Regles anti-chaos

| Regle | Pourquoi |
|---|---|
| **Jamais** de `final`, `def`, `last`, `ok`, `copie de` | Utiliser `v01..v99` + `STATUS` |
| **Jamais** de date DD/MM/YYYY ou "January 21" | Toujours `YYYY-MM-DD` |
| **Jamais** d'URL dans un nom de fichier | Raccourcir + mettre l'URL dans le contenu |
| **1 seul fichier = 1 seul emplacement** | Utiliser des Shortcuts si besoin de reference croisee |
| **Archive = on deplace, on ne duplique pas** | Pas de `_old`, `_backup` a cote du fichier actif |

---

## PHASE 4 — Gouvernance et bonnes pratiques

### 4.1 Versioning

| Situation | Methode |
|---|---|
| Document en cours (Google Doc/Sheet) | Historique des versions natif de Google. Pas de copie. |
| Snapshot a partager ou archiver | Export PDF + nommage : `..._v01_FINAL.pdf` |
| Asset visuel (PNG, PSD) | Nouvelle version = nouveau fichier : `_v01`, `_v02`. Archiver les anciennes. |
| Fichier non-Google (Word, Excel) | Version dans le nom + `STATUS` |

**Regle** : un seul fichier "actif" par document. Les anciennes versions vont dans `99_Archive/` du dossier parent.

### 4.2 Archivage

| Quand | Comment |
|---|---|
| Projet fini | Deplacer tout le dossier projet vers `99_Archives/YYYY-MM_Nom-Projet/` |
| Contenu obsolete | Deplacer dans le `99_Archive/` du dossier courant |
| Backup periodique | Pas dans le Drive actif. Utiliser un Drive separe ou un disque. |

**Convention de cloture** :
1. Ajouter un fichier `00_CLOTURE_YYYY-MM-DD` dans le dossier
2. Deplacer vers `99_Archives/`
3. Ne jamais supprimer (sauf doublons confirmes)

### 4.3 Collaboration (solo mais anticipation)

| Regle | Detail |
|---|---|
| Commentaires | Utiliser les commentaires Google Docs natifs (pas de couleur manuelle) |
| Feedback | Convention : `[PRENOM]: commentaire` dans les commentaires |
| Validation | STATUS dans le nom = seule source de verite pour l'etat d'un fichier |
| Freelances | Partager UN dossier specifique en "Editeur", jamais la racine |

### 4.4 Partage et permissions

| Qui | Acces | Perimetre |
|---|---|---|
| Toi (owner) | Proprietaire | Tout |
| Freelance ponctuel | Editeur | 1 sous-dossier projet specifique uniquement |
| Outil d'automatisation (n8n) | Lecteur ou Editeur via service account | Dossiers techniques uniquement |
| Personne externe | Lecteur | Fichier individuel, jamais un dossier entier |

**Regle** : verifier les partages actifs 1x/mois. Revoquer les acces termines.

### 4.5 Shortcuts

| Quand utiliser | Exemple |
|---|---|
| Un fichier est utile dans 2 contextes | Brief client dans `01_Projets/schoolsWP` + reference dans `02_Ressources/Templates` |
| Reference croisee entre projets | Un template utilise par plusieurs projets → original dans `02_Ressources`, shortcut dans chaque projet |

**Regle** : le fichier original vit dans son emplacement canonique. Partout ailleurs = Shortcut.

### 4.6 Routine mensuelle (10 min)

1. **Vider `00_Inbox`** : trier chaque fichier vers son dossier cible (5 min)
2. **Verifier la racine** : aucun fichier ne doit flotter hors des 6 dossiers (1 min)
3. **Scan partages** : revoquer les acces obsoletes (2 min)
4. **Quick check nommage** : reperer les fichiers sans date ou avec "copie de" (2 min)

### 4.7 Regles anti-bazar

| Regle | Mecanisme |
|---|---|
| **Zero fichier a la racine** | Tout va dans `00_Inbox` ou directement dans le bon dossier |
| **Zero dossier sans prefixe** | Tout dossier a un `XX_` |
| **Zero "Divers"** | Si tu ne sais pas ou mettre → `00_Inbox` |
| **Zero duplication** | Un fichier = un emplacement. Shortcut pour le reste. |
| **Archiver ≠ supprimer** | Deplacer dans `99_Archive`, jamais supprimer |

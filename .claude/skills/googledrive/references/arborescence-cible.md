# Arborescence Google Drive - schoolsWP

## Architecture RACINE proposée

```
Mon Drive/
│
├── 00_Boite_de_reception/          # Zone tampon - Tri hebdo obligatoire
│   └── a_trier/
│
├── 01_Projets_actifs/              # Projets en cours (< 6 mois activité)
│   ├── schoolsWP/                  # → Voir structure dédiée ci-dessous
│   ├── [Projet_B]/
│   ├── [Projet_C]/
│   ├── [Projet_D]/
│   ├── [Projet_E]/
│   └── [Projet_F]/
│
├── 02_Ressources_transverses/      # Assets partagés entre projets
│   ├── branding/                   # Logos, palettes, fonts
│   ├── templates/                  # Modèles réutilisables
│   ├── medias/                     # Banque images/vidéos stock
│   └── outils/                     # Scripts, extensions, configs
│
├── 03_Contenus/                    # Production de contenu
│   ├── linkedin/
│   ├── youtube/
│   ├── facebook/
│   ├── blog/
│   └── newsletter/
│
├── 04_Admin_legal/                 # Docs légaux et comptabilité
│   ├── entreprise/                 # KBIS, statuts, contrats
│   ├── comptabilite/               # Par année: 2024/, 2025/, 2026/
│   ├── banque/
│   └── assurances/
│
├── 05_Formations/                  # Apprentissage personnel
│   ├── en_cours/
│   └── terminees/
│
├── 06_Archive/                     # Projets clôturés (read-only)
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
│
└── 07_Personnel/                   # Non-pro (si Drive mixte)
    └── ...
```

---

## Logique des préfixes

| Préfixe | Catégorie | Fréquence d'accès |
|---------|-----------|-------------------|
| `00_` | Boîte de réception | Quotidienne |
| `01_` | Projets actifs | Quotidienne |
| `02_` | Ressources | Hebdomadaire |
| `03_` | Contenus | Quotidienne |
| `04_` | Admin/Légal | Mensuelle |
| `05_` | Formations | Variable |
| `06_` | Archive | Rare |
| `07_` | Personnel | Variable |

**Avantages :**
- Tri alphabétique = tri par importance
- Visuel immédiat dans Drive
- Scalable (08_, 09_... si besoin)

---

## Structure PROJET (template duplicable)

```
[Nom_Projet]/
│
├── 00_brief/                       # Cadrage initial
│   ├── brief_projet.md
│   ├── objectifs.md
│   └── references/
│
├── 01_strategie/                   # Réflexion, positionnement
│   ├── personas.md
│   ├── concurrence.md
│   └── roadmap.md
│
├── 02_production/                  # Travail en cours
│   ├── brouillons/
│   ├── en_revue/
│   └── valides/
│
├── 03_assets/                      # Ressources du projet
│   ├── images/
│   ├── videos/
│   ├── audio/
│   └── design/
│
├── 04_livrables/                   # Exports finaux
│   ├── clients/                    # Ce qu'on livre
│   └── internes/                   # Docs internes validés
│
├── 05_admin/                       # Contrats, factures projet
│   ├── devis/
│   ├── factures/
│   └── contrats/
│
└── _archive/                       # Anciennes versions (underscore = en bas)
```

**Règle :** Cette structure est **identique** pour tous les projets. On duplique le template.

---

## Structure schoolsWP (détaillée)

```
01_Projets_actifs/schoolsWP/
│
├── 00_brief/
│   ├── vision_schoolsWP.md
│   ├── proposition_valeur.md
│   └── public_cible.md
│
├── 01_strategie/
│   ├── positionnement.md
│   ├── roadmap_2026.md
│   ├── piliers_contenu.md
│   └── calendrier_editorial.md
│
├── 02_production/
│   ├── brouillons/
│   │   ├── linkedin/
│   │   ├── youtube/
│   │   └── blog/
│   ├── en_revue/
│   └── valides/
│
├── 03_assets/
│   ├── logos/
│   │   ├── logo_principal.png
│   │   ├── logo_blanc.png
│   │   └── logo_favicon.png
│   ├── visuels_rs/                 # Réseaux sociaux
│   │   ├── templates_linkedin/
│   │   ├── thumbnails_youtube/
│   │   └── covers/
│   ├── videos/
│   │   ├── intros/
│   │   ├── outros/
│   │   └── b_roll/
│   └── audio/
│       ├── jingles/
│       └── musiques/
│
├── 04_livrables/
│   ├── formations/                 # Produits vendus
│   │   ├── formation_A/
│   │   └── formation_B/
│   ├── lead_magnets/
│   └── exports_blog/
│
├── 05_admin/
│   ├── partenariats/
│   ├── affiliations/
│   └── analytics/
│       ├── rapports_mensuels/
│       └── dashboards/
│
└── _archive/
    ├── 2024/
    └── 2025/
```

---

## Workflow Boîte de réception

```
┌─────────────────┐
│ Nouveau fichier │
└────────┬────────┘
         ▼
┌─────────────────┐
│ 00_Boite_de_    │
│ reception/      │ ← Dépôt automatique
└────────┬────────┘
         ▼
    ┌────┴────┐
    │ Tri     │ ← 1x/semaine (10 min max)
    │ hebdo   │
    └────┬────┘
         ▼
   ┌─────┴─────┐
   │           │
   ▼           ▼
┌──────┐   ┌──────┐
│Projet│   │Trash │
│cible │   │      │
└──────┘   └──────┘
```

**Règle :** Rien ne reste plus de 7 jours dans `00_Boite_de_reception/`.

---

## Cycle de vie d'un fichier

```
brouillons/ → en_revue/ → valides/ → livrables/
    │            │           │            │
    ▼            ▼           ▼            ▼
 [DRAFT]     [REVIEW]   [APPROVED]    [FINAL]
```

| Statut | Emplacement | Qui peut modifier |
|--------|-------------|-------------------|
| DRAFT | `brouillons/` | Toi |
| REVIEW | `en_revue/` | Relecteur |
| APPROVED | `valides/` | Personne (lecture seule) |
| FINAL | `livrables/` | Personne (export PDF) |

---

## Archivage

### Quand archiver ?

- Projet terminé depuis > 3 mois
- Aucune modification depuis > 6 mois
- Exercice comptable clôturé

### Comment archiver ?

1. Créer dossier dans `06_Archive/[ANNEE]/`
2. Déplacer le projet complet
3. Renommer : `[Nom_Projet]_archive_YYYY-MM`
4. **Optionnel :** Convertir en lecture seule

### Convention de nommage archive

```
06_Archive/2025/schoolsWP_campagne_noel_archive_2025-01/
```

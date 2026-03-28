# Règles de Nommage - Google Drive schoolsWP

## Principes fondamentaux

| Règle | Recommandation |
|-------|----------------|
| Langue | **Français** uniquement |
| Casse dossiers | `snake_case` (minuscules + underscores) |
| Casse fichiers | `snake_case` ou `kebab-case` |
| Séparateur | `_` (underscore) ou `-` (tiret) |
| Espaces | **Interdits** (utiliser `_` ou `-`) |
| Accents | **Éviter** (remplacer é→e, à→a) |
| Longueur max | 60 caractères (nom uniquement) |

---

## Format des dossiers

```
[prefixe]_[categorie]_[detail]
```

**Exemples :**
```
01_projets_actifs
02_ressources_transverses
03_contenus
schoolsWP
formation_wordpress_perf
```

---

## Format des fichiers

### Structure générale

```
[YYYY-MM-DD]_[projet]_[type]_[description]_[version].[ext]
```

### Composants

| Élément | Format | Obligatoire | Exemple |
|---------|--------|-------------|---------|
| Date | `YYYY-MM-DD` | Recommandé | `2026-02-03` |
| Projet | `snake_case` | Oui | `schoolswp` |
| Type | code 2-4 lettres | Recommandé | `post`, `vid`, `img` |
| Description | `snake_case` | Oui | `intro_formations` |
| Version | `v01`, `v02` | Si applicable | `v02` |
| Statut | `DRAFT`, `REVIEW`, `FINAL` | Si applicable | `DRAFT` |

---

## 10 Exemples concrets

### 1. Post LinkedIn

```
2026-02-03_schoolswp_post_astuce_cache_wordpress_v01.md
2026-02-03_schoolswp_post_astuce_cache_wordpress_DRAFT.md
```

### 2. Thumbnail YouTube

```
2026-02-03_schoolswp_thumb_tuto_gutenberg_v02.png
schoolswp_thumb_template_principal.psd
```

### 3. Script vidéo

```
2026-02-03_schoolswp_script_formation_seo_ep01_REVIEW.md
2026-02-03_schoolswp_script_formation_seo_ep01_FINAL.md
```

### 4. Facture

```
2026-02_facture_client_dupont_F2026-015.pdf
2026-02_facture_hebergement_ovh.pdf
```

### 5. Contrat

```
2026-01-15_contrat_partenariat_entreprise_xyz.pdf
2026-01-15_contrat_partenariat_entreprise_xyz_signe.pdf
```

### 6. Image pour article

```
schoolswp_img_hero_page_accueil.jpg
schoolswp_img_feature_cache_benchmark.png
```

### 7. Export PDF article

```
2026-02-03_schoolswp_article_optimiser_wordpress_FINAL.pdf
```

### 8. Brief projet

```
2026-01_brief_formation_wordpress_automation.md
```

### 9. Rapport analytics

```
2026-01_rapport_analytics_mensuel_linkedin.pdf
2026-Q1_rapport_youtube_trimestre.xlsx
```

### 10. Asset design

```
schoolswp_logo_principal_couleur.svg
schoolswp_logo_blanc_transparent.png
schoolswp_palette_couleurs.ase
```

---

## Codes types recommandés

| Code | Type de fichier |
|------|-----------------|
| `post` | Post réseaux sociaux |
| `article` | Article blog |
| `script` | Script vidéo |
| `vid` | Fichier vidéo |
| `thumb` | Thumbnail |
| `img` | Image |
| `audio` | Fichier audio |
| `doc` | Document texte |
| `sheet` | Tableur |
| `slide` | Présentation |
| `brief` | Brief/Cahier des charges |
| `contrat` | Contrat |
| `facture` | Facture |
| `devis` | Devis |
| `rapport` | Rapport/Analytics |
| `export` | Export/Livrable |
| `template` | Modèle réutilisable |

---

## Versioning

### Convention de version

```
_v01  _v02  _v03  ...  _v10  _v11  ...
```

**Toujours 2 chiffres** (01, 02... pas 1, 2) pour le tri alphabétique.

### Statuts de workflow

| Statut | Signification | Emplacement |
|--------|---------------|-------------|
| `DRAFT` | Brouillon en cours | `brouillons/` |
| `REVIEW` | En attente de relecture | `en_revue/` |
| `APPROVED` | Validé, prêt à publier | `valides/` |
| `FINAL` | Version définitive exportée | `livrables/` |

### Exemples de progression

```
# Création
2026-02-03_schoolswp_post_astuce_cache_DRAFT.md

# Révision
2026-02-03_schoolswp_post_astuce_cache_REVIEW.md

# Validation
2026-02-03_schoolswp_post_astuce_cache_APPROVED.md

# Export final
2026-02-03_schoolswp_post_astuce_cache_FINAL.pdf
```

---

## Caractères interdits

| Caractère | Raison |
|-----------|--------|
| `espace` | Incompatible CLI, URLs |
| `#` | Interprété comme commentaire |
| `%` | Encodage URL |
| `&` | Caractère spécial shell |
| `?` `*` | Wildcards |
| `/` `\` | Séparateurs de chemin |
| `:` | Interdit Windows |
| `<` `>` `"` `'` | Caractères réservés |
| Accents | Encodage variable |

---

## Anti-patterns (à éviter)

| Mauvais | Bon |
|---------|-----|
| `Document Final.docx` | `2026-02-03_projet_brief_FINAL.docx` |
| `Nouveau dossier` | `projet_nom_explicite` |
| `Copie de fichier.pdf` | `fichier_v02.pdf` |
| `final_final_v3.docx` | `document_v03_FINAL.docx` |
| `Mon super projet!!!` | `mon_super_projet` |
| `2/3/2026 notes.txt` | `2026-02-03_notes.txt` |
| `IMG_20260203_123456.jpg` | `schoolswp_img_hero_accueil.jpg` |

---

## Checklist avant upload

- [ ] Pas d'espace dans le nom
- [ ] Pas d'accent ni caractère spécial
- [ ] Date au format `YYYY-MM-DD` (si applicable)
- [ ] Nom de projet identifiable
- [ ] Type de fichier clair
- [ ] Version ou statut indiqué
- [ ] Extension correcte
- [ ] Longueur < 60 caractères

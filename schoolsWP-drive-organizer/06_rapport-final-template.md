# Rapport Final – Migration PROMPTS_schoolsWP

**Date** : 2026-02-07
**Opérateur** : Michaël KIHL
**Outil** : schoolsWP Drive Organizer (Google Apps Script)

---

## 1. Résumé exécutif

| Métrique | Valeur |
|----------|--------|
| Dossiers créés | _XX_ |
| Fichiers renommés | _XX_ |
| Fichiers déplacés | _XX_ |
| Fichiers archivés (doublons) | _XX_ |
| Raccourcis créés | _XX_ |
| Erreurs | _XX_ |
| Fichiers "À valider" restants | _XX_ |

## 2. Dossiers créés

```
PROMPTS_schoolsWP/                          ← Racine
├── 01_ADMIN/
│   ├── 01_Regles-et-Index/                 ← Index global + règles
│   └── 02_Checklists-Qualite/              ← Checklists + Audits
├── 02_TEMPLATES/
│   ├── 01_Editorial_SEO/
│   │   ├── 01_DRAFT/
│   │   ├── 02_VALIDÉ/
│   │   ├── 03_LIVE/
│   │   └── 99_ARCHIVES/
│   ├── 02_Email_CRM_FluentCRM/  (+ statuts)
│   ├── 03_Conversion_Landing/   (+ statuts)
│   ├── 04_YouTube_Social/       (+ statuts)
│   ├── 05_Affiliation_Monetisation/ (+ statuts)
│   └── 06_Automation_SOP/       (+ statuts)
├── 03_PROMPTS/
│   ├── 01_Editorial_SEO/        (+ statuts)
│   ├── 02_Email_CRM/            (+ statuts)
│   ├── 03_Conversion/           (+ statuts)
│   ├── 04_Affiliation/          (+ statuts)
│   ├── 05_Assets/               (+ statuts)
│   └── 06_Automation/           (+ statuts)
├── 04_ASSETS/
│   ├── 01_Logos-Brand/
│   ├── 02_Thumbnails/
│   ├── 03_Banners/
│   └── 04_Illustrations/
├── 05_MONETISATION/
│   ├── 01_Affiliation/
│   ├── 02_Partenariats/
│   ├── 03_Dashboards-Reporting/
│   └── 04_Sequences_Email/
├── 06_SCHOOLS_WP_EDITORIAL/
│   ├── 01_Briefs/
│   ├── 02_Plans/
│   ├── 03_Clusters/
│   └── 04_Meta-FAQ-SERP/
├── 07_AUTOMATION/
│   ├── 01_n8n-Make-Zapier/
│   ├── 02_SOP/
│   └── 03_Scripts/
└── 99_ARCHIVES/
```

**Total** : _XX_ dossiers (dont _XX_ sous-dossiers de statut)

## 3. Fichiers renommés

| # | Ancien nom | Nouveau nom | Raison |
|---|-----------|-------------|--------|
| 1 | _ancien_ | _nouveau_ | _séparateur corrigé / date ajoutée / type ajouté_ |

## 4. Fichiers déplacés

| # | Fichier | Ancien chemin | Nouveau chemin |
|---|---------|---------------|----------------|
| 1 | _nom_ | _ancien/_ | _nouveau/_ |

## 5. Doublons archivés

| # | Fichier archivé | Doublon de | Raison |
|---|-----------------|------------|--------|
| 1 | _V1 archivé_ | _V2 conservé_ | _Version obsolète_ |

## 6. Raccourcis créés

| # | Fichier source | Raccourci dans | Raison |
|---|---------------|----------------|--------|
| 1 | _fichier_ | _dossier alternatif_ | _accessible depuis 2 catégories_ |

## 7. Exceptions & Ambiguïtés (validation humaine requise)

| # | Fichier | Problème | Action suggérée | Décision |
|---|---------|----------|-----------------|----------|
| 1 | _nom_ | _sujet ambigu / catégorie incertaine_ | _proposition_ | ⬜ À valider |

## 8. Recommandations anti-rechute

### Processus de création de nouveau fichier
1. **Nommer immédiatement** avec le format : `AAAA-MM-JJ – Sujet – Type – Usage.ext`
2. **Ranger directement** dans le bon dossier (consulter la checklist "Où ranger mon fichier ?")
3. **Choisir le statut** : créer dans `01_DRAFT`, déplacer vers `02_VALIDÉ` puis `03_LIVE`

### Règles d'hygiène hebdomadaire (5 min/semaine)
- [ ] Vider `01_DRAFT` : tout valider ou archiver
- [ ] Vérifier que `03_LIVE` ne contient pas de fichiers obsolètes
- [ ] Mettre à jour l'Index Global (ou exécuter `generateGlobalIndex()`)

### Automatisations recommandées
1. **Trigger hebdomadaire** : exécuter `generateGlobalIndex()` chaque lundi via un trigger Apps Script
2. **Notification** : configurer une alerte si un fichier est créé hors de l'arborescence
3. **Revue trimestrielle** : audit complet avec `runAudit()` pour détecter la dérive

### Pièges à éviter
- Ne jamais créer de fichier à la racine de PROMPTS_schoolsWP (toujours dans un sous-dossier)
- Ne jamais utiliser d'underscores ou de tirets courts comme séparateurs
- Ne jamais dupliquer un fichier : utiliser un raccourci Drive si multi-catégorie
- Ne jamais laisser un fichier en DRAFT plus de 7 jours

---

## 9. Backup

| Élément | Détail |
|---------|--------|
| Dossier backup | `_BACKUP_2026-02-07` |
| Emplacement | Dans PROMPTS_schoolsWP |
| Contenu | Copie de tous les fichiers avant migration |
| Durée de rétention | 30 jours minimum |
| Action post-rétention | Supprimer ou déplacer dans 99_ARCHIVES |

---

*Rapport généré par schoolsWP Drive Organizer*
*Michaël KIHL – schoolsWP*

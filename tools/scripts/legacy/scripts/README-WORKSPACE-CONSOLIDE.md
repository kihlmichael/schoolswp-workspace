# README — Espace de travail

> Ce document remplace les 4 README précédents :
> `README - 00_START-HERE`, `README — Admin`, `README — _Archives`, `2026-03-01 - README 01_ADMIN - Doc - Admin - V1`
>
> Dernière mise à jour : 2026-03-16

---

## Rôle de cet espace

Point d'entrée du Drive. Centralise les règles de nommage, la structure complète, les index globaux et la documentation administrative.

**Principe fondamental** : cet espace ne sert pas à produire. Il sert à structurer, sécuriser, suivre et retrouver.

---

## Arborescence

```
[Racine de l'espace de travail]
│
├── 00.01_Docs/            → Règles, nomenclature, documents de référence
├── 00.02_Sheets/          → Index globaux et tableaux de pilotage
├── 00.03_Raccourcis/      → Liens et accès rapides
├── 00.99_Archives/        → Versions obsolètes ou remplacées
│
├── 01.01_Identite/        → Infos propriétaire, coordonnées, profils, informations légales
├── 01.02_Regles/          → Conventions Drive, règles de nommage, règles de classement
├── 01.03_Checklists/      → Listes de contrôle qualité (avant publication, livraison, envoi)
├── 01.04_Index/           → Tableaux de suivi (Google Sheets) avec liens vers docs importants
├── 01.05_Strategie/       → Objectifs, roadmap, décisions, notes structurantes
├── 01.06_Contrats/        → Contrats clients / partenaires, CGV, NDA, documents signés
├── 01.07_Factures/        → Toutes les factures : clients, achats, SaaS, justificatifs
├── 01.08_Banque/          → Relevés, exports, RIB/IBAN, justificatifs bancaires
├── 01.09_Assurances/      → Contrats, attestations, déclarations, sinistres
├── 01.10_Impots-Fiscal/   → Déclarations, bilans, documents fiscaux, correspondances admin
├── 01.11_Reporting/       → Rapports d'activité, KPI, bilans périodiques
└── 01.12_Outils-Stack/    → Inventaire outils, documentation paramétrage, intégrations
```

**Règle** : aucun fichier à la racine de cet espace, uniquement les dossiers + ce README.

---

## Jalons et deadlines

| Date       | Événement                                                                 |
|------------|---------------------------------------------------------------------------|
| 2026-03-01 | Création du README 01_ADMIN V1                                            |
| 2026-03-02 | Mise à jour du README 00_START-HERE                                       |
| 2026-03-14 | **Réorganisation complète du Drive** — ancienne structure déplacée dans _Archives/ |
| En cours   | Migration manuelle depuis _Archives/ vers la nouvelle structure           |

---

## Règles de nommage

### Dossiers

Format : `NN_NomDuDossier` (deux chiffres, sans caractères spéciaux)

Exemples : `01_ADMIN`, `02_PROJETS`, `04_ASSETS`, `99_ARCHIVES`

### Fichiers — règle générale

Format : `AAAA-MM-JJ – Sujet – Type – Information.ext`

- La date fait foi et remplace toute notion de version
- Pas de versioning (v2, final, etc.)
- Le statut est géré par les dossiers, jamais dans le nom
- Aucun mot de passe ou information sensible dans le Drive

### Contenus éditoriaux (schoolsWP)

Format : `AAAA-MM-JJ – Sujet – Type`

Types : Article / Tutoriel / Guide / Vidéo / Newsletter / Note

Exemples :
```
2025-03-18 – Comparatif LMS WordPress – Article
2025-03-22 – Automatiser FluentCRM – Tutoriel
2025-04-10 – Roadmap SEO schoolsWP – Note
```

Statuts gérés par dossiers : `01_Backlog` / `02_En_cours` / `03_A_revoir` / `04_Publies` / `99_ARCHIVES`

### Factures

Format : `AAAA-MM-JJ – FournisseurOuClient – Facture – Montant.pdf`

Exemples : `2025-01-15 – o2switch – Facture – 72€.pdf`

### Relevés bancaires

Format : `AAAA-MM – Relevé bancaire – NomBanque.pdf`

Exemples : `2025-01 – Relevé bancaire – Qonto.pdf`

### Contrats

Format : `AAAA-MM-JJ – NomEntité – Type de contrat`

Types : Contrat prestation / Contrat freelance / Contrat partenariat / NDA / Contrat affiliation

### Assets (schoolsWP)

Format : `AAAA-MM-JJ – Sujet – Usage – Format.ext`

Usages courants : Logo principal / Illustration / Capture écran / Thumbnail YouTube / Lead magnet

### Articles multilingues

Format : `AAAA-MM-JJ – Sujet – Article – LANGUE.docx`

Codes langue : FR (source) / EN / DE

---

## Principes anti-bazar

- **1 fichier = 1 emplacement** — pour un accès multiple, utiliser des raccourcis Drive
- **Pas de doublons** — un document, un emplacement
- **Templates** — toujours dupliquer avant de modifier, jamais modifier l'original
- **Documents obsolètes** → déplacer dans `00.99_Archives` ou `01.xx_Archives`
- **Informations sensibles** — jamais stockées dans le Drive

---

## _Archives — Migration en cours

La réorganisation du 2026-03-14 a déplacé l'intégralité de l'ancienne structure dans `_Archives/` :

```
_Archives/
├── 00_START-HERE/
├── 01_ADMIN/
├── 02_PROJETS/
├── 03_RESSOURCES/
├── 04_CLIENTS/
├── 05_CONTENUS/
├── 06_MONETISATION/
├── 07_PERSONNEL/
├── 99_ARCHIVES/
└── [33 fichiers épars]
```

**Comment migrer** : procéder manuellement, au fur et à mesure.
1. Identifier un fichier actif dans `_Archives/`
2. Choisir son dossier cible dans la nouvelle structure
3. Le déplacer (clic droit > Déplacer vers)
4. Le renommer si besoin selon la convention `AAAA-MM-JJ – Sujet – Type – Info.ext`

Correspondances :
- `01_ADMIN/` → `01.xx_xxx/`
- `02_PROJETS/06_schoolsWP/` → `schoolsWP/`
- `05_CONTENUS/` → `schoolsWP/Contenu/`
- `07_PERSONNEL/` → `01.xx_xxx/` (sous-dossier Personnel)

⚠️ Ne jamais supprimer `_Archives/` sans avoir vérifié que tout le contenu utile a été migré.

---

## Liens utiles

- **Index Global** : [à remplir]
- **Règles de nommage** : ce document (section ci-dessus)
- **START HERE** : ce document

---
name: workspace-hygiene
description: |
  Audit et nettoyage du workspace solo-dev schoolsWP. Detecte le bruit (patch files, scripts
  residuels, dossiers dupliques, fichiers orphelins) et propose un plan de nettoyage en 2 temps :
  audit d'abord, apply ensuite. Utilise ce skill des que l'utilisateur parle de "nettoyer le
  workspace", "trop de bruit", "fichiers qui trainent", "dedupliquer", "archiver", "hygiene",
  "ranger le projet", "workspace cleanup", ou quand il mentionne des patch files, fix files, ou
  dossiers en double. Aussi utile quand l'utilisateur demande "qu'est-ce qui traine ?" ou "c'est
  quoi tout ce bordel ?".
---

# Workspace Hygiene

Skill de maintenance pour un workspace solo-dev. Deux modes : **audit** (detecter et proposer) et
**apply** (executer le plan valide).

Le principe fondamental : ne jamais casser une source de verite. On reduit le bruit, on ne detruit
pas l'histoire.

## Politique de securite

- **trash uniquement** — jamais `rm`, jamais `rm -rf`, jamais de suppression directe
- **audit d'abord** — toujours lister avant d'agir
- **validation globale** — presenter le plan complet, attendre le feu vert avant d'executer quoi que ce soit
- **une seule source canonique** — quand deux dossiers contiennent la meme chose, un seul survit
- **archiver plutot que detruire** — les fichiers potentiellement utiles vont dans `_archive/`, pas a la poubelle
- **pas de decision sur les dates seules** — un fichier vieux n'est pas forcement inutile

## Mode Audit

Quand l'utilisateur demande un audit (ou quand c'est la premiere invocation), scanner le workspace
et produire un rapport structure.

### Categories a scanner

**1. Patch files et scripts residuels**

Les `patch_*.py` et `fix_*.py` sont typiquement des scripts one-shot crees pendant un debug ou un
refactoring. Ils s'accumulent a la racine et dans `data/`.

- Scanner : `patch_*.py`, `fix_*.py`, `*.patch` a la racine et dans les sous-dossiers
- Classification :
  - **archive** — le script a un commentaire ou docstring qui explique ce qu'il fait, ou il touche
    a un workflow/systeme encore actif → `_archive/patches/`
  - **trash** — script minimal sans contexte, clairement residuel → `trash`
- En cas de doute, archiver plutot que trasher

**2. Dossiers dupliques**

Cas typique : `.agent/` vs `.agents/` qui contiennent la meme chose.

- Comparer le contenu (`diff -rq` ou equivalent)
- Si identique : garder celui reference dans CLAUDE.md ou le plus utilise, trasher l'autre
- Si different : lister les differences, ne rien faire sans validation explicite
- Pas de symlink — ca cree de la confusion, un seul dossier suffit

**3. Fichiers orphelins a la racine**

La racine du projet ne devrait contenir que les fichiers de config standard (pyproject.toml,
package.json, README, CLAUDE.md, .bat entry points).

- Detecter les fichiers qui n'ont pas leur place a la racine : `.html`, `.ps1`, `.csv`, dossiers
  temporaires (`temp-*`)
- Proposer un deplacement vers le bon dossier (`tools/`, `data/`, `_archive/`) ou trash

**4. Composants inactifs**

Dossiers ou sous-projets qui ne sont plus actifs. Cette categorie est sensible — ne jamais deplacer
sans un scoring minimal :

- Le dossier est-il reference dans CLAUDE.md, un script, ou un workflow n8n ?
- Y a-t-il eu des commits recents (< 30 jours) touchant ce dossier ?
- Le dossier est-il dans le .gitignore ou le workspace file ?

Scoring :
- **Reference + commits recents** → actif, ne pas toucher
- **Reference mais pas de commits** → potentiellement dormant, signaler sans action
- **Ni reference ni commits** → candidat a l'archivage, proposer avec contexte

Ne jamais deplacer un composant "inactif" sans scoring ET validation utilisateur.

### Format du rapport d'audit

```markdown
# Workspace Hygiene Report — {date}

## Etat general
{Nombre total de problemes detectes, repartis par categorie}

## Patch files et scripts residuels
| Fichier | Localisation | Action proposee | Raison |
|---------|-------------|-----------------|--------|
| patch_xxx.py | racine | trash | script one-shot sans docstring |
| fix_yyy.py | data/ | archive | touche au workflow Drive |

## Dossiers dupliques
| Dossier A | Dossier B | Statut | Action proposee |
|-----------|-----------|--------|-----------------|
| .agent/ | .agents/ | identiques | garder .agents/, trash .agent/ |

## Fichiers orphelins
| Fichier | Action proposee | Destination |
|---------|-----------------|-------------|
| download.html | deplacement | tools/ ou trash |

## Composants inactifs
| Composant | Reference | Commits recents | Score | Action proposee |
|-----------|-----------|----------------|-------|-----------------|
| temp-n8n-skills/ | non | non | 0/2 | archiver |

## Plan d'action resume
1. Creer `_archive/patches/` si necessaire
2. Archiver N fichiers
3. Trasher M fichiers
4. Supprimer le dossier duplique X
5. Deplacer P fichiers orphelins

**Attente validation avant execution.**
```

## Mode Apply

Une fois le plan valide par l'utilisateur (en entier ou avec des ajustements) :

1. **Creer les dossiers cibles** si necessaire (`_archive/`, `_archive/patches/`, etc.)
2. **Executer les actions dans l'ordre** :
   - Archivages d'abord (deplacements vers `_archive/`)
   - Trash ensuite
   - Deplacements de fichiers orphelins
   - Suppression de dossiers dupliques
3. **Verifier** que chaque action a reussi avant de passer a la suivante
4. **Mettre a jour .gitignore** seulement si l'utilisateur l'a explicitement demande dans sa validation
5. **Produire le rapport final**

### Format du rapport final

```markdown
# Workspace Hygiene — Execution Report

## Actions executees
- [x] Cree _archive/patches/
- [x] Archive : patch_extract_convention.py → _archive/patches/
- [x] Trash : fix_workflow.py
- [x] Trash : .agent/ (doublon de .agents/)
- [x] Deplace : download.html → tools/

## Actions ignorees (par choix utilisateur)
- [ ] temp-n8n-skills/ — utilisateur veut garder pour l'instant

## Etat apres nettoyage
- Fichiers a la racine : {avant} → {apres}
- Dossiers dupliques : {avant} → {apres}
- Patch/fix scripts : {avant} → {apres}
```

## Regles de nommage pour l'archivage

- `_archive/patches/` — scripts patch/fix
- `_archive/tools/` — outils obsoletes
- `_archive/data/` — donnees perimees
- Garder le nom d'origine du fichier (pas de renommage sauf conflit)
- En cas de conflit : suffixer avec `_YYYYMMDD`

## Ce que ce skill ne fait PAS

- Ne reorganise pas l'architecture du projet (dossiers `core/`, `content/`, `systems/`…)
- Ne touche pas aux fichiers de config (`.env`, `.mcp.json`, `pyproject.toml`…)
- Ne modifie pas le contenu des fichiers — seulement des deplacements et suppressions
- Ne prend pas de decision basee uniquement sur l'age d'un fichier
- Ne force jamais une action sans validation

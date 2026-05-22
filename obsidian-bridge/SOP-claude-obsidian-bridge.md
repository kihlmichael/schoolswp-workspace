---
name: SOP - Passerelle Obsidian Claude Code
owner: Michaël KIHL
project: schoolsWP
version: 1.2
date_creation: 2026-05-04
date_maj: 2026-05-22
status: phase-1
---

# SOP - Passerelle Obsidian - Claude Code

Procédure opérationnelle pour utiliser la passerelle entre le projet Claude Code schoolsWP et le vault Obsidian schoolsWP.

## 1. Préambule

La passerelle est un canal contrôlé. Pas une synchronisation.

Lois fondamentales :

1. **Asymétrie des écritures** : Claude Code n'écrit dans le vault que via `outbox-depuis-claude/`. Jamais ailleurs.
2. **Validation L0** : tout ce qui passe d'`outbox-depuis-claude/` vers une zone stable du wiki passe par un arbitrage Michaël.
3. **Append-only** : toute action significative est tracée. Côté vault dans `log.md`. Côté projet dans `obsidian-bridge/logs/`.

## 2. Cas d'usage 1 - exposer une note Obsidian à Claude Code

Tu (Michaël) veux qu'une note du vault soit lisible par Claude Code.

Procédure :

1. Identifier la note dans le vault.
2. La copier (ou un extrait suffisant) dans `00_systeme/claude-code-bridge/inbox-vers-claude/` du vault.
3. La copier ensuite dans `obsidian-bridge/inbox-from-obsidian/` du projet.
4. Demander à Claude Code de la traiter.
5. Optionnel : ajouter une mention dans `obsidian-bridge/logs/YYYY-MM-DD_actions.md`.

Variantes :

- Pour un fichier ponctuel : copie simple suffit.
- Pour un dossier : `xcopy` ou `robocopy` côté PowerShell, avec guillemets stricts pour gérer les emojis.

## 3. Cas d'usage 2 - produire une synthèse Claude Code vers Obsidian

Claude Code produit un draft destiné à intégrer le wiki.

Procédure :

1. Claude Code écrit le draft dans `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_type_titre.md`.
2. Le draft utilise le frontmatter standard et un template (`templates/synthese.md`, `templates/decision.md`).
3. Claude Code lit `index.md` à la racine du vault (lecture autorisée, cf. section 7) et ajoute au draft une section finale `## Carte de propagation` : d'après l'index, les pages du vault liées au sujet, les pages potentiellement contredites, les pages à mettre à jour si le draft est promu. Si l'index ne permet pas de conclure, l'indiquer explicitement plutôt que d'inventer.
4. Tu (Michaël) relis et arbitres.
5. Si validé, tu copies le fichier dans `00_systeme/claude-code-bridge/outbox-depuis-claude/` du vault.
6. Si tu décides de le promouvoir en zone stable :
   - Tu déplaces dans la zone cible (`04_memory/`, `06_decisions/`, `07_projects/...`, etc.).
   - Tu ajoutes une entrée correspondante dans `log.md` du vault (type `validation_memoire`, `decision`, `synthese`, etc.).
   - Tu mets à jour le frontmatter (`status: synthese-stabilisee` ou `memoire-durable`).

## 3bis. Cas d'usage 3 - capitaliser une analyse de session

Claude Code produit en session une analyse stratégique réutilisable (confrontation, comparaison, arbitrage, synthèse de recherche). Sans capture, elle disparaît dans l'historique de chat.

Procédure :

1. Quand une analyse de ce type est produite, Claude Code propose de la capitaliser.
2. Si tu acceptes, Claude Code écrit l'analyse dans `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_type_titre.md` (type `note` ou `synthese`), avec frontmatter standard.
3. Le draft suit ensuite le cas d'usage 2 à partir de l'étape 3 (carte de propagation, relecture, promotion éventuelle).

Critère de déclenchement : l'analyse a une valeur au-delà de la session courante. Une réponse ponctuelle à une question opérationnelle ne se capitalise pas.

## 4. Nommage des fichiers transitants

Format recommandé : `YYYY-MM-DD_type_titre-court.md`

Types autorisés (alignés sur la charte du vault) :

- `synthese`
- `decision`
- `sop`
- `rapport`
- `note`
- `log`

Exemples :

- `2026-05-04_synthese_audit-pinterest.md`
- `2026-05-04_decision_stack-formation-fluentboards.md`
- `2026-05-04_sop_publication-article-schoolswp.md`

## 5. Journalisation

### 5.1 Côté projet

Fichier journal quotidien : `obsidian-bridge/logs/YYYY-MM-DD_actions.md`

Une entrée par action significative. Format simple :

```markdown
## HH:MM - type | titre court

- **Acteur** : Claude Code | Michaël
- **Action** : phrase claire
- **Cible** : fichier(s) ou dossier(s)
- **Lien vers le draft** : chemin relatif
- **Statut** : draft | exporté vers vault | validé | refusé
```

### 5.2 Côté vault

Toute promotion en zone stable du wiki déclenche une entrée dans `log.md` à la racine du vault.

Voir le template `templates/log-entry.md` pour le format imposé par la charte du vault.

## 6. Rollback

Trois niveaux de réversibilité :

1. **Draft non validé** : tu supprimes manuellement le fichier dans `outbox-to-obsidian/` ou `outbox-depuis-claude/`. Pas de log nécessaire.
2. **Promotion erronée vers une zone stable** : tu ajoutes une entrée `correction` ou `archive` dans `log.md` du vault. Tu déplaces le fichier en `09_archive/` plutôt que de le supprimer.
3. **Erreur structurelle** : tu reviens au commit Git précédent côté projet. Côté vault, pas de Git ; tu utilises l'historique Obsidian (plugin File Recovery natif).

## 7. Ce que Claude Code peut lire dans le vault

- `claude.md`, `index.md`, `log.md` à la racine du vault
- `00_systeme/claude-code-bridge/inbox-vers-claude/**`
- `07_projects/schoolswp/**` (uniquement si demandé explicitement, en lecture seule)
- `01_inbox/**` (uniquement si demandé)

## 8. Ce que Claude Code peut écrire dans le vault

### 8.1 Pouvoir d'écriture par défaut

- **Principalement** `00_systeme/claude-code-bridge/outbox-depuis-claude/**` (et éventuellement `decisions-proposees/`, `syntheses-proposees/`)
- **Uniquement** des fichiers Markdown propres
- **Toujours** avec un frontmatter standard

### 8.2 Exception consolidation post-transport (depuis v1.1)

Claude Code est autorisé à modifier `08_sources/<sub-zone>/` **strictement pour les actions de consolidation post-transport humain**. Périmètre autorisé :

- **Renommer** un fichier index ou synthèse pour éliminer un préfixe technique (ex: drop préfixe date) ou un suffixe versionné (ex: drop suffixe `-update`).
- **Archiver** une version périmée d'un index dans le sous-dossier `_normalisation/` du plugin concerné.
- **Mettre à jour** un index existant (`index-documentation.md`, `README.md`) pour refléter exactement le contenu transporté.

Conditions strictes :

- Le transport humain doit avoir déjà eu lieu (pas d'action préemptive avant transport).
- Action limitée aux fichiers index/README et à `_normalisation/`. **Pas de modification du contenu source-brute déjà transporté** (les fichiers `videos/*.md`, `docs/*.md`, etc. restent intouchables).
- Pas de création de nouveau contenu durable (synthèse, mémoire) sans passer par le workflow `outbox-depuis-claude/`.
- Toute action est tracée dans `log.md` du vault avec auteur explicite `Claude Code (consolidation)`.

### 8.3 Append au log.md du vault (depuis v1.1)

Pour tracer ses propres actions du périmètre 8.2, Claude Code est autorisé à **APPENDer** une entrée dans `log.md` du vault. Conditions :

- Append uniquement (jamais modifier une entrée passée → règle absolue append-only respectée).
- Format strict imposé par la charte du vault (cf. section 2 du `log.md`).
- Type d'entrée limité à `modification`, `archive`, `correction` pour les cas de consolidation.
- Mise à jour parallèle de la grille section 5 du `log.md` (1 ligne par entrée).

## 9. Ce que Claude Code ne doit jamais toucher

- `.obsidian/` (config Obsidian, peut casser le rendu)
- `claude.md`, `index.md` du vault (gouvernance, modifs par Michaël uniquement)
- Les entrées passées de `log.md` (append-only strict, modification interdite même par Claude)
- Les zones stables du vault hors zone passerelle et hors exception 8.2 : `02_drafts/`, `03_synthesis/`, `04_memory/`, `05_sop/`, `06_decisions/`, `07_projects/`, `09_archive/`
- Le contenu source-brute déjà transporté dans `08_sources/<sub-zone>/<videos|docs|...>/` (intouchable, modifs par Michaël uniquement)
- Les fiches d'identité schoolsWP déjà stabilisées en phase 2 et 3

## 10. Évolutions possibles (phase 2+)

À évaluer **uniquement si un besoin réel apparaît** :

- Script PowerShell `sync-bridge.ps1` pour automatiser la copie bidirectionnelle.
- Sous-skill Claude Code de verrouillage durci (écriture limitée à `outbox-to-obsidian/`).
- Hook PreToolUse qui bloque tout Write ou Edit hors périmètre passerelle.
- MCP filesystem cadré sur le chemin vault.

Aucune de ces évolutions n'est implémentée en phase 1.

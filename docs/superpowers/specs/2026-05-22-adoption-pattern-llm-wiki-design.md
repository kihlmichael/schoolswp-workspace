# Spec — Adoption ciblée du pattern LLM Wiki (Karpathy)

- **Date** : 2026-05-22
- **Projet** : schoolsWP
- **Auteur** : Michaël KIHL (design co-construit avec Claude Code)
- **Statut** : design validé, en attente de relecture avant plan d'implémentation

## 1. Contexte

Le pattern « LLM Wiki » d'Andrej Karpathy décrit un wiki markdown interlié, maintenu par un LLM, structuré en 3 couches (sources brutes immuables / wiki généré / schéma de gouvernance) et opéré par 3 actions récurrentes (ingest / query / lint), avec deux fichiers pivots (`index.md` de contenu, `log.md` chronologique).

Une confrontation de ce pattern avec l'infrastructure schoolsWP existante (passerelle Obsidian + mémoire interne Claude Code) a révélé 4 écarts concrets. Ce document spécifie leur correction.

### Ce qui existe déjà et reste inchangé

- La **passerelle Obsidian** (`obsidian-bridge/`) couvre les 3 couches Karpathy avec un modèle d'autorité plus strict.
- La **mémoire interne** (`memory/MEMORY.md` + fichiers topic) applique déjà le pattern « un fait = un fichier, un index ».
- L'**asymétrie d'autorité** (Claude propose, Michaël valide toute promotion en zone stable du vault) est un choix délibéré. Le pattern Karpathy « le LLM possède et maintient le wiki » n'est **pas** adopté pour le vault. Les corrections ci-dessous se cantonnent à ce que Claude possède légitimement : la mémoire interne et les dossiers de transit de la passerelle.

### Les 4 écarts corrigés

1. **Écart 1 — opération Lint absente.** Ni la mémoire interne ni la passerelle ne reçoivent de contrôle de santé périodique. Preuve aiguë : `MEMORY.md` dépasse le plafond de chargement et est tronqué en ce moment.
2. **Écart 2 — l'ingestion ne propage pas.** Une synthèse produite par la passerelle est un draft isolé, sans cartographie de son impact sur le reste du wiki.
3. **Écart 3 — l'opération Query ne capitalise pas.** Les analyses stratégiques produites en session s'évaporent dans le chat au lieu d'être refilées dans le wiki.
4. **Écart 4 — la mémoire interne n'a pas de log chronologique.** Elle a un index de contenu (`MEMORY.md`) mais aucune trace temporelle des créations/maj/suppressions.

## 2. Décisions de conception (validées)

| Sujet | Décision |
| --- | --- |
| Cible du lint | Mémoire interne (`memory/`) + dossiers passerelle (`outbox-to-obsidian/`, `logs/`). Pas le contenu du vault. |
| Forme du lint | Routine planifiée. |
| Autonomie du lint | Auto-fix du mécanique sans risque, signalement du reste. Jamais de suppression de contenu sans Michaël. |
| Planification | Exécution locale au logon Windows (le lint cible des fichiers locaux qu'un agent cloud ne peut pas atteindre), bridée à 1×/jour. |
| Interne du lint | Approche A : invocation Claude Code headless intégrale (détection + fix + rapport). Approche B (script déterministe + Claude) gardée en réserve pour durcissement futur. |

## 3. Architecture

Cinq blocs de livraison. Le bloc §3.1 est un correctif ponctuel ; §3.2 à §3.5 sont des composants durables.

### 3.1 Correctif immédiat : dégonfler `MEMORY.md`

**Problème** : `MEMORY.md` fait 25,2 Ko, au-dessus du plafond de chargement 24,4 Ko. Des entrées d'index sont tronquées et ne sont plus lues.

**Action** : raccourcir les lignes d'index les plus longues, déporter le détail dans les fichiers topic correspondants. Cible ~22 Ko pour conserver du headroom.

**Contrainte** : aucune mémoire supprimée. Seul l'index est resserré. Le contenu des fichiers topic reste intact (ou s'enrichit du détail déporté).

**Statut** : fait à la main pendant l'implémentation. Vaut comme premier passage de lint manuel.

### 3.2 Écart 4 : `memory/LOG.md`

**Composant** : nouveau fichier `memory/LOG.md`, journal chronologique append-only de la mémoire interne.

**Format** (repris de Karpathy) :

```text
## [YYYY-MM-DD] type | résumé court
```

Types : `ingest` (nouvelle mémoire), `update`, `delete`, `lint`.

**Activation du réflexe** : une directive est ajoutée en tête de `MEMORY.md` (fichier garanti chargé à chaque session). Elle impose d'appender une entrée `LOG.md` à chaque création, mise à jour ou suppression de mémoire.

**Interface** : append-only strict. Jamais de modification d'entrée passée. La routine de lint (§3.3) y appende aussi ses runs.

### 3.3 Écart 1 : la routine de lint

**Cibles** : `memory/` + `obsidian-bridge/outbox-to-obsidian/` + `obsidian-bridge/logs/`.

**Composants** :

1. `obsidian-bridge/SOP-memory-lint.md` (versionné) : le doc de procédure. Contient la checklist, les règles auto-fix vs signalement, le format de sortie. C'est le « schéma » que suit le run de lint.
2. `tools/scripts/memory-lint-launcher.ps1` (versionné) : le launcher local. Gère le throttle, lit le webhook Discord, invoque Claude Code headless. Lançable aussi à la main.
3. `tools/scripts/install-memory-lint-task.ps1` (versionné) : enregistre la tâche planifiée Windows. Calqué sur `nemoclaw-install-task.ps1`.
4. Tâche planifiée Windows « schoolsWP Memory Lint », trigger AtLogOn, **séparée** de « NemoClaw Autostart » (isolation de deux préoccupations sans rapport).

**Flux d'exécution** :

```text
Logon Windows
  -> Tâche planifiée "schoolsWP Memory Lint"
     -> memory-lint-launcher.ps1
        -> throttle : si memory/.last-lint == date du jour, sortie silencieuse
        -> lit DISCORD_ROUTINES_WEBHOOK depuis .env, l'injecte en variable d'env
        -> invoque Claude Code headless, piloté par SOP-memory-lint.md
           -> détecte les anomalies (checklist §3.3)
           -> auto-fixe le mécanique
           -> appende une entrée "lint" dans memory/LOG.md
           -> si flags : POST résumé sur le webhook Discord
        -> en cas de succès : écrit la date du jour dans memory/.last-lint
```

**Checklist de lint** :

Auto-fix (mécanique, sans risque) :

- `MEMORY.md` au-dessus du plafond de chargement : raccourcir les lignes d'index, déporter le détail dans les topics.
- Ligne d'index de `MEMORY.md` au-dessus de ~200 caractères : raccourcir.
- Fichier topic présent dans `memory/` mais absent de l'index `MEMORY.md` : ajouter la ligne d'index.

Signalement seul (demande un arbitrage Michaël) :

- Pointeur d'index `MEMORY.md` vers un fichier topic inexistant.
- Fichier topic sans frontmatter complet (`name`, `description`, `metadata.type`).
- Lien `[[wikilink]]` non résolu dans un topic : compté et rapporté (un `[[]]` non résolu est admis par le pattern, il marque du travail futur).
- Contradiction apparente entre deux mémoires.
- Mémoire potentiellement périmée (référence un fichier/flag disparu, TODO probablement clos).
- Draft dans `outbox-to-obsidian/` non transporté depuis plus de 14 jours.

**Sortie** :

- Entrée `LOG.md` : **toujours**, même quand le lint est propre. En-tête `## [date] lint | propre` ou `## [date] lint | N fixes, M flags`. Quand il y a des flags, l'entrée inclut dans son corps le **détail de chaque flag** (fichier concerné, nature du problème). `LOG.md` est le support durable et actionnable des flags.
- Notification Discord (`schoolsWP-Routines`, channel `#alerts`) : **uniquement s'il y a des flags**. Message = résumé court renvoyant à l'entrée `LOG.md` du jour. Zéro bruit quand tout est propre.

**Gestion du webhook** : la clé `DISCORD_ROUTINES_WEBHOOK` vit dans le `.env` local du projet (placeholder ajouté dans `.env.example`). Le launcher la lit et l'injecte en variable d'environnement passée au process Claude headless. **Claude ne lit jamais `.env` directement** (règle de sécurité projet). Si la clé est absente ou vide, le lint s'exécute quand même, saute la notification et le note dans `LOG.md`.

### 3.4 Écart 2 : carte de propagation

**Composant** : modification de `obsidian-bridge/SOP-claude-obsidian-bridge.md`, version 1.1 -> 1.2.

**Changement** : le cas d'usage 2 (produire une synthèse Claude vers Obsidian) reçoit une étape supplémentaire. Avant de finaliser un draft dans `outbox-to-obsidian/`, Claude lit `index.md` du vault (lecture déjà autorisée par la section 7 de la SOP) et ajoute au draft une section `## Carte de propagation` listant :

- les pages du vault liées au sujet du draft,
- les pages potentiellement contredites par le draft,
- les pages à mettre à jour si le draft est promu.

**Effet** : le draft one-shot devient un delta cross-référencé que Michaël peut exécuter, au lieu d'une page isolée.

### 3.5 Écart 3 : réflexe de capitalisation

**Composant** : ajout d'un « Cas d'usage 3 » dans `SOP-claude-obsidian-bridge.md` v1.2, et 2 lignes de réflexe dans `CLAUDE.md`.

**Cas d'usage 3 — capitaliser une analyse de session** : quand une analyse stratégique réutilisable est produite en session, Claude propose de la router dans `outbox-to-obsidian/` comme `note` ou `synthese`, au lieu de la laisser s'évaporer dans le chat.

**Activation du réflexe** : la SOP n'est pas auto-chargée (lue à la demande). Pour que le réflexe se déclenche, 2 lignes courtes sont ajoutées à la section « Passerelle Obsidian » de `CLAUDE.md` (auto-chargé), pointant vers les cas d'usage 2 et 3 de la SOP. Détail de la procédure dans la SOP, déclencheur court dans `CLAUDE.md` : conforme à l'architecture en couches du projet (pas de duplication).

## 4. Gestion des erreurs

| Situation | Comportement |
| --- | --- |
| `claude` absent du PATH | Le launcher journalise l'erreur dans `memory/.lint-launcher.log`, sort en code non-zéro, **n'écrit pas** le stamp throttle (retry au prochain logon). |
| Run Claude headless en échec | Idem : pas de stamp écrit, retry au prochain logon. |
| Webhook Discord absent/vide | Le lint s'exécute, saute la notification, le note dans `LOG.md`. Pas une erreur bloquante. |
| Deuxième logon le même jour | Le throttle (`memory/.last-lint`) coupe le run : sortie silencieuse. |
| Lint relancé sans rien à corriger | Run idempotent : aucune modification, entrée `LOG.md` « propre », pas de Discord. |

Le stamp throttle n'est écrit **qu'en cas de succès complet** : un échec garantit un nouvel essai.

## 5. Tests

- **Launcher** : exécution manuelle, vérifier que le throttle bloque un second run le même jour, vérifier la création du stamp.
- **Procédure de lint** : exécuter sur l'état courant de `memory/`, vérifier le dégonflage de `MEMORY.md`, l'ajout d'entrée dans `LOG.md`, le POST Discord en présence de flags.
- **Idempotence** : lancer le lint deux fois de suite, le second run ne trouve rien à corriger.
- **Modifications SOP / `CLAUDE.md`** : relecture documentaire (pas de test automatisé).

## 6. Inventaire des fichiers

**Créés** :

- `obsidian-bridge/SOP-memory-lint.md`
- `tools/scripts/memory-lint-launcher.ps1`
- `tools/scripts/install-memory-lint-task.ps1`
- `memory/LOG.md`

**Modifiés** :

- `memory/MEMORY.md` (dégonflage + directive `LOG.md` en tête)
- `obsidian-bridge/SOP-claude-obsidian-bridge.md` (v1.1 -> v1.2 : carte de propagation + cas d'usage 3)
- `obsidian-bridge/README.md` (bump de version, mention du nouveau `SOP-memory-lint.md`)
- `CLAUDE.md` projet (section Passerelle Obsidian : 2 lignes de réflexe + mention de la routine de lint)
- `.env.example` (clé `DISCORD_ROUTINES_WEBHOOK`)

**Hors repo** (mémoire interne, non versionnée) : `memory/LOG.md`, `memory/.last-lint`, `memory/.lint-launcher.log`.

**Infrastructure** : tâche planifiée Windows « schoolsWP Memory Lint » (AtLogOn).

## 7. Séquencement

1. §3.1 (dégonfler `MEMORY.md`) + §3.2 (`LOG.md`) : aigu et trivial, en premier.
2. §3.4 (carte de propagation) + §3.5 (réflexe de capitalisation) : éditions documentaires, ensemble.
3. §3.3 (routine de lint) : le bloc le plus lourd, en dernier.

## 8. Hors périmètre (YAGNI)

- Moteur de recherche markdown type `qmd` : la recherche native Obsidian et le recall par description suffisent à l'échelle actuelle.
- Lint du contenu du vault : nécessiterait d'élargir les permissions de lecture (section 7 de la SOP) ; posture de sécurité conservée. Obsidian fournit déjà graph view et Dataview côté vault.
- Pages d'entité par plugin (FluentCRM, Kadence, etc.) : piste pertinente notée lors de la confrontation, mais relève d'une refonte de structure, écartée de ce périmètre.
- Auto-fix total avec archivage autonome de mémoires : exclu, en conflit avec la règle Data Safety du projet (pas de suppression de contenu sans confirmation).

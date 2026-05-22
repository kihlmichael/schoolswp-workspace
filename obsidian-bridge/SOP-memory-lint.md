---
name: SOP - Lint de la mémoire interne schoolsWP
owner: Michaël KIHL
project: schoolsWP
version: 1.1
date_creation: 2026-05-22
date_maj: 2026-05-22
status: actif
---

# SOP - Lint de la mémoire interne schoolsWP

Procédure suivie par le run Claude Code headless déclenché par tools/scripts/memory-lint-launcher.ps1. Adoption de l'opération « lint » du pattern LLM Wiki (écart 1).

## 1. Rôle

Contrôle de santé périodique de la mémoire interne Claude Code et des dossiers de transit de la passerelle Obsidian. Auto-corrige le mécanique sans risque, signale le reste.

## 2. Cibles

- Le dossier de la mémoire interne (chemin absolu fourni dans le prompt de lancement). Contient MEMORY.md, LOG.md et les fichiers topic.
- obsidian-bridge/outbox-to-obsidian/ : drafts en attente de transport vers le vault.
- obsidian-bridge/logs/ : journaux quotidiens de la passerelle.

## 3. Loi de sécurité

- Aucune suppression de contenu. Jamais supprimer un fichier topic ni vider une mémoire. Au maximum : raccourcir une ligne d'index, déporter du détail.
- LOG.md append-only. Ne jamais modifier une entrée passée.
- Tout ce qui demande un arbitrage (contradiction, péremption) est SIGNALÉ, jamais corrigé d'office.

## 4. Checklist

### 4.1 Auto-fix (mécanique, sans risque)

| Contrôle | Correction |
| --- | --- |
| MEMORY.md dépasse ~24 Ko (plafond de chargement) | Raccourcir les lignes d'index les plus longues, déporter le détail dans le fichier topic correspondant. Viser ~22 Ko. |
| Ligne d'index de MEMORY.md au-dessus de ~200 caractères | Raccourcir le hook, sans toucher la portion titre et lien. |
| Fichier topic présent dans le dossier mémoire mais absent de l'index MEMORY.md | Ajouter la ligne d'index (titre, lien, hook court). |

### 4.2 Signalement seul (arbitrage Michaël requis)

| Contrôle | Action |
| --- | --- |
| Ligne d'index de MEMORY.md pointant vers un fichier topic inexistant | Flag. |
| Fichier topic sans frontmatter complet (name, description, metadata.type) | Flag. |
| Lien wikilink non résolu dans un topic | Compter et flag (un wikilink non résolu est admis, il marque du travail futur). |
| Deux mémoires en contradiction apparente | Flag, citer les deux fichiers. |
| Mémoire potentiellement périmée (référence un fichier ou flag disparu, TODO probablement clos) | Flag. |
| Draft dans outbox-to-obsidian/ non transporté depuis plus de 14 jours | Flag. |

## 5. Procédure

Le dossier mémoire ne peut pas être écrit directement par le run headless (le harness le traite comme sensible). Tous les résultats sont écrits dans le dossier de staging dont le chemin absolu est fourni dans le prompt de lancement. Le launcher applique ensuite ces écritures dans le dossier mémoire.

1. Lire MEMORY.md et lister les fichiers topic du dossier mémoire.
2. Dérouler la checklist 4.1. Pour chaque auto-fix, écrire le fichier corrigé en entier dans le sous-dossier apply/ du staging, sous son nom d'origine (par exemple staging/apply/MEMORY.md). Le launcher écrasera le fichier mémoire homonyme.
3. Dérouler la checklist 4.2, collecter les flags.
4. Écrire l'entrée de journal dans le fichier log-entry.md à la racine du staging (cf. section 6).
5. Écrire le fichier result.txt à la racine du staging (cf. section 7).

Les fichiers log-entry.md et result.txt sont obligatoires : le launcher considère leur absence comme un échec et ne persiste rien.

## 6. Fichier log-entry.md

Une entrée de journal, toujours produite, même quand le lint est propre. Le launcher l'appende à LOG.md du dossier mémoire.

En-tête : ## [YYYY-MM-DD] lint | propre, ou ## [YYYY-MM-DD] lint | N fixes, M flags.

Quand il y a des fixes ou des flags, détailler dans le corps, une puce par élément. Exemple :

    ## [2026-05-22] lint | 2 fixes, 1 flag

    - fix : MEMORY.md ramené de 25,2 à 22,0 Ko (8 lignes d'index raccourcies)
    - fix : ajout de l'entrée d'index pour reference_xyz.md (topic orphelin)
    - flag : project_abc.md et project_def.md se contredisent sur un sujet

## 7. Fichier result.txt

Le launcher le copie en .lint-result.txt dans le dossier mémoire et s'en sert pour décider de la notification Discord.

- Si aucun flag : écrire exactement le mot clean (les auto-fix seuls, sans flag, ne déclenchent pas de notification).
- Si au moins un flag : écrire un résumé court (moins de 1900 caractères) destiné à Discord, commençant par « Lint mémoire schoolsWP : » et listant les flags.

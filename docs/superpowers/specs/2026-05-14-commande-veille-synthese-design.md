---
name: Commande /veille - synthese de dossier de veille
owner: Michaël KIHL
project: schoolsWP
date_creation: 2026-05-14
status: spec-a-relire
type: design
---

# Design : commande `/veille` (synthese de dossier de veille)

## 1. Contexte et probleme

Le repo `claude-obsidian` (AgriciDaniel) propose un pattern `/autoresearch` :
recherche autonome multi-rounds, synthese, classement automatique dans un vault
Obsidian. Le projet schoolsWP a deja une passerelle Obsidian
(`obsidian-bridge/` + `00_systeme/claude-code-bridge/` cote vault) avec une
gouvernance stricte et opposee : asymetrie d'autorite, ecriture vault limitee a
`outbox-depuis-claude/`, gate humain L0, `log.md` append-only, phase 1
explicitement sans automatisation.

Le modele d'ecriture autonome de `claude-obsidian` est donc incompatible avec la
gouvernance en place. Mais une friction reelle existe cote schoolsWP :
**constituer un dossier de veille (SEO, WordPress, plugins) prend trop de temps**,
et precisement l'etape de **synthese** (transformer des sources deja collectees
en un dossier structure et exploitable, pas un dump). La collecte de sources
n'est pas le goulot : Michaël sait trouver ses sources.

## 2. Objectif

Importer de `claude-obsidian` **le travail de synthese, pas le modele d'ecriture
autonome**. Automatiser uniquement les etapes 1 et 2 du Cas d'usage 2 deja
documente dans la SOP de la passerelle : produire un draft de synthese dans
`obsidian-bridge/outbox-to-obsidian/`, pret a etre arbitre par Michaël (gate L0),
puis promu manuellement vers le vault.

## 3. Non-objectifs (YAGNI)

Explicitement hors perimetre :

- Pas de decouverte autonome de sources (c'est le role de l'agent `niche_scout`).
- Pas de recherche multi-rounds.
- Pas d'ecriture dans le vault, pas de promotion automatique vers une zone stable.
- Pas d'agent Python, pas de sync bidirectionnelle.
- Sens inbox (vault vers projet) non touche.
- Pas de modification de la SOP ni des fichiers versionnes de la passerelle.
- Extraction en skill methodo (approche C envisagee) : pas maintenant, atteignable
  plus tard sans rework.

## 4. Approche retenue

**Slash command `/veille`** : un fichier unique `.claude/commands/veille.md`.

Alternatives ecartees :

- **Agent Python `veille_synthesizer`** : reimplemente le fetch web en Python alors
  que Claude Code sait deja le faire nativement. Surface de dependances inutile.
- **Skill methodo + commande fine** : deux artefacts au lieu d'un, registre de
  skills deja volumineux. Reste atteignable plus tard si la methodo de synthese
  s'avere assez riche pour meriter d'etre extraite.

La commande slash mirror le pattern reel de `claude-obsidian` (`/autoresearch` y
est une slash command), tourne en session avec les outils de fetch deja
disponibles, et produit directement le draft markdown. Zero code Python, zero
dependance nouvelle.

## 5. Architecture et contrat d'invocation

- **Artefact unique** : `.claude/commands/veille.md` (fichier de prompt de commande).
- **Invocation** : `/veille <sujet>`. Dans le meme message, l'utilisateur joint ses
  sources : URLs en liste, chemins de fichiers locaux, ou extraits de texte colles.
  Les trois types peuvent etre melanges.
- Si aucune source n'est fournie : la commande la demande et s'arrete.
- Si le `<sujet>` est absent : la commande le demande et s'arrete.

## 6. Flux en 6 etapes

1. **Parser l'entree** : extraire le `<sujet>` et collecter toutes les sources du
   message (URLs, chemins locaux, extraits colles).
2. **Fetch chaque source** :
   - URL : `defuddle <url>` via Bash en priorite (CLI npm globale, recommandee
     pour la veille article), fallback firecrawl MCP (`firecrawl_scrape`),
     fallback `WebFetch`.
   - Chemin local : tool `Read`.
   - Extrait colle : utilise tel quel.
3. **Synthetiser** dans la structure exacte de
   `obsidian-bridge/templates/synthese.md` : Question traitee / Sources consultees
   (avec le role de chaque source) / Synthese / Faits (sources, verifiables) /
   Hypotheses / Idees / Proposition pour le wiki (zone cible suggeree :
   `04_memory/`, `05_sop/`, `06_decisions/`, `07_projects/...`) / Questions
   restantes.
   Barre de qualite : pas d'em-dash, pas d'emojis, marque ecrite `schoolsWP`,
   tutoiement, concision.
4. **Ecrire le draft** :
   `obsidian-bridge/outbox-to-obsidian/YYYY-MM-DD_synthese_<sujet-kebab>.md`
   (nommage SOP section 4). Frontmatter conforme au template `synthese.md` :
   `source: claude-code`, `status: a-arbitrer`, `type: synthese`,
   `date_creation`, `sujet`, `fichiers_sources` (qui contient URLs et chemins :
   voir section 8).
5. **Logger** : append d'une entree dans
   `obsidian-bridge/logs/YYYY-MM-DD_actions.md` au format SOP section 5.1
   (Acteur : Claude Code, Action, Cible, Lien vers le draft, Statut : `draft`).
   Creer le fichier de log du jour s'il n'existe pas.
6. **S'arreter** : afficher un resume a l'utilisateur (chemin du draft + rappel
   "a toi d'arbitrer, SOP section 3"). Ne jamais toucher le vault, ne rien
   promouvoir.

## 7. Garanties de gouvernance

Ce qui rend l'integration sure : la commande automate uniquement les etapes 1-2
du Cas d'usage 2 deja documente dans la SOP. Elle n'introduit aucune autorite
nouvelle.

- **Chemins d'ecriture en dur** : la commande n'ecrit QUE dans
  `obsidian-bridge/outbox-to-obsidian/` et `obsidian-bridge/logs/`. Les deux sont
  cote projet, contenus gitignores. C'est un sous-ensemble strict de ce que la
  SOP section 8.1 autorise deja.
- **Vault jamais touche** : aucune ecriture vers `D:\...\12_Obsidian\schoolsWP\`.
  La commande n'a pas besoin de connaitre le chemin du vault.
- **Aucune promotion** : la commande ne deplace rien en zone stable, ne cree
  aucune entree dans le `log.md` du vault. Elle s'arrete au gate.
- **Draft auto-marque `status: a-arbitrer`** : le draft se signale lui-meme comme
  necessitant le L0 de Michaël.
- **Asymetrie et append-only intacts** : la SOP v1.1 ne bouge pas. La commande
  est un raccourci pour un workflow que la SOP decrit deja.

Verite testable : *les chemins d'ecriture de la commande sont un sous-ensemble de
SOP section 8.1*. Toute ecriture hors de ces deux dossiers est un bug, pas une
zone grise.

## 8. Gestion du champ `fichiers_sources`

Le template `synthese.md` a un champ frontmatter `fichiers_sources:` concu pour
des fichiers locaux. Les sources de veille sont surtout des URLs.

**Decision** : ne pas modifier le template versionne. La commande met les URLs et
les chemins locaux dans le champ `fichiers_sources:` existant, malgre son nom.
Choix le plus conservateur : aucun fichier de la passerelle touche.

## 9. Gestion d'erreurs

- `<sujet>` manquant : demander, stopper.
- Aucune source : demander, stopper.
- Une source echoue au fetch : la noter, continuer avec les autres. Les sources
  en echec sont listees explicitement dans "Sources consultees" (marquees echec)
  et signalees dans "Questions restantes". Ne jamais avorter toute la veille pour
  une URL morte.
- Toutes les sources echouent : ne pas ecrire un draft vide. Reporter l'echec a
  l'utilisateur, stopper.
- Fichier de log du jour absent : le creer (cas normal, pas une erreur).

## 10. Test et acceptation

Une commande slash est un fichier de prompt, pas unit-testable. La verification
est un smoke test manuel : lancer `/veille` avec 2-3 vraies sources sur un vrai
sujet, puis valider la checklist d'acceptation :

- draft cree au bon chemin et au bon nommage (`YYYY-MM-DD_synthese_<sujet>.md`) ;
- frontmatter valide et conforme au template `synthese.md` ;
- structure du draft conforme aux 8 sections de `synthese.md` ;
- entree de log appendee dans `obsidian-bridge/logs/YYYY-MM-DD_actions.md` ;
- vault intact (aucune ecriture hors `obsidian-bridge/`) ;
- commande arretee au gate (resume affiche, aucune promotion).

Ce smoke test est le critere d'acceptation de l'implementation.

## 11. Criteres de succes

- Une veille qui demandait un gros effort de synthese manuelle devient :
  `/veille` + coller les sources + une passe de relecture.
- Le draft atterrit pret-a-arbitrer : frontmatter valide, structure valide, logge.
- Zero surface de gouvernance ajoutee, prouvable : chemins d'ecriture de la
  commande inclus dans SOP section 8.1.

## 12. Note de coherence a reconcilier

La SOP section 5.1 documente le nommage du log projet comme
`YYYY-MM-DD_actions.md`. Le fichier existant dans `obsidian-bridge/logs/` est
nomme `bridge-2026-05-04.md`. La commande suit la convention SOP
(`YYYY-MM-DD_actions.md`). A reconcilier par Michaël si la convention reelle
differe de la SOP.

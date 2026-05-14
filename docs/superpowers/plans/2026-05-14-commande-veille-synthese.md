# Commande `/veille` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Creer la slash command `/veille` qui transforme une liste de sources pre-collectees en un draft de synthese structure depose dans la passerelle Obsidian, en s'arretant au gate humain L0.

**Architecture:** Artefact unique, un fichier de prompt `.claude/commands/veille.md`. La commande tourne en session avec les outils de fetch deja disponibles (defuddle CLI, firecrawl MCP, WebFetch), synthetise dans la structure du template `obsidian-bridge/templates/synthese.md`, ecrit un draft dans `obsidian-bridge/outbox-to-obsidian/`, append une entree de log, et stoppe. Aucune ecriture vault, aucun code Python, aucune dependance nouvelle.

**Tech Stack:** Slash command Claude Code (fichier markdown de prompt). Outils invoques au runtime : defuddle (CLI npm globale), MCP firecrawl, WebFetch, Read, Write, Edit, Bash.

**Spec source:** `docs/superpowers/specs/2026-05-14-commande-veille-synthese-design.md`
**Branche:** `feature/commande-veille-synthese`

---

## File Structure

- **Create:** `.claude/commands/veille.md` - la slash command, seul artefact de la feature. Responsabilite unique : decrire la procedure `/veille` (parsing entree, fetch, synthese, ecriture draft, log, stop).
- **Modify:** `CLAUDE.md` (racine projet schoolsWP) - ajouter `/veille` a la liste des slash commands projet (1 ligne).
- **Pas de fichier de test** - l'acceptation est un smoke test manuel (Task 3, checklist de la spec section 10). Une slash command est un fichier de prompt, pas unit-testable.

---

## Task 1: Creer la slash command `.claude/commands/veille.md`

**Files:**
- Create: `.claude/commands/veille.md`

**Known risk:** le hook `prompt-injection-detector` (PreToolUse Write) a un faux-positif documente sur certains motifs shell et backticks (voir memoire `feedback_hook_backtick_bug.md`). Si le Write du fichier est bloque, appliquer le workaround de cette memoire : reformuler les passages declencheurs, ou ecrire le fichier en deux passes (un Write minimal puis un Edit pour completer).

- [ ] **Step 1: Ecrire le fichier de commande**

Ecrire `.claude/commands/veille.md` avec exactement ce contenu :

```markdown
# /veille - Synthese d'un dossier de veille

Transforme une liste de sources deja collectees (URLs, fichiers locaux, extraits colles) en un draft de synthese structure, depose dans la passerelle Obsidian pour ton arbitrage.

Cette commande automate uniquement les etapes 1-2 du Cas d'usage 2 de la SOP (obsidian-bridge/SOP-claude-obsidian-bridge.md, section 3). Elle n'ecrit jamais dans le vault, ne promeut rien, et s'arrete au gate humain L0.

Tous les chemins ci-dessous sont relatifs a la racine du projet schoolsWP (le cwd de la session).

## Entree

Arguments attendus : ARGUMENTS

- Le bloc d'arguments contient le sujet de la veille.
- Les sources sont fournies dans le meme message : URLs en liste, chemins de fichiers locaux, ou extraits de texte colles. Les trois types peuvent etre melanges.

Avant tout traitement :

1. Si le sujet est absent : demande-le, stoppe.
2. Si aucune source n'est fournie dans le message : demande-les, stoppe.

## Etape 1 - Fetch des sources

Pour chaque source, selon son type :

- URL : tente la CLI defuddle via Bash en priorite (CLI npm globale, propre pour la veille article). Si echec, fallback firecrawl_scrape (MCP firecrawl). Si echec a nouveau, fallback WebFetch.
- Chemin de fichier local : tool Read.
- Extrait de texte colle : utilise-le tel quel, pas de fetch.

Gestion d'erreur de fetch :

- Une source echoue : note-la, continue avec les autres. Elle sera listee comme echec dans le draft (section Sources consultees) et signalee dans Questions restantes. N'avorte jamais toute la veille pour une URL morte.
- Toutes les sources echouent : n'ecris pas de draft vide. Reporte l'echec a l'utilisateur, stoppe.

## Etape 2 - Synthese

Synthetise le contenu fetche dans la structure exacte du template obsidian-bridge/templates/synthese.md, 8 sections :

1. Question traitee : une phrase claire.
2. Sources consultees : une ligne par source avec son role dans la synthese. Marque explicitement les sources en echec de fetch.
3. Synthese : texte court, structure.
4. Faits : verifiables, sources.
5. Hypotheses : a confirmer.
6. Idees : exploration libre.
7. Proposition pour le wiki : zone cible suggeree (04_memory/, 05_sop/, 06_decisions/, 07_projects/...), fichier cible, justification, validation requise : oui.
8. Questions restantes : y compris les sources non fetchees.

Barre de qualite : pas d'em-dash ni d'en-dash, pas d'emojis, marque toujours ecrite schoolsWP, tutoiement, concision.

## Etape 3 - Ecriture du draft

Ecris le draft dans le dossier obsidian-bridge/outbox-to-obsidian/ avec le nom :

    DATE_synthese_SUJET-KEBAB.md

ou DATE est la date du jour au format annee-mois-jour, et SUJET-KEBAB est le sujet en kebab-case minuscule, court.

Frontmatter (conforme au template synthese.md), entre deux lignes de trois tirets :

    source: claude-code
    status: a-arbitrer
    type: synthese
    date_creation: (date du jour)
    sujet: (sujet court)
    fichiers_sources:
      - (url ou chemin 1)
      - (url ou chemin 2)

Le champ fichiers_sources liste toutes les sources (URLs et chemins), meme celles en echec de fetch.

## Etape 4 - Journalisation

Append une entree dans le log projet du jour, fichier obsidian-bridge/logs/DATE_actions.md (DATE = date du jour).

Si ce fichier n'existe pas, cree-le. Format de l'entree (SOP section 5.1) :

    ## HEURE - synthese | titre court

    - **Acteur** : Claude Code
    - **Action** : Synthese de veille produite a partir de N sources.
    - **Cible** : obsidian-bridge/outbox-to-obsidian/nom-du-draft.md
    - **Lien vers le draft** : obsidian-bridge/outbox-to-obsidian/nom-du-draft.md
    - **Statut** : draft

## Etape 5 - Stop au gate

Affiche un resume a l'utilisateur :

- chemin du draft produit ;
- nombre de sources traitees et en echec ;
- rappel : a toi d'arbitrer (SOP section 3), le draft est en status a-arbitrer.

Ne touche jamais le vault. Ne promeus rien en zone stable. Ne cree aucune entree dans le log.md du vault. La commande s'arrete ici.

## Garde-fous

- Ecriture autorisee uniquement dans obsidian-bridge/outbox-to-obsidian/ et obsidian-bridge/logs/.
- Toute ecriture hors de ces deux dossiers est un bug.
```

- [ ] **Step 2: Verifier que le fichier est bien forme**

Run:
```
test -f .claude/commands/veille.md && grep -c "^## " .claude/commands/veille.md
```
Expected: le fichier existe, et le grep retourne 7 (sections : Entree, Etape 1, Etape 2, Etape 3, Etape 4, Etape 5, Garde-fous).

- [ ] **Step 3: Verifier l'absence d'em-dash et d'en-dash**

Run:
```
.venv/Scripts/python -c "import sys,io; t=io.open('.claude/commands/veille.md',encoding='utf-8').read(); bad=[c for c in t if c in '–—']; print('BAD' if bad else 'OK')"
```
Expected: `OK`. Si `BAD`, ouvrir le fichier, remplacer chaque tiret long fautif par un tiret simple ou un deux-points, puis relancer.

- [ ] **Step 4: Commit**

```
git add .claude/commands/veille.md
git commit -m "feat: add /veille slash command for veille dossier synthesis"
```

---

## Task 2: Enregistrer `/veille` dans la liste des slash commands du CLAUDE.md projet

**Files:**
- Modify: `CLAUDE.md` (racine du projet schoolsWP)

- [ ] **Step 1: Lire la ligne concernee**

Run:
```
grep -n "Slash commands projet" CLAUDE.md
```
Expected: une ligne s'affiche, contenant la liste des commandes terminee par le mot aidesigner entre backticks.

- [ ] **Step 2: Ajouter `/veille` a la liste**

Avec le tool `Read` puis `Edit` sur `CLAUDE.md`, ajouter `/veille` en fin de liste. L'ancienne valeur attendue de la ligne (verifier le texte exact avec le `Read` requis avant `Edit`) se termine par :

    `/todo`, `/aidesigner`

La nouvelle valeur se termine par :

    `/todo`, `/aidesigner`, `/veille`

Si le texte exact differe (espaces, ordre), adapter l'`old_string` au contenu reel lu, en se contentant d'ajouter `/veille` (entre backticks, precede d'une virgule) a la fin de la liste.

- [ ] **Step 3: Verifier la modification**

Run:
```
grep -c "/veille" CLAUDE.md
```
Expected: `1`.

- [ ] **Step 4: Commit**

```
git add CLAUDE.md
git commit -m "docs: register /veille in project slash commands list"
```

---

## Task 3: Smoke test d'acceptation

Verifie la feature complete contre la checklist d'acceptation de la spec (section 10). Une slash command n'est pas unit-testable : ce test consiste a executer la procedure decrite dans `.claude/commands/veille.md` avec des entrees concretes, puis a valider chaque critere.

**Files:**
- Aucune creation ni modification de code. Le test produit un draft reel dans `obsidian-bridge/outbox-to-obsidian/` (gitignored) et une entree de log dans `obsidian-bridge/logs/` (gitignored).

- [ ] **Step 1: Preparer les entrees du test**

Test deterministe avec deux fichiers locaux qui existent a coup sur (exerce le chemin Read, pas de dependance reseau) :

- Sujet : `passerelle-obsidian`
- Source 1 : `obsidian-bridge/README.md`
- Source 2 : `obsidian-bridge/SOP-claude-obsidian-bridge.md`

- [ ] **Step 2: Executer la procedure `/veille`**

Suivre pas a pas les etapes 1 a 5 du fichier `.claude/commands/veille.md` avec les entrees du Step 1 : fetch des deux fichiers locaux via Read, synthese dans la structure 8 sections, ecriture du draft, append du log, affichage du resume et arret.

- [ ] **Step 3: Verifier le draft produit**

Run:
```
ls obsidian-bridge/outbox-to-obsidian/*_synthese_passerelle-obsidian.md
```
Expected: un fichier existe, nomme `DATE_synthese_passerelle-obsidian.md` (DATE = date du jour).

Puis ouvrir le fichier et verifier :
- frontmatter present avec `source: claude-code`, `status: a-arbitrer`, `type: synthese`, `date_creation`, `sujet`, `fichiers_sources` (les 2 chemins) ;
- les 8 sections de `obsidian-bridge/templates/synthese.md` sont presentes ;
- aucun em-dash, aucun emoji.

Run (controle des tirets longs sur le draft, adapter le glob au nom reel du fichier) :
```
.venv/Scripts/python -c "import io,glob; f=glob.glob('obsidian-bridge/outbox-to-obsidian/*_synthese_passerelle-obsidian.md')[0]; t=io.open(f,encoding='utf-8').read(); print('BAD' if any(c in t for c in '–—') else 'OK')"
```
Expected: `OK`.

- [ ] **Step 4: Verifier l'entree de log**

Run:
```
ls obsidian-bridge/logs/*_actions.md
```
Expected: le fichier `DATE_actions.md` existe. L'ouvrir et verifier qu'il contient une entree `## HEURE - synthese | ...` avec `**Statut** : draft` et le chemin du draft.

- [ ] **Step 5: Verifier que le vault est intact et que la commande s'est arretee au gate**

- Confirmer qu'aucune ecriture n'a eu lieu hors de `obsidian-bridge/outbox-to-obsidian/` et `obsidian-bridge/logs/` : relire la trace d'execution, aucun Write ou Edit sur un chemin du vault (dossier 12_Obsidian), aucune ecriture sur une autre zone.
- Confirmer que le resume final a bien ete affiche et que la procedure s'est arretee sans promotion ni ecriture vault.

Run (confirme qu'aucun fichier suivi par git n'a ete modifie par le test : draft et log sont gitignored) :
```
git status --porcelain obsidian-bridge/
```
Expected: aucune ligne (les artefacts du test sont gitignored, donc invisibles pour git).

- [ ] **Step 6: Statuer**

Si les 5 criteres de la checklist spec section 10 passent (draft au bon chemin et bon nommage, frontmatter valide, structure conforme, log appende, vault intact et arret au gate) : la feature est acceptee.

Le draft de test (`*_synthese_passerelle-obsidian.md`) est un draft reel : Michael decide de l'arbitrer ou de le supprimer manuellement. Pas de suppression automatique (regle data-safety du projet).

Aucun commit pour cette task (les artefacts produits sont gitignored, et aucun code n'a change).

---

## Self-Review

**Spec coverage** (spec `2026-05-14-commande-veille-synthese-design.md`) :
- Section 2 Objectif et Section 4 Approche (slash command unique) : Task 1.
- Section 5 Architecture et contrat d'invocation (parsing sujet et sources, ask-if-missing) : Task 1 Step 1, section Entree.
- Section 6 Flux 6 etapes (fetch, synthese, draft, log, stop) : Task 1 Step 1, sections Etape 1 a 5.
- Section 7 Garanties de gouvernance : Task 1 Step 1, section Garde-fous et Etape 5 ; verifie en Task 3 Step 5.
- Section 8 Champ fichiers_sources (template non modifie, URLs dans le champ existant) : Task 1 Step 1, Etape 3.
- Section 9 Gestion d'erreurs : Task 1 Step 1, Etape 1.
- Section 10 Test et acceptation : Task 3 (checklist complete).
- Section 11 Criteres de succes : couvert par l'acceptation Task 3.
- Section 12 Note de coherence (nommage log DATE_actions.md) : la commande suit la convention SOP comme specifie ; pas d'action de reconciliation dans ce plan (reservee a Michael).

**Placeholder scan :** aucun TBD ni TODO. Le contenu complet de veille.md est dans Task 1 Step 1. Les commandes de verification ont des sorties attendues explicites.

**Type consistency :** les chemins (`obsidian-bridge/outbox-to-obsidian/`, `obsidian-bridge/logs/`), le nommage du draft (`DATE_synthese_SUJET-KEBAB.md`), le format de log et le frontmatter sont identiques entre la spec, le contenu de veille.md (Task 1) et les verifications (Task 3).

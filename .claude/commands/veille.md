# /veille - Synthese d'un dossier de veille

Transforme une liste de sources deja collectees (URLs, fichiers locaux, extraits colles) en un draft de synthese structure, depose dans la passerelle Obsidian pour ton arbitrage.

Cette commande automate uniquement les etapes 1-2 du Cas d'usage 2 de la SOP (obsidian-bridge/SOP-claude-obsidian-bridge.md, section 3). Elle n'ecrit jamais dans le vault, ne promeut rien, et s'arrete au gate humain L0.

Tous les chemins ci-dessous sont relatifs a la racine du projet schoolsWP (le cwd de la session).

## Entree

Arguments attendus : $ARGUMENTS

- $ARGUMENTS contient le sujet de la veille.
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

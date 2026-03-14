# Claude Code: CLAUDE.md vs Rules vs Skills vs Memory

Objectif
- Choisir le bon mecanisme d'instructions
- Garder le contexte propre et stable

## 1) CLAUDE.md
- Charge a chaque session
- Conventions de projet et regles globales
- A garder < 200 lignes
- Deplacer le detail dans rules ou skills

Quand l'utiliser
- normes de code
- commandes build/test
- structure du projet
- regles "toujours faire X"

## 2) .claude/rules/
- Charge a chaque session ou sur chemins
- Permet des regles par dossier ou type de fichier
- Evite de surcharger CLAUDE.md

Quand l'utiliser
- regles par dossier (ex: frontend, backend)
- directives specifiques par langage

## 3) Skills
- Chargees a la demande
- Invocables par /skill-name
- Peuvent etre cachees: disable-model-invocation: true

Quand l'utiliser
- flux de travail repetables
- checklists / templates
- docs de reference ponctuelles

## 4) Subagents
- Contexte isole
- Retourne un resume
- Utile pour lecture massive ou parallele

Quand l'utiliser
- recherches lourdes
- audit de code
- comparaison de solutions

## 5) MCP
- Connexion a services externes
- Skills enseignent comment utiliser ces outils

Quand l'utiliser
- base de donnees
- slack / email / navigateur
- services internes

## 6) Memoire (auto-memory)
- Notes auto-ecrites par Claude
- Stockees dans ~/.claude/projects/<project>/memory/
- MEMORY.md charge sur 200 lignes max

Quand l'utiliser
- commandes reccurentes
- preferences decouvertes
- notes de debogage

## Regle simple
- CLAUDE.md = global et stable
- Rules = specifique et local
- Skills = a la demande
- Subagents = isolation
- MCP = outils externes
- Memory = apprentissages automatiques

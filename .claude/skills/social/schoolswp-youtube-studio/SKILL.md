---
name: schoolswp-youtube-studio
description: >
  Skill de production YouTube complet pour schoolsWP. Architecture orchestrateur
  + 5 sous-agents specialises pour produire tous les elements d'une video YouTube :
  script, accroches, titres CTR, concepts de miniatures et SEO YouTube.
  Declencher ce skill des que l'utilisateur mentionne "video YouTube",
  "script video", "creer une video", "optimiser ma video", "titre YouTube",
  "miniature YouTube", "thumbnail", "hook video", "accroche video",
  "SEO YouTube", "description YouTube", ou toute demande liee a la production
  de contenu video pour une chaine YouTube. Fonctionne aussi pour un element
  isole (ex: "trouve-moi un bon titre YouTube" declenche le sous-agent
  Title/CTR Optimizer seul). Meme si la demande ne mentionne pas explicitement
  "YouTube", utiliser ce skill pour toute creation de contenu video pedagogique
  WordPress.
---

# schoolsWP YouTube Studio

Ce skill produit des videos YouTube optimisees pour la chaine schoolsWP. Il s'appuie sur une architecture multi-agents : un orchestrateur central dispatche le travail vers des sous-agents specialises, puis assemble le resultat final.

L'idee derriere cette architecture : chaque aspect d'une video YouTube performante (script, accroche, titre, miniature, SEO) demande une expertise distincte. Les traiter separement puis les assembler produit un resultat plus solide que de tout ecrire d'un bloc.

## Architecture

```
Requete utilisateur
       |
       v
  ORCHESTRATEUR
       |
       |---> Viral Script Writer       -> references/viral-script-writer.md
       |---> Hook Generator             -> references/hook-generator.md
       |---> Title/CTR Optimizer        -> references/title-ctr-optimizer.md
       |---> Thumbnail Idea Generator   -> references/thumbnail-idea-generator.md
       +---> YouTube SEO Agent          -> references/youtube-seo-agent.md
                                                |
                                                v
                                        REPONSE FINALE
```

## Contexte schoolsWP

Chaque sous-agent herite de ce contexte. Il definit le cadre dans lequel le contenu est produit — le respecter garantit la coherence de marque sur toute la chaine.

- **Niche** : WordPress (SEO, automatisation, CRM, LMS, plugins, strategie)
- **Ton** : conversationnel, pedagogique, direct, humain — jamais de jargon sans explication
- **Audience** : freelances, formateurs, createurs, entrepreneurs qui utilisent WordPress
- **Positionnement** : "WordPress. Clair. Structure. Utile."
- **Couleur signature** : vert #00D400
- **Expressions naturelles** : "En clair :", "Teste et approuve.", "Pas de blabla, juste du concret.", "L'idee, c'est de comprendre avant d'appliquer."
- **Outils frequemment mentionnes** : FluentCRM, OttoKit, TutorLMS, Elementor, Fluent Forms, SEOKey, RankMath
- **Ecriture orale** : phrases de 8 a 15 mots, tutoiement naturel, alternance phrases courtes / moyennes

## Orchestrateur — Logique de dispatch

L'orchestrateur est le point d'entree de chaque requete. Son role : comprendre ce que l'utilisateur veut produire, puis activer les bons sous-agents.

### Etape 1 — Analyser la requete

Identifier ces elements (demander si un element manque) :

1. **Sujet** — De quoi parle la video ?
2. **Objectif** — Tutoriel, comparatif, actualite, storytelling, test produit ?
3. **Cible** — Debutant, intermediaire, avance WordPress ?
4. **Format** — Court (3-5 min), standard (8-12 min), long (15-20 min) ?

### Etape 2 — Selectionner les sous-agents

**Mode complet** (par defaut) : activer les 5 sous-agents. C'est le cas quand l'utilisateur demande "creer une video sur X" sans preciser d'element specifique.

**Mode partiel** : activer uniquement le(s) sous-agent(s) pertinent(s). Exemples :
- "Trouve-moi un titre YouTube" -> Title/CTR Optimizer seul
- "Ecris un script video" -> Viral Script Writer + Hook Generator
- "Optimise le SEO de ma video" -> YouTube SEO Agent seul

En mode partiel, lire uniquement la reference du sous-agent active. Demander le contexte minimal necessaire (chaque fichier de reference precise ses prerequis).

### Etape 3 — Executer sequentiellement

Lire chaque fichier de reference active et produire le livrable correspondant. L'ordre d'execution a une logique : les hooks et titres alimentent le script, et le SEO s'appuie sur le contenu final.

Ordre recommande :
1. Hook Generator (les accroches influencent le script)
2. Title/CTR Optimizer (le titre cadre l'angle)
3. Viral Script Writer (le script s'appuie sur le hook et l'angle du titre)
4. Thumbnail Idea Generator (la miniature complete le titre visuellement)
5. YouTube SEO Agent (le SEO s'optimise une fois le contenu defini)

### Etape 4 — Assembler la reponse finale

Template pour le livrable complet :

```
======================================
YOUTUBE STUDIO — [SUJET DE LA VIDEO]
======================================

BRIEF VIDEO
- Sujet : ...
- Objectif : ...
- Cible : ...
- Format : ...
- Duree estimee : ...

--------------------------------------
ACCROCHES D'OUVERTURE (3-5 options)
--------------------------------------
[Livrables du Hook Generator]

--------------------------------------
TITRES OPTIMISES (5-8 options)
--------------------------------------
[Livrables du Title/CTR Optimizer]

--------------------------------------
SCRIPT COMPLET
--------------------------------------
[Livrable du Viral Script Writer]

--------------------------------------
CONCEPTS MINIATURES (3 options)
--------------------------------------
[Livrables du Thumbnail Idea Generator]

--------------------------------------
SEO YOUTUBE
--------------------------------------
[Livrables du YouTube SEO Agent]

======================================
```

## Controle qualite

Avant de livrer, verifier chaque livrable. Ces verifications existent parce que chaque point correspond a une erreur frequente qui fait baisser la performance d'une video :

1. **Le script sonne-t-il naturel a l'oral ?** Les spectateurs decrochent quand le presentateur "lit" au lieu de "parler".
2. **Les hooks creent-ils une tension dans les 5 premieres secondes ?** YouTube mesure la retention des la premiere seconde.
3. **Les titres tiennent-ils en 60 caracteres ?** Au-dela, YouTube tronque et le sens se perd.
4. **Les miniatures sont-elles lisibles sur mobile ?** 70%+ du trafic YouTube vient du mobile.
5. **Le SEO cible-t-il une intention de recherche claire ?** Un mot-cle sans intention = du trafic non qualifie.
6. **Le ton est-il fidele a schoolsWP ?** Clair, direct, utile, humain — jamais de jargon gratuit.
7. **Un debutant WordPress peut-il suivre sans decrocher ?** Si tu perds les debutants, tu perds l'audience cible.

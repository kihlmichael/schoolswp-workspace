---
name: youtube-shorts-schoolswp
description: |
  Pipeline complet de création de YouTube Shorts schoolsWP — script court (150-250 mots), prompts visuels séquentiels, hook en 2 secondes, payoff + CTA funnel. Couvre plusieurs formats : démonstration rapide, avant/après, erreur-piège, face caméra, chiffre surprenant, séries récurrentes. La série "Jusqu'où est-ce trop ?" (format dramatique à ton exceptionnel "choc/peur/urgence") est un cas d'usage parmi d'autres, pas le scope par défaut.
  Utiliser ce skill quand l'utilisateur demande : "Short YouTube", "Shorts", "vidéo courte", "script Short", "Short sur X", "format vertical 9:16", "série schoolsWP", "Jusqu'où est-ce trop ?", "vidéo courte WordPress", "scroll-stopper".
  NE PAS utiliser pour : vidéo YouTube longue (format standard 16:9) (voir `schoolswp-youtube-studio`), conception de miniatures (voir `thumbnail-strategist`), extraction de transcript d'une vidéo existante (voir `youtube-extractor`), pilotage ROI multi-canal (voir `youtube-omnichannel-engine`).
---

# YouTube Shorts schoolsWP — "Jusqu'où est-ce trop ?"

Pipeline en 3 modes pour créer des Shorts WordPress à fort impact. Chaque mode correspond à une
étape du processus de production. Tu peux les enchaîner ou les utiliser séparément selon où en
est l'utilisateur dans sa production.

## Contexte de la série

**Nom** : « Jusqu'où est-ce trop ? »
**Chaîne** : schoolsWP
**Format** : YouTube Shorts (< 60 secondes, lecture orale dynamique)
**Thèmes** : risques et erreurs WordPress — sécurité négligée, plugins obsolètes, backups ignorés,
hébergement sous-dimensionné, mises à jour ignorées, permissions mal configurées, etc.
**Audience** : entrepreneurs digitaux, freelances WordPress, blogueurs, créateurs de formations en ligne
**Ton** : choc, peur, urgence, curiosité — exception assumée au ton habituel schoolsWP, justifiée
par le format dramatique du Short
**Esthétique** : personnage 3D hyper-réaliste face caméra, fond violet uni, dégradation progressive
symbolique, rendu 8K Unreal Engine / Octane Render
**Personnage officiel** : Le Fondateur — voir fiche ci-dessous

## Personnage officiel — Le Fondateur

Ce personnage est fixé pour toute la série. Ne jamais le réinventer d'un épisode à l'autre.
La cohérence visuelle entre les épisodes est ce qui construit la reconnaissance de la série.

**Description** : Entrepreneur quarantenaire. Chemise sobre gris anthracite, col ouvert, manches
non retroussées. Assis naturellement, légèrement en arrière — quelqu'un qui vient de finir sa
journée. Peau entièrement transparente, squelette visible. Traits fins, légèrement marqués par
l'âge. Visage neutre, calme. Les mains posées sur les genoux.

**Ce qui le rend unique** : la dégradation ne vient pas de l'extérieur. Elle vient de dedans.
Le vecteur principal est le regard — des yeux d'une clarté froide, presque professionnels, qui
se vident progressivement. Le viewer se reconnaît. La peur vient de la familiarité, pas de
l'étrangeté.

**Éléments fixes immuables** :
- Chemise gris anthracite col ouvert — présente dans chaque scène, même au climax
- Fond violet uni profond
- Plan buste centré, caméra fixe frontale
- Rendu 8K Unreal Engine 5 / Octane Render

### Système de dégradation — 5 niveaux

La dégradation est cumulative : chaque scène hérite de l'état de la précédente et l'intensifie.

| Niveau | Lumière interne | Regard | Posture | Fissures |
|---|---|---|---|---|
| 1 — Intact | Blanche-ambre 100%, régulière | Clarté froide, professionnelle, 100% | Parfaitement droite | Aucune |
| 2 — Signal faible | 85%, micro-irrégularité | Légèrement moins assurée, 92% | Droite | Aucune visible |
| 3 — Porte ouverte | 78%, zone froide localisée | En retrait, 78% | Épaules -3° | 1 micro-fissure clavicule |
| 4 — Infection silencieuse | Apparemment normale + sphère noire dans cerveau | Vide — ouvert mais ne voit plus rien | Encore tenue à 85% | Inchangées |
| 5 — Effondrement | Quasi-éteinte, résidus rouges | Deux fentes blanches inertes, 20% | 35° en avant, bras tombés | Maximales, noires + liseré rouge |

**Règle clé du niveau 4** : c'est le paradoxe visuel de la série. Le personnage a l'air presque
intact. La chemise est nette. La posture est tenue. Mais le regard est vide et une sphère noire
dense est apparue dans le cerveau. Rien n'alerte. C'est exactement ce que dit le script.

## Règles schoolsWP V2 (toujours actives)

- **Naming** : toujours "schoolsWP" — jamais SchoolsWP, schoolswp, Schoolswp
- **Tutoiement** : systématique en français, sans exception
- **Mots interdits** : disruptif, game changer, scalable, hack, révolutionnaire, incroyable,
  en un clic, sans effort, il suffit de
- **Claims** : aucune promesse non prouvée — "dans mon cas", "sur schoolsWP", "ce que j'observe"
- **Couleurs de référence** : primary `#00D400`, secondary `#00A100`, accent `#E668D4`

## Les 3 modes

### Mode COMPLET — Tout-en-un

Utilise ce mode quand l'utilisateur part de zéro et veut générer le pipeline complet en une seule
passe : personnage → titre → script → prompts visuels.

**Lit le fichier** : `references/prompt-1-complet.md`

Ce prompt produit en une passe :
1. 3 concepts de personnage scroll-stopper (avec choix automatique du meilleur)
2. 8 titres viraux français + sélection du meilleur
3. Script 220-250 mots (Accroche + Étape 1 + Étape 2 + Étape 3 + Climax)
4. Prompt image + Prompt vidéo pour chacune des 5 parties du script

**Usage type** :
> "Crée un Short complet sur le thème : mises à jour WordPress ignorées"
> "Lance le pipeline complet Shorts pour 'permissions de fichiers mal configurées'"

### Mode SCRIPT — Script seul

Utilise ce mode quand le personnage et le titre sont déjà choisis, ou quand l'utilisateur veut
juste un nouveau script pour un thème donné.

**Lit le fichier** : `references/prompt-2-script.md`

Ce prompt produit :
- Script 220-250 mots format strict : Accroche + Étape 1 + Étape 2 + Étape 3 + Climax
- Étapes nommées par temps/quantité (pas de "Étape 1", "La panique", etc.)
- Narration au présent, rythme oral fort, escalade progressive

**Usage type** :
> "Écris juste le script sur 'ton hébergement est surchargé depuis ce matin'"
> "Script Shorts schoolsWP : backups ignorés depuis 6 mois"

### Mode VISUELS — Prompts depuis script existant

Utilise ce mode quand le script est déjà écrit et que l'utilisateur veut générer les prompts
image et vidéo correspondants.

**Lit le fichier** : `references/prompt-3-visuels.md`

Ce prompt produit pour chaque beat narratif visuel distinct :
- 1 prompt image ultra détaillé (posture, regard, lumière, rendu, niveau de dégradation exact)
- 1 prompt vidéo optimisé 3-6 secondes (mouvements subtils, caméra fixe, continuité)

**Usage type** :
> "Génère les prompts visuels pour ce script : [COLLER LE SCRIPT]"
> "Transforme mon script en prompts image/vidéo pour Midjourney et Runway"

## Workflow recommandé

```
[Thème] → Mode COMPLET
          ↓
    Si ajustement script → Mode SCRIPT (nouveau thème ou angle)
          ↓
    Si script OK mais visuels à refaire → Mode VISUELS
```

## Sujets prêts à l'emploi (thèmes schoolsWP validés)

- Sécurité négligée / site ouvert aux hackers
- Plugins obsolètes depuis des mois
- Aucun backup depuis X jours
- Hébergement sous-dimensionné
- Permissions de fichiers mal configurées
- Mises à jour WordPress ignorées
- Mot de passe admin "admin123"
- SSL expiré sans alerte
- Page de login exposée sans protection
- Thème premium piraté installé

## Contraintes visuelles absolues (rappel)

Ces contraintes s'appliquent dans tous les modes — ne jamais s'en écarter :

| Élément | Valeur fixe |
|---|---|
| Type de personnage | 3D hyper-réaliste symbolique |
| Position | Assis, face caméra, centré |
| Cadrage | Plan buste ou plan taille |
| Fond | Violet uni |
| Caméra | Fixe, frontale, aucun mouvement |
| Rendu | 8K, Unreal Engine 5 / Octane Render |
| Dégradation | Progressive, cumulative, jamais gore |
| Leviers de dégradation | Lumière interne, micro-fissures, tremblements, posture, éclat des yeux |
| Interdit | Organes, sang, violence, déchirure, changement de décor |

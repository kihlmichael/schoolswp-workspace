# Thumbnail Idea Generator

Ce sous-agent produit 3 concepts visuels de miniatures detailles et realisables.

La miniature et le titre forment un duo. Le titre cree la promesse, la miniature la rend visuelle et emotionnelle. Sur YouTube, la miniature est souvent vue avant le titre — c'est elle qui arrete le scroll. Son role n'est pas d'expliquer la video, mais de provoquer la curiosite en un coup d'oeil.

## Prerequis (mode partiel)

Quand ce sous-agent est active seul, demander :
- Le sujet de la video
- Le titre de la video (pour completer visuellement sans repeter)

## Principes de design

- **3 elements visuels max.** Au-dela, l'oeil ne sait plus ou se poser — surtout sur mobile (~3cm).
- **Texte overlay de 3-5 mots max.** Ne repete pas le titre. Le complete avec un angle emotionnel.
- **Contraste fort.** Fond blanc (desktop) et fond sombre (mobile/TV). Contraste fort = lisible partout.
- **Visage avec emotion.** L'oeil humain est attire par les visages. Expression marquee = connexion instantanee.
- **Lisibilite mobile.** 70%+ du trafic YouTube vient du mobile. Tester : comprehensible en 1,5 cm de large ?

## Palette schoolsWP

- **Accent principal** : vert #00D400
- **Fond** : blanc, gris clair, ou fond fonce pour contraste
- **Typographie** : epaisse, sans serif, majuscules pour le texte overlay
- **A eviter** : degrades complexes, textures chargees, plus de 3 couleurs

## Format de livraison

```
CONCEPT [N] — [Nom court du concept]
--------------------------------------
Disposition    : [description du layout]
Texte overlay  : "[3-5 mots]"
Typographie    : [style]
Couleurs       : [couleurs dominantes + accent]
Expression     : [emotion du visage]
Element visuel : [icone, fleche, capture d'ecran, logo]
Pourquoi ca marche : [1-2 phrases — mecanisme visuel exploite]
```

## Exemple complet

**Input :** Video "5 plugins WordPress gratuits qui changent tout"

```
CONCEPT 1 — Le compteur
--------------------------------------
Disposition    : Visage a gauche (surprise), chiffre "5" geant a droite
Texte overlay  : "5 PLUGINS GRATUITS"
Typographie    : Bold sans-serif blanc, ombre portee noire
Couleurs       : Fond bleu fonce → noir, chiffre 5 en vert #00D400
Expression     : Surprise / yeux ecarquilles
Element visuel : Icone WordPress stylisee derriere le chiffre 5
Pourquoi ca marche : Le chiffre geant attire l'oeil, le visage surpris
cree l'emotion, "GRATUITS" declenche le reflexe de clic.

CONCEPT 2 — La grille
--------------------------------------
Disposition    : 5 icones de plugins en grille (2+3), visage en bas a droite
Texte overlay  : "TU CONNAIS ?"
Typographie    : Bold sans-serif jaune sur bande noire
Couleurs       : Fond blanc, icones colorees, bande noire en bas
Expression     : Interrogation / sourcil leve
Element visuel : Logos des 5 plugins
Pourquoi ca marche : La grille de logos intrigue, la question cree
un gap de curiosite.

CONCEPT 3 — L'avant/apres
--------------------------------------
Disposition    : Split vertical — gauche "AVANT", droite "APRES"
Texte overlay  : "AVANT / APRES"
Typographie    : Bold condensed, rouge a gauche, vert #00D400 a droite
Couleurs       : Gauche desaturee/grise, droite vive/coloree
Expression     : Pas de visage — focus sur la transformation
Element visuel : Captures d'ecran stylisees du dashboard WordPress
Pourquoi ca marche : Le contraste avant/apres cree une promesse
de transformation immediate et tangible.
```

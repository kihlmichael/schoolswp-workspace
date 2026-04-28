# /cocon-batch - Generation parallele de cocons semantiques

Genere tous les briefs SEO d un cocon semantique en batch parallele.

## Usage

/cocon-batch [thematique du cocon]

## Process

1. Analyse : Delegue a l agent Radar pour identifier page pilier + satellites
2. Plan : Presente le plan (pilier + 5-15 satellites) pour validation
3. Batch : Lance /batch pour generer chaque brief en parallele
4. Consolidation : Verifie le maillage inter-pages et genere l index

## Commande batch a lancer apres validation du plan

/batch Generer les briefs SEO complets pour chaque page du cocon.
Pour chaque page produire un fichier Markdown dans content/cocons/thematique/
avec le format brief Radar.

## Structure de sortie

content/cocons/thematique/
  _index.md
  _calendrier.md
  page-pilier-slug.md
  satellite-01-slug.md

## Conseils

- Commencer par les cocons a fort potentiel
- Publier la page pilier en premier
- Relancer tous les trimestres pour etendre le cocon

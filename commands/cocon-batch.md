# /cocon-batch — Génération parallèle de cocons sémantiques

## Description

Cette commande génère en batch tous les briefs SEO d'un cocon sémantique.
Elle utilise `/batch` sous le capot pour paralléliser la création de chaque page satellite.

## Usage

```
/cocon-batch [thématique du cocon]
```

### Exemples

```
/cocon-batch sécurité WordPress
/cocon-batch monétisation WordPress
/cocon-batch OttoKit automatisation
/cocon-batch FluentCRM email marketing WordPress
```

## Process

### Phase 1 : Recherche et planification

Avant de lancer le batch, l'agent SEO Radar doit :

1. **Identifier la page pilier** : titre, URL, mot-clé principal
2. **Lister les pages satellites** (5-15 pages) avec pour chacune :
   - Titre provisoire
   - Mot-clé principal
   - Intention de recherche
3. **Définir le maillage interne** : chaque page satellite → page pilier + 2 pages voisines
4. **Proposer un calendrier de publication** : ordre de priorité

### Phase 2 : Exécution parallèle via /batch

Une fois le plan validé, lancer :

```
/batch Générer les briefs SEO complets pour chaque page du cocon [thématique].
Pour chaque page, produire un fichier Markdown dans content/cocons/[thematique]/
avec : URL slug, mot-clé principal, mots-clés secondaires, requêtes GEO,
structure H2/H3, maillage interne bidirectionnel, bloc AIO-ready, CTA recommandé.
```

Chaque agent parallèle travaille sur 1 page satellite dans son propre worktree.

### Phase 3 : Consolidation

Après le batch :
1. Vérifier la cohérence du maillage inter-pages
2. Valider l'absence de cannibalisation de mots-clés
3. Générer le fichier index du cocon (`_index.md`)
4. Créer le calendrier éditorial final

## Structure de sortie

```
content/cocons/[thematique]/
├── _index.md                    # Vue d'ensemble du cocon
├── _calendrier.md               # Ordre de publication
├── page-pilier-[slug].md        # Brief page pilier
├── satellite-01-[slug].md       # Brief satellite 1
├── satellite-02-[slug].md       # Brief satellite 2
├── ...
└── satellite-XX-[slug].md       # Brief satellite N
```

## Format de chaque brief

```markdown
# [Titre de la page]

## Métadonnées SEO
- **URL :** /[slug]/
- **Mot-clé principal :** [requête]
- **Volume estimé :** [si dispo]
- **Intention :** [info | transac | comparaison]
- **Mots-clés secondaires :** [3-5]
- **Requêtes conversationnelles GEO :** [2-3]

## Structure du contenu

### H1 : [Titre optimisé]

### H2 : [Section 1]
- H3 : [Sous-section]
- H3 : [Sous-section]

### H2 : [Section 2]
...

### H2 : FAQ
- H3 : [Question 1] → [Réponse directe]
- H3 : [Question 2] → [Réponse directe]

## Maillage interne
- → [Page pilier] (ancre : "[texte]")
- → [Satellite voisin 1] (ancre : "[texte]")
- → [Satellite voisin 2] (ancre : "[texte]")
- ← [Pages existantes qui doivent pointer ici]

## Bloc AIO-ready
### Réponse rapide
[2-3 phrases répondant directement à l'intention]

### Points clés
- [Point 1]
- [Point 2]
- [Point 3]

## CTA recommandé
[Type + destination + texte suggéré]

## Notes de rédaction
[Angle, ton, longueur cible, exemples concrets à inclure]
```

## Conseils

- Commencer par les cocons à fort potentiel SEO (volume + faible concurrence)
- Publier la page pilier en premier, puis les satellites par ordre de priorité
- Mettre à jour le maillage au fur et à mesure des publications
- Relancer `/cocon-batch` tous les trimestres pour étendre le cocon

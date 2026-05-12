# Format : Article de blog schoolsWP

## Objectif

Eduquer et apporter une solution concrete et actionnable a un probleme WordPress.

## Longueur

1200 a 2500 mots selon la complexite du sujet.

## Avant de rediger (etape 0)

Pour tout article visant un mot-cle SEO, executer la recherche concurrentielle BRAND_RULES regle 32 avant d'ecrire :

- 3 a 5 URLs top-ranked analysees
- angles dominants identifies
- 3 manques a exploiter listes
- angle schoolsWP retenu en 1 phrase

Archiver ces livrables dans `content/decisions/<slug>.md` ou en tete du brief. Si l'article n'apporte rien de plus que le top 3 actuel, ne pas le publier.

## Structure obligatoire

```markdown
# [Titre — H1 unique, clair, oriente benefice ou probleme]

## Reponse rapide

[Resume en 2-3 phrases. Le lecteur presse repart avec l'essentiel.]

## Points cles

[Promesse pedagogique orientee benefice lecteur, snippet-friendly. 3 a 5 bullets, 8 a 12 mots chacun. Zero emoji. Pensee pour cibler le featured snippet Google.]

- [Point 1 — benefice concret 8-12 mots]
- [Point 2 — benefice concret 8-12 mots]
- [Point 3 — benefice concret 8-12 mots]
- [Point 4 — optionnel]
- [Point 5 — optionnel]

---

## [Accroche — H2 qui nomme le probleme ou pose la question]

[2-3 paragraphes : probleme, contexte, promesse.]

## [Solution / Methode — H2 descriptif]

[Etapes, exemples, captures. Sous-sections H3 si besoin.]

### [Sous-partie 1 — H3]

[Explication + exemple concret.]

### [Sous-partie 2 — H3]

[Explication + exemple concret.]

## [Application concrete — H2]

[Comment le lecteur peut appliquer ca chez lui, maintenant.]

## FAQ

### [Question frequente 1 ?]

[Reponse directe. Pas de paragraphe introductif.]

### [Question frequente 2 ?]

[Reponse directe.]

## En resume

[Synthese en 2-3 phrases. Rappel de la valeur principale.]

[CTA doux — lien utile, outil recommande, ou invitation newsletter.]

## Sources & ressources

[Section conditionnelle — uniquement si l'article cite des donnees, etudes, benchmarks ou outils externes. Voir BRAND_RULES regle 33.]

- *titre source* - editeur - annee
- *titre source* - editeur - annee
```

## Regles specifiques aux articles

- Le H1 est unique. Jamais deux H1.
- Les H2 sont descriptifs et autonomes (comprehensibles hors contexte).
- Les H3 sont reserves aux sous-parties des H2 et aux questions FAQ.
- La section "Reponse rapide" est obligatoire pour le SEO et la lisibilite.
- La section "Points cles" est obligatoire (3-5 bullets, 8-12 mots, benefice lecteur, snippet-friendly).
- La section "En resume" est obligatoire.
- La FAQ contient 2-5 questions, chacune en H3 avec reponse directe.
- La section "Sources & ressources" (H2) est obligatoire si l'article cite des donnees externes. Format : *titre source* - editeur - annee. Liens sortants en `rel="noopener"`. Voir BRAND_RULES regle 33.

## Exemple d'intro type

> Tu envoies tes emails manuellement a chaque nouveau contact ?
>
> C'est normal au debut. Mais des que tu depasses 50 abonnes, ca devient ingerable.
>
> La solution : automatiser avec FluentCRM.
>
> Dans cet article, je te montre comment creer ta premiere automatisation email en moins de 15 minutes. Meme si tu debutes.

## Mots-cles et SEO

- Integrer le mot-cle principal dans le H1 et le premier paragraphe.
- Utiliser des variantes naturelles dans les H2.
- Pas de bourrage de mots-cles. Jamais.
- Les liens internes vers d'autres articles schoolsWP sont encourages.

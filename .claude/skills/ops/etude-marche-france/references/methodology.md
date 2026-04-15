# Methodologie de Recherche — Etude de Marche France

## 1. Registre de sources

Chaque source recoit un identifiant incremental `[web:N]` attribue dans l'ordre de decouverte.
Le registre complet est publie en section G du livrable.

Format : `[web:N] Nom du site — Titre de la page (Mois Annee)`

Exemples :
```
[web:2] Codeur.com — Prix site WordPress 2025 (Nov 2024)
[web:54] Paul Vengeons — Tarif article SEO 2025 (Mar 2025)
[web:74] Legavox — Contrats abusifs AXECIBLES (Jan 2024)
```

## 2. Regles de croisement des tarifs

### Principe : un tarif n'est fiable que s'il est confirme par plusieurs sources independantes.

| Nombre de sources | Statut | Marquage |
|-------------------|--------|----------|
| 5+ sources independantes | Confirme | Fourchette directe |
| 3-4 sources | Probable | Fourchette + note "3-4 sources" |
| 1-2 sources | Estime | `[ESTIME]` + justification |
| 0 source | Non publie | Ne pas inclure dans le tableau |

### Sources independantes = sources qui ne se citent pas mutuellement.
- Un article qui cite un autre article = 1 source, pas 2
- Deux agences publiant leurs propres tarifs = 2 sources independantes
- Un comparateur qui agrege des tarifs publics = 1 source

### Justification des estimations `[ESTIME]`

Quand un tarif est estime, toujours justifier par l'une de ces methodes :
1. **TJM x jours** : "Estime : audit technique 4-8h freelance (TJM ~450 EUR/jour)" [web:95]
2. **Marge sectorielle** : "Estime : agence +20-30 % vs. freelance, premium +40-60 % vs. agence"
3. **Extrapolation** : "Estime : base sur [offre similaire sourcee] + complexite supplementaire X"

## 3. Fiabilite des avis

### Plateformes acceptees (par ordre de fiabilite)
1. **Trustpilot** — avis verifies, volume important
2. **Sortlist** — specifique agences, avis pro verifies
3. **Google Reviews** — volume, mais moins filtre
4. **Clutch** — specifique B2B, avis detailles
5. **Malt / Codeur** — specifique freelances France

### Criteres de selection
- Minimum 20 avis pour etre cite comme "avis verifies"
- Note mentionnee avec nombre d'avis : "4.9/5 (50+ avis)"
- Date des avis : privilegier les avis < 12 mois
- Avis negatifs : utilises en section E (plaintes), cites individuellement

### Red flags (ne pas citer comme source fiable)
- < 5 avis
- Avis tous publies le meme jour
- Que des notes 5/5 sans texte
- Plateforme inconnue ou auto-hebergee

## 4. Jurisprudence

### Sources acceptees
- **Legifrance** — decisions de justice officielles
- **Village Justice** — analyses juridiques par avocats
- **Legavox** — cas pratiques et jurisprudence
- **Cours d'appel** — decisions citables (ville + annee)

### Format de citation
```
Cas jurisprudence (Cour d'appel [Ville] [Annee]) : [Resume en 1 phrase]. [web:N]
```

### Ce qui n'est PAS de la jurisprudence
- Avis d'un avocat sur un blog (= opinion)
- Article de presse relatant un litige (= source secondaire)
- Plainte DGCCRF sans suite judiciaire (= signalement, pas jurisprudence)

Ces sources restent utiles pour les plaintes (section E) mais ne doivent pas etre presentees
comme jurisprudence.

## 5. Strategie de recherche web

### Methode eprouvee : 10 requetes ciblees puis redaction directe

Les tests montrent qu'un budget de 10 requetes web bien ciblees suffit a produire un livrable complet
de 200-360 lignes. Depasser 20 requetes est contre-productif (temps perdu, pas de gain qualitatif).

### Construction des 10 requetes

Repartir les 10 requetes sur 4 axes :

1. **Marche global** (2-3 requetes) :
   - `"marche [sujet] France 2025 chiffre affaires milliards"`
   - `"[sujet] France croissance tendances 2025 2026"`

2. **Tarifs et offres** (3-4 requetes) :
   - `"[sujet] tarifs prix France 2025"` / `"combien coute [sujet]"`
   - `"[concurrent1] [concurrent2] tarifs avis comparatif"`
   - `"freelance [sujet] TJM France"` ou `"[sujet] prix agence vs freelance"`

3. **Concurrents** (2-3 requetes) :
   - `"[sujet] agence France classement top meilleur 2025"`
   - `"[concurrent specifique] avis clients equipe"`

4. **Plaintes et risques** (1-2 requetes) :
   - `"[sujet] arnaque plainte avis negatif France"`
   - `"[sujet] DGCCRF probleme litige contrat"`

### Outils par preference

1. **WebSearch** : recherches Google classiques — ideal pour tarifs, avis, actualites
2. **firecrawl_search** / **web_search_exa** : recherches semantiques — ideal pour articles de fond
3. **WebFetch** : scraper une page specifique (page tarifs, article juridique)

### Budget requetes

| Phase | Requetes | Objectif |
|-------|----------|----------|
| Recherche | 10 (max) | Cartographier marche + tarifs + concurrents + plaintes |
| Redaction | 0 | Rediger le livrable complet A-G en une seule passe |
| **Total** | **10** | — |

Ne pas relancer de recherches pendant la redaction. Si une donnee manque, marquer `[ESTIME]`.

## 6. Fenetre de recency

- **Prioritaire** : sources datees des 18 derniers mois (fenetre glissante)
- **Acceptable** : sources de 18-36 mois si l'information est structurelle (ex: jurisprudence)
- **A eviter** : sources > 3 ans sauf reference historique

Toujours mentionner la date de la source dans le registre.
Si une source ne date pas son contenu, marquer `(date non precisee)` et baisser sa priorite.

## 7. Qualite redactionnelle

- Langue : francais
- Tarifs : toujours en EUR HT (sauf mention contraire explicite)
- Pas de copier-coller : paraphraser systematiquement
- Exemples plaintes : toujours anonymiser ("Client A", "Prestataire B")
- Ton : factuel, precis, zero superlatif
- Branding schoolsWP : uniquement en section F (pas dans les sections analytiques A-E)

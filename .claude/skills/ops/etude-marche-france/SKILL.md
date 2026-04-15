---
name: etude-marche-france
description: |
  Realise une etude de marche en temps reel en France sur un sujet donne (niche, secteur, segment B2B).
  Produit un livrable structure complet : executive summary, segmentation marche, tableau tarifs,
  concurrents leaders, plaintes clients sourcees, synthese strategique avec packaging schoolsWP.
  Utilise les outils web (firecrawl_search, web_search_exa, WebSearch, WebFetch) pour sourcer en direct.
  Declenche ce skill des que l'utilisateur mentionne "etude de marche", "analyse marche", "benchmark concurrentiel",
  "etude concurrentielle", "analyse sectorielle", "marche France", "segmentation marche", "tarifs concurrents",
  "plaintes clients secteur", "opportunites marche", "positionnement niche", ou toute demande d'analyse de marche
  B2B en France (TPE/PME/independants). Meme si la demande est vague ("je veux comprendre le marche de X en France"),
  ce skill est le bon point d'entree.
---

# Etude de Marche France — Skill d'Analyse Temps Reel

Ce skill produit une etude de marche professionnelle, sourcee en temps reel, sur n'importe quelle niche B2B en
France. Le livrable final est un document Markdown de 8.000-15.000 mots structure en 7 sections (A-G), avec
tarifs croises, concurrents analyses, plaintes sourcees et packaging strategique schoolsWP.

## Parametres d'entree

L'utilisateur fournit au minimum :
- **Sujet / niche** : ex. "WordPress B2B", "formation en ligne", "cybersecurite PME"
- **Segment cible** : ex. "TPE/PME/independants", "ETI", "startups"

Parametres optionnels (sinon le skill les determine automatiquement) :
- **Perimetre geographique** : France par defaut (regions specifiques possibles)
- **Fenetre de recency** : 18 mois glissants par defaut
- **Focus particulier** : ex. "pricing", "concurrents SEO", "plaintes DGCCRF"

## Pipeline d'execution

Le skill s'execute en 2 phases strictes. La cle : rechercher vite (10 requetes ciblees), puis rediger
le livrable complet en une seule passe. Ne PAS faire 50+ requetes — cela epuise le budget sans
ameliorer la qualite.

### Phase 1 — Recherche ciblee (10 requetes web, pas plus)

**Objectif** : Collecter les donnees essentielles en 10 recherches maximum.

Construire 10 requetes qui couvrent les 4 axes du livrable :

1. **Marche global** (2-3 requetes) :
   - `"marche [sujet] France 2025 chiffre affaires milliards"`
   - `"[sujet] France croissance tendances 2025 2026"`

2. **Tarifs et offres** (3-4 requetes) :
   - `"[sujet] tarifs prix France 2025"` / `"combien coute [sujet]"`
   - `"[concurrent1] [concurrent2] tarifs avis comparatif"`
   - `"freelance [sujet] TJM France"` ou `"[sujet] prix agence vs freelance"`

3. **Concurrents** (2-3 requetes) :
   - `"[sujet] agence France classement top meilleur 2025"`
   - `"[concurrent specifique] avis clients taille equipe"`

4. **Plaintes et risques** (1-2 requetes) :
   - `"[sujet] arnaque plainte avis negatif France"`
   - `"[sujet] DGCCRF probleme litige contrat"`

Adapter les requetes a la niche. Les exemples ci-dessus sont des modeles — utiliser les termes
specifiques du secteur etudie.

### Phase 2 — Redaction complete du livrable (0 nouvelles requetes)

**Objectif** : Rediger les 7 sections A-G en une seule passe a partir des donnees collectees.

Des que les 10 recherches sont terminees, COMMENCER A REDIGER immediatement. Ne pas relancer de
recherches. Si une donnee manque, marquer `[ESTIME]` et continuer.

Ordre de redaction :
1. **Section A** — Executive Summary (synthese du marche)
2. **Section B** — Segmentation (3 segments adaptes a la niche)
3. **Section C** — Tableau tarifs (croiser les donnees trouvees)
4. **Section D** — Concurrents leaders (6+ acteurs profiles)
5. **Section E** — Plaintes clients (5 principales avec cause/impact/prevention)
6. **Section F** — Synthese strategique schoolsWP (opportunites, risques, 3 offres, garanties)
7. **Section G** — Sources completes (registre [web:N])

Pour la segmentation (section B), identifier les 3 segments naturels du marche :
- Par defaut : Independants/Solo → Petite structure (2-15 pers.) → Premium/Corporate
- Adapter si le marche a une structure differente (ex: SaaS = freemium/pro/enterprise)

Pour le packaging (section F), construire 3 offres adaptees :
- **Offre 1 "Starter"** : entree de gamme, cible TPE/independants
- **Offre 2 "Growth"** : milieu de gamme, cible PME en croissance
- **Offre 3 "Authority"** : haut de gamme, accompagnement long terme

Chaque offre inclut : cible, contenu detaille, delai, pricing EUR HT, marge estimee, upsells.

Les garanties (section F) doivent repondre directement aux 5 plaintes identifiees en section E.

## Format du livrable

Lire `references/template-structure.md` pour le template exact avec toutes les sections et sous-sections.
Le livrable doit suivre cette structure precisement.

## Regles de sourcing

Lire `references/methodology.md` pour les regles detaillees de sourcing et de verification.

Resume des regles critiques :
- Chaque tarif croise avec 5+ sources independantes
- Sources < 18 mois prioritaires (dates 2024-2026)
- Estimates marques `[ESTIME]` avec justification
- Jurisprudence = decisions de cours d'appel validees
- Avis = plateformes verifiees (Trustpilot, Sortlist, Google Reviews, Clutch) avec >= 20 avis min
- Registre sources `[web:N]` incremental, liste complete en section G

## Outils a utiliser

Utiliser les outils web disponibles dans cet ordre de preference :

1. **firecrawl_search** ou **web_search_exa** : recherches semantiques, ideal pour trouver des articles
   de fond, comparatifs, etudes sectorielles
2. **WebSearch** : recherches Google classiques, ideal pour tarifs, avis, actualites
3. **WebFetch** / **firecrawl_scrape** : scraper une page specifique pour extraire des donnees detaillees
   (page tarifs d'un concurrent, article de jurisprudence, fiche Trustpilot)

Paralleliser les requetes quand possible (phases 1-4 peuvent lancer plusieurs recherches en simultane).

## Branding schoolsWP (section F uniquement)

- Nom : **schoolsWP** (toujours cette casse)
- Tutoiement systematique
- Mots interdits : disruptif, game changer, scalable, hack, revolutionnaire, incroyable, en un clic, sans effort
- Ton : expert accessible, factuel, zero bullshit
- Positionnement : contenu + WordPress + automatisation, transparent, ethique

## Exemple de livrable

L'exemple complet pour "WordPress B2B (TPE/PME/Independants)" est disponible dans la conversation
d'origine ou peut etre fourni sur demande. Il fait ~12.000 mots, 120+ sources, et couvre les 7 sections A-G.

Cet exemple est le gold standard en termes de :
- Profondeur d'analyse (6 concurrents detailles, 5 plaintes sourcees)
- Precision des tarifs (tableau multi-segment, variabilite documentee)
- Qualite du packaging (3 offres avec pricing, marge, upsells)
- Rigueur du sourcing (references croisees, jurisprudence)

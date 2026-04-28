# Guide Apify — Scraping structure pour prospection locale

Ce document est un guide de choix pour l'utilisateur qui souhaite enrichir la collecte
au-dela de la recherche web manuelle, en utilisant Apify comme plateforme de scraping.

---

## Quand utiliser Apify

La recherche web (WebSearch + WebFetch) est suffisante pour la plupart des cas :

- Departements de taille moyenne (< 50 prestataires attendus)
- Premieres explorations / cartographies rapides
- Budget zero

Apify devient pertinent quand :

- Tu veux couvrir un territoire large (region entiere, plusieurs departements)
- Tu veux des donnees structurees directement (JSON, pas du HTML a parser)
- Tu veux croiser systematiquement Google Maps + Pages Jaunes + annuaires
- Tu veux automatiser la collecte pour la relancer regulierement

---

## Actors recommandes par source

### Google Maps

**Actor** : `compass/crawler-google-places` (anciennement Google Maps Scraper)

**Configuration type :**

```json
{
  "searchStringsArray": [
    "agence creation site internet",
    "creation site web",
    "agence web",
    "conception site internet",
    "refonte site internet",
    "agence digitale creation site",
    "creation site vitrine",
    "creation site e-commerce",
    "developpement site internet"
  ],
  "locationQuery": "Moselle, France",
  "maxCrawledPlacesPerSearch": 50,
  "language": "fr",
  "includeWebResults": false
}
```

**Strategie multi-niveaux :**

Pour couvrir une region entiere, lancer le scraper 3 fois :

1. **Niveau regional** : `locationQuery: "Grand Est, France"` avec requetes larges
2. **Niveau departemental** : un run par departement (ex: `"Bas-Rhin, France"`, `"Moselle, France"`)
3. **Niveau ville** : un run par ville principale pour les zones sous-representees

**Donnees recuperees :** nom, adresse, telephone, site web, categorie, note, nombre d'avis,
horaires, coordonnees GPS.

**Avantages :** donne l'adresse complete + telephone + site web en une seule passe.
Tres fiable pour la localisation.

**Limites :** ne dit rien sur les services proposes (pas de preuve de creation de site).
Il faut ensuite visiter chaque site web pour qualifier.

### Pages Jaunes

**Actor** : `tri_angle/pagesjaunes-scraper` ou equivalent

**Configuration type :**

```json
{
  "searchQuery": "agence creation site internet",
  "location": "Moselle (57)",
  "maxResults": 100
}
```

**Variantes de requetes recommandees :**

- agence creation site internet
- creation site web
- agence web
- conception site internet
- developpement web
- refonte site internet

**Donnees recuperees :** nom, adresse, telephone, categorie, description, site web.

**Avantages :** description souvent riche (mentionne les technologies et services).
Bonne couverture des TPE/PME locales.

**Limites :** pas toujours a jour, certaines fiches sont obsoletes.

### Sites web (verification creation de site)

**Actor** : `apify/website-content-crawler`

**Configuration type :**

```json
{
  "startUrls": ["liste des URLs de sites recuperes"],
  "maxCrawlPages": 5,
  "crawlerType": "cheerio"
}
```

**Usage :** une fois les sites web identifies via Google Maps ou Pages Jaunes,
crawler les pages "services", "a propos", "mentions legales" pour trouver les
mentions de creation de site internet, conception web, refonte, etc.

**Mots-cles a chercher :** creation de site, conception web, developpement web,
refonte de site, site vitrine, site e-commerce, CMS, WordPress, PrestaShop,
Drupal, Shopify, developpement sur mesure.

---

## Pipeline Apify recommande

```
Etape 1 : Google Maps Scraper (3 niveaux : region > departement > ville)
   → Liste brute : nom, adresse, telephone, site web
   ↓
Etape 2 : Pages Jaunes Scraper (par departement + variantes requetes)
   → Enrichissement : description, categorie
   ↓
Etape 3 : Deduplication (par nom + ville ou site web)
   → Liste unique
   ↓
Etape 4 : Website Content Crawler (sur les sites identifies)
   → Verification preuve creation de site internet
   ↓
Etape 5 : Nettoyage + qualification + priorisation commerciale
   → Base finale
```

---

## Regles de nettoyage post-scraping

1. **Supprimer les annuaires** : si le "site web" pointe vers pagesjaunes.fr, sortlist.com,
   starofservice.com → ce n'est pas un site officiel, c'est l'annuaire lui-meme
2. **Filtrer par code postal** : ne garder que les CP du territoire cible
3. **Deduplication** : grouper par domaine de site web normalise (sans www, sans protocole)
4. **Validation telephone** : format francais 10 chiffres ou +33
5. **URLs cassees** : tester les sites avec un HEAD request, exclure les 404/timeout
6. **Pages SEO locales** : verifier que l'adresse correspond a une presence reelle, pas une page
   SEO generee pour le referencement local

---

## Couts indicatifs Apify (mars 2025)

| Actor                   | Cout approximatif         |
| ----------------------- | ------------------------- |
| Google Maps Scraper     | ~0.50 USD / 100 resultats |
| Pages Jaunes Scraper    | ~0.30 USD / 100 resultats |
| Website Content Crawler | ~1.00 USD / 100 pages     |

Pour un departement moyen : budget total ~2-5 USD.
Pour une region entiere (10 departements) : budget total ~20-50 USD.

---

## Alternative sans Apify

Si tu ne veux pas utiliser Apify :

- **Firecrawl** (disponible comme skill) : scraping + recherche web, retourne du Markdown propre
- **Recherche web directe** (WebSearch + WebFetch) : gratuit, suffisant pour < 50 resultats
- **Google Custom Search API** : si tu veux automatiser via n8n
- **SerpAPI / DataForSEO** : pour les resultats Google Maps structures

Le choix depend du volume et de la frequence de mise a jour souhaitee.

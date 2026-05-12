---
name: local-prospecting-pipeline
description: |
  Pipeline générique de prospection locale B2B en 8 étapes : sources Google Maps + Pages Jaunes + annuaires + Apify, collecte, filtrage, nettoyage, déduplication et qualification d'entreprises par zone géographique et niche. Sortie CSV / Google Sheets / Markdown. Qualité prime sur quantité.
  Utilise ce skill quand l'utilisateur dit : "trouve des agences", "base de prospection", "liste d'entreprises", "prospection locale", "scraping entreprises", "agences niche ville/département", "fichier de prospection", "base contacts B2B", "trouve des prestataires dans zone", ou "veille concurrentielle locale".
  NE PAS utiliser pour : prospection ciblée création de site internet (utiliser `local-prospector` plus spécialisé), étude de marché B2B (utiliser `etude-marche-france`), enrichissement contacts FluentCRM (utiliser MCP `fluentcrm`), ou scraping de contenu éditorial (utiliser `firecrawl`).
---

# Local Prospecting Pipeline

Tu es un analyste senior en prospection locale, scraping ethique, automatisation de collecte de donnees et structuration de bases de contacts B2B.

Ta mission : constituer une base de donnees propre, fiable, dedupliquee et exploitable d'entreprises dans une niche et une zone geographique definies par l'utilisateur.

La qualite prime sur la quantite. Toujours.

---

## Inputs requis

Demande ces informations avant de commencer :

```yaml
niche: ""           # Ex: "agences SEO", "plombiers", "restaurants bio", "studios photo"
zone: ""            # Ex: "Moselle", "Lyon", "Ile-de-France", "Strasbourg"
objectif: ""        # Ex: "prospection commerciale", "veille concurrentielle", "partenariats"
```

Optionnel (infere si non fourni) :

```yaml
villes_cles: []     # Villes principales a cibler dans la zone (auto-detectees si omis)
criteres_inclusion: []  # Ex: "doit avoir un site web", "doit mentionner [service] explicitement"
criteres_exclusion: []  # Ex: "pas de freelances", "pas d'auto-entrepreneurs"
format_sortie: "csv"    # csv, google-sheets, ou markdown
```

---

## Pipeline — 8 etapes sequentielles

### Etape 1 — Definir les sources et les requetes

**Sources a exploiter (par ordre de priorite) :**
1. Google Maps (via recherche web ou Apify si disponible)
2. Pages Jaunes / Annuaires professionnels du secteur
3. Google Search (requetes locales)
4. Sites specialises de la niche
5. LinkedIn (si pertinent et accessible)

**Generer les variantes de requetes :**

A partir de la niche et de la zone, genere au minimum 8 requetes complementaires en variant :
- les synonymes du metier (ex: "agence SEO" / "consultant referencement" / "expert SEO")
- les villes principales de la zone
- les formulations (avec/sans "agence", "cabinet", "studio", "expert", "prestataire")

Exemple pour niche="agences SEO" zone="Moselle" :
```
agence referencement SEO Moselle
agence SEO Metz
expert referencement Thionville
agence web SEO Forbach
consultant SEO Sarreguemines
referencement naturel Moselle
agence webmarketing Metz
```

**Outils disponibles :**
- `mcp__exa__web_search_exa` ou `WebSearch` — recherche web semantique
- `mcp__firecrawl__firecrawl_scrape` — scraper une page pour extraire des donnees
- Apify MCP (si configure) — scraping Google Maps, Pages Jaunes
- `WebFetch` — recuperer le contenu d'une page

Adapte les outils aux MCP disponibles dans la session. Si Apify n'est pas disponible, compense par des recherches web multiples et du scraping cible.

---

### Etape 2 — Collecter largement

Lance toutes les requetes definies a l'etape 1 en parallele quand c'est possible.

Pour chaque resultat, capture :
- Nom de l'entreprise
- Ville
- URL source (fiche Google, page annuaire, site web)
- Indices d'activite (description, categories, mots-cles)

Ne filtre pas encore — collecte tout ce qui peut etre pertinent.

---

### Etape 3 — Filtrer strictement

Ne conserve que les structures qui respectent **tous** ces criteres :
- Implantation dans la zone cible (ou presence locale claire)
- Lien explicite avec la niche ciblee
- Structure identifiable (agence, cabinet, studio, entreprise, consultant identifie)

**Exclus systematiquement :**
- Annuaires et agregateurs
- Marketplaces
- Fiches sans site identifiable
- Entreprises hors zone
- Structures generalistes sans preuve de specialisation dans la niche
- Profils trop flous ou incomplets pour etre exploitables

En cas de doute → classer en "a verifier", pas en "confirme".

---

### Etape 4 — Extraire les donnees utiles

Pour chaque structure retenue, recupere si disponible :

| Champ | Obligatoire | Description |
|-------|-------------|-------------|
| Nom | Oui | Nom de l'entreprise |
| Ville | Oui | Ville d'implantation |
| Adresse complete | Non | Adresse postale |
| Code postal | Non | CP |
| Telephone | Non | Numero principal |
| Email | Non | Email de contact |
| Site web | Oui | URL du site officiel |
| Source | Oui | URL de la fiche source |
| Type de source | Oui | Google Maps / Pages Jaunes / Search / Annuaire pro |
| Activite / specialite | Oui | Description courte de l'activite |
| Preuve de specialisation | Oui | Preuve factuelle du lien avec la niche |
| Niveau de confiance | Oui | Eleve / Moyen / Faible |
| Statut | Oui | Confirme / A verifier / Incomplet |
| Commentaire | Non | Remarques sur les donnees manquantes ou doutes |

**Si une donnee manque, laisser vide. Ne jamais inventer.**

Pour enrichir les donnees manquantes, scrape le site web de l'entreprise avec Firecrawl pour extraire email, telephone, adresse et description des services.

---

### Etape 5 — Nettoyer et normaliser

- Harmonise les noms (casse, accents, abreviations)
- Normalise les villes (nom officiel, pas d'abreviations)
- Normalise les telephones (format +33 X XX XX XX XX ou 0X XX XX XX XX)
- Normalise les URLs (https://, sans trailing slash)
- Supprime les caracteres parasites
- Conserve les champs vides tels quels

---

### Etape 6 — Dedupliquer intelligemment

Fusionne les entrees similaires en comparant :
- Nom proche ou identique
- Meme site web
- Meme telephone
- Meme adresse
- Meme ville + meme activite

Regles de fusion :
- Conserver la version la plus complete
- Fusionner les informations complementaires non contradictoires
- Garder la source la plus fiable
- Documenter la fusion dans le commentaire

---

### Etape 7 — Qualifier chaque ligne

**Niveau de confiance :**
- **Eleve** : entreprise clairement identifiee, implantee dans la zone, specialisation prouvee
- **Moyen** : signaux serieux mais information partielle ou indirecte
- **Faible** : presence plausible mais insuffisamment demontree

**Statut :**
- **Confirme** : donnees suffisantes et coherentes
- **A verifier** : doute sur activite, localisation ou completude
- **Incomplet** : trop peu de donnees mais structure potentiellement pertinente

**Preuve de specialisation :**
Chaque ligne doit contenir une preuve factuelle courte :
- "page service [niche] identifiee sur le site"
- "categorie Google Maps liee a [niche]"
- "description Pages Jaunes mentionne [niche]"
- "portfolio/references visibles dans le domaine"

Sans preuve → statut "A verifier" maximum.

---

### Etape 8 — Produire le livrable

**Format : tableau markdown (par defaut) ou CSV si demande.**

Colonnes exactes :
```
Nom | Ville | Adresse complete | Code postal | Telephone | Email | Site web | Source | Type de source | Activite / specialite | Preuve de specialisation | Niveau de confiance | Statut | Commentaire
```

**Synthese obligatoire a la fin :**
- Nombre total de resultats bruts collectes
- Nombre de resultats retenus
- Nombre de doublons supprimes
- Nombre de resultats exclus
- Principales raisons d'exclusion
- Couverture geographique (villes representees)
- Recommandations pour enrichir la base (sources complementaires, outils)

---

## Qualification par niche — regles specialisees

Certaines niches ont des criteres de qualification specifiques (preuves acceptables, pieges a eviter, requetes recommandees).

**Consulte `references/niche-qualification-rules.md`** quand la niche correspond a l'une de celles documentees (WordPress, SEO, e-commerce). Ce fichier contient :
- les preuves acceptables par ordre de fiabilite
- les mots-cles de detection
- les pieges specifiques a la niche (ex: fausses pages SEO locales pour WordPress)
- les variantes de requetes supplementaires

Si la niche n'est pas documentee, applique les regles generales du pipeline.

### Piege universel : fausses pages SEO locales

Pour toute niche "services web" (agences web, SEO, WordPress, e-commerce), verifier systematiquement que l'entreprise a une **presence physique reelle** dans la zone :
- Verifier les mentions legales / CGV pour le siege social
- Comparer avec la fiche Google Maps
- Exclure les agences nationales qui creent des pages localisees pour 10+ villes

---

## Regles critiques

- Ne rien inventer — jamais
- Ne pas confondre generaliste et specialiste sans preuve
- Ne pas conserver un annuaire comme s'il etait une entreprise
- Ne pas inclure des structures hors zone
- Ne pas privilegier la quantite au detriment de la fiabilite
- En cas de doute : "a verifier" ou exclure
- Toujours privilegier les sources directes et fiables
- Documenter chaque decision ambigue dans le commentaire

---

## Workflow d'execution

1. Collecter les inputs (niche, zone, objectif)
2. Generer les requetes de recherche
3. Lancer la collecte en parallele
4. Filtrer → nettoyer → dedupliquer → qualifier
5. Produire le tableau final + synthese
6. Proposer les prochaines actions (enrichissement, export, integration CRM)

---

## Exemple d'invocation

```
Utilisateur : Trouve-moi toutes les agences SEO en Moselle
```

Parametres inferes :
```yaml
niche: agences SEO / referencement naturel
zone: Moselle (57)
villes_cles: [Metz, Thionville, Forbach, Sarreguemines, Saint-Avold, Sarrebourg]
objectif: prospection commerciale
```

---

## Qualite attendue

**Bonne ligne :**
- Agence identifiee avec site officiel
- Ville dans la zone cible
- Activite dans la niche confirmee par preuve
- Coordonnees coherentes
- Confiance justifiee

**Ligne a exclure :**
- Simple page d'annuaire
- Pas de site officiel
- Specialisation non demontree
- Localisation hors zone ou incertaine
- Doublon evident

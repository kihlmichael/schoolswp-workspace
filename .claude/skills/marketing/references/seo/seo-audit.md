# SEO Audit — schoolsWP Marketing

Audit SEO complet pour sites WordPress : technique, on-page, contenu et autorité.

## Triggers

- "audit SEO", "SEO audit"
- "pourquoi je ne ranke pas"
- "problèmes SEO", "SEO issues"
- "optimisation Google"

## Pré-requis

Avant l'audit, collecter :

```
□ URL du site
□ Objectifs SEO (mots-clés cibles, pages prioritaires)
□ Accès Search Console (recommandé)
□ Accès Analytics (recommandé)
□ Problèmes connus
□ Historique récent (migrations, refonte, pénalités)
```

## Framework d'audit

### Ordre de priorité

```
1. Crawlabilité & Indexation (fondations)
   ↓
2. SEO Technique (infrastructure)
   ↓
3. On-Page (contenu)
   ↓
4. Performance (Core Web Vitals)
   ↓
5. Autorité (backlinks, E-E-A-T)
```

## 1. Crawlabilité & Indexation

### Vérifications robots.txt

```
URL: /robots.txt

□ Fichier accessible
□ Pas de blocage accidentel de ressources importantes
□ Sitemap déclaré
□ Pas de Disallow: / en production
```

**Problèmes WordPress courants** :
- Plugin de maintenance qui bloque les bots
- `Disallow: /wp-admin/` OK, mais pas `/wp-includes/`
- Sitemap non déclaré

### Vérifications sitemap

```
URL: /sitemap.xml ou /sitemap_index.xml

□ Sitemap accessible (200)
□ Format XML valide
□ URLs importantes incluses
□ Pas d'URLs 404 ou redirigées
□ Dernière modification à jour
□ Soumis dans Search Console
```

**Plugins recommandés** : Yoast SEO, Rank Math, XML Sitemap Generator

### Vérifications indexation

```
COMMANDES DE DIAGNOSTIC

site:domaine.com
→ Nombre de pages indexées

site:domaine.com/page-specifique
→ Page spécifique indexée ?

cache:domaine.com/page
→ Version en cache Google
```

**Search Console** :
- Couverture > Pages indexées vs exclues
- Raisons d'exclusion (noindex, canonical, etc.)

### Canonicals

```
□ Chaque page a un canonical
□ Canonical = URL de la page (self-referencing)
□ Pas de canonical vers pages 404
□ Cohérence www vs non-www
□ Cohérence http vs https
□ Trailing slash cohérent
```

**WordPress** : Vérifier les réglages Yoast/Rank Math

## 2. SEO Technique

### Architecture du site

```
□ Structure en silo logique
□ Profondeur max 3-4 clics depuis homepage
□ Breadcrumbs présents
□ Navigation claire
□ URLs propres et descriptives
```

**Structure URL WordPress idéale** :
```
domaine.com/categorie/titre-article/
domaine.com/service/nom-service/
```

### Redirections

```
□ Pas de chaînes de redirections (A→B→C)
□ Pas de boucles de redirections
□ 301 pour redirections permanentes
□ Anciennes URLs redirigées après migration
```

**Outil** : Screaming Frog, Redirect checker

### HTTPS & Sécurité

```
□ SSL valide
□ Pas de mixed content
□ Redirection HTTP → HTTPS
□ HSTS activé (optionnel mais recommandé)
```

### Erreurs à corriger

| Code | Impact | Action |
|------|--------|--------|
| 404 | Haut | Rediriger ou corriger le lien |
| 500 | Critique | Fix serveur immédiat |
| 302 | Moyen | Convertir en 301 si permanent |
| Soft 404 | Moyen | Ajouter contenu ou rediriger |

## 3. On-Page SEO

### Audit par page

Pour chaque page importante :

```
TITLE TAG
□ Présent et unique
□ 50-60 caractères
□ Mot-clé principal inclus (début si possible)
□ Attractif pour le clic

META DESCRIPTION
□ Présente et unique
□ 150-160 caractères
□ Mot-clé inclus naturellement
□ Call-to-action implicite

STRUCTURE Hn
□ Un seul H1 par page
□ H1 contient le mot-clé principal
□ Hiérarchie logique (H1 > H2 > H3)
□ Pas de sauts (H1 > H3)

CONTENU
□ Mot-clé dans les 100 premiers mots
□ Variations sémantiques utilisées
□ Longueur appropriée au type de page
□ Contenu unique (pas de duplicate)
□ À jour et pertinent

IMAGES
□ Alt text descriptif
□ Noms de fichiers optimisés
□ Format optimisé (WebP)
□ Dimensions appropriées
□ Lazy loading

LIENS INTERNES
□ Ancres descriptives (pas "cliquez ici")
□ Liens vers pages importantes
□ Pas de liens cassés
□ Maillage contextuel
```

### Checklist WordPress spécifique

```
□ Yoast/Rank Math correctement configuré
□ Breadcrumbs activés
□ Schema automatique vérifié
□ Pas de "page d'exemple" indexée
□ Pages auteur : indexer ou noindex selon stratégie
□ Archives de date : généralement noindex
□ Tags : consolider ou noindex si thin content
```

## 4. Performance (Core Web Vitals)

### Métriques cibles

| Métrique | Bon | À améliorer | Mauvais |
|----------|-----|-------------|---------|
| LCP | < 2.5s | 2.5-4s | > 4s |
| INP | < 200ms | 200-500ms | > 500ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |

### Audit performance WordPress

```
SERVEUR
□ Hébergement adapté (pas de mutualisé bas de gamme)
□ PHP 8.0+
□ TTFB < 200ms

CACHE
□ Cache page activé (LiteSpeed, WP Rocket, etc.)
□ Cache navigateur configuré
□ Cache objet si possible (Redis)

ASSETS
□ CSS/JS minifiés
□ CSS critique inline
□ JS différé (defer/async)
□ Images optimisées et WebP
□ Lazy loading natif ou plugin

BASE DE DONNÉES
□ Tables optimisées
□ Révisions limitées
□ Transients nettoyés
□ Requêtes lentes identifiées
```

**Référence** : Voir `06_Dev` pour implémentation technique

## 5. Autorité & E-E-A-T

### Profil de backlinks

```
□ Diversité des domaines référents
□ Qualité > Quantité
□ Ancres naturelles (pas sur-optimisées)
□ Pas de liens toxiques évidents
□ Croissance organique
```

### Signaux E-E-A-T

```
EXPERIENCE
□ Contenu basé sur l'expérience réelle
□ Exemples concrets et cas pratiques

EXPERTISE
□ Auteur identifié et qualifié
□ Bio auteur complète
□ Liens vers profils sociaux/LinkedIn

AUTORITÉ
□ Mentions de la marque
□ Citations dans le secteur
□ Présence sociale active

FIABILITÉ
□ Page À propos complète
□ Contact accessible
□ Mentions légales
□ HTTPS
□ Contenu à jour
```

## Format du rapport

### Structure recommandée

```markdown
# Audit SEO — [Domaine]
Date : [Date]

## Résumé exécutif
- Score global estimé : X/100
- Points critiques : X
- Quick wins identifiés : X

## Problèmes critiques (à corriger immédiatement)
1. [Problème] — Impact: Critique
   - Diagnostic : [Description]
   - Solution : [Action]
   - Priorité : 1

## Problèmes importants
[...]

## Quick wins (effort faible, impact visible)
[...]

## Recommandations long terme
[...]

## Annexes
- Liste complète des 404
- Audit des pages principales
- Données Search Console
```

### Scoring par catégorie

| Catégorie | Poids | Score |
|-----------|-------|-------|
| Crawlabilité | 20% | /20 |
| Technique | 25% | /25 |
| On-Page | 25% | /25 |
| Performance | 20% | /20 |
| Autorité | 10% | /10 |
| **Total** | 100% | **/100** |

## Outils recommandés

| Outil | Usage | Gratuit |
|-------|-------|---------|
| Search Console | Indexation, erreurs, performance | ✅ |
| Screaming Frog | Crawl technique | ✅ (500 URLs) |
| PageSpeed Insights | Core Web Vitals | ✅ |
| Ahrefs/SEMrush | Backlinks, keywords | ❌ |
| GTmetrix | Performance détaillée | ✅ |

## Checklist finale

```
□ Crawlabilité vérifiée (robots, sitemap, indexation)
□ Technique audité (redirections, HTTPS, erreurs)
□ On-page analysé (titles, metas, Hn, contenu)
□ Performance mesurée (Core Web Vitals)
□ Autorité évaluée (backlinks, E-E-A-T)
□ Rapport structuré avec priorités
□ Quick wins identifiés
□ Plan d'action fourni
```

## Ressources

- [programmatic-seo.md](programmatic-seo.md) — SEO à grande échelle
- [schema-markup.md](schema-markup.md) — Données structurées
- [06_Dev](../../../06_Dev/) — Implémentation technique

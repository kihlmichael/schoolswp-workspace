# Regles de qualification par niche

Ce fichier contient les criteres de qualification specifiques a certaines niches.
Le pipeline principal les charge automatiquement quand la niche correspond.

---

## WordPress (agences, freelances, studios)

### Preuves acceptables du lien avec WordPress (par ordre de fiabilite)

1. **Mention directe sur le site officiel** : "WordPress", "creation de site WordPress", "developpement WordPress", "maintenance WordPress"
2. **Page service dediee WordPress** sur le site officiel
3. **Portfolio ou cas client mentionnant WordPress**
4. **Description Google Maps / Pages Jaunes mentionnant clairement WordPress**
5. **Metadonnees ou indices faibles** (URLs /wp-content/, site construit sur WP) — uniquement si recoupes avec une autre source fiable

Si aucune preuve claire n'est trouvee : ne pas inclure, ou marquer "A verifier" uniquement si la structure reste potentiellement pertinente.

### Mots-cles de detection WordPress

Rechercher ces termes sur les sites officiels et fiches :
- WordPress, WooCommerce, Elementor, Divi, Gutenberg
- "CMS WordPress", "theme WordPress", "plugin WordPress"
- "maintenance WordPress", "depannage WordPress"
- "site sous WordPress", "migration WordPress"

### Piege specifique : fausses pages SEO locales

Phenomene massif dans la niche WordPress/web : des agences nationales creent des pages SEO ciblant des villes ou elles n'ont aucune presence physique.

**Comment les detecter :**
- L'agence a des pages pour 10+ villes differentes dans toute la France
- L'adresse physique (mentions legales, CGV) est hors de la zone ciblee
- La fiche Google Maps n'existe pas ou est inconsistante avec l'adresse du site
- Le contenu des pages locales est quasi-identique d'une ville a l'autre (template)
- Le SIRET/SIREN revele un siege hors zone

**Action :** exclure systematiquement, meme si la page mentionne la ville ciblee et WordPress.

### Requetes specifiques WordPress

Ajouter ces variantes aux requetes generees par le pipeline :
```
agence WordPress [zone]
creation site WordPress [ville]
expert WordPress [zone]
freelance WordPress [zone]
studio WordPress [zone]
developpeur WordPress [zone]
maintenance WordPress [zone]
agence web WordPress [zone]
creation site internet WordPress [ville]
```

---

## SEO / Referencement

### Preuves acceptables
1. Page service SEO / referencement naturel sur le site
2. Etudes de cas SEO avec resultats chiffres
3. Description Google Maps mentionnant SEO / referencement
4. Certifications Google (Ads, Analytics) — preuve indirecte, combiner avec autre

### Piege specifique
Beaucoup d'agences web generalistes mentionnent "SEO" sans competence reelle. Verifier si c'est un service a part entiere ou juste un mot-cle dans une liste.

---

## E-commerce / WooCommerce

### Preuves acceptables
1. Page service e-commerce / boutique en ligne sur le site
2. Portfolio de boutiques en ligne realisees
3. Mention WooCommerce, Prestashop, Shopify avec expertise demontree

### Piege specifique
Distinguer "creation de boutique en ligne" (service) de "vente en ligne" (l'entreprise vend elle-meme des produits).

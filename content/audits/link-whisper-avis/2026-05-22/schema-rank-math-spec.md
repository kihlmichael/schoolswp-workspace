# Schema Rank Math - post 58166 (link-whisper-avis)

> À appliquer manuellement dans l'éditeur Gutenberg du post 58166.
> Sidebar Rank Math → onglet **Schema** → **Schema Generator**.

## Garde-fou : ne pas perdre l'entité Article

Rank Math peut retirer le schema Article par défaut quand tu ajoutes un schema custom.
Après avoir ajouté Review + FAQ, **vérifie que la liste des schemas du post contient toujours
un schema `Article`**. Si l'Article a disparu : Schema Generator → ajoute un schema **Article**
(laisse les valeurs par défaut, Rank Math les remplit avec les variables du post).

Résultat visé dans le JSON-LD final : `BlogPosting` + `Review` + `FAQPage`.

---

## 1. Schema Review

Schema Generator → **Review** (ou **Software Application** avec bloc Rating, selon ta préférence).

| Champ | Valeur |
| --- | --- |
| Headline / Name | `Link Whisper` |
| Description | `Avis détaillé sur Link Whisper, plugin de maillage interne WordPress, après 21 mois d'utilisation sur schoolsWP.` |
| Rating (note attribuée) | `4.5` |
| Rating Minimum | `1` |
| Rating Maximum | `5` |
| Item Reviewed - Type | `SoftwareApplication` |
| Item Reviewed - Name | `Link Whisper` |
| Operating System | `WordPress` |
| Application Category | `BusinessApplication` |
| Author - Type | `Person` |
| Author - Name | `Michaël KIHL` |

JSON-LD cible :

```json
{
  "@type": "Review",
  "itemReviewed": {
    "@type": "SoftwareApplication",
    "name": "Link Whisper",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "WordPress"
  },
  "author": { "@type": "Person", "name": "Michaël KIHL" },
  "reviewRating": { "@type": "Rating", "ratingValue": "4.5", "bestRating": "5", "worstRating": "1" }
}
```

Note : un avis d'un `SoftwareApplication` est éligible aux étoiles dans la SERP Google.

---

## 2. Schema FAQ (FAQPage)

Schema Generator → **FAQ**. Ajoute les 6 paires question / réponse ci-dessous
(texte identique à la section FAQ déjà présente dans l'article).

**Q1.** Link Whisper est-il gratuit ?
**R1.** Non, il n'existe pas de version totalement gratuite. Une formule freemium donne accès à des fonctions de base, mais les automatisations clés (suggestions avancées, auto-linking, rapports) sont réservées à la version premium.

**Q2.** Combien coûte Link Whisper ?
**R2.** La licence 1 site est à 77 $/an, la licence 10 sites à 167 $/an. Plus tu prends de licences, plus le coût par site baisse. Avec le code schoolsWP10, tu obtiens 10 % de réduction.

**Q3.** Link Whisper ralentit-il mon site ?
**R3.** Non. Le plugin insère des liens internes classiques dans ton contenu. L'analyse se fait côté administration, elle ne pèse pas sur le temps de chargement vu par tes visiteurs.

**Q4.** Link Whisper fonctionne-t-il avec Rank Math et les autres plugins SEO ?
**R4.** Oui. Link Whisper est compatible avec les principaux plugins SEO WordPress. Il gère le maillage interne, là où un plugin SEO gère les métadonnées : les deux se complètent sans conflit.

**Q5.** Que deviennent mes liens si je désinstalle Link Whisper ?
**R5.** Les liens que tu as ajoutés manuellement dans tes articles restent : ils sont écrits dans le contenu. En revanche, les liens générés par l'auto-linking dynamique disparaissent, car ils dépendent du plugin.

**Q6.** Existe-t-il un code promo Link Whisper ?
**R6.** Oui. Le code schoolsWP10 te donne 10 % de réduction sur ta licence Link Whisper.

### Alternative plus rapide pour la FAQ

Plutôt que de retaper les 6 paires dans le générateur, tu peux remplacer la section
FAQ de l'article par un **bloc FAQ Rank Math** (`Rank Math → FAQ by Rank Math`) : il génère
le schema `FAQPage` automatiquement et cohabite avec l'Article. Inconvénient : le rendu
visuel de la section FAQ change (accordéon Rank Math au lieu des H3 + paragraphes actuels).

Note : depuis 2023, Google n'affiche plus les rich results FAQ pour la majorité des sites.
Le schema `FAQPage` reste valide et utile (compréhension d'entité, parsing par les LLM),
mais n'attends pas d'extrait enrichi FAQ visible dans la SERP.

---

## Vérification après application

Une fois le post mis à jour :
1. Ouvre `https://schoolswp.com/link-whisper-avis/`, code source, cherche `application/ld+json`.
2. Le `@graph` doit contenir `BlogPosting` **+** `Review` **+** `FAQPage`.
3. Teste l'URL dans le Rich Results Test de Google : Review + Breadcrumbs doivent ressortir.

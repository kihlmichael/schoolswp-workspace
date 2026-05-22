# FluentPlayer — Plan de formation schoolsWP

> Statut : plan validé, 40 scripts produits et vérifiés contre le plugin installé (2026-05-22). Étape suivante : production vidéo.
> Angle : outcome « la vidéo qui convertit ». Cible : formateurs et créateurs de cours.

## Architecture globale

```text
FluentPlayer/
├── FPL-011 : Quick Start (offerte)                 → Lead magnet · 6 leçons · ~35 min
└── FPL-012 : Masterclass "La vidéo qui convertit"  → 6 modules · 34 leçons · ~4h45
```

**Plateforme** : TutorLMS sur schoolsWP
**Checkout** : FluentCart
**Production** : vidéos HeyGen + voix ElevenLabs (français, tutoiement)
**Builder** : Gutenberg + Kadence Blocks (thème Kadence)

Le Quick Start ne couvre que des fonctions de **FluentPlayer Free** (réalisable sans dépenser un euro). La Masterclass enseigne Free **et** Pro, avec recommandation honnête de Pro via le lien affilié WPManageNinja.

---

## Qu'est-ce que FluentPlayer (rappel produit)

Lecteur vidéo WordPress nouvelle génération par WPManageNinja (éditeur de FluentCRM, Fluent Forms, FluentCommunity, FluentBooking, FluentCart). ADN du produit : la vidéo qui convertit, pas seulement qui se lit.

- **Couches interactives** posées à un timestamp précis : formulaire, capture email, bannière CTA, hotspot cliquable, pub/sponsor, shortcode, bloc Gutenberg minuté.
- **Sources multiples** : self-hosted, YouTube, Vimeo, BunnyCDN, Mux, HLS, audio.
- **Navigation** : playlists, chapitres, sous-titres multilingues, reprise de lecture.
- **Analytics intégrés** : rétention d'audience, taux de complétion, viewers uniques, top vidéos, tendances.
- **Branding** du player et presets réutilisables.
- **Intégration native écosystème Fluent** : FluentCRM, Fluent Forms, FluentCommunity (gratuites) ; Mailchimp, Webhook, Google Analytics, BunnyCDN, Mux (Pro).

Free vs Pro, à retenir : la version Free gère le branding, les chapitres, les couches Formulaire et Capture email, les sources self-hosted / YouTube / Vimeo / audio. La version Pro débloque les playlists, les analytics, les couches CTA / Hotspot / Ad / Shortcode, le contenu minuté, les sous-titres, la reprise de lecture, les presets personnalisables, BunnyCDN / Mux / HLS, Mailchimp / Webhook / Google Analytics.

Pas de documentation officielle publique à ce jour : la formation s'appuie sur les pages produit, les articles de blog FluentPlayer et la vérification directe du plugin installé sur schoolsWP (FluentPlayer Pro 1.0.5).

---

## FPL-011 — FluentPlayer Quick Start (offerte)

**Objectif** : embarquer sa première vidéo FluentPlayer propre et capturer un email dans la vidéo, en environ 30 minutes.
**Rôle** : lead magnet qui nourrit la liste, puis upsell vers la Masterclass.
**Accès** : 100% gratuit, réalisable avec FluentPlayer Free uniquement.

| # | Leçon | Durée |
|---|---|---|
| 1 | Pourquoi un vrai lecteur change tout (ce que l'embed YouTube ne fera jamais) | 5 min |
| 2 | Installer FluentPlayer et créer ton premier média | 6 min |
| 3 | Habiller le player à ta marque : logo, couleurs, preset, poster | 6 min |
| 4 | Découper ta vidéo en chapitres | 6 min |
| 5 | Capturer ton premier email dans la vidéo : couche de capture et FluentCRM | 8 min |
| 6 | Récap et ce que débloque la Masterclass | 4 min |

**Total** : 6 leçons, ~35 min.
**Livrable** : checklist PDF « Ma première vidéo FluentPlayer prête en 30 min ».
**Détails de contenu**

- **Leçon 1** : le problème de l'embed YouTube (publicité, vidéos suggérées, marque YouTube, zéro donnée, zéro capture). Ce que résout FluentPlayer : ton player, tes données, ta conversion.
- **Leçon 2** : installation depuis le répertoire WordPress.org, tour du menu (Media, Playlists, Analytics, Settings), création d'un média dans l'éditeur de blocs, insertion via le bloc FluentPlayer.
- **Leçon 3** : logo, couleurs de la barre de contrôle, choix d'un preset, image d'attente (poster), ratio.
- **Leçon 4** : créer des chapitres, montrer la navigation, expliquer pourquoi les chapitres augmentent la complétion.
- **Leçon 5** : ajouter une couche Capture email ou Formulaire, brancher FluentCRM, choisir le bon moment de déclenchement.
- **Leçon 6** : récapitulatif, puis teaser de la Masterclass (playlists, CTA, hotspots, analytics, ventes in-video).

---

## FPL-012 — Masterclass « La vidéo qui convertit avec FluentPlayer » (premium)

Structure par **système de conversion** : chaque module fait progresser la vidéo d'un cran vers le résultat business, et se termine par un **projet concret** pour le créateur de cours.

Chaque module comprend : leçons vidéo de 4 à 10 min, 1 fiche PDF, 1 livrable réutilisable (preset, template, grille), 1 quiz de validation qui débloque le module suivant.

### Module 1 — Fondations : poser des vidéos rapides et pro (6 leçons, 52 min)

| # | Leçon | Durée |
|---|---|---|
| 1.1 | FluentPlayer Free vs Pro : quoi débloquer, et quand | 8 min |
| 1.2 | Choisir sa source vidéo : self-hosted, YouTube, Vimeo, BunnyCDN, Mux, HLS | 10 min |
| 1.3 | Hébergement vidéo et vitesse de page : ne pas plomber ton site | 10 min |
| 1.4 | L'interface FluentPlayer : menu, Media List et bloc | 8 min |
| 1.5 | Presets : configurer une fois, réutiliser partout | 8 min |
| 1.6 | Branding : logo, couleurs, poster, ratio, titre en surimpression | 8 min |

**Fiche PDF** : arbre de décision « Quelle source vidéo pour quel besoin ».
**Livrable** : preset FluentPlayer aux couleurs de ta marque, prêt à importer.
**Projet** : poser une vidéo de présentation 100% à ta marque, légère et rapide.

### Module 2 — Structurer pour qu'on regarde jusqu'au bout (6 leçons, 46 min)

| # | Leçon | Durée |
|---|---|---|
| 2.1 | Pourquoi la complétion est ta vraie métrique | 6 min |
| 2.2 | Chapitres : découper une vidéo longue | 8 min |
| 2.3 | Sous-titres et langues : élargir ton audience | 8 min |
| 2.4 | Reprise de lecture : l'élève repart où il s'est arrêté | 6 min |
| 2.5 | Playlists : organiser une bibliothèque ou un cours en vidéos | 10 min |
| 2.6 | Layouts et apparence de playlist | 8 min |

**Fiche PDF** : anatomie d'une vidéo qu'on regarde jusqu'au bout.
**Livrable** : template de structuration de playlist ou de cours (Sheets).
**Projet** : transformer une vidéo longue en parcours chapitré, et une série en playlist de mini-cours.

### Module 3 — Capturer des leads dans la vidéo (5 leçons, 44 min)

| # | Leçon | Durée |
|---|---|---|
| 3.1 | La couche interactive : le concept qui change tout | 6 min |
| 3.2 | Capture email in-video : le bon déclencheur au bon moment | 10 min |
| 3.3 | Formulaires Fluent Forms dans la vidéo | 10 min |
| 3.4 | Connecter les leads à FluentCRM : tags, listes, segmentation | 10 min |
| 3.5 | Connecter à Mailchimp ou un autre outil via webhook | 8 min |

**Fiche PDF** : les 5 moments où capturer un email dans une vidéo.
**Livrable** : convention de tags FluentCRM et checklist de couche de capture.
**Projet** : une vidéo-aimant gratuite qui capture des emails et les tague dans FluentCRM.

### Module 4 — Pousser à l'action : CTA, hotspots, ventes (6 leçons, 46 min)

| # | Leçon | Durée |
|---|---|---|
| 4.1 | Bannières CTA : guider sans interrompre | 8 min |
| 4.2 | Hotspots cliquables : rendre la vidéo explorable | 8 min |
| 4.3 | Contenu minuté : afficher un bloc Gutenberg au bon moment | 8 min |
| 4.4 | Couche Ad et sponsor : monétiser un emplacement | 6 min |
| 4.5 | Vendre depuis la vidéo : paiement Fluent Forms in-video | 10 min |
| 4.6 | Shortcodes : intégrer n'importe quoi dans la vidéo | 6 min |

**Fiche PDF** : 3 CTA in-video qui convertissent, avec exemples.
**Livrable** : 3 templates de bannière CTA et un script de vidéo de vente.
**Projet** : une vidéo de vente avec CTA et paiement intégré, sans sortir l'acheteur de la page.

### Module 5 — Mesurer et décider avec les analytics (5 leçons, 42 min)

| # | Leçon | Durée |
|---|---|---|
| 5.1 | Le dashboard analytics FluentPlayer : lire les bons chiffres | 8 min |
| 5.2 | Rétention d'audience : repérer où les gens décrochent | 10 min |
| 5.3 | Complétion, viewers, tendances : quoi en faire | 8 min |
| 5.4 | Google Analytics : croiser vidéo et parcours du site | 8 min |
| 5.5 | Améliorer une vidéo à partir de ses données | 8 min |

**Fiche PDF** : lire ses analytics vidéo sans se noyer.
**Livrable** : grille d'audit vidéo (Sheets).
**Projet** : audit chiffré d'une de tes vidéos et plan d'amélioration.

### Module 6 — Automatiser avec l'écosystème Fluent (6 leçons, 54 min)

| # | Leçon | Durée |
|---|---|---|
| 6.1 | FluentPlayer et FluentCRM : déclencher une automation depuis une vidéo | 10 min |
| 6.2 | FluentPlayer et FluentCommunity : vidéo dans un espace communautaire | 8 min |
| 6.3 | FluentPlayer pour un cours en ligne : structurer un cours en vidéos | 10 min |
| 6.4 | Webhooks et intégrations avancées | 8 min |
| 6.5 | Migration : passer tes anciennes vidéos sur FluentPlayer | 8 min |
| 6.6 | FluentPlayer vs Presto Player, Vimeo, Wistia : le verdict schoolsWP | 10 min |

**Fiche PDF** : le mini-tunnel vidéo, schéma complet.
**Livrable** : blueprint de tunnel vidéo (Notion ou PDF).
**Projet final** : un mini-tunnel vidéo complet, de la vidéo gratuite qui capture jusqu'à la vidéo de vente.

---

## Récapitulatif

| Formation | Modules | Leçons | Durée | Accès |
|---|---|---|---|---|
| FPL-011 Quick Start | 1 | 6 | ~35 min | Gratuit |
| FPL-012 Masterclass | 6 | 34 | ~4h45 | Premium |
| **Total** | **7** | **40** | **~5h20** | |

Détail des durées Masterclass : M1 52 min · M2 46 min · M3 44 min · M4 46 min · M5 42 min · M6 54 min = 284 min (~4h45).

---

## Tunnel de vente, drip et tags

| Étape | Objet | Pricing indicatif |
|---|---|---|
| Lead magnet | FPL-011 Quick Start contre email | Gratuit |
| Séquence welcome | 6 emails sur 6 jours, 1 par étape, push achat à J5-J6 | — |
| Offre de fond | Masterclass FPL-012 | 127 à 167 € |
| Upsell post-achat | Audit vidéo perso 30 min | 47 à 67 € |
| Cross-sell J+14 | Pack presets et templates CTA seul | 17 à 27 € |

**Drip TutorLMS** : déblocage progressif sur 6 à 7 jours (1 module par jour, modules 5 et 6 sur le dernier créneau).

**Tags FluentCRM** :

- `abonne_lead_magnet_fluentplayer` — déclencheur de la séquence welcome
- `acheteur_formation_fluentplayer` — déclencheur de la séquence onboarding élève
- `lang_fr` — langue (décliner en `lang_en` / `lang_de` si la formation est traduite)

**Affiliation** : la Masterclass recommande honnêtement FluentPlayer Pro. Lien cloaké via le mu-plugin d'affiliation (`schoolswp.com/fluentplayer/` redirige vers WPManageNinja avec `?ref=723`). Placement : module 1 (Free vs Pro) et chaque module qui enseigne une fonction Pro.

---

## Annexe — Kit de marque FluentPlayer (pour vignettes et montages)

Assets téléchargés dans [brand-kit/](brand-kit/). À utiliser pour les vignettes de cours, les miniatures vidéo et les montages image.

### Couleurs de marque FluentPlayer

| Rôle | Hex | Usage |
|---|---|---|
| Primaire | `#DD1F13` | Rouge, couleur principale de marque, ton neutre ou représentation de marque |
| Secondaire | `#07090C` | Quasi-noir, boutons et zones de focus |
| Accent | `#0163DD` | Bleu, accents et mises en avant |
| Texte | `#696F84` | Gris, couleur de texte par défaut |

### Logos et icônes

Pack de marque officiel WPManageNinja : `brand-kit/FluentPlayer_Brand_Assets.zip` (vérifié, archive valide, 24 fichiers image).

- **Logos** : 4 variantes (Primary, Secondary, Monotone Dark, Monotone Light), chacune en SVG, PNG et PNG haute résolution.
- **Icônes** : l'icône « F » abstraite, 4 variantes (Primary, Secondary, Monotone Dark, Monotone Light), en SVG, PNG et PNG haute résolution.
- **Structure interne du zip** : `Logos/SVG`, `Logos/PNG`, `Logos/High Res`, `Icons/SVG`, `Icons/PNG`, `Icons/High Res`.

Note : la variante nommée « Monotone White » sur fluentplayer.com correspond au fichier `monotone_light` du pack (logo clair, destiné aux fonds sombres).

### Règles d'usage FluentPlayer à respecter

- Logo plein couleur **uniquement** sur fond blanc, noir ou bleu. Sur une photo, le poser sur une zone claire ou foncée pour garder le contraste.
- Pour les petites tailles : logo small entre 140 et 240 px de large. En dessous de 70 px de haut, utiliser **uniquement l'icône**, jamais le logo empilé.
- Ne jamais altérer les couleurs ni les formes du logo et de l'icône.
- Écrire **« FluentPlayer »** en un seul mot, capitalisation correcte, jamais « Fluent Player » avec une espace. Ne pas l'abréger, ne pas l'employer comme verbe, ne pas le styliser avec une police de marque.
- Ne pas impliquer un partenariat ou une caution sans accord de WPManageNinja.

### Articulation avec la marque schoolsWP

Sur les vignettes de la formation, la marque **schoolsWP** reste dominante (vert signature `#00D400`, fonds light `#F4F5F7` ou dark `#0F1419`). Le logo FluentPlayer sert de sujet du tutoriel :

- Sur fond schoolsWP dark `#0F1419` : utiliser la variante **Monotone Light** du logo ou de l'icône (logo clair).
- Sur fond schoolsWP light `#F4F5F7` : utiliser le logo **plein couleur** (le `#F4F5F7` est assez proche du blanc pour respecter la règle de fond).

---

## Pipeline de production

1. **Recherche** : terminée (site officiel, features, free vs pro, intégrations, brand resources) puis vérification contre le plugin installé.
2. **Plan** : ce document.
3. **Scripts** : produits et vérifiés — Quick Start (6 leçons) et Masterclass (34 leçons), 8 fichiers dans ce dossier.
4. **Production vidéo** : HeyGen + ElevenLabs (français, tutoiement).
5. **Fiches PDF et livrables** : pipeline PDF brand schoolsWP, templates Sheets et Notion publics et dupliquables.
6. **Publication** : TutorLMS sur schoolsWP, quiz et drip configurés, certificat.
7. **Tunnel** : produit FluentCart, séquence welcome FluentCRM, page de vente, article pilier blog pour le SEO.

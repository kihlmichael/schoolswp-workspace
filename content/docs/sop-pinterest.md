# SOP Pinterest — 12 procédures opérationnelles

**Source :** Base de connaissance V3 — 1 606 unités extraites des formations Luc Bermond (100+ comptes Pinterest, plusieurs millions €/an en ads).
**Date :** 2026-04-06
**Usage :** Copier-coller la SOP concernée dans le contexte avant de travailler.

---

## SOP 1 — Lancer un compte Pinterest de zéro

**Objectif :** Créer un compte business solide, optimisé SEO, prêt à recevoir des publicités dans les 48h.

**Durée estimée :** 2-3 heures

**Prérequis :** Site web en ligne avec URL stable. Logo en HD. Bannière 800×450px. Liste de 8-10 thématiques clés de la niche.

### Étapes

1. **Créer le compte business.** Aller sur pinterest.com/business > Créer un compte professionnel. Ne pas convertir un compte personnel existant si possible — partir d'une base propre.

2. **Optimiser le profil immédiatement.**
   - Nom d'utilisateur : mot-clé niche en kebab-case (ex : `decoration-interieure-france`, pas `user123`).
   - Nom du compte : nom du site ou de la marque.
   - Description : 160 caractères avec 3-4 mots-clés principaux. Phrase impactante, pas de jargon.
   - Accroche courte : tagline visible sous le nom, mots-clés en premier.

3. **Ajouter bannière + logo.** Bannière : image ou courte vidéo < 10 Mo. Logo : carré, lisible en miniature. Pinterest utilise ces éléments pour catégoriser le compte.

4. **Revendiquer le site web.** Paramètres > Revendiquer vos contenus > insérer le code de vérification dans le header du site. Valider. Sans cette étape : impossible de lancer des publicités.

5. **Créer 8-10 tableaux thématiques.**
   - Un tableau = une catégorie (ex : "Idées déco salon", "Tendances mode automne").
   - Titre : mot-clé principal + contexte.
   - Description : 200-300 caractères avec synonymes et mots-clés secondaires.
   - Miniature personnalisée : visuel cohérent avec la thématique.
   - Ne jamais cocher "garder ce tableau secret" — un tableau secret ne diffuse pas.

6. **Alimenter chaque tableau : 15-20 épingles minimum.**
   - Priorité aux propres épingles (format vertical 1 000×1 500px).
   - Compléter avec des épingles existantes de qualité pour donner du volume au compte.
   - Titre épingle : 40-60 caractères, mots-clés en premier.
   - Description : 200-300 caractères, 3-5 mots-clés, pas de spam.
   - Renommer les fichiers images avant upload : `mot-cle-principal-contexte.jpg`.

7. **Vérifier le rendu mobile.** Installer l'app Pinterest sur mobile. Vérifier que les titres s'affichent correctement, que les miniatures sont lisibles. 80%+ du trafic Pinterest est mobile.

8. **Créer 5 épingles idées.** Format plein écran multi-slides (5-8 slides) pour nourrir l'algorithme et construire une première audience reciblable. Ces épingles n'ont pas de lien — elles servent à la notoriété.

9. **Installer le pixel Pinterest.** (Voir SOP 2 pour le détail complet.)

10. **Programmer le premier batch de publication.** Planifier avec Tailwind : 5 épingles/jour, horaires variés, pas tout le même jour. Espacer les republications d'une même image entre tableaux : minimum 30 jours d'intervalle.

### Outils nécessaires

- Pinterest Business (gratuit)
- Canva — format épingle 1 000×1 500px
- Tailwind — planificateur (version payante recommandée)
- Keyword Tool (keywordtool.io) — recherche mots-clés Pinterest
- Pinterest Trends — validation volumes

### Erreurs à éviter

- Lancer des publicités sans avoir revendiqué le site.
- Tableaux vides ou avec moins de 5 épingles — l'algorithme ignore les comptes "squelettes".
- Tableaux secrets (ne diffusent pas).
- Balancer 100 épingles le jour 1 — le reach chute. Étaler sur 20 jours.
- Contenu de mauvaise qualité (images floues, format horizontal).
- Publier le même contenu dans plusieurs tableaux le même jour.

### Benchmarks attendus

- Compte bien brandé : 10 tableaux × 15 épingles = 150 épingles au lancement.
- Premières impressions organiques : J+3 à J+7.
- Trafic organique notable en décoration : 1-1,5 mois. En beauté : 3-4 mois.

### Checklist de validation

- [ ] Compte créé en mode Business (pas personnel)
- [ ] Nom d'utilisateur avec mot-clé niche
- [ ] Description profil avec mots-clés
- [ ] Logo + bannière uploadés
- [ ] Site web revendiqué et validé
- [ ] 8-10 tableaux créés (publics, avec description)
- [ ] 15-20 épingles par tableau
- [ ] Pixel installé et vérifié (Tag Helper)
- [ ] Premier batch programmé sur Tailwind

---

## SOP 2 — Installer le tracking Pinterest

**Objectif :** Pixel opérationnel, événements trackés (vue, ajout panier, achat), API Conversion activée. Sans ça, impossible d'optimiser en conversion.

**Durée estimée :** 30-60 minutes

**Prérequis :** Compte Pinterest Business créé. Accès admin au site e-commerce. Extension Chrome "Pinterest Tag Helper" installée.

### Étapes

**Phase 1 — Trouver l'ID du pixel**

1. Aller dans Annonces > Conversions.
2. Cliquer "Créer une balise Pinterest".
3. Nommer la balise (ex : "MonSite - Principal").
4. Copier l'ID de la balise (format numérique).

**Phase 2 — Installer le pixel selon le CMS**

**Sur Shopify :**
1. Apps Shopify > Pinterest for Shopify (app officielle Pinterest).
2. Connecter le compte Pinterest Business.
3. L'app installe automatiquement le pixel + les événements standard (ViewContent, AddToCart, Checkout).
4. Activer la synchronisation catalogue si applicable.

**Sur WooCommerce :**
1. Installer le plugin officiel "Pinterest for WooCommerce" (WordPress.org).
2. Connecter le compte Business via OAuth.
3. L'extension déploie automatiquement la balise + les événements.
4. Cocher "Enhanced Match" (correspondance avancée).

**Sur PrestaShop :**
1. Module Pinterest for PrestaShop (disponible sur PrestaShop Marketplace).
2. Saisir l'ID de balise manuellement.
3. Configurer les événements via l'interface du module.

**Via Google Tag Manager (solution universelle) :**
1. Dans GTM : Nouvelle balise > Balise HTML personnalisée.
2. Coller le code base du pixel Pinterest.
3. Déclencheur : toutes les pages.
4. Créer des balises d'événements séparées pour AddToCart et Checkout avec les déclencheurs correspondants.
5. Publier le conteneur GTM.

**Phase 3 — Vérifier l'installation**

1. Installer l'extension Chrome "Pinterest Tag Helper" (Chrome Web Store, gratuit).
2. Se rendre sur son site e-commerce.
3. Activer l'extension : elle détecte le pixel et les événements déclenchés.
4. Naviguer : page produit (ViewContent), ajouter un produit au panier (AddToCart), aller en caisse (InitiateCheckout).
5. Vérifier que chaque événement apparaît en vert dans Tag Helper.

**Phase 4 — Activer la correspondance avancée**

1. Annonces > Conversions > sélectionner la balise.
2. Activer "Correspondance avancée automatique".
3. Vérifier que des événements remontent dans "Historique des événements" (délai max 30 min).

**Phase 5 — Débloquer l'objectif Conversion**

L'objectif Conversion se débloque automatiquement une fois que Pinterest enregistre des achats ou ajouts au panier.

Si le pixel vient d'être installé et qu'aucun événement n'est encore enregistré :
1. Faire 2-3 faux ajouts au panier sur le site.
2. Attendre 48-72h.
3. Si toujours bloqué : lancer une campagne Trafic avec 50-100€ pour générer des événements.
4. Une fois des checkouts enregistrés : l'objectif Conversion se débloque automatiquement.

**Phase 6 — API Conversion server-side (optionnel, recommandé)**

L'API Conversion complète le pixel côté serveur pour pallier les blocages navigateur (ad blockers, ITP).

1. Dans Pinterest : Annonces > Conversions > API Conversion.
2. Générer un token d'accès API.
3. Configurer côté serveur (ou via l'intégration officielle Shopify/GTM).
4. Les événements côté serveur s'affichent en complément des événements pixel.

### Outils nécessaires

- Pinterest Tag Helper (extension Chrome, gratuit)
- Google Tag Manager (si installation manuelle)
- App officielle Pinterest Shopify/WooCommerce (si applicable)
- Accès admin backend site

### Erreurs à éviter

- Installer le pixel en manuel quand une intégration officielle existe — source d'erreurs.
- Oublier d'activer la correspondance avancée automatique.
- Ne pas tester les événements avec Tag Helper avant de lancer.
- Croire que le pixel suffit sans l'API Conversion (perte de ~20-30% des données sur certains navigateurs).
- Supprimer le pixel pour "réinstaller" — préférer corriger l'installation existante.

### Benchmarks attendus

- Pixel installé correctement : événements visibles dans Tag Helper sous 5 min.
- Historique des événements Pinterest : données visibles sous 24-48h.
- Objectif Conversion débloqué : 48-72h après premiers achats enregistrés.

### Checklist de validation

- [ ] ID balise Pinterest copié depuis Annonces > Conversions
- [ ] Pixel installé via intégration officielle ou GTM
- [ ] Extension Tag Helper installée et vérification effectuée
- [ ] ViewContent, AddToCart, Checkout visibles en vert dans Tag Helper
- [ ] Correspondance avancée automatique activée
- [ ] Événements remontent dans l'historique Pinterest (Annonces > Conversions)
- [ ] Objectif Conversion débloqué
- [ ] API Conversion configurée (si volume > 50 ventes/mois)

---

## SOP 3 — Lancer la première campagne Ads

**Objectif :** Première campagne conversion opérationnelle en moins d'une heure, avec le bon ciblage, le bon budget, et les bonnes créatives.

**Durée estimée :** 45-60 minutes

**Prérequis :** Pixel installé et fonctionnel. Objectif Conversion débloqué. 3-5 créatives verticales prêtes. Landing page cohérente avec les créatives.

### Étapes

**Phase 1 — Créer la campagne**

1. Annonces > Créer une annonce > Campagne.
2. Objectif : **Conversion** — jamais "Trafic" ou "Notoriété" pour un e-commerce, même si un account manager Pinterest le recommande.
3. Nom de campagne : format lisible (ex : `[Produit] - Conversion - FR - [Date]`).
4. Budget : quotidien 5-10€ pour un nouveau compte. Méthode test recommandée : budget total ÷ 10 = budget quotidien (ex : 200€ budget test = 20€/jour × 10 jours).
5. **Ne pas activer Performance Plus au démarrage** — laisser le contrôle manuel pour la phase de test.

**Phase 2 — Configurer le groupe d'annonces**

6. **Ciblage — règle absolue : un seul type par groupe.**
   - Groupe 1 : centres d'intérêt UNIQUEMENT (ex : "Décoration intérieure", "Mode femme"). Taille minimum : 1 million de personnes.
   - Groupe 2 : mots-clés UNIQUEMENT (20-50 mots-clés par campagne). Ne jamais mélanger les deux dans un même groupe.
   - Démarrer avec les centres d'intérêt parents (ex : "Beauté" pas "Démaquillant") — plus large = meilleure optimisation algorithme.

7. **Démographie.**
   - Genre : Femme + **Non précisé** (contient ~80% de femmes, ne jamais décocher).
   - Âge : 25+ ans (ou 25-44 selon le produit).
   - Ne pas cibler "Hommes" pour les produits mixtes — l'audience masculine est trop faible sur Pinterest FR.

8. **Localisation :** France (ou marché cible). Ne pas mélanger plusieurs pays dans une même campagne.

9. **Enchère :** Automatique pour débutants. L'enchère manuelle est réservée aux comptes avec data établie.

10. **Événement d'optimisation :** Sélectionner "Achat finalisé" (Checkout) — pas "Ajout au panier".

**Phase 3 — Ajouter les créatives**

11. Ajouter 3-5 épingles verticales (format 1 000×1 500px ou 9:16).
    - Sélectionner des épingles déjà publiées sur le compte (épingles "naturelles").
    - Ou créer de nouvelles épingles directement.
    - L'algorithme Pinterest sélectionne automatiquement la meilleure créa — lui laisser au moins 3 options.

12. **Vérifier la cohérence créa → landing page.** Si l'épingle montre un produit rouge, la page doit afficher ce produit rouge immédiatement. Pas de redirection vers la homepage.

13. **Prévisualiser sur mobile.** Cliquer "Aperçu de l'épingle" > vérifier sur smartphone. Titre lisible ? Visuel impactant ? CTA visible ?

**Phase 4 — Paramétrer le lancement**

14. **Date de démarrage : lendemain à 01h16 (heure Paris).** Ne jamais lancer en fin de journée — l'algorithme dépenserait tout le budget en 4h. Un lancement à 01h laisse 23h pour dépenser progressivement.

15. **Date de fin :** J+10 (phase de test). Configurer une date de fin automatique pour ne pas oublier.

16. Valider et lancer.

**Phase 5 — Gérer la phase d'apprentissage**

17. **Ne pas y toucher pendant 10 jours.** La phase d'apprentissage dure ~10 jours sur un nouveau compte (3 semaines si très nouveau compte avec zéro historique). Sur un compte existant : 5-6 jours.
18. Pendant les 3-6 premiers jours : perte de performance normale de 40-80% — c'est attendu. Ne pas couper.
19. Regarder les stats 2-3 fois par semaine maximum. Pas quotidiennement.

### Outils nécessaires

- Gestionnaire d'annonces Pinterest
- App Pinterest mobile (pour la prévisualisation)
- Canva ou IA générative pour les créatives (format 1 000×1 500px)

### Erreurs à éviter

- Choisir l'objectif Trafic ou Notoriété pour un e-commerce.
- Mélanger centres d'intérêt ET mots-clés dans le même groupe.
- Démarrer en broad sur un tout nouveau compte.
- Modifier la campagne dans les 10 premiers jours — perturbe l'algorithme, peut relancer une phase d'apprentissage.
- Lancer à 20h ou 22h (budget brûlé en quelques heures).
- N'avoir qu'une seule créative — l'algorithme n'a rien à tester.
- Ne pas vérifier la cohérence créa/landing page avant de lancer.

### Benchmarks attendus

- CPM : 1-1,50€ (France, hors Q4).
- CPC : 10-15 centimes.
- CTR : ~1%.
- CPA cible : variable selon le panier. Panier 50€ → CPA cible 15-20€. Panier 100€ → CPA cible 20-30€.
- ROAS minimum viable : 3x.
- Phase d'apprentissage : 10 jours nouveau compte, 5-6 jours compte existant.

### Checklist de validation

- [ ] Objectif Conversion sélectionné (pas Trafic)
- [ ] Budget quotidien cohérent (budget total ÷ 10)
- [ ] Centres d'intérêt OU mots-clés (jamais les deux dans le même groupe)
- [ ] Taille audience minimum 1 million
- [ ] Genre : Femme + Non précisé
- [ ] Enchère automatique
- [ ] Événement d'optimisation : Achat finalisé
- [ ] 3-5 créatives vertiales chargées
- [ ] Cohérence créa ↔ landing page vérifiée
- [ ] Prévisualisation mobile effectuée
- [ ] Lancement programmé à 01h16 le lendemain
- [ ] Date de fin à J+10 configurée

---

## SOP 4 — Analyser les résultats après 7-10 jours

**Objectif :** Lire les données correctement pour décider : garder, ajuster ou couper. Pas de décision avant J+7 minimum.

**Durée estimée :** 15-20 minutes

**Prérequis :** Campagne en ligne depuis 7 jours minimum. Accès à Annonces > Informations.

### Étapes

**Phase 1 — Configurer le dashboard**

1. Annonces > Informations.
2. Sélectionner la période : depuis le lancement jusqu'à aujourd'hui.
3. Afficher uniquement ces colonnes : Dépenses, Revenus, ROAS, CPA, CTR, CPM, Conversions.
4. Éliminer les autres colonnes pour ne pas se noyer.

**Phase 2 — Lire les métriques dans l'ordre**

5. **CPM (coût pour 1 000 impressions).**
   - Attendu France : 1-1,50€.
   - CPM > 3€ → problème de concurrence ou ciblage trop étroit.
   - CPM < 0,50€ → audience trop large ou faible qualité de créa.

6. **CTR (taux de clic).**
   - Attendu : ~1%.
   - CTR < 0,4% → problème créatif. La créa n'accroche pas, pas le ciblage.
   - CTR > 2% → excellente accroche. Vérifier la landing page si le ROAS est faible.

7. **CPC (coût par clic).**
   - Attendu : 10-15 centimes.
   - CPC > 50 centimes → problème de CTR ou de concurrence.

8. **CPA (coût par achat).**
   - Calculer : Dépenses ÷ Nombre de conversions.
   - CPA < panier moyen ÷ 2 → rentable.
   - CPA > 2x panier moyen → problème sérieux (créa, ciblage ou landing page).

9. **ROAS (Return on Ad Spend).**
   - Calculer : Revenus ÷ Dépenses.
   - ROAS ≥ 3 → campagne rentable, passer au scaling.
   - ROAS entre 1 et 3 → ajuster sans couper.
   - ROAS < 1 après J+14 → revoir le produit, le ciblage ou les pages.

**Phase 3 — Diagnostiquer selon les signaux**

10. **CTR bas + ROAS bas → problème créatif.** Changer les visuels.

11. **CTR correct + ROAS bas → problème landing page.** Tester d'autres pages de destination (page produit vs article éducatif vs landing dédiée).

12. **CTR bas + CPM élevé → problème de ciblage.** Élargir l'audience ou tester un autre centre d'intérêt.

13. **ROAS instable (bon 1 jour, mauvais le suivant) → patience.** L'algorithme est encore en apprentissage. Ne pas toucher avant J+14.

**Phase 4 — Décider**

14. **ROAS ≥ 3 depuis au moins 7 jours consécutifs** → passer à la SOP 5 (scaling).
15. **ROAS entre 1 et 3** → ne pas couper. Changer les créatives (pas le budget, pas le ciblage). Dupliquer le groupe et tester une landing page différente.
16. **ROAS < 1 après 14 jours** → analyser chaque point de la checklist SOP 10. Si tout est OK : tester un autre produit.
17. **Campagne qui ne dépense pas du tout** → enchère trop basse ou ciblage trop étroit. Passer en enchère automatique ou élargir l'audience.

### Outils nécessaires

- Annonces > Informations (dashboard Pinterest Ads)
- Google Analytics ou analytics e-commerce pour croiser les données de revenus

### Erreurs à éviter

- Analyser avant J+7 — les données sont biaisées par la phase d'apprentissage.
- Modifier la campagne en réaction à 2-3 jours mauvais — attendre J+7 minimum.
- Couper une campagne avec CTR correct et ROAS faible sans tester la landing page.
- Se fier uniquement au ROAS sans regarder CTR et CPM — manque de diagnostic.
- Micro-ajustements quotidiens — perturbent l'algorithme.

### Benchmarks de référence (France)

| Métrique | Mauvais | Correct | Excellent |
|----------|---------|---------|-----------|
| CPM | > 3€ | 1-1,50€ | < 0,80€ |
| CPC | > 0,50€ | 0,10-0,15€ | < 0,08€ |
| CTR | < 0,4% | ~1% | > 1,5% |
| ROAS | < 1 | 2-3x | > 5x |
| CPA (panier 100€) | > 50€ | 20-30€ | 12-16€ |

### Checklist de validation

- [ ] Période sélectionnée : depuis le lancement
- [ ] Dashboard configuré : ROAS, CPA, CTR, CPM, Conversions
- [ ] CPM vérifié (1-1,50€ = normal)
- [ ] CTR vérifié (> 0,5% = ok)
- [ ] CPA calculé et comparé au panier moyen
- [ ] ROAS calculé
- [ ] Décision prise : garder / ajuster créative / ajuster page / couper
- [ ] Aucune modification faite avant J+7

---

## SOP 5 — Scaler une campagne gagnante

**Objectif :** Multiplier les résultats d'une campagne rentable sans la casser. Règle d'or : ne jamais augmenter le budget d'une campagne qui fonctionne.

**Durée estimée :** 15 minutes par duplication

**Prérequis :** Campagne avec ROAS ≥ 3 stable depuis au moins 7 jours consécutifs.

### Étapes

**Méthode principale : scaling horizontal (duplication)**

1. **Identifier la campagne gagnante.** ROAS ≥ 3 sur 7 jours consécutifs = signal de scaling.

2. **Ne jamais augmenter le budget de la campagne originale.** Augmenter le budget = relance une phase d'apprentissage + perturbe l'optimisation algorithmique. La campagne originale reste intacte.

3. **Dupliquer la campagne à l'identique.**
   - Annonces > sélectionner la campagne > Dupliquer.
   - Garder exactement le même budget, même ciblage, mêmes créatives.
   - Renommer : `[Campagne originale] - COPIE 1`.
   - Lancer au même horaire (01h16).

4. **Attendre 7-10 jours avant d'évaluer la copie.** La copie repart en phase d'apprentissage.

5. **Si la copie performe aussi (ROAS ≥ 3) → dupliquer à nouveau.** Empiler progressivement : 2 → 4 → 6 → 8 → 10 campagnes identiques.

6. **Objectif de portefeuille diversifié.** 10-20 campagnes en parallèle = stabilité maximale. Si l'une chute, les autres compensent.

**Méthode complémentaire : méthode escalier (augmentation prudente si nécessaire)**

Utilisée uniquement si la duplication ne suffit pas ou si le budget est limité.

1. Budget de départ : 5€/jour.
2. Palier 1 → 10€/jour : attendre 3-5 jours de performance stable avant d'augmenter.
3. Palier 2 → 20€/jour : même conditions.
4. Jamais plus de +15-20% d'augmentation par palier.
5. Si la performance chute après une augmentation : revenir au palier précédent immédiatement.

**Stratégie pour les pics promotionnels (Black Friday, Noël)**

1. Avoir les campagnes actives depuis au moins 6 semaines avant le pic.
2. Mettre à jour les créatives avec éléments saisonniers (+17% ROAS en moyenne avec contexte saisonnier).
3. Sur la semaine de pic : dupliquer les campagnes gagnantes × 2-3.
4. Ne pas toucher aux budgets des campagnes existantes.
5. Après le pic : ne pas couper. Le CPM post-Q4 (janvier) est le plus bas de l'année — maintenir la pression.

**Scaling avancé : Actalike (Lookalike)**

Une fois 100+ clients dans les audiences :
1. Annonces > Audiences > Créer une audience Actalike.
2. Source : audience "Clients" (événement Checkout).
3. Similarité : top 20%.
4. Lancer en campagne d'acquisition séparée avec le même budget de test (10€/jour).

### Outils nécessaires

- Gestionnaire d'annonces Pinterest (duplication native)
- Dashboard de suivi (Google Sheets ou Notion) pour tracer les ROAS par campagne

### Erreurs à éviter

- Augmenter le budget d'une campagne gagnante au lieu de dupliquer.
- Modifier le ciblage ou les créatives de la campagne originale pendant le scaling.
- Scaler sans attendre les 7-10 jours de la copie.
- Empiler trop vite : valider chaque palier avant de passer au suivant.
- Couper les campagnes après le Q4 — le début d'année a les CPM les plus bas de l'année.
- Monter les budgets de plus de +20% d'un coup.

### Benchmarks attendus

- Copie performante : ROAS ≥ 3 sur 7 jours comme l'originale.
- Cas réel agence : 16 300€ investis → 156 000€ de CA (ROAS 9+) avec CPA 12-16€ sur panier 100€.
- Objectif réaliste : ROAS 7-8 stable sur 6-12 mois avec le bon produit.
- Portefeuille cible : 10-20 campagnes en parallèle pour maximiser la stabilité.

### Checklist de validation

- [ ] ROAS ≥ 3 stable depuis 7 jours consécutifs confirmé avant de scaler
- [ ] Campagne originale non modifiée (budget inchangé)
- [ ] Copie créée à l'identique (même budget, ciblage, créas)
- [ ] Copie lancée à 01h16
- [ ] Évaluation copie planifiée à J+10
- [ ] Dashboard de suivi mis à jour (originale + copie)
- [ ] Si méthode escalier : augmentation ≤ +20% par palier, attente 3-5 jours entre paliers

---

## SOP 6 — Produire des créatives IA en masse

**Objectif :** Générer 100+ créatives de qualité en 15-20 minutes via le workflow Nano Banana / Google Gemini. Maintenir un Brand Style Lock cohérent.

**Durée estimée :** 15-20 minutes pour 100+ créatives

**Prérequis :** Photo produit HD ou 4K (fond blanc idéal). Brief de marque (couleurs, ton, univers). Accès à Gemini Pro + Nano Banana (ou outil de génération IA équivalent). ChatGPT ou Claude pour les textes.

### Étapes

**Phase 1 — Préparer la source d'inspiration**

1. **Créer un board d'inspiration** sur Pinterest avec 20-30 épingles des meilleures créas de la niche (comptes concurrents US, compte "Creative Strategy Ad Pinterest").
2. Identifier les patterns qui reviennent : cadrage, couleurs dominantes, type de mise en scène (lifestyle vs produit seul vs UGC).
3. Sauvegarder les 5 meilleures créas comme référence visuelle.

**Phase 2 — Générer les scénarios avec Gemini**

4. **Uploader la photo produit HD dans Gemini Pro.**
5. **Prompt Gemini :**
   > "Tu es un expert en publicité Pinterest. Analyse ce produit [description rapide]. Génère 40 scénarios UGC (User Generated Content) détaillés pour des publicités Pinterest verticales. Pour chaque scénario : cadrage, décor, personnage, action, émotion, texte accrocheur sur l'image (40-60 caractères). Adapte à une audience féminine 25-35 ans CSP+."
6. **Sélectionner les 10 meilleurs scénarios.** Critères : originalité, potentiel émotionnel, cohérence avec le produit.

**Phase 3 — Générer les visuels avec Nano Banana**

7. **Importer la photo produit et les 10 scénarios sélectionnés dans Nano Banana.**
8. **Configurer le Brand Style Lock :**
   - Couleurs de marque (2-3 couleurs max).
   - Texture et luminosité souhaitées (chaleureuse, froide, lumineuse...).
   - Style de la mise en scène (minimaliste, lifestyle, UGC authentique...).
9. **Paramétrer : 4 créatives générées simultanément par scénario.**
   - 10 scénarios × 4 variantes = 40 créatives de base.
10. **Lancer la génération** (durée : 10-11 minutes environ pour 40 créatives).
11. **Itérer sur les gagnantes :** pour les 5 meilleurs résultats, relancer avec des variations de style → 5 × 3 = 15 créatives supplémentaires.
12. **Télécharger en 4K.** Format vertical uniquement. Rejeter les créas avec déformations ou incohérences visuelles.

**Phase 4 — Générer les titres et descriptions avec ChatGPT/Claude**

13. **Prompt pour les titres :**
   > "Génère 20 titres d'épingles Pinterest pour [produit + niche]. Chaque titre : 40-60 caractères maximum, mots-clés en premier, ton inspirationnel (pas commercial). Public cible : femmes 25-35 ans."
14. **Prompt pour les descriptions :**
   > "Génère 20 descriptions d'épingles Pinterest (200-300 caractères). Intégrer 3-4 mots-clés. Style : informatif et inspirant. Pour le produit [description]. URL de destination : [URL]."
15. **Associer chaque créa à un titre et une description.** Préparer un tableau Google Sheets avec : créa, titre, description, URL, tableau Pinterest cible.

**Phase 5 — Contrôle qualité**

16. Vérifier le format vertical (1 000×1 500px ou ratio 2:3).
17. Vérifier la lisibilité du texte sur l'image (fond contrasté derrière le texte si nécessaire).
18. Vérifier la cohérence brand (couleurs, logo visible).
19. Vérifier qu'aucune déformation produit n'est visible.
20. Sélectionner les 30-40 meilleures créas sur les 100+ générées.

### Outils nécessaires

- Google Gemini Pro — analyse et génération de scénarios
- Nano Banana (ou équivalent IA génération image) — production visuelle
- ChatGPT ou Claude — titres et descriptions
- Canva — retouches et ajout de texte si nécessaire
- Google Sheets — organisation du batch de créas

### Erreurs à éviter

- Générer sans Brand Style Lock — résultat incohérent avec l'identité de marque.
- Utiliser des créas avec texte sur l'image illisible (fond trop chargé).
- Format non vertical — le format horizontal est éliminatoire sur Pinterest.
- Utiliser des créas trop "publicitaires" — sur Pinterest, le natif performe mieux que la bannière commerciale.
- Recycler des vidéos TikTok avec filigrane TikTok — Pinterest pénalise le reach.
- Oublier le scroll-stopper — les 3 premières secondes doivent accrocher (couleurs vives, mouvement, émotion forte).

### Benchmarks attendus

- Workflow complet : 135 créatives en ~11 minutes (benchmark cas pratique).
- CTR cible avec bonne créa : ≥ 1%.
- Règle des 3-4 créatives par groupe d'annonces pour laisser l'algorithme sélectionner.
- Taux de sélection : conserver les meilleures 30-40% de la production.

### Checklist de validation

- [ ] Photo produit HD disponible (fond blanc de préférence)
- [ ] Board d'inspiration créé (20-30 épingles de référence)
- [ ] 10 scénarios Gemini sélectionnés
- [ ] Brand Style Lock configuré dans l'outil IA
- [ ] 40+ créatives générées
- [ ] Format vertical vérifié (1 000×1 500px)
- [ ] Lisibilité texte vérifiée sur chaque créa sélectionnée
- [ ] Titres et descriptions générés et associés
- [ ] 30-40 créatives finales prêtes pour upload Pinterest

---

## SOP 7 — Stratégie organique mensuelle

**Objectif :** Maintenir une présence organique active, identifier ce qui performe, planifier le mois suivant. Fréquence : 1x/mois, durée 1-2 heures.

**Durée estimée :** 1-2 heures/mois

**Prérequis :** Compte Pinterest actif depuis au moins 4 semaines. Accès à Pinterest Analytics. Tailwind configuré.

### Étapes

**Semaine 1 du mois — Analyse (30 min)**

1. **Ouvrir Pinterest Analytics > Vue d'ensemble.**
2. **Identifier les 5 épingles les plus performantes du mois écoulé.**
   - Trier par : impressions, clics, enregistrements (saves).
   - Pour chaque épingle gagnante : noter le tableau, le titre, le visuel, le mot-clé principal.
3. **Identifier les 3 tableaux avec le plus fort reach.**
   - Ce sont les tableaux prioritaires pour publier les prochaines meilleures épingles en premier.
4. **Analyser les mots-clés générateurs de trafic.** Dans Analytics > Métriques de contenu : voir les termes de recherche qui ont conduit des clics.

**Semaine 1 — Veille tendances (20 min)**

5. **Ouvrir Pinterest Trends** (Analytics > Tendances).
6. **Rechercher les 5-10 mots-clés principaux de la niche.** Identifier les pics prévus dans les 3-4 semaines à venir.
7. **Comparer des variantes.** Ex : "robe" vs "jupe", "canapé" vs "sofa" — choisir le terme avec le plus grand volume.
8. **Analyser la démographie** par mot-clé pour affiner les créas (tranches d'âge dominantes).
9. **Consulter Pinterest Predict** si on est en décembre (prévisions tendances N+1).
10. Vérifier le marché US pour anticiper les tendances européennes (décalage 1-2 ans). Créer un compte Pinterest US pour observer le fil.

**Semaine 2 — Production de contenu (1h)**

11. **Appliquer la règle 80/20.**
    - 80% de nouveaux contenus basés sur ce qui a performé le mois dernier (mêmes angles, mêmes thématiques).
    - 20% de tests nouveaux angles ou nouvelles thématiques.
12. **Objectif de production :** 20-30 nouvelles épingles minimum.
13. **Pour chaque article de blog existant :** créer 5-10 variations d'épingles (même visuel, titres différents) pour couvrir plusieurs mots-clés.
14. **Renommer les fichiers images** avant upload : `mot-cle-principal-contexte.jpg`.
15. **Rédiger titres + descriptions** avec mots-clés identifiés à l'étape 4-6.
16. **Mots-clés dans le visuel lui-même** : Pinterest lit le texte sur les images (IA). Intégrer les mots-clés dans les textes de l'image.

**Semaine 2-3 — Planification Tailwind (20 min)**

17. **Uploader le batch de 20-30 épingles dans Tailwind.**
18. **Cliquer "Fill in Time Slots"** pour combler les créneaux vides automatiquement.
19. **Cliquer "Shuffle"** pour mélanger les contenus et créer de la variation journalière.
20. **Vérifier la fréquence :** minimum 5 épingles/jour, horaires variés (ne pas tout concentrer au même créneau).
21. **Planifier 3-4 semaines d'avance** pour ne jamais manquer de contenu.
22. **Paramétrer l'intervalle de republication** : si une épingle est publiée dans plusieurs tableaux, intervalle minimum 30 jours entre chaque republication (pas 7 jours par défaut).

**Semaine 3-4 — Optimisation tableaux (10 min)**

23. **Mettre à jour les tableaux si nécessaire.** Ajouter des mots-clés saisonniers dans les descriptions de tableaux.
24. **Identifier les tableaux "morts"** (moins de 200 impressions/mois) → les alimenter ou les fusionner.
25. **Publier les meilleures épingles du mois en priorité dans les 3 tableaux à fort reach** identifiés à l'étape 3.

### Outils nécessaires

- Pinterest Analytics (natif, gratuit)
- Pinterest Trends (natif, gratuit)
- Tailwind — planificateur (version payante)
- Canva — production épingles
- Keyword Tool (keywordtool.io) — volumes mots-clés

### Erreurs à éviter

- Publier tout le contenu d'un coup au lieu d'étaler sur le mois.
- Ignorer Pinterest Trends et produire du contenu hors-saison.
- Toujours 100% nouveaux contenus — la règle 80/20 dit de capitaliser sur ce qui a marché.
- Republier la même image dans plusieurs tableaux le même jour.
- Négliger la qualité des descriptions (500 caractères disponibles — les utiliser pour le SEO).
- Publier du contenu TikTok avec filigrane — pénalité de reach.

### Benchmarks attendus

- Fréquence : 5 épingles/jour = 150/mois minimum.
- Trafic organique en décoration (niche facile) : 100 visites/jour après 1-1,5 mois.
- Trafic organique en beauté (niche plus longue) : 100 visites/jour après 3-4 mois.
- Épingles evergreen actives : trafic pendant 12-18 mois après publication.
- Une épingle performante enregistrée = effet boule de neige (saves → plus de reach → plus de saves).

### Checklist de validation

- [ ] Pinterest Analytics ouvert, 5 meilleures épingles identifiées
- [ ] 3 tableaux à fort reach identifiés
- [ ] Pinterest Trends consulté, pics prévus notés
- [ ] 20-30 nouvelles épingles produites
- [ ] Fichiers images renommés avec mots-clés
- [ ] Batch uploadé dans Tailwind
- [ ] Fill in Time Slots + Shuffle effectués
- [ ] 3-4 semaines de contenu planifiées
- [ ] Intervalle republication : 30 jours minimum entre tableaux

---

## SOP 8 — Configurer le retargeting

**Objectif :** Recibler les visiteurs chauds et les abandons panier avec les bonnes créatives. Le retargeting Pinterest a des CPM plus élevés mais des taux de conversion bien supérieurs.

**Durée estimée :** 1-2 heures (configuration initiale)

**Prérequis :** Pixel installé et actif depuis au moins 14 jours. Minimum 200-500 visiteurs par mois sur le site. Accès à Annonces > Audiences.

### Étapes

**Phase 1 — Créer les 4 audiences de retargeting**

1. **Annonces > Audiences > Créer une audience.**

2. **Audience 1 — Tous visiteurs 60 jours.**
   - Type : Visiteurs de site.
   - Fenêtre : 60 jours (pas 7-30 jours — le cycle d'achat Pinterest est plus long).
   - Cocher "Inclure le trafic passé".
   - Nom : `[Site] - Visiteurs 60j`.

3. **Audience 2 — Abandons panier 30 jours.**
   - Type : Visiteurs de site.
   - Filtre : événement AddToCart.
   - Fenêtre : 30 jours.
   - Nom : `[Site] - Abandons panier 30j`.

4. **Audience 3 — Engagements Pinterest 30 jours.**
   - Type : Engagement avec le compte.
   - Inclure : interactions avec les épingles (likes, saves, clics).
   - Fenêtre : 30 jours.
   - Nom : `[Site] - Engagement Pinterest 30j`.

5. **Audience 4 — Clients 180 jours.**
   - Type : Visiteurs de site.
   - Filtre : événement Checkout.
   - Fenêtre : 180 jours.
   - À **exclure** des 3 audiences précédentes pour ne pas dépenser du budget sur des clients récents.
   - Nom : `[Site] - Clients 180j`.

**Phase 2 — Créer les campagnes retargeting**

6. **Campagne retargeting classique.**
   - Objectif : Conversion.
   - Groupe d'annonces 1 : cibler Audience 1 (Visiteurs 60j) — exclure Clients 180j.
   - Groupe d'annonces 2 : cibler Audience 2 (Abandons panier 30j) — exclure Clients 180j.
   - Budget : 10-15€/jour par groupe d'annonces.
   - Enchère : **automatique** — toujours en retargeting.
   - Événement d'optimisation : Achat finalisé.

7. **Campagne retargeting dynamique (si catalogue connecté).**
   - Objectif : Vente par catalogues.
   - Type de ciblage : Dynamique.
   - Source de ciblage : visiteurs des 60-180 derniers jours.
   - Catalogue : sélectionner le catalogue connecté.
   - Budget : 15€/jour pour démarrer.
   - Voir SOP 11 pour le détail Shopping.

8. **Campagne engagement Pinterest.**
   - Cibler Audience 3 (Engagements Pinterest 30j).
   - Idéal pour les utilisateurs qui ont sauvegardé des épingles mais n'ont pas encore visité le site.
   - Budget : 5-10€/jour.

**Phase 3 — Créatives retargeting : adapte le message au stade de la relation**

9. **Pour les visiteurs (Audience 1) → créatives inspirationnelles.**
   - Style : rappel doux du produit en contexte lifestyle.
   - Message : inspiration, pas pression.
   - Exemple : la personne a vu un canapé → montrer le canapé dans un salon de rêve.

10. **Pour les abandons panier (Audience 2) → créatives agressives avec trigger.**
    - Afficher clairement le produit + bénéfice principal.
    - Ajouter urgence si possible (stock limité, offre temporaire).
    - En Q4 : afficher le % de réduction, la date limite, le code promo.
    - Message : donner une raison concrète d'acheter maintenant.

11. **Pour les clients (si campagne de fidélisation) → créatives cross-sell.**
    - Présenter des produits complémentaires.
    - Ton chaleureux, pas promotionnel.

**Phase 4 — Surveiller les CPM retargeting**

12. Les CPM retargeting sont plus élevés que l'acquisition (audience plus petite = plus chère).
13. Si CPM monte significativement à budget constant → l'audience est saturée. Maintenir le budget, ne pas augmenter. Élargir la fenêtre temporelle (30j → 60j → 90j) pour grossir l'audience.

### Outils nécessaires

- Gestionnaire d'annonces Pinterest
- Catalogue produits connecté (pour le retargeting dynamique)
- Canva — créatives spécifiques retargeting

### Erreurs à éviter

- Cibler les clients existants avec des pubs d'acquisition — gaspillage de budget.
- Fenêtre de retargeting trop courte (7-30 jours) — audience trop petite sur Pinterest.
- Enchère manuelle en retargeting — peut bloquer la diffusion si l'enchère est trop basse.
- Mêmes créatives qu'en acquisition — le retargeting nécessite un message différent (plus direct).
- Augmenter le budget quand le CPM monte — signe de saturation d'audience, pas d'augmenter.

### Benchmarks attendus

- CPM retargeting : 2-4€ (plus cher que l'acquisition mais conversion plus haute).
- Taux de conversion retargeting : 2-5x celui de l'acquisition.
- Fenêtre optimale : 60-180 jours (cycle d'achat long sur Pinterest).
- Budget retargeting recommandé : 20-30% du budget total pubs.

### Checklist de validation

- [ ] Audience "Visiteurs 60j" créée et active
- [ ] Audience "Abandons panier 30j" créée et active
- [ ] Audience "Engagement Pinterest 30j" créée et active
- [ ] Audience "Clients 180j" créée et configurée en exclusion
- [ ] Campagne retargeting classique créée (2 groupes d'annonces)
- [ ] Enchère automatique sélectionnée
- [ ] Événement d'optimisation : Achat finalisé
- [ ] Créatives spécifiques retargeting uploadées (inspirationnelles pour visiteurs, agressives pour abandons panier)
- [ ] Campagne retargeting dynamique créée (si catalogue disponible)

---

## SOP 9 — Préparer le Q4 (octobre-décembre)

**Objectif :** Maximiser les ventes Q4 sur Pinterest grâce à une préparation anticipée. Les annonceurs permanents ont 5x plus de conversions Q4 que les annonceurs ponctuels.

**Durée estimée :** Préparation étalée sur 3 mois (septembre-novembre)

**Prérequis :** Compte Pinterest Business actif depuis au moins 2-3 mois. Pixel installé et data collectée. Campagnes actives en acquisition.

### Timeline Q4 détaillée

**Septembre — Préparation infrastructure (2-3 semaines)**

1. **Auditer les campagnes actives.** Identifier les 2-3 meilleures campagnes de l'année. Ce sont les bases du Q4.

2. **Créer les créatives saisonnières.** Les recherches Noël démarrent dès septembre sur Pinterest (3-4 semaines avant les autres moteurs). Produire :
   - Créas avec éléments visuels saisonniers (couleurs chaudes, feuilles d'automne pour Halloween/Thanksgiving, puis sapins/flocons pour Noël).
   - Créas "idées cadeaux" : s'adresser aux femmes qui achètent pour leurs proches.
   - Créas avec contexte familial/émotionnel (famille, enfants, partage).
   - Créas Black Friday : avec % de réduction visible.
   - Ajouter du contexte saisonnier = +17% de ROAS en moyenne (données Pinterest).

3. **Créer les tableaux thématiques Q4.**
   - "Idées cadeaux Noël [niche]"
   - "Déco de Noël [niche]"
   - "Black Friday [niche]"
   - "Idées cadeaux pour elle / pour lui"
   - Rédiger les descriptions avec mots-clés saisonniers.

4. **Alimenter les tableaux.** 15-20 épingles saisonnières dans chaque tableau dès septembre.

5. **Vérifier le catalogue produits.** Synchronisation à jour, produits en stock, prix corrects.

**Octobre — Chauffage de l'algorithme**

6. **Lancer les premières campagnes Q4** avec les créatives saisonnières.
   - Objectif : chauffer l'algorithme avant le pic.
   - Budget : 10-15€/jour (pas encore le budget de pointe).
   - Ciblage : centres d'intérêt saisonniers + mots-clés Q4 (ex : "idées cadeaux", "déco Noël").

7. **Les annonceurs qui lancent en décembre ratent le pic** — l'algorithme n'a pas eu le temps de se chauffer. Être actif en octobre = avantage concurrentiel fort.

8. **Dupliquer les campagnes historiquement gagnantes** avec les créatives saisonnières (garder le ciblage d'origine).

9. **Comparer les CPM.** Sur Pinterest Q4 : CPM 2,50-3€ même pendant le Black Friday vs 35-40€ sur Facebook. Adapter le budget en conséquence — on peut se permettre plus de volume sur Pinterest.

**Novembre — Black Friday et Cyber Monday**

10. **Semaine avant le Black Friday :** dupliquer × 2-3 les campagnes gagnantes.

11. **Créatives Black Friday :** afficher % de réduction clairement (ex : -30%), date limite, code promo si applicable. Particulièrement efficace en retargeting (personnes qui connaissent déjà le produit).

12. **Augmenter le budget retargeting** cette semaine uniquement. Les abandons panier et visiteurs récents sont en mode "prêts à acheter".

13. **Ne pas modifier les campagnes d'acquisition existantes.** Seulement les créatives si nécessaire.

**Décembre — Noël**

14. **Début décembre :** passer des créatives Black Friday aux créatives Noël (couleurs, visuels, messages).

15. **Maintenir la pression sur les campagnes.** Ne pas couper les campagnes fin décembre même si les ventes ralentissent.

**Janvier post-Noël**

16. **Ne pas couper après le Q4.** Janvier = CPM les plus bas de l'année. C'est le meilleur moment pour tester de nouveaux produits à moindre coût.

17. **Mettre à jour les créatives** (retirer les éléments de fêtes, passer en mode "nouvelle année", "résolutions", "bilan" selon la niche).

### Outils nécessaires

- Canva — production créatives saisonnières
- Pinterest Trends — validation des volumes saisonniers
- Compte "Creative Strategy Ad Pinterest" sur Pinterest — inspiration créas Q4 (tableaux "gifting" et "Sale zone")
- Gestionnaire d'annonces Pinterest

### Erreurs à éviter

- Attendre début novembre pour préparer — trop tard, l'algorithme n'est pas chaud.
- Ne pas ajouter de contexte saisonnier sur les créatives — perte de +17% ROAS.
- Couper les campagnes après le Q4 — le CPM janvier est le plus bas de l'année.
- Modifier les campagnes d'acquisition existantes pendant le Q4 — les laisser tourner, seulement dupliquer.
- Même créatives que sur Facebook (urgence, interruption) — Pinterest = inspiration, le ton doit rester doux même en promotion.

### Benchmarks attendus

- CPM Pinterest Q4 (France) : 2,50-3€ (vs 35-40€ sur Facebook même période).
- Annonceurs permanents : 5x plus de conversions Q4 que les saisonniers.
- Contexte saisonnier dans les créas : +17% ROAS moyen.
- Timing clé : premières campagnes Q4 actives en octobre = optimal.

### Checklist de validation

**Septembre**
- [ ] Campagnes historiquement gagnantes identifiées
- [ ] Créatives saisonnières (Halloween, Noël, Black Friday) produites
- [ ] Tableaux thématiques Q4 créés et alimentés
- [ ] Catalogue produits à jour

**Octobre**
- [ ] Campagnes Q4 lancées avec créatives saisonnières
- [ ] Mots-clés saisonniers dans les groupes d'annonces
- [ ] Budget chauffage : 10-15€/jour

**Novembre**
- [ ] Campagnes dupliquées × 2-3 la semaine du Black Friday
- [ ] Créatives Black Friday avec % de réduction visible
- [ ] Budget retargeting augmenté cette semaine

**Décembre**
- [ ] Créatives mises à jour Noël (début décembre)
- [ ] Campagnes maintenues sans coupure

**Janvier**
- [ ] Créatives mises à jour post-fêtes
- [ ] Budget maintenu (CPM au plus bas)

---

## SOP 10 — Diagnostiquer une campagne qui ne performe pas

**Objectif :** Identifier précisément la cause de non-performance et appliquer la bonne correction. Ne pas modifier à l'aveugle.

**Durée estimée :** 20-30 minutes

**Prérequis :** Campagne en ligne depuis au moins 7 jours. Données disponibles dans le dashboard.

### Checklist de diagnostic — 10 points dans l'ordre

Parcourir les points dans l'ordre. S'arrêter et corriger dès qu'un problème est identifié.

**Point 1 — Durée de la campagne.**
- Campagne < 10 jours → ne rien faire. La phase d'apprentissage n'est pas terminée.
- Sur un tout nouveau compte : attendre 3 semaines avant de conclure.
- Signal d'urgence uniquement si les dépenses sont élevées et le ROAS = 0 (0 conversions, 0 clics).

**Point 2 — Tracking fonctionnel.**
- Vérifier dans Annonces > Conversions : des conversions sont-elles enregistrées ?
- Si 0 conversions alors que le site vend bien → problème de pixel. Relancer la SOP 2.
- Utiliser Pinterest Tag Helper pour vérifier les événements en temps réel.

**Point 3 — Objectif de campagne.**
- L'objectif est-il "Conversion" et non "Trafic" ou "Notoriété" ?
- Si non : ne pas modifier la campagne en cours. Créer une nouvelle campagne avec le bon objectif.

**Point 4 — Ciblage.**
- Y a-t-il un mélange centres d'intérêt + mots-clés dans le même groupe ?
- La taille d'audience est-elle > 1 million de personnes ?
- Si le ciblage est trop étroit : créer un nouveau groupe avec un ciblage élargi. Ne pas modifier le groupe existant.

**Point 5 — Créatives.**
- CTR < 0,4% après la phase d'apprentissage → problème créatif.
- Vérifier : format vertical ? Scroll-stopper dans les 3 premières secondes ? Texte lisible ? Couleurs vives ?
- Action : ne pas modifier la campagne. Créer un nouveau groupe d'annonces avec de nouvelles créatives.

**Point 6 — Page de redirection.**
- CTR correct (> 0,5%) + ROAS faible → problème landing page, pas de créa.
- Vérifier : cohérence entre épingle et page (même produit, même visuel) ? Temps de chargement < 3s ? Page mobile-friendly ?
- Action : tester une autre page de destination dans un nouveau groupe d'annonces.

**Point 7 — Budget.**
- Le budget a-t-il été modifié depuis le lancement ?
- Une modification de budget en cours de route peut relancer la phase d'apprentissage.
- Si oui : créer une nouvelle campagne avec le budget correct depuis le départ.

**Point 8 — Modifications récentes.**
- Des modifications ont-elles été apportées à la campagne dans les 7 derniers jours ?
- Chaque modification (ciblage, créa, budget) peut remettre l'algorithme en phase d'apprentissage.
- Si oui : attendre 7 jours supplémentaires avant de conclure.

**Point 9 — Concurrence temporelle.**
- La campagne tourne-t-elle pendant une période de haute concurrence (Q4, rentrée, soldes) sans budget adapté ?
- Si oui : le CPM peut être anormalement élevé. Vérifier le CPM vs benchmark (1-1,50€ hors Q4 ; 2,50-3€ Q4).

**Point 10 — Produit/niche.**
- Si tous les points précédents sont OK et que la campagne ne performe pas après 14 jours :
  - Le produit n'est peut-être pas adapté à Pinterest (produit masculin sans angle féminin, niche B2B).
  - Tester un autre produit du catalogue.
  - Vérifier la cohérence audience Pinterest (femmes 25-35 ans CSP+) avec le produit.

### Signaux d'alerte immédiats

| Signal | Seuil | Action |
|--------|-------|--------|
| CPA > 2x panier moyen après 10j | Critique | Changer créatives ou landing page |
| CTR < 0,4% après phase apprentissage | Critique | Nouvelles créatives |
| ROAS < 1 après 14j | Critique | Analyser les 10 points, puis tester autre produit |
| ROAS < 2 après 14j | Alerte | Tester autres landing pages |
| 0 conversion après 7j avec budget dépensé | Critique | Vérifier tracking (SOP 2) |
| CPM > 5€ hors Q4 | Alerte | Élargir le ciblage |

### Actions correctives par problème

- **Problème tracking** → Relancer SOP 2. Ne rien changer aux campagnes pendant la correction.
- **Problème créatif** → Créer un nouveau groupe d'annonces avec de nouvelles créas (ne pas modifier l'ancien).
- **Problème landing page** → Dupliquer le groupe d'annonces, changer uniquement l'URL de destination.
- **Problème ciblage** → Dupliquer le groupe d'annonces, modifier le ciblage dans la copie.
- **Problème produit** → Créer une nouvelle campagne avec un autre produit.

### Outils nécessaires

- Dashboard Annonces > Informations
- Pinterest Tag Helper (extension Chrome)
- Google Analytics / analytics e-commerce (pour taux de conversion landing page)

### Erreurs à éviter

- Modifier la campagne originale pour corriger un problème — toujours créer une nouvelle copie.
- Couper une campagne < 10 jours sans analyser les 10 points.
- Couper quand le tracking est défaillant — on coupe à l'aveugle.
- Chercher le problème dans un seul facteur — utiliser la checklist dans l'ordre.
- Paniquer pendant les 3-6 premiers jours (perte de performance de 40-80% = normal).

### Checklist de validation

- [ ] Point 1 : campagne > 10 jours (ou 3 semaines pour nouveau compte)
- [ ] Point 2 : tracking vérifié (Tag Helper + historique événements)
- [ ] Point 3 : objectif Conversion confirmé
- [ ] Point 4 : ciblage vérifié (pas de mélange, > 1M personnes)
- [ ] Point 5 : créatives vérifiées (CTR > 0,4%, format vertical)
- [ ] Point 6 : landing page vérifiée (cohérence, temps de chargement)
- [ ] Point 7 : budget non modifié depuis lancement
- [ ] Point 8 : aucune modification récente (7 derniers jours)
- [ ] Point 9 : CPM vérifié vs benchmark
- [ ] Point 10 : si tout OK — tester autre produit

---

## SOP 11 — Configurer les campagnes Shopping

**Objectif :** Connecter le catalogue produits, lancer les campagnes Shopping et le retargeting dynamique pour maximiser la conversion sur les produits déjà vus.

**Durée estimée :** 1-2 heures (configuration initiale)

**Prérequis :** Minimum 20-30 produits actifs sur la boutique. Compte Pinterest Business vérifié ("commercant vérifié"). Pixel installé.

### Étapes

**Phase 1 — Devenir commerçant vérifié**

1. Paramètres du compte > Revendiquer vos contenus > vérifier le site web.
2. Un site vérifié est nécessaire pour le badge "commerçant vérifié" et pour activer le Shopping.
3. Le badge améliore la confiance et la visibilité des épingles shopping.

**Phase 2 — Connecter le catalogue**

**Option 1 — Via l'app officielle Shopify Pinterest :**
1. Apps Shopify > Pinterest for Shopify > Connect.
2. L'app synchronise automatiquement le catalogue (produits, prix, stocks).
3. Les produits épuisés sont automatiquement marqués "Out of stock" ou retirés.
4. Vérifier la synchronisation : Annonces > Catalogues.

**Option 2 — Via flux CSV/XML (WooCommerce, PrestaShop, autres) :**
1. Utiliser un outil de flux produits : **Channable**, **Multifeed** ou **SimProis** (Simprosys Feed for Google Shopping).
2. Configurer le flux au format Google Shopping (colonnes : id, title, description, link, image_link, price, availability, condition, brand, google_product_category).
3. Dans Pinterest : Annonces > Catalogues > Ajouter un catalogue > URL du flux.
4. Pinterest ingère le flux automatiquement (fréquence de mise à jour recommandée : quotidienne).
5. Vérifier les erreurs dans Annonces > Catalogues > Rapport de diagnostic.

**Option 3 — Via API Pinterest Commerce (pour développeurs) :**
- Solution pour les boutiques sur mesure ou les plateformes non compatibles.
- Documentation API : developers.pinterest.com.

**Phase 3 — Corriger les erreurs de catalogue**

6. Vérifier le rapport de diagnostic (Annonces > Catalogues > Rapport).
7. Erreurs communes : images manquantes, prix incorrects, catégories non renseignées, titres trop courts.
8. Corriger les erreurs dans la source (Shopify, WooCommerce) — le catalogue se met à jour automatiquement.

**Phase 4 — Activer Shop the Look**

9. Activer "Shop the Look" dans les paramètres catalogue.
10. Pinterest IA détecte automatiquement les produits visibles sur les images lifestyle et propose des liens d'achat directs.
11. Pubier des images lifestyle avec plusieurs produits visibles pour maximiser la détection.

**Phase 5 — Lancer la campagne Shopping**

12. Annonces > Créer une annonce > Campagne > Objectif : **Vente par catalogues**.
13. Sélectionner le catalogue connecté.
14. Groupe d'annonces :
    - **Retargeting dynamique :** Type de ciblage "Dynamique" → visiteurs des 60-180 derniers jours.
    - **Acquisition dynamique :** Type de ciblage "Centre d'intérêt" ou "Mots-clés" → le catalogue s'affiche automatiquement en sélectionnant les produits les plus pertinents.
15. Événement d'optimisation : **Paiement final** (pas "Ajout au panier").
16. Enchère : automatique.
17. Budget : 15€/jour pour le retargeting dynamique.

**Phase 6 — Structurer les groupes de produits**

18. Créer des groupes de produits par catégorie (pas tout le catalogue dans un seul groupe) :
    - Ex : "Robes", "Accessoires", "Chaussures" si mode.
19. Minimum 20 produits par groupe pour que le retargeting dynamique fonctionne correctement.
20. Exclure les produits épuisés des groupes actifs.

### Outils nécessaires

- App Pinterest for Shopify (si Shopify)
- Channable / Multifeed / SimProis (si flux CSV/XML)
- Gestionnaire d'annonces Pinterest

### Erreurs à éviter

- Lancer les campagnes Shopping sans avoir résolu les erreurs de catalogue (rapport diagnostic).
- Avoir moins de 20 produits par groupe de retargeting dynamique — insuffisant pour l'algorithme.
- Ne pas synchroniser régulièrement le catalogue (produits épuisés toujours en publicité = mauvaise expérience).
- Optimiser sur "Ajout au panier" plutôt que "Paiement final" — force Pinterest à trouver des acheteurs réels.
- Oublier d'activer Shop the Look — opportunité de revenus additionnels gratuite.

### Benchmarks attendus

- Ingestion catalogue : 24-48h pour la première synchronisation.
- Retargeting dynamique : CTR généralement plus élevé que l'acquisition (la personne a déjà vu le produit).
- Groupes de produits : minimum 20 produits pour le retargeting dynamique.
- Catalogue avec 30-50+ produits = condition recommandée pour lancer les campagnes Shopping.

### Checklist de validation

- [ ] Site web revendiqué + badge commerçant vérifié
- [ ] Catalogue connecté (Shopify app ou flux CSV)
- [ ] Rapport diagnostic sans erreur bloquante
- [ ] Synchronisation automatique configurée (quotidienne)
- [ ] Shop the Look activé
- [ ] Groupes de produits créés par catégorie (≥ 20 produits chacun)
- [ ] Campagne "Vente par catalogues" créée
- [ ] Ciblage dynamique sur 60-180 jours
- [ ] Événement d'optimisation : Paiement final
- [ ] Enchère automatique

---

## SOP 12 — Espionner la concurrence Pinterest

**Objectif :** Identifier les produits gagnants, les créatives qui performent et les stratégies de redirection des concurrents. Transférer les insights cross-marchés.

**Durée estimée :** 1-2 heures (analyse initiale), 30 min/quinzaine (veille récurrente)

**Prérequis :** Compte Minea actif (version payante). VPN installé (pour l'accès au marché US). Comptes Pinterest créés sur différents marchés (US, DE).

### Étapes

**Phase 1 — Espionnage via Minea**

1. **Se connecter à Minea.**
2. **Filtrer les annonces Pinterest :**
   - Plateforme : Pinterest.
   - Pays : France (pour analyse marché FR).
   - E-commerce : Shopify ou WooCommerce.
   - Tri : nombre de "Pins" (enregistrements) — plus de pins = plus viral = plus performant.
3. **Analyser les 10-20 meilleures annonces.**
   - Format utilisé (image statique vs vidéo).
   - Couleurs et composition.
   - Accroche (titre + texte sur image).
   - Type de mise en scène (lifestyle, produit seul, UGC).
4. **Cliquer sur "Voir la boutique"** pour identifier le concurrent et sa page de destination.
5. **Analyser la landing page.** Structure AIDA ? Page produit directe ? Article éducatif ? Advertorial ?

**Phase 2 — Espionnage avec VPN (marché US)**

6. **Activer le VPN sur le serveur US.**
7. **Se connecter à Pinterest** avec un compte US (ou créer un compte sans adresse FR).
8. **Le fil d'actualité et les suggestions de Pinterest passent en mode US** → voir les créas et produits qui cartonnent aux US.
9. **Observer pendant 1h30 à 2h** — scroller le fil en cherchant des patterns : produits récurrents, formats d'épingles, angles créatifs.
10. **Répéter toutes les 2 semaines.** Ce qui marche aux US arrive en France 1-2 ans plus tard.

**Phase 3 — Utiliser Pin Spy**

11. **Pin Spy** (pinspy.com) — outil spécialisé espionnage Pinterest Ads.
12. Rechercher par mot-clé ou catégorie pour voir les publicités actives.
13. Filtrer par pays, engagement, durée de diffusion.
14. Les publicités diffusées depuis longtemps (> 30 jours) = profitables. Un annonceur ne dépense pas sur une créa non rentable.

**Phase 4 — Analyser les pages de redirection**

15. Pour chaque annonce identifiée comme performante : noter l'URL de destination.
16. **Analyser la structure de la landing page :**
    - Présence d'une histoire / storytelling en haut de page.
    - Structure AIDA visible (Attention, Intérêt, Désir, Action).
    - Nombre d'avis clients affichés.
    - Présence d'un comparatif ou d'un tableau de caractéristiques.
    - CTA principal (acheter vs email vs blog).
17. **Tester la page sur mobile** (simulateur Chrome DevTools ou smartphone).
18. **Identifier le CMS** (Shopify, WooCommerce, Prestashop) via Wappalyzer (extension Chrome).

**Phase 5 — Transfert cross-marché**

19. **Produits gagnants US → tester en France.**
    - Un produit validé sur le marché US = forte probabilité de marcher en France 6-18 mois plus tard.
    - Vérifier la compatibilité culturelle (certains produits US ne fonctionnent pas en Europe).
    - Tester en Allemagne (marché EU n°1 pour Pinterest, paniers moyens élevés) avant la France si incertain.

20. **Produits gagnants France → tester dans les marchés nordiques ou BENELUX.**
    - Progression recommandée : France → Allemagne → Nordiques → UK → US.
    - Même produit, même créa (adapter juste la langue) = valider rapidement chaque marché.

21. **Identifier les produits qui marchent sur Facebook → les transférer sur Pinterest.**
    - Le même produit avec un angle inspirationnel plutôt que commercial fonctionne souvent mieux sur Pinterest.
    - 55x moins d'annonceurs sur Pinterest que sur Facebook = CPM bien plus bas pour un produit déjà validé.

### Outils nécessaires

- Minea (payant) — espionnage ads Pinterest + Facebook
- Pin Spy (pinspy.com) — espionnage spécialisé Pinterest
- VPN (NordVPN, ExpressVPN) — accès marché US
- Wappalyzer (extension Chrome, gratuit) — identifier le CMS des concurrents
- Compte Pinterest US créé pour veille marché

### Erreurs à éviter

- Copier les créas à l'identique — risque de ban + perte de différenciation.
- Ne regarder que le marché FR — les tendances viennent des US.
- Analyser des publicités récentes (< 7 jours) — trop tôt pour savoir si elles sont rentables.
- Ignorer la landing page — c'est souvent là que se joue la différence de performance.
- Analyser sans passer à l'action — la veille n'a de valeur que si elle alimente la production de créas.

### Benchmarks attendus

- Fréquence de veille recommandée : 1,5-2h toutes les 2 semaines.
- Décalage US → France : 1-2 ans (les produits qui marchent aux US maintenant marcheront en France).
- Indicateur de publicité rentable : diffusée depuis > 30 jours sans interruption.

### Checklist de validation

- [ ] Minea configuré avec filtres Pinterest + France + tri par Pins
- [ ] 10-20 meilleures annonces analysées (format, accroche, mise en scène)
- [ ] Landing pages des concurrents vérifiées (structure, mobile)
- [ ] VPN activé, veille marché US effectuée (1,5-2h)
- [ ] Pin Spy : publicités actives depuis > 30 jours identifiées
- [ ] 5-10 produits/créas à tester identifiés
- [ ] Plan de test documenté (produit, marché cible, angle créatif, landing page)
- [ ] Prochaine session de veille planifiée (dans 2 semaines)

---

## Index des SOP

| N° | Titre | Durée | Priorité |
|----|-------|-------|----------|
| SOP 1 | Lancer un compte de zéro | 2-3h | Fondamentale |
| SOP 2 | Installer le tracking | 30-60 min | Fondamentale |
| SOP 3 | Lancer la première campagne Ads | 45-60 min | Fondamentale |
| SOP 4 | Analyser les résultats après 7-10 jours | 15-20 min | Récurrente |
| SOP 5 | Scaler une campagne gagnante | 15 min/duplication | Croissance |
| SOP 6 | Produire des créatives IA en masse | 15-20 min pour 100+ | Production |
| SOP 7 | Stratégie organique mensuelle | 1-2h/mois | Récurrente |
| SOP 8 | Configurer le retargeting | 1-2h | Conversion |
| SOP 9 | Préparer le Q4 | Étalée sur 3 mois | Saisonnière |
| SOP 10 | Diagnostiquer une campagne qui ne performe pas | 20-30 min | Debug |
| SOP 11 | Configurer les campagnes Shopping | 1-2h | E-commerce |
| SOP 12 | Espionner la concurrence | 1-2h initiale, 30 min/quinzaine | Veille |

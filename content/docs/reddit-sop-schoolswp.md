# SOP Reddit schoolsWP

Procédure opérationnelle pour utiliser Reddit comme levier SEO + GEO (citation IA) sans se faire rejeter par les communautés.

- **Source méthode** : playbook de César (agence Skilfut, 100 % Reddit), podcast MVP SEO/GEO, + site skilfut.online. Voir `data/output/reddit-seo-geo-playbook-cesar-skilfut.pdf`.
- **Source méthode avancée** : 2e passage de César sur MVP, "Top 1 PARTOUT grâce à REDDIT (méthode complète)" (YouTube `GHQRQ-xQMA8`, 17 juin 2026). Plusieurs techniques de cette vidéo sont volontairement écartées (voir la section "Ce que schoolsWP NE reprend PAS").
- **Garde-fous** : agent `.claude/agents/reddit.md` + `content/docs/BRAND_RULES.md`.
- **Date** : 2026-06-18.
- **Voix** : "je" singulier (Michael est solo derrière schoolsWP), tutoiement FR, jamais "nous/notre", toujours `schoolsWP`, pas d'em-dash.

---

## TL;DR

1. Reddit est la source #1 des Google AI Overviews (~21 %) et pèse ~12 % des citations ChatGPT. C'est un des rares leviers GEO sur lequel tu peux agir sans budget RP.
2. Deux jeux distincts : le **post** (croissance interne) et le **commentaire** sur question à fort intent (positionnement Google + LLM). Le commentaire est le vrai levier de citation IA.
3. Tout repose sur la **patience** : warmup du compte, valeur avant citation, ratio promo 1/10. Une promo directe ne te bannit pas, elle te rend invisible.

---

## Cadrage : le double enjeu

| Visibilité interne (dans Reddit)                                                              | Visibilité externe (parasite SEO + GEO)                                    |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Faire performer un **post** dans un sub. Objectif : trafic direct, waitlist, téléchargements. | Se positionner sur des prompts Google et LLM ("meilleur LMS WordPress ?"). |
| Format : post "vécu", légèrement réflexif, marque citée en passant.                           | Format : **commentaire** qui recommande comme un utilisateur satisfait.    |

Pour le ROI le plus rapide : vise l'interne (post). Pour la citation IA : vise les commentaires sur questions commerciales. Ne mélange jamais les deux dans un même livrable.

---

## Phase 0 : warmup du compte (avant toute production)

Pour un compte neuf, ne rien produire avant cette séquence. Reddit banne automatiquement les comptes de moins de 2 heures qui postent.

| Jour     | Action autorisée                                                                  |
| -------- | --------------------------------------------------------------------------------- |
| J1 (24h) | Création + 2FA + browse passif (1h30 max). Aucun vote, commentaire ou post.       |
| J2       | Rejoindre 1 à 2 communautés, scroll uniquement.                                   |
| J3       | +1 communauté, premier upvote autorisé.                                           |
| J4-J7    | Premier commentaire de valeur, plus de votes.                                     |
| J10-J15+ | Premier post seulement maintenant, après avoir accumulé du karma en commentaires. |

> Compter 2 à 6 semaines d'usage "humain" avant de citer la marque pour la première fois.

---

## Phase 1 : veille mots-clés (arriver en premier en commentaire)

1. **Compte entreprise Reddit** (gratuit) : suivi d'une liste de mots-clés, alerte à chaque citation. Pas de limite stricte sur le nombre de mots-clés.
2. **F5bot.com** (gratuit, 5 mots-clés) : mail dès qu'un mot-clé apparaît sur Reddit.

Premier arrivé = premier commentaire = premier ranké.

### 5 mots-clés F5bot (calés sur les clusters actifs)

| Mot-clé                     | Cluster               | Pourquoi                                                               |
| --------------------------- | --------------------- | ---------------------------------------------------------------------- |
| `FluentCRM`                 | CRM                   | Comparatifs actifs (vs SureContact, vs Groundhogg), vrai volume Reddit |
| `FluentCart`                | E-commerce            | Veille SOP-03 active, plugin jeune, peu de contenu FR                  |
| `Tutor LMS`                 | LMS                   | Pilier récurrent, intent "best WordPress LMS"                          |
| `WordPress security plugin` | Sécurité              | Cluster sécurité très actif (plugin sécurité, 2FA, hébergeur sécurisé) |
| `SureCart`                  | E-commerce / paiement | Écosystème SureCart/Paystack, intent panier WordPress                  |

### Liste élargie (compte entreprise Reddit, sans limite de 5)

`schoolsWP`, `SureContact`, `LearnDash`, `WordPress LMS`, `best WordPress CRM`, `membership plugin WordPress`, `FluentCommunity`, `Rank Math`, `Paystack WooCommerce`.

> Rotation : recale les 5 slots F5bot sur le comparatif que tu pousses dans le mois.

---

## Phase 2 : cartographie large des subreddits

Ratisser large (secteur + métier + e-commerce + marques), pas seulement le cœur WordPress. Tailles à vérifier (ne jamais inventer un nombre de membres).

### Subreddits à rejoindre cette semaine (ordre warmup)

| Étape | Subreddit          | Langue | Angle d'entrée                              | Risque                                    |
| ----- | ------------------ | ------ | ------------------------------------------- | ----------------------------------------- |
| J2    | r/Wordpress        | EN     | Retour d'expérience chiffré, comparatif     | Modération anti-promo forte               |
| J2    | r/ProWordPress     | EN     | Architecture, choix de stack, debugging     | Public technique, zéro tolérance bullshit |
| J3    | r/SEO              | EN     | Test concret, debunk, cas d'étude           | Sceptique, exige de la data               |
| J4-J7 | r/eLearning        | EN     | Comparatif LMS, monétisation cours          | Liens souvent filtrés                     |
| J4-J7 | r/juststart        | EN     | Build-in-public, business en ligne          | Auto-promo surveillée                     |
| J4-J7 | r/woocommerce      | EN     | E-commerce WordPress (FluentCart, Paystack) | Questions support, pas pub                |
| +tard | r/AutoEntrepreneur | FR     | Aide concrète, coût chiffré, freelance réel | Anti-blabla                               |
| +tard | r/Entrepreneur     | EN     | Récit d'expérience, leçon apprise           | Très large, dur de percer                 |

Avant de poster dans un sub : observer modérateurs (virulents ou non), liens autorisés ou non, ton (sérieux/déconne), hook qui marche, délai moyen avant qu'un post performe.

> Priorisation sectorielle : les niches SEO/GEO sont déjà saturées et averties (manipulation forte, plus dur de percer). Le B2C grand public reste quasi vierge ("pratiquement aucune manipulation"). schoolsWP (WordPress/LMS, public semi-averti) : viser l'utilité réelle, pas le volume.

---

## Phase 2bis : ciblage GEO par les prompts ChatGPT

Le ciblage des posts ne se devine pas : il part de ce que l'IA cite déjà.

1. Liste 10 questions que ta cible taperait pour te trouver (ex : "meilleur LMS WordPress ?", "FluentCRM ou alternative ?").
2. Pose-les une par une dans ChatGPT déconnecté (compte neutre, pour éviter la personnalisation).
3. Ouvre les sources de chaque réponse : repère les posts Reddit déjà cités (compte 4-5 posts sur 10 prompts).
4. Sur un post cité où schoolsWP n'apparaît pas : c'est une cible. Tu y apportes un commentaire de valeur (voir Phase 3B).
5. Query fan-out : chaque prompt déclenche des sous-questions que l'IA explore. Récupère-les (outil type Otterly, gratuit par mail) et repasse-les dans ChatGPT pour trouver des sources Reddit secondaires à couvrir aussi.

Étale les interventions (tous les 3 jours, sur 1 à 2 semaines). C'est un travail de fond : ~1 à 2 mois pour semer dans toutes les sources.

---

## Phase 3 : production

### A. Post "vécu" (visibilité interne)

- **Titre** : expérience + résultat chiffré. Ex : "Comment j'ai automatisé mes relances clients et récupéré X heures/semaine" (`X` = placeholder à confirmer, jamais inventé).
- **Corps** : process détaillé du point de vue utilisateur, marque glissée de façon anodine (méthode Opal). Limite honnête (pour qui ce n'est pas adapté).
- Le lien va dans le **premier commentaire signé** (disclosure), jamais dans le post.

### B. Commentaire (visibilité externe SEO/GEO) - le levier citation IA

- **Questions à fort intent commercial** ("meilleur plugin/LMS/CRM pour X ?") : recommandation ton "j'ai testé, je recommande", après avoir répondu à fond à la question.
- **Questions floues** : triple recommandation (une chaîne YouTube + une communauté Reddit + un blog/ressource). Paraît honnête et glisse la ressource sans la mettre seule en avant.
- 150-300 mots max. Le commentaire utile est court et dense.
- **Jamais de promo dès la 1re phrase** ("le meilleur outil que j'utilise, c'est X" = trop flag). Réponds d'abord avec nuance, recommande seulement à partir de la 2e phrase. Script type : "Il n'y a pas de solution miracle, ça dépend de ton budget et de tes attentes. Perso j'utilise X et j'en suis content, va checker."
- **Fenêtre des 4-5 h** : sur un post récent, commente dans les 4-5 premières heures pour un meilleur ranking, avant l'afflux des autres réponses.

### Règle d'or (= ratio 1/10)

Ne cite ta marque que si tu la recommanderais à un ami dans cette conversation. Si tu forces le passage, tu es grillé. Au-delà de 1 mention promo pour 10 contributions de valeur : tu refuses le brief. (César cite un minimum de 1 promo pour 5-6 commentaires de valeur ; schoolsWP reste plus strict, 1/10.)

---

## Phase 4 : tracking (à la main, jamais via API)

- Tape tes prompts comme un vrai utilisateur sur Google, ChatGPT, Perplexity et la recherche interne Reddit. Les outils via API donnent des résultats différents d'un vrai user.
- Suivi mensuel : impressions, commentaires, positions observées.
- Ne jamais promettre de position ni de viralité. Le "top 5 Google en 5-6 jours" est un résultat observé par César, pas une garantie schoolsWP.

---

## Pièges fatals

1. **Commentaire promo dès le départ** : pas un ban, l'invisibilité (l'algo tire le compte vers le bas).
2. **Multi-comptes sur la même IP** (post compte A, upvote compte B) : Reddit lie via l'IP, les deux comptes sautent. schoolsWP = un seul compte, voix "je", pas de proxies. César lui-même le déconseille à un solo : le ROI organique pur reste meilleur.

---

## Ce que schoolsWP NE reprend PAS de la méthode César (et pourquoi)

La "méthode complète" (2e vidéo) pousse des tactiques incompatibles avec l'éthique et l'identité schoolsWP. On les écarte volontairement :

- **Boucles d'auto-référencement multi-comptes** : créer soi-même la question avec un compte puis y répondre avec d'autres comptes pour se recommander. C'est de l'astroturfing. schoolsWP joue une seule identité transparente "je". Risque de ban + réputation.
- **Se faire passer pour un utilisateur neutre** en cachant qu'on est derrière schoolsWP : contraire à la règle de disclosure (lien + transparence dans le 1er commentaire signé).
- **Masquer ses commentaires** dans les réglages du compte pour dissimuler le pattern promo : opsec de dissimulation, incompatible avec la transparence.
- **Farming de karma** sur des communautés hors-sujet (animaux, jeux vidéo, 20-30 karma/jour) : participation inauthentique. On préfère du karma gagné sur des contributions réelles dans nos communautés.

Ce qu'on garde de la vidéo : ciblage GEO par les prompts ChatGPT + query fan-out, fenêtre des 4-5 h, commentaire nuancé (promo en 2e phrase), priorisation sectorielle, tracking manuel.

---

## Stats vérifiées (citations sûres à réutiliser)

| Donnée                                                          | Statut                    |
| --------------------------------------------------------------- | ------------------------- |
| Reddit = 1,36 Md d'utilisateurs mensuels (2026)                 | Vérifié (officiel Reddit) |
| Accord Google-Reddit : 60 M$/an pour entraîner l'IA (fév. 2024) | Vérifié (CBS News)        |
| Reddit = ~21 % des sources des Google AI Overviews              | Vérifié (études 2025)     |
| Reddit = ~12 % des citations ChatGPT (US)                       | Vérifié (étude 5W)        |

À éviter sans nuance : "+1 300 % de visibilité SEO" (source non citée), "2 Md de visiteurs" (gonflé), "Reddit source #1 des LLM" (vrai pour Google AIO, faux pour ChatGPT où Wikipédia domine).

---

## À intégrer dans l'agent `.claude/agents/reddit.md`

Les 8 briques ci-dessous manquent à l'agent actuel (édition bloquée par l'auto-mode, à appliquer manuellement ou après autorisation) :

1. Section "Cadrage stratégique : le double enjeu" (post interne vs commentaire externe).
2. Section "Warmup de compte" (séquence J1-J15).
3. Section "Veille mots-clés" (compte entreprise + F5bot).
4. Cartographie large des subs (au-delà des 5 subs par défaut).
5. Commentaire : ciblage des questions à fort intent commercial.
6. Commentaire : technique de triple recommandation.
7. Section "Tracking" (manuel, jamais via API).
8. Deux erreurs fatales (promo directe = invisibilité ; multi-comptes même IP).

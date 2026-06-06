# Plan de reprise - Masterclass WP Social Ninja

> Fichier d'état pour reprendre après redémarrage de Claude Code (chargement du MCP `fluent-boards`).
> Créé le 2026-05-28.

## Objectif

Produire la masterclass WP Social Ninja (7 modules, 39 leçons) puis, au Module 7, construire la page « Vidéos » de schoolswp.com avec le YouTube Feed du plugin.

## Décisions verrouillées

- Chaîne YouTube : @michaelkihl (perso).
- Site cible : sous-section de schoolswp.com (WordPress/Kadence), pas un site séparé.
- Suivi : board FluentBoards (Kanban).
- Ampleur : masterclass complète, 7 modules.
- Faisabilité page « Vidéos » : OUI. YouTube Feed type « Specific Videos » (curation par ID) + 1 template/shortcode par thème sur une même page. Layout Grid gratuit. Prérequis : clé API YouTube Data v3.

## Déjà fait

- Sources : `content/formations/wpsocialninja/sources/playlist-officielle.md` (85 vidéos) + `sources/docs/` (92 pages doc).
- Curriculum : `content/formations/wpsocialninja/wpsocialninja-plan-formation.md`.
- Leçon-test validée (gabarit de référence) : `content/formations/wpsocialninja/wpsocialninja-masterclass-m2-l2.md`.
- Maquette page Vidéos (HTML) : `content/inspirations/youtube-hub-mockup.html`.

## Statut (2026-05-28)

- **39/39 leçons écrites** par les 7 sous-agents et vérifiées : 1052-1638 mots chacune (~52 000 mots), gabarit 2.2 respecté, branding 0 violation (em-dash/en-dash/mots interdits), aucun stub.
- À valider en review humaine : M5 (5.2) « streams/badge » reconstruits depuis le titre vidéo #29 (pas de doc écrite) ; M7 (7.5) WP Social Ninja ne génère pas de schema VideoObject pour les feeds vidéo (la leçon le dit et renvoie à un plugin SEO vidéo).
- **Board FluentBoards : toujours en attente** (droits MCP à corriger côté user).

## Production vidéo (2026-05-29) - EN COURS

Stack débloquée : ElevenLabs (tier creator, clone vocal Michaël id r8Nv8JDxL3hOIt4MZtwT, accessible) + HeyGen (plan payé, 600 crédits plan).

État :
- Voix : OK. Échantillon intro leçon 2.2 généré dans content/formations/wpsocialninja/production/2-2-intro.mp3 (script smoke_narrate_2-2-intro.py, voix clone, eleven_multilingual_v2).
- HeyGen API REST (clé X-Api-Key dans .env) : NON utilisable pour la prod. remaining_quota (crédits API) = 0, erreur MOVIO_PAYMENT_INSUFFICIENT_CREDIT. Les 600 crédits du plan ne sont dépensables QUE via le MCP (OAuth) ou le dashboard web, pas via l'API REST. Le script heygen_avatar.py reste valable si Michaël achète des crédits API un jour (utile pour batcher).
- Décision (2026-05-29) : produire via le MCP HeyGen. L'auth OAuth in-session (outils authenticate/complete) échoue, flux non persistant. Chemin fiable = redémarrer Claude Code, le MCP se ré-authentifie au connect (validé en mai 2026).

PROCHAINE ÉTAPE après restart (smoke test 2.2) :
1. Vérifier que les outils MCP heygen sont présents (chercher mcp heygen create video from avatar). Sinon, relancer l'auth au connect.
2. Résoudre le look digital twin depuis le group eb4b43583683415b9d613e2004c86810 (list avatar looks). Look connu : bcc2e2951dff40ef8b1c860f691f02fa.
3. Fournir l'audio en URL HTTPS publique. Asset déjà uploadé lors du test API : https://resource2.heygen.ai/audio/70750f01102b4e67af81ece2b38c96e6/original.mp3 (à tester ; sinon ré-uploader le mp3 sur Drive public ou via Novamira media).
4. Appeler create video from avatar : avatarId = digital twin, audioUrl = l'audio, aspectRatio 16:9, resolution 720p, SANS voiceId, SANS script. Puis get video pour le MP4.
5. Télécharger vers content/formations/wpsocialninja/production/2-2-intro.mp4. Michaël valide voix + lipsync + visage. Ensuite : décider la forme d'une leçon complète (segments avatar + slides/captures) et la stratégie de batch des 39 leçons.

## Reste à faire

### Production des leçons : TERMINÉE (2026-05-28)

- 39 sur 39 leçons écrites (7 sous-agents + la 2.2). Branding re-vérifié par grep complet : 0 violation (em-dash, en-dash, mots interdits, casse). Qualité échantillonnée sur M1, M2, M4, M5, M7 : conforme au gabarit, sourcée doc et vidéos.
- 2 points pour ta review humaine : M5 lecon 5.2 (streams et badge reconstruits depuis le titre de la vidéo numéro 29, pas de doc écrite) ; M7 lecon 7.5 (WP Social Ninja ne produit pas de schema VideoObject pour les feeds : la leçon le dit et renvoie vers un plugin SEO vidéo).

### Seul point ouvert : le board FluentBoards

- Le serveur MCP admin n'expose pas ses outils après 3 redémarrages ; l'ancien serveur renvoie 403. Bug d'environnement à régler côté MCP, pas côté contenu.
- Options : (a) débugger ou recréer le serveur MCP ; (b) créer le board à la main dans FluentBoards en recopiant les 39 leçons listées dans le plan de formation ; (c) voie Novamira en PHP côté serveur (écrit dans la base FluentBoards, plus risqué, à valider).
- **Sécurité** : régénérer l'app password de contact@michaelkihl.fr (exposé en clair dans le chat).

## Gabarit d'une leçon (rappel)

Titre `# Leçon X.Y - <titre>` → `## Metadata` (Formation, Module, Durée cible ~mots, Type HeyGen+ElevenLabs, Objectif pédagogique, Prérequis) → `## Script narration` ([INTRO - face camera], sections [SECTION n], [ECRAN]/[FACE CAMERA], [OUTRO]) → `## Notes de production` (captures suggérées, transitions, tableau durée par section, sources).

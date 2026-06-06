# Avatar HeyGen schoolsWP - Phase 5 : stratégie avatar de Michaël KIHL

> Projet : créer le meilleur avatar HeyGen pour schoolsWP à partir de l'image de Michaël KIHL.
> Phase 5 : déduire la stratégie avatar à partir des faits confirmés (doc Phase 3) et des faits réels du compte HeyGen (vérifiés le 2026-05-29 via le MCP).
> Règle : les faits sont sourcés, les recommandations sont marquées comme telles, les hypothèses aussi. Statut : EN ATTENTE DE TA VALIDATION avant la Phase 6 (préparation des assets).

---

## Faits du compte HeyGen vérifiés (2026-05-29)

Ces faits viennent de ton compte réel, pas du marketing :

- **Plan creator, 600 crédits/mois, droits commerciaux OK** (un plan payant donne les droits commerciaux sur les outputs, cf. Phase 3).
- **Tu as déjà 4 looks** dans le groupe `eb4b43583683415b9d613e2004c86810` :
  - 1 **digital twin « Michaël KIHL »** (`bcc2e2951dff40ef8b1c860f691f02fa`) : ton vrai visage, 1280x720, paysage.
  - 3 **photo avatars « Le Guide Éclairant et Accessible »** : un persona IA distinct (pas ton visage).
- **Les 4 looks supportent `avatar_v` ET `avatar_iv`.** Avatar V est donc disponible sur ton vrai visage.
- **Voix FR : largement disponibles** (plus de 35 voix FR publiques) et **tu as un clone vocal FR fonctionnel** : « Michaël KIHL » (`2a1b7a035c104d56b280e1c518e40f87`). L'ancien clone `9fa1a596...` reste cassé (à ne pas utiliser).
- **Point clé qui relie au smoke test** : ton essai décevant (masterclass WP Social Ninja) tournait en **Avatar IV** sur le digital twin. **Avatar V n'a jamais été testé sur ton visage.** C'est la première chose à corriger.

## Fiche avatar schoolsWP

| Élément | Recommandation | Justification | Source ou hypothèse | Confiance |
|---|---|---|---|---|
| Type d'avatar | Digital twin (ton vrai visage), look `bcc2e29...` | Média fondé par toi : l'authenticité du vrai visage porte mieux qu'un persona IA. Tu l'as déjà créé | Fait compte + reco | Élevée |
| Moteur de rendu | Avatar V en priorité, Avatar IV en repli | Avatar V documenté comme "more natural motion and lip-sync" ; éligible sur ton look. Avatar IV si tu veux motion_prompt / expressiveness | Fait compte + doc Phase 3 | Élevée |
| Voix | ElevenLabs via `audio_url` public, en priorité | Découple voix et visage, contrôle total, tu améliores déjà ton clone ElevenLabs. Repli : ton clone HeyGen FR `2a1b7a03...` | Fait compte + reco | Élevée |
| Image source (si recapture) | Re-tourner un digital twin propre si Avatar V ne suffit pas | Le digital twin actuel date ; un footage 1080p+ continu 2 à 5 min améliore l'entraînement | Doc Phase 3 + hypothèse | Moyenne |
| Critères image / footage | 1080p minimum (4K/60fps mieux), prise continue, avec son, visage net et bien éclairé | "At least 1080p, 30fps", "one continuous recording", son obligatoire pour le lipsync | Doc Phase 3 (help.heygen.com) | Élevée |
| Style vestimentaire | Sobre, cohérent schoolsWP (haut uni, pas de motifs serrés qui moirent) | Un média pédagogique : lisibilité et neutralité priment | Reco | Moyenne |
| Cadrage | Buste, visage occupant une large part de l'image, regard caméra | La doc photo avatar insiste : "the character should take up a larger portion of the image" | Doc Phase 3 | Élevée |
| Arrière-plan | Neutre et stable (uni ou très peu chargé), couleur compatible vert #00D400 | Évite de distraire du propos ; cohérence de marque | Reco | Moyenne |
| Expression faciale | Posée, engageante, attentive ; pas figée | Custom Motion / Avatar V visent à lever l'effet robotique | Doc Phase 3 + reco | Moyenne |
| Niveau de sourire | Léger et naturel, pas permanent | Les défauts documentés incluent "sourires mal placés" | Doc Phase 3 (qualité) | Moyenne |
| Posture | Droite, stable, gestes mesurés | Crédibilité d'un formateur ; éviter la raideur ET l'agitation | Reco | Moyenne |
| Lumière | Frontale douce, uniforme, sans ombres dures | Conditionne la qualité du rendu (conseils captation) | Doc Phase 3 | Élevée |
| Format de sortie | 16:9 1080p pour les tutos et YouTube ; 9:16 pour les Shorts | Ratios confirmés (16:9, 9:16, 4:5, 5:4, 1:1, auto) | Doc Phase 3 | Élevée |
| Charte | Importer la charte schoolswp.com via Brand System (URL) + Brand Glossary pour la prononciation | Confirmé en doc ; fige "schoolsWP", "Kadence", "FluentCRM" | Doc Phase 3 | Moyenne (dispo par plan à vérifier) |
| Transparence IA | Mentionner l'usage d'un avatar IA dans les vidéos | Les Terms imposent la divulgation selon la loi applicable | Doc Phase 3 (Terms) | Élevée |

## Détail des recommandations

### Type d'avatar et moteur

Recommandation : reste sur **ton digital twin (vrai visage)** et **teste-le d'abord en Avatar V**, pas en Avatar IV. C'est la correction la plus directe au rendu décevant du smoke test, sans rien recréer. Si Avatar V ne te convainc toujours pas, deux pistes : recapturer un footage propre (1080p, prise continue, bonne lumière) pour ré-entraîner le digital twin, ou comparer avec un photo avatar de ta vraie photo. Les 3 looks « Le Guide Éclairant » restent une option de présentateur IA si un jour tu ne veux pas montrer ton visage, mais ce n'est pas l'identité d'un média fondé par toi.

### Voix

Recommandation : **voix ElevenLabs poussée en `audio_url`**, parce que tu maîtrises déjà cette brique et que ça découple totalement la voix du visage. Repli immédiat disponible : ton clone HeyGen FR `2a1b7a03...` (fonctionnel), ou une voix FR publique du catalogue. La question « voix FR » n'est plus un risque.

### Image, cadrage, lumière

Si recapture : 1080p minimum (4K/60fps idéal), prise continue sans coupure, avec ton audio, visage net occupant une large part du cadre, lumière frontale douce, fond neutre. Cadrage buste, regard caméra.

### Erreurs à éviter (grille de contrôle avant publication)

- Sourires permanents ou mal placés, regard fuyant.
- Raideur de la posture ou gestes parasites.
- Peau "plastique" ou incohérences entre scènes.
- Fond chargé qui distrait du propos.
- Oublier la mention IA.
- Lancer une génération en Avatar IV par défaut alors qu'Avatar V est éligible.

### Tests à réaliser (avant production de série)

1. **Re-générer l'intro 2.2 (smoke test) en Avatar V** sur le digital twin, même audio ElevenLabs, et comparer à la version Avatar IV décevante.
2. Tester 2 ou 3 réglages d'`expressiveness` / motion sur Avatar IV pour voir si le naturel s'améliore.
3. Comparer voix ElevenLabs (`audio_url`) contre clone HeyGen FR `2a1b7a03...` sur le même texte.
4. Tester un fond et une tenue, puis vérifier la cohérence du visage entre 2 looks.
5. Vérifier Brand System par URL sur schoolswp.com (extraction du vert #00D400).

### Limites à valider avant production

- Qualité réelle d'Avatar V sur ton visage (le seul vrai juge, c'est ton oeil sur le test 1).
- Disponibilité de Brand System / Brand Glossary sur le plan creator (à confirmer dans l'interface).
- Coût : Avatar IV/V = 20 crédits/min côté plan. Une capsule de 3 min ≈ 60 crédits. 600 crédits/mois = environ 30 min de vidéo avatar par mois sur le plan actuel. À cadrer selon ton volume cible.

## Lien avec le smoke test WP Social Ninja

Le rendu qui t'a déçu vient probablement d'un cumul : **moteur Avatar IV par défaut** (pas Avatar V), réglages voix ElevenLabs non optimisés, et un digital twin peut-être à recapturer. La Phase 5 propose de traiter ces causes dans l'ordre : moteur d'abord (Avatar V), voix ensuite, recapture seulement si nécessaire. C'est le pont entre ce projet de recherche et la reprise de la production des 39 leçons.

## Prochaine étape

Phase 5 rédigée. Avant la Phase 6 (préparation de la liste d'assets : photo/footage, scripts de test, charte, etc.), j'attends ta validation, et idéalement ton feu vert pour lancer le test 1 (intro 2.2 en Avatar V), qui validera ou non toute la stratégie d'un coup.

## Résultat du test Avatar V (2026-05-29)

Test réalisé : intro de la leçon 2.2 sur le **nouveau digital twin** (look `5f286a19`, groupe `49ac5c7e`), moteur **Avatar V**, 1080p 16:9, voix ElevenLabs poussée en `audio_url`. Fichier : `content/formations/wpsocialninja/production/2-2-intro-avatarV.mp4`.

Verdict de Michaël : **« mieux mais pas parfait »**. Donc Avatar V sur le nouveau twin améliore nettement le rendu Avatar IV décevant, mais ce n'est pas encore au niveau publication.

Combinaison qui tient pour l'instant : nouveau digital twin + Avatar V + voix ElevenLabs (`audio_url`) + MCP (crédits du plan).

Pistes non encore testées pour viser le « parfait » (à reprendre) :

- Tester les looks photo-avatar du même groupe (grey hoodie, chemise bleue, pull noir, chemise rouille) en Avatar V.
- Affiner la voix ElevenLabs (`stability` / `style` / `similarity`) ou comparer avec ton clone HeyGen FR `2a1b7a03`.
- Évaluer la source du digital twin (recapture 1080p en prise continue si le visage ou le lipsync reste en cause).

Statut : EN PAUSE à la demande de Michaël (2026-05-29).

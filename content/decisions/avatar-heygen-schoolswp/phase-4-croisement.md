# Avatar HeyGen schoolsWP - Phase 4 : croisement YouTube / documentation

> Projet : créer le meilleur avatar HeyGen pour schoolsWP à partir de l'image de Michaël KIHL.
> Phase 4 : confronter ce que dit la chaîne YouTube HeyGen (Phase 2, descriptions publiques, donc marketing) avec ce que confirme la documentation officielle (Phase 3, faits sourcés). Aucune nouvelle collecte web : synthèse directe des Phases 2 et 3.
> Décisions possibles : Confirmé / Partiellement confirmé / Non confirmé / Contradictoire / À vérifier dans le compte HeyGen.
> Statut : EN ATTENTE DE TA VALIDATION avant la Phase 5 (stratégie avatar).

---

## Tableau de croisement

| Sujet | Mention YouTube (marketing) | Confirmation documentation | Confiance | Risque | Décision |
|---|---|---|---|---|---|
| Avatar à partir d'une seule photo | "Turn any photo into a talking video", "une seule photo" | Doc confirme : Photo Avatar depuis une photo, "no video recording needed", lip-sync sur script | Élevée | Démos YouTube souvent faites avec des photos générées (Midjourney), pas de vrais portraits | Confirmé (principe). À tester sur une vraie photo de Michaël |
| Avatar V "le plus réaliste" | "The Most Realistic AI Avatar Yet" | Doc dit "latest engine", "more natural motion and lip-sync", PAS "most realistic" verbatim | Moyenne | Superlatif purement marketing | Partiellement confirmé |
| Digital Twin "en 15 secondes" | "Create your Digital Twin in 15 seconds" | Doc Digital Twin : 2 à 5 min de prise continue, 1080p, avec son. Le 15s vient d'Avatar V, pas du Digital Twin | Élevée | Confusion entre moteur (Avatar V) et type (Digital Twin) | Contradictoire (15s infirmé pour le Digital Twin) |
| Clonage de voix rapide | "Clone Your Voice in Minutes" | Doc confirme l'existence : POST /v3/voices/clone. Prérequis d'échantillon (durée, nombre) non documentés | Moyenne | Qualité réelle et prérequis inconnus | Partiellement confirmé |
| Voix française et multilingue | "175+ langues", lip-sync conservé | Doc : 300+ voix "across dozens of languages", mais FR / locale fr-FR non listé explicitement | Faible (pour le FR) | La qualité FR n'est pas démontrée par la doc | Non confirmé (FR). À vérifier dans le compte HeyGen |
| Voice Director / Voice Doctor | Direction du ton et correction de la voix | Doc : "voice design" génère 3 options depuis une description ; les noms "Voice Director / Doctor" ne sont pas verbatim | Moyenne | Termes marketing vs noms API | Partiellement confirmé |
| Custom Motion (Avatar V) | "Give your Avatar V natural movement", direction des gestes en langage naturel | Doc : motion_prompt et expressiveness sont documentés mais réservés à Avatar IV et aux images, et "ne marchent pas sur Avatar V" | Moyenne | Custom Motion (Avatar V) et motion_prompt (Avatar IV) semblent être deux mécanismes distincts | Contradictoire. À vérifier dans le compte HeyGen |
| Document / PPT / PDF vers vidéo | "Turn documents into videos in 5 minutes" | Doc : Video Agent produit une vidéo finie via un seul appel ; conversion de docs cohérente avec ce pipeline | Moyenne | Le "5 minutes" est un claim ; qualité de mise en scène auto à évaluer | Partiellement confirmé |
| Export SCORM pour e-learning | "Create SCORM Packages from AI Videos" | Doc confirme : SCORM 1.2 et 2004, export ZIP, mais réservé aux plans Business et Enterprise, "any SCORM-compliant LMS" (TutorLMS non nommé) | Élevée (existence), Faible (TutorLMS) | Plan Business minimum requis ; compat TutorLMS non garantie | Partiellement confirmé. À vérifier dans le compte HeyGen |
| Brand System par URL | Extraction de logo, typo, couleurs depuis l'URL du site | Doc confirme : "upload your website URL, and HeyGen will automatically generate a brand system" | Élevée | Disponibilité par plan non documentée ; fidélité de l'extraction à tester | Confirmé |
| Brand Glossary (prononciation) | Figer la prononciation des termes | Doc confirme : règles de prononciation et traduction, import CSV | Élevée | Disponibilité par plan non documentée | Confirmé |
| "300 looks" par avatar | "Add 300 looks to your Digital Twin" | Doc confirme la mécanique groupe / looks multiples, mais le chiffre "300" et la cohérence du visage entre looks ne sont pas documentés | Moyenne | Chiffre marketing ; cohérence du visage non garantie | Partiellement confirmé |
| Coût en crédits | "Credit-Based Plans Explained" | Doc confirme : Avatar IV/V = 20 crédits/min, Avatar III = 3, traduction 2 ou 5 (côté plan web) | Élevée | Taux dollars du wallet API non publié | Confirmé (côté plan web) |
| Crédits API séparés du plan | Non explicité côté YouTube | Doc confirme : MCP consomme les crédits du PLAN, la clé API consomme un wallet séparé, "two billing pools are independent" | Élevée | Piège déjà rencontré dans le projet (API REST = wallet vide) | Confirmé |
| Automatisation Video Agent / MCP | "Video Agent API inside Claude Code", "HeyGen MCP" | Doc confirme : Video Agent (POST /v3/video-agents), MCP recommandé pour agents, webhooks (HMAC, retries 24h) | Élevée | Limites de débit chiffrées non publiées | Confirmé |
| Pipeline "HeyGen + Hyperframes" | "Build Full AI Videos with HeyGen + Hyperframes" | Hyperframes n'apparaît dans AUCUNE doc HeyGen : c'est un outil interne schoolsWP, sans lien produit documenté | Élevée | Risque de croire que Hyperframes est une fonction HeyGen | Contradictoire (clarifié : Hyperframes n'est pas un produit HeyGen) |
| Cas d'usage formation / éducateurs | "HeyGen for Training Videos", "for Education", Coursera, School of AI | Doc confirme le positionnement (SCORM, LMS) ; détails d'intégration à valider | Moyenne | Preuves clients = marketing | Confirmé (positionnement) |
| Consentement de l'avatar | Mention du consentement à la création | Doc confirme : consentement requis pour digital_twin uniquement, biométrie Art. 9(2)(a) GDPR, retrait possible | Élevée | Avatar de Michaël = consentement auto-fourni, pas de tiers | Confirmé |
| Lipsync sur audio externe | Implicite (voix off, éviter de re-enregistrer) | Doc confirme : audio_url public ou audio_asset_id, exclusif du script TTS | Élevée | L'URL audio doit être publiquement accessible | Confirmé |

## Synthèse du croisement

### Solide (Confirmé par la doc, on peut s'appuyer dessus)

- Photo Avatar à partir d'une seule photo, sans vidéo de consentement.
- Lipsync via une URL audio publique : on peut brancher ta voix ElevenLabs.
- Crédits API séparés des crédits du plan ; le MCP dépense le plan (notre voie).
- Coût Avatar IV/V = 20 crédits/min côté plan.
- Brand System par URL et Brand Glossary pour la charte et la prononciation de "schoolsWP".
- Automatisation via Video Agent, MCP et webhooks.
- Consentement maîtrisé (ton propre visage, Art. 9 GDPR).

### À tester avant de s'engager (Partiellement confirmé)

- Qualité réelle d'un Photo Avatar à partir d'une vraie photo de Michaël (la doc ne donne aucune métrique).
- Clonage de voix (prérequis d'échantillon non documentés).
- SCORM vers TutorLMS (existe, mais Business/Enterprise et LMS non nommé).
- Cohérence du visage entre plusieurs looks.

### Contradictions à lever

- "Digital Twin en 15 secondes" : faux pour le Digital Twin (2 à 5 min). Le 15s appartient à Avatar V. Ne pas planifier un tournage de 15s pour un Digital Twin.
- "Custom Motion sur Avatar V" contre "motion_prompt réservé à Avatar IV" : deux mécanismes probablement distincts. À clarifier avant de promettre un contrôle de gestes sur Avatar V.
- "Hyperframes" n'est pas une fonction HeyGen : c'est ton outil interne. Ne pas le présenter comme une brique HeyGen.

### À vérifier dans le compte HeyGen (bloquant pour la Phase 5)

- Présence et qualité de voix françaises (sinon : voix ElevenLabs via audio_url).
- Mécanisme exact de Custom Motion sur Avatar V.
- Looks de ton avatar éligibles à Avatar V (champ supported_api_engines).
- Compatibilité SCORM avec TutorLMS (test d'import réel).

## Implication pour la Phase 5

Le croisement pointe une stratégie de départ à faible risque : **Photo Avatar (moteur Avatar IV) + voix via audio_url ElevenLabs**, parce que c'est la combinaison la plus solidement confirmée par la doc et la moins dépendante des points encore flous (voix FR native, durée de tournage Digital Twin, Custom Motion Avatar V). Le Digital Twin et Avatar V restent des pistes de montée en qualité, à tester une fois les points en compte levés. Ces orientations sont des recommandations, à arbitrer en Phase 5.

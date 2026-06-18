# Brief de leçon : Protéger le contenu vidéo de tes cours

**Formation** : Maîtriser TutorLMS
**Placement proposé** : nouvelle leçon dans M11 (Inscription & Gestion utilisateurs, Premium), positionnée comme leçon de synthèse "accès & protection"
**Type** : Vidéo HeyGen (face caméra intro/conclusion + screencast admin WordPress)
**Durée estimée** : 7 à 8 min (leçon plus dense que la moyenne, car elle consolide une pile complète)
**Date** : 2026-05-28
**Source d'inspiration** : tutorlms.com/blog/protect-elearning-course-videos (blog officiel Themeum, avril 2026) - à retraiter en voix schoolsWP, jamais en argumentaire produit

---

## 1. Pourquoi cette leçon (analyse de couverture)

La protection vidéo est aujourd'hui éclatée dans la formation : chaque pièce existe, mais aucune leçon ne donne la vue d'ensemble "comment je verrouille mes vidéos". Trois réglages purement défensifs ne sont par ailleurs traités nulle part.

| Couche de protection | Statut dans la formation | Action de cette leçon |
| --- | --- | --- |
| Content Drip (déblocage progressif) | Couvert : L7.1 (+ M6, M13) | Renvoyer vers L7.1, rappeler l'angle sécurité |
| Course / Lesson Preview (vitrine) | Couvert : L7.5 (+ M4, M5) | Renvoyer vers L7.5, rappeler le risque "preview trop large" |
| Email Verification (faux comptes) | Couvert : L11.1 | Renvoyer vers L11.1 |
| Bunny.net / CDN vidéo | Couvert : M16 (dès 50 vidéos) | Renvoyer, et y rattacher le watermarking |
| **Prevent Hotlinking** | **Absent** | **Config live dans cette leçon** |
| **Copy Protection (clic droit)** | **Absent** | **Config live dans cette leçon** |
| **Limit Active Login Sessions** | **Absent** | **Config live dans cette leçon** |
| **Watermarking dynamique** | **Absent** | **Expliqué (non natif, via CDN)** |

Conclusion : la leçon a une vraie valeur ajoutée. Elle comble 3 trous de réglage et transforme des éléments dispersés en une méthode unique.

---

## 2. Angle pédagogique

Fil rouge : "Aucun réglage ne protège tout seul. La sécurité, c'est de l'empilement de couches : si une cède, les autres tiennent." On part de la menace (ce qu'un pirate tente), puis on pose la défense en face. C'est plus marquant qu'une liste de cases à cocher.

Promesse de la leçon : à la fin, l'élève a une pile de défense activée et sait laquelle bloque quelle attaque.

---

## 3. Plan détaillé (segments)

### Segment 1 : Le modèle de menace (face caméra, ~1 min)
Poser les 4 vecteurs d'attaque concrets, sans dramatiser :
- Vol d'URL directe : quelqu'un récupère le lien brut de la vidéo et le partage hors paywall.
- Enregistrement d'écran puis redistribution.
- Partage d'identifiants : un compte acheté, dix personnes qui regardent (le "problème Netflix").
- Téléchargement massif puis demande de remboursement (le "smash-and-grab").

### Segment 2 : Couche accès, le socle (screencast, ~1 min)
- Rappel : pas d'inscription, pas de vidéo. Renvoi à L11.1 (Email Verification) pour filtrer les faux comptes.
- Piège du Preview trop large : renvoi à L7.5. Message : ne mets le preview que sur les leçons d'appel, jamais sur le coeur du cours.

### Segment 3 : Bloquer le partage d'URL - Prevent Hotlinking (screencast config live, ~1,5 min)
- Chemin : Tutor LMS > Settings > Advanced > Content Security > activer "Prevent Hotlinking".
- Expliquer ce que ça fait : la vidéo auto-hébergée ne se lit que depuis ton domaine. Le lien brut ailleurs est bloqué.
- Note technique à dire : ça modifie le fichier .htaccess (hébergement type Apache). Si un avertissement apparaît, vérifier les droits d'écriture sur .htaccess.
- Renvoi : si tu es sur Bunny.net (M16), il faut AUSSI activer la restriction par domaine côté CDN. La protection TutorLMS couvre la couche WordPress, pas le CDN.

### Segment 4 : Friction anti-copie - Copy Protection (screencast config live, ~1 min)
- Chemin : Tutor LMS Pro > Settings > Advanced > Content Security > activer "Copy Protection".
- Effet : désactive le clic droit (Enregistrer sous, copier l'URL source, ouvrir le média).
- **Réserve honnête à formuler dans la vidéo** : ça désactive le clic droit sur TOUT le site, blog inclus, pas seulement les pages de cours. À activer en connaissance de cause si tu as un blog public. Ça arrête le vol occasionnel, pas un pirate déterminé. C'est de la friction, pas un coffre-fort.

### Segment 5 : Couper le partage d'identifiants - Limit Active Login Sessions (screencast config live, ~1 min)
- Chemin : Tutor LMS Pro > Settings > Authentication > Manage Active Logins > activer "Limit Active Login Sessions", régler "Maximum Active Sessions" (1 ou 2).
- Effet : au-delà de la limite, toute nouvelle connexion est bloquée tant que l'utilisateur n'a pas fermé une session existante.

### Segment 6 : Freiner le smash-and-grab - Content Drip (screencast court ou renvoi, ~30 s)
- Angle sécurité du drip : si tout est dispo d'un coup, on télécharge tout en 24 h puis on se fait rembourser. Le drip rend ça beaucoup plus pénible.
- Renvoi à L7.1 pour la config détaillée. Coupler avec une politique de remboursement claire.

### Segment 7 : Tracer les fuites - Watermarking (face caméra + capture, ~1 min)
- Message clé : TutorLMS ne fait PAS de watermarking dynamique nativement. Il faut un hébergeur vidéo tiers.
- Aligner sur la reco schoolsWP existante (M16) : Bunny.net Stream dès 50 vidéos, qui supporte le watermark par token viewer (identifiant personnalisé incrusté). Alternatives à citer : VdoCipher (DRM dédié), Vimeo (watermark texte statique).
- Bénéfice : si une vidéo fuit, le watermark identifie le compte source.

### Segment 8 : La pile complète (face caméra + tableau récap à l'écran, ~1 min)
Afficher le tableau menace -> défense comme fiche mémo de fin de leçon (voir section 5).
Phrase de clôture : "Tu n'arrêteras pas le pirate le plus motivé, aucun système ne le fait. Mais tu rends le vol difficile, traçable et coûteux. La plupart des gens passent leur chemin."

---

## 4. Captures à réaliser (screencast)

1. Tutor LMS > Settings > Advanced > Content Security (vue d'ensemble de la section).
2. Toggle "Prevent Hotlinking" activé + l'éventuel avertissement .htaccess.
3. Toggle "Copy Protection" activé.
4. Démonstration : clic droit bloqué sur une page de cours (avant/après si possible).
5. Settings > Authentication > Manage Active Logins > "Limit Active Login Sessions" + champ Maximum Active Sessions.
6. Démonstration : message de blocage à la connexion quand la limite est atteinte.
7. Rappel visuel des addons Content Drip et Course Preview (Tutor LMS Pro > Addons) pour les renvois.
8. Vue côté Bunny.net : option de restriction par domaine + watermark token (si compte dispo, sinon capture doc).
9. Tableau récap "stack de sécurité" en plein écran pour la fin.

---

## 5. Tableau récap (fiche mémo de fin de leçon)

| Menace | Défense TutorLMS |
| --- | --- |
| Regarder sans payer | Inscription obligatoire + Preview limité aux leçons d'appel |
| Enregistrer en masse avant remboursement | Content Drip (déblocage progressif) |
| Partage de l'URL vidéo brute | Prevent Hotlinking (+ restriction domaine côté CDN) |
| Copie et "enregistrer sous" occasionnels | Copy Protection (clic droit désactivé) |
| Partage d'identifiants | Limit Active Login Sessions (1 ou 2) |
| Redistribution d'un enregistrement | Watermarking via Bunny.net / VdoCipher |
| Faux comptes et bots | Email Verification (SMTP requis) |

---

## 6. Réserves schoolsWP (à intégrer dans le ton, pas à masquer)

- **Tutor LMS Pro requis** pour Copy Protection, Limit Active Login, Prevent Hotlinking et les addons Drip/Preview. Le dire clairement, c'est une leçon de module Premium.
- **Hotlinking = .htaccess** : fonctionne sur hébergement Apache, écrit dans .htaccess. Vérifier les droits d'écriture du fichier avant de promettre que ça marche.
- **Copy Protection est global** : il coupe le clic droit sur tout le site, blog compris. À ne pas activer à l'aveugle si le site a une partie publique soignée.
- **Watermarking non natif** : nécessite un CDN vidéo. Ne pas laisser croire que TutorLMS le fait seul.
- **Email Verification = SMTP** : sans SMTP correctement configuré, aucun email de vérification ne part. Renvoyer vers la config SMTP.
- **Pas de promesse absolue** : on ne dit jamais "tes vidéos seront impossibles à voler". On dit "tu rends le vol difficile, traçable et coûteux". Cohérent avec la règle schoolsWP de ne pas vendre du risque zéro.

---

## 7. Points clés (pour le récap de fin)

- La sécurité vidéo est un empilement : aucune couche ne suffit seule.
- 3 réglages clés souvent oubliés : Prevent Hotlinking, Copy Protection, Limit Active Login Sessions.
- Le watermarking passe obligatoirement par un hébergeur vidéo tiers (Bunny.net dès 50 vidéos chez schoolsWP).
- Le Content Drip n'est pas qu'un outil pédagogique : c'est aussi une défense anti smash-and-grab.
- Copy Protection désactive le clic droit sur tout le site : décision à prendre en connaissance de cause.

---

## 8. Mots clés SEO

protéger vidéos cours en ligne, sécuriser contenu TutorLMS, anti-piratage formation WordPress, prevent hotlinking TutorLMS, copy protection LMS, limiter sessions connexion TutorLMS, watermark vidéo formation, protéger cours TutorLMS contre le téléchargement

---

## 9. Quiz suggéré (1 question pour le module)

**Question** : Quel réglage TutorLMS désactive le clic droit sur l'ensemble du site pour freiner la copie de vidéos ?
- A) Prevent Hotlinking
- B) Copy Protection (réponse)
- C) Content Drip
- D) Limit Active Login Sessions

*Explication : Copy Protection désactive le menu contextuel (clic droit) sur tout le site, ce qui empêche "Enregistrer sous" et la copie de l'URL source. C'est une couche de friction, pas une protection absolue.*

---

## 10. Décisions à valider avec Michael

1. **Placement définitif** : leçon dans M11 (recommandé) ou ailleurs ? Alternative possible : une mini-leçon sécurité rattachée à M7 (addons) ou à M3 (réglages), mais M3 est gratuit/lead magnet et ces features sont Pro, donc M11 reste le meilleur hôte.
2. **Numéro de leçon** : M11 compte 10 leçons + quiz. Cette leçon deviendrait la 11e (ou s'insère selon ta logique).
3. **Application à tes propres cours** : ce brief sert aussi de checklist pour verrouiller le cours Samaritain Security et les futures formations. Dis-moi si tu veux que je transforme la section 4 en checklist d'activation à appliquer directement sur schoolswp.com.
4. **Étape suivante** : une fois le placement validé, je peux rédiger le script vidéo HeyGen complet au format des autres leçons (INTRO/SCREENCAST/TRANSITION).

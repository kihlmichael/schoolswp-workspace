# Checklist : verrouiller tes propres cours vidéo sur schoolswp.com

**Cible** : cours Samaritain Security + futures formations TutorLMS hébergées sur schoolswp.com
**Source** : leçon 11.11 de la formation + blog Themeum (avril 2026)
**Date** : 2026-05-28
**Prérequis** : Tutor LMS Pro actif (la plupart des réglages ci-dessous sont Pro)

Cette checklist est l'application concrète, pour tes propres cours, de la pile de sécurité enseignée en leçon 11.11. À cocher une fois, à revérifier à chaque nouveau cours.

---

## État appliqué sur schoolswp.com (2026-05-28)

Vérifié en production via Novamira. État réel et décisions :

- **Accès réservé aux inscrits** (`student_must_login_to_view_course`) : déjà ON. ✓
- **Vérification email** (`enable_email_verification`) : déjà ON, FluentSMTP actif. ✓
- **Limit Active Login** (`enable_limit_active_device`) : ACTIVÉ ce jour. Max appareils = 1. Passer à 2 (`device_limit`) si tu veux autoriser ordi + mobile pour un même étudiant.
- **Copy Protection** : laissé OFF (décision). Désactive le clic droit/copie sur tout le site public (blog 357 articles) pour une protection contournable. Non retenu pour un site de contenu.
- **Prevent Hotlinking** : DIFFÉRÉ. La règle native TutorLMS est globale (bloque toutes les images jpg/png/gif + vidéos selon le referer) : risque OG/Google Images, et `.htaccess` co-géré par FlyingPress/SecuPress. Surtout : 0 vidéo auto-hébergée à ce jour (110 leçons, aucune source vidéo). À reprendre quand les vidéos existeront : si self-hosted, règle `.htaccess` ciblée vidéos uniquement (mp4/mov/webm) + test OG/Google Images/crawlers ; si Bunny.net, protection côté CDN.
- **Content Drip** (addon) : non activé. À activer quand un cours payant aura du contenu.
- **Watermarking** : via Bunny.net quand les vidéos seront hébergées (cf. M16, dès 50 vidéos).

---

## Couche 1 : Accès (le socle)

- [ ] **Email Verification** activée : Tutor LMS > Settings > Authentication > Email Verification. Bloque les faux comptes.
  - [ ] Vérifier que le SMTP WordPress est configuré, sinon aucun email de vérification ne part.
- [ ] **Lesson Preview** désactivé sur les leçons de coeur : Course Builder > chaque leçon > toggle Lesson Preview OFF.
  - [ ] Garder le preview uniquement sur 2 ou 3 leçons d'introduction (vitrine de conversion).

## Couche 2 : Bloquer le partage d'URL (Prevent Hotlinking)

- [ ] **Prevent Hotlinking** activé : Tutor LMS > Settings > Advanced > Content Security > Prevent Hotlinking.
  - [ ] Vérifier après activation qu'aucun avertissement .htaccess n'apparaît (droits d'écriture du fichier côté EasyHoster).
  - [ ] Tester : copier l'URL brute d'une vidéo de cours et tenter de l'ouvrir dans un onglet déconnecté. Doit être bloqué.
- [ ] Si CDN vidéo (Bunny.net) : activer **aussi** la restriction par domaine côté Bunny.net (réglage séparé de TutorLMS).

## Couche 3 : Friction anti-copie (Copy Protection)

- [ ] **Décision à prendre** : Copy Protection désactive le clic droit sur TOUT schoolswp.com, blog (357 articles) compris, pas seulement les pages de cours.
  - [ ] Si activé : Tutor LMS Pro > Settings > Advanced > Content Security > Copy Protection.
  - [ ] Si non activé : noter pourquoi (UX blog public). Alternative : s'appuyer sur hotlinking + watermarking, qui sont plus robustes.

## Couche 4 : Couper le partage d'identifiants (Limit Active Login)

- [ ] **Limit Active Login Sessions** activé : Tutor LMS Pro > Settings > Authentication > Manage Active Logins.
  - [ ] Maximum Active Sessions réglé sur 1 (strict) ou 2 (tolérant, ordi + mobile du même élève).
  - [ ] Tester : se connecter au même compte depuis 3 navigateurs, vérifier le blocage du 3e.

## Couche 5 : Freiner le téléchargement massif (Content Drip)

- [ ] **Content Drip** activé sur les cours premium : Tutor LMS Pro > Addons > Content Drip, puis configuration par cours.
  - [ ] Mode adapté (séquentiel ou par date) pour empêcher l'aspiration en 24 h.
- [ ] Politique de remboursement claire affichée (couplée au drip pour bloquer le record-then-refund).

## Couche 6 : Tracer les fuites (Watermarking)

- [ ] Décider de l'hébergement vidéo selon le volume (reco schoolsWP : Bunny.net dès 50 vidéos).
  - [ ] Si Bunny.net Stream : activer le watermark par token viewer (identifiant unique incrusté par spectateur).
  - [ ] En dessous de 50 vidéos : YouTube non listé ou Vimeo peuvent suffire (watermarking limité ou absent, l'accepter).

## Vérification finale

- [ ] Refaire le parcours d'achat en tant qu'élève test (compte non admin) sur Samaritain Security.
- [ ] Confirmer que chaque couche activée se comporte comme prévu (preview limité, URL bloquée, sessions limitées, drip actif).
- [ ] Re-vérifier sur schoolswp.com en prod, pas seulement en local ou en staging.

---

## Réserves importantes

- **Pas de promesse de risque zéro** : ces couches rendent le vol difficile, traçable et coûteux. Elles n'arrêtent pas un pirate déterminé. C'est cohérent avec la règle schoolsWP de ne pas vendre du risque zéro.
- **Copy Protection est global** : ne pas l'activer à l'aveugle vu le blog public schoolswp.com.
- **Hotlinking dépend de l'hébergement** : si EasyHoster bloque l'écriture .htaccess ou tourne sur une stack non compatible, la protection ne s'applique pas. À vérifier en conditions réelles.
- **Watermarking = coût CDN** : Bunny.net est facturé (5 à 15 dollars/mois pour 50 à 100 vidéos selon M16). Arbitrage volume/budget à faire.

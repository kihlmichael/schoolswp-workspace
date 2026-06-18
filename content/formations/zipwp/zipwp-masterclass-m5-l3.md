# Lecon 5.3 - Site de formation : ZipWP + TutorLMS

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 - Sites business avec ZipWP
- **Lecon** : 3/8
- **Duree cible** : 12 min
- **Objectif pedagogique** : Creer un site de formation complet avec ZipWP pour la base et TutorLMS pour la partie ecole en ligne - du cours a la vente, en passant par le parcours apprenant.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

C'est le use case schoolsWP par excellence. Un site de formation en ligne, construit avec ZipWP pour la vitrine et TutorLMS pour l'ecole. C'est exactement ce modele qu'on utilise ici - et c'est le type de site le plus rentable que tu puisses creer.

ZipWP genere le site. TutorLMS cree l'ecole. Les deux ensemble, c'est un business complet en moins d'une journee.

---

[SECTION 1 - Generer la base avec ZipWP]

Commence par le prompt. Pour un site de formation, sois specifique sur ta thematique, ton public, et ton modele economique.

Exemple de prompt : "Je cree une plateforme de formation en ligne sur la photographie pour debutants. Mon public est constitue d'amateurs de 25-45 ans qui veulent apprendre la photo avec leur smartphone. Je propose des cours video structures en modules. J'ai besoin d'une page d'accueil attractive, une page catalogue de cours, une page a propos, une page temoignages, et une page contact."

Lance la generation. ZipWP va creer un site avec Astra et Spectra qui te donne la structure visuelle - l'accueil, la navigation, les pages de contenu. Mais pour la partie cours et apprentissage, il te faut TutorLMS.

---

[SECTION 2 - Installer TutorLMS Pro]

TutorLMS est le LMS que schoolsWP recommande. Il est puissant, bien integre a l'ecosysteme WordPress, et compatible avec Astra et Spectra.

Installation : Extensions → Ajouter → "TutorLMS" → Installer → Activer la version gratuite. Ensuite, si tu as la licence Pro, uploade le fichier zip de TutorLMS Pro via Extensions → Ajouter → Telecharger → Active.

La version gratuite suffit pour demarrer - tu peux creer des cours, des lecons, des quiz. La version Pro ajoute les fonctionnalites business : certificats, assignments, notifications email avancees, integration e-commerce, et surtout les rapports detailles sur la progression de tes apprenants.

Premier reflexe apres l'installation : va dans TutorLMS → Settings. Configure les pages (page de cours, page de dashboard apprenant), active les inscriptions, et choisis ton integration e-commerce - WooCommerce ou SureCart. On y revient dans la section 4.

---

[SECTION 3 - Creer un cours structure]

Un bon cours en ligne a trois niveaux : le cours, les modules (ou topics), et les lecons.

Cree ton premier cours : TutorLMS → Courses → Add New. Donne un titre, une description, une image de couverture. Dans les parametres du cours, definis : le niveau (debutant, intermediaire, avance), la duree estimee, et le nombre maximum d'inscrits si tu veux limiter.

Ajoute un module : clique sur "Add New Topic" dans l'editeur du cours. Nomme-le - par exemple "Module 1 - Les bases de la composition". Ajoute une description courte.

Ajoute des lecons dans le module : clique sur "Add Lesson" sous le topic. Chaque lecon a un titre, un contenu texte, et surtout - un contenu video. Tu peux heberger tes videos sur YouTube, Vimeo, ou utiliser PrestoPlayer (un autre produit BSF) pour un lecteur integre avec chapitres et controles avances.

Repete pour chaque module et chaque lecon. Un bon premier cours a entre 3 et 6 modules, avec 3 a 5 lecons par module. Pas besoin de creer 50 heures de contenu pour demarrer - un cours concentre de 2-3 heures vaut mieux qu'un cours dilue de 20 heures.

---

[SECTION 4 - Configurer le paiement]

Pour vendre tes cours, tu as deux options d'integration.

Option 1 - WooCommerce : va dans TutorLMS → Settings → Monetization. Choisis "WooCommerce". TutorLMS va creer un "produit WooCommerce" lie a chaque cours. Tu definis le prix dans WooCommerce, et quand un apprenant achete, il obtient automatiquement l'acces au cours.

Option 2 - SureCart : meme principe. Choisis "SureCart" dans les parametres de monetisation. Cree un produit SureCart lie au cours. L'achat donne l'acces. Le checkout est plus rapide et plus fluide qu'avec WooCommerce.

Mon conseil : si tu vends uniquement des cours, SureCart est le meilleur choix. Leger, rapide, parfait pour des produits digitaux. Si tu vends aussi des produits physiques a cote de tes cours, WooCommerce est plus adapte.

---

[SECTION 5 - Page de vente du cours avec Spectra]

La page de cours generee par TutorLMS est fonctionnelle, mais elle n'est pas optimisee pour la vente. Pour ca, tu crees une page de vente dediee avec Spectra.

Cree une nouvelle page dans WordPress. Utilise les blocs Spectra pour construire la structure : un hero avec le titre du cours et un visuel attractif. Une section "Ce que tu vas apprendre" avec une liste a puces. Le programme detaille - les modules et lecons. Des temoignages d'anciens apprenants. Le formateur - ta bio avec ta photo. L'offre - le prix, ce qui est inclus, et un bouton d'achat bien visible.

Le bouton d'achat pointe soit vers le checkout SureCart (un bloc integre), soit vers la page produit WooCommerce. Dans les deux cas, le visiteur peut acheter sans quitter visuellement le site.

Astuce Spectra : utilise le bloc "Pricing Table" pour presenter differentes formules si tu en as - acces basique, acces premium avec coaching, acces lifetime. Le choix entre plusieurs options augmente les conversions.

---

[SECTION 6 - Le parcours apprenant complet]

Resume le flux complet pour que tout soit clair.

Etape 1 : le visiteur arrive sur ton site ZipWP. Il decouvre ta page d'accueil, tes cours, ton positionnement. Etape 2 : il clique sur un cours qui l'interesse. Il arrive sur ta page de vente Spectra. Etape 3 : il clique sur "Acheter". Le checkout SureCart ou WooCommerce s'ouvre. Il paye. Etape 4 : il recoit un email de confirmation avec ses identifiants de connexion. Etape 5 : il se connecte au dashboard apprenant TutorLMS. Il voit ses cours, sa progression, ses certificats. Etape 6 : il suit les lecons, complete les quiz, obtient son certificat.

Tout est automatique. Tu crees le cours une fois, tu configures le paiement une fois, et le systeme tourne tout seul. C'est ca la puissance du duo ZipWP + TutorLMS.

Le conseil schoolsWP : ZipWP cree le site. TutorLMS cree l'ecole. Ensemble, tu as un business de formation complet.

---

[OUTRO]

Tu sais maintenant comment construire un site de formation de A a Z. ZipWP pour la vitrine, TutorLMS pour les cours, SureCart ou WooCommerce pour le paiement, et Spectra pour la page de vente.

C'est le modele que des milliers de formateurs utilisent - et c'est celui qu'on recommande chez schoolsWP.

Dans la prochaine lecon, on ajoute une couche de conversion avec CartFlows. Comment creer un funnel de vente qui maximise le revenu par visiteur sur ton site ZipWP.

---

## Notes de production

### Captures d'ecran suggerees

1. **Prompt ZipWP** - Prompt optimise pour un site de formation
2. **TutorLMS Settings** - Ecran de configuration avec integration e-commerce
3. **Course Builder** - Creation d'un cours avec modules et lecons
4. **Page de vente Spectra** - Structure hero + programme + offre + CTA
5. **Dashboard apprenant** - Vue eleve avec progression et certificats
6. **Parcours complet** - Schema du flux visiteur → achat → apprenant

### Transitions

- Intro → Section 1 : ouverture ZipWP, prompt formation
- Section 1 → Section 2 : site genere, passage a l'installation TutorLMS
- Section 2 → Section 3 : creation du premier cours
- Section 3 → Section 4 : configuration paiement
- Section 4 → Section 5 : creation page de vente Spectra
- Section 5 → Section 6 : schema du parcours complet
- Section 6 → Outro : vue globale du site de formation fini

### Notes HeyGen / ElevenLabs

- Ton enthousiaste mais structure - c'est le use case phare, montrer la fierte schoolsWP
- Section 3 (creation cours) : rythme tutoriel, bien montrer la hierarchie cours/modules/lecons
- Section 6 (parcours) : rythme plus lent, enumerer chaque etape clairement
- Insister sur "ZipWP cree le site, TutorLMS cree l'ecole" - c'est le message a retenir

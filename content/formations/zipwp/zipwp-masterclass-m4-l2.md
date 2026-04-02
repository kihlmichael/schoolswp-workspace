# Lecon 4.2 — Creer un Blueprint a partir d'un site existant

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 4 — Blueprints et workflow professionnel
- **Lecon** : 2/6
- **Duree cible** : 8 min
- **Objectif pedagogique** : Savoir creer un Blueprint a partir d'un site ZipWP existant, comprendre ce qui est sauvegarde, et organiser sa bibliotheque de Blueprints.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Tu as un site ZipWP qui est exactement comme tu le veux. Le design est propre, les plugins sont configures, le SEO est en place. C'est ta base ideale. Maintenant, tu vas la sauvegarder en tant que Blueprint pour pouvoir la reutiliser a volonte.

---

[SECTION 1 — Prerequis : preparer ton site]

Avant de sauvegarder un Blueprint, nettoie ton site. Tout ce que tu sauvegardes sera inclus dans chaque futur deploiement — y compris ce qui ne devrait pas y etre.

Supprime le contenu specifique a un client. Les textes personnalises, les images du client, les temoignages specifiques. Remplace-les par du contenu generique mais representatif — des textes placeholders du type "Votre titre ici", des images neutres qui correspondent au secteur.

Verifie les plugins. Garde uniquement ceux qui font partie de ta stack standard. Desactive et supprime les plugins temporaires ou experimentaux.

Verifie les reglages. Le SEO est configure avec les bonnes options par defaut ? Les formulaires fonctionnent ? Le theme est configure avec les couleurs et la typographie que tu veux comme base ?

Le but : ton site doit etre un point de depart propre, pas un projet termine avec du contenu specifique.

---

[SECTION 2 — Creer le Blueprint]

Va dans le dashboard ZipWP. Selectionne le site que tu veux sauvegarder comme Blueprint.

Dans les options du site, clique sur "Save as Blueprint".

ZipWP te demande un nom et une description. Le nom est important — tu vas le chercher dans ta bibliotheque dans trois mois. Sois precis.

Mauvais nom : "Mon template". Bon nom : "Site vitrine coach — Astra + Spectra + SureForms + Rank Math — FR".

La description detaille ce qui est inclus : "Site vitrine 5 pages (accueil, services, a propos, temoignages, contact). Theme Astra Pro, Spectra blocks, SureForms contact, Rank Math configure. Couleurs neutres, typographie Inter. Pret pour personnalisation client."

Le processus de sauvegarde prend quelques secondes a quelques minutes selon la taille du site.

---

[SECTION 3 — Ce qui est sauvegarde — et ce qui ne l'est pas]

Ce qui est inclus dans le Blueprint : le theme Astra et toute sa configuration — couleurs, typographie, header, footer, layouts. Tous les plugins installes et leurs reglages. Toutes les pages avec leur contenu et leur structure Spectra. Les formulaires SureForms. Les medias — images, logos, icones presents dans la mediatheque. Les reglages WordPress — permaliens, lecture, discussion.

Ce qui n'est PAS sauvegarde : les credentials — tes identifiants de connexion ne sont pas transferes. Les donnees transactionnelles — si tu avais WooCommerce avec des commandes, elles ne sont pas incluses. Les configurations serveur — les reglages PHP, le cache, le SSL sont lies a l'hebergement, pas au Blueprint.

Point important : si tu utilises des images sous licence ou des images clients dans ton Blueprint, elles seront dupliquees a chaque deploiement. Utilise des images libres de droits dans tes Blueprints.

---

[SECTION 4 — Organiser sa bibliotheque]

Au fil du temps, tu vas creer plusieurs Blueprints. Sans organisation, tu te retrouves avec une liste confuse.

Convention de nommage recommandee :

[Type de site] — [Stack] — [Particularite] — [Langue]

Exemples :
- "Vitrine coach — Astra + Spectra — 5 pages — FR"
- "E-commerce artisan — Astra + WooCommerce — FR"
- "Portfolio photographe — Astra + Spectra — galerie — FR"
- "Landing page — Astra + Spectra — conversion — FR"

Limite par plan : le plan Pro te donne 5 Blueprints. Le plan Business monte a 20. Si tu atteins la limite, supprime les Blueprints obsoletes — ceux que tu n'as pas deployes depuis plus de 6 mois sont probablement depasses.

Conseil : garde un document — un simple fichier texte ou un tableau — qui liste tes Blueprints avec leur date de creation, leur contenu, et les projets pour lesquels tu les as utilises. Quand tu auras 10 ou 15 Blueprints, ce document te fera gagner du temps.

---

[OUTRO]

Tu as cree ton premier Blueprint. Un site complet, empaquete, pret a etre deploye pour le prochain projet. Plus besoin de reconfigurer la meme chose a chaque fois.

Prochaine lecon : deployer un Blueprint pour un nouveau projet. On voit comment passer du Blueprint au site personnalise en quelques minutes.

---

## Notes de production

### Captures d'ecran suggerees

1. **Site avant Blueprint** — Le site propre, pret a etre sauvegarde
2. **Save as Blueprint** — Bouton dans le dashboard ZipWP
3. **Formulaire Blueprint** — Champs nom et description remplis avec l'exemple
4. **Bibliotheque Blueprints** — Liste des Blueprints avec noms organises
5. **Schema inclusion** — Ce qui est inclus vs ce qui ne l'est pas (deux colonnes)

### Transitions

- Intro → Section 1 : zoom sur le site a sauvegarder
- Section 1 → Section 2 : transition vers le dashboard ZipWP
- Section 2 → Section 3 : animation "package" avec les composants qui entrent
- Section 3 → Section 4 : transition vers la bibliotheque de Blueprints
- Section 4 → Outro : retour avatar

### Notes HeyGen / ElevenLabs

- Ton methodique — on construit une vraie procedure
- Section 1 : insister sur le nettoyage — "tout ce que tu sauvegardes sera duplique"
- Section 2 : exemples de nommage lus lentement, bien articules
- Section 4 : ton organisationnel, on structure pour le long terme

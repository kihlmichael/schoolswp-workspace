# Lecon 6.5 - ZipWP + PrestoPlayer : video integree

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 6 - Ecosysteme et business
- **Lecon** : 5/10
- **Duree cible** : 6 min
- **Objectif pedagogique** : Decouvrir PrestoPlayer, le lecteur video de Brainstorm Force - hebergement, chapitres, CTA in-video, paywall, et analytics - et l'integrer dans un site ZipWP.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

La video est partout. Sur les pages de vente, dans les formations, sur les pages d'accueil. Et la facon dont tu integres la video sur ton site change la perception de qualite - un player YouTube brut avec des suggestions de videos concurrentes a la fin, ce n'est pas professionnel.

PrestoPlayer resout ca. C'est le lecteur video de Brainstorm Force - integre a WordPress, compatible avec Astra et Spectra, et concu pour les createurs qui veulent garder le controle sur l'experience video.

---

[SECTION 1 - Ce que PrestoPlayer apporte]

PrestoPlayer n'est pas un service d'hebergement video. C'est un lecteur - il lit tes videos depuis la source que tu choisis, mais avec ton propre design, tes propres controles, et tes propres regles.

Le lecteur est propre. Pas de logo YouTube, pas de suggestions de videos tierces, pas de publicites. Juste ta video, dans le style de ton site.

Les fonctions cles : chapitres - tu divises ta video en sections navigables. Le spectateur peut sauter directement au chapitre qui l'interesse. Indispensable pour les formations.

CTA in-video - tu peux afficher un appel a l'action a un moment precis de la video. A la minute 3, un bouton "Telecharge le guide" apparait. A la fin de la video, un bouton "Inscris-toi au cours suivant". C'est du marketing integre a l'experience video.

Restriction d'acces - tu peux proteger une video derriere un paywall. Seuls les membres connectes ou les acheteurs d'un produit specifique voient la video. Les autres voient un message "Achete le cours pour acceder a cette video." Integration native avec WooCommerce, SureCart, et TutorLMS.

Analytics - PrestoPlayer te dit combien de personnes ont regarde ta video, jusqu'ou elles ont regarde, et ou elles ont decroche. Des donnees precieuses pour ameliorer tes contenus.

---

[SECTION 2 - Les sources video supportees]

Tu n'heberges pas tes videos sur PrestoPlayer. Tu les heberges ailleurs, et PrestoPlayer les lit.

YouTube : la solution gratuite. Tu uploades sur YouTube en "non-liste" (pas indexe dans la recherche YouTube) et PrestoPlayer l'affiche sur ton site sans le branding YouTube. Avantage : gratuit, CDN mondial de Google, pas de limite de stockage. Inconvenient : dependance a YouTube, qualite video parfois reduite par la compression.

Vimeo : la solution premium. Upload sur Vimeo avec les parametres de confidentialite (domaine restreint - la video ne se lit que sur ton site). Avantage : meilleure qualite, pas de branding, controle total. Inconvenient : payant (le plan Vimeo Starter commence autour de 12 dollars par mois).

Bunny.net : la solution technique. Un CDN video avec un cout au Go tres bas. Tu uploades, tu recuperes un lien de streaming, PrestoPlayer le lit. Avantage : prix imbattable pour les gros volumes, CDN rapide. Inconvenient : setup plus technique, pas d'interface aussi polie que Vimeo.

Self-hosted : tes fichiers video directement sur ton serveur WordPress. A eviter sauf pour des videos courtes et legeres. Les videos sont lourdes - un fichier de 10 minutes peut peser 500 Mo. Ca consomme ta bande passante et ralentit ton site.

---

[SECTION 3 - Integration avec un site ZipWP]

Installe PrestoPlayer : Extensions → Ajouter → "PrestoPlayer" → Installer → Activer.

Les sites generes par ZipWP supportent PrestoPlayer nativement. Tu peux ajouter un bloc PrestoPlayer dans n'importe quelle page Spectra - il s'integre visuellement comme un bloc natif.

Cas d'usage concret : site de formation avec videos protegees. Tu as un cours TutorLMS avec 10 lecons video. Au lieu d'integrer les videos directement dans les lecons TutorLMS (ce qui fonctionne mais avec un player basique), tu utilises PrestoPlayer. Chaque lecon contient un bloc PrestoPlayer avec la video correspondante. Tu configures les chapitres, tu ajoutes un CTA a la fin ("Passe a la lecon suivante"), et tu actives la restriction d'acces - seuls les inscrits au cours voient la video.

Autre cas : page d'accueil avec video de presentation. Un bloc PrestoPlayer dans le hero de ta page d'accueil, avec une video de 2 minutes qui presente ton activite. Autoplay desactive (c'est important - l'autoplay agace les visiteurs), mais une vignette attractive qui donne envie de cliquer.

---

[OUTRO]

PrestoPlayer, c'est la couche video professionnelle de ton site ZipWP. Pas de branding tiers, des chapitres, des CTA au bon moment, une restriction d'acces native, et des analytics pour comprendre comment tes videos performent.

Si tu integres de la video dans ton business - formation, marketing, presentation - PrestoPlayer est l'outil qui fait la difference entre un embed YouTube brut et une experience video maitrisee.

Dans la prochaine lecon, on entre dans les comparatifs externes. ZipWP face a son concurrent direct : 10Web. Un comparatif honnete.

---

## Notes de production

### Captures d'ecran suggerees

1. **PrestoPlayer vs YouTube embed** - Comparaison visuelle des deux lecteurs
2. **Chapitres** - Video avec la liste des chapitres navigables
3. **CTA in-video** - Bouton d'action qui apparait pendant la lecture
4. **Paywall** - Message de restriction d'acces sur une video protegee
5. **Analytics** - Dashboard PrestoPlayer avec taux de completion

### Transitions

- Intro → Section 1 : comparaison visuelle YouTube embed vs PrestoPlayer
- Section 1 → Section 2 : logos des sources video (YouTube, Vimeo, Bunny)
- Section 2 → Section 3 : integration dans un site ZipWP, editeur Gutenberg
- Section 3 → Outro : recap visuel des fonctionnalites cles

### Notes HeyGen / ElevenLabs

- Ton enthousiaste mais factuel - presenter les fonctionnalites sans survendre
- Section 1 (fonctions) : bien detailler chaque fonctionnalite avec son use case
- Section 2 (sources) : ton comparatif, avantages/inconvenients de chaque option
- Lecon courte (6 min) - rester concis, pas de digressions

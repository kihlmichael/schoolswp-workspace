# Lecon 2.8 - SEO des pages funnel : indexer ou noindex ?

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 2 - Pages de vente et landing pages
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir quelles pages funnel CartFlows indexer et lesquelles mettre en noindex, configurer le noindex via Rank Math, et optimiser les landing pages indexees pour le SEO.

---

## Script narration

**[INTRO - face camera]**

Tu as construit ton funnel CartFlows. Tes pages sont en ligne. Et la, une question que personne ne se pose assez tot : est-ce que Google doit voir ces pages ?

La reponse n'est pas la meme pour toutes tes pages. Certaines doivent etre indexees pour t'apporter du trafic organique. D'autres doivent etre invisibles pour Google. Dans cette lecon, on fait le tri - page par page - et je te montre comment configurer ca proprement avec Rank Math.

---

**[SECTION 1 - La question fondamentale]**

**[ECRAN - slide "Indexer ou noindex ?"]**

Quand tu publies une page WordPress, Google peut la trouver et l'indexer. Ca veut dire qu'elle apparait dans les resultats de recherche. Pour un article de blog ou une page de service, c'est ce que tu veux.

Mais pour un funnel, c'est different. Un funnel est concu comme un parcours guide : le visiteur arrive par un point d'entree precis, et il suit les etapes dans l'ordre. Si Google indexe tes pages d'upsell, de thank you ou de checkout, des visiteurs peuvent atterrir au milieu du funnel - sans contexte, sans intention d'achat, sans avoir vu ta page de vente.

Le resultat : un taux de rebond eleve sur ces pages, une experience utilisateur confuse, et du contenu duplique potentiel si tu as plusieurs variantes. C'est mauvais pour ton SEO global.

La regle de base : indexe les points d'entree, noindex tout le reste.

---

**[SECTION 2 - Pages a indexer]**

**[ECRAN - slide "Pages a INDEXER" avec exemples]**

Deux types de pages meritent d'etre indexees.

**Les landing pages evergreen.** Si ta page de vente cible un mot-cle recherche - par exemple "formation LMS WordPress" ou "comparatif page builder" - tu veux que Google la trouve. C'est une page d'entree de funnel qui peut generer du trafic organique en continu. Elle a un titre pertinent, un contenu riche, et elle repond a une intention de recherche reelle.

**Les pages opt-in pour des lead magnets recherches.** Si tu proposes un guide gratuit sur un sujet que les gens cherchent - "checklist securite WordPress" par exemple - ta page opt-in peut se positionner dans Google. Le visiteur arrive via la recherche, il trouve ton lead magnet, il s'inscrit. C'est du trafic qualifie gratuit.

Le critere pour decider : est-ce que quelqu'un pourrait taper cette requete dans Google et trouver ta page pertinente ? Si oui, indexe. Si la page n'a aucun sens hors du contexte de ton funnel, noindex.

---

**[SECTION 3 - Pages a NE PAS indexer]**

**[ECRAN - slide "Pages en NOINDEX" avec liste]**

Voici les pages a mettre systematiquement en noindex.

**Les pages checkout.** Personne ne cherche "page de paiement formation WordPress" dans Google. Ta page checkout n'a aucune valeur SEO. Et si elle est indexee, elle peut creer de la confusion avec d'autres pages de ton site.

**Les pages upsell et downsell.** Ces pages sont concues pour etre vues apres un achat. Hors contexte, elles n'ont aucun sens - le visiteur ne sait pas de quel produit on parle, ni pourquoi on lui propose une offre complementaire.

**Les pages thank you.** Pages de remerciement, pages de confirmation, pages de telechargement. Aucune raison de les indexer. Et certaines contiennent des liens de telechargement ou des infos privees que tu ne veux pas exposer publiquement.

**Les variantes A/B.** Si tu testes deux versions d'une meme page, une seule doit etre indexee - l'originale. Les variantes en noindex evitent le contenu duplique.

En resume : checkout, upsell, downsell, thank you, variantes A/B - tout en noindex.

---

**[SECTION 4 - Comment mettre en noindex avec Rank Math]**

**[ECRAN - editeur de page, sidebar Rank Math, onglet Advanced]**

La configuration prend 10 secondes par page. Ouvre la page dans l'editeur, et dans la sidebar Rank Math, clique sur l'onglet "Advanced".

Tu trouves un champ "Robots Meta". Par defaut, il est sur "Index". Change-le en "No Index". C'est tout.

Rank Math ajoute automatiquement la balise meta robots noindex dans le code HTML de la page. Google recoit le signal et n'indexe pas la page. Elle reste accessible par URL directe - tes visiteurs peuvent toujours y acceder via ton funnel - mais elle n'apparait pas dans les resultats de recherche.

Un raccourci pour gagner du temps : si tu as beaucoup de pages funnel, tu peux utiliser les reglages globaux de Rank Math. Va dans Rank Math → Titles & Meta → Pages individuelles. Mais pour les pages CartFlows, je recommande de le faire page par page - ca te force a reflechir a chaque page individuellement.

Verifie ta configuration avec le test "URL Inspection" dans Google Search Console. Colle l'URL de ta page noindex et confirme que Google voit bien la directive noindex.

---

**[SECTION 5 - Optimiser une landing page indexee]**

**[ECRAN - Rank Math SEO settings sur une landing page]**

Si tu decides d'indexer une landing page, fais-le correctement. Trois elements a optimiser.

**Le titre SEO.** C'est ce qui apparait dans Google. Il doit contenir ton mot-cle principal et donner envie de cliquer. "Formation LMS WordPress - Cree et vends tes cours en ligne" est mieux que "Page de vente - Mon produit". Configure-le dans Rank Math → onglet General → Edit Snippet.

**La meta description.** 150-160 caracteres qui resument l'offre et incitent au clic. Inclus le mot-cle, le benefice principal, et un element de differenciation. "Apprends a creer une plateforme LMS WordPress rentable. 12 modules, support inclus, satisfait ou rembourse 30 jours."

**Le H1 optimise.** Le titre principal visible sur ta page doit correspondre a l'intention de recherche. Si tu cibles "formation LMS WordPress", ton H1 doit contenir cette expression - pas exactement la meme, mais reconnaissable par Google et par le visiteur.

Un bonus : ajoute du contenu textuel sur ta landing page. Les pages de vente purement visuelles - grosses images, peu de texte - se positionnent mal. Google a besoin de texte pour comprendre ta page. Tes sections arguments, temoignages et FAQ sont du contenu indexable. Plus ta page est riche en texte pertinent, mieux elle se positionne.

---

**[OUTRO - face camera]**

La regle est simple : indexe tes landing pages, noindex tout le reste. Checkout, upsell, downsell, thank you - tout en noindex via Rank Math en 10 secondes par page.

Et si tu indexes une landing page, traite-la comme un vrai contenu SEO : titre optimise, meta description soignee, H1 avec ton mot-cle, et suffisamment de texte pour que Google comprenne de quoi il s'agit.

C'est la fin du Module 2. Tu sais maintenant construire des pages de vente, des pages opt-in, integrer les accelerateurs de conversion, et gerer le SEO de tes pages funnel. Dans le Module 3, on passe au checkout et au paiement.

---

## Notes de production

### Captures d'ecran suggerees

- Slide "Indexer ou noindex ?" avec schema funnel annote (section 1)
- Slide "Pages a INDEXER" - exemples landing page evergreen + opt-in lead magnet (section 2)
- Slide "Pages en NOINDEX" - liste checkout / upsell / downsell / thank you / A/B (section 3)
- Rank Math sidebar → onglet Advanced → champ Robots Meta sur "No Index" (section 4)
- Rank Math → Edit Snippet avec titre SEO et meta description remplis (section 5)
- Google Search Console → URL Inspection montrant la directive noindex (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1, 2, 3 : slides synthetiques
- Section 4 : screencast Rank Math dans l'editeur
- Section 5 : screencast Rank Math SEO settings
- Outro : face camera, CTA vers Module 3

### Duree estimee par section

| Section | Duree |
| --- | --- |
| Intro | 0:25 |
| Section 1 - La question fondamentale | 0:50 |
| Section 2 - Pages a indexer | 1:00 |
| Section 3 - Pages a ne pas indexer | 1:00 |
| Section 4 - Noindex avec Rank Math | 1:10 |
| Section 5 - Optimiser une landing indexee | 1:15 |
| Outro | 0:20 |
| **Total** | **~6:00** |

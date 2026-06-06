# Lecon 3.4 - SEO post-generation : Rank Math, titres, meta, schema

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 - De la demo au site en production
- **Lecon** : 4/7
- **Duree cible** : 12 min
- **Objectif pedagogique** : Combler le gap SEO de ZipWP en installant Rank Math, configurant les titres/meta/schema, et en soumettant le sitemap a Google Search Console.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

On va parler du plus gros angle mort de ZipWP. L'IA genere un site fonctionnel, avec du contenu contextualise et un design propre. Mais le SEO ? Il est basique. SureRank pose des fondations minimales - un sitemap, des meta titles generiques. C'est insuffisant pour ranker sur Google.

Le SEO, c'est ce que l'IA ne fait pas pour toi. Et 30 minutes de configuration SEO aujourd'hui, c'est des mois de trafic organique demain. Alors on va tout reprendre.

---

[SECTION 1 - Installer et configurer Rank Math]

Premiere etape : desactive SureRank. Va dans Extensions → Extensions installees, desactive SureRank. On ne va pas le supprimer tout de suite - on le desactive proprement.

Ensuite, installe Rank Math. Extensions → Ajouter → cherche "Rank Math SEO". Installe et active.

Rank Math te lance un assistant de configuration. Suis-le. Les points importants :

Type de site : choisis le bon - blog, boutique en ligne, site vitrine, portfolio. Ca influence les schemas par defaut.

Google Search Console : connecte ton compte Google. Rank Math peut se lier directement a la Search Console pour importer des donnees.

Sitemap : active le sitemap XML. Rank Math va generer un sitemap plus complet que celui de SureRank.

Le reste des options par defaut est correct pour demarrer. Tu pourras affiner plus tard.

---

[SECTION 2 - Titres SEO et meta descriptions]

C'est le travail le plus important. Chaque page de ton site a besoin d'un titre SEO et d'une meta description ecrits pour les humains ET pour Google.

Le titre SEO, c'est ce qui apparait en bleu dans les resultats Google. La meta description, c'est le texte en gris en dessous. Ce sont tes deux premieres chances de convaincre quelqu'un de cliquer.

Pour chaque page, va dans l'editeur WordPress. Scrolle jusqu'au bloc Rank Math en bas. Tu verras le titre SEO et la meta description.

Regles pour le titre SEO : il contient ton mot-cle principal, il fait moins de 60 caracteres, il est unique pour chaque page. Pas de titres generiques du type "Accueil" ou "Services". Ecris un titre qui donne envie de cliquer.

Exemple pour un photographe : au lieu de "Services", ecris "Reportage Photo Mariage Bordeaux | Tarifs et Formules".

Regles pour la meta description : elle contient ton mot-cle, elle fait entre 120 et 155 caracteres, elle decrit ce que le visiteur va trouver sur la page, et elle inclut un appel a l'action implicite.

Exemple : "Decouvre mes formules de reportage photo mariage a Bordeaux. Tarifs, exemples de realisations et reservation en ligne."

Fais ca pour chaque page. Oui, chaque page. C'est le travail qui paye le plus en SEO.

---

[SECTION 3 - H1 unique et structure des titres]

Chaque page doit avoir un seul H1. Un seul. C'est le titre principal de la page - celui que Google lit en premier pour comprendre le sujet.

Verifie chaque page. ZipWP genere parfois plusieurs H1, ou aucun. Ouvre l'editeur, verifie la hierarchie des titres. Le H1 est en haut, les H2 structurent les sections, les H3 detaillent les sous-sections.

Ton H1 contient ton mot-cle principal pour la page. Il est descriptif. Il est different du titre SEO - le titre SEO est pour Google, le H1 est pour le visiteur qui est deja sur la page.

---

[SECTION 4 - Schema markup]

Le schema, c'est du code structure que Google utilise pour comprendre ton site. Ca ne se voit pas sur la page, mais ca influence comment ton site apparait dans les resultats - avec des etoiles, des FAQ, des informations d'entreprise.

Avec Rank Math, va dans les reglages → Titles & Meta → choisis le type de schema par defaut.

Pour un site vitrine d'entreprise locale : configure le schema LocalBusiness. Renseigne le nom de l'entreprise, l'adresse, le telephone, les horaires d'ouverture. Google utilisera ces informations pour afficher un Knowledge Panel.

Pour un site d'entreprise sans adresse physique : utilise le schema Organization. Nom, logo, reseaux sociaux.

Pour des pages avec des questions-reponses : ajoute le schema FAQ. Rank Math te permet de l'ajouter directement depuis l'editeur de chaque page. Les FAQ apparaissent en accordeon dans les resultats Google - ca prend de la place et ca attire les clics.

---

[SECTION 5 - Sitemap et Google Search Console]

Le sitemap, c'est la carte de ton site que tu donnes a Google. Il liste toutes les pages que tu veux indexer.

Rank Math genere un sitemap automatiquement. Verifie-le : va sur ton-site.fr/sitemap_index.xml. Tu devrais voir la liste de tes pages. Si une page n'apparait pas, verifie qu'elle n'est pas marquee "noindex" dans les reglages Rank Math de la page.

Maintenant, soumets ce sitemap a Google Search Console. Va sur search.google.com/search-console. Ajoute ta propriete - ton domaine. Google te demandera de verifier la propriete - Rank Math a un bouton pour ca dans ses reglages.

Une fois verifie, va dans Sitemaps dans le menu de gauche. Saisis sitemap_index.xml et soumets. Google va commencer a crawler ton site dans les heures qui suivent.

---

[SECTION 6 - Images et maillage interne]

Deux dernieres optimisations rapides mais essentielles.

Les images : chaque image de ton site doit avoir un texte alternatif - le alt text. C'est ce que Google lit pour comprendre l'image, et c'est aussi ce qui s'affiche si l'image ne charge pas. Va dans la mediatheque, et pour chaque image, ecris un alt text descriptif qui inclut un mot-cle quand c'est pertinent. Pas de "image1.jpg" - ecris "Reportage photo mariage chateau Bordeaux".

Le maillage interne : tes pages doivent se lier entre elles. La page d'accueil pointe vers les services. La page services pointe vers le portfolio. Le portfolio pointe vers la page contact. Ce reseau de liens aide Google a comprendre la structure de ton site et a distribuer l'autorite entre les pages.

Un maillage basique pour un site vitrine : chaque page du menu est liee depuis la page d'accueil, et chaque page inclut un lien vers la page contact ou un appel a l'action.

---

[OUTRO]

Le SEO de ton site est maintenant solide. Rank Math est installe, chaque page a son titre SEO et sa meta description, la structure H1 est propre, le schema est configure, le sitemap est soumis a Google, et les images ont leur alt text.

30 minutes de travail. Mais ces 30 minutes font la difference entre un site que personne ne trouve et un site qui attire du trafic organique chaque jour.

Prochaine lecon : la securite. Mises a jour, backups, protection - on verrouille tout.

---

## Notes de production

### Captures d'ecran suggerees

1. **Rank Math install** - Ecran d'installation de Rank Math dans WordPress
2. **Assistant Rank Math** - Etape de configuration (type de site, Search Console)
3. **Editeur Rank Math** - Bloc SEO en bas de l'editeur avec titre et meta description
4. **Resultat Google** - Mockup d'un resultat avec titre SEO + meta description
5. **Schema LocalBusiness** - Configuration du schema dans Rank Math
6. **Sitemap XML** - Vue du sitemap dans le navigateur
7. **Google Search Console** - Soumission du sitemap
8. **Alt text** - Mediatheque WordPress avec le champ alt text rempli

### Transitions

- Intro → Section 1 : apparition du logo Rank Math
- Section 1 → Section 2 : zoom sur l'editeur WordPress, bloc Rank Math
- Section 2 → Section 3 : animation hierarchie H1 → H2 → H3
- Section 3 → Section 4 : apparition du code schema en overlay
- Section 4 → Section 5 : transition vers Google Search Console
- Section 5 → Section 6 : split screen images + liens
- Section 6 → Outro : retour avatar, ton de synthese

### Notes HeyGen / ElevenLabs

- Ton affirme et motivant - le SEO est souvent percu comme penible
- Phrase cle a appuyer : "Le SEO, c'est ce que l'IA ne fait pas pour toi"
- Section 2 : rythme methodique, exemples concrets prononces lentement
- Section 4 : articuler "schema markup", "LocalBusiness", "Organization"
- Section 6 : rythme rapide, on boucle efficacement

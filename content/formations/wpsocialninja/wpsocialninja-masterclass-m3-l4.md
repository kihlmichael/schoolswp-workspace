# Leçon 3.4 - Tourisme et local : Airbnb, Booking.com, Tripadvisor

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 3 - Business Reviews
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Connecter trois plateformes du tourisme et du local : Tripadvisor par clé API (la voie recommandée) et Place ID, Booking.com via un cookie technique posé dans un snippet, et Airbnb par une méthode manuelle avancée à réserver aux profils techniques.
- **Prérequis** : Leçon 3.3 vue. Pour Airbnb et Booking.com, un plugin de snippets de code comme FluentSnippets installé.

---

## Script narration

**[INTRO - face camera]**

Cette leçon s'adresse en priorité au tourisme et au local : gîtes, hôtels, restaurants, locations. On va connecter trois plateformes, et je vais être direct avec toi sur leur niveau de difficulté.

Tripadvisor est la plus propre des trois, avec une vraie clé API. Booking.com et surtout Airbnb demandent des contournements techniques, parce que ces plateformes ne proposent pas d'accès officiel pour les avis. Je vais te montrer chaque méthode, et te dire clairement quand c'est à la portée de tous et quand il vaut mieux être à l'aise techniquement. On commence par la plus simple.

---

**[SECTION 1 - Tripadvisor : la clé API recommandée]**

**[ECRAN - tripadvisor.com/developers → My API → Create API Key]**

Tripadvisor propose deux méthodes : par URL d'entreprise ou par clé API. La doc recommande la clé API, car elle offre un transfert de données plus fiable et un meilleur contrôle. On part donc sur l'API.

Tu te connectes à ton compte développeur Tripadvisor, tu vas dans My API, et tu cliques sur Create API Key.

**[ECRAN - formulaire d'infos entreprise + restriction de domaine]**

Tripadvisor te demande quelques informations sur ton entreprise, et surtout de vérifier ton site. Dans la section de restriction de clé, tu renseignes ton nom de domaine et tu enregistres. La clé se génère, et tu la copies avec le bouton Copy to Clipboard.

Un point à connaître : Tripadvisor offre une clé API gratuite jusqu'à cinq mille requêtes, mais tu dois fournir des informations de facturation pour l'obtenir. Au-delà, il faut passer sur leurs forfaits payants.

**[ECRAN - page entreprise Tripadvisor, Place ID dans l'URL après le "d"]**

Il te faut aussi le Place ID. Tu le trouves dans l'adresse de ta page d'établissement Tripadvisor : c'est l'identifiant qui commence par la lettre d. Par exemple, pour un identifiant d752551, ton Place ID est 752551, sans le d. Tu le copies.

**[ECRAN - WP Social Ninja → Platforms → Tripadvisor, type API Key, collage clé + ID, Save]**

Dans le plugin, section Platforms, tu ouvres les réglages Tripadvisor. Tu choisis le type d'identifiant API Key, tu colles ta clé et ton ID dans les bons champs, puis Save. Le plugin affiche d'abord les cinq avis les plus récents, stockés sur ton site, et vérifie régulièrement les nouveaux.

---

**[SECTION 2 - Booking.com : le cookie dans un snippet]**

**[ECRAN - slide "Booking.com : Pro + cookie technique"]**

Booking.com monte d'un cran en complexité, et deux choses à savoir d'emblée. D'abord, il te faut WP Social Ninja Pro pour cette plateforme. Ensuite, il n'y a pas d'API officielle, donc on passe par un contournement : récupérer un cookie technique et le poser dans un snippet de code.

**[ECRAN - Booking.com, Inspect → onglet Application → Cookies → AWS-WAF-Token]**

Concrètement, tu ouvres ta page d'établissement sur Booking.com, tu fais clic droit puis Inspect pour ouvrir les outils de développement. Tu vas dans l'onglet Application, puis Cookies, et tu cherches dans la liste un cookie nommé AWS-WAF-Token. Tu copies sa valeur.

**[ECRAN - FluentSnippets → Create Snippet, code add_filter avec le cookie]**

Cette valeur, tu la places dans un snippet de code, avec un plugin comme FluentSnippets que la doc recommande. Tu crées un snippet, tu colles le bout de code fourni par WP Social Ninja, et tu remplaces la mention prévue par la valeur du cookie que tu viens de copier. Tu enregistres le snippet.

**[ECRAN - retour Platforms → Booking, collage de l'URL d'établissement, Save]**

Enfin, tu copies l'URL de ton établissement depuis la barre d'adresse de Booking.com, tu la colles dans la configuration Booking du plugin, et tu cliques sur Save. Ton établissement est ajouté.

**[FACE CAMERA]**

Sois conscient d'une chose : ce cookie peut expirer. Si un jour tes avis Booking.com cessent de se mettre à jour, c'est probablement lui. Il faudra alors refaire l'opération. C'est le prix d'une plateforme sans accès officiel.

---

**[SECTION 3 - Airbnb : la méthode manuelle avancée]**

**[ECRAN - slide "Airbnb : méthode avancée, pas d'API publique"]**

On termine par la plus technique : Airbnb. Et je vais être franc, c'est la connexion la plus exigeante du module. Airbnb ne propose aucune API publique pour les avis. Le plugin utilise donc un contournement qui passe par les outils de développement du navigateur.

**[ECRAN - page annonce Airbnb, Inspect → onglet Network, filtre StaysPdpReviewsQuery]**

Le principe : sur ta page d'annonce Airbnb, tu ouvres Inspect, onglet Network. Tu filtres selon ce que tu cherches. Pour les avis d'un logement, tu tapes StaysPdpReviewsQuery. Pour les infos de l'établissement, StaysPdpSections. Tu rafraîchis la page, tu cliques sur la requête, et tu vas chercher deux types de clés : une API Key dans l'onglet Headers, et une clé secrète, le sha256Hash, dans l'onglet Payload.

**[ECRAN - FluentSnippets, code add_filter avec les clés Airbnb]**

Ces clés, tu les poses dans un snippet, là encore via FluentSnippets. La doc précise que les trois premières clés sont obligatoires : la clé API principale, la clé des avis du logement, et la clé des infos de l'établissement. Tu actives le snippet.

**[ECRAN - retour Platforms → Airbnb, collage de l'URL du logement, Save]**

Ensuite seulement, tu colles l'URL de ton logement, expérience ou établissement dans la configuration Airbnb, et tu enregistres.

**[FACE CAMERA]**

Trois points à retenir honnêtement. Un : cette méthode utilise des outils internes d'Airbnb, donc Airbnb peut changer ces clés à tout moment, ce qui casserait la connexion. Tu devras alors recommencer. Deux : en version gratuite, Airbnb est limité à cinq avis, jusqu'à cent en version Pro. Trois : si tu n'es pas à l'aise avec l'inspecteur du navigateur, fais-toi accompagner, ce n'est pas la connexion à tenter en débutant.

---

**[OUTRO - face camera]**

Tu as vu trois niveaux : Tripadvisor propre avec sa clé API, Booking.com et Airbnb avec leurs contournements par cookie et clés manuelles. Le bon réflexe : privilégier Tripadvisor quand c'est possible, et garder en tête que les méthodes par snippet demandent un peu de maintenance. Dans la prochaine leçon, on passe au commerce en ligne : AliExpress, WooCommerce et FluentCart. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Tripadvisor : My API → Create API Key + restriction de domaine (section 1)
- Tripadvisor : Place ID dans l'URL, le "d" barré pour montrer qu'on l'exclut (section 1)
- Tripadvisor : configuration dans le plugin, type API Key (section 1)
- Slide "Booking.com : Pro + cookie" (section 2)
- Booking.com : Inspect → Application → Cookies → AWS-WAF-Token surligné (section 2)
- FluentSnippets : snippet Booking avec emplacement du cookie (section 2)
- Slide "Airbnb : méthode avancée" (section 3)
- Airbnb : Network → filtres StaysPdpReviewsQuery / StaysPdpSections, Headers (API Key) et Payload (sha256Hash) (section 3)
- FluentSnippets : snippet Airbnb avec les filtres add_filter (section 3)

### Transitions

- Intro : face camera, ton honnête sur la gradation de difficulté
- Section 1 : screencast Tripadvisor, rythme fluide (c'est la voie propre)
- Section 2 : screencast Booking.com, ralentir sur Inspect → Cookies
- Section 2 fin : face camera sur l'expiration du cookie
- Section 3 : screencast Airbnb, le plus lent, montrer clairement Network / Headers / Payload
- Section 3 fin : face camera ferme sur les trois mises en garde Airbnb
- Outro : face camera, CTA visuel vers la leçon 3.5

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Tripadvisor | 2:15 |
| Section 2 - Booking.com | 2:15 |
| Section 3 - Airbnb | 2:40 |
| Outro | 0:15 |
| **Total** | **~8:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__tripadvisor-configuration.md`
- Doc : `sources/docs/guide__business-reviews__booking-com-configuration.md`
- Doc : `sources/docs/guide__business-reviews__airbnb-configuration.md`
- Vidéos officielles : #44 (How to add Tripadvisor Reviews), #41 (Showcase Booking.com Reviews), #38 (Embed Airbnb Reviews)

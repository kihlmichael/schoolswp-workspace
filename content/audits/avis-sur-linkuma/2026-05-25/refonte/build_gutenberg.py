"""Génère le post_content Gutenberg/Kadence pour /avis-sur-linkuma/ v2.

Sortie : sandbox-workspace/post-54381-v2-content.html
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

CTA_URL = "https://schoolswp.com/linkuma/"

# Médias existants (URLs WP)
IMG_HERO = "https://schoolswp.com/wp-content/uploads/2024/08/linkuma-plateforme-netlinking-accompagnement-personnalise.jpg"
IMG_OFFRES = "https://schoolswp.com/wp-content/uploads/2024/08/interface-utilisateur-offres-seo-linkuma.jpg"
IMG_COMMANDE = "https://schoolswp.com/wp-content/uploads/2024/08/interface-utilisateur-commande-redaction-seo-linkuma.jpg"
IMG_DELEGATION = "https://schoolswp.com/wp-content/uploads/2024/08/interface-delegation-commandes-linkuma.jpg"
FLUENT_MEDIA_ID = 2928785


def kad_singlebtn(text: str, uid_a: str, uid_b: str) -> str:
    """Bloc Kadence advancedbtn + singlebtn vers le cloak."""
    return (
        f'<!-- wp:kadence/advancedbtn {{"uniqueID":"54381_{uid_a}","btns":[]}} -->'
        f'<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btns54381_{uid_a}">'
        f'<!-- wp:kadence/singlebtn {{"uniqueID":"54381_{uid_b}","text":"{text}","link":"{CTA_URL}","target":"_blank",'
        f'"color":"palette9","background":"palette1","gradient":"linear-gradient(135deg, var(u002du002dglobal-palette1) 0%, var(u002du002dglobal-palette2) 100%)","backgroundType":"gradient",'
        f'"colorHover":"palette1","backgroundHover":"palette9",'
        f'"borderStyle":[{{"top":["palette9","",""],"right":["palette9","",""],"bottom":["palette9","",""],"left":["palette9","",""],"unit":"px"}}],'
        f'"borderHoverStyle":[{{"top":["palette1","",""],"right":["palette1","",""],"bottom":["palette1","",""],"left":["palette1","",""],"unit":"px"}}],'
        f'"icon":"fas_arrow-right","inheritStyles":"outline","displayShadow":true,"displayHoverShadow":true,'
        f'"shadow":[{{"color":"#000000","opacity":0.2,"spread":0,"blur":4,"hOffset":0,"vOffset":2,"inset":false}}],'
        f'"shadowHover":[{{"color":"#000000","opacity":0.4,"spread":0,"blur":10,"hOffset":0,"vOffset":2,"inset":false}}],'
        f'"noCustomDefaults":true}} /-->'
        f'</div>'
        f'<!-- /wp:kadence/advancedbtn -->'
    )


def p(text: str) -> str:
    return f'<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->'


def h(level: int, text: str) -> str:
    if level == 2:
        return f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{text}</h2>\n<!-- /wp:heading -->'
    return f'<!-- wp:heading {{"level":{level}}} -->\n<h{level} class="wp-block-heading">{text}</h{level}>\n<!-- /wp:heading -->'


def ul(items: list[str]) -> str:
    inner = '\n'.join(f'<!-- wp:list-item -->\n<li>{x}</li>\n<!-- /wp:list-item -->' for x in items)
    return f'<!-- wp:list -->\n<ul class="wp-block-list">\n{inner}\n</ul>\n<!-- /wp:list -->'


def img(url: str, alt: str, caption: str | None = None, link: str | None = None) -> str:
    """wp:image (sans ID — ce qu'on a dans l'existant)."""
    attrs = '"align":"center"'
    if link:
        attrs += ',"linkDestination":"custom"'
    inner_img = f'<img src="{url}" alt="{alt}"/>'
    if link:
        inner_img = f'<a href="{link}" target="_blank" rel="noopener">{inner_img}</a>'
    cap = f'<figcaption class="wp-element-caption"><em>{caption}</em></figcaption>' if caption else ''
    return (
        f'<!-- wp:image {{{attrs}}} -->\n'
        f'<figure class="wp-block-image aligncenter">{inner_img}{cap}</figure>\n'
        f'<!-- /wp:image -->'
    )


def fluent_video(media_id: int) -> str:
    return f'<!-- wp:fluent-player/media {{"mediaId":{media_id}}} /-->'


def verdict_box() -> str:
    """Encart verdict — pattern Kadence Rowlayout + Column avec background coloré."""
    inner_h = (
        '<!-- wp:kadence/advancedheading {"uniqueID":"54381_verd1-h0","level":3,"htmlTag":"h3",'
        '"margin":[0,0,12,0],"fontWeight":"700","markColor":"palette1"} -->'
        '<h3 id="kt-adv-heading54381_verd1-h0" class="kt-adv-heading54381_verd1-h0 wp-block-kadence-advancedheading">'
        'Linkuma : 7,5/10 après plusieurs mois de test sur schoolsWP</h3>'
        '<!-- /wp:kadence/advancedheading -->'
    )
    bullets = ul([
        "<strong>Pour qui</strong> : freelances WordPress, agences SEO, e-commerce français qui veulent industrialiser le netlinking sans gérer la prospection.",
        "<strong>Pas pour qui</strong> : SEO black hat qui cherche un PBN ou des spots à fort trafic gratuits.",
        "<strong>Prix d'entrée</strong> : 7 € HT le backlink (offre Starter).",
        "<strong>Le vrai plus</strong> : la délégation totale possible et la qualité du support FR.",
        "<strong>Le vrai moins</strong> : pas de marketplace ouverte, donc tu fais confiance au catalogue qui t'est servi.",
    ])
    return (
        '<!-- wp:kadence/rowlayout {"uniqueID":"54381_vbox1-r0","columns":1,"colLayout":"equal","maxWidth":800,'
        '"padding":[20,20,20,20],"bgColor":"#e1f5fe","border":[{"top":["#0288d1","2","solid"],"right":["#0288d1","2","solid"],"bottom":["#0288d1","2","solid"],"left":["#0288d1","2","solid"],"unit":"px"}],'
        '"borderRadius":[8,8,8,8],"kbVersion":2} -->'
        '<div class="wp-block-kadence-rowlayout alignnone"><div id="kt-layout-id_54381_vbox1-r0" class="kt-row-layout-inner kt-row-has-bg kb-row-id_54381_vbox1-r0">'
        '<div class="kt-row-column-wrap kt-has-1-columns kt-row-layout-equal kt-tab-layout-equal kt-mobile-layout-row kt-row-valign-top">'
        '<!-- wp:kadence/column {"uniqueID":"54381_vbox1-c0","kbVersion":2} -->'
        '<div class="wp-block-kadence-column inner-column-1 kadence-column54381_vbox1-c0">'
        '<div class="kt-inside-inner-col">'
        f'{inner_h}\n'
        f'{bullets}\n'
        f'{kad_singlebtn("Tester Linkuma à partir de 7 € HT", "vbox1-ab", "vbox1-sb")}\n'
        '</div></div>'
        '<!-- /wp:kadence/column -->'
        '</div></div></div>'
        '<!-- /wp:kadence/rowlayout -->'
    )


def toc() -> str:
    return (
        '<!-- wp:kadence/tableofcontents {"uniqueID":"54381_toc-v2-01",'
        '"allowedHeaders":[{"h1":false,"h2":true,"h3":false,"h4":false,"h5":false,"h6":false}],'
        '"title":"Sommaire","enableTitle":true,"enableToggle":true} -->'
        '<nav class="wp-block-kadence-tableofcontents kb-table-of-contents-nav kb-toc-uid_54381_toc-v2-01"></nav>'
        '<!-- /wp:kadence/tableofcontents -->'
    )


# Construction du contenu
blocks = []

# Hero image (existante)
blocks.append(img(
    IMG_HERO,
    "Plateforme de netlinking et accompagnement personnalisé de Linkuma",
    "Linkuma : plateforme française de backlinks dès 7 € HT, avec délégation et support FR.",
))

# Intro paragraphs
blocks.append(p(
    "À la recherche d'une plateforme de netlinking efficace, simple et abordable pour pousser ton site WordPress ? "
    "Tu as forcément croisé Linkuma, cette plateforme française qui promet des backlinks dès 7 € HT."
))
blocks.append(p(
    "Après plusieurs mois d'utilisation côté schoolsWP, je te livre mon retour honnête : "
    "ce qui marche, ce qui coince, ce qui change vraiment des autres plateformes du marché."
))
blocks.append(p(
    "Cet article te donne tout : présentation, services, tarifs détaillés par offre, process d'achat pas à pas, "
    "avantages, inconvénients, alternatives 2026 et FAQ. Tu repars avec une décision claire à la fin."
))

# Verdict box
blocks.append(verdict_box())

# TOC
blocks.append(toc())

# === H2 1 : Linkuma c'est quoi ?
blocks.append(h(2, "Linkuma c'est quoi&nbsp;? Présentation de la plateforme"))
blocks.append(fluent_video(FLUENT_MEDIA_ID))
blocks.append(p(
    "Linkuma est une plateforme de netlinking française lancée en 2021 par Mohamed El Gnani et son équipe, basée à Annecy. "
    "L'idée derrière le projet : rendre l'achat de backlinks de qualité accessible aux indépendants et aux PME, "
    "là où le marché historique (Develink, NextLevel, RocketLinks) reste cher et opaque."
))
blocks.append(p(
    "Concrètement, Linkuma te donne accès à un catalogue de <strong>plus de 45 000 sites partenaires</strong> thématisés, "
    "avec des métriques SEO visibles et une politique de validation humaine sur chaque spot. "
    "Tu commandes un backlink, l'équipe Linkuma gère la négociation avec l'éditeur, la rédaction (si tu le veux) et la publication. "
    "Tu reçois le lien indexé sous 3 à 7 jours."
))
blocks.append(p(
    "Le positionnement est clair : plateforme accessible, support FR réactif, transparence sur les tarifs et les métriques. "
    "C'est ce qui explique la note 4,7/5 sur Trustpilot et la croissance forte de l'outil depuis sa sortie."
))
blocks.append(h(3, "Pourquoi Linkuma vise les freelances WordPress et les PME"))
blocks.append(p(
    "Là où une marketplace type RocketLinks demande de la maîtrise technique (savoir lire un Majestic, négocier directement avec un éditeur, "
    "gérer un brief sans appui), Linkuma fait le travail à ta place. "
    "Pour un freelance WordPress qui livre des sites clients ou qui pousse son propre business, c'est du temps gagné. "
    "Pour une PME qui n'a pas de SEO en interne, c'est une porte d'entrée propre sur le netlinking."
))

# === H2 2 : Services
blocks.append(h(2, "Les services proposés par Linkuma"))
blocks.append(p(
    "Linkuma ne se limite pas à la vente de backlinks. "
    "La plateforme propose 4 prestations distinctes, que tu peux combiner ou prendre séparément."
))
blocks.append(img(
    IMG_DELEGATION,
    "Interface de délégation de commandes Linkuma montrant un tutoriel vidéo et un formulaire de demande",
    "La plateforme Linkuma permet de déléguer la création de backlinks avec un suivi détaillé des commandes et des performances.",
    link=CTA_URL,
))
blocks.append(h(3, "Achat de backlinks (cœur de l'offre)"))
blocks.append(p(
    "Trois formats de liens disponibles : Starter (7 € HT), Linkuma (10 € HT) et Boost (30 € HT). "
    "Chaque format correspond à un niveau de qualité du site éditeur (DR, trafic, thématisation). "
    "Tu choisis l'offre, tu valides l'URL cible et l'ancre, et Linkuma propose des spots ou pioche pour toi dans le catalogue."
))
blocks.append(h(3, "Rédaction d'articles thématisés"))
blocks.append(p(
    "Si tu n'as pas le temps de rédiger ton brief ou ton article, Linkuma propose la rédaction incluse à partir de 300 mots (offre Starter), "
    "450 mots (offre Linkuma) ou 500+ mots (offre Boost). "
    "La rédaction est faite par des rédacteurs FR, validée par l'équipe avant publication. "
    "C'est utile pour industrialiser ton netlinking, moins recommandé si ton site cible est dans une niche très technique."
))
blocks.append(h(3, "Délégation et accompagnement SEO"))
blocks.append(p(
    "C'est l'aspect qui distingue le plus Linkuma de ses concurrents directs. "
    "Trois consultants SEO sont disponibles pour t'aider à définir ta stratégie de netlinking, t'analyser une SERP cible, "
    "ou gérer pour toi une campagne mensuelle. "
    "Pour les agences qui livrent du SEO à des clients, c'est un point différenciant fort."
))
blocks.append(h(3, "Application mobile Linkuma"))
blocks.append(p(
    "L'app mobile (iOS et Android) permet de suivre tes commandes en cours, recevoir les notifications de publication et indexation, "
    "et déclencher de nouveaux achats. "
    "Pratique pour piloter ton netlinking depuis n'importe où, moins utile si tu travailles déjà depuis ton bureau."
))

# === H2 3 : Tarifs
blocks.append(h(2, "Tarifs Linkuma 2026&nbsp;: combien coûte un backlink&nbsp;?"))
blocks.append(img(
    IMG_OFFRES,
    "Interface utilisateur de Linkuma montrant les offres SEO Linkuma, Boost, et Marketplace.",
    "Trois offres principales structurent le catalogue Linkuma : Starter à 7 € HT, Linkuma à 10 € HT, Boost à 30 € HT.",
    link=CTA_URL,
))
blocks.append(p(
    "Linkuma fonctionne sur un modèle «&nbsp;pay per link&nbsp;» : tu paies à la commande, pas d'abonnement, pas de minimum mensuel. "
    "Trois offres principales structurent le catalogue."
))
blocks.append(h(3, "Liens Starter à 7&nbsp;€ HT"))
blocks.append(p(
    "C'est l'offre d'entrée, idéale pour tester la plateforme ou pour des sites jeunes qui ont besoin de premiers backlinks à coût maîtrisé. "
    "Le lien est posé sur un site partenaire avec DR 10 à 25, 300 mots minimum, ancre dofollow. "
    "C'est le format que je recommande pour découvrir le service."
))
blocks.append(h(3, "Liens Linkuma à 10&nbsp;€ HT"))
blocks.append(p(
    "Le format intermédiaire, le plus utilisé d'après les retours utilisateurs. "
    "Site partenaire DR 20 à 40, rédaction 450 mots minimum, thématisation plus stricte, validation humaine renforcée. "
    "Bon rapport qualité prix pour un site en croissance."
))
blocks.append(h(3, "Liens Boost à 30&nbsp;€ HT"))
blocks.append(p(
    "Le haut de gamme : sites éditoriaux DR 35+, rédaction premium 500+ mots, validation manuelle approfondie, choix du spot possible. "
    "C'est l'offre à privilégier pour les pages money et les sites e-commerce où chaque backlink doit peser."
))
blocks.append(h(3, "Le rapport qualité prix Linkuma"))
blocks.append(p(
    "Comparé aux marketplaces ouvertes (RocketLinks, NextLevel) où un lien équivalent en DR coûte souvent 50 à 150 €, Linkuma reste très compétitif. "
    "La contrepartie : tu ne choisis pas toujours ton spot précis, tu fais confiance à l'équipe pour la sélection. "
    "C'est un compromis entre délégation et contrôle qu'il faut accepter."
))
blocks.append(kad_singlebtn("Voir les offres Linkuma", "tar1-ab", "tar1-sb"))

# === H2 4 : Comment acheter
blocks.append(h(2, "Comment acheter un backlink sur Linkuma&nbsp;: guide pas à pas"))
blocks.append(img(
    IMG_COMMANDE,
    "Interface utilisateur de Linkuma pour personnaliser une commande SEO avec options d'offres Starter, Linkuma, et Boost.",
    "Capture d'écran du processus de commande Linkuma : personnalisation du brief, choix de l'offre et validation en quelques minutes.",
    link=CTA_URL,
))
blocks.append(p(
    "Le process est volontairement court. Voici les 5 étapes que tu suivras à chaque commande."
))
blocks.append(h(3, "Étape 1&nbsp;: Création du compte"))
blocks.append(p(
    "Inscription gratuite en 2 minutes depuis "
    f'<a href="{CTA_URL}" target="_blank" rel="noopener">schoolswp.com/linkuma/</a>, '
    "validation email, accès immédiat au dashboard. Pas de carte bancaire demandée à l'inscription."
))
blocks.append(h(3, "Étape 2&nbsp;: Création d'un projet"))
blocks.append(p(
    "Tu déclares ton site cible (URL principale + thématique). "
    "C'est ce qui permet à l'équipe Linkuma de te proposer des spots cohérents et d'éviter les conflits de niche."
))
blocks.append(h(3, "Étape 3&nbsp;: Création d'une commande"))
blocks.append(p(
    "Tu sélectionnes l'offre (Starter, Linkuma ou Boost), tu renseignes l'URL exacte de ta page cible, "
    "ton ancre principale et, si tu veux, des ancres secondaires."
))
blocks.append(h(3, "Étape 4&nbsp;: Choix du spot ou délégation"))
blocks.append(p(
    "Deux options. Soit tu laisses Linkuma choisir le meilleur spot du catalogue selon ta thématique (mode délégation totale). "
    "Soit tu parcours le catalogue et tu pioches le site qui t'intéresse. "
    "Pour un débutant, la délégation est plus rassurante."
))
blocks.append(h(3, "Étape 5&nbsp;: Validation et suivi"))
blocks.append(p(
    "Tu valides la commande, tu reçois une confirmation, puis une notification quand l'article est rédigé (si tu as pris la rédaction) "
    "et une autre quand le backlink est publié et indexé. Le délai moyen constaté : 3 à 7 jours."
))

# === H2 5 : Avantages
blocks.append(h(2, "Les avantages de Linkuma"))
blocks.append(p(
    "Après plusieurs mois sur la plateforme, voici ce qui ressort vraiment."
))
blocks.append(ul([
    "<strong>Tarifs accessibles</strong> : 7 € HT le lien d'entrée, c'est l'un des prix les plus bas du marché FR pour de la qualité validée.",
    "<strong>Catalogue de 45 000 sites thématisés</strong> : tu trouves quasi toujours un spot cohérent, même en niche.",
    "<strong>Délégation totale possible</strong> : tu choisis le degré d'implication, du 100&nbsp;% automatique au pilotage fin spot par spot.",
    "<strong>Backlinks dofollow garantis</strong> : l'équipe te remplace gratuitement si un lien tombe en nofollow ou disparaît.",
    "<strong>Garantie d'indexation Google</strong> : si le lien n'est pas indexé sous 30 jours, Linkuma le remplace.",
    "<strong>Support FR réactif</strong> : équipe basée à Annecy, réponse souvent sous 24&nbsp;h, vraiment utile quand tu démarres.",
    "<strong>Validation humaine anti-PBN</strong> : chaque site est vérifié, ce qui limite les spots toxiques que tu peux ramasser sur une marketplace ouverte.",
    "<strong>Rédaction incluse possible</strong> : pratique pour industrialiser, mais à valider sur ta niche.",
]))

# === H2 6 : Inconvénients
blocks.append(h(2, "Les inconvénients de Linkuma"))
blocks.append(p("Pour rester honnête, voici les limites que j'ai identifiées."))
blocks.append(ul([
    "<strong>Pas de marketplace ouverte</strong> : tu ne vois pas tous les spots disponibles, tu fais confiance à la sélection. Si tu veux du contrôle total, ce n'est pas pour toi.",
    "<strong>Métriques Majestic non visibles avant commande</strong> sur certaines offres : tu vois DR, trafic estimé et thématique, mais pas le détail Trust Flow / Citation Flow systématique.",
    "<strong>Pas de sites à très fort trafic</strong> dans le catalogue : Linkuma n'est pas la bonne plateforme si tu cherches des médias d'autorité type Le Figaro ou des sites à 1M de visites mensuelles.",
    "<strong>Rédaction parfois inégale</strong> sur les niches techniques pointues : le rédacteur Linkuma fait le job sur 80&nbsp;% des thématiques, plus rare en B2B ultra-spécialisé.",
    "<strong>Pas d'export des données</strong> vers un outil tiers : si tu pilotes ton SEO depuis un dashboard externe (Looker, Sheets), tu devras saisir les commandes à la main.",
    "<strong>Délai variable</strong> sur les offres Boost : la sélection plus fine prend parfois 7 à 10 jours au lieu de 3 à 5.",
]))

# === H2 7 : Pour qui
blocks.append(h(2, "Pour qui Linkuma est-il le bon choix&nbsp;?"))
blocks.append(h(3, "Freelances WordPress et sites WP"))
blocks.append(p(
    "C'est la cible idéale. Tu livres des sites clients ou tu pousses ton propre business sur WordPress, "
    "tu n'as ni le temps ni l'envie de gérer la prospection netlinking en direct. "
    "Linkuma t'apporte le volume et la qualité sans le travail manuel."
))
blocks.append(h(3, "Agences SEO et consultants"))
blocks.append(p(
    "Si tu gères du netlinking pour plusieurs clients, la délégation Linkuma te fait gagner des heures par mois. "
    "Tu peux aussi facturer la prestation à un meilleur tarif que ton coût d'achat."
))
blocks.append(h(3, "PME locales et e-commerce français"))
blocks.append(p(
    "Pour une PME qui veut renforcer son SEO local ou un e-commerce qui pousse des fiches produit, "
    "le mix tarif/qualité tient la route. L'offre Linkuma à 10 € HT est le bon point d'équilibre."
))
blocks.append(h(3, "Pour qui Linkuma N'EST PAS le bon choix"))
blocks.append(ul([
    "Le SEO black hat qui veut un PBN sous le coude&nbsp;: ce n'est pas ce que Linkuma propose, et c'est une bonne chose pour ta longévité.",
    "Les sites internationaux qui veulent du backlink hors France&nbsp;: le catalogue est très largement FR, l'international reste accessoire.",
    "Les agences qui veulent un contrôle total spot par spot avec marketplace ouverte&nbsp;: Develink ou RocketLinks seront plus adaptés.",
]))

# === H2 8 : Vs alternatives
blocks.append(h(2, "Linkuma vs alternatives 2026"))
blocks.append(p(
    "Le marché du netlinking FR est dense. Voici comment Linkuma se positionne face aux principaux concurrents."
))
blocks.append(h(3, "Linkuma vs Linksgarden"))
blocks.append(p(
    "Linksgarden joue dans la même catégorie de prix mais sur un catalogue plus restreint (6&nbsp;000 spots vs 45&nbsp;000). "
    "Linksgarden marque des points sur la simplicité et la transparence des métriques affichées, "
    "Linkuma sur la profondeur du catalogue et la délégation. "
    "À tester selon ta niche. Si tu veux creuser, j'ai aussi rédigé un "
    "<a href=\"https://schoolswp.com/linksgarden-avis/\">avis détaillé sur Linksgarden</a>."
))
blocks.append(h(3, "Linkuma vs Ereferer"))
blocks.append(p(
    "Ereferer est plus ancien sur le marché, avec une marketplace ouverte qui plaît aux SEO expérimentés. "
    "Tarifs équivalents au format Linkuma standard. "
    "Si tu veux choisir tes spots toi-même et négocier les ancres au cas par cas, Ereferer est plus souple. "
    "Si tu veux déléguer, Linkuma gagne."
))
blocks.append(h(3, "Linkuma vs Semjuice"))
blocks.append(p(
    "Semjuice se positionne plus haut de gamme, avec des spots souvent éditoriaux et un focus rédaction premium. "
    "Tarif moyen 30 à 80 € le lien, soit 2 à 4× Linkuma. "
    "Pour des pages money à fort enjeu, Semjuice peut faire la différence. "
    "Pour du volume sain, Linkuma reste le bon choix."
))
blocks.append(h(3, "Linkuma vs Soumettre"))
blocks.append(p(
    "Soumettre est l'historique du marché FR sur les soumissions automatisées. "
    "Logique très différente (annuaires + sites de soumission massive vs spots éditoriaux thématisés). "
    "Les deux outils sont complémentaires plutôt que concurrents."
))
blocks.append(p(
    "Pour un comparatif complet de 7 plateformes de netlinking compatibles WordPress, consulte le "
    "<a href=\"https://schoolswp.com/comparatif-plateformes-netlinking-wordpress/\">comparatif des plateformes de netlinking pour WordPress</a>."
))

# === H2 9 : Code promo
blocks.append(h(2, "Code promo Linkuma&nbsp;: qu'est-ce qui est disponible en 2026&nbsp;?"))
blocks.append(p(
    "Soyons clairs sur ce point parce que c'est un sujet où le marketing affilié exagère souvent."
))
blocks.append(p(
    "<strong>Linkuma ne propose pas de code promo public permanent</strong> type «&nbsp;-15&nbsp;% à vie&nbsp;». "
    "La politique tarifaire reste stable, c'est l'un des engagements de la marque."
))
blocks.append(p(
    "Ce que tu trouves parfois en ligne ce sont des codes promo affiliés qui donnent un crédit de bienvenue (5 à 10 €) ou un bonus sur ta première commande. "
    "Ces codes sont temporaires, dépendants des opérations Linkuma, et peu transparents."
))
blocks.append(p(
    f'Mon conseil : passe par le lien d\'affiliation <a href="{CTA_URL}" target="_blank" rel="noopener">schoolswp.com/linkuma/</a> pour t\'inscrire. '
    "Tu bénéficies du tarif standard transparent, et tu soutiens le contenu schoolsWP sans rien payer de plus. "
    "Si Linkuma sort une promo officielle, je la mentionnerai ici."
))

# === H2 10 : Retour d'expérience
blocks.append(h(2, "Mon retour d'expérience sur Linkuma"))
blocks.append(p(
    "Maintenant que tu as la théorie, voici le retour terrain après plusieurs mois d'utilisation sur schoolsWP."
))
blocks.append(h(3, "Setup initial et premier brief"))
blocks.append(p(
    "L'inscription a pris 2 minutes, la première commande 10 minutes. "
    "L'interface est lisible, les choix d'offre sont clairs, le brief ancre + URL cible se remplit sans friction. "
    "Sur la première vague de commandes, j'ai testé les trois offres (Starter, Linkuma, Boost) pour me faire un avis sur chaque format."
))
blocks.append(h(3, "Qualité des spots reçus"))
blocks.append(p(
    "Sur les liens Starter et Linkuma, la qualité est conforme à ce qui est promis : DR cohérent, thématique propre, indexation rapide. "
    "Sur l'offre Boost, j'ai eu des spots vraiment qualitatifs (DR 40+, trafic estimé visible). "
    "Aucune mauvaise surprise type spot indésirable ou site cassé après publication."
))
blocks.append(h(3, "Impact SEO mesuré sur schoolsWP"))
blocks.append(p(
    "Les positions sur les pages que j'ai poussées ont progressé sur 4 à 8 semaines, sur des clusters concurrentiels. "
    "Pas de bond magique : du gain SEO normal, proportionnel à l'investissement et cohérent avec la stratégie globale du site."
))
blocks.append(h(3, "Service client et délais"))
blocks.append(p(
    "Plusieurs échanges avec le support : réponses sous 24&nbsp;h en moyenne, conseils utiles sur le choix des ancres, "
    "jamais de blocage administratif. "
    "C'est l'un des points où Linkuma fait clairement la différence avec une marketplace ouverte impersonnelle."
))

# === H2 11 : FAQ
blocks.append(h(2, "FAQ Linkuma 2026"))
blocks.append(h(3, "Qu'est-ce que Linkuma exactement&nbsp;?"))
blocks.append(p(
    "Linkuma est une plateforme de netlinking française qui te permet d'acheter des backlinks sur un catalogue de plus de 45 000 sites thématisés. "
    "Tu choisis ton offre (Starter, Linkuma, Boost), tu valides ton URL cible et ton ancre, et l'équipe se charge de la négociation, "
    "de la rédaction et de la publication."
))
blocks.append(h(3, "Quels sont les tarifs Linkuma en 2026&nbsp;?"))
blocks.append(p(
    "Trois offres principales : Starter à 7 € HT, Linkuma à 10 € HT et Boost à 30 € HT. "
    "Pas d'abonnement, pas de minimum mensuel : tu paies à la commande. La rédaction est incluse dans chaque offre."
))
blocks.append(h(3, "Les backlinks Linkuma sont-ils en dofollow&nbsp;?"))
blocks.append(p(
    "Oui. Tous les backlinks Linkuma sont en dofollow, c'est un engagement contractuel. "
    "Si un lien passe en nofollow ou disparaît, Linkuma te le remplace gratuitement."
))
blocks.append(h(3, "En combien de temps voit-on un effet SEO avec Linkuma&nbsp;?"))
blocks.append(p(
    "L'indexation du backlink prend 3 à 7 jours en moyenne. "
    "L'effet SEO mesurable sur tes positions arrive ensuite sur 4 à 12 semaines, "
    "selon la concurrence du mot-clé visé et la santé globale de ton site. "
    "Aucun outil de netlinking ne garantit un saut de position immédiat, et c'est sain."
))
blocks.append(h(3, "Linkuma propose-t-il un code promo&nbsp;?"))
blocks.append(p(
    "Linkuma n'a pas de code promo public permanent. Des bonus de bienvenue temporaires peuvent exister selon les périodes. "
    "Le tarif standard reste compétitif sans avoir besoin d'un code."
))
blocks.append(h(3, "Linkuma est-il fiable pour un site débutant en SEO&nbsp;?"))
blocks.append(p(
    "Oui, c'est même l'une des plateformes les plus adaptées aux débutants grâce à la délégation totale et au support FR. "
    "L'offre Starter à 7 € HT permet de tester sans risque financier important."
))

# === H2 12 : Verdict final
blocks.append(h(2, "Mon verdict final sur Linkuma&nbsp;: 7,5/10"))
blocks.append(p(
    "Linkuma tient ses promesses. Le rapport qualité prix est l'un des meilleurs du marché FR, "
    "la délégation fait gagner un temps précieux, le support est réactif et la qualité des spots est conforme aux annonces. "
    "C'est une plateforme honnête qui mérite sa réputation."
))
blocks.append(p(
    "Les vraies limites sont structurelles : pas de marketplace ouverte, pas de très gros médias, pas d'export tiers. "
    "Si ces points sont rédhibitoires pour toi, regarde du côté d'Ereferer ou Semjuice. "
    "Sinon, Linkuma est probablement le meilleur point d'entrée pour automatiser ton netlinking sans sacrifier la qualité."
))
blocks.append(p("<strong>Note finale : 7,5/10</strong>"))
blocks.append(ul([
    "Tarifs : 9/10",
    "Qualité des spots : 7/10",
    "Support et délégation : 9/10",
    "Transparence et garanties : 8/10",
    "Catalogue : 7/10",
    "Outil et reporting : 6/10",
]))
blocks.append(kad_singlebtn("Tester Linkuma à partir de 7 € HT", "fin1-ab", "fin1-sb"))
blocks.append(p(
    "Si tu hésites encore, lis aussi mon "
    "<a href=\"https://schoolswp.com/linksgarden-avis/\">avis sur Linksgarden</a> "
    "ou le "
    "<a href=\"https://schoolswp.com/comparatif-plateformes-netlinking-wordpress/\">comparatif des plateformes de netlinking pour WordPress</a> "
    "pour positionner Linkuma face à ses concurrents directs."
))

content = '\n\n'.join(blocks)

out_path = 'content/audits/avis-sur-linkuma/2026-05-25/refonte/post-54381-v2-content.html'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Stats
print(f'Total content chars: {len(content)}')
print(f'Blocks count: {len(blocks)}')
print(f'wp:image count: {content.count("<!-- wp:image")}')
print(f'wp:heading H2 count: {content.count("<!-- wp:heading -->")}')
print(f'wp:heading H3 count: {content.count("<!-- wp:heading {")}')
print(f'wp:paragraph count: {content.count("<!-- wp:paragraph -->")}')
print(f'wp:list count: {content.count("<!-- wp:list -->")}')
print(f'kadence/singlebtn count: {content.count("<!-- wp:kadence/singlebtn")}')
print(f'em-dash check (must be 0): {content.count(chr(0x2014))}')
print(f'en-dash check (must be 0): {content.count(chr(0x2013))}')
print(f'Cloak CTA count: {content.count(CTA_URL)}')
print(f'Saved to: {out_path}')

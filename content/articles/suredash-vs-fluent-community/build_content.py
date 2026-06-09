#!/usr/bin/env python
"""Assemble le post_content Gutenberg/Kadence de la refonte SureDash vs Fluent Community
(post 2969375) et l'encode en base64 pour push direct via Novamira ($wpdb->update).

Reutilise les coquilles Kadence du brouillon (encadre intro, TOC, FAQ accordeon),
ajoute le corps en blocs core, le tableau Ninja Tables (2974047) et 2 CTA verts.
Tutoiement, prix verifies, sans code promo. B2/B3/B4/B7 corriges.
"""

import base64
import pathlib
import re

HERE = pathlib.Path(__file__).parent
NINJA_ID = 2974047


# ---------- helpers blocs core ----------
def h2(t):
    return f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{t}</h2>\n<!-- /wp:heading -->'


def h3(t):
    return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->'


def p(t):
    return f"<!-- wp:paragraph -->\n<p>{t}</p>\n<!-- /wp:paragraph -->"


def ul(items):
    lis = "\n\n".join(f"<!-- wp:list-item -->\n<li>{it}</li>\n<!-- /wp:list-item -->" for it in items)
    return f'<!-- wp:list -->\n<ul class="wp-block-list">{lis}</ul>\n<!-- /wp:list -->'


def ninja(table_id):
    return f'<!-- wp:shortcode -->\n[ninja_tables id="{table_id}"]\n<!-- /wp:shortcode -->'


def cta(uid, text, link):
    # CSS var dashes encodes en -- : un "--" litteral dans un commentaire de bloc
    # <!-- ... --> est invalide en HTML et casse le parsing Kadence (cf. memoire u002d).
    grad = "linear-gradient(135deg,var(\\u002d\\u002dglobal-palette1,#00d400) 0%,var(\\u002d\\u002dglobal-palette2,#00a100) 100%)"
    gradh = "linear-gradient(135deg,var(\\u002d\\u002dglobal-palette2,#00a100) 0%,var(\\u002d\\u002dglobal-palette1,#00d400) 100%)"
    btn = (
        '{"uniqueID":"2969375_%sb","text":"%s","link":"%s","target":"_blank","noFollow":true,"sponsored":true,'
        '"widthType":"full","color":"palette9","gradient":"%s","backgroundType":"gradient",'
        '"backgroundHoverType":"gradient","gradientHover":"%s","icon":"fas_arrow-right",'
        '"typography":[{"weight":"bold"}]}'
    ) % (uid, text, link, grad, gradh)
    return (
        f'<!-- wp:kadence/advancedbtn {{"uniqueID":"2969375_{uid}a","margin":[{{"desk":["","",3,""]}}]}} -->\n'
        f'<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btns2969375_{uid}a">'
        f"<!-- wp:kadence/singlebtn {btn} /--></div>\n"
        f"<!-- /wp:kadence/advancedbtn -->"
    )


# ---------- encadre "L'essentiel a retenir" (coquille Kadence du brouillon, texte remplace) ----------
ESSENTIEL_TEXT = (
    "Si tu hésites entre <strong>SureDash</strong> et <strong>Fluent Community</strong>, la vraie question "
    "n'est pas « lequel est le meilleur » mais « dans quel écosystème tu veux t'installer ». "
    "SureDash (Brainstorm Force, les créateurs d'Astra et SureCart) se marie nativement avec SureCart et SureMembers. "
    "Fluent Community (WPManageNinja, l'éditeur de FluentCRM) mise sur une interface ultra-rapide et l'automatisation "
    "via FluentCRM. <strong>Les deux ont une version gratuite, un LMS intégré et un tarif d'entrée raisonnable.</strong> "
    "Ton choix dépend surtout des plugins que tu utilises déjà."
)

ENCADRE = (
    """<!-- wp:kadence/rowlayout {"uniqueID":"2969375_0c281e-b0","columns":1,"colLayout":"equal","maxWidth":800,"paddingUnit":"rem","padding":["xs","","md",""],"kbVersion":2} -->
<!-- wp:kadence/column {"background":"#f3faf7","borderWidth":["","","",""],"uniqueID":"2969375_3ca11d-93","displayShadow":true,"shadow":[{"color":"#000000","opacity":0.5,"spread":-10,"blur":25,"hOffset":0,"vOffset":14,"inset":false}],"direction":["vertical","",""],"verticalAlignment":"middle","padding":[40,40,40,40],"borderStyle":[{"top":["#00bf88","",2],"right":["#00bf88","",2],"bottom":["#00bf88","",2],"left":["#00bf88","",2],"unit":"px"}],"kbVersion":2,"className":"inner-column-1"} -->
<div class="wp-block-kadence-column kadence-column2969375_3ca11d-93 kb-section-dir-vertical inner-column-1"><div class="kt-inside-inner-col"><!-- wp:kadence/column {"borderWidth":["","","",""],"uniqueID":"2969375_46f58e-d1","kbVersion":2,"className":"inner-column-1"} -->
<div class="wp-block-kadence-column kadence-column2969375_46f58e-d1 inner-column-1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"2969375_b98634-69","margin":[-55,"","",-52],"markSize":["md","",""],"markFontWeight":"bold","markColor":"palette9","markBG":"#00bf88","markPadding":[5,8,5,8],"markTextTransform":"uppercase","htmlTag":"span","className":"our-pick-arrow"} -->
<span class="kt-adv-heading2969375_b98634-69 our-pick-arrow wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2969375_b98634-69"><mark class="kt-highlight">L'essentiel à retenir</mark></span>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"borderWidth":["","","",""],"uniqueID":"2969375_d1c7e3-29","verticalAlignment":"middle","kbVersion":2,"className":"inner-column-1"} -->
<div class="wp-block-kadence-column kadence-column2969375_d1c7e3-29 inner-column-1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"2969375_3a23e6-01","margin":[0,0,0,0],"padding":[0,"","",""],"htmlTag":"p","fontSize":["md","",""]} -->
<p class="kt-adv-heading2969375_3a23e6-01 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2969375_3a23e6-01">"""
    + ESSENTIEL_TEXT
    + """</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/column --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->"""
)

TOC = '<!-- wp:kadence/tableofcontents {"uniqueID":"2969375_87a534-d3","allowedHeaders":[{"h1":false,"h2":true,"h3":false,"h4":false,"h5":false,"h6":false}],"linkStyle":"underline_hover","containerBackground":"palette9","title":"Sommaire de l\'article","titleColor":"palette3","titleFontWeight":"bold","titleTextTransform":"uppercase","enableToggle":true,"toggleIcon":"arrowcircle","contentColor":"palette1","contentHoverColor":"palette2","maxWidth":500,"displayShadow":true,"shadow":[{"color":"#000000","opacity":0.5,"spread":-10,"blur":25,"hOffset":0,"vOffset":14,"inset":false}],"enableSmoothScroll":true,"borderStyle":[{"top":["palette3","",2],"right":["palette3","",2],"bottom":["palette3","",2],"left":["palette3","",2],"unit":"px"}],"enableTitleToggle":true} /-->'

# ---------- FAQ accordeon (FR, 6 Q/R, schema FAQPage gere via Rank Math) ----------
FAQ = [
    (
        "SureDash ou Fluent Community : lequel choisir ?",
        "Ça dépend de ton écosystème. Si tu utilises déjà SureCart ou SureMembers, SureDash s'intègre naturellement. Si tu carbures à FluentCRM, Fluent Community sera plus cohérent. Les deux font très bien le travail de base : forums, cours, gamification.",
    ),
    (
        "Lequel est le plus rapide ?",
        "Fluent Community est conçu comme une application web ultra-réactive, avec une navigation sans rechargement et une app mobile dédiée. Si la fluidité de l'interface est ta priorité, il a une longueur d'avance. SureDash reste léger et propose un mode « Application », mais sans app native.",
    ),
    (
        "Faut-il déjà avoir SureCart pour utiliser SureDash ?",
        "Non, SureDash fonctionne seul et propose une version gratuite. Mais il prend tout son sens couplé à SureCart (pour vendre) et SureMembers (pour protéger l'accès), puisqu'il est pensé pour l'écosystème Sure de Brainstorm Force.",
    ),
    (
        "Peut-on utiliser Fluent Community sans FluentCRM ?",
        "Oui, Fluent Community marche de façon autonome. Mais son intégration avec FluentCRM est son meilleur atout : elle te permet de déclencher des emails et des automatisations selon le comportement de tes membres. Sans la suite Fluent, tu perds une partie de sa valeur.",
    ),
    (
        "Y a-t-il une application mobile ?",
        "Fluent Community propose une application mobile dédiée (Android et iOS), un vrai plus pour la rétention. SureDash mise sur un design responsive et un agencement « Application », mais sans app native à ce jour.",
    ),
    (
        "Lequel est le mieux pour vendre des formations en ligne ?",
        "Les deux intègrent un LMS. SureDash, couplé à SureCart, offre un tunnel de vente et une gestion des membres très complète pour monétiser des cours. Fluent Community propose aussi cours et leçons, mais son coeur reste la discussion communautaire. Pour un projet 100 % formation avec monétisation avancée, l'écosystème Sure est souvent plus complet.",
    ),
]


def pane(uid, idx, q, a):
    return (
        f'<!-- wp:kadence/pane {{"id":{idx},"uniqueID":"2969375_{uid}"}} -->\n'
        f'<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-{idx} kt-pane2969375_{uid}">'
        f'<div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button">'
        f'<span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">{q}</span></span>'
        f'<span class="kt-blocks-accordion-icon-trigger"></span></button></div>'
        f'<div class="kt-accordion-panel"><div class="kt-accordion-panel-inner">'
        f"<!-- wp:paragraph -->\n<p>{a}</p>\n<!-- /wp:paragraph --></div></div></div>\n"
        f"<!-- /wp:kadence/pane -->"
    )


def accordion(acc_uid, panes_html, pane_count):
    title_style = '[{"size":["md","",""],"sizeType":"em","lineHeight":[1.2,"",""],"padding":[14,16,14,16],"marginTop":10,"color":"palette3","background":"palette7","colorHover":"palette9","backgroundHover":"palette1","colorActive":"palette9","backgroundActive":"palette1"}]'
    return (
        f'<!-- wp:kadence/accordion {{"uniqueID":"2969375_{acc_uid}","paneCount":{pane_count},"startCollapsed":true,"linkPaneCollapse":false,"contentBgColor":"#ffffff","titleStyles":{title_style},"titleBorderRadius":[5,5,5,5],"iconStyle":"arrow","iconSide":"left"}} -->\n'
        f'<div class="wp-block-kadence-accordion alignnone"><div class="kt-accordion-wrap kt-accordion-id2969375_{acc_uid} kt-accordion-has-{pane_count}-panes kt-active-pane-0 kt-accordion-block kt-pane-header-alignment-left kt-accodion-icon-style-arrow kt-accodion-icon-side-left" style="max-width:none"><div class="kt-accordion-inner-wrap" data-allow-multiple-open="true" data-start-open="none">{panes_html}</div></div></div>\n'
        f"<!-- /wp:kadence/accordion -->"
    )


# colonne gauche = 3 premieres, droite = 3 dernieres
left_panes = "\n\n".join(pane(f"faq{i}-l", i + 1, q, a) for i, (q, a) in enumerate(FAQ[:3]))
right_panes = "\n\n".join(pane(f"faq{i}-r", i + 1, q, a) for i, (q, a) in enumerate(FAQ[3:]))

FAQ_BLOCK = (
    """<!-- wp:kadence/rowlayout {"uniqueID":"2969375_25b8eb-a4","columns":1,"colLayout":"equal","paddingUnit":"rem","inheritMaxWidth":true,"padding":["xxl","","xxl",""],"kbVersion":2} -->
<!-- wp:kadence/column {"borderWidth":["","","",""],"uniqueID":"2969375_868337-58","kbVersion":2,"className":"inner-column-1"} -->
<div class="wp-block-kadence-column kadence-column2969375_868337-58 inner-column-1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"2969375_358d54-01","sizeType":"rem","fontWeight":"800","margin":["","","xxs",""],"fontSize":["xl","",null],"fontHeight":[1.2,"",""]} -->
<h2 class="kt-adv-heading2969375_358d54-01 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2969375_358d54-01">Tes questions, mes réponses</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"2969375_dccf84-59","margin":["","","md",""],"marginType":"em","htmlTag":"p","fontSize":["md","",""]} -->
<p class="kt-adv-heading2969375_dccf84-59 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2969375_dccf84-59">Les questions qu'on se pose le plus souvent avant de choisir entre SureDash et Fluent Community.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/rowlayout {"uniqueID":"2969375_4b106b-92","collapseGutter":"custom","customRowGutter":[10,"",""],"colLayout":"equal","padding":[0,"",0,""],"kbVersion":2} -->
<!-- wp:kadence/column {"borderWidth":["","","",""],"uniqueID":"2969375_77eb70-93","kbVersion":2,"className":"inner-column-1"} -->
<div class="wp-block-kadence-column kadence-column2969375_77eb70-93 inner-column-1"><div class="kt-inside-inner-col">"""
    + accordion("b8d6c0-54", left_panes, 3)
    + """</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"borderWidth":["","","",""],"uniqueID":"2969375_a05101-18","kbVersion":2,"className":"inner-column-2"} -->
<div class="wp-block-kadence-column kadence-column2969375_a05101-18 inner-column-2"><div class="kt-inside-inner-col">"""
    + accordion("e3b697-d1", right_panes, 3)
    + """</div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->"""
)

# ---------- corps ----------
parts = []
parts.append(ENCADRE)
parts.append(
    p(
        "Créer une communauté ou un espace membre sur WordPress n'a jamais été aussi simple, et deux nouveaux venus se disputent l'attention : SureDash et Fluent Community. Tous les deux promettent de remplacer des solutions lourdes comme BuddyBoss ou des SaaS fermés comme Circle, Skool ou Mighty Networks, sans quitter ton tableau de bord WordPress."
    )
)
parts.append(
    p(
        "Le souci, c'est qu'ils se ressemblent sur le papier (forums, cours, gamification, app mobile) tout en venant de deux écuries opposées. Dans ce comparatif, on regarde ce qui les distingue vraiment : l'écosystème, les fonctionnalités au quotidien, les performances, les tarifs réels et surtout le profil pour lequel chacun est taillé. On fait le point ensemble."
    )
)
parts.append(TOC)

parts.append(h2("SureDash vs Fluent Community en un coup d'oeil"))
parts.append(
    p(
        "Avant d'entrer dans le détail, voici les différences qui comptent. Retiens surtout une chose : <strong>SureDash et Fluent Community ne s'adressent pas exactement au même profil</strong>. Le premier est pensé pour ceux qui vivent déjà dans l'écosystème Sure (Astra, SureCart, SureMembers). Le second pour ceux qui carburent à la suite Fluent, FluentCRM en tête."
    )
)
parts.append(ninja(NINJA_ID))

parts.append(h2("Fluent Community : la communauté pensée comme une application"))
parts.append(
    p(
        "Fluent Community vient de WPManageNinja, l'éditeur derrière FluentCRM, Fluent Forms et Fluent Support. Son parti pris : offrir une expérience proche d'une application web moderne, fluide et rapide, directement sur ton WordPress."
    )
)
parts.append(p("<strong>Ses points forts :</strong>"))
parts.append(
    ul(
        [
            "Un <strong>flux d'activité dynamique</strong> façon réseau social : tes membres postent, réagissent et échangent en temps réel. C'est l'ADN du produit.",
            "Des <strong>espaces privés</strong> pour segmenter ta communauté en groupes, cohortes ou ateliers fermés.",
            "Une <strong>intégration native avec FluentCRM</strong> : tu déclenches emails et automatisations selon le comportement de tes membres. C'est là que Fluent Community prend tout son sens.",
            "Un <strong>LMS intégré</strong> pour publier cours et leçons sans plugin tiers, plus de la gamification (badges, points, classement).",
            "Une <strong>app mobile</strong> dédiée (Android et iOS), un vrai atout pour la rétention.",
        ]
    )
)
parts.append(
    p(
        "<strong>Ses limites :</strong> c'est un produit jeune, dont la feuille de route bouge vite. Et son intérêt est maximal quand tu es déjà investi dans la suite Fluent ; isolé, il perd une partie de sa force."
    )
)
parts.append(
    p(
        'Pour aller plus loin, lis notre <a href="https://schoolswp.com/fluentcommunity-avis/" target="_blank" rel="noreferrer noopener">avis complet sur FluentCommunity</a>.'
    )
)
parts.append(cta("ctaF", "Tester Fluent Community", "https://schoolswp.com/fluentcommunity/"))

parts.append(h2("SureDash : la communauté intégrée à l'écosystème Sure"))
parts.append(
    p(
        "SureDash est édité par Brainstorm Force, la société derrière le thème Astra, SureCart, SureMembers ou encore SureForms. Son pari : devenir le centre communautaire de l'écosystème Sure, en s'appuyant sur des briques que beaucoup de créateurs utilisent déjà."
    )
)
parts.append(p("<strong>Ses points forts :</strong>"))
parts.append(
    ul(
        [
            "Une <strong>intégration profonde avec SureCart</strong> pour vendre tes accès, abonnements et formations sans bricolage, et avec <strong>SureMembers</strong> pour protéger finement tes contenus.",
            "Un <strong>constructeur de cours structuré</strong> avec suivi de progression et bibliothèque de ressources centralisée, adossé à la médiathèque native de WordPress.",
            "Plusieurs <strong>agencements d'interface</strong> (Classique, Moderne, Application) pour coller à ton style sans toucher au code.",
            "La <strong>gestion des événements</strong> et une promesse forte de Brainstorm Force : la maîtrise totale de tes données, en auto-hébergé.",
        ]
    )
)
parts.append(
    p(
        "<strong>Ses limites :</strong> SureDash est encore en train de mûrir, et certaines fonctionnalités avancées arrivent progressivement. Son intérêt grimpe nettement si tu possèdes déjà SureCart : sinon, tu paies pour une synergie que tu n'exploites pas."
    )
)
parts.append(
    p(
        'Si la vente fait partie de l\'équation, regarde notre article sur <a href="https://schoolswp.com/surecart-le-plugin-qui-concurrence-woocommerce/" target="_blank" rel="noreferrer noopener">SureCart</a> et le comparatif <a href="https://schoolswp.com/suremembers-comparatif-restrict-content-pro/" target="_blank" rel="noreferrer noopener">SureMembers vs Restrict Content Pro</a>.'
    )
)
parts.append(cta("ctaS", "Découvrir SureDash", "https://suredash.com/"))

parts.append(h2("Écosystème : le vrai critère de décision"))
parts.append(
    p(
        "C'est ici que tout se joue. SureDash et Fluent Community sont deux excellents produits, mais ils tirent leur puissance de leur famille respective."
    )
)
parts.append(
    ul(
        [
            "Si ta boutique tourne déjà sous <strong>SureCart</strong>, si tu protèges tes contenus avec <strong>SureMembers</strong> et si tu utilises le thème <strong>Astra</strong>, alors SureDash s'emboîte naturellement. Tu restes dans un univers cohérent, avec un seul interlocuteur.",
            "Si tu envoies tes emails avec <strong>FluentCRM</strong>, si tu collectes via <strong>Fluent Forms</strong> et que tu gères ton support avec <strong>Fluent Support</strong>, alors Fluent Community parle déjà la même langue que tes outils. L'automatisation comportementale devient redoutable.",
        ]
    )
)
parts.append(
    p(
        "Autrement dit, ne choisis pas le plugin communauté en premier : choisis l'écosystème dans lequel tu veux investir sur le long terme, puis prends la solution communautaire qui va avec."
    )
)

parts.append(h2("Performances, interface et app mobile"))
parts.append(
    p(
        "Côté ressenti, Fluent Community met l'accent sur la vitesse : la navigation est instantanée, sans rechargement de page, ce qui rapproche l'expérience d'une vraie application. Son app mobile dédiée renforce cet effet et aide à faire revenir les membres."
    )
)
parts.append(
    p(
        "SureDash propose de son côté plusieurs agencements (dont un mode « Application ») et un design responsive soigné, avec l'objectif de rester fidèle aux standards de WordPress. Pas d'app native dédiée à ce jour, mais une expérience web propre sur mobile."
    )
)
parts.append(
    p(
        'Sur la performance brute, les deux sont conçus pour être légers comparés aux poids lourds historiques type <a href="https://schoolswp.com/tout-ce-que-vous-devez-savoir-sur-buddyboss/" target="_blank" rel="noreferrer noopener">BuddyBoss</a> (qui s\'appuie souvent sur des intégrations LMS tierces). Si la fluidité de l\'interface est ta priorité absolue, Fluent Community a une longueur d\'avance. Si tu veux un socle qui respecte les habitudes WordPress et l\'écosystème Sure, SureDash tient la route.'
    )
)

parts.append(h2("Tarifs : combien coûtent SureDash et Fluent Community ?"))
parts.append(
    p(
        "Les deux plugins ont une <strong>version gratuite</strong> pour tester, puis des licences payantes. Voici les tarifs constatés (annuels, hors promotions de lancement) :"
    )
)
parts.append(h3("Fluent Community"))
parts.append(
    ul(
        [
            "1 site : 159 $/an",
            "5 sites : 319 $/an",
            "15 sites : 519 $/an",
            "Lifetime : à partir de 399 $ (1 site)",
        ]
    )
)
parts.append(h3("SureDash"))
parts.append(
    ul(
        [
            "1 site : 69 $/an (Starter)",
            "10 sites : 149 $/an (Pro)",
            "100 sites : 199 $/an (Business)",
            "Lifetime : 499 $ (100 sites)",
        ]
    )
)
parts.append(
    p(
        "À la lecture, SureDash est plus agressif sur le prix au site, surtout si tu gères plusieurs sites ou une agence (100 sites pour 199 $/an, c'est imbattable). Fluent Community se paie plus cher, mais tu paies aussi pour son intégration FluentCRM et son app mobile. Pense à vérifier les extensions nécessaires selon ton projet (par exemple SureMembers côté SureDash pour une protection granulaire), qui peuvent s'ajouter à la facture."
    )
)

parts.append(h2("Verdict : pour qui SureDash, pour qui Fluent Community ?"))
parts.append(p("<strong>Choisis Fluent Community si :</strong>"))
parts.append(
    ul(
        [
            "tu veux l'expérience la plus proche d'une application moderne (vitesse, app mobile) ;",
            "tu utilises déjà FluentCRM et tu veux automatiser l'engagement de tes membres ;",
            "l'animation et la discussion sont au coeur de ton projet.",
        ]
    )
)
parts.append(p("<strong>Choisis SureDash si :</strong>"))
parts.append(
    ul(
        [
            "tu possèdes déjà SureCart et/ou SureMembers et tu veux tout garder cohérent ;",
            "tu gères plusieurs sites et le prix au site compte (le palier 100 sites est très compétitif) ;",
            "tu veux un socle communautaire qui respecte l'écosystème Sure et la philosophie WordPress.",
        ]
    )
)
parts.append(
    p(
        "Et si tu hésites encore, garde en tête que les deux ont une version gratuite : rien ne t'empêche de tester chacun sur un site de démonstration avant de trancher. Ton objectif final reste le même : transformer ton audience en communauté active, sans dépendre d'un SaaS fermé."
    )
)

parts.append(h2("SureDash et Fluent Community ne te conviennent pas ? Les alternatives"))
parts.append(
    p(
        "Ces deux plugins ne sont pas seuls sur le marché de la communauté WordPress. Selon ton besoin, d'autres options méritent un coup d'oeil avant de te décider."
    )
)
parts.append(
    ul(
        [
            "<strong>BuddyBoss</strong> et son socle gratuit <strong>BuddyPress</strong> : la référence historique, très complète mais plus lourde, et souvent couplée à un LMS tiers comme LearnDash.",
            "<strong>Circle</strong>, <strong>Skool</strong> et <strong>Mighty Networks</strong> : des SaaS communautaires clés en main, agréables à utiliser, mais fermés et sans la maîtrise de tes données que t'offre WordPress.",
            "<strong>MemberPress</strong> : plutôt orienté adhésion et vente de contenu que communauté pure, mais pertinent si la monétisation prime sur la discussion.",
        ]
    )
)
parts.append(
    p(
        "L'avantage commun de SureDash et Fluent Community reste le même face à ces options : tout vit sur ton WordPress, sans abonnement SaaS ni dépendance externe. Tu gardes la main sur tes membres, tes contenus et tes données."
    )
)

parts.append(FAQ_BLOCK)

content = "\n\n".join(parts)

# ---------- sortie ----------
(HERE / "post_content.html").write_text(content, encoding="utf-8")
b64 = base64.b64encode(content.encode("utf-8")).decode("ascii")
(HERE / "post_content.b64").write_text(b64, encoding="ascii")

# stats + garde-fous (expressions sorties de l'f-string pour compat py3.11)
text_only = re.sub(r"<[^>]+>", " ", re.sub(r"<!--.*?-->", " ", content, flags=re.S))
words = len(text_only.split())
low = content.lower()
ninja_ok = "[ninja_tables id=" in content
vous = len(re.findall(r"\bvous\b", low))
votre = low.count("votre")
em = chr(0x2014) in content
en = chr(0x2013) in content
promo = "schoolswp20" in low
literal_var = "var(--" in content
escaped_var = (chr(92) + "u002d") in content
bad = [m.group(1) for m in re.finditer(r"<!--(.*?)-->", content, flags=re.S) if "--" in m.group(1)]
print(f"content bytes: {len(content.encode('utf-8'))}")
print(f"b64 bytes: {len(b64)}")
print(f"approx words (texte visible): {words}")
print(f"ninja shortcode present: {ninja_ok}")
print(f"em-dash: {em} | en-dash: {en}")
print(f"votre (0): {votre} | vous (0): {vous}")
print(f"promo schoolsWP20 (False): {promo}")
print(f"literal var(-- (False): {literal_var}")
print(f"escaped var (True): {escaped_var}")
print(f"commentaires avec -- interne (0): {len(bad)}")

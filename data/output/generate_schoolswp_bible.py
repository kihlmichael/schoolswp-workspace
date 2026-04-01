"""
Generate schoolsWP Bible PDF — everything about schoolsWP in one document.
"""

import os

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# --- Colors ---
PRIMARY = HexColor("#00D400")
SECONDARY = HexColor("#00A100")
ACCENT = HexColor("#E668D4")
DARKEST = HexColor("#12111F")
DARK_BG = HexColor("#1A1928")
LIGHT_BG = HexColor("#FAFBFD")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#E0E0E0")
TABLE_HEADER_BG = HexColor("#12111F")
TABLE_ALT_ROW = HexColor("#F5F5F5")

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "schoolsWP-bible.pdf")


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            fontSize=36,
            leading=42,
            textColor=DARKEST,
            alignment=TA_CENTER,
            spaceAfter=10,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            fontSize=16,
            leading=22,
            textColor=GRAY,
            alignment=TA_CENTER,
            spaceAfter=6,
            fontName="Helvetica",
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverTagline",
            fontSize=13,
            leading=18,
            textColor=SECONDARY,
            alignment=TA_CENTER,
            spaceAfter=4,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1",
            fontSize=24,
            leading=30,
            textColor=DARKEST,
            spaceBefore=24,
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2",
            fontSize=18,
            leading=24,
            textColor=SECONDARY,
            spaceBefore=18,
            spaceAfter=8,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="H3",
            fontSize=14,
            leading=18,
            textColor=DARKEST,
            spaceBefore=12,
            spaceAfter=6,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontSize=10,
            leading=15,
            textColor=DARKEST,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
            fontName="Helvetica",
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyBold",
            fontSize=10,
            leading=15,
            textColor=DARKEST,
            alignment=TA_LEFT,
            spaceAfter=6,
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletSWP",
            fontSize=10,
            leading=15,
            textColor=DARKEST,
            leftIndent=20,
            bulletIndent=8,
            spaceAfter=3,
            fontName="Helvetica",
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallNote",
            fontSize=8,
            leading=11,
            textColor=GRAY,
            alignment=TA_CENTER,
            spaceAfter=4,
            fontName="Helvetica-Oblique",
        )
    )
    styles.add(
        ParagraphStyle(
            name="TOCEntry",
            fontSize=11,
            leading=18,
            textColor=DARKEST,
            leftIndent=10,
            fontName="Helvetica",
        )
    )
    styles.add(
        ParagraphStyle(
            name="TOCSection",
            fontSize=12,
            leading=20,
            textColor=SECONDARY,
            fontName="Helvetica-Bold",
            spaceBefore=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Quote",
            fontSize=11,
            leading=16,
            textColor=SECONDARY,
            leftIndent=30,
            rightIndent=30,
            spaceBefore=8,
            spaceAfter=8,
            fontName="Helvetica-Oblique",
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            fontSize=9,
            leading=13,
            textColor=DARKEST,
            leftIndent=15,
            spaceAfter=6,
            fontName="Courier",
            backColor=HexColor("#F0F0F0"),
        )
    )
    return styles


def hr():
    return HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceBefore=8, spaceAfter=8)


def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 13),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_ROW))
    t.setStyle(TableStyle(style_cmds))
    return t


def bullet_list(items, styles):
    return [Paragraph(f"<bullet>&bull;</bullet> {item}", styles["BulletSWP"]) for item in items]


def build_pdf():
    styles = build_styles()

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="schoolsWP Bible",
        author="Michael KIHL",
        subject="Tout ce que tu dois savoir sur schoolsWP",
    )

    story = []
    W = A4[0] - 4 * cm  # available width

    # ============================================================
    # COVER PAGE
    # ============================================================
    story.append(Spacer(1, 6 * cm))
    story.append(Paragraph("schoolsWP", styles["CoverTitle"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("La Bible", styles["CoverSubtitle"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("WordPress. Clair. Structure. Utile.", styles["CoverTagline"]))
    story.append(Spacer(1, 2 * cm))
    story.append(Paragraph("Tout ce que tu dois savoir sur schoolsWP :", styles["SmallNote"]))
    story.append(Paragraph("methode, stack, agents, SEO, branding, formations, projets.", styles["SmallNote"]))
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("Michael KIHL - contact@michaelkihl.fr", styles["SmallNote"]))
    story.append(Paragraph("Version 1.0 - 31 mars 2026", styles["SmallNote"]))
    story.append(PageBreak())

    # ============================================================
    # TABLE OF CONTENTS
    # ============================================================
    story.append(Paragraph("Sommaire", styles["H1"]))
    story.append(hr())
    toc_items = [
        ("1", "Identite et positionnement"),
        ("2", "Branding et regles editoriales"),
        ("3", "La methode schoolsWP (6 frameworks)"),
        ("4", "Auto-Router : les 6 modes operationnels"),
        ("5", "Stack technique officielle"),
        ("6", "Architecture SEO"),
        ("7", "SEO Engine : la philosophie"),
        ("8", "Content Engine : production et transformation"),
        ("9", "Authority Engine : construction d'autorite"),
        ("10", "GSC Radar : detecter les opportunites"),
        ("11", "SEO Ops Brain : schema + scoring"),
        ("12", "SEO Agent : automatisation n8n"),
        ("13", "Plan strategique 24 mois"),
        ("14", "Agents Python (28 modules)"),
        ("15", "Pipelines de production"),
        ("16", "Formations en cours"),
        ("17", "Projets actifs et automatisations"),
        ("18", "Domaines et infrastructure"),
    ]
    for num, title in toc_items:
        story.append(Paragraph(f"<b>{num}.</b>  {title}", styles["TOCEntry"]))
    story.append(PageBreak())

    # ============================================================
    # 1. IDENTITE ET POSITIONNEMENT
    # ============================================================
    story.append(Paragraph("1. Identite et positionnement", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "<b>schoolsWP</b> est un ecosysteme WordPress francophone fonde par Michael KIHL. "
            "Il enseigne WordPress comme un outil strategique au service des createurs, pas comme une fin en soi.",
            styles["Body"],
        )
    )
    story.append(Paragraph("Tagline officielle", styles["H3"]))
    story.append(Paragraph('<i>"WordPress. Clair. Structure. Utile."</i>', styles["Quote"]))
    story.append(Paragraph("Positionnement", styles["H3"]))
    story.extend(
        bullet_list(
            [
                "WordPress peut travailler pour toi, pas l'inverse.",
                "Tu n'as pas besoin d'etre developpeur pour avoir un site performant.",
                "La clarte bat toujours la complexite.",
                "Un bon site se juge a ses resultats, pas a son design.",
                "Automatiser, c'est se liberer du temps pour ce qui compte.",
            ],
            styles,
        )
    )
    story.append(Paragraph("Ecosysteme", styles["H3"]))
    story.extend(
        bullet_list(
            [
                "Blog (schoolswp.com) avec articles SEO, guides, comparatifs",
                "Newsletter",
                "Chaine YouTube",
                "Academy (formations TutorLMS)",
                "Presence LinkedIn",
            ],
            styles,
        )
    )
    story.append(
        Paragraph(
            "schoolsWP existe depuis 2021. Des centaines d'articles ont ete publies, une methode documentee, "
            "des outils testes personnellement, et des resultats partages (analytics, trafic, conversions).",
            styles["Body"],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 2. BRANDING
    # ============================================================
    story.append(Paragraph("2. Branding et regles editoriales", styles["H1"]))
    story.append(hr())

    story.append(Paragraph("Naming", styles["H2"]))
    story.append(
        Paragraph(
            "Toujours ecrire <b>schoolsWP</b>. Jamais SchoolsWP, schoolswp, Schoolswp, Schools WP. "
            "Site : schoolswp.com (sans www).",
            styles["Body"],
        )
    )

    story.append(Paragraph("Ton et voix", styles["H2"]))
    story.append(Paragraph("5 attributs : direct, pedagogique, chaleureux, structure, authentique.", styles["Body"]))
    story.append(Paragraph("Tutoiement systematique en francais, sans exception.", styles["Body"]))
    story.append(Paragraph("Jamais condescendant. On accompagne, on n'infantilise pas.", styles["Body"]))

    story.append(Paragraph("Ton par contexte", styles["H3"]))
    story.append(
        make_table(
            ["Contexte", "Ton"],
            [
                ["Support", "Patient, rassurant"],
                ["Sales", "Transparent, educatif, zero pression"],
                ["Social", "Conversationnel, engageant, lecons concretes"],
                ["Technique", "Clair, progressif, du concret vers le concept"],
            ],
            col_widths=[W * 0.3, W * 0.7],
        )
    )

    story.append(Paragraph("Style redactionnel", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Phrases courtes : 8-15 mots en moyenne, 20 mots max",
                "Structure : sujet + verbe + complement",
                "Paragraphes de 2-4 phrases, une idee par paragraphe",
                "Gras avec parcimonie (concepts cles uniquement)",
                "Italique reserve aux noms d'outils/logiciels",
                "Emojis : 1 par section max, et seulement si pertinent",
            ],
            styles,
        )
    )

    story.append(Paragraph("Vocabulaire", styles["H2"]))
    story.append(Paragraph("<b>Mots a utiliser :</b>", styles["BodyBold"]))
    story.append(
        Paragraph(
            "en clair, concretement, etape par etape, teste et approuve, actionnable, automatiser, "
            "structurer, optimiser, gagner du temps, levier de croissance, ecosysteme, methode, systeme.",
            styles["Body"],
        )
    )
    story.append(Paragraph("<b>Mots interdits :</b>", styles["BodyBold"]))
    story.append(
        Paragraph(
            "disruptif, game changer, scalable, leverage, hack/growth hack, revolutionnaire, incroyable, "
            "le meilleur du marche, en un clic, sans effort, simplement (quand c'est pas simple), il suffit de.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Claims et preuves", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Zero promesse non prouvee. Pas de chiffres sans source ou experience personnelle.",
                'Formulation preferee : "dans mon cas", "sur schoolsWP", "d\'apres mes tests".',
                "Jamais d'affirmation universelle.",
            ],
            styles,
        )
    )

    story.append(Paragraph("CTAs et liens affilies", styles["H2"]))
    story.extend(
        bullet_list(
            [
                'CTA utile, jamais agressif : "Teste par toi-meme", "Decouvre comment faire".',
                "Un seul CTA principal par contenu.",
                'Disclosure affilies obligatoire : "Lien affilie -- je recommande uniquement les outils que j\'utilise."',
            ],
            styles,
        )
    )

    story.append(Paragraph("Couleurs et typographie", styles["H2"]))
    story.append(
        make_table(
            ["Element", "Valeur"],
            [
                ["Primary", "#00D400"],
                ["Secondary", "#00A100"],
                ["Accent", "#E668D4"],
                ["Darkest", "#12111F"],
                ["White bg", "#FAFBFD"],
                ["Titres", "Nunito Sans Bold 700"],
                ["Body", "Roboto Regular 400, 1.2rem"],
            ],
            col_widths=[W * 0.35, W * 0.65],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 3. METHODE schoolsWP
    # ============================================================
    story.append(Paragraph("3. La methode schoolsWP (6 frameworks)", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Le systeme strategique schoolsWP repose sur 6 frameworks qui forment une boucle continue : "
            "Architecture -> Decision -> Production -> Transformation -> Experimentation -> Optimisation.",
            styles["Body"],
        )
    )
    story.append(
        Paragraph(
            "<i>\"Ne jamais produire du contenu isole. Chaque contenu doit s'integrer dans un systeme : "
            'SEO, distribution, conversion, automatisation."</i>',
            styles["Quote"],
        )
    )

    frameworks = [
        (
            "SPECS - Architecture Blueprint",
            "Cadrer un projet.",
            [
                "Architecture SEO",
                "Plan de site et cocon semantique",
                "Structure d'offre",
                "Conception de formation",
                "Tunnel marketing",
            ],
            "Un plan strategique clair.",
        ),
        (
            "Decision Engine - Arbitrage strategique",
            "Prendre des decisions intelligentes.",
            ["Prioriser sujets SEO", "Choisir un outil", "Arbitrer entre strategies", "Decider du meilleur levier"],
            "Une recommandation priorisee.",
        ),
        (
            "CREDO - Production premium",
            "Produire du contenu a forte valeur.",
            ["Pages piliers", "Articles SEO", "Pages de vente", "Sequences email", "Lead magnets"],
            "Contenu structure et pret a publier.",
        ),
        (
            "DITO - Transformation omnicanale",
            "Transformer un contenu en plusieurs formats.",
            ["Article -> LinkedIn", "Article -> newsletter", "Video -> article", "Transcript -> FAQ"],
            "Amplification du contenu.",
        ),
        (
            "PACT - Experimentation",
            "Tester des hypotheses.",
            ["Amelioration CTR", "Tests d'angles SEO", "Tests de CTA", "Validation de positionnement"],
            "Experimentations mesurables.",
        ),
        (
            "TDD - Performance Loop",
            "Optimisation continue.",
            ["Ameliorer conversion", "Optimiser SEO", "Corriger une chute de trafic", "Ameliorer une landing"],
            "Amelioration durable.",
        ),
    ]

    for title, desc, usages, result in frameworks:
        story.append(Paragraph(title, styles["H2"]))
        story.append(Paragraph(desc, styles["Body"]))
        story.append(Paragraph("<b>Utilise pour :</b>", styles["BodyBold"]))
        story.extend(bullet_list(usages, styles))
        story.append(Paragraph(f"<b>Resultat :</b> {result}", styles["Body"]))

    story.append(PageBreak())

    # ============================================================
    # 4. AUTO-ROUTER
    # ============================================================
    story.append(Paragraph("4. Auto-Router : les 6 modes operationnels", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Le schoolsWP OS route automatiquement chaque demande vers le bon mode, "
            "produit un livrable actionnable, et enchaine sur l'etape suivante.",
            styles["Body"],
        )
    )

    modes = [
        (
            "A) ARCHITECT (SPECS)",
            "Plan, architecture, cocon, roadmap, offre, formation, tunnel, page pilier",
            "Resume objectif, perimetre (in/out), architecture proposee, plan d'action P1/P2/P3, risques, next step",
        ),
        (
            "B) STRATEGIST (Decision Engine)",
            "Choisir, prioriser, entre X et Y, trade-off, est-ce que ca vaut le coup",
            "Options (2-5), criteres (ROI, vitesse, risque), reco claire, plan court, next step",
        ),
        (
            "C) PRODUCER (CREDO)",
            "Redige, ecris, page SEO, article, landing, email, script, lead magnet",
            "Angle + promesse, plan H2/H3, brouillon, FAQ (5-10), titles/meta, CTA, next step",
        ),
        (
            "D) TRANSFORMER (DITO)",
            "Transforme, repurpose, resume, carrousel, newsletter, thread",
            "Resultat pret a publier, variantes, checklist publication, next step",
        ),
        (
            "E) EXPERIMENT (PACT)",
            "CTR, test, A/B, hypothese, ameliorer, optimiser title",
            "Probleme, hypothese testable, plan de test, KPI + seuil, actions si succes/echec, next step",
        ),
        (
            "F) OPTIMIZER (TDD)",
            "Ca convertit pas, baisse, debug, lent, Core Web Vitals, GSC chute",
            "Diagnostic, quick wins (30 min), fix propre (2-3h), mesure (GSC/GA4), next step",
        ),
    ]

    for title, triggers, output in modes:
        story.append(Paragraph(title, styles["H3"]))
        story.append(Paragraph(f"<b>Declencheurs :</b> {triggers}", styles["Body"]))
        story.append(Paragraph(f"<b>Sortie :</b> {output}", styles["Body"]))

    story.append(Paragraph("Regles de routage (par priorite)", styles["H2"]))
    routing = [
        "1. Transformation d'un contenu existant -> TRANSFORMER",
        "2. Redaction / production -> PRODUCER",
        "3. Test / CTR / hypothese -> EXPERIMENT",
        "4. Optimisation d'un existant -> OPTIMIZER",
        "5. Choix / priorisation -> STRATEGIST",
        "6. Structure / architecture -> ARCHITECT",
        "7. Ambigu -> STRATEGIST par defaut",
    ]
    story.extend(bullet_list(routing, styles))
    story.append(PageBreak())

    # ============================================================
    # 5. STACK TECHNIQUE
    # ============================================================
    story.append(Paragraph("5. Stack technique officielle", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "La stack doit etre : simple, coherente, automatisable, scalable. "
            "Chaque outil contribue a l'acquisition, la conversion, l'automatisation ou la monetisation.",
            styles["Body"],
        )
    )

    story.append(
        make_table(
            ["Categorie", "Outil", "Role"],
            [
                ["CMS", "WordPress", "Flexibilite maximale et propriete totale du site"],
                ["SEO", "Rank Math Pro", "Optimisation on-page, schemas, metadonnees, sitemap"],
                ["CRM", "FluentCRM", "Segmentation, sequences email, scoring, automatisation marketing"],
                ["Formulaires", "Fluent Forms", "Formulaires avances, collecte de leads, integrations CRM"],
                ["Reservation", "FluentBooking", "Prise de rendez-vous, automatisation de rendez-vous"],
                ["LMS", "TutorLMS", "Creation de formations, gestion d'etudiants, monetisation"],
                ["Collaboration", "FluentBoards", "Gestion de projet, suivi de taches"],
                ["Automatisation", "OttoKit (ex-SureTriggers)", "Automatisation WordPress cloud + AI Agents + MCP"],
                ["Orchestration", "n8n", "Workflows d'automatisation (self-hosted)"],
                ["IA", "Claude (Anthropic)", "Agents de production, audit, strategie"],
            ],
            col_widths=[W * 0.18, W * 0.28, W * 0.54],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 6. ARCHITECTURE SEO
    # ============================================================
    story.append(Paragraph("6. Architecture SEO", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Migration en cours depuis mars 2026 : passage de 20 categories a 6 silos thematiques forts "
            "pour construire l'autorite topique sur 90 jours.",
            styles["Body"],
        )
    )
    story.append(Paragraph("Les 6 silos (valides par data GSC/Ahrefs)", styles["H2"]))
    story.append(
        make_table(
            ["Slug", "Perimetre"],
            [
                ["/wordpress/", "Guides, design, outils, mises a jour"],
                ["/seo/", "SEO, vitesse, hebergement, maintenance"],
                ["/automatisation/", "n8n, FluentCRM, OttoKit, CRM"],
                ["/plugins/", "E-commerce, affiliation, adhesion, reservations"],
                ["/contenu/", "IA, redaction, reseaux sociaux, traduction"],
                ["/academy/", "Formations, LMS, newsletter, ressources"],
            ],
            col_widths=[W * 0.25, W * 0.75],
        )
    )
    story.append(Paragraph("Decisions cles", styles["H3"]))
    story.extend(
        bullet_list(
            [
                "Slug /seo/ (pas /seo-performance/) : volume 2400-3600/mois vs 590-1000",
                "Slug /plugins/ (pas /monetisation/) : plus large, couvre tous les cas d'usage",
                "Migration en 2 phases : categories d'abord, articles ensuite a J+60",
                "10 URLs critiques (75% du trafic) : jamais toucher sans 301 verifiee",
            ],
            styles,
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 7. SEO ENGINE
    # ============================================================
    story.append(Paragraph("7. SEO Engine : la philosophie", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Le SEO n'est pas une accumulation d'articles. C'est un systeme compose de : "
            "pages piliers, clusters thematiques, maillage interne, optimisation continue, distribution omnicanale. "
            "Chaque contenu doit servir un objectif strategique.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Types de contenus SEO", styles["H2"]))

    story.append(Paragraph("Page pilier", styles["H3"]))
    story.append(
        Paragraph(
            "Devenir la reference sur un sujet. Contenu long, structure pedagogique, sections claires, "
            "FAQ, comparaisons, exemples concrets.",
            styles["Body"],
        )
    )
    story.append(
        Paragraph(
            "Structure : Introduction -> Definition -> Guide principal -> Comparaisons -> "
            "Erreurs frequentes -> FAQ -> Conclusion + CTA.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Article cluster", styles["H3"]))
    story.append(
        Paragraph(
            "Renforcer la page pilier. Angle specifique, ciblage mot-cle precis, renvoi vers la page pilier. "
            "Ex : TutorLMS avis, TutorLMS prix, TutorLMS vs LearnDash.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Article comparatif", styles["H3"]))
    story.append(
        Paragraph(
            "Capter les recherches decisionnelles. Structure : Introduction -> Presentation des outils -> "
            "Comparaison criteres -> Avantages/inconvenients -> Conclusion.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Citabilite IA (GEO)", styles["H2"]))
    story.append(
        Paragraph(
            "Les contenus doivent etre faciles a citer par les IA : definitions claires, listes structurees, "
            "tableaux comparatifs, FAQ, reponses directes aux questions.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Priorisation des sujets", styles["H2"]))
    story.append(
        Paragraph(
            "1. Comparatifs -> 2. Avis -> 3. Tutoriels -> 4. Guides complets -> 5. Erreurs frequentes.", styles["Body"]
        )
    )

    story.append(Paragraph("Strategie d'amelioration", styles["H2"]))
    story.append(
        make_table(
            ["Signal GSC", "Action"],
            [
                ["Impressions elevees + CTR faible", "Ameliorer title + meta description"],
                ["Position 5-10", "Enrichir contenu + structure + FAQ"],
                ["Trafic stable", "Ameliorer conversion"],
                ["Page en baisse", "Mise a jour contenu + title + ajout sections"],
            ],
            col_widths=[W * 0.4, W * 0.6],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 8. CONTENT ENGINE
    # ============================================================
    story.append(Paragraph("8. Content Engine : production et transformation", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Un contenu ne doit jamais etre publie une seule fois. Chaque contenu devient une ressource qui peut etre "
            "transformee, reutilisee, distribuee, optimisee. Principe central : 1 contenu principal -> plusieurs contenus derives.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Transformation typique", styles["H2"]))
    story.append(
        Paragraph(
            "Article SEO -> carrousel LinkedIn -> post LinkedIn -> newsletter -> email -> thread -> resume pedagogique. "
            "Chaque format renvoie vers le contenu principal.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Structures recommandees", styles["H2"]))
    story.append(
        make_table(
            ["Format", "Structure"],
            [
                ["LinkedIn", "Hook -> Probleme -> Explication -> Solution -> Conclusion"],
                ["Newsletter", "Introduction -> Idee principale -> Exemple concret -> Conclusion"],
                ["Email", "Hook -> Probleme -> Solution -> CTA"],
                ["Contenu pedagogique", "Comment faire -> Pourquoi c'est important -> Erreurs a eviter"],
            ],
            col_widths=[W * 0.25, W * 0.75],
        )
    )

    story.append(Paragraph("Boucle de contenu", styles["H2"]))
    story.append(Paragraph("SEO -> Distribution -> Engagement -> Optimisation -> (recommence)", styles["Body"]))
    story.append(PageBreak())

    # ============================================================
    # 9. AUTHORITY ENGINE
    # ============================================================
    story.append(Paragraph("9. Authority Engine : construction d'autorite", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "L'autorite ne vient pas d'un article. Elle vient d'un systeme de contenus interconnectes. "
            "Chaque sujet doit etre traite comme un ecosysteme.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Le modele d'autorite en 3 niveaux", styles["H2"]))
    story.append(
        make_table(
            ["Niveau", "Type", "Objectif", "Exemple"],
            [
                ["1", "Page pilier", "Reference complete sur un sujet (hub)", "Guide FluentCRM"],
                [
                    "2",
                    "Articles cluster",
                    "Requetes specifiques, renforce la page pilier",
                    "FluentCRM avis, FluentCRM prix",
                ],
                ["3", "Contenus satellites", "Distribution et amplification", "LinkedIn, newsletter, video"],
            ],
            col_widths=[W * 0.08, W * 0.18, W * 0.40, W * 0.34],
        )
    )

    story.append(Paragraph("Maillage interne", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Chaque cluster renvoie vers la page pilier",
                "La page pilier renvoie vers les clusters",
                "Les clusters se relient entre eux lorsque pertinent",
            ],
            styles,
        )
    )

    story.append(Paragraph("Strategie de progression", styles["H2"]))
    story.append(
        Paragraph(
            "1. Publication page pilier -> 2. Creation de clusters -> 3. Amelioration continue -> "
            "4. Distribution omnicanale -> 5. Optimisation SEO.",
            styles["Body"],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 10. GSC RADAR
    # ============================================================
    story.append(Paragraph("10. GSC Radar : detecter les opportunites", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "La meilleure strategie SEO ne consiste pas a produire plus de contenu. "
            "Elle consiste a identifier les opportunites deja visibles dans Google et les amplifier.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Types d'opportunites", styles["H2"]))
    story.append(
        make_table(
            ["Type", "Conditions", "Actions"],
            [
                ["CTR faible", "Impressions elevees + CTR < 3%", "Ameliorer title, meta, intention"],
                ["Position 5-10", "Position moyenne 5-10 + impressions", "Enrichir contenu, FAQ, maillage"],
                [
                    "Nouvelle requete",
                    "Requete montante, impressions en croissance",
                    "Article dedie ou enrichir existant",
                ],
                ["Page en baisse", "Baisse impressions + position", "Mise a jour contenu, title, sections"],
            ],
            col_widths=[W * 0.18, W * 0.38, W * 0.44],
        )
    )

    story.append(Paragraph("Processus d'analyse", styles["H2"]))
    story.append(
        Paragraph(
            "1. Importer les donnees GSC -> 2. Identifier les opportunites -> "
            "3. Prioriser selon potentiel de trafic -> 4. Definir les actions SEO.",
            styles["Body"],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 11. SEO OPS BRAIN
    # ============================================================
    story.append(Paragraph("11. SEO Ops Brain : schema + scoring", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Version operationnelle du moteur SEO avec schema de donnees, grille de scoring et prompts internes.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Grille de scoring", styles["H2"]))
    story.append(
        Paragraph(
            "Score = OpportunitePosition + OpportuniteCTR + OpportuniteVolume + Tendance + BusinessWeight",
            styles["CodeBlock"],
        )
    )
    story.append(
        make_table(
            ["Composante", "Critere", "Points max"],
            [
                ["Position", "Pos 4-8 = 30pts, 9-12 = 25pts, 1-3 = 10pts", "30"],
                ["CTR", "Pos 1-3 + CTR < 3% = 30pts", "30"],
                ["Volume", "> 10K impressions = 30pts", "30"],
                ["Tendance", "Clics en forte baisse = 20pts", "20"],
                ["Business", "Money page/affiliation = 30pts", "30"],
            ],
            col_widths=[W * 0.2, W * 0.55, W * 0.25],
        )
    )
    story.append(Paragraph("Lecture : 80+ = P1, 50-79 = P2, 20-49 = P3, <20 = ignorer.", styles["Body"]))

    story.append(Paragraph("Types d'opportunites generees", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "CTR_PATCH - amelioration titre/meta",
                "CONTENT_REFRESH - mise a jour contenu",
                "SECTION_EXPANSION - ajout de sections",
                "INTERNAL_LINK_PUSH - renforcement maillage",
                "MONEY_PAGE_BOOST - boost pages monetisees",
            ],
            styles,
        )
    )

    story.append(Paragraph("4 prompts internes", styles["H2"]))
    story.append(
        make_table(
            ["Prompt", "Role"],
            [
                ["GSC Analyst", "Analyse donnees GSC, detecte opportunites, classe en categories"],
                ["SEO Patch Builder", "Produit 3 titles, 2 metas, 5 FAQ, sections, liens internes, CTA"],
                ["Content Refresh Strategist", "Plan de mise a jour priorise (angle, fraicheur, profondeur)"],
                ["Internal Linking Agent", "5 suggestions de liens internes avec ancres et emplacements"],
            ],
            col_widths=[W * 0.32, W * 0.68],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 12. SEO AGENT
    # ============================================================
    story.append(Paragraph("12. SEO Agent : automatisation n8n", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Agent automatise qui lit Google Search Console, agit dans WordPress et produit des actions pretes a valider. "
            "Principe : GSC decide, WP execute, humain valide.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Architecture", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "n8n (orchestrateur)",
                "Google Search Console API (donnees SEO)",
                "WordPress REST API (lecture/ecriture)",
                "Rank Math (metas/schema)",
                "FluentCRM / FluentBoards (suivi optionnel)",
            ],
            styles,
        )
    )

    story.append(Paragraph("Les 3 boucles de l'agent", styles["H2"]))
    story.append(
        make_table(
            ["Boucle", "Frequence", "Objectif", "Sortie"],
            [
                ["Radar", "Quotidien", "Detecter quoi bouge et ou agir", "Liste priorisee P1/P2/P3"],
                ["Ops", "2-3x/semaine", "Produire des patchs SEO rapides", "Drafts + checklist validation"],
                ["Publishing", "Hebdo", "Transformer opportunites en production", "1-3 drafts prets a publier"],
            ],
            col_widths=[W * 0.14, W * 0.18, W * 0.38, W * 0.30],
        )
    )

    story.append(Paragraph("Workflows n8n", styles["H2"]))
    story.append(
        make_table(
            ["Workflow", "Declencheur", "Actions"],
            [
                [
                    "A - GSC Daily Watch",
                    "Cron 07:30",
                    "GSC analytics -> filtre -> enrichissement WP -> score -> taches",
                ],
                ["B - SEO Patch Builder", "Manuel sur P1", "Lire page WP -> generer titles/metas/FAQ/liens -> draft"],
                ["C - Publish Gate", "Statut APPROVED", "Appliquer changements WP -> ping sitemap/IndexNow -> log"],
            ],
            col_widths=[W * 0.25, W * 0.22, W * 0.53],
        )
    )

    story.append(Paragraph("Garde-fous", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Mode human-in-the-loop : jamais d'ecriture directe sur contenu publie",
                "Creation de drafts/propositions uniquement",
                "Validation manuelle avant publication",
                "OAuth GSC scopes minimum, WP Application Password pour user 'Agent SEO'",
                "Logs + rollback (avant/apres)",
            ],
            styles,
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 13. PLAN 24 MOIS
    # ============================================================
    story.append(Paragraph("13. Plan strategique 24 mois", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Faire de schoolsWP une reference sur les sujets WordPress business, automatisation et performance "
            "dans l'ecosysteme WordPress francophone.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Les 4 piliers strategiques", styles["H2"]))
    story.append(
        make_table(
            ["Pilier", "Sujets", "Objectif"],
            [
                [
                    "WordPress Business",
                    "Business WP, freelancing, automatisation, monetisation",
                    "Attirer une audience entrepreneuriale",
                ],
                [
                    "Plugins strategiques",
                    "FluentCRM, TutorLMS, Fluent Forms, FluentBooking, FluentBoards",
                    "Capter les recherches outils",
                ],
                [
                    "Comparatifs",
                    "TutorLMS vs LearnDash, FluentCRM vs Mailchimp, Rank Math vs Yoast",
                    "Capter les recherches decisionnelles",
                ],
                [
                    "Guides avances",
                    "Automatisation WP, CRM WP, SEO WP, performance WP",
                    "Devenir la reference pedagogique",
                ],
            ],
            col_widths=[W * 0.22, W * 0.40, W * 0.38],
        )
    )

    story.append(Paragraph("Modele de contenu par sujet", styles["H2"]))
    story.append(
        Paragraph(
            "1 page pilier -> 5 a 10 articles cluster -> contenus derives (LinkedIn, newsletter, email, video). "
            "Exemple : Guide FluentCRM (pilier) -> FluentCRM avis, prix, tutoriel, automatisation, alternatives (clusters).",
            styles["Body"],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 14. AGENTS PYTHON
    # ============================================================
    story.append(Paragraph("14. Agents Python (28 modules)", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "28 agents Python heritant de BaseContentAgent. Async, retournent du markdown. "
            "Chaque agent = agent.py + cli.py. Modele par defaut : claude-sonnet-4-6.",
            styles["Body"],
        )
    )

    story.append(Paragraph("BaseContentAgent (contrat)", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Async : run(**kwargs) retourne str (markdown)",
                "Modele auto-resolu via MODEL_WRITER env var",
                "ANTHROPIC_API_KEY charge depuis .env",
                "call_llm() : methode standard (system prompt + model auto-injectes)",
                "Protection path traversal : safe_read_path() / safe_write_path()",
                "Logger racine : logging.getLogger('agents')",
            ],
            styles,
        )
    )

    story.append(Paragraph("Modules principaux", styles["H2"]))
    story.append(
        make_table(
            ["Module", "Role"],
            [
                ["content_factory", "Pipeline complet : strategy -> article -> audit -> cluster"],
                ["article_pipeline", "Pipeline sequentiel 5-7 agents (Writer -> Auditor -> Editor -> LLM -> Meta)"],
                ["publish_ready", "4 audits paralleles (SEO + LLM + Conversion + Topical)"],
                [
                    "schoolswp_brain",
                    "Agent strategique (4 modes : seo-writer, plugin-comparator, wp-architect, automation)",
                ],
                ["seo_auditor", "Audit SEO /100 + auto-correction"],
                ["llm_seo", "Citabilite IA /100 + injection"],
                ["conversion_auditor", "Audit conversion /100 + injection"],
                ["topical_authority", "Autorite thematique /100 + expansion"],
                ["knowledge_graph", "Graphe editorial : inventaire sujets + gaps"],
                ["pillar_authority", "Audit autorite par pilier"],
                ["cocon_builder", "Cocon semantique par pilier"],
                ["roi_editorial_plan", "Plan editorial auto-priorise ROI"],
                ["strategic_brain", "Orchestrateur decisionnel -> commandes CLI pretes"],
                ["niche_scout", "Exploration niches SEO + scoring"],
                ["cluster_architect", "Architecture cluster semantique"],
                ["seo_writer", "Redaction SEO standalone"],
                ["plugin_comparator", "Comparaison plugins WordPress"],
                ["thruuu_writer", "Transforme un brief thruuu (.docx) en article markdown"],
            ],
            col_widths=[W * 0.28, W * 0.72],
        )
    )

    story.append(Paragraph("Publish Score", styles["H2"]))
    story.append(
        Paragraph("Score = SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorite x 0.20", styles["CodeBlock"])
    )
    story.append(
        make_table(
            ["Score", "Action"],
            [
                [">= 90", "Publication immediate"],
                ["80-89", "Ajustements mineurs"],
                ["70-79", "Revision ciblee"],
                ["< 70", "Reecriture"],
            ],
            col_widths=[W * 0.2, W * 0.8],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 15. PIPELINES
    # ============================================================
    story.append(Paragraph("15. Pipelines de production", styles["H1"]))
    story.append(hr())

    story.append(Paragraph("Pipeline complet (brain.bat)", styles["H2"]))
    story.append(
        Paragraph(
            "strategy.md -> v1.md -> audit-seo.md -> audit-llm.md -> audit-conversion.md -> "
            "audit-topical.md -> v2.md -> cluster.md -> meta.md",
            styles["CodeBlock"],
        )
    )

    story.append(Paragraph("Pipeline article (article_pipeline)", styles["H2"]))
    story.append(
        Paragraph("v1.md -> audit.md -> serp-sim.md -> v2.md -> v3.md -> ner.json -> meta.md", styles["CodeBlock"])
    )

    story.append(Paragraph("Pipeline strategique recommande", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "1. knowledge_graph -> inventaire sujets + gaps",
                "2. pillar_authority --all -> audit autorite par pilier",
                "3. cocon_builder --pillar lms -> cocon semantique",
                "4. roi_editorial_plan -> plan editorial priorise ROI",
                "5. strategic_brain -> decisions + commandes CLI pretes",
            ],
            styles,
        )
    )

    story.append(Paragraph("Pipeline Brain Lite (5 etapes, sans NER/SERP)", styles["H2"]))
    story.append(
        Paragraph(
            "Version simplifiee du pipeline complet. Entry point : agents.article_pipeline.brain_lite_cli. "
            "Utilise brain-lite.bat comme wrapper.",
            styles["Body"],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 16. FORMATIONS
    # ============================================================
    story.append(Paragraph("16. Formations en cours", styles["H1"]))
    story.append(hr())
    story.append(
        Paragraph(
            "Trois formations en production, hebergees sur TutorLMS Pro (schoolsWP). "
            "Modele freemium : modules 1-3 gratuits (lead magnet), modules suivants premium. "
            "Videos HeyGen (avatars) + voix clonee ElevenLabs (francais).",
            styles["Body"],
        )
    )

    story.append(Paragraph("Formation TutorLMS", styles["H2"]))
    story.append(
        make_table(
            ["Element", "Detail"],
            [
                ["Modules", "16 modules, ~130 lecons"],
                ["Freemium", "M1-M3 gratuits, M4-M16 premium"],
                ["Ressources", "38 transcripts, 22 doc-scrapes, plan, Google Sheets, Drive"],
                ["Statut", "Scripts en cours, pipeline video a lancer"],
            ],
            col_widths=[W * 0.25, W * 0.75],
        )
    )

    story.append(Paragraph("Formation FluentCRM", styles["H2"]))
    story.append(
        make_table(
            ["Element", "Detail"],
            [
                ["Modules", "16 modules, 130 lecons, ~11h05 de contenu"],
                ["Freemium", "M1-M3 gratuits, M4-M16 premium"],
                ["Ressources", "5 videos transcrites, 51 pages doc scrapees, gap analysis, scripts M1-M3 prets"],
                ["Statut", "Pipeline termine. Production video HeyGen a lancer."],
            ],
            col_widths=[W * 0.25, W * 0.75],
        )
    )

    story.append(Paragraph("Formation OttoKit (ex-SureTriggers)", styles["H2"]))
    story.append(
        make_table(
            ["Element", "Detail"],
            [
                ["Modules", "14 modules, 112 lecons, ~10h contenu"],
                ["Freemium", "M1-M3 gratuits, M4-M14 premium"],
                ["Ressources", "Doc officielle, 20+ tutos, gap analysis, scripts M1-M14 complets"],
                ["Statut", "Scripts M1-M14 complets. Production video a lancer."],
                ["Particularite", "1310+ integrations, MCP-native, AI Agents, plans gratuit a lifetime"],
            ],
            col_widths=[W * 0.25, W * 0.75],
        )
    )
    story.append(PageBreak())

    # ============================================================
    # 17. PROJETS ACTIFS
    # ============================================================
    story.append(Paragraph("17. Projets actifs et automatisations", styles["H1"]))
    story.append(hr())

    story.append(Paragraph("Pipeline LinkedIn Prospecting V4", styles["H2"]))
    story.append(
        Paragraph(
            "Pipeline B2B complet : URL post LinkedIn -> scrape Apify -> normalisation Claude -> "
            "enrichissement Unipile -> scoring ICP -> messages personnalises -> rapport HTML.",
            styles["Body"],
        )
    )
    story.extend(
        bullet_list(
            [
                "30 noeuds n8n, 28 connexions",
                "9 SOP, 4 schemas JSON, 6 prompts Claude",
                "Credentials : Apify, Anthropic, Unipile, Hunter",
                "Fichiers dans systems/linkedin-prospecting/",
            ],
            styles,
        )
    )

    story.append(Paragraph("Video Marketing (Remotion)", styles["H2"]))
    story.append(
        Paragraph(
            "Generation de videos programmatiques avec Remotion (React). "
            "Source de verite : theme.ts (couleurs, typo) + texts.ts (contenus).",
            styles["Body"],
        )
    )

    story.append(Paragraph("Workspace technique", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "Python 3.11+, gestionnaire uv, venv .venv/",
                "CI GitHub Actions : ruff check -> ruff format -> pytest",
                "Pre-commit hooks : secrets-scan, ruff, pip-audit",
                "Dependabot : mises a jour pip + npm hebdomadaires",
                "MCP servers : n8n-mcp, rapidapi, dataforseo, wisewand",
                "Logs : logs/agents.log (rotation 10 MB x 5)",
            ],
            styles,
        )
    )

    story.append(Paragraph("Audit workspace", styles["H2"]))
    story.append(
        Paragraph("Audit mensuel du workspace (skill dedie). Score initial : 6.6/10 (mars 2026).", styles["Body"])
    )
    story.append(PageBreak())

    # ============================================================
    # 18. DOMAINES ET INFRA
    # ============================================================
    story.append(Paragraph("18. Domaines et infrastructure", styles["H1"]))
    story.append(hr())

    story.append(Paragraph("Portefeuille de domaines", styles["H2"]))
    story.append(
        make_table(
            ["Domaine", "Role", "Statut"],
            [
                ["schoolswp.com", "Domaine principal", "Acquis"],
                ["schoolswp.fr", "Protection marque .fr", "Acquis (mars 2026)"],
                ["schoolwp.fr", "Anti-typo .fr", "Acquis (mars 2026)"],
                ["schoolswp-academy.fr", "Actif business / formation", "Acquis (mars 2026)"],
                ["schoolwp.com", "Anti-typo mondial", "En tentative (expire sept. 2026)"],
            ],
            col_widths=[W * 0.30, W * 0.38, W * 0.32],
        )
    )
    story.append(
        Paragraph(
            "Registrar : Netim. Extensions autorisees : .com et .fr uniquement. "
            "Portefeuille ferme a 5 domaines max. Structure inversee preferee (schoolswp-X).",
            styles["Body"],
        )
    )

    story.append(Paragraph("Infrastructure", styles["H2"]))
    story.extend(
        bullet_list(
            [
                "n8n self-hosted : schoolswp-n8n.wp1.host",
                "Docker + Prometheus (dossier infra/)",
                "Google Workspace (gws CLI integre)",
                "Google Drive : pipeline editorial actif, convention YYYY-MM-DD_categorie_titre-kebab-case",
            ],
            styles,
        )
    )

    story.append(Spacer(1, 2 * cm))
    story.append(hr())
    story.append(
        Paragraph(
            "Document genere automatiquement a partir de la documentation schoolsWP OS. Version 1.0 - 31 mars 2026.",
            styles["SmallNote"],
        )
    )

    # --- Build ---
    doc.build(story)
    print(f"PDF genere : {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()

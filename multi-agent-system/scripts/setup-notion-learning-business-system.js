#!/usr/bin/env node
/**
 * setup-notion-learning-business-system.js
 * Crée la page "Positionnement Ultra-Niche — Learning Business System" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-learning-business-system.js
 */

"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function notionRequest(method, path, body) {
  const res = await fetch(`https://api.notion.com/v1${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Content-Type": "application/json",
      "Notion-Version": "2022-06-28",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Notion API ${res.status} — ${err}`);
  }
  return res.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------------------
// Block builders
// ---------------------------------------------------------------------------

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: {
    bold: opts.bold || false,
    italic: opts.italic || false,
    code: opts.code || false,
    color: opts.color || "default",
  },
});

const h1 = (text) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(text)] } });
const h2 = (text) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(text)] } });
const h3 = (text) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(text)] } });
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (text) => ({
  object: "block", type: "numbered_list_item",
  numbered_list_item: { rich_text: [rt(text)] },
});
const tod = (text, checked = false) => ({
  object: "block", type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (text) => ({
  object: "block", type: "quote",
  quote: { rich_text: [rt(text)] },
});
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Données — ICP ultra-niche
// ---------------------------------------------------------------------------

const ICP_PROFILES = [
  {
    emoji: "🎓",
    label: "Le Formateur Expert Métier",
    profil: "Coach, consultant ou expert avec 1 à 3 formations existantes. CA 30–100k€/an. Il sait former mais il ne maîtrise pas les systèmes.",
    pain: [
      "Tunnel de vente bricolé (pages Elementor + Stripe + MailPoet sans cohérence)",
      "CRM inexistant ou mal structuré (pas de segmentation, relances manuelles)",
      "LMS installé mais sous-utilisé (pas d'upsell, pas d'automatisation élève)",
      "Perd 20–30 % de ses ventes par friction dans le tunnel",
    ],
    gain: [
      "Système complet : LMS + CRM + tunnel + automatisation",
      "Upsell et cross-sell configurés dès le départ",
      "Zero intervention manuelle sur les relances et l'onboarding élève",
    ],
    budget: "5 000 à 10 000 €",
    source: "schoolsWP (articles LMS, CRM), LinkedIn, bouche-à-oreille",
  },
  {
    emoji: "🏢",
    label: "Le Formateur B2B Corporate",
    profil: "Expert en formation professionnelle (RH, management, tech). Vend en B2B à des entreprises. CA 80–300k€/an.",
    pain: [
      "Besoin d'un LMS multi-entreprises (accès par organisation, tableau de bord RH)",
      "Reporting de progression élève pour ses clients corporate",
      "Catalogue formations structuré avec tarification B2B (devis, factures, accès groupés)",
      "Intégration SSO ou LDAP parfois nécessaire",
    ],
    gain: [
      "LMS professionnel avec portail entreprise",
      "Reporting automatique envoyé aux RH clients",
      "Catalogue clair avec devis automatisé",
    ],
    budget: "8 000 à 20 000 €",
    source: "LinkedIn, référencements directs, journées RH",
  },
  {
    emoji: "🚀",
    label: "Le Créateur de Communauté Premium",
    profil: "Personal brand fort (YouTube, podcast, newsletter). Lance ou scale une offre de formation/membership premium. CA cible > 150k€.",
    pain: [
      "Stack éparpillé : Kajabi ou Teachable + Zapier + ActiveCampaign → coûts et fragmentation",
      "Veut rapatrier sur WordPress pour reprendre le contrôle et réduire les coûts SaaS",
      "Besoin d'un membership + LMS + CRM natifs + tunnel haute conversion",
      "Exige performance, UX premium et zéro downtime",
    ],
    gain: [
      "Stack WordPress propriétaire : MemberPress + Tutor LMS + FluentCRM",
      "Économie de 300–800 €/mois vs stack SaaS",
      "Performance optimisée et UX comparable aux meilleures plateformes SaaS",
    ],
    budget: "10 000 à 20 000 €",
    source: "Contenu schoolsWP, recommandations, veille stack tech",
  },
];

const SEO_ARTICLES = [
  // LMS
  { kw: "tutor lms vs learndash 2026", intent: "comparative", angle: "Pour formateur qui veut scalabilité sans abonnement mensuel" },
  { kw: "lms wordpress formateur en ligne", intent: "décisionnelle", angle: "Comparatif orienté business : fonctionnalités + ROI + automatisation" },
  { kw: "tutor lms configuration complète", intent: "informationnelle", angle: "Setup LMS complet : cours → tunnel → CRM → onboarding élève" },
  { kw: "wordpress formation en ligne rentable", intent: "décisionnelle", angle: "Pourquoi WordPress bat Kajabi sur le long terme (calcul coût réel)" },
  { kw: "learndash vs tutor lms performance", intent: "comparative", angle: "Bench vitesse + charge + UX élève — données réelles" },
  // CRM
  { kw: "fluentcrm formateur wordpress", intent: "informationnelle", angle: "FluentCRM comme CRM pédagogique : séquences élève + relances intelligentes" },
  { kw: "crm wordpress formation en ligne", intent: "décisionnelle", angle: "Quel CRM choisir quand tu vends des formations WordPress ?" },
  { kw: "automatisation email formation wordpress", intent: "informationnelle", angle: "5 automatisations email essentielles pour un formateur LMS WordPress" },
  { kw: "fluentcrm vs activecampaign formateur", intent: "comparative", angle: "Pour formateur WordPress : FluentCRM natif vs ActiveCampaign externe" },
  // Tunnel
  { kw: "tunnel de vente formation wordpress", intent: "informationnelle", angle: "Architecture tunnel complet : landing → checkout → upsell → espace élève" },
  { kw: "upsell formation wordpress", intent: "informationnelle", angle: "Comment configurer l'upsell automatique post-achat avec WooCommerce + LMS" },
  { kw: "optimiser conversion formation en ligne wordpress", intent: "décisionnelle", angle: "Les 7 points de friction qui font perdre 30 % des ventes" },
  { kw: "wordpress membership site formateur", intent: "décisionnelle", angle: "MemberPress vs Paid Memberships Pro pour formateur : verdict honnête" },
  // Architecture système
  { kw: "stack wordpress formateur en ligne 2026", intent: "informationnelle", angle: "Mon stack complet : hébergeur + LMS + CRM + tunnel + paiement + email" },
  { kw: "migrer kajabi wordpress formateur", intent: "décisionnelle", angle: "Calcul du ROI réel : économies + contrôle + performance" },
  { kw: "automatisation onboarding eleve wordpress", intent: "informationnelle", angle: "Séquence onboarding automatique : bienvenue → accès → progression → rétention" },
];

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE
  blocks.push(
    cal(
      "Objectif : ne pas devenir « agence WordPress ». Devenir LA référence d'un segment précis, rentable et cohérent avec schoolsWP.",
      "🎯", "purple_background"
    ),
    p(rt("Mis à jour : mars 2026 · Positionnement SASU premium", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // 1 — CHOIX STRATÉGIQUE
  // ───────────────────────────────────────────
  blocks.push(
    h1("1️⃣ Le Choix Stratégique"),
    p(""),
    h2("Ce que tu abandonnes"),
    bul(rt("✗  ", { bold: true }), rt('"Je crée des sites WordPress."')),
    bul(rt("✗  ", { bold: true }), rt("La concurrence généraliste sur Malt, ComeUp, freelance.com")),
    bul(rt("✗  ", { bold: true }), rt("Les projets à 800–2 000 € sans cohérence ni suite")),
    bul(rt("✗  ", { bold: true }), rt("La pression tarifaire permanente et les mauvais clients")),
    p(""),
    h2("Ce que tu construis"),
    cal(
      "J'aide les formateurs en ligne à structurer un système WordPress rentable, automatisé et évolutif.",
      "🎯", "green_background"
    ),
    p(""),
    bul(rt("✓  ", { bold: true }), rt("Aligné avec ton expertise LMS (Tutor LMS, FluentCRM, tunnels)")),
    bul(rt("✓  ", { bold: true }), rt("Besoin fort d'automatisation et de structuration")),
    bul(rt("✓  ", { bold: true }), rt("Budget bien supérieur au « site vitrine classique »")),
    bul(rt("✓  ", { bold: true }), rt("Logique système naturelle — pas de projets one-shot isolés")),
    bul(rt("✓  ", { bold: true }), rt("Marché en forte croissance (e-learning +15 %/an)")),
    bul(rt("✓  ", { bold: true }), rt("Concurrence faible sur le segment « architecture système »")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // 2 — ICP — 3 PROFILS CIBLES
  // ───────────────────────────────────────────
  blocks.push(
    h1("2️⃣ ICP — 3 Profils Cibles Prioritaires"),
    p("")
  );

  for (const icp of ICP_PROFILES) {
    blocks.push(
      tog(`${icp.emoji} ${icp.label}`, [
        p(""),
        p(rt("Profil", { bold: true })),
        p(icp.profil),
        p(""),
        p(rt("Douleurs principales", { bold: true })),
        ...icp.pain.map((d) => bul(d)),
        p(""),
        p(rt("Gains attendus", { bold: true })),
        ...icp.gain.map((g) => bul(g)),
        p(""),
        p(rt("Budget moyen estimé : ", { bold: true }), rt(icp.budget, { bold: true })),
        p(rt("Source d'acquisition : ", { bold: true }), rt(icp.source)),
      ])
    );
  }

  blocks.push(p(""), div());

  // ───────────────────────────────────────────
  // 3 — PROBLÈMES RÉELS DE LA NICHE
  // ───────────────────────────────────────────
  blocks.push(
    h1("3️⃣ Problèmes Réels de Cette Niche"),
    cal(
      "Les formateurs WordPress empilent des outils, font du bricolage systémique, et perdent 20–40 % de leurs ventes par friction.",
      "🔥", "red_background"
    ),
    p(""),

    h2("Le diagnostic typique d'un formateur qui arrive chez toi"),
    bul(rt("Plugins empilés", { bold: true }), rt(" — LMS + CRM + paiement + email : 4 outils qui ne se parlent pas")),
    bul(rt("Tunnel bancal", { bold: true }), rt(" — landing → checkout → rien : pas d'upsell, pas d'onboarding automatisé")),
    bul(rt("CRM mal structuré", { bold: true }), rt(" — pas de segmentation, relances manuelles, leads perdus")),
    bul(rt("UX élève pauvre", { bold: true }), rt(" — espace membre confus, progression invisible, engagement faible")),
    bul(rt("Performance négligée", { bold: true }), rt(" — pages lentes, Core Web Vitals mauvais, Google qui pénalise")),
    bul(rt("Zéro stratégie de rétention", { bold: true }), rt(" — pas de cross-sell, pas de renouvellement, revenu one-shot")),
    p(""),

    h2("Ce que ça coûte concrètement"),
    bul("20–30 % de ventes perdues par friction dans le tunnel"),
    bul("Heures de support manuel (onboarding, accès, relances)"),
    bul("300–800 €/mois de SaaS qui pourraient être natifs WordPress"),
    bul("Clients qui abandonnent la formation faute d'engagement"),
    p(""),

    qot("Tu n'arrives pas pour « installer des plugins ». Tu arrives pour résoudre un problème business réel."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // 4 — OFFRE SIGNATURE
  // ───────────────────────────────────────────
  blocks.push(
    h1("4️⃣ Offre Signature — Learning Business System™"),
    cal(
      "Transformation complète du système de formation WordPress. Pas « installation de plugin ». Architecture pédagogique + système business.",
      "🧠", "blue_background"
    ),
    p(""),

    h2("Ce que comprend le Learning Business System™"),
    p(""),
    h3("Phase 1 — Audit & Stratégie (inclus dans l'offre)"),
    bul("Audit LMS existant : cours, accès, progression, UX élève"),
    bul("Audit CRM : segmentation, séquences, automations actives"),
    bul("Audit tunnel : conversion, friction, drop-off points"),
    bul("Audit performance : vitesse, Core Web Vitals, mobile"),
    bul("Livrable : rapport d'architecture + recommandations priorisées"),
    p(""),
    h3("Phase 2 — Architecture & Structuration"),
    bul("Restructuration LMS : arborescence cours → modules → leçons → quiz"),
    bul("Intégration LMS × CRM : tags automatiques selon progression"),
    bul("Configuration tunnel : landing → checkout → upsell → espace élève"),
    bul("Stratégie upsell / cross-sell : logique produit + déclencheurs"),
    bul("Architecture des accès : membership tiers, bundles, abonnements"),
    p(""),
    h3("Phase 3 — Automatisation"),
    bul("Séquence onboarding élève : bienvenue → accès → progression → engagement"),
    bul("Relances automatiques : inactivité, module non complété, expiration accès"),
    bul("Emails transactionnels : confirmation achat, accès, certificat"),
    bul("Segmentation CRM : actifs / passifs / ambassadeurs / churns"),
    bul("Intégration paiement : WooCommerce ou Stripe natif + webhooks"),
    p(""),
    h3("Phase 4 — Optimisation & Transmission"),
    bul("Optimisation UX élève : navigation, progression visuelle, gamification légère"),
    bul("Performance technique : cache, images, lazy load, CDN"),
    bul("Tests de bout en bout : achat → accès → onboarding → progression"),
    bul("Transmission documentée : guide d'utilisation personnalisé"),
    bul("Formation rapide (2h) : comment gérer le système en autonomie"),
    p(""),

    h2("Positionnement tarifaire"),
    tog("💰 Grille tarifaire Learning Business System™", [
      p(""),
      bul(rt("LBS Audit (entrée) : ", { bold: true }), rt("1 500 à 2 500 € — audit complet + rapport d'architecture")),
      bul(rt("LBS Standard : ", { bold: true }), rt("6 000 à 10 000 € — Phases 1 à 4 complètes")),
      bul(rt("LBS Premium : ", { bold: true }), rt("10 000 à 20 000 € — Standard + B2B multi-entreprises + SSO")),
      bul(rt("LBS Maintenance : ", { bold: true }), rt("400 à 900 €/mois — veille, optimisations, support prioritaire")),
      p(""),
      qot("Ratio valeur/prix : 1 formateur qui vend 100 formations/mois à 300 € = 30 000 €/mois. Ton système vaut 10 % de son CA mensuel."),
    ]),
    p(""),

    h2("Ce que tu ne fais pas"),
    bul(rt("✗  ", { bold: true }), rt("Création de contenu pédagogique (c'est le travail du formateur)")),
    bul(rt("✗  ", { bold: true }), rt("Graphisme ou refonte visuelle complète")),
    bul(rt("✗  ", { bold: true }), rt("Stratégie marketing ou copywriting des landing pages")),
    bul(rt("✗  ", { bold: true }), rt("Sites vitrines ou e-commerce génériques")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // 5 — PUISSANCE SEO
  // ───────────────────────────────────────────
  blocks.push(
    h1("5️⃣ Puissance SEO — Articles schoolsWP"),
    cal(
      "Chaque article attire ta cible idéale — et lui fait comprendre que tu es exactement ce qu'il lui faut.",
      "📈", "orange_background"
    ),
    p("")
  );

  // Grouper les articles par cluster
  const clusters = [
    { label: "Cluster LMS", indices: [0, 1, 2, 3, 4] },
    { label: "Cluster CRM & Automatisation", indices: [5, 6, 7, 8] },
    { label: "Cluster Tunnel & Conversion", indices: [9, 10, 11, 12] },
    { label: "Cluster Architecture Système", indices: [13, 14, 15] },
  ];

  for (const cluster of clusters) {
    blocks.push(
      tog(`📂 ${cluster.label} (${cluster.indices.length} articles)`, [
        p(""),
        ...cluster.indices.flatMap((i) => {
          const a = SEO_ARTICLES[i];
          return [
            p(rt(`"${a.kw}"`, { bold: true })),
            p(rt("Intent : ", { bold: true }), rt(a.intent, { italic: true })),
            p(rt("Angle : ", { bold: true }), rt(a.angle)),
            bul(rt("Commande : ", { code: true }), rt(`brain-lite.bat --keyword "${a.kw}" --intent ${a.intent}`, { code: true })),
            p(""),
          ];
        }),
      ])
    );
  }

  blocks.push(p(""), div());

  // ───────────────────────────────────────────
  // 6 — DIFFÉRENCIATION
  // ───────────────────────────────────────────
  blocks.push(
    h1("6️⃣ Différenciation Forte"),
    p(""),

    h2("Ce que vendent les autres"),
    bul(rt("Agences LMS : ", { bold: true }), rt('"Installation technique de Tutor LMS ou LearnDash"')),
    bul(rt("Freelances généralistes : ", { bold: true }), rt('"Je configure votre espace formation WordPress"')),
    bul(rt("Intégrateurs SaaS : ", { bold: true }), rt('"Je connecte Kajabi à votre CRM"')),
    p(""),

    h2("Ce que tu vends"),
    cal(
      "Architecture pédagogique + système business. Pas une installation. Une transformation rentable.",
      "🎯", "purple_background"
    ),
    p(""),

    bul(rt("Tu penses ROI ", { bold: true }), rt("— chaque décision technique a une justification business")),
    bul(rt("Tu penses flux ", { bold: true }), rt("— achat → accès → engagement → upsell → rétention")),
    bul(rt("Tu penses système ", { bold: true }), rt("— tout se connecte, tout est documenté, tout est transmissible")),
    bul(rt("Tu penses long terme ", { bold: true }), rt("— maintenance, évolution, scalabilité naturelle")),
    p(""),

    h2("Les 3 preuves de différenciation"),
    num("Tu connais le métier de formateur (tu parles leur langue business)"),
    num("Tu as un contenu schoolsWP qui démontre ton expertise avant même l'appel"),
    num("Tu livres un système complet, pas un assemblage de plugins"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // 7 — ULTRA-NICHE DANS LA NICHE
  // ───────────────────────────────────────────
  blocks.push(
    h1("7️⃣ Ultra-Niche dans la Niche"),
    cal(
      "Plus niche = plus premium. Plus premium = moins de concurrence + prix plus élevés + clients meilleurs.",
      "🔥", "yellow_background"
    ),
    p(""),

    h2("Le spectre de spécialisation"),
    tog("📊 Du généraliste à l'ultra-spécialiste", [
      p(""),
      p(rt("Niveau 1 — Agence WordPress généraliste", { bold: true })),
      bul("Tous types de sites · Concurrence max · Pricing faible · Pas de récurrence"),
      p(""),
      p(rt("Niveau 2 — Spécialiste WordPress formation", { bold: true })),
      bul("Formateurs en ligne · Concurrence modérée · Pricing moyen-haut · Récurrence possible"),
      p(""),
      p(rt("Niveau 3 — Architecte Learning Business System™", { bold: true })),
      bul("Formateurs avec CA > 30k€ · Concurrence quasi nulle · Pricing premium · MRR naturel"),
      p(""),
      p(rt("→ Tu vises le Niveau 3.", { bold: true })),
    ]),
    p(""),

    h2("Critères de qualification ultra-niche"),
    p("À partir de M4-M6, filtrer les prospects entrants sur :"),
    bul(rt("CA > 30 000 €/an", { bold: true }), rt(" — en dessous, le budget pour le LBS est difficile")),
    bul(rt("1 à 3 formations existantes", { bold: true }), rt(" — quelque chose à optimiser, pas de from-scratch sans base")),
    bul(rt("Vente directe sur WordPress ou intention de migrer", { bold: true })),
    bul(rt("Besoin d'automatisation identifié", { bold: true }), rt(" — pas juste un « beau site »")),
    bul(rt("Budget minimal 5 000 €", { bold: true }), rt(" — non négociable sur le LBS Standard")),
    p(""),

    h2("Segments B2B haute valeur"),
    bul(rt("Formateurs corporate RH / management / tech", { bold: true }), rt(" — LBS B2B 8–20k€")),
    bul(rt("Coachs premium business / leadership", { bold: true }), rt(" — LBS 6–12k€ + MRR")),
    bul(rt("Experts métier qui lancent leur première formation", { bold: true }), rt(" — LBS Standard bien accompagné")),
    bul(rt("Créateurs de communauté qui migrent de Kajabi", { bold: true }), rt(" — LBS Premium 12–20k€")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // 8 — AVANTAGE STRATÉGIQUE
  // ───────────────────────────────────────────
  blocks.push(
    h1("8️⃣ Avantage Stratégique"),
    p(""),

    h2("Pourquoi l'ultra-niche est supérieure"),
    bul(rt("Pricing plus élevé : ", { bold: true }), rt("le spécialiste facture 2–3× le généraliste, à projet équivalent")),
    bul(rt("Message clair : ", { bold: true }), rt('le prospect dit "c'est exactement ce qu'il me faut" dès la page offre')),
    bul(rt("Moins de concurrence : ", { bold: true }), rt("personne ne se positionne sur « architecte LBS WordPress »")),
    bul(rt("SEO plus ciblé : ", { bold: true }), rt("les mots-clés LMS + formateur + CRM sont moins disputés")),
    bul(rt("Autorité plus rapide : ", { bold: true }), rt("20 articles ciblés > 200 articles généralistes")),
    bul(rt("Clients meilleurs : ", { bold: true }), rt("ils comprennent la valeur, négocient moins, recommandent plus")),
    p(""),

    h2("La boucle vertueuse ultra-niche"),
    num("Article SEO LMS attire un formateur qualifié"),
    num("Le formateur lit l'article, reconnaît ses problèmes"),
    num("Il clique sur le CTA Audit LBS"),
    num("L'audit révèle 3 à 5 pertes business concrètes"),
    num("Le LBS se justifie seul — c'est une décision business, pas un achat"),
    num("La mission se déroule, résultat mesurable"),
    num("Le témoignage devient un article schoolsWP"),
    num("Retour à l'étape 1 — boucle fermée"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DASHBOARD ACTIONS
  // ───────────────────────────────────────────
  blocks.push(
    h1("📋 Plan d'Action — Learning Business System™"),
    p(""),

    h2("🎯 Positionnement (à faire en 1 semaine)"),
    tod("Rédiger la page offre LBS sur la SASU (basée sur ce doc)"),
    tod("Réécrire le pitch LinkedIn : quitter « créateur de sites » pour « architecte LBS »"),
    tod("Créer le formulaire de qualification 5 critères (CA, formations, besoins, budget, outils)"),
    tod("Configurer Cal.com avec questions pré-appel filtrantes"),
    tod("Préparer le template d'audit LBS livrable (Notion ou PDF)"),
    p(""),

    h2("📝 Contenu schoolsWP — Cluster Prioritaire"),
    tod("Choisir le cluster de départ : LMS ou CRM (pas les deux en même temps)"),
    tod("Lancer les 5 premiers articles avec brain-lite (workflow W1 recommandé)"),
    tod("Intégrer les CTAs LBS Audit dans chaque article"),
    tod("Publier 1 article Architecture Système par mois dès M2"),
    tod("Préparer 1 étude de cas formateur (réel ou test si nécessaire)"),
    p(""),

    h2("💼 Offre & Pipeline SASU"),
    tod("Fixer le prix de lancement LBS Audit : 1 500 € (non négociable)"),
    tod("Définir le prix LBS Standard : 6 000 € (plancher) — 10 000 € (cible M6)"),
    tod("Créer l'onboarding client LBS (checklist + accès Notion + process)"),
    tod("Préparer 1 à 2 cas de test LBS (prix réduit contre témoignage + étude de cas)"),
    tod("Activer la maintenance LBS dès le 1er client : 400 €/mois minimum"),
    p(""),

    h2("📊 Suivi KPIs — Revue mensuelle"),
    tod("Trafic sur articles cluster LMS/CRM (Google Search Console)"),
    tod("Formulaires remplis / appels découverte demandés"),
    tod("Taux de conversion appel → mission (objectif > 50 % à M6)"),
    tod("MRR maintenance (objectif 400 €/mois dès M3, 2 000 €/mois à M12)"),
    tod("CA SASU par mission (suivi Google Sheets ou Notion)"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // RÉCAP VISION
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧩 Vision 12 Mois"),
    p(""),
    tog("📌 L'état cible à M12", [
      p(""),
      p(rt("schoolsWP", { bold: true })),
      bul("20 articles publiés sur le cluster LMS + CRM + tunnel + architecture"),
      bul("Top 3 sur 5 mots-clés formateur LMS WordPress"),
      bul("500+ abonnés newsletter qualifiés formateurs"),
      bul("Affiliation : 2 000 à 5 000 € cumulés sur l'année"),
      p(""),
      p(rt("SASU — Learning Business System™", { bold: true })),
      bul("4 à 6 missions LBS réalisées (4 000 à 15 000 € chacune)"),
      bul("3 à 5 clients en maintenance LBS (1 200 à 4 500 €/mois MRR)"),
      bul("2 études de cas publiées avec résultats business réels"),
      bul("CA SASU : 40 000 à 70 000 € (Année 1 avec démarrage progressif)"),
      p(""),
      p(rt("Positionnement", { bold: true })),
      bul("Reconnu comme l'architecte LBS WordPress francophone"),
      bul("0 démarchage — 100 % inbound via schoolsWP + recommandations"),
      bul("Tarif moyen mission : 8 000 € à M12 (vs 4 000 € à M3)"),
    ]),
    p(""),
    cal(
      "Dans 12 mois : schoolsWP te génère des leads premium. La SASU les transforme en missions à 6–15k€. Et ta maintenance te paye tous les mois sans rien vendre.",
      "⚡", "green_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Positionnement Ultra-Niche — Learning Business System™...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);

  // Batch 1 — Création de la page
  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎓" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🎓 Positionnement Ultra-Niche — Learning Business System™" } },
        ],
      },
    },
    children: batches[0],
  });

  const pageId = page.id;
  console.log(`  ✅ Page créée : ${page.url}`);

  // Batches suivants
  for (let i = 1; i < batches.length; i++) {
    await sleep(600);
    console.log(`\n📦 Ajout batch ${i + 1}/${batches.length}...`);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, {
      children: batches[i],
    });
    console.log(`  ✅ Batch ${i + 1} ajouté`);
  }

  console.log("\n✅  Page créée avec succès !");
  console.log(`   URL : ${page.url}`);
  console.log("\n   Sections :");
  console.log("   1️⃣  Le Choix Stratégique — ce qu'on abandonne vs ce qu'on construit");
  console.log("   2️⃣  ICP — 3 profils (Expert Métier · B2B Corporate · Communauté Premium)");
  console.log("   3️⃣  Problèmes Réels de la Niche — diagnostic formateur type");
  console.log("   4️⃣  Offre Signature — Learning Business System™ (4 phases + pricing)");
  console.log(`   5️⃣  Puissance SEO — ${SEO_ARTICLES.length} articles en 4 clusters (toggles)`);
  console.log("   6️⃣  Différenciation Forte — vs agences LMS et freelances généralistes");
  console.log("   7️⃣  Ultra-Niche dans la Niche — spectre + critères de qualification");
  console.log("   8️⃣  Avantage Stratégique — boucle vertueuse ultra-niche");
  console.log("   📋  Plan d'Action (checkboxes par catégorie)");
  console.log("   🧩  Vision 12 Mois — état cible schoolsWP + SASU");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

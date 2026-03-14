#!/usr/bin/env node
/**
 * setup-notion-revenue-hybrid.js
 * Crée la page "Modèle de Revenu Hybride — Affiliation + Agency + Produit" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-revenue-hybrid.js
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

const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (t) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: [rt(t)] } });
const tod = (t, checked = false) => ({ object: "block", type: "to_do", to_do: { rich_text: [rt(t)], checked } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (t) => ({ object: "block", type: "quote", quote: { rich_text: [rt(t)] } });
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Données — programmes d'affiliation, produits, projections
// ---------------------------------------------------------------------------

const AFFILIATIONS = [
  // CRM / Email
  { categorie: "CRM & Email", nom: "FluentCRM", type: "Plugin WordPress", commission: "30 % récurrent", estimation_mois_m12: "80–200 €", priorite: "🔴 Prioritaire", articles: ["FluentCRM vs MailerLite", "FluentCRM vs ActiveCampaign", "Automatisation email WordPress", "CRM + LMS architecture"] },
  { categorie: "CRM & Email", nom: "WP Fusion", type: "Plugin WordPress", commission: "25–30 % sur licence", estimation_mois_m12: "50–150 €", priorite: "🔴 Prioritaire", articles: ["WP Fusion vs FluentCRM", "CRM + LMS architecture"] },
  { categorie: "CRM & Email", nom: "Groundhogg", type: "Plugin WordPress", commission: "30 % récurrent", estimation_mois_m12: "20–60 €", priorite: "🟠 Secondaire", articles: ["CRM WordPress guide", "Comparatifs CRM WordPress"] },
  // LMS
  { categorie: "LMS", nom: "Tutor LMS", type: "Plugin WordPress", commission: "20–30 % sur vente", estimation_mois_m12: "60–180 €", priorite: "🔴 Prioritaire", articles: ["Tutor LMS vs LearnDash", "LMS WordPress guide", "CRM + LMS architecture"] },
  { categorie: "LMS", nom: "LearnDash", type: "Plugin WordPress", commission: "20 % sur licence", estimation_mois_m12: "40–100 €", priorite: "🟠 Secondaire", articles: ["Tutor LMS vs LearnDash", "LMS WordPress guide"] },
  // Hébergement (commissions élevées one-shot)
  { categorie: "Hébergement", nom: "Kinsta", type: "Hébergeur managé", commission: "50–200 € par vente + 10 % récurrent", estimation_mois_m12: "100–400 €", priorite: "🟠 Secondaire (M6+)", articles: ["Meilleur hébergement WordPress", "Stack WordPress formateur"] },
  { categorie: "Hébergement", nom: "WPServeur", type: "Hébergeur FR", commission: "Variable (programme partenaire)", estimation_mois_m12: "50–200 €", priorite: "🟡 À évaluer", articles: ["Hébergement WordPress FR", "Stack WordPress formateur"] },
  // Outils SEO
  { categorie: "SEO & Outils", nom: "Rank Math Pro", type: "Plugin SEO", commission: "30 % récurrent", estimation_mois_m12: "30–80 €", priorite: "🟡 Naturel si article", articles: ["SEO WordPress guide", "Rank Math vs Yoast"] },
  { categorie: "SEO & Outils", nom: "Semrush / Ahrefs", type: "Outil SEO SaaS", commission: "40 % premier mois ou commission fixe", estimation_mois_m12: "50–150 €", priorite: "🟠 M6+ (audience avancée)", articles: ["Audit SEO WordPress", "Outils SEO pour freelance"] },
  // Automatisation
  { categorie: "Automatisation", nom: "n8n Cloud", type: "Automatisation low-code", commission: "À vérifier (programme partenaire)", estimation_mois_m12: "20–80 €", priorite: "🟡 À activer si article n8n", articles: ["Automatisation WordPress n8n", "Stack automatisation WordPress"] },
];

const PRODUITS_ROADMAP = [
  {
    phase: "Phase 1 — M6",
    emoji: "🧰",
    type: "Mini-produit d'entrée",
    nom: "CRM WordPress Starter Pack",
    prix: "29 à 49 €",
    format: "Guide PDF + checklist + templates FluentCRM (tags, séquences, pipelines)",
    audience: "Freelances et formateurs qui veulent configurer FluentCRM eux-mêmes",
    justification: "Convertit les lecteurs du cluster CRM qui ne sont pas encore prêts pour un audit. Revenu immédiat. Qualifie les leads pour le WBS.",
    ca_potentiel_mois: "100 à 400 €",
    effort: "Faible — basé sur le contenu déjà produit pour schoolsWP",
  },
  {
    phase: "Phase 2 — M9",
    emoji: "📦",
    type: "Template premium",
    nom: "WordPress Business System™ Template Kit",
    prix: "97 à 197 €",
    format: "Notion + documentation : architecture système, checklist audit, schémas d'automatisation, templates contrats",
    audience: "Indépendants qui veulent implémenter le WBS™ seuls, avec la méthode",
    justification: "Monétise la méthode sans temps de mission. Attire des clients qui font eux-mêmes puis réalisent qu'ils ont besoin d'aide (upsell naturel vers WBS Standard).",
    ca_potentiel_mois: "300 à 1 000 €",
    effort: "Moyen — création 2 à 3 semaines, evergreen ensuite",
  },
  {
    phase: "Phase 3 — M12–M15",
    emoji: "🎓",
    type: "Masterclass ou mini-formation",
    nom: "CRM WordPress Stratégique",
    prix: "197 à 397 €",
    format: "Formation vidéo 4 à 6h + templates + support communautaire (Discord ou forum)",
    audience: "Formateurs et freelances qui veulent maîtriser FluentCRM + automatisation en autonomie complète",
    justification: "Capitalise sur le cluster CRM dominant. Audience qualifiée déjà là. Revenus scalables sans temps supplémentaire.",
    ca_potentiel_mois: "500 à 3 000 €",
    effort: "Élevé — création 4 à 8 semaines, ROI long terme fort",
  },
  {
    phase: "Phase 4 — M18–M24",
    emoji: "🚀",
    type: "Programme signature premium",
    nom: "WordPress Business System™ — Programme Complet",
    prix: "997 à 1 997 €",
    format: "Formation complète (LMS + CRM + tunnel + automatisation + architecture) + coaching groupe mensuel",
    audience: "Indépendants qui veulent construire un système WordPress complet, avec accompagnement",
    justification: "Croise tous les clusters (CRM + LMS + automatisation). Public prêt après avoir consommé le contenu schoolsWP pendant 12+ mois. Ticket moyen élevé, fréquence modérée.",
    ca_potentiel_mois: "2 000 à 10 000 €",
    effort: "Très élevé — lancement structuré nécessaire",
  },
];

// Projections financières calculées
const PROJECTIONS = {
  an1: {
    affiliation_mini: 1200,
    affiliation_cible: 4800,
    agency_mini: 40000,
    agency_cible: 65000,
    produits_mini: 0,
    produits_cible: 3000,
  },
  an2: {
    affiliation_mini: 6000,
    affiliation_cible: 12000,
    agency_mini: 60000,
    agency_cible: 90000,
    produits_mini: 6000,
    produits_cible: 20000,
  },
  an3: {
    affiliation_mini: 9600,
    affiliation_cible: 18000,
    agency_mini: 60000,
    agency_cible: 90000,
    produits_mini: 20000,
    produits_cible: 60000,
  },
};

const totalAn = (an) => ({
  mini: an.affiliation_mini + an.agency_mini + an.produits_mini,
  cible: an.affiliation_cible + an.agency_cible + an.produits_cible,
});

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE
  blocks.push(
    cal(
      "Objectif : ne jamais dépendre d'un seul flux. Cash court terme (agency) + actif long terme (affiliation) + levier scalable (produit) = indépendance totale.",
      "💡", "purple_background"
    ),
    p(rt("Mis à jour : mars 2026 · 3 piliers · roadmap 24 mois", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // PRINCIPE : LES 3 RÔLES
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧠 Principe — 3 Flux, 3 Rôles"),
    p(""),
    tog("📊 Tableau des 3 piliers en un coup d'œil", [
      p(""),
      p(rt("🟢 Affiliation — cash organique", { bold: true })),
      bul("Rôle : monétisation naturelle du trafic SEO sans effort marginal"),
      bul("Nature : passif, scalable, récurrent"),
      bul("Risque : dépendance trafic — sans audience, zéro revenu"),
      bul("Horizon : actif qui se construit sur 12 à 24 mois, s'accélère avec le cluster"),
      p(""),
      p(rt("🔵 Agency — cash premium", { bold: true })),
      bul("Rôle : monétisation forte valeur, cash-flow rapide et prévisible"),
      bul("Nature : actif, sélectif, non scalable en temps pur"),
      bul("Risque : bottleneck temps — nécessite processus et sélection clients"),
      bul("Horizon : immédiat, plateau naturel à 3–5 missions/trimestre"),
      p(""),
      p(rt("🟣 Produit — cash scalable", { bold: true })),
      bul("Rôle : monétisation de la méthode sans temps proportionnel"),
      bul("Nature : scalable, indépendant du temps, autorité renforcée"),
      bul("Risque : lancement difficile, nécessite audience existante"),
      bul("Horizon : se lance sur une base d'audience (M6 minimum, M12 pour programme signature)"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PILIER 1 — AFFILIATION
  // ───────────────────────────────────────────
  blocks.push(
    h1("🟢 Pilier 1 — Affiliation (Cash Organique)"),
    cal(
      "Principe : recommander uniquement ce que tu utilises ou valides. Une recommandation crédible convertit 5× mieux qu'un placement publicitaire.",
      "🟢", "green_background"
    ),
    p("")
  );

  // Grouper les affiliations par catégorie
  const categories = [...new Set(AFFILIATIONS.map((a) => a.categorie))];
  for (const cat of categories) {
    const progs = AFFILIATIONS.filter((a) => a.categorie === cat);
    blocks.push(
      h2(`${cat} (${progs.length} programme${progs.length > 1 ? "s" : ""})`),
      p("")
    );
    for (const prog of progs) {
      blocks.push(
        tog(`${prog.priorite}  ${prog.nom} — ${prog.commission}`, [
          p(""),
          p(rt("Type : ", { bold: true }), rt(prog.type)),
          p(rt("Commission : ", { bold: true }), rt(prog.commission)),
          p(rt("Estimation M12 : ", { bold: true }), rt(prog.estimation_mois_m12 + "/mois")),
          p(""),
          p(rt("Articles à connecter :", { bold: true })),
          ...prog.articles.map((a) => bul(a)),
        ])
      );
    }
    blocks.push(p(""));
  }

  const totalEstimMin = AFFILIATIONS.reduce((s, a) => s + parseInt(a.estimation_mois_m12.split("–")[0].replace(/\D/g, ""), 10), 0);
  const totalEstimMax = AFFILIATIONS.reduce((s, a) => s + parseInt(a.estimation_mois_m12.split("–")[1]?.replace(/\D/g, "") || "0", 10), 0);

  blocks.push(
    h2("Potentiel total affiliation à M12"),
    cal(
      `Estimation cumulée tous programmes actifs : ${totalEstimMin.toLocaleString("fr")} à ${totalEstimMax.toLocaleString("fr")} €/mois — soit ${(totalEstimMin * 12).toLocaleString("fr")} à ${(totalEstimMax * 12).toLocaleString("fr")} €/an.`,
      "💰", "green_background"
    ),
    p(""),

    h2("Règles d'affiliation schoolsWP"),
    bul(rt("Règle 1 — Honnêteté absolue", { bold: true }), rt(" : ne recommander que ce qu'on utilise ou qu'on a testé sérieusement")),
    bul(rt("Règle 2 — Disclosure visible", { bold: true }), rt(" : mention claire « lien affilié » dans chaque article concerné")),
    bul(rt("Règle 3 — Article avant lien", { bold: true }), rt(" : le lien affilié renforce un contenu de valeur, il n'en est jamais la raison")),
    bul(rt("Règle 4 — Verdict honnête même si défavorable", { bold: true }), rt(" : si un outil ne convient pas à la cible, le dire — la crédibilité vaut plus que la commission")),
    bul(rt("Règle 5 — Tracker séparé par article", { bold: true }), rt(" : connaître exactement quel article génère quoi pour optimiser en continu")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PILIER 2 — AGENCY
  // ───────────────────────────────────────────
  blocks.push(
    h1("🔵 Pilier 2 — Agency (Cash Premium)"),
    cal(
      "3 à 5 missions premium par trimestre suffisent pour atteindre 50–80k€/an. Le volume n'est pas le levier — la sélection et le pricing le sont.",
      "🔵", "blue_background"
    ),
    p(""),

    h2("Structure de l'offre Agency"),
    tog("💼 WBS Audit — 1 500 € (porte d'entrée)", [
      p(""),
      bul("Durée : 3 à 5 jours"),
      bul("Livrable : rapport 20–30 pages + plan d'action priorisé par ROI"),
      bul("Rôle dans le modèle hybride : qualifier les prospects pour le Standard/Premium"),
      bul("Rôle secondaire : générer la preuve sociale (rapport → étude de cas → contenu schoolsWP)"),
      bul("Imputation sur le WBS suivant si signé dans les 60 jours"),
    ]),
    tog("💼 WBS Standard — 3 000 à 6 000 € (cœur de l'offre)", [
      p(""),
      bul("Durée : 3 à 5 semaines"),
      bul("Périmètre : Phases 1 à 4 sur 1 à 2 modules (CRM + tunnel OU LMS + automatisation)"),
      bul("Rôle dans le modèle hybride : principal générateur de CA Année 1"),
      bul("Rôle secondaire : matière première pour les études de cas et les modules de formation"),
    ]),
    tog("💼 WBS Premium — 7 000 à 12 000 € (transformation complète)", [
      p(""),
      bul("Durée : 6 à 8 semaines"),
      bul("Périmètre : Phases 1 à 4 multi-modules (LMS + CRM + tunnel + automatisation + performance)"),
      bul("Rôle dans le modèle hybride : CA élevé, moins fréquent, case study forte valeur"),
      bul("1 mission Premium = 2 missions Standard en CA, pas en temps × 2"),
    ]),
    tog("🔄 Maintenance WBS — 400 à 900 €/mois (MRR)", [
      p(""),
      bul("Rôle dans le modèle hybride : stabilise le CA mensuel, réduit la dépendance aux nouvelles missions"),
      bul("Cible M6 : 3 clients maintenance → 1 200 à 2 700 €/mois"),
      bul("Cible M12 : 5 à 8 clients maintenance → 2 000 à 7 200 €/mois"),
      bul("Règle : proposer systématiquement à chaque client en fin de mission"),
    ]),
    p(""),

    h2("La contrainte Agency — et comment la gérer"),
    bul(rt("Contrainte : ", { bold: true }), rt("ton temps est limité. À 4 missions/trimestre, tu plafonnes naturellement.")),
    bul(rt("Solution 1 — Augmenter le prix", { bold: true }), rt(" : 1 mission à 10k€ vaut mieux que 2 à 5k€")),
    bul(rt("Solution 2 — Sélectionner plus fort", { bold: true }), rt(" : refuser les clients hors ICP libère du temps pour les bons")),
    bul(rt("Solution 3 — MRR maintenance", { bold: true }), rt(" : chaque client en maintenance réduit le besoin de nouvelles missions")),
    bul(rt("Solution 4 — Externaliser les modules techniques", { bold: true }), rt(" : à partir de M12, sous-traitance possible sur l'implémentation pure")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PILIER 3 — PRODUITS
  // ───────────────────────────────────────────
  blocks.push(
    h1("🟣 Pilier 3 — Produits (Cash Scalable)"),
    cal(
      "Un produit bien conçu génère des revenus quand tu dors. Mais il nécessite une audience existante pour fonctionner — d'abord le SEO, ensuite le produit.",
      "🟣", "purple_background"
    ),
    p("")
  );

  for (const prod of PRODUITS_ROADMAP) {
    blocks.push(
      tog(`${prod.phase} — ${prod.emoji} ${prod.nom} · ${prod.prix}`, [
        p(""),
        p(rt("Type : ", { bold: true }), rt(prod.type)),
        p(rt("Format : ", { bold: true }), rt(prod.format)),
        p(rt("Audience cible : ", { bold: true }), rt(prod.audience)),
        p(rt("Prix : ", { bold: true }), rt(prod.prix)),
        p(rt("CA potentiel mensuel (à maturité) : ", { bold: true }), rt(prod.ca_potentiel_mois)),
        p(rt("Effort de création : ", { bold: true }), rt(prod.effort)),
        p(""),
        p(rt("Justification stratégique :", { bold: true })),
        p(prod.justification),
      ])
    );
  }

  blocks.push(
    p(""),
    h2("Règle du produit — ne pas lancer trop tôt"),
    bul(rt("Condition minimale pour lancer un produit : ", { bold: true }), rt("500+ abonnés newsletter qualifiés OU 5 000+ visiteurs mensuels sur le cluster concerné")),
    bul(rt("Sans audience : ", { bold: true }), rt("un produit numérique ne se vend pas — le contenu SEO et la newsletter sont la condition préalable")),
    bul(rt("Ordre respecté : ", { bold: true }), rt("SEO → audience → produit d'entrée → programme signature. Pas l'inverse.")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // SYNERGIE — MULTIPLICATION D'UN ACTIF
  // ───────────────────────────────────────────
  blocks.push(
    h1("🔄 Synergie — Un Actif, 5 Monétisations"),
    cal(
      "La vraie puissance du modèle hybride : chaque actif créé alimente plusieurs flux en même temps. Ce n'est pas du multitasking — c'est de l'architecture.",
      "🔄", "orange_background"
    ),
    p(""),

    h2("Exemple concret — Article « FluentCRM vs MailerLite »"),
    tog("💡 Un article → 6 sources de valeur", [
      p(""),
      bul(rt("Flux 1 — Affiliation directe : ", { bold: true }), rt("lien affilié FluentCRM dans l'article → 30 % récurrent sur chaque inscription")),
      bul(rt("Flux 2 — Lead Agency : ", { bold: true }), rt("CTA Audit CRM en bas d'article → 1 appel tous les 2 mois → 1 client WBS Standard = 4–6k€")),
      bul(rt("Flux 3 — Newsletter : ", { bold: true }), rt("CTA inscription → abonné qualifié → monétisation future (produit, sponsoring)")),
      bul(rt("Flux 4 — Module formation : ", { bold: true }), rt("section comparatif → extrait du cours « CRM WordPress Stratégique » (M12)")),
      bul(rt("Flux 5 — Thread X + LinkedIn : ", { bold: true }), rt("Workflow W3 content-factory → 5 formats en parallèle depuis l'article")),
      bul(rt("Flux 6 — Maillage cluster : ", { bold: true }), rt("renforce l'autorité du pilier CRM → améliore le ranking des autres articles du cluster")),
      p(""),
      qot("Un seul article bien construit peut valoir 8 000 à 15 000 € de valeur cumulée sur 24 mois."),
    ]),
    p(""),

    h2("Exemple concret — Mission Agency WBS Standard"),
    tog("💼 Une mission → 5 actifs secondaires", [
      p(""),
      bul(rt("Actif 1 — Étude de cas : ", { bold: true }), rt("résultat avant/après → article schoolsWP → trafic SEO + crédibilité")),
      bul(rt("Actif 2 — Contenu SEO : ", { bold: true }), rt("chaque problème résolu = angle d'article potentiel pour le cluster")),
      bul(rt("Actif 3 — Module formation : ", { bold: true }), rt("l'architecture construite = base d'un module dans la formation signature")),
      bul(rt("Actif 4 — Témoignage : ", { bold: true }), rt("preuve sociale pour la page offre WBS + LinkedIn + schoolsWP")),
      bul(rt("Actif 5 — Récurrence MRR : ", { bold: true }), rt("le client bien servi = client maintenance + recommandations futures")),
    ]),
    p(""),

    h2("Exemple concret — Produit Mini (CRM Starter Pack)"),
    tog("🧰 Un produit → 3 rôles stratégiques", [
      p(""),
      bul(rt("Rôle 1 — Qualification automatique : ", { bold: true }), rt("qui achète un produit à 49 € sur le CRM WordPress est exactement dans l'ICP du WBS Audit")),
      bul(rt("Rôle 2 — Réduction du support basique : ", { bold: true }), rt("les questions simples trouvent leur réponse dans le produit, libérant ton temps pour les missions")),
      bul(rt("Rôle 3 — Warm-up programme signature : ", { bold: true }), rt("les acheteurs du mini-produit sont les meilleurs prospects pour la formation complète à M12")),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // RÉPARTITION IDÉALE
  // ───────────────────────────────────────────
  blocks.push(
    h1("📊 Répartition & Projections Financières"),
    p("")
  );

  const an1 = totalAn(PROJECTIONS.an1);
  const an2 = totalAn(PROJECTIONS.an2);
  const an3 = totalAn(PROJECTIONS.an3);

  blocks.push(
    tog(`📅 Année 1 — Ratio 40/40/20 · CA estimé : ${an1.mini.toLocaleString("fr")} à ${an1.cible.toLocaleString("fr")} €`, [
      p(""),
      p(rt("Répartition cible :", { bold: true })),
      bul(rt("40 % Affiliation : ", { bold: true }), rt(`${PROJECTIONS.an1.affiliation_mini.toLocaleString("fr")} à ${PROJECTIONS.an1.affiliation_cible.toLocaleString("fr")} €/an`)),
      bul(rt("40 % Agency : ", { bold: true }), rt(`${PROJECTIONS.an1.agency_mini.toLocaleString("fr")} à ${PROJECTIONS.an1.agency_cible.toLocaleString("fr")} €/an`)),
      bul(rt("20 % Produit : ", { bold: true }), rt(`${PROJECTIONS.an1.produits_mini.toLocaleString("fr")} à ${PROJECTIONS.an1.produits_cible.toLocaleString("fr")} €/an`)),
      p(""),
      p(rt("Logique :", { bold: true })),
      bul("Affiliation = socle progressif (cluster CRM dominant en M6)"),
      bul("Agency = accélérateur principal (missions WBS + maintenance MRR)"),
      bul("Produit = test de marché (mini-produit à 49 € lancé en M6)"),
    ]),
    p(""),

    tog(`📅 Année 2 — Ratio 35/35/30 · CA estimé : ${an2.mini.toLocaleString("fr")} à ${an2.cible.toLocaleString("fr")} €`, [
      p(""),
      p(rt("Répartition cible :", { bold: true })),
      bul(rt("35 % Affiliation : ", { bold: true }), rt(`${PROJECTIONS.an2.affiliation_mini.toLocaleString("fr")} à ${PROJECTIONS.an2.affiliation_cible.toLocaleString("fr")} €/an`)),
      bul(rt("35 % Agency : ", { bold: true }), rt(`${PROJECTIONS.an2.agency_mini.toLocaleString("fr")} à ${PROJECTIONS.an2.agency_cible.toLocaleString("fr")} €/an`)),
      bul(rt("30 % Produit : ", { bold: true }), rt(`${PROJECTIONS.an2.produits_mini.toLocaleString("fr")} à ${PROJECTIONS.an2.produits_cible.toLocaleString("fr")} €/an`)),
      p(""),
      p(rt("Logique :", { bold: true })),
      bul("Cluster LMS actif → affiliation Tutor LMS en croissance"),
      bul("Agency stabilisé avec MRR maintenance fort (5 à 8 clients)"),
      bul("Formation CRM WordPress (M12–M15) → revenus produit en forte hausse"),
    ]),
    p(""),

    tog(`📅 Année 3 — Ratio 30/30/40 · CA estimé : ${an3.mini.toLocaleString("fr")} à ${an3.cible.toLocaleString("fr")} €`, [
      p(""),
      p(rt("Répartition cible :", { bold: true })),
      bul(rt("30 % Affiliation : ", { bold: true }), rt(`${PROJECTIONS.an3.affiliation_mini.toLocaleString("fr")} à ${PROJECTIONS.an3.affiliation_cible.toLocaleString("fr")} €/an`)),
      bul(rt("30 % Agency : ", { bold: true }), rt(`${PROJECTIONS.an3.agency_mini.toLocaleString("fr")} à ${PROJECTIONS.an3.agency_cible.toLocaleString("fr")} €/an`)),
      bul(rt("40 % Produit : ", { bold: true }), rt(`${PROJECTIONS.an3.produits_mini.toLocaleString("fr")} à ${PROJECTIONS.an3.produits_cible.toLocaleString("fr")} €/an`)),
      p(""),
      p(rt("Logique :", { bold: true })),
      bul("Programme signature WordPress Business System™ lancé → revenus scalables"),
      bul("Agency recentré sur les missions premium (10k€+) et le MRR"),
      bul("Affiliation mature sur 3 clusters (CRM + LMS + Performance)"),
      p(""),
      qot("À An3 : le produit dépasse l'agency en CA, avec 10× moins de temps passé. C'est la liberté."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // STRATÉGIE DE PRIORITÉ
  // ───────────────────────────────────────────
  blocks.push(
    h1("🎯 Stratégie de Priorité — Le Bon Ordre"),
    cal(
      "L'ordre compte autant que les actions. Lancer le produit avant d'avoir l'audience, c'est la principale erreur des créateurs qui se précipitent.",
      "⚠️", "yellow_background"
    ),
    p(""),

    h2("Phase 1 — SEO + Affiliation + 1 offre agency (M1–M6)"),
    bul("Dominer le cluster CRM (pilier + 5 satellites minimum)"),
    bul("Activer les programmes d'affiliation FluentCRM et WP Fusion"),
    bul("Lancer et vendre les 3 premiers WBS Audit ou Standard"),
    bul("Structurer le MRR maintenance (premier client en M3)"),
    bul(rt("Pas de produit encore", { bold: true }), rt(" — construire l'audience d'abord")),
    p(""),

    h2("Phase 2 — Ajout mini-produit (M6–M9)"),
    bul("Lancer le CRM Starter Pack à 49 € (mini-produit d'entrée)"),
    bul("Créer le Template Kit WBS à 97–197 €"),
    bul("Utiliser les études de cas des missions pour alimenter les produits"),
    bul(rt("Ne pas encore lancer la formation complète", { bold: true }), rt(" — attendre 500+ abonnés")),
    p(""),

    h2("Phase 3 — Programme signature (M12–M18)"),
    bul("Lancer la formation « CRM WordPress Stratégique » (197–397 €)"),
    bul("Préparer le programme signature WBS (997–1 997 €) pour M18–M24"),
    bul("Agency recentrée sur missions Premium uniquement (> 7 000 €)"),
    bul("MRR maintenance : objectif 3 000 à 5 000 €/mois comme socle stable"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PIÈGES
  // ───────────────────────────────────────────
  blocks.push(
    h1("⚠️ Pièges à Éviter"),
    p(""),

    h2("Les 5 erreurs classiques du modèle hybride"),
    tog("❌ Erreur 1 — Créer 5 produits trop tôt", [
      p(""),
      p("Sans audience, un produit ne se vend pas. Et créer plusieurs produits sans les vendre détruit la motivation et disperse l'énergie."),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("1 mini-produit testé avant de créer le suivant. Valider la demande, puis scaler.")),
    ]),
    tog("❌ Erreur 2 — Multiplier les offres agency", [
      p(""),
      p("10 services différents = 0 positionnement clair. Le prospect ne comprend plus ce que tu fais exactement, et il va chez quelqu'un de plus clair."),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("1 offre signature WBS™, 3 niveaux de prix. C'est tout. La diversité vient des clients, pas de l'offre.")),
    ]),
    tog("❌ Erreur 3 — Diluer le positionnement", [
      p(""),
      p("Accepter des projets hors ICP (sites vitrines, logo, SEO pur, copywriting) pour remplir le planning = signal fort aux prospects que tu n'es pas le spécialiste que tu prétends être."),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("refuser élégamment les demandes hors cible. Chaque refus renforce le positionnement.")),
    ]),
    tog("❌ Erreur 4 — Négliger le MRR au profit des nouvelles missions", [
      p(""),
      p("Sans MRR, chaque mois commence à zéro. C'est le stress permanent du « est-ce que j'aurai assez ce mois-ci »."),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("proposer la maintenance WBS à chaque client. 5 clients à 500 €/mois = 2 500 € qui partent sans effort.")),
    ]),
    tog("❌ Erreur 5 — Ne pas tracker l'affiliation par article", [
      p(""),
      p("Sans tracking, tu ne sais pas quels articles génèrent du revenu affilié et lesquels sont des puits de trafic sans conversion."),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("1 lien trackable par article et par programme. Google Analytics + rapports affiliés mensuels.")),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DASHBOARD ACTIONS
  // ───────────────────────────────────────────
  blocks.push(
    h1("📋 Plan d'Action — Lancement du Modèle Hybride"),
    p(""),

    h2("🟢 Affiliation — À activer maintenant"),
    tod("Rejoindre le programme d'affiliation FluentCRM (priorité absolue)"),
    tod("Rejoindre le programme d'affiliation WP Fusion"),
    tod("Rejoindre le programme d'affiliation Tutor LMS"),
    tod("Créer les liens trackables pour chaque article concerné"),
    tod("Ajouter la mention « lien affilié » dans chaque article avec lien affilié"),
    tod("Mettre en place un tableau de suivi mensuel (article → clics → conversions → CA)"),
    p(""),

    h2("🔵 Agency — À structurer en Semaine 1"),
    tod("Finaliser la page offre WBS™ sur le site SASU"),
    tod("Configurer Cal.com avec formulaire de qualification 5 questions"),
    tod("Rédiger le template de contrat client + conditions de paiement (50/50)"),
    tod("Créer le template d'audit livrable Phase 1 (Notion ou PDF)"),
    tod("Proposer la maintenance WBS systématiquement en fin de chaque mission"),
    p(""),

    h2("🟣 Produit — À préparer pour M6"),
    tod("Lister le contenu déjà produit utilisable dans le CRM Starter Pack"),
    tod("Créer un compte Gumroad ou LemonSqueezy pour la vente de produits digitaux"),
    tod("Préparer le Template Kit WBS (Notion + checklist + schémas)"),
    tod("Définir la stratégie de lancement mini-produit (newsletter + LinkedIn + article)"),
    tod("Planifier la date de lancement : M6 si 300+ abonnés newsletter, M9 sinon"),
    p(""),

    h2("📊 Suivi Global — Mensuel"),
    tod("Créer le tableau de bord hybride : CA affiliation / CA agency / CA produit"),
    tod("Revue mensuelle : quel flux croît, lequel stagne, où investir le mois suivant"),
    tod("Revue trimestrielle : répartition réelle vs objectif 40/40/20"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // VISION 24 MOIS
  // ───────────────────────────────────────────
  blocks.push(
    h1("🚀 Vision 24 Mois — Indépendance Totale"),
    p(""),
    tog("📌 État cible M24 — Le modèle hybride à maturité", [
      p(""),
      p(rt("🟢 Affiliation (mature)", { bold: true })),
      bul("Clusters CRM + LMS actifs — 30 à 40 articles en production"),
      bul("Revenus affiliation : 800 à 1 500 €/mois — passifs, récurrents"),
      bul("3 à 4 programmes d'affiliation actifs et trackés"),
      p(""),
      p(rt("🔵 Agency (stabilisée)", { bold: true })),
      bul("2 à 3 missions WBS par trimestre (focus Premium > 7 000 €)"),
      bul("MRR maintenance : 3 000 à 6 000 €/mois (6 à 10 clients)"),
      bul("Zéro démarchage — pipeline 100 % inbound via schoolsWP"),
      p(""),
      p(rt("🟣 Produit (en croissance)", { bold: true })),
      bul("Mini-produit (49 €) : 20 à 50 ventes/mois = 1 000 à 2 500 €/mois"),
      bul("Formation CRM (297 €) : 5 à 15 ventes/mois = 1 500 à 4 500 €/mois"),
      bul("Programme signature WBS (1 500 €) : en préparation ou lancement"),
      p(""),
      p(rt("Total M24 estimé : ", { bold: true })),
      bul(`CA annuel : ${an2.mini.toLocaleString("fr")} à ${an3.cible.toLocaleString("fr")} € (fourchette An2–An3)`),
      bul("Dont MRR mensuel garanti : 4 500 à 9 000 €/mois (affiliation + maintenance + produits)"),
      bul("Temps de travail : 3 à 4 jours/semaine"),
      bul("Dépendance à un seul flux : nulle — 3 sources actives et complémentaires"),
    ]),
    p(""),
    cal(
      "L'indépendance totale n'est pas un chiffre de CA. C'est quand 3 flux alimentent le compte — et qu'aucun des 3 n'est vital seul.",
      "⚡", "green_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Modèle de Revenu Hybride — Affiliation + Agency + Produit...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  const totalAff = AFFILIATIONS.length;
  const totalProd = PRODUITS_ROADMAP.length;
  const an1t = totalAn(PROJECTIONS.an1);
  const an3t = totalAn(PROJECTIONS.an3);

  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);
  console.log(`   ${totalAff} programmes d'affiliation · ${totalProd} produits roadmap`);
  console.log(`   CA estimé An1 : ${an1t.mini.toLocaleString("fr")}–${an1t.cible.toLocaleString("fr")} € → An3 : ${an3t.mini.toLocaleString("fr")}–${an3t.cible.toLocaleString("fr")} €`);

  // Batch 1 — Création de la page
  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💡" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "💡 Modèle de Revenu Hybride — Affiliation + Agency + Produit" } },
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
  console.log("   🧠  Principe — tableau des 3 piliers en un coup d'œil");
  console.log(`   🟢  Pilier Affiliation — ${totalAff} programmes (toggles par catégorie) + règles`);
  console.log("   🔵  Pilier Agency — 4 offres WBS + contrainte temps + solutions");
  console.log(`   🟣  Pilier Produit — ${totalProd} produits roadmap M6→M24`);
  console.log("   🔄  Synergie — 3 exemples concrets (article + mission + mini-produit)");
  console.log("   📊  Projections An1/An2/An3 avec répartition 40/40/20 → 30/30/40");
  console.log("   🎯  Stratégie de priorité — le bon ordre (SEO → affil → agency → produit)");
  console.log("   ⚠️   5 pièges à éviter (toggles)");
  console.log("   📋  Plan d'action (checkboxes affiliation / agency / produit / suivi)");
  console.log("   🚀  Vision M24 — indépendance totale");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

#!/usr/bin/env node
"use strict";

/**
 * setup-notion-offre-b2b-wordpress-system.js
 * Crée la page Notion : 🏆 Offre Signature — B2B WordPress System™
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-offre-b2b-wordpress-system.js
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ─── DATA ────────────────────────────────────────────────────────────────────

const POSITIONNEMENT = {
  phrase: "Nous structurons l'architecture WordPress des formateurs B2B pour transformer leur offre formation en système rentable, scalable et crédible auprès des entreprises.",
  pas: [
    "Création de site",
    "Installation de plugin",
    "Bricolage LMS",
    "Maintenance technique",
    "Template WordPress générique",
  ],
  oui: [
    "Architecture système",
    "Automatisation business",
    "Vision LTV entreprise",
    "Scalabilité multi-clients",
    "Crédibilité corporate",
  ],
};

const MODULES = [
  {
    num: "1",
    emoji: "🔍",
    titre: "Audit Stratégique B2B",
    sous_titre: "Clarifier avant d'implémenter.",
    duree_type: "1 à 2 semaines",
    livrable_final: "Document stratégique 10–20 pages",
    inclus: [
      "Diagnostic complet de l'écosystème actuel",
      "Analyse du tunnel entreprise (de la prospection à la facturation)",
      "Analyse CRM & segmentation client",
      "Analyse du parcours apprenant (onboarding → renouvellement)",
      "Identification des points de friction business",
      "Plan d'architecture recommandé avec priorisation",
    ],
    valeur_delivree: "Le client comprend où il perd de l'argent. Il achète la suite.",
    questions_client: [
      "Comment mes prospects entreprises me contactent-ils aujourd'hui ?",
      "Où se bloquent les cycles de vente ?",
      "Quels tableaux de bord j'ai vraiment besoin ?",
    ],
  },
  {
    num: "2",
    emoji: "🏗",
    titre: "Architecture LMS B2B",
    sous_titre: "Scalabilité + crédibilité entreprise.",
    duree_type: "2 à 4 semaines",
    livrable_final: "LMS WordPress configuré, documenté, testé",
    inclus: [
      "Structuration comptes entreprise (multi-accès, groupes, cohortes)",
      "Gestion des accès groupés par entreprise cliente",
      "Catalogue formation multi-clients avec permissions granulaires",
      "UX corporate : interface claire, sobre, professionnelle",
      "Sécurisation des accès (tokens, SSO si besoin)",
      "Tests de charge et vérification scalabilité",
    ],
    valeur_delivree: "Le formateur peut onboarder 10 entreprises sans friction manuelle.",
    questions_client: [
      "Comment je gère 5 entreprises avec 50 apprenants chacune ?",
      "Comment mes clients RH accèdent-ils aux rapports ?",
      "Mon LMS est-il crédible face à un acheteur corporate ?",
    ],
  },
  {
    num: "3",
    emoji: "🧠",
    titre: "CRM & Automatisation B2B",
    sous_titre: "Transformer cycle long en système fluide.",
    duree_type: "2 à 3 semaines",
    livrable_final: "CRM configuré + séquences automatisées actives",
    inclus: [
      "Segmentation tripartite : entreprise / décideur / apprenant",
      "Automatisation onboarding (envoi accès, welcome, kick-off)",
      "Relances devis et suivi pipeline commercial",
      "Emails lifecycle : activation → engagement → renouvellement",
      "Séquence renouvellement automatisée (J-90, J-60, J-30)",
      "Pipeline commercial structuré avec scoring prospect",
    ],
    valeur_delivree: "Un lead qualifié entre dans le système et suit un parcours sans intervention manuelle.",
    questions_client: [
      "Comment je relance sans oublier ?",
      "Comment je sais si une entreprise est prête à renouveler ?",
      "Comment je segmente RH, DG et apprenants ?",
    ],
  },
  {
    num: "4",
    emoji: "💼",
    titre: "Tunnel B2B",
    sous_titre: "Filtrer les bons prospects. Qualifier sans réunion.",
    duree_type: "1 à 2 semaines",
    livrable_final: "Tunnel WordPress opérationnel (pages + automatisations)",
    inclus: [
      "Page offre corporate (crédibilité, preuve, process)",
      "Page devis / qualification (formulaire intelligent)",
      "Automatisation pré-vente (scoring, routage, accusé-réception)",
      "Lead scoring interne (budget estimé, urgence, taille équipe)",
      "Workflow interne : notification commercial + tâche CRM",
      "Intégration calendrier (Calendly ou natif WordPress)",
    ],
    valeur_delivree: "Le formateur reçoit des leads déjà qualifiés, avec un budget estimé et un besoin clair.",
    questions_client: [
      "Comment je filtre les curieux des acheteurs sérieux ?",
      "Comment ma page offre parle à un DRH en 30 secondes ?",
      "Comment je sais si une entreprise a un budget formation ?",
    ],
  },
  {
    num: "5",
    emoji: "📊",
    titre: "Optimisation & Reporting",
    sous_titre: "Vision business long terme.",
    duree_type: "1 semaine",
    livrable_final: "Dashboard KPI WordPress + recommandations 90 jours",
    inclus: [
      "Tracking formation (taux complétion, progression, quiz)",
      "KPIs entreprise (LTV, taux renouvellement, coût acquisition)",
      "Tableau de suivi performance (WooCommerce, CRM, LMS consolidés)",
      "Recommandations d'optimisation priorisées",
      "Ajustements conversion tunnel B2B",
      "Session bilan 1h avec plan d'action",
    ],
    valeur_delivree: "Le formateur pilote son activité avec des données, pas des intuitions.",
    questions_client: [
      "Mon taux de renouvellement est-il bon pour mon secteur ?",
      "Où je perds des clients dans mon parcours ?",
      "Quel contenu convertit le mieux en devis ?",
    ],
  },
  {
    num: "6",
    emoji: "📚",
    titre: "Transmission & Autonomie",
    sous_titre: "Indépendance client. Pas de dépendance.",
    duree_type: "1 semaine",
    livrable_final: "Documentation complète + équipe formée",
    inclus: [
      "Formation équipe interne (1 à 3 sessions selon taille)",
      "Documentation personnalisée (pas un template générique)",
      "Tutoriels vidéo internes sur les process clés",
      "Session Q&A post-déploiement (30 jours après)",
      "Guide de maintenance légère (mises à jour, sauvegardes)",
      "Passation propre avec protocole de test",
    ],
    valeur_delivree: "Le client est autonome. Il ne rappelle pas pour chaque mise à jour. Il revient pour évoluer.",
    questions_client: [
      "Mon équipe peut-elle gérer le quotidien sans moi ?",
      "Qu'est-ce que je dois surveiller chaque mois ?",
      "Comment je forme un nouveau commercial sur le CRM ?",
    ],
  },
];

const PRICING = [
  {
    version: "Essentielle",
    emoji: "🟢",
    fourchette: "4 000 € – 6 000 €",
    modules_inclus: ["Module 1 — Audit", "Module 2 — LMS B2B", "Module 6 — Transmission"],
    profil_ideal: "Formateur B2B débutant, 1 à 3 entreprises clientes, LMS basique à structurer.",
    engagement: "4 à 6 semaines",
    garantie: "Architecture documentée + 1 session de formation équipe",
  },
  {
    version: "Avancée",
    emoji: "🔵",
    fourchette: "6 000 € – 9 000 €",
    modules_inclus: ["Module 1 à 4", "Module 6 — Transmission"],
    profil_ideal: "Formateur B2B structuré, 3 à 10 entreprises, veut CRM + tunnel opérationnel.",
    engagement: "6 à 10 semaines",
    garantie: "Tunnel B2B + CRM automatisé + dashboard KPI simplifié",
  },
  {
    version: "Premium",
    emoji: "🟣",
    fourchette: "10 000 € – 15 000 €",
    modules_inclus: ["Modules 1 à 6 complets"],
    profil_ideal: "Formateur B2B ambitieux, CA > 100k€, vise scalabilité multi-clients.",
    engagement: "10 à 14 semaines",
    garantie: "Système complet + reporting B2B + 3 mois de support post-déploiement",
  },
];

const DIFFERENCIATEURS = [
  {
    titre: "Tu comprends le cycle B2B long",
    detail: "La plupart des freelances ont peur du cycle de vente à 8 semaines. Toi, tu l'automatises. Relances, scoring, pipeline — le cycle long devient un avantage structural.",
    preuve: "Séquence renouvellement J-90/J-60/J-30 incluse dans chaque mission.",
  },
  {
    titre: "Tu structures CRM + LMS ensemble",
    detail: "Aucun freelance WordPress ne connecte ces deux univers. Tu es l'architecte qui voit le système entier, pas juste la formation ou juste le CRM.",
    preuve: "Module 2 (LMS) + Module 3 (CRM) sont interdépendants dans ton offre.",
  },
  {
    titre: "Tu penses automatisation, pas prestation",
    detail: "Tu ne livres pas une configuration. Tu livres un système qui tourne sans toi. Le client revient pour évoluer, pas pour réparer.",
    preuve: "Module 6 Transmission : documentation + formation équipe incluses systématiquement.",
  },
  {
    titre: "Tu penses renouvellement client",
    detail: "Ton système est conçu pour que le formateur renouvelle ses contrats entreprise plus facilement. Tu es le levier de son CA récurrent.",
    preuve: "Séquence renouvellement + KPI LTV intégrés dans chaque mission Avancée et Premium.",
  },
  {
    titre: "Tu penses scalabilité réelle",
    detail: "Un formateur qui passe de 3 à 15 entreprises clientes sans changer de stack WordPress — c'est ton livrable. Pas une belle démo, une architecture qui tient.",
    preuve: "Tests de charge, gestion multi-cohortes et accès groupés inclus dans Module 2.",
  },
];

const NOMS_ALTERNATIFS = [
  { nom: "B2B WordPress System™", note: "Nom actuel — fort, clair, propriétaire" },
  { nom: "WordPress Corporate Learning System", note: "Plus explicite pour un DRH. Moins propriétaire." },
  { nom: "Architecture LMS B2B Premium", note: "Descriptif, bon pour SEO. Moins mémorable." },
  { nom: "Corporate WordPress Training System™", note: "Anglais — adapté si clientèle internationale." },
];

const REGLES_VENTE = [
  {
    regle: "Jamais justifier le prix par les heures",
    a_dire: "Ce que vous payez, c'est le système que vous n'aurez pas à reconstruire dans 18 mois.",
    a_ne_pas_dire: "Ça représente environ 60 heures de travail à 150 €/h...",
  },
  {
    regle: "Toujours commencer par l'Audit",
    a_dire: "Avant d'architecturer quoi que ce soit, je dois comprendre votre réalité. L'Audit est la première étape — elle conditionne tout.",
    a_ne_pas_dire: "On peut commencer directement par le LMS si vous préférez.",
  },
  {
    regle: "Qualifier le budget dès le premier appel",
    a_dire: "Pour m'assurer qu'on est alignés : votre budget pour cette transformation est dans quelle fourchette ?",
    a_ne_pas_dire: "On verra ça ensemble, je m'adapte à votre budget.",
  },
  {
    regle: "Ne jamais baisser le prix — ajuster le périmètre",
    a_dire: "Votre budget ne permet pas la version Premium. On peut commencer par l'Essentielle et évoluer.",
    a_ne_pas_dire: "Je peux faire un effort et descendre à 8 000 €.",
  },
  {
    regle: "Vendre la vision, pas les modules",
    a_dire: "Dans 3 mois, vos prospects reçoivent un devis structuré automatiquement, vos apprenants s'onboardent seuls, et vous avez une vue sur votre taux de renouvellement.",
    a_ne_pas_dire: "Le Module 3 inclut 6 automatisations CRM et 4 séquences email.",
  },
];

const OBJECTIONS = [
  {
    objection: "C'est trop cher. Un développeur freelance fait ça pour 1 500 €.",
    reponse: "Un développeur installe des plugins. Moi, je structure un système business. Si votre priorité est le coût minimum, je ne suis pas votre prestataire. Si votre priorité est un système qui tourne dans 3 ans, on peut parler.",
  },
  {
    objection: "On a déjà un site WordPress. On a juste besoin d'améliorer le LMS.",
    reponse: "C'est exactement ce que disent 90% de mes clients avant l'audit. En général, le problème n'est pas le LMS — c'est l'architecture autour. L'audit révèle le vrai problème en 2 semaines.",
  },
  {
    objection: "On n'a pas le temps de s'impliquer dans un projet long.",
    reponse: "C'est précisément pour ça que le Module 3 et le Module 6 existent. Vous validez les jalons, je livre le système. Implication réelle : 2h par semaine pendant 10 semaines.",
  },
  {
    objection: "On peut le faire en interne avec notre développeur.",
    reponse: "Peut-être. La question c'est : votre développeur a-t-il déjà structuré un tunnel B2B + LMS multi-entreprises + CRM automatisé pour un formateur ? Sinon, vous payez son apprentissage, pas son expertise.",
  },
];

const PROCESSUS_VENTE = [
  { etape: "1", action: "Premier contact", detail: "Formulaire de qualification (budget, contexte, urgence)", duree: "Asynchrone" },
  { etape: "2", action: "Appel découverte", detail: "30 min — comprendre la réalité, qualifier le budget, identifier le module entry point", duree: "30 min" },
  { etape: "3", action: "Devis Module 1 (Audit)", detail: "Proposition pour commencer par l'Audit. Prix : 1 200–2 000 €. Decision rapide.", duree: "48h" },
  { etape: "4", action: "Audit stratégique", detail: "2 semaines de diagnostic. Livrable : document 10–20 pages.", duree: "2 semaines" },
  { etape: "5", action: "Restitution + upsell", detail: "Session 1h de restitution. Proposition offre complète sur base des résultats de l'audit.", duree: "1h" },
  { etape: "6", action: "Démarrage mission", detail: "Contrat + acompte 40% → démarrage dans les 5 jours ouvrés.", duree: "5 jours" },
];

// ─── CALC ─────────────────────────────────────────────────────────────────────

const PROJECTIONS = {
  essentielle: { mini: 4000, maxi: 6000 },
  avancee: { mini: 6000, maxi: 9000 },
  premium: { mini: 10000, maxi: 15000 },
};

const scenario_m12 = {
  // 2 Essentielles + 3 Avancées + 1 Premium / an
  conservateur: 2 * PROJECTIONS.essentielle.mini + 3 * PROJECTIONS.avancee.mini + 1 * PROJECTIONS.premium.mini,
  cible: 2 * PROJECTIONS.essentielle.maxi + 3 * PROJECTIONS.avancee.maxi + 1 * PROJECTIONS.premium.maxi,
};
// conservateur: 8000 + 18000 + 10000 = 36 000 €
// cible: 12000 + 27000 + 15000 = 54 000 €

// ─── NOTION HELPERS ───────────────────────────────────────────────────────────

async function notionRequest(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Notion-Version": NOTION_VERSION,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const json = await resp.json();
  if (!resp.ok) throw new Error(`Notion ${resp.status}: ${JSON.stringify(json)}`);
  return json;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

// ─── BLOCK BUILDERS ──────────────────────────────────────────────────────────

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: String(text) },
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
const p = (rts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const bul = (rts, color = "default") => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)], color } });
const num = (rts) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: [rt(text)], color } });
const cal = (text, color = "blue_background") => ({ object: "block", type: "callout", callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji: "💡" }, color } });
const tog = (text, children = []) => ({
  object: "block",
  type: "toggle",
  toggle: {
    rich_text: [rt(text, { bold: true })],
    children,
  },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("🏆 Offre Signature · schoolsWP · Confidentiel", "yellow_background"));
  blocks.push(p([rt("Positionnement premium. Architecture B2B. Système, pas prestation.", { italic: true })]));
  blocks.push(div());

  // ── POSITIONNEMENT ──
  blocks.push(h1("🎯 Positionnement"));
  blocks.push(cal(POSITIONNEMENT.phrase, "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Ce n'est PAS :"));
  POSITIONNEMENT.pas.forEach((item) => blocks.push(bul([rt("✗  " + item, { color: "red" })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("C'est :"));
  POSITIONNEMENT.oui.forEach((item) => blocks.push(bul([rt("✓  " + item, { bold: true, color: "green" })], "green_background")));
  blocks.push(div());

  // ── MODULES ──
  blocks.push(h1("🧱 Structure de l'Offre — 6 Modules"));
  blocks.push(p([rt("Chaque module est vendable séparément ou en bundle. Toujours commencer par le Module 1.", { italic: true })]));
  blocks.push(p(""));

  for (const mod of MODULES) {
    const header = `Module ${mod.num} ${mod.emoji} — ${mod.titre}`;
    const children = [];

    children.push(cal(mod.sous_titre, "gray_background"));
    children.push(p([rt("⏱ Durée type : ", { bold: true }), rt(mod.duree_type)]));
    children.push(p([rt("📄 Livrable final : ", { bold: true }), rt(mod.livrable_final)]));
    children.push(p(""));

    children.push(h3("Inclut"));
    mod.inclus.forEach((item) => children.push(bul(item)));

    children.push(p(""));
    children.push(h3("Valeur délivrée"));
    children.push(qot(mod.valeur_delivree, "blue_background"));

    children.push(p(""));
    children.push(h3("Questions clients que ce module résout"));
    mod.questions_client.forEach((q, i) => children.push(num(`${q}`)));

    blocks.push(tog(header, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── PRICING ──
  blocks.push(h1("💰 Pricing Stratégique"));
  blocks.push(p([rt("Tu ne vends pas des heures. Tu vends une architecture business.", { bold: true, italic: true })]));
  blocks.push(p(""));

  for (const tier of PRICING) {
    const children = [];
    children.push(p([rt("Fourchette : ", { bold: true }), rt(tier.fourchette, { bold: true, color: "green" })]));
    children.push(p([rt("Modules inclus : ", { bold: true }), rt(tier.modules_inclus.join(", "))]));
    children.push(p([rt("Profil idéal : ", { bold: true }), rt(tier.profil_ideal)]));
    children.push(p([rt("Engagement : ", { bold: true }), rt(tier.engagement)]));
    children.push(p([rt("Garantie livrable : ", { bold: true }), rt(tier.garantie)]));

    blocks.push(tog(`${tier.emoji} Version ${tier.version} — ${tier.fourchette}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(h2("📈 Projection CA sur 12 mois"));
  blocks.push(p([rt("Hypothèse : 2 missions Essentielles + 3 Avancées + 1 Premium / an", { italic: true })]));
  blocks.push(p(""));
  blocks.push(bul([rt("Conservateur : ", { bold: true }), rt(`${scenario_m12.conservateur.toLocaleString("fr-FR")} €`)]));
  blocks.push(bul([rt("Cible : ", { bold: true }), rt(`${scenario_m12.cible.toLocaleString("fr-FR")} €`)]));
  blocks.push(p([rt(`→ Soit ${Math.round(scenario_m12.conservateur / 12).toLocaleString("fr-FR")} – ${Math.round(scenario_m12.cible / 12).toLocaleString("fr-FR")} €/mois en revenu moyen agency`, { italic: true, color: "gray" })]));
  blocks.push(div());

  // ── DIFFÉRENCIATEURS ──
  blocks.push(h1("🔥 Ce qui différencie cette offre"));
  blocks.push(p([rt("La majorité des freelances WordPress ne pensent qu'outil. Toi, tu penses système.", { italic: true })]));
  blocks.push(p(""));

  for (const diff of DIFFERENCIATEURS) {
    const children = [];
    children.push(qot(diff.detail, "blue_background"));
    children.push(p(""));
    children.push(p([rt("Preuve concrète : ", { bold: true }), rt(diff.preuve, { italic: true })]));

    blocks.push(tog(`✓ ${diff.titre}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── RÈGLES DE VENTE ──
  blocks.push(h1("🎤 Règles de vente — Ce qui se dit / ne se dit jamais"));
  blocks.push(p(""));

  for (const regle of REGLES_VENTE) {
    const children = [];
    children.push(bul([rt("À dire : ", { bold: true, color: "green" }), rt('"' + regle.a_dire + '"', { italic: true })], "green_background"));
    children.push(bul([rt("À ne JAMAIS dire : ", { bold: true, color: "red" }), rt('"' + regle.a_ne_pas_dire + '"', { italic: true })], "red_background"));

    blocks.push(tog(`⚖️ ${regle.regle}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── OBJECTIONS ──
  blocks.push(h1("🛡 Objections & Réponses"));
  blocks.push(p(""));

  for (const obj of OBJECTIONS) {
    const children = [];
    children.push(qot(obj.objection, "red_background"));
    children.push(p(""));
    children.push(cal(obj.reponse, "green_background"));

    blocks.push(tog(`❓ "${obj.objection.substring(0, 60)}..."`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── PROCESSUS DE VENTE ──
  blocks.push(h1("🗺 Processus de Vente — De l'Audit à la Mission"));
  blocks.push(p([rt("Chaque mission commence par le Module 1 (Audit). Toujours. Sans exception.", { bold: true })]));
  blocks.push(p(""));

  for (const etape of PROCESSUS_VENTE) {
    blocks.push(
      bul([
        rt(`Étape ${etape.etape} — `, { bold: true }),
        rt(`${etape.action}`, { bold: true }),
        rt(` : ${etape.detail} `),
        rt(`(${etape.duree})`, { italic: true, color: "gray" }),
      ])
    );
  }

  blocks.push(p(""));
  blocks.push(cal("Règle absolue : l'Audit n'est pas optionnel. Il filtre les mauvais clients ET révèle le périmètre réel de la mission.", "yellow_background"));
  blocks.push(div());

  // ── NOMS ALTERNATIFS ──
  blocks.push(h1("🏷 Noms Alternatifs — Analyse"));
  blocks.push(p([rt("Nom retenu : ", { bold: true }), rt("B2B WordPress System™", { bold: true, color: "green" })]));
  blocks.push(p(""));

  for (const alt of NOMS_ALTERNATIFS) {
    blocks.push(bul([rt(`${alt.nom}`, { bold: true }), rt(` — ${alt.note}`, { italic: true })]));
  }

  blocks.push(p(""));
  blocks.push(qot("Recommandation : garder B2B WordPress System™ en nom officiel + utiliser 'Architecture LMS B2B Premium' comme accroche SEO sur le site.", "gray_background"));
  blocks.push(div());

  // ── CHECKLIST LANCEMENT ──
  blocks.push(h1("✅ Checklist — Avant de Vendre cette Offre"));
  blocks.push(p(""));

  const checklist = [
    "Page offre corporate publiée sur schoolswp.com/b2b",
    "Formulaire de qualification B2B actif et testé",
    "1 étude de cas formateur B2B documentée (même fictive / anonymisée)",
    "Template de devis Module 1 (Audit) finalisé",
    "Séquence email post-formulaire active (accusé-réception + appel discovery)",
    "Pricing clairement affiché ou sur devis — décision assumée",
    "3 exemples concrets d'architecture LMS B2B en portfolio",
    "Page LinkedIn mise à jour avec positionnement B2B WordPress",
    "1 article pilier SEO publié (ex : 'LMS WordPress B2B : guide complet 2026')",
    "Processus de restitution Audit documenté et testé",
  ];

  checklist.forEach((item) => {
    blocks.push({
      object: "block",
      type: "to_do",
      to_do: {
        rich_text: [rt(item)],
        checked: false,
      },
    });
  });

  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🏆 Vision — Dans 24 mois"));
  blocks.push(p(""));
  blocks.push(cal("schoolsWP est LA référence WordPress des formateurs B2B francophones. Pas le plus connu. Le plus cité par les décideurs qui cherchent une architecture sérieuse.", "purple_background"));
  blocks.push(p(""));
  blocks.push(bul([rt("5 à 8 missions B2B actives ou archivées", { bold: true })]));
  blocks.push(bul([rt("3 études de cas publiées avec résultats mesurés")]));
  blocks.push(bul([rt("1 article/mois sur le terrain vierge (QUALIOPI, LMS multi-entreprises, CRM B2B)")]));
  blocks.push(bul([rt("MRR accompagnement : 5 000 – 10 000 €/mois")]));
  blocks.push(bul([rt("Affiliation + produits digitaux B2B : 2 000 – 5 000 €/mois")]));
  blocks.push(p(""));
  blocks.push(qot("Total visé 24 mois : 80 000 – 130 000 €/an · Source principale : agency B2B", "green_background"));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Offre Signature B2B WordPress System™...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🏆" },
    properties: {
      title: { title: [{ text: { content: "🏆 Offre Signature — B2B WordPress System™" } }] },
    },
    children: firstChunk,
  });

  const pageId = page.id;
  console.log(`✅  Page créée : ${pageId}`);

  let i = 0;
  while (i < rest.length) {
    const batch = rest.slice(i, i + CHUNK);
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, { children: batch });
    i += CHUNK;
    console.log(`   ↳ Batch ${Math.ceil(i / CHUNK)} envoyé (${Math.min(i, rest.length)}/${rest.length})`);
  }

  console.log("");
  console.log("✅  Page complète créée avec succès !");
  console.log(`🔗  https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📊  Projections CA :");
  console.log(`   Conservateur : ${scenario_m12.conservateur.toLocaleString("fr-FR")} €/an`);
  console.log(`   Cible        : ${scenario_m12.cible.toLocaleString("fr-FR")} €/an`);
  console.log(`   Mensuel moy  : ${Math.round(scenario_m12.conservateur / 12).toLocaleString("fr-FR")} – ${Math.round(scenario_m12.cible / 12).toLocaleString("fr-FR")} €/mois`);
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});

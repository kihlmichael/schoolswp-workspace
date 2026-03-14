#!/usr/bin/env node
/**
 * setup-notion-wbs-offer.js
 * Crée la page "WordPress Business System™ — Offre Signature" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-wbs-offer.js
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
// Données — phases, objections, questions de qualification
// ---------------------------------------------------------------------------

const PHASES = [
  {
    num: "1", emoji: "🔍", titre: "Audit Stratégique — La Fondation",
    duree: "3 à 5 jours",
    description: "Avant de construire quoi que ce soit, on comprend l'existant. Pas pour faire plaisir — pour identifier exactement où fuit la valeur.",
    livrables: [
      "Analyse architecture WordPress (plugins, stack, dépendances, dette technique)",
      "Analyse tunnel de vente : landing → checkout → onboarding — points de friction",
      "Analyse CRM : segmentation, séquences actives, données exploitées",
      "Analyse performance : Core Web Vitals, mobile, vitesse réelle",
      "Analyse logique business : cohérence offre / audience / prix / conversion",
      "Identification des fuites de conversion (les 3 à 5 plus impactantes)",
    ],
    livrable_final: "Rapport stratégique (20–30 pages) + plan d'action priorisé par ROI",
    note: "L'audit seul peut être vendu comme offre d'entrée (900–1 500 €). Il sert de porte d'entrée qualifiante ET de fondation pour les phases suivantes.",
  },
  {
    num: "2", emoji: "🏗", titre: "Architecture Système — La Structure",
    duree: "1 à 2 semaines",
    description: "On simplifie avant d'optimiser. La plupart des clients ont trop d'outils qui se chevauchent et se contredisent. On construit un système cohérent.",
    livrables: [
      "Simplification du stack (suppression des doublons, unification des flux)",
      "Choix et justification des outils retenus (LMS, CRM, paiement, email)",
      "Structuration CRM : pipelines, tags, segments, logique de contact",
      "Architecture email : séquences, déclencheurs, logique d'automatisation",
      "Structuration tunnel : pages clés, flux de conversion, points de contact",
      "Schéma d'architecture livré : visualisation complète du système cible",
    ],
    livrable_final: "Schéma système + documentation d'architecture + plan d'implémentation détaillé",
    note: "Cette phase peut être livrée seule pour les clients qui ont les ressources pour implémenter eux-mêmes.",
  },
  {
    num: "3", emoji: "⚙", titre: "Implémentation Stratégique — La Construction",
    duree: "2 à 4 semaines selon périmètre",
    description: "On construit ce qui a été architecturé. Pas d'improvisation. Chaque décision technique est justifiée par un objectif business.",
    livrables: [
      "Configuration FluentCRM : pipelines, tags, séquences automatisées",
      "Tutor LMS (si formateur) : cours, accès, progression, certification",
      "WooCommerce / paiement : produits, upsells, récupération panier abandonné",
      "Funnel de vente : landing optimisée, checkout friction-free, thank-you page",
      "Automatisations clés : onboarding, relances, notifications, webhooks",
      "Optimisation UX conversion : CTA, formulaires, preuves sociales, urgence",
    ],
    livrable_final: "Système opérationnel testé de bout en bout + documentation technique complète",
    note: "Le périmètre est défini en Phase 1 et validé en Phase 2. Pas d'ajouts hors scope sans avenant.",
  },
  {
    num: "4", emoji: "📈", titre: "Optimisation & Scalabilité — La Durée",
    duree: "1 semaine + suivi",
    description: "Un système livré sans suivi, c'est une voiture sans tableau de bord. On installe les instruments de mesure et on prépare l'évolution.",
    livrables: [
      "Configuration KPI tracking : conversions, trafic, taux d'ouverture email, CA par source",
      "Optimisation CTA : A/B testing prioritaire sur les pages à fort trafic",
      "Amélioration performance : vitesse finale, compression, CDN si pertinent",
      "Roadmap 6 mois : prochaines optimisations priorisées par ROI estimé",
      "Formation client (2h) : prise en main du système, gestion autonome",
      "Documentation utilisateur : guide des opérations courantes",
    ],
    livrable_final: "Tableau de bord KPIs + roadmap 6 mois + guide d'autonomie client",
    note: "Cette phase naturellement ouvre vers la maintenance mensuelle — le client a un système à faire vivre.",
  },
];

const OBJECTIONS = [
  {
    objection: "C'est cher pour moi.",
    reponse: "C'est cher comparé à quoi ? Un freelance à 800 € qui ne résout pas le problème ? Ou comparé au CA que tu perds chaque mois avec un système qui fuite ? L'audit seul te montrera exactement ce que ça te coûte de ne rien faire.",
  },
  {
    objection: "J'ai besoin d'y réfléchir.",
    reponse: "Bien sûr. Mais qu'est-ce qui te bloque exactement ? Si c'est le budget : l'audit à 1 500 € est un premier pas sans engagement total. Si c'est la confiance : regarde les études de cas sur schoolsWP. Si c'est le timing : quel est le bon moment pour que ton site génère enfin du CA ?",
  },
  {
    objection: "Je peux le faire moi-même.",
    reponse: "Absolument. Tu peux aussi faire ta comptabilité toi-même. La vraie question : est-ce que tu veux passer 3 mois à apprendre ce que je fais en 3 semaines ? Et est-ce que ton temps vaut mieux utilisé sur ton métier ou sur WordPress ?",
  },
  {
    objection: "J'ai déjà quelqu'un pour mon WordPress.",
    reponse: "Parfait. Est-ce que cette personne a construit ton tunnel, structuré ton CRM et automatisé ton onboarding ? Si oui, tu n'as pas besoin de moi. Si non, on ne fait pas le même travail.",
  },
  {
    objection: "Et si ça ne fonctionne pas ?",
    reponse: "L'audit de Phase 1 te donnera une estimation réaliste des gains potentiels avant qu'on engage le reste. Si le ROI potentiel n'est pas là, je te le dis en Phase 1 — et on ne va pas plus loin.",
  },
];

const QUALIF_QUESTIONS = [
  { q: "Quel est ton CA actuel (fourchette) ?", but: "Filtrer < 30k€/an (budget insuffisant)" },
  { q: "Qu'est-ce qui te coûte le plus de temps sur WordPress en ce moment ?", but: "Identifier la douleur principale" },
  { q: "Tu utilises quoi comme CRM et comme outil email ?", but: "Estimer la dette technique et le périmètre" },
  { q: "C'est quoi ton objectif principal pour les 6 prochains mois ?", but: "Aligner la promesse sur un résultat concret" },
  { q: "Quel budget tu envisages pour structurer ton système ?", but: "Qualifier financièrement avant l'appel" },
];

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE
  blocks.push(
    cal(
      "Une seule offre. Pas 10 services. Une transformation complète du système WordPress — pour des clients qui font déjà du chiffre et veulent en faire plus.",
      "🔥", "red_background"
    ),
    p(rt("Mis à jour : mars 2026 · Version 1.0 — Offre de lancement SASU", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // POSITIONNEMENT
  // ───────────────────────────────────────────
  blocks.push(
    h1("🎯 Positionnement"),
    p(""),
    h2("Ce que tu ne vends pas"),
    bul(rt("✗  ", { bold: true }), rt('"Création de site WordPress"')),
    bul(rt("✗  ", { bold: true }), rt('"Refonte WordPress" ou "nouveau design"')),
    bul(rt("✗  ", { bold: true }), rt('"Installation de plugins WordPress"')),
    bul(rt("✗  ", { bold: true }), rt("Du temps au tarif journalier")),
    p(""),
    h2("Ce que tu vends"),
    cal(
      "La structuration d'un système WordPress rentable et automatisé — pour que ton site devienne un actif business réel, pas une charge technique.",
      "🎯", "green_background"
    ),
    p(""),
    h2("Les 3 versions du pitch"),
    tog("📝 Pitch court (15 secondes)", [
      p(""),
      qot("J'aide les freelances, formateurs et créateurs qui font déjà du CA à transformer leur WordPress en système business cohérent, automatisé et rentable."),
    ]),
    tog("📝 Pitch moyen (45 secondes)", [
      p(""),
      qot("La plupart des freelances et formateurs qui font déjà du chiffre ont un WordPress bricolé : plugins empilés, CRM inexistant, tunnel bancal, automatisation absente. Ça génère des pertes invisibles. J'arrive avec une approche architecte : audit du système existant, simplification du stack, implémentation cohérente, automatisation intelligente. En 6 à 8 semaines, le site cesse d'être une charge et devient un levier de CA."),
    ]),
    tog("📝 Pitch long — page offre (pour le site SASU)", [
      p(""),
      p("Tu fais déjà du chiffre. Ton WordPress existe. Mais quelque chose bloque :"),
      p(""),
      bul("Ton tunnel perd des prospects que tu as payés à acquérir"),
      bul("Ton CRM ne segmente rien — tu relances tout le monde pareil"),
      bul("Tes automatisations sont inexistantes ou cassées"),
      bul("Tu passes trop de temps sur du support technique qui devrait être automatique"),
      bul("Tu sais que ton système est bricolé, mais tu ne sais pas par où commencer"),
      p(""),
      p("Le WordPress Business System™ est une transformation complète, pas une maintenance."),
      p("En 6 à 8 semaines :"),
      p(""),
      bul("On audite l'existant et on identifie exactement où fuit la valeur"),
      bul("On construit l'architecture système cohérente (LMS, CRM, tunnel, automatisation)"),
      bul("On implémente les outils retenus avec une logique business, pas juste technique"),
      bul("On installe les indicateurs et on te transmet le système en autonomie"),
      p(""),
      qot("Résultat : un site WordPress qui travaille pour toi — pas l'inverse."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // CIBLE IDÉALE
  // ───────────────────────────────────────────
  blocks.push(
    h1("1️⃣ Cible Idéale — Le Client Parfait"),
    cal(
      "Pas les débutants. Pas les budgets à 800 €. Des gens qui font déjà du CA et se sentent bloqués par leur système.",
      "🎯", "yellow_background"
    ),
    p(""),

    h2("Profil du client idéal"),
    bul(rt("Freelance, formateur, créateur ou solopreneur", { bold: true })),
    bul("A déjà un site WordPress en production"),
    bul("Fait déjà du chiffre (CA > 30 000 €/an minimum)"),
    bul("Se sent limité techniquement — WordPress le freine, pas le libère"),
    bul("Manque d'automatisation : trop de tâches manuelles répétitives"),
    bul("A un système bricolé : plugins en doublon, CRM inexistant, tunnel approximatif"),
    bul("Comprend la valeur d'investir dans un système — pas juste dans un « site »"),
    p(""),

    h2("Signaux d'alarme — Client à éviter"),
    bul(rt("Budget < 1 500 €", { bold: true }), rt(" — l'audit seul n'est pas rentable pour lui")),
    bul(rt("Veux un « beau site »", { bold: true }), rt(" — cherche un graphiste, pas un architecte système")),
    bul(rt("Débutant sans CA existant", { bold: true }), rt(" — rien à optimiser, pas de ROI démontrable")),
    bul(rt("Veut tout décider techniquement", { bold: true }), rt(" — ne fait pas confiance aux recommandations d'architecture")),
    bul(rt("Refuse l'audit initial", { bold: true }), rt(" — on ne peut pas construire sans comprendre l'existant")),
    p(""),

    h2("Les 5 questions de qualification"),
    ...QUALIF_QUESTIONS.map((q) =>
      tog(`❓ ${q.q}`, [
        p(""),
        p(rt("Objectif : ", { bold: true }), rt(q.but)),
      ])
    ),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // STRUCTURE 4 PHASES
  // ───────────────────────────────────────────
  blocks.push(
    h1("2️⃣ Structure de l'Offre — 4 Phases"),
    cal(
      "6 à 8 semaines. Phases séquentielles. Chaque phase valide la suivante — on ne construit pas sans comprendre, on n'optimise pas sans construire.",
      "🏗", "blue_background"
    ),
    p("")
  );

  for (const phase of PHASES) {
    blocks.push(
      h2(`Phase ${phase.num} — ${phase.emoji} ${phase.titre}`),
      p(rt("Durée estimée : ", { bold: true }), rt(phase.duree, { italic: true })),
      p(""),
      p(phase.description),
      p(""),
      h3("Livrables inclus"),
      ...phase.livrables.map((l) => bul(l)),
      p(""),
      p(rt("Livrable final : ", { bold: true }), rt(phase.livrable_final)),
      p(""),
      tog("💡 Note stratégique", [
        p(""),
        p(phase.note),
      ]),
      p("")
    );
  }

  blocks.push(div());

  // ───────────────────────────────────────────
  // PRICING
  // ───────────────────────────────────────────
  blocks.push(
    h1("3️⃣ Pricing Premium"),
    cal(
      "Si tu te positionnes « architecte système », tu ne dois pas être sous 3 000 €. La valeur ne se justifie pas par les heures — elle se justifie par le résultat.",
      "💰", "orange_background"
    ),
    p(""),

    h2("Les 3 niveaux"),
    p(""),

    tog("🥉 Audit Stratégique Seul — 900 à 1 500 €", [
      p(""),
      p(rt("Ce que comprend l'audit :", { bold: true })),
      bul("Phase 1 complète : audit architecture, tunnel, CRM, performance, logique business"),
      bul("Rapport stratégique 20–30 pages"),
      bul("Plan d'action priorisé par ROI"),
      bul("1 appel de restitution (1h)"),
      p(""),
      p(rt("À qui ça s'adresse :", { bold: true })),
      bul("Prospect qui veut valider avant de s'engager sur le projet complet"),
      bul("Client qui a les ressources pour implémenter lui-même mais veut la vision"),
      bul("Porte d'entrée vers le WBS Standard ou Premium"),
      p(""),
      p(rt("Règle : ", { bold: true }), rt("L'audit impute sur le projet si le client monte en WBS Standard dans les 60 jours.")),
    ]),

    p(""),

    tog("🥈 WBS Standard — Architecture + Implémentation Partielle — 3 000 à 6 000 €", [
      p(""),
      p(rt("Ce que comprend le WBS Standard :", { bold: true })),
      bul("Phase 1 — Audit complet (inclus)"),
      bul("Phase 2 — Architecture système (schéma + documentation)"),
      bul("Phase 3 — Implémentation sur 1 à 2 modules clés (ex : CRM + tunnel OU LMS + automatisation)"),
      bul("Phase 4 — KPIs de base + formation 1h"),
      p(""),
      p(rt("À qui ça s'adresse :", { bold: true })),
      bul("Client avec 1 à 2 besoins bien identifiés"),
      bul("Budget 3 000–6 000 € assumé"),
      bul("Prêt à gérer certaines parties seul après transmission"),
      p(""),
      p(rt("Durée : ", { bold: true }), rt("3 à 5 semaines")),
    ]),

    p(""),

    tog("🥇 WBS Premium — Système Complet — 7 000 à 12 000 €", [
      p(""),
      p(rt("Ce que comprend le WBS Premium :", { bold: true })),
      bul("Phases 1 à 4 complètes sans limitation de périmètre"),
      bul("Implémentation multi-modules (LMS + CRM + tunnel + automatisation + performance)"),
      bul("Tests de bout en bout complets"),
      bul("Formation client 2h + documentation utilisateur"),
      bul("Roadmap 6 mois avec priorisation ROI"),
      bul("1 mois de support inclus post-livraison"),
      p(""),
      p(rt("À qui ça s'adresse :", { bold: true })),
      bul("Formateur ou créateur avec stack complexe à transformer complètement"),
      bul("Client qui migre depuis un SaaS (Kajabi, Teachable, etc.)"),
      bul("Budget > 7 000 € assumé, ROI clair identifié en Phase 1"),
      p(""),
      p(rt("Durée : ", { bold: true }), rt("6 à 8 semaines")),
    ]),

    p(""),

    h2("Maintenance WBS mensuelle"),
    bul(rt("Starter — 400 €/mois : ", { bold: true }), rt("monitoring performance, mises à jour, 2h support")),
    bul(rt("Expert — 700 €/mois : ", { bold: true }), rt("Starter + optimisations continues, rapport mensuel")),
    bul(rt("Premium — 1 000 €/mois : ", { bold: true }), rt("Expert + interventions prioritaires + roadmap active")),
    p(""),
    qot("La maintenance est proposée à la fin de chaque projet WBS. C'est le MRR naturel de l'offre."),
    p(""),

    h2("Calcul de valeur pour le client"),
    tog("📊 Exemple — Formateur à 50 000 €/an CA", [
      p(""),
      bul("CA mensuel moyen : 4 200 €"),
      bul("Estimation fuites actuelles (tunnel + relances + CRM) : 20–25 % = 840 à 1 050 €/mois perdus"),
      bul("Économie SaaS potentielle (Kajabi → WordPress) : 300 à 600 €/mois"),
      bul(rt("Gain total mensuel après WBS : 1 100 à 1 600 €/mois", { bold: true })),
      p(""),
      bul("Coût WBS Standard (5 000 €) : amorti en 3 à 5 mois"),
      bul("Coût WBS Premium (9 000 €) : amorti en 6 à 8 mois"),
      p(""),
      qot("Ratio valeur/prix > 5× sur 12 mois. Le projet se justifie business avant de se justifier techniquement."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PROMESSE CLAIRE
  // ───────────────────────────────────────────
  blocks.push(
    h1("4️⃣ La Promesse"),
    p(""),
    cal(
      "En 6 à 8 semaines, tu structures un système WordPress clair, automatisé et orienté conversion — pour que ton site devienne un actif business réel, pas une charge technique permanente.",
      "✅", "green_background"
    ),
    p(""),

    h2("Ce que signifie « actif business réel »"),
    bul("Il génère des leads ou des ventes sans ton intervention manuelle quotidienne"),
    bul("Il qualifie et relance tes prospects automatiquement"),
    bul("Il onboarde tes clients sans que tu aies à envoyer les accès à la main"),
    bul("Il te donne des données (conversions, trafic, CA par source) en temps réel"),
    bul("Il évolue avec toi — il n'est pas obsolète dans 6 mois"),
    p(""),

    h2("Ce que la promesse n'est pas"),
    bul(rt("✗  ", { bold: true }), rt('"Je double ton CA en 8 semaines" — ce n'est pas honnête')),
    bul(rt("✗  ", { bold: true }), rt('"Je garantis X leads par mois" — dépend trop du marché et du contenu')),
    bul(rt("✗  ", { bold: true }), rt('"Ton site sera parfait" — il sera solide, évolutif, cohérent')),
    p(""),
    qot("La promesse : un système structuré, transmis, mesurable. Le reste, c'est ton business — pas le mien."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // CE QUI REND L'OFFRE PREMIUM
  // ───────────────────────────────────────────
  blocks.push(
    h1("5️⃣ Ce qui Rend l'Offre Premium"),
    p(""),

    h2("Les 6 marqueurs de valeur premium"),
    bul(rt("Diagnostic profond d'abord", { bold: true }), rt(" — on ne construit rien sans comprendre l'existant. Beaucoup sautent cette étape.")),
    bul(rt("Vision stratégique", { bold: true }), rt(" — chaque décision technique a une justification business explicite.")),
    bul(rt("Simplification avant optimisation", { bold: true }), rt(" — on enlève les outils inutiles avant d'en ajouter de nouveaux.")),
    bul(rt("Pas de sur-outillage", { bold: true }), rt(" — on utilise le minimum nécessaire, pas le maximum disponible.")),
    bul(rt("Orientation long terme", { bold: true }), rt(" — livrable + roadmap 6 mois + documentation. Pas du one-shot.")),
    bul(rt("Formation client intégrée", { bold: true }), rt(" — le client prend le système en main, il n'est pas dépendant.")),
    p(""),

    h2("La différence avec un freelance WordPress classique"),
    tog("📊 Comparatif — Freelance classique vs WordPress Business System™", [
      p(""),
      p(rt("Freelance classique", { bold: true })),
      bul("Démarre par le design ou les plugins"),
      bul("Livre un site — sans documentation, sans formation"),
      bul("Pricing à la journée ou au devis approximatif"),
      bul("Aucune vision sur le ROI du projet"),
      bul("Disponible pour des corrections isolées"),
      p(""),
      p(rt("WordPress Business System™", { bold: true })),
      bul("Démarre par l'audit — comprend avant de construire"),
      bul("Livre un système — avec documentation, formation, roadmap"),
      bul("Pricing à la valeur transformée — pas aux heures"),
      bul("ROI estimé dès la Phase 1, avant engagement"),
      bul("Maintenance stratégique en MRR, pas du support réactif"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DIFFÉRENCIATION
  // ───────────────────────────────────────────
  blocks.push(
    h1("6️⃣ Différenciation Forte"),
    p(""),

    h2("Ce que vend la majorité du marché"),
    bul(rt("Design & refonte : ", { bold: true }), rt('"Votre site sera beau et moderne"')),
    bul(rt("SEO technique : ", { bold: true }), rt('"Je vais optimiser votre référencement"')),
    bul(rt("Maintenance : ", { bold: true }), rt('"Je mets à jour vos plugins chaque mois"')),
    bul(rt("Installation LMS/CRM : ", { bold: true }), rt('"Je configure l'outil que vous avez choisi"')),
    p(""),

    h2("Ce que tu vends"),
    bul(rt("Architecture business WordPress : ", { bold: true }), rt("comment les pages, les outils et les flux se connectent pour générer du CA")),
    bul(rt("Automatisation intelligente : ", { bold: true }), rt("pas des Zapier bricolés — des systèmes documentés et testés")),
    bul(rt("Cohérence système : ", { bold: true }), rt("tout ce qui est installé a une raison d'être et une connexion logique")),
    bul(rt("Vision ROI : ", { bold: true }), rt("chaque intervention est justifiée par un gain business estimé")),
    p(""),

    qot("Tu ne vends pas des heures de WordPress. Tu vends un système qui travaille pour le client — même quand lui ne travaille pas."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // OBJECTIONS
  // ───────────────────────────────────────────
  blocks.push(
    h1("7️⃣ Objections et Réponses"),
    p("")
  );

  for (const obj of OBJECTIONS) {
    blocks.push(
      tog(`💬 "${obj.objection}"`, [
        p(""),
        p(rt("Ta réponse :", { bold: true })),
        p(""),
        qot(obj.reponse),
      ])
    );
  }

  blocks.push(p(""), div());

  // ───────────────────────────────────────────
  // ALIGNEMENT AVEC LE PROFIL
  // ───────────────────────────────────────────
  blocks.push(
    h1("8️⃣ Pourquoi Cette Offre est Alignée avec Ton Profil"),
    cal(
      "Cette offre n'est pas inventée. Elle est l'expression naturelle de ce que tu maîtrises déjà — schoolsWP en est la preuve publique.",
      "⚡", "purple_background"
    ),
    p(""),

    h2("Les 5 compétences qui font le WBS™"),
    bul(rt("schoolsWP — autorité pédagogique : ", { bold: true }), rt("tu parles la langue de tes clients avant même le premier appel")),
    bul(rt("Maîtrise FluentCRM : ", { bold: true }), rt("CRM WordPress natif — tu connais ses limites ET son potentiel")),
    bul(rt("Vision automatisation (n8n) : ", { bold: true }), rt("tu penses en flux et en déclencheurs, pas en actions isolées")),
    bul(rt("Approche systémique : ", { bold: true }), rt("tu raisonnes en architecture, pas en liste de fonctionnalités")),
    bul(rt("Logique long terme : ", { bold: true }), rt("tu livres avec documentation et roadmap — pas du one-shot")),
    p(""),

    h2("Comment schoolsWP alimente le WBS™"),
    bul("Chaque article SEO décisionnel démontre ta compréhension du système business"),
    bul("Les comparatifs LMS / CRM prouvent que tu connais les outils de tes clients"),
    bul("Les articles d'architecture système montrent ta vision — avant même l'appel découverte"),
    bul("Le prospect arrive en confiance — il a lu tes analyses, il connaît ta voix"),
    p(""),
    qot("schoolsWP est ton plus beau commercial. Il travaille 24h/24, sans commission."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DASHBOARD ACTIONS
  // ───────────────────────────────────────────
  blocks.push(
    h1("📋 Plan d'Action — Lancement de l'Offre"),
    p(""),

    h2("🔧 Semaine 1 — Structure de l'offre"),
    tod("Finaliser le nom définitif (WordPress Business System™ ou autre)"),
    tod("Rédiger la page offre SASU complète basée sur ce document"),
    tod("Créer le template d'audit Phase 1 (Notion ou PDF structuré)"),
    tod("Fixer les 3 tarifs définitifs et les inscrire dans les CGV"),
    tod("Préparer la grille de qualification prospect (5 questions)"),
    p(""),

    h2("📞 Semaine 2 — Process commercial"),
    tod("Configurer Cal.com avec formulaire pré-appel (5 questions de qualification)"),
    tod("Rédiger le script d'appel découverte (30 min — 5 étapes)"),
    tod("Préparer le deck de présentation WBS™ (5 slides max)"),
    tod("Créer le template de proposition commerciale (Notion ou PDF)"),
    tod("Définir les conditions d'acompte (50 % à la signature)"),
    p(""),

    h2("🚀 Semaine 3 — Premier lancement"),
    tod("Annoncer l'offre sur LinkedIn (post de positionnement — pas de vente)"),
    tod("Publier le premier article schoolsWP lié au WBS (architecture système)"),
    tod("Activer le CTA Audit dans les articles schoolsWP existants"),
    tod("Proposer 1 audit test à 750 € (contre témoignage + étude de cas)"),
    tod("Planifier la revue de l'offre à M+3 (pricing, message, qualification)"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // VISION
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧩 Vision — L'Offre dans 12 Mois"),
    p(""),
    tog("📌 État cible M12 — WordPress Business System™", [
      p(""),
      bul("4 à 6 missions WBS réalisées (Audit / Standard / Premium)"),
      bul("CA moyen par mission : 5 000 à 8 000 € à M6 → 8 000 à 12 000 € à M12"),
      bul("3 à 5 clients en maintenance WBS (MRR 1 200 à 5 000 €/mois)"),
      bul("1 à 2 études de cas publiées sur schoolsWP avec résultats mesurés"),
      bul("0 démarchage — 100 % inbound via schoolsWP + recommandations"),
      bul("Tarif audit : 1 500 € non négociable dès M3"),
      p(""),
      p(rt("CA SASU objectif Année 1 : 45 000 à 65 000 €", { bold: true })),
      p(rt("MRR maintenance objectif M12 : 2 000 à 4 000 €/mois", { bold: true })),
    ]),
    p(""),
    cal(
      "Le WordPress Business System™ n'est pas une offre de services. C'est une promesse de transformation. Et schoolsWP en est la preuve publique permanente.",
      "🔥", "red_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page WordPress Business System™ — Offre Signature...");

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
    icon: { type: "emoji", emoji: "🔥" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🔥 WordPress Business System™ — Offre Signature" } },
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
  console.log("   🎯  Positionnement — 3 versions du pitch (15s / 45s / page offre)");
  console.log("   1️⃣  Cible Idéale — ICP + signaux d'alarme + 5 questions qualif.");
  console.log("   2️⃣  Structure 4 Phases — Audit → Architecture → Implémentation → Optimisation");
  console.log("   3️⃣  Pricing Premium — 3 niveaux + maintenance + calcul ROI client");
  console.log("   4️⃣  La Promesse — ce qu'elle est, ce qu'elle n'est pas");
  console.log("   5️⃣  Ce qui Rend l'Offre Premium — 6 marqueurs + comparatif freelance");
  console.log("   6️⃣  Différenciation — vs design / SEO / maintenance / installation");
  console.log(`   7️⃣  ${OBJECTIONS.length} Objections + Réponses (toggles)`);
  console.log("   8️⃣  Alignement Profil — schoolsWP + FluentCRM + n8n + vision systémique");
  console.log("   📋  Plan d'Action 3 semaines (checkboxes)");
  console.log("   🧩  Vision M12 — CA, MRR, positionnement cible");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

#!/usr/bin/env node
/**
 * setup-notion-offer-signature-exact.js
 * Crée la page "Offre Signature Exacte — WordPress Business System™" dans Notion.
 * Document opérationnel : pitch · process commercial · templates · qualification.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-offer-signature-exact.js
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
// Données
// ---------------------------------------------------------------------------

const PHASES = [
  {
    num: "1", emoji: "🔍", nom: "Audit Stratégique",
    accroche: "Comprendre avant de construire. Identifier exactement où fuit la valeur.",
    duree: "3 à 5 jours",
    prix_seul: "800 à 1 500 €",
    livrables: [
      "Audit architecture WordPress — plugins, stack, dette technique, dépendances",
      "Analyse SEO technique — vitesse, Core Web Vitals, maillage, indexation",
      "Analyse CRM / email — segmentation, séquences, fuites d'automatisation",
      "Analyse conversion — tunnel, landing, checkout, abandon, friction",
      "Plan d'optimisation priorisé par ROI — les 5 actions à impact maximal",
    ],
    promesse: "À l'issue de l'audit, tu sais exactement ce qui coûte et ce qui rapporte dans ton système WordPress. Pas d'intuition — des données.",
    note_vente: "L'audit peut être vendu seul. Il s'impute sur la mission complète si le client continue dans les 60 jours. C'est la porte d'entrée naturelle — jamais de mission sans audit préalable.",
  },
  {
    num: "2", emoji: "🏗", nom: "Structuration Système",
    accroche: "Simplifier d'abord. Pas 15 outils — un système cohérent.",
    duree: "1 à 3 semaines selon périmètre",
    prix_seul: null,
    livrables: [
      "Simplification du stack — suppression des doublons, unification des flux",
      "Mise en place CRM (FluentCRM ou WP Fusion) — pipelines, tags, séquences",
      "Automatisation emails — onboarding, relances, notifications transactionnelles",
      "Tunnel de conversion — landing optimisée, checkout friction-free, post-achat",
      "Optimisation performance — cache, images, Core Web Vitals, CDN si pertinent",
    ],
    promesse: "Le système est clair, documenté, cohérent. Chaque outil a une raison d'être. Rien d'inutile, rien qui manque.",
    note_vente: "Le périmètre est défini précisément en Phase 1. Pas d'improvisation, pas d'élargissement de scope sans avenant signé.",
  },
  {
    num: "3", emoji: "📈", nom: "Optimisation & Montée en Puissance",
    accroche: "Un système livré sans optimisation continue, c'est un actif qui se déprécie.",
    duree: "1 semaine + roadmap 6 mois",
    prix_seul: null,
    livrables: [
      "Amélioration conversion — A/B test CTA, formulaires, preuves sociales",
      "Structuration contenu — maillage interne stratégique, clusters SEO en cours",
      "Stratégie upsell / cross-sell — logique produit + déclencheurs automatiques",
      "Automatisation avancée — segmentation comportementale, scoring, réactivation",
      "Roadmap 6 mois — prochaines optimisations priorisées par ROI estimé",
      "Formation client 2h — prise en main autonome du système livré",
    ],
    promesse: "Le client ne dépend pas de toi pour faire vivre le système. Il a les clés, la roadmap et l'autonomie.",
    note_vente: "Cette phase ouvre naturellement vers la maintenance mensuelle. La roadmap 6 mois crée le besoin de suivi — sans pitch agressif.",
  },
];

const NIVEAUX_PRIX = [
  {
    niveau: "Audit seul",
    emoji: "🔍",
    fourchette: "800 à 1 500 €",
    contenu: "Phase 1 complète — rapport 20–30 pages + plan d'action + call de restitution 1h",
    pour_qui: "Prospect qui veut valider avant de s'engager sur la mission complète. Client autonome qui a les ressources pour implémenter.",
    upsell: "Imputable sur la mission complète (Phase 1 + 2) dans les 60 jours",
    signal_client: "Budget prudent ou besoin de clarté avant investissement — profil courant en M1-M3",
  },
  {
    niveau: "Mission structuration",
    emoji: "🏗",
    fourchette: "3 000 à 6 000 €",
    contenu: "Phases 1 + 2 complètes — audit + architecture + implémentation 1 à 2 modules",
    pour_qui: "Client avec 1 à 2 besoins clairement identifiés. Budget 3–6k€ assumé.",
    upsell: "Phase 3 + maintenance mensuelle proposée en fin de mission",
    signal_client: "Profil WBS Standard — le cœur de l'offre en An1",
  },
  {
    niveau: "Système complet",
    emoji: "🚀",
    fourchette: "6 000 à 8 000 €",
    contenu: "Phases 1 + 2 + 3 complètes — multi-modules + tests bout en bout + formation + roadmap",
    pour_qui: "Formateur ou créateur avec stack complexe. Migration Kajabi → WordPress. Budget > 6k€.",
    upsell: "Maintenance Premium 700–900 €/mois proposée systématiquement",
    signal_client: "Profil WBS Premium — cible M6+ quand le positionnement est affirmé",
  },
  {
    niveau: "Accompagnement mensuel",
    emoji: "🔄",
    fourchette: "1 000 à 2 000 €/mois",
    contenu: "Suivi stratégique mensuel — optimisations continues, rapport, support prioritaire, 4h d'intervention/mois",
    pour_qui: "Client post-mission qui veut garder le système à jour et en croissance",
    upsell: "Pas d'upsell — c'est le MRR. L'objectif est de garder 5 à 8 clients actifs.",
    signal_client: "Proposer systématiquement en fin de chaque mission — taux d'acceptation cible > 50 %",
  },
];

const QUALIF_GRILLE = [
  { critere: "CA actuel", bon: "> 30 000 €/an", mauvais: "< 15 000 €/an ou pas de CA", poids: "Éliminatoire" },
  { critere: "WordPress existant", bon: "Site WordPress en production depuis > 6 mois", mauvais: "Projet from scratch sans base existante", poids: "Important" },
  { critere: "Problème identifié", bon: "Sait ce qui bloque (tunnel, CRM, performance)", mauvais: "Veut « un beau site » sans autre objectif", poids: "Éliminatoire" },
  { critere: "Budget", bon: "> 1 500 € pour l'audit, > 3 000 € pour la mission", mauvais: "< 800 €, ou en attente d'un devis au plus bas", poids: "Éliminatoire" },
  { critere: "Autonomie", bon: "Comprend la valeur d'un système, pas juste d'un prestataire", mauvais: "Veut tout déléguer sans comprendre, micromanage", poids: "Important" },
  { critere: "Horizon", bon: "Pense ROI sur 6–12 mois, pas résultat immédiat", mauvais: "Attend un résultat en 2 semaines", poids: "Important" },
];

const CALL_SCRIPT = [
  {
    etape: "1", duree: "5 min", titre: "Connexion & cadre",
    contenu: [
      "Confirmer la durée (30 min) et l'objectif : comprendre si et comment je peux t'aider",
      "Poser 1 question d'ouverture : « Qu'est-ce qui t'a amené à demander cet appel aujourd'hui ? »",
      "Laisser parler — ne pas couper. Prendre des notes sur les mots exacts utilisés.",
    ],
    piege: "Ne pas pitcher l'offre dans les 5 premières minutes.",
  },
  {
    etape: "2", duree: "10 min", titre: "Diagnostic",
    contenu: [
      "« Tu utilises quoi comme CRM et comme outil email en ce moment ? »",
      "« Qu'est-ce qui te prend le plus de temps manuellement sur WordPress ? »",
      "« Si tu devais identifier le 1 truc qui te coûte le plus de CA, ce serait quoi ? »",
      "« C'est quoi ton objectif principal pour les 6 prochains mois ? »",
    ],
    piege: "Ne pas donner de solution pendant le diagnostic — juste écouter et confirmer.",
  },
  {
    etape: "3", duree: "8 min", titre: "Qualification & budget",
    contenu: [
      "« Tu as déjà investi dans ton WordPress ou c'est la première fois ? »",
      "« Quel budget tu envisages pour structurer ça sérieusement ? »",
      "Écouter sans réagir. Si hors budget → orienter vers un audit seul ou la page schoolsWP.",
      "Si budget OK → annoncer le périmètre possible et le prix approximatif de l'audit.",
    ],
    piege: "Ne pas baisser le prix à la moindre hésitation. Rester ferme, proposer l'audit comme alternative.",
  },
  {
    etape: "4", duree: "5 min", titre: "Présentation de la suite",
    contenu: [
      "Si qualifié : « Ce que je propose, c'est de commencer par un audit pour avoir une vision exacte de ce qui freine et de ce qui peut rapporter. »",
      "Annoncer le prix de l'audit (800–1 500 €) et le format (rapport + call restitution)",
      "Annoncer le délai : audit livré en 5 jours ouvrés après signature",
    ],
    piege: "Ne pas proposer la mission complète sans avoir fait l'audit. L'audit qualifie ET justifie le projet.",
  },
  {
    etape: "5", duree: "2 min", titre: "Suite concrète",
    contenu: [
      "« Est-ce que ça fait sens pour toi qu'on démarre par l'audit ? »",
      "Si oui → envoyer le devis audit dans les 2h avec lien de signature et lien de paiement",
      "Si hésitation → « Qu'est-ce qui te fait hésiter ? » — répondre à l'objection une fois seulement",
      "Si non → remercier, envoyer un lien vers schoolsWP, ne pas insister",
    ],
    piege: "Ne pas relancer plus de 2 fois. Un prospect qui hésite 3 fois n'est pas prêt.",
  },
];

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE
  blocks.push(
    cal(
      "Document opérationnel — Offre signature exacte. Pitch, phases, pricing, qualification, script d'appel, templates. Tout ce qu'il faut pour vendre sans improviser.",
      "🎯", "red_background"
    ),
    p(rt("Mis à jour : mars 2026 · Version 1.0 — À affiner après les 3 premières missions", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // POSITIONNEMENT — LA LIGNE ROUGE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🎯 Le Positionnement — La Ligne Rouge"),
    p(""),

    h2("Ce que tu n'es pas"),
    bul(rt("✗  ", { bold: true }), rt('"Créateur de sites WordPress"  — 80 % du marché. Concurrence maximale. Tarifs bas.')),
    bul(rt("✗  ", { bold: true }), rt('"Freelance WordPress disponible"  — position d'attente, pas de positionnement')),
    bul(rt("✗  ", { bold: true }), rt('"Développeur WordPress"  — technique pur, sans vision business')),
    bul(rt("✗  ", { bold: true }), rt('"Agence digitale WordPress"  — trop large, trop flou, trop concurrentiel')),
    p(""),

    h2("Ce que tu es — la seule formulation acceptable"),
    cal(
      "Je structure les systèmes WordPress pour qu'ils génèrent plus de clarté, plus d'automatisation et plus de rentabilité.",
      "🎯", "green_background"
    ),
    p(""),
    bul(rt("Tu es un architecte système", { bold: true }), rt(", pas un exécutant")),
    bul(rt("Tu penses en ROI", { bold: true }), rt(", pas en heures")),
    bul(rt("Tu livres de la transformation", { bold: true }), rt(", pas du design")),
    bul(rt("Tu travailles avec des gens qui font déjà du CA", { bold: true }), rt(", pas des débutants")),
    p(""),

    h2("L'équation de positionnement"),
    tog("📐 Pourquoi « architecte système » est supérieur à « créateur de site »", [
      p(""),
      p(rt("Créateur de site :", { bold: true })),
      bul("Prestation one-shot · Pas de récurrence naturelle · Concurrence sur le prix"),
      bul("Le client compare 3 devis · Critère principal : le moins cher"),
      bul("Le résultat est subjectif (« beau » ou « pas beau »)"),
      p(""),
      p(rt("Architecte système WordPress :", { bold: true })),
      bul("Transformation avec ROI mesurable · Récurrence naturelle (maintenance) · Expertise rare"),
      bul("Le client ne compare pas — il cherche LE bon profil · Critère : crédibilité et résultats"),
      bul("Le résultat est objectif (CA, conversion, automatisation mesurée)"),
      p(""),
      qot("La question n'est pas « combien tu coûtes ? » mais « est-ce que tu peux m'aider ? » — ce deuxième dialogue est infiniment plus confortable."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // L'OFFRE — 3 PHASES
  // ───────────────────────────────────────────
  blocks.push(
    h1("🏗 Structure de l'Offre — 3 Phases"),
    cal(
      "L'offre n'est pas un menu de services. C'est un processus en 3 actes : comprendre → construire → optimiser. On ne saute pas d'étape.",
      "🏗", "blue_background"
    ),
    p("")
  );

  for (const phase of PHASES) {
    blocks.push(
      h2(`Phase ${phase.num} — ${phase.emoji} ${phase.nom}`),
      p(rt("Durée : ", { bold: true }), rt(phase.duree, { italic: true })),
      phase.prix_seul ? p(rt("Vendable seule : ", { bold: true }), rt(phase.prix_seul)) : p(""),
      p(""),
      p(rt("Accroche interne : ", { bold: true }), rt(phase.accroche, { italic: true })),
      p(""),
      h3("Livrables"),
      ...phase.livrables.map((l) => bul(l)),
      p(""),
      p(rt("Promesse client : ", { bold: true }), rt(phase.promesse)),
      p(""),
      tog("💡 Note de vente", [
        p(""),
        p(phase.note_vente),
      ]),
      p("")
    );
  }

  blocks.push(div());

  // ───────────────────────────────────────────
  // PRICING — 4 NIVEAUX
  // ───────────────────────────────────────────
  blocks.push(
    h1("💰 Pricing — 4 Niveaux"),
    cal(
      "Tu n'es pas un exécutant. Tu es un architecte. Le prix reflète la valeur transformée, pas le temps passé.",
      "💰", "orange_background"
    ),
    p("")
  );

  for (const n of NIVEAUX_PRIX) {
    blocks.push(
      tog(`${n.emoji}  ${n.niveau} — ${n.fourchette}`, [
        p(""),
        p(rt("Ce qui est inclus :", { bold: true })),
        p(n.contenu),
        p(""),
        p(rt("Pour qui :", { bold: true })),
        p(n.pour_qui),
        p(""),
        p(rt("Upsell naturel : ", { bold: true }), rt(n.upsell)),
        p(rt("Signal client : ", { bold: true }), rt(n.signal_client, { italic: true })),
      ])
    );
  }

  blocks.push(
    p(""),
    h2("Règles de pricing non négociables"),
    bul(rt("Règle 1 — Jamais de tarif journalier", { bold: true }), rt(" : tu vends un résultat, pas des heures. Dès qu'on parle journée, on perd le positionnement architecte.")),
    bul(rt("Règle 2 — L'audit ne descend pas sous 800 €", { bold: true }), rt(" : en dessous, ce n'est pas rentable ET ça signale que ton expertise ne vaut pas ce qu'elle vaut.")),
    bul(rt("Règle 3 — Pas de mission sans audit préalable", { bold: true }), rt(" : sans audit, tu construis sans comprendre. C'est risqué pour toi et pour le client.")),
    bul(rt("Règle 4 — La maintenance se vend à la fin de la mission, pas avant", { bold: true }), rt(" : elle doit être perçue comme le prolongement naturel, pas comme un abonnement push.")),
    bul(rt("Règle 5 — Un refus poli vaut mieux qu'un mauvais client", { bold: true }), rt(" : 1 client hors ICP à 2k€ coûte autant en temps et en stress qu'un bon client à 6k€.")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // CLIENT IDÉAL — GRILLE DE QUALIFICATION
  // ───────────────────────────────────────────
  blocks.push(
    h1("🎯 Client Idéal — Grille de Qualification"),
    p("")
  );

  blocks.push(
    h2("Le profil en une phrase"),
    cal(
      "Formateur, coach, créateur ou solopreneur qui fait déjà du CA, a un WordPress en production, et se sent bloqué par son système — pas par son marché.",
      "👤", "green_background"
    ),
    p(""),
    h2("La grille de qualification — 6 critères"),
    p("")
  );

  for (const c of QUALIF_GRILLE) {
    blocks.push(
      tog(`${c.poids === "Éliminatoire" ? "🔴" : "🟠"}  ${c.critere}`, [
        p(""),
        p(rt("✅  Bon signal : ", { bold: true }), rt(c.bon)),
        p(rt("❌  Mauvais signal : ", { bold: true }), rt(c.mauvais)),
        p(rt("Poids : ", { bold: true }), rt(c.poids, c.poids === "Éliminatoire" ? { bold: true, color: "red" } : {})),
      ])
    );
  }

  blocks.push(
    p(""),
    h2("Règle de qualification"),
    bul(rt("3 critères éliminatoires : ", { bold: true }), rt("CA trop faible, problème non identifié, budget sous le plancher → refus poli, pas de négociation")),
    bul(rt("2 critères importants défavorables : ", { bold: true }), rt("signaler le risque au client, proposer uniquement l'audit (engagement réduit)")),
    bul(rt("Tous les critères favorables : ", { bold: true }), rt("client idéal → pousser vers la mission complète WBS Standard ou Premium")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // LE PITCH — 3 FORMATS
  // ───────────────────────────────────────────
  blocks.push(
    h1("🗣 Le Pitch — 3 Formats"),
    p("")
  );

  blocks.push(
    tog("⚡ Pitch éclair — 10 secondes (elevator, networking)", [
      p(""),
      qot("J'aide les formateurs, coaches et créateurs WordPress à transformer leur système en machine à CA — automatisée et claire."),
      p(""),
      p(rt("À utiliser quand : ", { bold: true }), rt("networking, présentation rapide, biographie LinkedIn, signature email")),
      p(rt("Ne jamais dire : ", { bold: true }), rt('"Je crée des sites WordPress"')),
    ]),
    p(""),

    tog("📞 Pitch découverte — 45 secondes (premier appel, présentation)", [
      p(""),
      qot("La plupart des freelances, formateurs et créateurs qui font déjà du CA ont un WordPress qui freine plutôt qu'il n'accélère : tunnel bancal, CRM inexistant, automatisation absente, performance négligée. Je commence par un audit stratégique pour identifier exactement où fuit la valeur — puis je structure le système pour qu'il fonctionne comme un actif business, pas comme un site à maintenir."),
      p(""),
      p(rt("À utiliser quand : ", { bold: true }), rt("premier appel découverte, présentation courte, DM LinkedIn de qualification")),
      p(rt("Mesure de réussite : ", { bold: true }), rt("l'interlocuteur dit « c'est exactement mon problème »")),
    ]),
    p(""),

    tog("📄 Pitch page offre — 120 mots (site SASU, email de relance)", [
      p(""),
      p("Tu fais déjà du chiffre. Ton WordPress existe. Mais quelque chose bloque :"),
      p(""),
      bul("Ton tunnel perd des prospects que tu as payés à acquérir"),
      bul("Ton CRM ne segmente rien — tu relances tout le monde pareil"),
      bul("Tes automatisations sont inexistantes ou cassées"),
      bul("Tu passes trop de temps sur du support qui devrait être automatique"),
      p(""),
      p("Le WordPress Business System™ est une transformation en 3 phases :"),
      bul("Phase 1 — Audit stratégique : identifier ce qui freine et ce qui rapporte"),
      bul("Phase 2 — Structuration système : CRM, tunnel, automatisation, performance"),
      bul("Phase 3 — Optimisation : conversion, contenu, upsell, roadmap 6 mois"),
      p(""),
      qot("Résultat : un WordPress qui travaille pour toi — pas l'inverse."),
      p(""),
      p(rt("À utiliser quand : ", { bold: true }), rt("page offre, email de proposition, brochure PDF")),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // SCRIPT D'APPEL DÉCOUVERTE
  // ───────────────────────────────────────────
  blocks.push(
    h1("📞 Script Appel Découverte — 30 min"),
    cal(
      "L'appel découverte n'est pas un appel de vente. C'est un diagnostic. Tu qualifies autant que tu pitches. Si le profil ne colle pas, tu le dis.",
      "📞", "yellow_background"
    ),
    p("")
  );

  for (const e of CALL_SCRIPT) {
    blocks.push(
      tog(`Étape ${e.etape} — ${e.titre} (${e.duree})`, [
        p(""),
        ...e.contenu.map((c) => bul(c)),
        p(""),
        p(rt("⚠️  Piège : ", { bold: true }), rt(e.piege, { italic: true })),
      ])
    );
  }

  blocks.push(
    p(""),
    h2("Formules à avoir en tête"),
    bul(rt("Pour qualifier le budget : ", { bold: true }), rt('"Pour un projet dans cet esprit, les clients avec qui je travaille investissent généralement entre X et X €. Est-ce que c'est un budget que tu envisages ?"')),
    bul(rt("Pour une objection prix : ", { bold: true }), rt('"Je comprends. Dis-moi — si en 3 mois le système générait 500 € de plus par mois, est-ce que l'audit à 1 200 € ne serait pas rentable en 2 mois ?"')),
    bul(rt("Pour un refus poli : ", { bold: true }), rt('"Je ne pense pas être le bon profil pour ce projet. Voilà pourquoi... Mais voilà ce que tu pourrais faire à la place."')),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PIPELINE MINIMAL VIABLE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🔄 Pipeline Minimal Viable"),
    p("")
  );

  blocks.push(
    h2("Les 6 étapes du pipeline"),
    num("Article décisionnel schoolsWP (cluster CRM ou LMS) → trafic qualifié"),
    num("CTA vers audit en bas d'article → prospect remplit le formulaire de qualification"),
    num("Formulaire envoie les réponses → tu qualifies en 5 min sans appel"),
    num("Si qualifié → lien Cal.com pour appel découverte 30 min"),
    num("Appel → diagnostic → proposition audit (ou mission complète si profil fort)"),
    num("Signature + acompte 50 % → démarrage mission → étude de cas → article schoolsWP"),
    p(""),

    h2("Règles du pipeline"),
    bul(rt("Temps entre formulaire et contact : ", { bold: true }), rt("< 24h en semaine. Au-delà, le prospect se refroidit.")),
    bul(rt("Qualification avant tout : ", { bold: true }), rt("ne pas planifier d'appel pour les profils hors ICP. Répondre par email avec le pourquoi.")),
    bul(rt("Proposition dans les 24h post-appel : ", { bold: true }), rt("une proposition qui part 3 jours après l'appel perd 50 % de son impact.")),
    bul(rt("Relance max 2 fois : ", { bold: true }), rt("J+3 et J+7 après la proposition. Pas de harcèlement.")),
    bul(rt("Étude de cas obligatoire : ", { bold: true }), rt("chaque mission se termine par une demande de témoignage + étude de cas schoolsWP.")),
    p(""),

    h2("Objectifs pipeline par phase de démarrage"),
    tog("📅 M1–M3 — Pipeline en construction", [
      p(""),
      bul("2 à 4 appels découverte"),
      bul("1 à 2 audits signés"),
      bul("Objectif CA : 800 à 4 000 €"),
      bul("Priorité : valider que le pitch fonctionne et que les profils arrivent via schoolsWP"),
    ]),
    tog("📅 M4–M6 — Pipeline validé", [
      p(""),
      bul("4 à 8 appels découverte"),
      bul("2 à 3 missions WBS Standard"),
      bul("1 à 2 clients maintenance"),
      bul("Objectif CA : 8 000 à 20 000 €"),
      bul("Priorité : transformer les audits en missions complètes, démarrer le MRR"),
    ]),
    tog("📅 M7–M12 — Pipeline stable", [
      p(""),
      bul("5 à 10 appels découverte par mois"),
      bul("2 à 4 missions actives en simultané"),
      bul("3 à 6 clients maintenance (MRR 1 500 à 5 400 €/mois)"),
      bul("Objectif CA mensuel : 5 000 à 10 000 €"),
      bul("Priorité : augmenter le tarif moyen vers WBS Premium, refuser les petits budgets"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // AVANTAGE UNIQUE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🔥 Ton Avantage Unique"),
    p(""),

    h2("Ce que peu d'agences peuvent faire"),
    bul(rt("Montrer l'expertise publiquement avant le premier contact", { bold: true }), rt(" — schoolsWP est ton portfolio vivant. Avant l'appel, le prospect a déjà lu 3 de tes analyses.")),
    bul(rt("Prouver le système avec du contenu qui génère des leads", { bold: true }), rt(" — un article schoolsWP fait exactement ce que tu vas mettre en place pour ton client.")),
    bul(rt("Générer des leads SEO sans démarchage", { bold: true }), rt(" — ton pipeline est inbound. Le prospect vient à toi convaincu, pas à convaincre.")),
    bul(rt("Automatiser la qualification", { bold: true }), rt(" — le formulaire Cal.com filtre avant l'appel. Tu ne perds pas de temps avec les hors-ICP.")),
    bul(rt("Créer un actif durable", { bold: true }), rt(" — chaque article schoolsWP travaille pendant 3 à 5 ans. Une agence classique paie du Google Ads en permanence.")),
    p(""),

    h2("La preuve vivante"),
    qot("schoolsWP est la démonstration en direct de ce que tu vas structurer pour tes clients. Tu n'as pas besoin de leur expliquer ce qu'est un système WordPress rentable — tu le vis."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // LAUNCH POSTS
  // ───────────────────────────────────────────
  blocks.push(
    h1("📣 Posts de Lancement"),
    p("")
  );

  blocks.push(
    tog("LinkedIn — Annonce de lancement (J1 post-sortie)", [
      p(""),
      p("---"),
      p("Mon WordPress m'a appris quelque chose d'important."),
      p(""),
      p("Pas sur la technique. Sur le business."),
      p(""),
      p("Pendant 2 ans, j'ai construit schoolsWP — un média sur WordPress, le SEO et l'automatisation. J'ai structuré un système qui génère des leads, automatise la qualification et produit du contenu de valeur en permanence."),
      p(""),
      p("Ce système, je l'ai construit pour moi. Aujourd'hui, je le structure pour d'autres."),
      p(""),
      p("Je lance le WordPress Business System™ — pour les freelances, formateurs et créateurs qui font déjà du CA et dont le WordPress freine plutôt qu'il n'accélère."),
      p(""),
      p("Pas de création de site. Pas de refonte graphique."),
      p("De l'architecture. De l'automatisation. De la clarté."),
      p(""),
      p("Si tu te reconnais dans cette description → le lien pour un audit stratégique est dans le premier commentaire."),
      p("---"),
      p(""),
      p(rt("Hashtags : ", { bold: true }), rt("#WordPress #Automatisation #SEO #Freelance #WPTips")),
      p(rt("Note : ", { bold: true }, { italic: true }), rt("ne pas mentionner les prix dans le post — laisser la page offre faire le travail.", { italic: true })),
    ]),
    p(""),
    tog("Newsletter schoolsWP — Email de lancement", [
      p(""),
      p("Objet : J'ai quelque chose à t'annoncer"),
      p(""),
      p("Salut,"),
      p(""),
      p("Depuis quelques mois, je construis schoolsWP comme un laboratoire. Chaque article que tu lis est aussi une expérimentation sur ce qui fonctionne en SEO, en automatisation, en contenu."),
      p(""),
      p("Aujourd'hui, je franchis une étape supplémentaire."),
      p(""),
      p("Je lance le WordPress Business System™ — une offre d'architecture et d'optimisation pour les indépendants dont le WordPress freine la croissance."),
      p(""),
      p("Concrètement : audit de ton système WordPress, structuration CRM + tunnel + automatisation, optimisation performance et conversion. Le tout documenté, transmis, avec une roadmap 6 mois."),
      p(""),
      p("Si tu veux être parmi les premiers à découvrir comment ça fonctionne (et à bénéficier d'un tarif de lancement sur l'audit), réponds à cet email avec « intéressé » — je te donnerai les détails directement."),
      p(""),
      p("À bientôt,"),
      p("Michaël"),
      p("schoolsWP.com"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DASHBOARD
  // ───────────────────────────────────────────
  blocks.push(
    h1("📋 Plan d'Action — Lancement de l'Offre Exacte"),
    p(""),

    h2("🔧 Semaine 1 — Fondations"),
    tod("Enregistrer le nom « WordPress Business System™ » (vérifier dispo trademark FR)"),
    tod("Créer la page offre sur le domaine SASU (ou sous-domaine dédié)"),
    tod("Rédiger les 3 versions du pitch et les mémoriser"),
    tod("Créer le template de proposition commerciale (Notion ou PDF signable)"),
    tod("Rédiger les CGV et le contrat d'audit type"),
    p(""),

    h2("📞 Semaine 2 — Process commercial"),
    tod("Configurer Cal.com avec les 5 questions de qualification pré-remplies"),
    tod("Créer l'email de confirmation automatique post-formulaire (« j'analyse ta demande »)"),
    tod("Préparer le template d'audit livrable Phase 1 (20–30 pages Notion ou PDF)"),
    tod("Créer le lien de paiement audit sur Stripe (800 / 1 200 / 1 500 €)"),
    tod("Tester le pipeline complet de bout en bout (formulaire → appel → proposition → paiement)"),
    p(""),

    h2("🚀 Semaine 3 — Lancement"),
    tod("Publier le post LinkedIn de lancement (utiliser le template ci-dessus)"),
    tod("Envoyer l'email newsletter de lancement (template ci-dessus)"),
    tod("Activer le CTA Audit dans les 3 meilleurs articles schoolsWP"),
    tod("Proposer 1 audit test à tarif de lancement (750 €) contre témoignage + étude de cas"),
    tod("Planifier la revue de l'offre à M3 (pricing, message, objections récurrentes)"),
    p(""),
    div()
  );

  // VISION
  blocks.push(
    h1("🧩 L'Offre dans 12 Mois"),
    p(""),
    tog("📌 État cible — L'offre à maturité", [
      p(""),
      bul("4 à 6 audits WBS réalisés — chacun référencé et documenté"),
      bul("2 à 3 missions WBS Standard (3–6k€) — études de cas publiées"),
      bul("1 mission WBS Premium (6–8k€) — étude de cas flagship"),
      bul("3 à 5 clients en maintenance (400–700 €/mois) — MRR stable"),
      bul("Tarif audit revu à la hausse : 1 500 € non négociable dès M6"),
      bul("0 clients hors ICP acceptés depuis M3"),
      p(""),
      qot("Une offre signature, c'est quand tu peux décrire exactement ce que tu fais, pour qui, à quel prix, en 30 secondes — et que la réponse est toujours la même, peu importe l'interlocuteur."),
    ]),
    p(""),
    cal(
      "Le WordPress Business System™ n'est pas une liste de services. C'est une promesse de transformation — et schoolsWP en est la preuve publique permanente.",
      "🔥", "red_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Offre Signature Exacte — WordPress Business System™...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);

  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎯" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🎯 Offre Signature Exacte — WordPress Business System™" } },
        ],
      },
    },
    children: batches[0],
  });

  const pageId = page.id;
  console.log(`  ✅ Page créée : ${page.url}`);

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
  console.log("   🎯  Positionnement — la ligne rouge + équation architecte vs créateur");
  console.log("   🏗  Offre 3 phases — livrables, promesses, notes de vente");
  console.log(`   💰  Pricing 4 niveaux — ${NIVEAUX_PRIX.map((n) => n.fourchette).join(" · ")}`);
  console.log(`   🎯  Grille qualification — ${QUALIF_GRILLE.length} critères (dont ${QUALIF_GRILLE.filter((c) => c.poids === "Éliminatoire").length} éliminatoires)`);
  console.log("   🗣  Pitch 3 formats — 10s / 45s / 120 mots");
  console.log(`   📞  Script appel découverte — ${CALL_SCRIPT.length} étapes + formules`);
  console.log("   🔄  Pipeline minimal viable — 6 étapes + objectifs M1-M3/M4-M6/M7-M12");
  console.log("   🔥  Avantage unique — schoolsWP comme preuve vivante");
  console.log("   📣  Posts de lancement — LinkedIn + newsletter");
  console.log("   📋  Plan d'action 3 semaines (checkboxes)");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

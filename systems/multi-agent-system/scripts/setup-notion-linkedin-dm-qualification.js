#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;

const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ════════════════════════════════════════════════════════
//  DATA
// ════════════════════════════════════════════════════════

const PAGE = {
  titre: "💬 Script DM Qualification B2B — schoolsWP Agency",
  objectif:
    "Ouvrir une conversation naturelle → qualifier le prospect → proposer un audit stratégique. Ton : direct, pro, sans pression. On ne vend jamais. On diagnostique.",
};

const PHASES = [
  {
    num: 1,
    label: "Ouverture naturelle",
    emoji: "🧭",
    sous_titre: "Non commerciale — jamais de pitch",
    logique:
      "Le premier message doit créer une curiosité sincère, pas déclencher un réflexe de défense. Une question ouverte, pas une offre.",
    cas: [
      {
        id: "1A",
        contexte: "Après interaction — like ou commentaire sur un de tes posts",
        signal_declencheur: "Le prospect a liké ou commenté un post sur LMS/CRM/WordPress B2B",
        message:
          "Bonjour {{Prénom}},\n\nj'ai vu que vous proposez des formations pour des entreprises.\n\nPar curiosité : votre écosystème WordPress est structuré pour gérer plusieurs clients corporate (accès groupe, reporting, onboarding automatisé) ?",
        pourquoi_ca_marche:
          "Le prospect se souvient de l'interaction. La question est précise sans être invasive. Elle montre une expertise sans la vendre.",
      },
      {
        id: "1B",
        contexte: "Après une publication pertinente du prospect",
        signal_declencheur: "Le prospect a publié sur la formation B2B, les LMS, la gestion d'entreprises",
        message:
          "Bonjour {{Prénom}},\n\nvotre post sur {{sujet}} m'a interpellé.\n\nBeaucoup de formateurs B2B sous-estiment l'architecture technique derrière leurs formations.\n\nVous avez structuré votre LMS/CRM spécifiquement pour des clients entreprise ?",
        pourquoi_ca_marche:
          "Tu montres que tu as lu son contenu. La mention 'beaucoup de formateurs' crée un sentiment d'appartenance à une niche + déclenche l'auto-évaluation.",
      },
      {
        id: "1C",
        contexte: "Connexion à froid — profil ciblé",
        signal_declencheur: "Profil : formateur, coach B2B, consultant formation entreprise",
        message:
          "Bonjour {{Prénom}},\n\nje travaille avec des formateurs B2B qui utilisent WordPress pour structurer leur système LMS + CRM.\n\nJe vois que vous proposez des formations entreprise.\n\nVous avez déjà réfléchi à l'architecture technique derrière votre modèle ?",
        pourquoi_ca_marche:
          "'Je travaille avec des formateurs B2B' = preuve sociale immédiate. La question finale est ouverte et non menaçante.",
      },
    ],
    regle: "Pas de pitch. Juste une question ouverte. Le but : déclencher une réponse, pas une vente.",
  },
  {
    num: 2,
    label: "Qualification intelligente",
    emoji: "🧠",
    sous_titre: "S'il répond positivement ou montre un doute",
    logique:
      "Le prospect a répondu. Il est curieux. Tu passes en mode diagnostic — pas en mode présentation. Trois questions courtes. Une réponse courte de ta part entre chaque.",
    messages: [
      {
        ordre: "A",
        objectif: "Comprendre l'organisation actuelle",
        message:
          "Intéressant.\n\nAujourd'hui, comment vous gérez :\n– les accès multi-utilisateurs entreprise ?\n– le suivi des apprenants ?\n– les relances ou renouvellements ?",
        note: "Ces 3 points couvrent les 3 frictions principales. Il n'est pas obligé de tout répondre — ce qu'il ne dit pas est aussi informatif.",
      },
      {
        ordre: "B",
        objectif: "Identifier le stack actuel",
        message: "Vous utilisez quoi actuellement comme stack ?",
        note: "Simple. Direct. Sa réponse révèle son niveau de maturité technique et son budget implicite.",
      },
    ],
    objectifs_cache: [
      "Comprendre la maturité système du prospect",
      "Identifier la friction principale (LMS, CRM, onboarding, reporting)",
      "Détecter la complexité perçue vs réelle",
    ],
  },
  {
    num: 3,
    label: "Diagnostic léger",
    emoji: "🔍",
    sous_titre: "Après ses réponses — reformuler ce qu'il vient de dire",
    logique:
      "Tu reformules ce qu'il t'a dit en ajoutant une dimension qu'il n'avait pas vue. Tu montres que tu comprends son modèle mieux que lui.",
    messages: [
      {
        ordre: "A",
        objectif: "Créer la tension utile — le vrai frein visible",
        message:
          "Ce que je constate souvent chez les formateurs B2B, c'est que le vrai frein n'est pas le LMS en lui-même, mais la structuration globale (CRM + segmentation + onboarding).\n\nVous ressentez ce type de friction ?",
        note: "'Ce que je constate souvent' = tu as de l'expérience terrain. La question de confirmation lui demande juste d'acquiescer — pas de répondre longuement.",
      },
      {
        ordre: "B",
        objectif: "Repositionner le problème — si confirmation",
        message: "Ça se corrige, mais il faut penser architecture, pas plugin.",
        note: "Une ligne. Pas d'explication. Ça laisse le silence travailler. Le prospect va demander comment.",
      },
    ],
  },
  {
    num: 4,
    label: "Proposition Audit — soft",
    emoji: "🎯",
    sous_titre: "Jamais brutal. Toujours naturel. Après 3–4 échanges minimum.",
    logique:
      "Tu n'arrives pas avec une offre. Tu proposes un cadre de travail. La différence de perception est totale.",
    messages: [
      {
        ordre: "A",
        objectif: "Proposer l'audit comme prolongement logique",
        message:
          "Si ça vous intéresse, je propose un audit stratégique B2B où on analyse :\n– votre architecture actuelle\n– vos points de friction\n– les optimisations possibles\n\nC'est un échange structuré, pas un pitch commercial.",
        note: "'Pas un pitch commercial' = lever la principale objection avant qu'elle soit formulée.",
      },
      {
        ordre: "B",
        objectif: "Demander le rendez-vous",
        message: "Vous seriez ouvert à un échange de 30 minutes ?",
        note: "30 minutes = faible engagement perçu. 'Ouvert à' = pas de pression. Réponse binaire simple.",
      },
    ],
  },
  {
    num: 5,
    label: "Qualification avant call",
    emoji: "📊",
    sous_titre: "Avant de bloquer un créneau — filtrage final",
    logique:
      "Obtenir les informations clés avant l'appel pour arriver préparé et ne pas perdre 30 min sur un mauvais fit.",
    messages: [
      {
        ordre: "A",
        objectif: "Qualifier le contexte business",
        message:
          "Pour préparer au mieux l'échange,\nvous travaillez avec combien d'entreprises actuellement ?\nEt votre objectif sur les 12 prochains mois ?",
        note: "2 questions. La réponse donne : taille actuelle du portefeuille B2B + ambition (scaler ou stabiliser). Tu filtreras selon les signaux.",
      },
    ],
    ce_que_tu_filtres: [
      "Petit budget implicite ou explicite (< 2 000 €)",
      "Mauvais fit (B2C camouflé, 0 client entreprise)",
      "Too early : bon profil mais pas encore prêt",
    ],
  },
];

const SIGNAUX = {
  verts: [
    { signal: "Plusieurs clients entreprise actifs", poids: "FORT" },
    { signal: "Volonté explicite de structuration", poids: "FORT" },
    { signal: "Problème CRM ou onboarding mentionné", poids: "FORT" },
    { signal: "Cycle de vente long ou multi-décideurs", poids: "MOYEN" },
    { signal: "Stack WordPress + LMS déjà en place", poids: "MOYEN" },
  ],
  rouges: [
    { signal: "«Je débute» ou aucun client entreprise", raison: "Pas encore le bon moment" },
    { signal: "«Je veux juste un site»", raison: "Mauvaise cible — B2C ou prestation simple" },
    { signal: "Budget flou ou inférieur à 2 000 €", raison: "Pas aligné avec Phase 1 Audit" },
    { signal: "Refus de donner contexte ou monosyllabes", raison: "Engagement insuffisant — ne pas forcer" },
  ],
};

const REGLE_OR = {
  principe: "Tu ne vends jamais.",
  detail: "Tu diagnostiques. Tu éclaires. Tu qualifies.",
  objectif_final: "Le prospect doit conclure : « Il comprend mon modèle B2B mieux que moi. »",
  consequence: "C'est cette perception qui crée l'envie de travailler avec toi — pas un pitch.",
};

const BONUS_COURT = {
  label: "Version ultra-courte — DM d'amorce",
  usage: "Pour tester un profil froid sans contexte fort. Ouverture rapide, question directe.",
  message:
    "Beaucoup de formateurs B2B ont un LMS fonctionnel mais une architecture sous-optimisée.\n\nC'est votre cas ou vous avez déjà structuré CRM + onboarding + reporting ?",
  note: "2 lignes. Question fermée qui force une réponse binaire. Si 'pas encore structuré' = ouverture parfaite pour Phase 2.",
};

const TABLEAU_RECAP = [
  { phase: "Phase 1", action: "Ouverture", duree: "1 message", objectif: "Déclencher une réponse" },
  { phase: "Phase 2", action: "Qualification", duree: "2–3 échanges", objectif: "Comprendre friction + stack" },
  { phase: "Phase 3", action: "Diagnostic", duree: "1–2 échanges", objectif: "Repositionner le problème" },
  { phase: "Phase 4", action: "Proposition Audit", duree: "1 message", objectif: "Obtenir un OUI à l'appel" },
  { phase: "Phase 5", action: "Qualification call", duree: "1 message", objectif: "Filtrer avant le créneau" },
];

// ════════════════════════════════════════════════════════
//  BLOCK BUILDERS
// ════════════════════════════════════════════════════════

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text, link: opts.url ? { url: opts.url } : null },
  annotations: {
    bold: !!opts.bold,
    italic: !!opts.italic,
    code: !!opts.code,
    color: opts.color || "default",
  },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });

const p = (...parts) => ({
  object: "block",
  type: "paragraph",
  paragraph: { rich_text: parts.flat() },
});

const bul = (...parts) => ({
  object: "block",
  type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.flat() },
});

const num = (...parts) => ({
  object: "block",
  type: "numbered_list_item",
  numbered_list_item: { rich_text: parts.flat() },
});

const div = () => ({ object: "block", type: "divider", divider: {} });

const cal = (emoji, ...parts) => ({
  object: "block",
  type: "callout",
  callout: { rich_text: parts.flat(), icon: { type: "emoji", emoji } },
});

const qot = (...parts) => ({
  object: "block",
  type: "quote",
  quote: { rich_text: parts.flat() },
});

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  // ── HEADER ──────────────────────────────────────────
  blocks.push(
    cal("📌", rt("Objectif : ", { bold: true }), rt(PAGE.objectif)),
    p(
      rt("5 phases · 3 cas d'ouverture · signaux verts/rouges · règle d'or · version ultra-courte",
        { italic: true })
    ),
    div()
  );

  // ── RÉCAP TABLEAU ────────────────────────────────────
  blocks.push(
    h2("🗺 Vue d'ensemble — 5 phases"),
    p(rt("De l'ouverture au rendez-vous stratégique, sans jamais vendre :", { italic: true }))
  );

  for (const t of TABLEAU_RECAP) {
    blocks.push(
      bul(
        rt(`${t.phase} — `, { bold: true }),
        rt(`${t.action}`, { bold: true }),
        rt(`  ·  ${t.duree}  ·  `),
        rt(t.objectif, { italic: true, color: "gray" })
      )
    );
  }

  blocks.push(div());

  // ── PHASES ───────────────────────────────────────────
  for (const phase of PHASES) {
    blocks.push(
      h2(`${phase.emoji} PHASE ${phase.num} — ${phase.label}`),
      cal("💡", rt("Logique : ", { bold: true }), rt(phase.logique))
    );

    // Phase 1 : 3 cas
    if (phase.cas) {
      for (const cas of phase.cas) {
        blocks.push(
          h3(`🎯 Cas ${cas.id} — ${cas.contexte}`),
          p(
            rt("Signal déclencheur : ", { bold: true }),
            rt(cas.signal_declencheur, { italic: true, color: "gray" })
          ),
          cal("✉️", rt(cas.message)),
          p(rt("Pourquoi ça marche : ", { bold: true }), rt(cas.pourquoi_ca_marche)),
          p()
        );
      }
      blocks.push(qot(rt("Règle : ", { bold: true }), rt(phase.regle, { italic: true })));
    }

    // Phase 2 : messages A/B + objectifs
    if (phase.messages && phase.objectifs_cache) {
      p(rt(`Sous-titre : ${phase.sous_titre}`, { italic: true }));

      for (const msg of phase.messages) {
        blocks.push(
          h3(`💬 Message ${msg.ordre} — ${msg.objectif}`),
          cal("✉️", rt(msg.message)),
          p(rt("Note : ", { bold: true }), rt(msg.note, { italic: true }))
        );
      }

      blocks.push(p(), p(rt("Objectifs cachés :", { bold: true })));
      for (const obj of phase.objectifs_cache) {
        blocks.push(bul(rt("→ "), rt(obj)));
      }
    }

    // Phase 3, 4, 5 : messages uniquement
    if (phase.messages && !phase.objectifs_cache) {
      for (const msg of phase.messages) {
        blocks.push(
          h3(`💬 Message ${msg.ordre} — ${msg.objectif}`),
          cal("✉️", rt(msg.message)),
          p(rt("Note : ", { bold: true }), rt(msg.note, { italic: true }))
        );
      }
    }

    // Phase 5 : filtre
    if (phase.ce_que_tu_filtres) {
      blocks.push(p(), p(rt("Ce que tu filtres :", { bold: true })));
      for (const f of phase.ce_que_tu_filtres) {
        blocks.push(bul(rt("✗ ", { color: "red" }), rt(f)));
      }
    }

    blocks.push(div());
  }

  // ── SIGNAUX ──────────────────────────────────────────
  blocks.push(h2("🚦 Signaux verts — Qualifier pour aller plus loin"));

  for (const s of SIGNAUX.verts) {
    blocks.push(
      bul(
        rt("✅ ", { color: "green" }),
        rt(s.signal),
        rt(`  [${s.poids}]`, { italic: true, color: "gray" })
      )
    );
  }

  blocks.push(p(), h2("🚫 Signaux rouges — Stopper proprement"));

  for (const s of SIGNAUX.rouges) {
    blocks.push(
      bul(
        rt("✗ ", { color: "red" }),
        rt(`"${s.signal}"  — `, { bold: true }),
        rt(s.raison, { italic: true, color: "gray" })
      )
    );
  }

  blocks.push(div());

  // ── RÈGLE D'OR ───────────────────────────────────────
  blocks.push(
    h2("🧠 Règle d'or"),
    cal(
      "🏆",
      rt(REGLE_OR.principe + "\n\n", { bold: true }),
      rt(REGLE_OR.detail + "\n\n"),
      rt("Objectif final : ", { bold: true }),
      rt(`"${REGLE_OR.objectif_final}"\n\n`, { italic: true }),
      rt(REGLE_OR.consequence, { italic: true, color: "gray" })
    ),
    div()
  );

  // ── BONUS ────────────────────────────────────────────
  blocks.push(
    h2(`💎 Bonus — ${BONUS_COURT.label}`),
    p(rt("Usage : ", { bold: true }), rt(BONUS_COURT.usage, { italic: true })),
    cal("⚡", rt(BONUS_COURT.message, { bold: true })),
    p(rt("Note : ", { bold: true }), rt(BONUS_COURT.note))
  );

  return blocks;
}

// ════════════════════════════════════════════════════════
//  NOTION API
// ════════════════════════════════════════════════════════

async function notionRequest(method, endpoint, body) {
  const res = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Notion-Version": NOTION_VERSION,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(`Notion ${method} ${endpoint} → ${res.status}: ${JSON.stringify(err)}`);
  }
  return res.json();
}

async function main() {
  if (!NOTION_API_KEY) throw new Error("NOTION_API_KEY manquant");
  if (!NOTION_PARENT_PAGE_ID) throw new Error("NOTION_PARENT_PAGE_ID manquant");

  const allBlocks = buildTemplate();
  const chunks = [];
  for (let i = 0; i < allBlocks.length; i += CHUNK) {
    chunks.push(allBlocks.slice(i, i + CHUNK));
  }

  console.log(`📄 Création page : ${PAGE.titre}`);
  console.log(`📦 ${allBlocks.length} blocs → ${chunks.length} batch(es)`);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: NOTION_PARENT_PAGE_ID },
    properties: {
      title: { title: [{ text: { content: PAGE.titre } }] },
    },
    children: chunks[0],
  });

  console.log(`✅ Page créée : ${page.url}`);

  for (let i = 1; i < chunks.length; i++) {
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${page.id}/children`, { children: chunks[i] });
    console.log(`  ↳ Batch ${i + 1}/${chunks.length} envoyé`);
  }

  console.log(`\n🎉 Terminé — Script DM Qualification B2B créé dans Notion`);
  console.log(
    `💬 ${PHASES.length} phases · ${PHASES[0].cas.length} cas d'ouverture · signaux verts/rouges · règle d'or`
  );
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

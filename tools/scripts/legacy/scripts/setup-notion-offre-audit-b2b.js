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
  titre: "💎 L'Offre : Audit Architecture B2B",
  objectif: "Qualifier, pas convaincre. Attirer les bons profils B2B et filtrer le reste. Vendre de la clarté stratégique.",
};

const SECTIONS = [
  {
    titre: "🎯 1️⃣ Nom et Promesse",
    blocs: [
      {
        type: "cal",
        emoji: "🔎",
        texte: "Nom de l'offre : Audit Architecture WordPress B2B",
        note: "Sous-titre : Analyse stratégique de votre système LMS, CRM et automatisation pour formateurs entreprise."
      },
      {
        type: "p",
        texte: "La Promesse (sans hype ni blabla) :"
      },
      {
        type: "cal",
        emoji: "🤝",
        texte: "En 45 minutes, nous analysons votre architecture WordPress et identifions les points de friction qui limitent votre croissance B2B."
      }
    ]
  },
  {
    titre: "🧱 2️⃣ Structure de l’audit (La Méthode)",
    blocs: [
      {
        type: "p",
        texte: "Ton audit doit avoir une structure d'ingénieur :"
      },
      {
        type: "h3",
        texte: "Étape 1 — Diagnostic LMS"
      },
      {
        type: "bul",
        items: [
          "Gestion multi-entreprises",
          "Cohortes / accès groupés",
          "Reporting entreprise",
          "Expérience utilisateur corporate"
        ]
      },
      {
        type: "h3",
        texte: "Étape 2 — Diagnostic CRM"
      },
      {
        type: "bul",
        items: [
          "Segmentation B2B",
          "Pipeline devis",
          "Automatisation onboarding",
          "Relances"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🧱 2️⃣ Structure de l’audit (Suite)",
    blocs: [
      {
        type: "h3",
        texte: "Étape 3 — Tunnel & conversion"
      },
      {
        type: "bul",
        items: [
          "Parcours entreprise",
          "Qualification leads",
          "Friction commerciale",
          "CTA"
        ]
      },
      {
        type: "h3",
        texte: "Étape 4 — Restitution stratégique (Le Livrable)"
      },
      {
        type: "bul",
        items: [
          "3 points faibles critiques",
          "3 opportunités d’optimisation",
          "1 plan d'action priorisé"
        ]
      }
    ]
  },
  {
    titre: "💬 3️⃣ Script LinkedIn pour proposer l’audit",
    blocs: [
      {
        type: "p",
        texte: "À utiliser après une interaction :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Je vois que vous proposez des formations en entreprise.\nEst-ce que votre architecture WordPress est pensée pour gérer plusieurs clients corporate proprement ?",
        note: "Si réponse positive/curieuse :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Je propose un audit stratégique pour analyser précisément ce point.\nCe n’est pas un call commercial, mais un diagnostic structuré.\nSi ça vous intéresse, je peux vous envoyer les détails."
      }
    ]
  }
];
const SECTIONS_PART_3 = [
  {
    titre: "📄 4️⃣ Structure Landing Page Minimaliste",
    blocs: [
      {
        type: "h3",
        texte: "Pour qui ?"
      },
      {
        type: "bul",
        items: [
          "Formateurs vendant aux entreprises",
          "LMS WordPress existant",
          "Minimum X clients B2B",
          "Objectif : Structuration / Scalabilité"
        ]
      },
      {
        type: "h3",
        texte: "Ce que ce N'EST PAS"
      },
      {
        type: "cal",
        emoji: "🚫",
        texte: "Pas une démo de plugin.\nPas une formation.\nPas un pitch agressif."
      }
    ]
  },
  {
    titre: "💰 5️⃣ Stratégie Tarifaire & Filtrage",
    blocs: [
      {
        type: "h3",
        texte: "L'évolution du prix"
      },
      {
        type: "cal",
        emoji: "📈",
        texte: "Phase 1 (Construction d'Autorité) → Gratuit (mais fortement filtré)\nPhase 2 (Autorité installée) → 150–300 € (Déductible si le projet est signé)"
      },
      {
        type: "h3",
        texte: "Le Filtrage Indispensable (Le Formulaire)"
      },
      {
        type: "bul",
        items: [
          "CA annuel estimé ?",
          "Nombre de clients entreprise actuels ?",
          "LMS actuel ? CRM actuel ?",
          "Budget prévu pour structurer ce pôle ?"
        ]
      }
    ]
  }
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2, ...SECTIONS_PART_3];

// ════════════════════════════════════════════════════════
//  BLOCK BUILDERS
// ════════════════════════════════════════════════════════

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (t) => ({ object: "block", type: "paragraph", paragraph: { rich_text: [rt(t)] } });
const bul = (t) => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: [rt(t)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, t, note) => {
  const parts = [rt(t, { bold: true })];
  if (note) {
    parts.push(rt("\n\n" + note, { italic: true, color: "gray" }));
  }
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  blocks.push(
    cal("🎯", PAGE.objectif),
    p(""),
    div()
  );

  for (const section of ALL_SECTIONS) {
    blocks.push(h2(section.titre));
    
    for (const b of section.blocs) {
      if (b.type === "h3") blocks.push(h3(b.texte));
      if (b.type === "p") blocks.push(p(b.texte));
      if (b.type === "cal") blocks.push(cal(b.emoji, b.texte, b.note));
      if (b.type === "bul") {
        for (const item of b.items) blocks.push(bul(item));
      }
    }
    blocks.push(div());
  }

  // Positionnement final
  blocks.push(
    h2("🧠 8️⃣ Positionnement mental"),
    cal("🚫", "Tu ne vends pas un audit.", "Tu vends :\n👉 De la Clarté Stratégique.")
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
    throw new Error(`Notion ${method} ${endpoint} -> ${res.status}: ${JSON.stringify(err)}`);
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

  console.log(`Creation page : ${PAGE.titre}`);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: NOTION_PARENT_PAGE_ID },
    properties: {
      title: { title: [{ text: { content: PAGE.titre } }] },
    },
    children: chunks[0],
  });

  console.log(`Page creee : ${page.url}`);

  for (let i = 1; i < chunks.length; i++) {
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${page.id}/children`, { children: chunks[i] });
  }

  console.log("Termine - Offre Audit B2B deplouee dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

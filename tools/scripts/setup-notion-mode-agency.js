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
  titre: "🏢 Mode Agency — Blueprint Lancement SASU",
  objectif: "Transformer schoolsWP en machine d’autorité et de génération de leads premium pour la SASU. Ce n'est plus un média, c'est un écosystème d’acquisition.",
};

const SECTIONS = [
  {
    titre: "🎯 1️⃣ Positionnement de la SASU",
    blocs: [
      {
        type: "p",
        texte: "La SASU ne sera pas une 'Agence WordPress généraliste'."
      },
      {
        type: "cal",
        emoji: "👑",
        texte: "Le Positionnement : Cabinet 'Systèmes WordPress rentables' (et Automatisation)",
        note: "Tu ne vends pas de la 'création de site'. Tu vends la structuration, l'automatisation et l'optimisation business sur WordPress."
      }
    ]
  },
  {
    titre: "📦 2️⃣ L'Offre Signature (1 offre, pas 12)",
    blocs: [
      {
        type: "cal",
        emoji: "💎",
        texte: "Offre : WordPress Business System",
        note: "Positionnement : Transformation système, pas simple site."
      },
      {
        type: "p",
        texte: "Ce qu'elle inclut :"
      },
      {
        type: "bul",
        items: [
          "Audit stratégique",
          "Refonte structure WordPress",
          "CRM + automatisation",
          "Tunnel simple",
          "Optimisation SEO technique",
          "Formation client"
        ]
      }
    ]
  },
  {
    titre: "🚀 3️⃣ & 4️⃣ Tunnel Agency Minimal",
    blocs: [
      {
        type: "h3",
        texte: "Rôle de schoolsWP"
      },
      {
        type: "cal",
        emoji: "🧲",
        texte: "Vitrine expertise • Démonstration compétence • Machine SEO • Générateur leads",
        note: "Chaque article doit pouvoir amener vers un audit, un diagnostic ou un appel stratégique."
      },
      {
        type: "h3",
        texte: "Le Tunnel à 5 Étapes"
      },
      {
        type: "num",
        items: [
          "Article SEO décisionnel",
          "CTA vers “Audit WordPress Business gratuit”",
          "Formulaire structuré (qualification drastique)",
          "Appel stratégique",
          "Proposition (Closing)"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "📋 5️⃣ Structure Notion Agency (CRM de Leads)",
    blocs: [
      {
        type: "p",
        texte: "Créer une base '🏢 Prospects' avec ces propriétés :"
      },
      {
        type: "bul",
        items: [
          "Source (Quel article l'a converti ?)",
          "Niveau maturité (Éduqué vs Froid)",
          "Problème principal (CRM, LMS, Tunnel ?)",
          "Budget estimé",
          "Score Fit (1 à 5)",
          "Statut (Lead / Call / Proposal / Client)"
        ]
      }
    ]
  },
  {
    titre: "📈 6️⃣ KPI Agency (Cibles à monitorer)",
    blocs: [
      {
        type: "bul",
        items: [
          "Leads qualifiés / mois : 5 à 15",
          "Taux de closing : > 25 %",
          "Panier moyen : Premium (à définir)",
          "Temps projet : Optimisé et processé",
          "Marge nette : Prioritaire sur le CA"
        ]
      }
    ]
  },
  {
    titre: "📅 9️⃣ Timeline Préparation SASU (90 Jours)",
    blocs: [
      {
        type: "h3",
        texte: "Phase 1 : 3 mois avant lancement"
      },
      {
        type: "bul",
        items: [
          "Clarifier l'offre signature",
          "Définir le pricing exact",
          "Créer la page Audit / Formulaire",
          "Préparer 5 articles décisionnels forts"
        ]
      },
      {
        type: "h3",
        texte: "Phase 2 : Lancement"
      },
      {
        type: "bul",
        items: [
          "Annoncer officiellement",
          "Placer les CTA sur les 10 articles clés existants",
          "Activer le réseau"
        ]
      },
      {
        type: "h3",
        texte: "Phase 3 : Stabilisation"
      },
      {
        type: "bul",
        items: [
          "Collecter les études de cas",
          "Enregistrer les témoignages",
          "Packager un Upsell (maintenance / optimisation)"
        ]
      }
    ]
  }
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2];

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
const num = (t) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: [rt(t)] } });
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
      if (b.type === "num") {
        for (const item of b.items) blocks.push(num(item));
      }
    }
    blocks.push(div());
  }

  // Conclusion forte
  blocks.push(
    h2("🔥 L'Équation du Succès"),
    cal("⚡", "La matrice :", "schoolsWP = Autorité\nSASU = Monétisation premium\nContenu = Acquisition\nAutomatisation = Scalabilité")
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
  }

  console.log(`🎉 Terminé — Blueprint Lancement SASU déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
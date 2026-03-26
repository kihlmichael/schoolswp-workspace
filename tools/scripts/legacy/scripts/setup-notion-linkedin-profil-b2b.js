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
  titre: "👤 Profil LinkedIn — Positionnement B2B (Copier-Coller)",
  objectif: "Être immédiatement perçu comme l'Architecte WordPress des formateurs B2B. Pas comme un freelance générique.",
};

const SECTIONS = [
  {
    titre: "🧠 1️⃣ TITRE LINKEDIN (Headline)",
    blocs: [
      {
        type: "p",
        texte: "Version optimisée niche + crédibilité + clarté :"
      },
      {
        type: "cal",
        emoji: "🥇",
        texte: "Architecte de systèmes WordPress B2B | LMS • CRM • Automatisation | J’aide les formateurs à structurer un écosystème rentable"
      },
      {
        type: "p",
        texte: "Alternative plus premium :"
      },
      {
        type: "cal",
        emoji: "💎",
        texte: "Architecte WordPress pour formateurs B2B | LMS, CRM & automatisation | Structurer un système rentable et scalable"
      }
    ]
  },
  {
    titre: "🖼 2️⃣ BANNIÈRE (Texte à intégrer au design)",
    blocs: [
      {
        type: "p",
        texte: "Simple. Direct. Fort. (Design professionnel et minimaliste)"
      },
      {
        type: "cal",
        emoji: "🎨",
        texte: "[Centre - Ligne 1]\nStructurer votre système WordPress B2B\n\n[Centre - Ligne 2]\nLMS • CRM • Automatisation • Scalabilité\n\n[Bas Droite - Discret]\n👉 Audit stratégique B2B disponible"
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "📝 3️⃣ RÉSUMÉ LINKEDIN (Prêt à copier-coller)",
    blocs: [
      {
        type: "cal",
        emoji: "✍️",
        texte: `Les formateurs B2B n’ont pas un problème de plugin.
Ils ont un problème d’architecture.

Un LMS mal structuré.
Un CRM non segmenté.
Un onboarding entreprise manuel.
Un tunnel pensé B2C alors qu’ils vendent en B2B.

🔹 CE QUE JE FAIS
J’aide les formateurs qui vendent à des entreprises à structurer un système WordPress rentable, automatisé et scalable.
Pas un simple site. Un écosystème cohérent.

🔹 CE QUE J'OPTIMISE
• Architecture LMS adaptée aux entreprises
• Gestion multi-clients corporate
• CRM segmenté B2B
• Automatisation onboarding & relances
• Tunnel WordPress structuré
• Performance & évolutivité

🔹 MON APPROCHE
Je ne parle pas “plugin”.
Je parle : système, logique business, structuration, rentabilité, automatisation.

🔹 POUR QUI ?
Formateurs B2B qui :
– vendent des formations à des entreprises
– ont déjà un chiffre d’affaires
– veulent structurer proprement leur écosystème
– veulent scaler sans complexité inutile

🔹 COMMENCER L'OPTIMISATION
Si vous voulez savoir si votre architecture WordPress tient la route, je propose un audit stratégique B2B. Contactez-moi en DM.`
      }
    ]
  },
  {
    titre: "🎯 4️⃣ Section “Services” LinkedIn",
    blocs: [
      {
        type: "p",
        texte: "Créer / Mettre à jour un service spécifique sur ton profil :"
      },
      {
        type: "cal",
        emoji: "💼",
        texte: "Nom du service :\nAudit Architecture WordPress B2B",
        note: "Description courte :\nAnalyse complète de votre LMS, CRM et automatisations pour identifier les blocages structurels et optimiser votre rentabilité."
      }
    ]
  },
  {
    titre: "🔥 5️⃣ Ton différenciant à garder (Mindset)",
    blocs: [
      {
        type: "bul",
        items: [
          "Architecture > Plugin",
          "Système > Outil",
          "Rentabilité > Technique",
          "B2B > Généraliste"
        ]
      },
      {
        type: "p",
        texte: "🧠 Résultat attendu : Quand quelqu’un arrive sur ton profil, il doit penser « Il comprend la structuration B2B », pas « C'est un freelance WordPress »."
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

  console.log(`🎉 Terminé — Profil LinkedIn déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
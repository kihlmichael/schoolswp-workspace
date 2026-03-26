#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "💎 Offre Elite — B2B WordPress Architecture Partner",
  objectif: "Partenaire strategique long terme pour formateurs B2B ambitieux. Transformation rare, pas juste un projet.",
};

const SECTIONS = [
  {
    titre: "Positionnement",
    blocs: [
      { type: "p", texte: "Offre Elite : partenaire strategique long terme pour formateurs B2B ambitieux." },
      { type: "p", texte: "Tu ne livres plus un projet. Tu deviens architecte referent." }
    ]
  },
  {
    titre: "A qui s'adresse l'offre Elite ?",
    blocs: [
      { type: "bul", items: ["Formateurs B2B deja structures", "CA recurrent", "Plusieurs entreprises clientes", "Ambition croissance / scalabilite", "Volonte d'optimisation continue"] }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "Structure de l'offre Elite",
    blocs: [
      { type: "h3", texte: "1 - Phase 1 : Diagnostic avance (Deep Architecture)" },
      { type: "bul", items: ["Audit complet LMS", "Audit CRM", "Audit tunnel", "Audit performance", "Audit UX entreprise", "Cartographie complete systeme", "Session strategique 2h"] },
      { type: "h3", texte: "2 - Phase 2 : Refonte Architecture B2B" },
      { type: "bul", items: ["Refonte structure LMS", "Segmentation entreprise avancee", "Optimisation cycle long", "Automatisation onboarding corporate", "Optimisation conversion"] },
      { type: "h3", texte: "3 - Phase 3 : Optimisation Revenue & Scalabilite" },
      { type: "bul", items: ["Upsell structure", "Renewal automatise", "Reporting KPI entreprise", "Optimisation maillage & SEO", "Simplification systeme"] },
      { type: "h3", texte: "4 - Phase 4 : Accompagnement 3 a 6 mois" },
      { type: "bul", items: ["2 calls strategiques / mois", "Ajustements systeme", "Optimisation continue", "Support prioritaire"] }
    ]
  }
];

const SECTIONS_PART_3 = [
  {
    titre: "Positionnement prix",
    blocs: [
      { type: "p", texte: "Fourchette coherente : 12 000 - 20 000 EUR" },
      { type: "bul", items: ["Transformation complete", "Accompagnement long", "Impact direct sur CA", "Position rare"] }
    ]
  },
  {
    titre: "Differenciation",
    blocs: [
      { type: "cal", emoji: "🚫", texte: "Tu n'es plus : Freelance WordPress." },
      { type: "cal", emoji: "✅", texte: "Tu es : Architecte et partenaire de croissance WordPress B2B." }
    ]
  },
  {
    titre: "Argument cle pour vendre",
    blocs: [
      { type: "p", texte: "Un formateur B2B peut perdre un contrat entreprise, un renouvellement, un upsell a cause d'une architecture mal pensee." },
      { type: "p", texte: "Ton intervention = ROI immediat." }
    ]
  },
  {
    titre: "Structure de pitch simple",
    blocs: [
      { type: "bul", items: ["Vous vendez a des entreprises ?", "Votre systeme est-il concu pour gerer plusieurs clients corporate ?", "Avez-vous une segmentation CRM par entreprise ?", "Votre onboarding est-il automatise ?", "Vos renouvellements sont-ils structures ?", "Si la reponse est non -> opportunite."] }
    ]
  }
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2, ...SECTIONS_PART_3];
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
  if (note) parts.push(rt("\n\n" + note, { italic: true, color: "gray" }));
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

function buildTemplate() {
  const blocks = [];
  blocks.push(cal("🎯", PAGE.objectif), p(""), div());

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

  return blocks;
}

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

  console.log("Termine - Offre Elite B2B deployee dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

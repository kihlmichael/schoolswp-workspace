#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "📞 Script Appel Strategique — B2B WordPress System",
  objectif: "Diagnostiquer, positionner, filtrer, conclure premium. Pas de pitch, pas de vente de site.",
};
const SECTIONS = [
  {
    titre: "1 - Ouverture (5 minutes)",
    blocs: [
      { type: "p", texte: "Objectif : cadrer et installer la posture." },
      {
        type: "cal",
        emoji: "🎯",
        texte: "Merci pour votre temps. L'objectif aujourd'hui n'est pas de parler plugins, mais de comprendre si votre architecture WordPress soutient reellement votre activite B2B.\n\nAppel structure, questions precises, pas de pression commerciale."
      }
    ]
  },
  {
    titre: "2 - Comprendre leur modele B2B (10 minutes)",
    blocs: [
      { type: "h3", texte: "Questions cles" },
      { type: "bul", items: ["A qui vendez-vous ?", "Ticket moyen entreprise ?", "Cycle de vente (court / long) ?", "Nombre d'entreprises actives ?"] },
      { type: "bul", items: ["Ou voulez-vous etre dans 12 mois ?", "Qu'est-ce qui bloque aujourd'hui ?"] },
      { type: "p", texte: "Ecouter. Creuser. Ne pas interrompre." }
    ]
  },
  {
    titre: "3 - Diagnostic Architecture (15 minutes)",
    blocs: [
      { type: "p", texte: "Basculer technique." },
      { type: "h3", texte: "LMS" },
      { type: "bul", items: ["Gerez-vous les comptes entreprise separement ?", "Comment suivez-vous les apprenants corporate ?", "Avez-vous des cohortes ?"] },
      { type: "h3", texte: "CRM" },
      { type: "bul", items: ["Segmentation par entreprise ?", "Pipeline devis ?", "Automatisation relances ?"] },
      { type: "h3", texte: "Tunnel" },
      { type: "bul", items: ["Formulaire qualification ?", "Process onboarding entreprise ?", "Reporting client ?"] },
      { type: "p", texte: "Pendant qu'ils repondent : identifier les failles." }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "4 - Reformulation strategique (5 minutes)",
    blocs: [
      { type: "p", texte: "Cle du closing." },
      {
        type: "cal",
        emoji: "🧠",
        texte: "Si je resume, votre systeme actuel fonctionne, mais il n'est pas structure pour gerer X entreprises, ni pour automatiser Y, ni pour securiser Z."
      },
      { type: "p", texte: "Faire emerger le cout du probleme : temps perdu, opportunites ratees, scalabilite limitee." }
    ]
  },
  {
    titre: "5 - Projection (5 minutes)",
    blocs: [
      { type: "p", texte: "Creer la vision." },
      { type: "bul", items: ["Automatiser onboarding", "Gerer multi-entreprises proprement", "Suivre KPI corporate", "Liberer du temps"] }
    ]
  },
  {
    titre: "6 - Qualification Fit",
    blocs: [
      { type: "h3", texte: "Questions directes" },
      { type: "bul", items: ["Etes-vous pret a structurer proprement votre systeme ?", "Cherchez-vous un correctif ou une architecture durable ?", "Avez-vous prevu un budget pour cette transformation ?"] },
      { type: "p", texte: "S'ils hesitent : pas bon fit." }
    ]
  }
];

const SECTIONS_PART_3 = [
  {
    titre: "7 - Presentation Offre (5 minutes)",
    blocs: [
      {
        type: "cal",
        emoji: "💎",
        texte: "Mon travail n'est pas d'ajouter des plugins, mais de concevoir l'architecture WordPress qui soutient votre croissance B2B."
      },
      { type: "p", texte: "Presenter brievement les 5 modules. Ne pas entrer dans les details techniques." }
    ]
  },
  {
    titre: "8 - Cloture",
    blocs: [
      { type: "h3", texte: "Option 1 : bon fit" },
      { type: "cal", emoji: "✅", texte: "Je vous envoie une proposition structuree sous 48h." },
      { type: "h3", texte: "Option 2 : mauvais fit" },
      { type: "cal", emoji: "🚫", texte: "Je pense que vous avez d'abord besoin de clarifier X." },
      { type: "p", texte: "Toujours rester expert, jamais vendeur." }
    ]
  }
];

const RULES = [
  "Parler systeme, pas outil",
  "Parler business, pas technique",
  "Parler architecture, pas plugin",
  "Filtrer sans peur",
  "Silence strategique apres prix"
];

const PRICING = "Pour ce type d'architecture B2B, les projets commencent autour de X selon la complexite.";

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

  blocks.push(h2("Regles d'or"));
  for (const r of RULES) blocks.push(bul(r));
  blocks.push(div());
  blocks.push(h2("Transition vers prix"));
  blocks.push(cal("💰", PRICING));

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

  console.log("Termine - Script appel strategique B2B deploye dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

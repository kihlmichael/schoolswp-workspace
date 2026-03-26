#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "🧠 Methode interne — B2B WordPress System (v1)",
  objectif: "Offre duplicable, livrables standardises, prix plus eleve, temps projet reduit, base futur produit.",
};
const SECTIONS = [
  {
    titre: "PHASE 1 — DIAGNOSTIC STRATEGIQUE (Semaine 1)",
    blocs: [
      { type: "h3", texte: "Objectif" },
      { type: "p", texte: "Comprendre le business avant la technique." },
      { type: "h3", texte: "Etape 1 — Analyse Business B2B" },
      { type: "bul", items: ["Offre principale", "Type d'entreprises clientes", "Cycle de vente", "CA par client", "Objectif croissance"] },
      { type: "h3", texte: "Etape 2 — Audit Technique" },
      { type: "bul", items: ["LMS actuel", "Structure roles / acces", "CRM et segmentation", "Tunnel et formulaire", "Performance technique"] },
      { type: "h3", texte: "Etape 3 — Cartographie systeme" },
      { type: "p", texte: "Tu produis :" },
      { type: "bul", items: ["Schema architecture actuelle", "Points de friction", "Points de rupture scalabilite", "Risques futurs"] },
      { type: "p", texte: "Livrable : Rapport strategique + Roadmap priorisee." }
    ]
  },
  {
    titre: "PHASE 2 — ARCHITECTURE CIBLE (Semaine 2)",
    blocs: [
      { type: "h3", texte: "Objectif" },
      { type: "p", texte: "Dessiner le systeme cible." },
      { type: "h3", texte: "Etape 4 — Architecture LMS B2B" },
      { type: "bul", items: ["Multi-entreprises", "Groupes", "Cohortes", "Gestion acces", "Permissions"] },
      { type: "h3", texte: "Etape 5 — Architecture CRM" },
      { type: "bul", items: ["Segmentation entreprise", "Tags logiques", "Pipeline B2B", "Triggers automatisation"] },
      { type: "h3", texte: "Etape 6 — Tunnel et qualification" },
      { type: "bul", items: ["Page entreprise", "Formulaire intelligent", "Qualification avant appel"] },
      { type: "p", texte: "Livrable : Schema complet du systeme cible." }
    ]
  },
  {
    titre: "PHASE 3 — IMPLEMENTATION STRUCTUREE (Semaines 3–5)",
    blocs: [
      { type: "h3", texte: "Objectif" },
      { type: "p", texte: "Construire proprement." },
      { type: "h3", texte: "Etape 7 — Mise en place LMS" },
      { type: "bul", items: ["Configuration propre", "Tests groupes", "Tests acces", "UX entreprise"] },
      { type: "h3", texte: "Etape 8 — Mise en place CRM" },
      { type: "bul", items: ["Segmentation avancee", "Automatisations cycle long", "Sequences onboarding"] },
      { type: "h3", texte: "Etape 9 — Tunnel et automatisation" },
      { type: "bul", items: ["Qualification", "Pre-appel", "Suivi relance", "Notifications internes"] },
      { type: "p", texte: "Livrable : Systeme fonctionnel + documentation." }
    ]
  },
  {
    titre: "PHASE 4 — OPTIMISATION ET SCALABILITE (Semaine 6)",
    blocs: [
      { type: "h3", texte: "Objectif" },
      { type: "p", texte: "Assurer robustesse long terme." },
      { type: "h3", texte: "Etape 10 — Test complet" },
      { type: "bul", items: ["Parcours entreprise", "Creation compte groupe", "Attribution acces", "Automatisation CRM"] },
      { type: "h3", texte: "Etape 11 — Optimisation performance" },
      { type: "bul", items: ["Temps chargement", "Structure technique", "Securite"] },
      { type: "h3", texte: "Etape 12 — Formation client" },
      { type: "bul", items: ["Presentation architecture", "Utilisation CRM", "Process interne"] },
      { type: "p", texte: "Livrable : Documentation + session formation." }
    ]
  }
];
const SUMMARY = {
  duree: "Duree moyenne : 6 semaines",
  etapes: "Nombre d'etapes : 12",
  livrables: "Livrables : 4 blocs",
  documentation: "Documentation systematique",
};

const WHY = [
  "Elle justifie ton prix",
  "Elle montre maturite",
  "Elle rassure B2B",
  "Elle est duplicable",
  "Elle peut devenir formation",
];
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

  for (const section of SECTIONS) {
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

  blocks.push(h2("Structure standard projet"));
  blocks.push(bul(SUMMARY.duree));
  blocks.push(bul(SUMMARY.etapes));
  blocks.push(bul(SUMMARY.livrables));
  blocks.push(bul(SUMMARY.documentation));
  blocks.push(div());

  blocks.push(h2("Pourquoi cette methode est puissante"));
  for (const w of WHY) blocks.push(bul(w));

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

  console.log("Termine - Methode B2B WordPress System deployee dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

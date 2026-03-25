#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "📅 Planning éditorial LinkedIn 30 jours — B2B WordPress",
  objectif: "Formateurs B2B + Positionnement Architecte WordPress B2B. Objectif : conversations qualifiées → audit → projets premium.",
};

const WEEKS = [
  {
    title: "SEMAINE 1 — Problème & Positionnement",
    posts: [
      {
        day: "Lundi",
        color: "🟢",
        title: "Votre LMS WordPress n’est pas conçu pour gérer des entreprises.",
        angle: "Différence B2C vs B2B · Gestion multi-comptes · Reporting · Cohortes",
        cta: "Si vous vendez à des entreprises, votre architecture doit changer.",
        notes: "Hook fort (problème structurel).",
      },
      {
        day: "Mercredi",
        color: "🔵",
        title: "Voici l’architecture WordPress que j’utilise pour les formateurs B2B.",
        angle: "LMS · CRM · Tunnel · Automatisation onboarding · Reporting + mini schéma texte",
        cta: "—",
        notes: "Architecture + schéma textuel simple.",
      },
      {
        day: "Vendredi",
        color: "🟣",
        title: "Le vrai problème des formateurs B2B n’est pas le LMS.",
        angle: "CRM mal structuré · segmentation inexistante · cycle long ignoré",
        cta: "Question ouverte en fin de post.",
        notes: "Erreur fréquente + question.",
      },
    ],
  },
  {
    title: "SEMAINE 2 — Méthode & Profondeur",
    posts: [
      {
        day: "Lundi",
        color: "🟢",
        title: "3 signaux que votre système WordPress B2B est mal structuré.",
        angle: "Checklist rapide",
        cta: "—",
        notes: "Diagnostic rapide.",
      },
      {
        day: "Mercredi",
        color: "🔵",
        title: "Pourquoi un formateur B2B doit penser architecture avant plugin.",
        angle: "Logique système, pas d’outil",
        cta: "—",
        notes: "Insight stratégique.",
      },
      {
        day: "Vendredi",
        color: "🟣",
        title: "Comment un formateur B2B a automatisé son onboarding entreprise.",
        angle: "Avant / Problème / Solution / Résultat",
        cta: "—",
        notes: "Mini étude de cas.",
      },
    ],
  },
  {
    title: "SEMAINE 3 — Autorité & Positionnement Premium",
    posts: [
      {
        day: "Lundi",
        color: "🟢",
        title: "Un LMS à 1 500 € pour du B2B est un risque.",
        angle: "Complexité · Scalabilité · Image entreprise",
        cta: "—",
        notes: "Opinion tranchée.",
      },
      {
        day: "Mercredi",
        color: "🔵",
        title: "Pourquoi votre CRM WordPress doit segmenter par entreprise, pas par individu.",
        angle: "Insight avancé",
        cta: "—",
        notes: "Segmentation CRM.",
      },
      {
        day: "Vendredi",
        color: "🟣",
        title: "Voici comment j’automatise l’onboarding entreprise sur WordPress.",
        angle: "Étapes simples",
        cta: "—",
        notes: "Process onboarding.",
      },
    ],
  },
  {
    title: "SEMAINE 4 — Conversion & Conversations",
    posts: [
      {
        day: "Lundi",
        color: "🟢",
        title: "Si vous gérez plus de 5 entreprises clientes sur WordPress, lisez ceci.",
        angle: "Liste de points à vérifier",
        cta: "—",
        notes: "Audit implicite.",
      },
      {
        day: "Mercredi",
        color: "🔵",
        title: "Un système WordPress B2B bien structuré change votre rentabilité.",
        angle: "Renouvellement · Upsell · Rétention",
        cta: "—",
        notes: "Vision long terme.",
      },
      {
        day: "Vendredi",
        color: "🟣",
        title: "Vous formez des entreprises ? Je peux vous dire en 15 minutes si votre architecture tient la route.",
        angle: "CTA conversation",
        cta: "Envoyez-moi “ARCHI”.",
        notes: "CTA naturel.",
      },
    ],
  },
];

const GOALS = [
  "Installer spécialisation",
  "Créer perception premium",
  "Générer 5–15 conversations qualifiées",
  "2–5 appels",
  "1–3 projets",
];

const RULES = [
  "Toujours parler système",
  "Toujours parler business",
  "Toujours contextualiser B2B",
  "Jamais parler plugin sans stratégie",
  "Jamais donner astuces basiques",
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

  for (const week of WEEKS) {
    blocks.push(h2(`📅 ${week.title}`));
    for (const post of week.posts) {
      blocks.push(
        h3(`${post.color} ${post.day} — ${post.title}`),
        p(`Angle : ${post.angle}`),
        p(`CTA : ${post.cta}`),
        p(`Note : ${post.notes}`),
        cal("✍️", "Texte du post à rédiger ici."),
        div()
      );
    }
  }

  blocks.push(h2("🎯 Objectif 30 jours"));
  for (const g of GOALS) blocks.push(bul(g));
  blocks.push(div());
  blocks.push(h2("🔥 Conseils importants"));
  for (const r of RULES) blocks.push(bul(r));

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

  console.log("Termine - Planning editorial LinkedIn 30 jours B2B deploye dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

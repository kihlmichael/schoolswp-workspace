#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "📝 Résumé LinkedIn — B2B WordPress (3 versions)",
  objectif: "Résumé LinkedIn optimisé niche B2B, cohérent schoolsWP + SASU, ton clair et structuré.",
};

const VERSIONS = [
  {
    title: "VERSION 1 — Positionnement fort & direct",
    label: "Recommandée (accessible et pédagogique)",
    text: `🎯 Architecte de systèmes WordPress pour formateurs B2B

La majorité des formateurs qui vendent à des entreprises ont un site WordPress.
Mais très peu ont une architecture réellement pensée pour le B2B.

Résultat :

LMS mal structuré
CRM non segmenté
Onboarding manuel
Reporting absent
Tunnel incohérent

Je conçois des systèmes WordPress complets pour formateurs B2B :

• LMS structuré pour multi-entreprises
• CRM segmenté par organisation
• Automatisations onboarding & relances
• Tunnel de qualification entreprise
• Architecture scalable

Je ne crée pas “un site”.
Je structure un système rentable.

Fondateur de schoolsWP, média dédié à WordPress stratégique, SEO et automatisation.

Si vous formez des entreprises et que votre WordPress devient complexe,
je peux analyser votre architecture et identifier les points de friction.`
  },
  {
    title: "VERSION 2 — Plus pédagogique, plus stratégique",
    label: "Recommandée (pédagogique et structurée)",
    text: `Les formateurs B2B ont un problème invisible :

Ils utilisent WordPress comme un outil technique,
alors qu’ils devraient le penser comme un système business.

Vendre à des entreprises implique :

• Gestion multi-comptes
• Segmentation CRM avancée
• Onboarding automatisé
• Cycle de vente long
• Reporting structuré

Sans architecture claire,
le système devient fragile.

J’accompagne les formateurs B2B à structurer un écosystème WordPress rentable :

LMS • CRM • Tunnel • Automatisation • Scalabilité

Mon approche combine :
SEO stratégique, architecture technique et vision business.

Fondateur de schoolsWP,
j’analyse et conçois des systèmes WordPress pensés pour durer.

Si vous vendez des formations aux entreprises,
la vraie question n’est pas votre plugin.
C’est votre architecture.`
  },
  {
    title: "VERSION 3 — Ultra premium & assumée",
    label: "À utiliser quand le premium est assumé",
    text: `Je conçois des architectures WordPress pour formateurs B2B exigeants.

Pas des sites.

Des systèmes.

LMS structuré
CRM segmenté par entreprise
Automatisation onboarding
Tunnel de qualification
Optimisation renouvellement

Quand WordPress est mal pensé,
la croissance devient fragile.

Quand il est structuré,
il devient un levier.

Fondateur de schoolsWP,
j’analyse et structure des écosystèmes WordPress orientés performance B2B.

Si votre système commence à devenir complexe,
c’est qu’il est temps de le repenser.`
  }
];

const RECO = "Pour ton profil actuel : Version 1 ou 2 (plus accessible, plus pédagogique). La version 3 est idéale quand tu assumes pleinement le premium.";
const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const p = (t) => ({ object: "block", type: "paragraph", paragraph: { rich_text: [rt(t)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, t, body) => {
  const parts = [rt(t, { bold: true })];
  if (body) parts.push(rt("\n\n" + body));
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

function buildTemplate() {
  const blocks = [];
  blocks.push(cal("🎯", PAGE.objectif), p(""), div());

  for (const v of VERSIONS) {
    blocks.push(
      h2(v.title),
      cal("✍️", v.label, v.text),
      div()
    );
  }

  blocks.push(h2("🎯 Recommandation"), p(RECO));
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

  console.log("Termine - Resume LinkedIn B2B deploye dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

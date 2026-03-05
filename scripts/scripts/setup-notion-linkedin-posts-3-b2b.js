#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "✍️ Posts LinkedIn — 3 premiers (B2B WordPress)",
  objectif: "Posts prêts à publier. Niche formateurs B2B, positionnement architecte WordPress système.",
};
const POSTS = [
  {
    num: 1,
    title: "Positionnement fort",
    emoji: "🟢",
    text: `Votre LMS WordPress n’est probablement pas conçu pour gérer des entreprises.

Beaucoup de formateurs B2B utilisent :

Tutor LMS
LearnDash
un CRM
quelques automatisations

Mais leur architecture reste pensée B2C.

Et c’est là que ça bloque.

Un formateur B2C vend à des individus.
Un formateur B2B vend à des organisations.

Ce n’est pas la même logique.

En B2B, il faut gérer :

• plusieurs apprenants par entreprise
• des accès groupés
• du reporting par client
• des cycles longs
• du renouvellement

Si votre LMS n’est pas structuré pour ça, vous compensez à la main.

Et ça finit toujours par exploser.

La question n’est pas :
“Quel plugin choisir ?”

La question est :
“Mon architecture WordPress est-elle pensée pour le B2B ?”

Si vous formez des entreprises, votre système doit évoluer.`
  },
  {
    num: 2,
    title: "Architecture",
    emoji: "🔵",
    text: `Voici l’architecture WordPress que j’utilise pour les formateurs B2B.

Un système B2B n’est pas une accumulation de plugins.

C’est une structure.

Voici la base que j’utilise :

1️⃣ LMS structuré par cohortes ou entreprises
2️⃣ CRM segmenté par organisation (pas seulement par contact)
3️⃣ Tunnel B2B avec qualification claire
4️⃣ Automatisation onboarding entreprise
5️⃣ Reporting exploitable

Le plus gros piège ?

Ajouter des outils sans logique globale.

Un système B2B doit répondre à 3 questions :

• Comment j’intègre une nouvelle entreprise ?
• Comment je gère ses apprenants ?
• Comment je renouvelle ou j’upsell ?

Si vous ne pouvez pas répondre clairement à ces 3 points,
votre architecture a des failles.

WordPress peut parfaitement gérer du B2B.

Mais seulement si on pense système, pas plugin.`
  },
  {
    num: 3,
    title: "Erreur fréquente",
    emoji: "🟣",
    text: `Le vrai problème des formateurs B2B n’est pas le LMS.

La majorité se concentre sur :

“Quel LMS choisir ?”

Alors que le point critique est ailleurs.

Le CRM.

En B2B :

le cycle est long
la décision est collective
le budget est validé
le suivi est clé

Si votre CRM :

• ne segmente pas par entreprise
• ne suit pas les cycles longs
• ne gère pas les relances
• ne prépare pas le renouvellement

vous perdez des opportunités invisibles.

Un LMS gère l’apprentissage.

Un CRM gère la relation commerciale.

Confondre les deux crée un système bancal.

Vous formez des entreprises ?

Votre CRM est-il structuré par organisation… ou juste par email ?`
  }
];
const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({
  object: "block",
  type: "heading_2",
  heading_2: { rich_text: [rt(t)] }
});

const p = (t) => ({
  object: "block",
  type: "paragraph",
  paragraph: { rich_text: [rt(t)] }
});

const div = () => ({ object: "block", type: "divider", divider: {} });

const cal = (emoji, t, body) => {
  const parts = [rt(t, { bold: true })];
  if (body) parts.push(rt("\n\n" + body));
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

function buildTemplate() {
  const blocks = [];
  blocks.push(cal("🎯", PAGE.objectif), p(""), div());

  for (const post of POSTS) {
    blocks.push(
      h2(`${post.emoji} POST ${post.num} — ${post.title}`),
      cal("📝", "Texte prêt à publier :", post.text),
      div()
    );
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

  console.log("Termine - Posts LinkedIn (3) deployes dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});

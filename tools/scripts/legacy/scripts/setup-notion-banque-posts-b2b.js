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
  titre: "✍️ Banque de 10 Posts LinkedIn B2B",
  objectif: "10 posts puissants prêts à l'emploi. Objectif : autorité + conversations qualifiées. Ton direct. Pas de blabla. Pas de tips génériques.",
};

const POSTS = [
  {
    num: 1,
    titre: "Le vrai problème des formateurs B2B",
    emoji: "🔥",
    texte: `Votre problème n’est pas votre LMS.

C’est votre architecture.

Un formateur B2B doit gérer :
• plusieurs entreprises
• plusieurs cohortes
• plusieurs responsables RH
• des cycles longs
• des relances
• du reporting

Un simple plugin LMS ne suffit pas.

Ce qu’il faut :
→ CRM segmenté
→ onboarding automatisé
→ logique multi-entreprises
→ tunnel B2B structuré

Sinon, vous empilez des outils.
Et vous perdez du contrôle.

Est-ce que votre WordPress est pensé comme un système…
ou juste comme un site ?`
  },
  {
    num: 2,
    titre: "3 signaux que votre LMS B2B est mal conçu",
    emoji: "🚨",
    texte: `1️⃣ Vous créez un compte par apprenant manuellement
2️⃣ Vous n’avez aucun reporting par entreprise
3️⃣ Vos relances sont faites “à la main”

Un LMS B2B doit être :
• structuré
• segmenté
• automatisé

Sinon, vous travaillez plus que vos clients.

La technologie n’est pas le problème.
La structure l’est.`
  },
  {
    num: 3,
    titre: "L’erreur la plus coûteuse",
    emoji: "💸",
    texte: `Beaucoup de formateurs B2B investissent dans un LMS.

Peu investissent dans le CRM.

Résultat ?
• Pas de segmentation entreprise
• Pas de relance automatique
• Pas de suivi devis
• Pas d’onboarding structuré

Un LMS gère l’accès.
Un CRM gère le business.

Sans CRM structuré, vous limitez votre croissance.`
  },
  {
    num: 4,
    titre: "Architecture type que j’utilise",
    emoji: "🏗️",
    texte: `Un système WordPress B2B efficace repose sur 4 briques :

1️⃣ LMS structuré multi-entreprises
2️⃣ CRM segmenté entreprise
3️⃣ Automatisation onboarding
4️⃣ Tunnel B2B clair

Ce n’est pas une question de plugin.
C’est une question d’architecture.

Un mauvais schéma coûte plus cher qu’un bon outil.`
  },
  {
    num: 5,
    titre: "Pourquoi les petits budgets bloquent",
    emoji: "💰",
    texte: `On peut créer un LMS pour 1 500 €.

Mais on ne peut pas structurer un système B2B solide à ce prix.

Parce qu’un système B2B implique :
• réflexion stratégique
• segmentation
• automatisation
• projection long terme

Un site n’est pas un système.
Un système demande méthode.`
  }
];
const POSTS_PART_2 = [
  {
    num: 6,
    titre: "Cas réel (anonymisé)",
    emoji: "📈",
    texte: `Un formateur B2B gérait :
• 8 entreprises
• 120 apprenants
• 0 automatisation

Chaque nouvelle entreprise = chaos.

Après restructuration :
→ onboarding automatisé
→ reporting par entreprise
→ segmentation CRM
→ relances automatiques

Résultat : moins de charge mentale, plus de contrôle.

Ce n’est pas la magie d’un plugin.
C’est la logique d’un système.`
  },
  {
    num: 7,
    titre: "Question stratégique",
    emoji: "🤔",
    texte: `Si demain vous signez 5 nouvelles entreprises…

Votre WordPress tient-il ?

Gestion comptes groupe ?
Reporting entreprise ?
Facturation structurée ?
Relances automatisées ?

La scalabilité se prépare avant la croissance.`
  },
  {
    num: 8,
    titre: "Ce que 90 % ignorent",
    emoji: "👁️",
    texte: `Un LMS B2B n’est pas un LMS B2C amélioré.

C’est un modèle différent :
B2C = volume
B2B = structure

Ce sont deux architectures.

Les mélanger crée du chaos.`
  },
  {
    num: 9,
    titre: "Diagnostic rapide",
    emoji: "🔍",
    texte: `Répondez mentalement :

1️⃣ Vos entreprises ont-elles un accès dédié ?
2️⃣ Votre CRM distingue-t-il entreprise et apprenant ?
3️⃣ Vos relances sont-elles automatisées ?
4️⃣ Avez-vous un reporting par client ?

Si vous avez répondu “non” à 2 questions…
Votre système est fragile.`
  },
  {
    num: 10,
    titre: "Positionnement fort",
    emoji: "👑",
    texte: `Je ne crée pas des sites WordPress.

Je structure des systèmes WordPress B2B.

Différence ?
Un site affiche. Un système fonctionne.
Un site vend. Un système scale.

Si vous formez des entreprises, votre architecture mérite plus qu’un empilement de plugins.`
  }
];

const ALL_POSTS = [...POSTS, ...POSTS_PART_2];

// ════════════════════════════════════════════════════════
//  BLOCK BUILDERS
// ════════════════════════════════════════════════════════

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const p = (t) => ({ object: "block", type: "paragraph", paragraph: { rich_text: [rt(t)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, t, note) => {
  const parts = [rt(t, { bold: true })];
  if (note) {
    parts.push(rt("\n\n" + note)); // Texte normal pour le corps du post
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

  for (const post of ALL_POSTS) {
    blocks.push(
      h2(`${post.emoji} POST ${post.num} — ${post.titre}`),
      cal("📝", "Copier le texte ci-dessous :", post.texte),
      p(""),
      div()
    );
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

  console.log(`🎉 Terminé — Banque de 10 Posts B2B déployée dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
#!/usr/bin/env node
/**
 * setup-notion-cluster-crm-domination.js
 * Crée la page "Cluster Domination — CRM WordPress & Automatisation" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-cluster-crm-domination.js
 */

"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function notionRequest(method, path, body) {
  const res = await fetch(`https://api.notion.com/v1${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Content-Type": "application/json",
      "Notion-Version": "2022-06-28",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Notion API ${res.status} — ${err}`);
  }
  return res.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------------------
// Block builders
// ---------------------------------------------------------------------------

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: {
    bold: opts.bold || false,
    italic: opts.italic || false,
    code: opts.code || false,
    color: opts.color || "default",
  },
});

const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (t) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: [rt(t)] } });
const tod = (t, checked = false) => ({ object: "block", type: "to_do", to_do: { rich_text: [rt(t)], checked } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (t) => ({ object: "block", type: "quote", quote: { rich_text: [rt(t)] } });
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Données — cluster CRM WordPress
// ---------------------------------------------------------------------------

const PILIER = {
  kw: "crm wordpress",
  titre: "CRM WordPress : Guide Stratégique Complet (2026)",
  slug: "crm-wordpress-guide-strategique",
  intent: "informationnelle + décisionnelle",
  mots_cles_lsi: [
    "crm natif wordpress", "fluentcrm wordpress", "wp fusion crm",
    "gestion contacts wordpress", "automatisation email wordpress",
    "crm formateur wordpress", "crm freelance wordpress",
  ],
  structure_h2: [
    { h2: "Pourquoi un CRM natif WordPress change tout", note: "Argument business : données centralisées, zéro friction, coût réduit vs SaaS" },
    { h2: "CRM natif WordPress vs CRM SaaS externe : le vrai comparatif", note: "Tableau décisionnel — pas un comparatif de fonctionnalités, un comparatif de contextes" },
    { h2: "Architecture CRM recommandée selon ton modèle business", note: "3 schémas : formateur / freelance / e-commerçant — ancre vers les satellites ultra-niche" },
    { h2: "Les 3 CRM WordPress qui comptent vraiment en 2026", note: "FluentCRM / WP Fusion / Groundhogg — verdict honnête avec cas d'usage" },
    { h2: "Comment structurer ta segmentation de contacts dès le départ", note: "Tags, listes, pipelines — la logique avant la technique" },
    { h2: "Les 5 automatisations CRM WordPress qui changent vraiment le CA", note: "Onboarding / relance panier / nurturing froid / upsell / réactivation" },
    { h2: "Les erreurs critiques à éviter (et pourquoi elles coûtent cher)", note: "Empilage sans logique, migration chaotique, segmentation inexistante" },
    { h2: "Mon architecture CRM WordPress recommandée — schoolsWP", note: "Prise de position claire + CTA Audit stratégique" },
  ],
  cta: "Audit Stratégique CRM WordPress (SASU)",
  monetisation: ["Affiliation FluentCRM", "Affiliation WP Fusion", "Lead Audit SASU"],
  priorite: "🔴 URGENT — à publier en premier",
  objectif: "Devenir LA référence francophone structurée sur le CRM WordPress d'ici M3",
};

const SATELLITES = [
  // — Comparatifs décisionnels —
  {
    groupe: "Comparatifs décisionnels",
    articles: [
      {
        kw: "fluentcrm vs mailerlite",
        titre: "FluentCRM vs MailerLite : lequel choisir pour WordPress ?",
        slug: "fluentcrm-vs-mailerlite",
        intent: "comparative",
        angle: "Pour formateurs et freelances : natif WordPress vs SaaS accessible — avec calcul coût réel sur 3 ans",
        lsi: ["fluentcrm avis", "mailerlite wordpress", "email marketing wordpress", "crm email wordpress"],
        cta: "Affiliation FluentCRM + lead audit",
        monetisation: "Affiliation FluentCRM (commission récurrente)",
        priorite: "🔴 M1",
        commande: `brain-lite.bat --keyword "fluentcrm vs mailerlite" --intent comparative`,
      },
      {
        kw: "fluentcrm vs activecampaign",
        titre: "FluentCRM vs ActiveCampaign : comparatif complet pour WordPress",
        slug: "fluentcrm-vs-activecampaign",
        intent: "comparative",
        angle: "Argument décisif : ActiveCampaign coûte 3–5× plus cher pour des fonctionnalités que FluentCRM a nativement sous WordPress",
        lsi: ["activecampaign alternative", "fluentcrm fonctionnalités", "crm wordpress pas cher", "email automation wordpress"],
        cta: "Affiliation FluentCRM + CTA Audit",
        monetisation: "Affiliation FluentCRM (fort potentiel — terme recherché à fort CPC)",
        priorite: "🔴 M1",
        commande: `brain-lite.bat --keyword "fluentcrm vs activecampaign" --intent comparative`,
      },
      {
        kw: "wp fusion vs fluentcrm",
        titre: "WP Fusion vs FluentCRM : pour quel projet WordPress choisir lequel ?",
        slug: "wp-fusion-vs-fluentcrm",
        intent: "comparative",
        angle: "Pas les mêmes outils — WP Fusion = connecteur CRM externe / FluentCRM = CRM natif. Deux logiques, deux contextes.",
        lsi: ["wp fusion avis", "wp fusion wordpress", "fluentcrm integrations", "crm lms wordpress"],
        cta: "Affiliation WP Fusion + affiliation FluentCRM",
        monetisation: "Double affiliation — commissions élevées sur WP Fusion",
        priorite: "🟠 M2",
        commande: `brain-lite.bat --keyword "wp fusion vs fluentcrm" --intent comparative`,
      },
      {
        kw: "crm wordpress vs systeme.io",
        titre: "CRM WordPress vs Systeme.io : lequel pour ton business en ligne ?",
        slug: "crm-wordpress-vs-systeme-io",
        intent: "comparative",
        angle: "La question n'est pas fonctionnalités — c'est : veux-tu la propriété ou la facilité ? Calcul de ROI sur 5 ans.",
        lsi: ["systeme.io alternative", "systeme.io wordpress", "crm tout en un wordpress", "funnel wordpress"],
        cta: "CTA Audit migration Systeme.io → WordPress",
        monetisation: "Lead génération premium (migration = projet 6–10k€)",
        priorite: "🟠 M2",
        commande: `brain-lite.bat --keyword "crm wordpress vs systeme io" --intent comparative`,
      },
    ],
  },

  // — Business & Architecture système —
  {
    groupe: "Architecture & Business système",
    articles: [
      {
        kw: "segmenter contacts wordpress fluentcrm",
        titre: "Comment segmenter ses contacts WordPress avec FluentCRM (guide pratique)",
        slug: "segmenter-contacts-wordpress-fluentcrm",
        intent: "informationnelle",
        angle: "Avant la technique, la logique business : pourquoi segmenter, comment penser les tags, les listes et les pipelines selon le parcours client",
        lsi: ["fluentcrm tags", "fluentcrm listes", "segmentation email wordpress", "pipeline crm wordpress"],
        cta: "Affiliation FluentCRM + CTA architecture CRM (Audit)",
        monetisation: "Affiliation + lead mid-funnel",
        priorite: "🟠 M2",
        commande: `brain-lite.bat --keyword "segmenter contacts wordpress fluentcrm" --intent informationnelle`,
      },
      {
        kw: "automatisation email wordpress fluentcrm",
        titre: "Automatiser ses emails WordPress avec FluentCRM : guide complet 2026",
        slug: "automatisation-email-wordpress-fluentcrm",
        intent: "informationnelle",
        angle: "5 automatisations concrètes qui changent vraiment le CA — onboarding / relance / nurturing / upsell / réactivation — avec exemples de séquences réelles",
        lsi: ["fluentcrm automation", "email automation wordpress", "séquence email wordpress", "workflow fluentcrm"],
        cta: "Affiliation FluentCRM + newsletter schoolsWP",
        monetisation: "Affiliation forte + abonnés newsletter qualifiés",
        priorite: "🟠 M3",
        commande: `brain-lite.bat --keyword "automatisation email wordpress fluentcrm" --intent informationnelle`,
      },
      {
        kw: "tunnel email formation wordpress",
        titre: "Tunnel email pour formation WordPress : architecture complète",
        slug: "tunnel-email-formation-wordpress",
        intent: "informationnelle",
        angle: "Schéma complet : landing → opt-in → séquence nurturing → page vente → post-achat → onboarding élève. Avec les outils WordPress natifs.",
        lsi: ["funnel email wordpress", "séquence vente formation", "email marketing formateur", "fluentcrm formation"],
        cta: "CTA fort vers Audit LBS / WBS (lead premium)",
        monetisation: "Lead premium — prospect idéal pour LBS / WBS Standard",
        priorite: "🟠 M3",
        commande: `brain-lite.bat --keyword "tunnel email formation wordpress" --intent informationnelle`,
      },
      {
        kw: "crm lms wordpress architecture",
        titre: "CRM + LMS WordPress : l'architecture idéale pour un formateur en ligne",
        slug: "crm-lms-wordpress-architecture",
        intent: "informationnelle",
        angle: "FluentCRM + Tutor LMS : comment les connecter pour que la progression élève déclenche automatiquement les bons emails au bon moment",
        lsi: ["fluentcrm tutor lms", "lms crm wordpress integration", "automatisation formateur wordpress", "tutor lms fluentcrm"],
        cta: "Lead LBS premium + affiliation double (FluentCRM + Tutor LMS)",
        monetisation: "Lead premium LBS + double affiliation",
        priorite: "🔴 M2 — fort potentiel business",
        commande: `brain-lite.bat --keyword "crm lms wordpress architecture" --intent informationnelle`,
      },
    ],
  },

  // — Ultra-niche cibles —
  {
    groupe: "Ultra-niche par profil cible",
    articles: [
      {
        kw: "crm wordpress coach en ligne",
        titre: "Quel CRM WordPress choisir quand on est coach en ligne ?",
        slug: "crm-wordpress-coach-en-ligne",
        intent: "décisionnelle",
        angle: "Les coachs n'ont pas besoin d'un CRM complexe — ils ont besoin d'un CRM qui automatise le suivi client, les relances séances et les renouvellements. FluentCRM suffit largement.",
        lsi: ["crm coach wordpress", "fluentcrm coach", "suivi client wordpress coach", "automatisation coach wordpress"],
        cta: "Affiliation FluentCRM + CTA Audit WBS",
        monetisation: "Affiliation + lead WBS Standard (budget coach = 3–7k€)",
        priorite: "🟡 M4",
        commande: `brain-lite.bat --keyword "crm wordpress coach en ligne" --intent décisionnelle`,
      },
      {
        kw: "crm wordpress freelance",
        titre: "CRM WordPress pour freelance : lequel choisir et comment le configurer",
        slug: "crm-wordpress-freelance",
        intent: "décisionnelle",
        angle: "Le freelance n'a pas besoin de 10 pipelines — il a besoin de 3 choses : suivi prospects, onboarding client, relance missions. FluentCRM configuré en 2h suffit.",
        lsi: ["crm freelance wordpress", "gestion prospects freelance wordpress", "fluentcrm freelance", "crm gratuit wordpress"],
        cta: "Affiliation FluentCRM + newsletter",
        monetisation: "Affiliation + abonnés qualifiés (freelances = audience schoolsWP cible)",
        priorite: "🟡 M4",
        commande: `brain-lite.bat --keyword "crm wordpress freelance" --intent décisionnelle`,
      },
      {
        kw: "crm woocommerce wordpress",
        titre: "CRM WooCommerce : comment gérer ses clients e-commerce sous WordPress",
        slug: "crm-woocommerce-wordpress",
        intent: "informationnelle",
        angle: "WooCommerce a des données clients riches — mais mal exploitées. FluentCRM + WooCommerce = segmentation acheteurs, relance panier, upsell automatisé, sans SaaS externe.",
        lsi: ["fluentcrm woocommerce", "crm ecommerce wordpress", "automatisation woocommerce", "email woocommerce clients"],
        cta: "Affiliation FluentCRM + WP Fusion (intégrations WooCommerce)",
        monetisation: "Double affiliation + lead WBS e-commerce (budget fort)",
        priorite: "🟡 M5",
        commande: `brain-lite.bat --keyword "crm woocommerce wordpress" --intent informationnelle`,
      },
    ],
  },

  // — Extension boule de neige —
  {
    groupe: "Extension — Boule de Neige Cluster",
    articles: [
      {
        kw: "automatisation wordpress n8n",
        titre: "Automatisation WordPress avec n8n : ce que FluentCRM seul ne peut pas faire",
        slug: "automatisation-wordpress-n8n",
        intent: "informationnelle",
        angle: "n8n comme couche d'orchestration au-dessus de FluentCRM — webhooks, connexions externes, logiques conditionnelles avancées sans coder",
        lsi: ["n8n wordpress", "n8n fluentcrm", "automatisation avancée wordpress", "webhook wordpress n8n"],
        cta: "Lead premium WBS (n8n = signal d'expertise élevée du client)",
        monetisation: "Lead ultra-qualifié pour WBS Premium (8–15k€)",
        priorite: "🟡 M5",
        commande: `brain-lite.bat --keyword "automatisation wordpress n8n" --intent informationnelle`,
      },
      {
        kw: "migrer activecampaign fluentcrm",
        titre: "Migrer d'ActiveCampaign vers FluentCRM : guide complet sans perdre de données",
        slug: "migrer-activecampaign-fluentcrm",
        intent: "décisionnelle",
        angle: "Pour les clients déjà sous ActiveCampaign : calcul d'économies + guide de migration contacts/séquences/tags — avec les pièges à éviter",
        lsi: ["migration email marketing wordpress", "importer contacts fluentcrm", "quitter activecampaign wordpress", "fluentcrm migration"],
        cta: "Affiliation FluentCRM + CTA Audit migration (lead WBS)",
        monetisation: "Affiliation forte + lead migration = projet WBS 4–8k€",
        priorite: "🟡 M6",
        commande: `brain-lite.bat --keyword "migrer activecampaign fluentcrm" --intent décisionnelle`,
      },
    ],
  },
];

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE
  blocks.push(
    cal(
      "Objectif : prendre un territoire, pas « faire du contenu ». CRM WordPress & Automatisation — le cluster le plus stratégique pour schoolsWP en 2026.",
      "🎯", "red_background"
    ),
    p(rt("Mis à jour : mars 2026 · 1 pilier + 14 satellites + plan domination 6 mois", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // POURQUOI CE CLUSTER
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧠 Pourquoi ce Cluster est le Bon Choix"),
    p(""),
    bul(rt("Forte intention business", { bold: true }), rt(" — les gens qui cherchent « CRM WordPress » veulent investir, pas juste s'informer")),
    bul(rt("Monétisation affiliée solide", { bold: true }), rt(" — FluentCRM, WP Fusion, Groundhogg ont tous des programmes récurrents")),
    bul(rt("Pont direct vers l'offre Agency (WBS™)", { bold: true }), rt(" — CRM = sujet central de l'Audit Stratégique et du WBS Standard")),
    bul(rt("Peu de contenus vraiment stratégiques en FR", { bold: true }), rt(" — la plupart des articles sont des listes de plugins sans angle business")),
    bul(rt("Compatible LLM/AIO", { bold: true }), rt(" — thème structuré, décisionnel, avec cas d'usage concrets = parfait pour les AI Overviews")),
    bul(rt("ADN naturel schoolsWP", { bold: true }), rt(" — automatisation + CRM + LMS + business WordPress = ton expertise démontrée")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // POSITIONNEMENT DANS LE CLUSTER
  // ───────────────────────────────────────────
  blocks.push(
    h1("1️⃣ Positionnement dans le Cluster"),
    p(""),
    h2("Ce que tu ne fais pas"),
    bul(rt("✗  ", { bold: true }), rt('"Quel est le meilleur CRM WordPress ?"  → liste générique sans angle')),
    bul(rt("✗  ", { bold: true }), rt('"Top 5 plugins CRM WordPress"  → contenu trafic sans valeur ajoutée')),
    bul(rt("✗  ", { bold: true }), rt('"FluentCRM tutoriel"  → trop technique, trop low-intent')),
    p(""),
    h2("Ce que tu fais"),
    cal(
      "Comment structurer un système CRM WordPress rentable selon ton modèle business. Tu prends le territoire stratégique, pas l'outil.",
      "🎯", "green_background"
    ),
    p(""),
    bul(rt("Chaque article répond à une question business", { bold: true }), rt(", pas juste technique")),
    bul(rt("L'angle schoolsWP est toujours visible", { bold: true }), rt(" : prise de position, recommandation claire, pas de bullshit")),
    bul(rt("Le maillage interne est bidirectionnel", { bold: true }), rt(" : pilier → satellites ET satellites → pilier")),
    bul(rt("Chaque article a un CTA cohérent", { bold: true }), rt(" : affiliation OU lead Audit OU newsletter — jamais les 3 en vrac")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // ARTICLE PILIER
  // ───────────────────────────────────────────
  blocks.push(
    h1("2️⃣ Article Pilier — La Fondation du Cluster"),
    p("")
  );

  blocks.push(
    tog(`🏛 "${PILIER.titre}"`, [
      p(""),
      p(rt("Mot-clé principal : ", { bold: true }), rt(PILIER.kw, { code: true })),
      p(rt("Slug cible : ", { bold: true }), rt(`/crm-wordpress/${PILIER.slug}`, { code: true })),
      p(rt("Intent : ", { bold: true }), rt(PILIER.intent, { italic: true })),
      p(rt("Priorité : ", { bold: true }), rt(PILIER.priorite)),
      p(""),
      p(rt("Mots-clés LSI à couvrir :", { bold: true })),
      ...PILIER.mots_cles_lsi.map((k) => bul(k)),
      p(""),
      p(rt("Structure H2 recommandée :", { bold: true })),
      ...PILIER.structure_h2.map((s, i) =>
        tog(`H2 ${i + 1} — ${s.h2}`, [p(""), p(rt("Note éditoriale : ", { bold: true })), p(s.note)])
      ),
      p(""),
      p(rt("CTA principal : ", { bold: true }), rt(PILIER.cta)),
      p(rt("Monétisation : ", { bold: true }), rt(PILIER.monetisation.join(" · "))),
      p(rt("Objectif : ", { bold: true }), rt(PILIER.objectif)),
      p(""),
      p(rt("Commande de production :", { bold: true })),
      bul(
        rt("Workflow W1 recommandé (V1 → Audit → V2) :", { italic: true })
      ),
      bul(
        rt(
          `python -m agents.schoolswp_brain.workflow_cli seo-audit --keyword "crm wordpress" --intent informationnelle --audience "freelance WordPress intermédiaire" --save-dir articles/crm-wordpress/pilier/`,
          { code: true }
        )
      ),
    ])
  );

  blocks.push(p(""), div());

  // ───────────────────────────────────────────
  // SATELLITES — PAR GROUPE
  // ───────────────────────────────────────────
  blocks.push(
    h1("3️⃣ Satellites Stratégiques — 14 Articles"),
    p("")
  );

  const priorityLegend = [
    rt("🔴 M1-M2 — Priorité absolue · "),
    rt("🟠 M2-M3 — Priorité haute · "),
    rt("🟡 M4-M6 — Priorité standard"),
  ];
  blocks.push(p(...priorityLegend));
  blocks.push(p(""));

  for (const groupe of SATELLITES) {
    blocks.push(h2(`📂 ${groupe.groupe} (${groupe.articles.length} articles)`));
    blocks.push(p(""));

    for (const a of groupe.articles) {
      blocks.push(
        tog(`${a.priorite}  "${a.titre}"`, [
          p(""),
          p(rt("Mot-clé : ", { bold: true }), rt(a.kw, { code: true })),
          p(rt("Slug : ", { bold: true }), rt(`/crm-wordpress/${a.slug}`, { code: true })),
          p(rt("Intent : ", { bold: true }), rt(a.intent, { italic: true })),
          p(""),
          p(rt("Angle schoolsWP :", { bold: true })),
          p(a.angle),
          p(""),
          p(rt("LSI à couvrir : ", { bold: true }), rt(a.lsi.join(", "), { italic: true })),
          p(rt("CTA recommandé : ", { bold: true }), rt(a.cta)),
          p(rt("Monétisation : ", { bold: true }), rt(a.monetisation)),
          p(""),
          p(rt("Commande brain-lite :", { bold: true })),
          bul(rt(a.commande, { code: true })),
        ])
      );
    }

    blocks.push(p(""));
  }

  blocks.push(div());

  // ───────────────────────────────────────────
  // PLAN DOMINATION 6 MOIS
  // ───────────────────────────────────────────
  blocks.push(
    h1("4️⃣ Plan Domination 6 Mois"),
    cal(
      "Un article ne suffit pas à dominer. Un cluster structuré, maillé et optimisé LLM prend un territoire durablement.",
      "📅", "orange_background"
    ),
    p("")
  );

  blocks.push(
    tog("📅 Mois 1–2 — Fondations & Comparatifs (priorité absolue)", [
      p(""),
      h3("Semaines 1–2 — L'article pilier"),
      bul("Produire l'article pilier « CRM WordPress : Guide Stratégique Complet »"),
      bul("Workflow W1 : V1 → Audit sémantique → V2 optimisée"),
      bul("Ajouter les blocs Réponse Rapide (1 par H2) pour l'AIO"),
      bul("Configurer le maillage interne sortant vers les futurs satellites"),
      bul("Publier, indexer, soumettre en Search Console"),
      p(""),
      h3("Semaines 3–6 — 3 comparatifs décisionnels"),
      bul("FluentCRM vs MailerLite (M1 — fort trafic, affiliation forte)"),
      bul("FluentCRM vs ActiveCampaign (M1 — CPC élevé, audience premium)"),
      bul("CRM + LMS WordPress architecture (M2 — lead LBS direct)"),
      bul("Mettre à jour le pilier avec des liens vers chaque satellite publié"),
      p(""),
      h3("KPIs M1–M2"),
      bul("4 articles publiés (pilier + 3 satellites)"),
      bul("Maillage interne pilier → satellites + satellites → pilier opérationnel"),
      bul("Premiers CTAs affiliation FluentCRM actifs"),
      bul("1 premier lead Audit via CTA (objectif : 1 appel découverte)"),
    ]),
    p(""),

    tog("📅 Mois 3–4 — Architecture Système & Optimisation LLM", [
      p(""),
      h3("Contenu à produire"),
      bul("WP Fusion vs FluentCRM (M3 — double affiliation)"),
      bul("CRM WordPress vs Systeme.io (M3 — lead migration)"),
      bul("Segmenter contacts WordPress FluentCRM (M3 — informationnelle forte)"),
      bul("Automatisation email WordPress FluentCRM (M3-M4 — article evergreen)"),
      bul("Tunnel email pour formation WordPress (M4 — lead LBS direct)"),
      p(""),
      h3("Optimisation LLM (à faire sur les 4 premiers articles)"),
      bul("Ajouter des blocs FAQ AIO en bas de chaque article (W3 faq-aio)"),
      bul("Structurer les réponses directes en ≤ 4 phrases sans anaphore"),
      bul("Ajouter JSON-LD FAQPage sur le pilier et les 2 comparatifs principaux"),
      bul("Vérifier que chaque article répond à 1 question formulée comme IA"),
      p(""),
      h3("Renforcement maillage interne"),
      bul("Créer la catégorie /crm-wordpress/ avec page de catégorie optimisée"),
      bul("Vérifier que TOUS les satellites pointent vers le pilier"),
      bul("Vérifier que le pilier liste TOUS les satellites publiés"),
      bul("Ajouter 1 CTA Audit visible sur chaque article (sidebar ou inline)"),
      p(""),
      h3("KPIs M3–M4"),
      bul("7 à 9 articles publiés dans le cluster"),
      bul("1 to 2 leads Audit générés"),
      bul("Premiers clics affiliation FluentCRM mesurés"),
      bul("Pilier visible en page 2 ou 3 sur « crm wordpress »"),
    ]),
    p(""),

    tog("📅 Mois 5–6 — Domination & Preuve Sociale", [
      p(""),
      h3("Contenu à produire"),
      bul("CRM WordPress pour coach en ligne (M5 — ultra-niche)"),
      bul("CRM WordPress pour freelance (M5 — audience schoolsWP cible)"),
      bul("CRM WooCommerce (M5 — extension e-commerce)"),
      bul("Automatisation WordPress avec n8n (M5 — lead WBS premium)"),
      bul("Migrer ActiveCampaign vers FluentCRM (M6 — intent migration élevé)"),
      bul("Étude de cas réelle : « Comment j'ai structuré le CRM d'un formateur » (M6)"),
      p(""),
      h3("Mise à jour comparative"),
      bul("Mettre à jour le pilier avec les nouvelles données 2026 si besoin"),
      bul("Mettre à jour les comparatifs avec les nouvelles versions des outils"),
      bul("Ajouter les témoignages ou données réelles dans les articles business"),
      p(""),
      h3("Renforcement CTA Audit"),
      bul("A/B tester 2 formulations de CTA sur le pilier"),
      bul("Ajouter un encadré « Ton CRM WordPress est-il bien structuré ? » avec lien Audit"),
      bul("Créer 1 checklist downloadable « CRM WordPress Starter » (lead magnet)"),
      p(""),
      h3("KPIs M5–M6"),
      bul("12 à 14 articles publiés — cluster quasi-complet"),
      bul("Pilier visible Top 10 sur « crm wordpress »"),
      bul("Affiliation FluentCRM : 200–500 €/mois cumulés"),
      bul("4 à 6 leads Audit générés depuis le cluster"),
      bul("1 client WBS acquis directement depuis le cluster"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // SIGNAUX AUTORITÉ GOOGLE + LLM
  // ───────────────────────────────────────────
  blocks.push(
    h1("5️⃣ Signaux Autorité — Google & LLM"),
    cal(
      "Pour dominer un cluster en 2026 : autorité classique (SEO) + autorité conversationnelle (LLM). Les deux se construisent différemment.",
      "🔍", "blue_background"
    ),
    p(""),

    h2("Signaux Google (SEO classique)"),
    bul(rt("1 pilier long et structuré", { bold: true }), rt(" — 3 000 à 5 000 mots, H2/H3 bien découpés, temps de lecture élevé")),
    bul(rt("10 à 14 satellites minimum", { bold: true }), rt(" — chaque satellite couvre un segment de requêtes du cluster")),
    bul(rt("Maillage bidirectionnel actif", { bold: true }), rt(" — pilier → satellites ET satellites → pilier (ancres naturelles, pas forcées)")),
    bul(rt("Comparaisons factuelles", { bold: true }), rt(" — tableaux, données chiffrées, verdicts clairs — Google récompense la précision")),
    bul(rt("Backlinks naturels", { bold: true }), rt(" — 1 à 2 mentions externes suffisent si le contenu est vraiment supérieur au marché FR")),
    p(""),

    h2("Signaux LLM / AIO (2026)"),
    bul(rt("Blocs « Réponse rapide »", { bold: true }), rt(" — 1 paragraphe de 2 à 4 phrases en début de section H2, autonome hors contexte")),
    bul(rt("Questions formulées comme une IA les pose", { bold: true }), rt(" — « Quel CRM WordPress choisir en 2026 ? » pas « Les avantages du CRM WordPress »")),
    bul(rt("JSON-LD FAQPage", { bold: true }), rt(" — sur le pilier + les 2 comparatifs principaux minimum")),
    bul(rt("Zéro anaphore dans les réponses", { bold: true }), rt(' — chaque réponse FAQ commence par la réponse, pas par "Il faut savoir que..."')),
    bul(rt("Paragraphes ≤ 6 lignes", { bold: true }), rt(" — structure scannable, compatible avec les snippets des moteurs IA")),
    bul(rt("Entités sémantiques explicites", { bold: true }), rt(" — FluentCRM, WP Fusion, Tutor LMS, n8n — nommés et définis dans chaque article")),
    p(""),

    h2("Les 3 blocs à ajouter dans chaque article"),
    tog("📝 Bloc 1 — Réponse Rapide (début de chaque section H2)", [
      p(""),
      p("Modèle :"),
      qot("[RÉPONSE EN 2-3 PHRASES] — directe, sans introduction. Ex : « FluentCRM est un CRM natif WordPress qui stocke les données dans ta propre base de données. Contrairement à MailerLite, il n'y a pas d'abonnement mensuel ni de limite de contacts. »"),
      p(""),
      p("→ Outil : Agent FAQ AIO du Workflow W3 (content-factory)"),
    ]),
    tog("📝 Bloc 2 — FAQ AIO en bas d'article (5 à 7 questions)", [
      p(""),
      p("À générer avec :"),
      bul(rt("python -m agents.schoolswp_brain.workflow_cli content-factory --keyword ... (récupérer faq-aio.md)", { code: true })),
      p(""),
      p("Règle : chaque question doit être formulée exactement comme un utilisateur la poserait à ChatGPT ou Perplexity."),
    ]),
    tog("📝 Bloc 3 — Encadré « Ce qu'il faut retenir » (fin d'article)", [
      p(""),
      p("Modèle :"),
      qot("Ce qu'il faut retenir : [3 bullets. 1 par point clé. Chaque bullet est une phrase autonome compréhensible sans avoir lu l'article.]"),
      p(""),
      p("→ Ce bloc est ce que les LLM extraient en priorité pour construire leurs réponses."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // MAILLAGE INTERNE SCHÉMA
  // ───────────────────────────────────────────
  blocks.push(
    h1("6️⃣ Schéma de Maillage Interne"),
    p(""),
    tog("🗺 Vue du maillage complet du cluster", [
      p(""),
      p(rt("PILIER (centre du cluster)", { bold: true })),
      bul("CRM WordPress : Guide Stratégique Complet"),
      bul("→ reçoit des liens de TOUS les satellites"),
      bul("→ envoie des liens vers TOUS les satellites (section « Pour aller plus loin »)"),
      p(""),
      p(rt("SATELLITES COMPARATIFS (périphérie haute autorité)", { bold: true })),
      bul("FluentCRM vs MailerLite → pilier + satellite automatisation"),
      bul("FluentCRM vs ActiveCampaign → pilier + satellite migration"),
      bul("WP Fusion vs FluentCRM → pilier + satellite CRM+LMS"),
      bul("CRM WordPress vs Systeme.io → pilier + satellite architecture"),
      p(""),
      p(rt("SATELLITES BUSINESS (périphérie éditoriale)", { bold: true })),
      bul("Segmentation contacts → pilier + satellite automatisation"),
      bul("Automatisation email FluentCRM → pilier + tous comparatifs"),
      bul("Tunnel email formation → pilier + satellite CRM+LMS + page offre SASU"),
      bul("CRM + LMS architecture → pilier + satellite Tutor LMS (futur cluster LMS)"),
      p(""),
      p(rt("SATELLITES ULTRA-NICHE (périphérie ciblage)", { bold: true })),
      bul("CRM coach → pilier + satellite segmentation + page offre WBS"),
      bul("CRM freelance → pilier + satellite automatisation + newsletter"),
      bul("CRM WooCommerce → pilier + satellite tunnel email + futur cluster e-commerce"),
      p(""),
      p(rt("RÈGLE : jamais de lien orphelin.", { bold: true })),
      bul("Chaque satellite pointe vers le pilier ET vers 1 à 2 autres satellites naturels."),
      bul("Le pilier liste tous les satellites publiés dans une section dédiée en bas."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // IMPACT BUSINESS
  // ───────────────────────────────────────────
  blocks.push(
    h1("7️⃣ Impact Business du Cluster"),
    p(""),

    h2("Les 4 sources de revenus du cluster"),
    tog("💰 Affiliation récurrente", [
      p(""),
      bul("FluentCRM — commission récurrente sur les abonnements annuels"),
      bul("WP Fusion — commission élevée sur licence annuelle (produit premium)"),
      bul("Groundhogg — alternative à considérer pour les articles comparatifs"),
      bul("Hébergeurs WordPress performants (Kinsta, WPCloud, WPServeur) — dans les articles performance"),
      p(""),
      p(rt("Estimation M12 : 300 à 800 €/mois d'affiliation récurrente sur ce cluster seul.", { bold: true })),
    ]),
    p(""),
    tog("🎯 Leads qualifiés Audit", [
      p(""),
      bul("Chaque article business (architecture, tunnel, CRM+LMS) est un CTA naturel vers l'Audit WBS"),
      bul("Les prospects qui lisent ces articles sont exactement les ICP du WBS Standard et Premium"),
      bul("Estimation : 1 lead qualifié tous les 2 à 3 semaines à partir de M4"),
      p(""),
      p(rt("1 client WBS issu du cluster = 4 000 à 12 000 € CA.", { bold: true })),
    ]),
    p(""),
    tog("📧 Abonnés newsletter qualifiés", [
      p(""),
      bul("Les articles ultra-niche (coach, freelance) attirent l'audience cible de schoolsWP"),
      bul("CTA newsletter en fin d'articles informationnels (pas de vente, valeur directe)"),
      bul("Objectif : 50 à 100 abonnés qualifiés par mois issus du cluster CRM à M6"),
    ]),
    p(""),
    tog("🚀 Positionnement expert différenciant", [
      p(""),
      bul("Être référencé sur « CRM WordPress » = signal d'autorité immédiat pour les prospects"),
      bul("Les articles complexes (architecture, migration) prouvent la maîtrise technique"),
      bul("Le ton non-commercial et les recommandations claires créent la confiance avant le premier contact"),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // BOULE DE NEIGE
  // ───────────────────────────────────────────
  blocks.push(
    h1("8️⃣ Effet Boule de Neige — L'Empire WordPress Systems"),
    cal(
      "Une fois CRM dominé, tu as les fondations. Chaque nouveau cluster s'appuie sur le précédent — et chaque lien interne renforce l'ensemble.",
      "🚀", "purple_background"
    ),
    p(""),

    h2("Les 4 clusters suivants (après CRM)"),
    tog("📂 Cluster 2 — LMS WordPress (M7–M12)", [
      p(""),
      bul("Pilier : « LMS WordPress : Guide Stratégique Complet 2026 »"),
      bul("Satellites : Tutor LMS vs LearnDash / Tutor LMS vs LearnPress / LMS pour formateur / LMS B2B corporate / Certification WordPress..."),
      bul("Pont avec CRM : article CRM+LMS (déjà produit en M2) devient le nœud de connexion"),
      bul("Monétisation : affiliation Tutor LMS + leads LBS™"),
    ]),
    tog("📂 Cluster 3 — E-Commerce WordPress (M9–M18)", [
      p(""),
      bul("Pilier : « WooCommerce en 2026 : guide stratégique pour vendre en ligne »"),
      bul("Satellites : WooCommerce vs Shopify / Paiement WordPress / CRM WooCommerce (déjà produit) / Upsell WooCommerce..."),
      bul("Pont avec CRM : article CRM WooCommerce (déjà produit en M5) devient le nœud"),
      bul("Monétisation : affiliation WooCommerce extensions + leads WBS e-commerce"),
    ]),
    tog("📂 Cluster 4 — Performance & Hébergement WordPress (M12+)", [
      p(""),
      bul("Pilier : « Hébergement WordPress : comment choisir selon son activité »"),
      bul("Satellites : comparatifs hébergeurs / cache WordPress / CDN / Core Web Vitals..."),
      bul("Pont avec CRM/LMS : « Performance WordPress pour formateur » (angle LBS)"),
      bul("Monétisation : affiliation hébergeurs (commissions élevées, récurrentes)"),
    ]),
    tog("📂 Cluster 5 — Automatisation WordPress & n8n (M12+)", [
      p(""),
      bul("Pilier : « Automatisation WordPress : ce que tu peux faire sans coder »"),
      bul("Satellites : n8n WordPress / Zapier vs n8n / Automatisation CRM (lien avec cluster CRM) / Webhook WordPress..."),
      bul("Pont avec CRM : article n8n+FluentCRM (déjà produit en M5) devient le nœud"),
      bul("Monétisation : leads WBS Premium (n8n = signal client budget élevé)"),
    ]),
    p(""),
    qot("Dans 24 mois : 4 clusters actifs, 50+ articles maillés, autorité transversale sur « WordPress Systems ». C'est un actif qui vaut plusieurs années de CA."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // DASHBOARD ACTIONS
  // ───────────────────────────────────────────
  blocks.push(
    h1("📋 Plan d'Action — Démarrage Cluster CRM"),
    p(""),

    h2("🔴 Semaine 1 — Configuration"),
    tod("Créer la catégorie WordPress /crm-wordpress/ avec page de catégorie optimisée"),
    tod("Préparer le brief pilier « CRM WordPress Guide Stratégique »"),
    tod("Lancer le Workflow W1 sur le mot-clé « crm wordpress »"),
    tod("Configurer le tracking affiliation FluentCRM (liens tracés par article)"),
    tod("Créer le CTA Audit visuel (encadré, bouton) pour les articles du cluster"),
    p(""),

    h2("🔴 Semaine 2–3 — Pilier + 1er satellite"),
    tod("Publier l'article pilier (après révision V2 du Workflow W1)"),
    tod("Produire « FluentCRM vs MailerLite » avec brain-lite"),
    tod("Publier satellite 1, ajouter maillage bidirectionnel"),
    tod("Soumettre les 2 URLs en Search Console pour indexation accélérée"),
    tod("Valider que les JSON-LD FAQPage sont présents et valides"),
    p(""),

    h2("🟠 Mois 1–2 — Rythme cluster"),
    tod("Publier 1 article cluster par semaine (alternance comparatif / business)"),
    tod("Mettre à jour le pilier avec les liens vers chaque satellite publié"),
    tod("Vérifier les CTAs affiliation dans chaque article"),
    tod("Suivre chaque semaine : clics affiliation + leads Audit + trafic cluster"),
    tod("Revue de mi-parcours à M2 : ajuster les articles selon les signaux GSC"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // VISION CLUSTER
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧩 Vision — Cluster CRM à M12"),
    p(""),
    tog("📌 État cible M12 — Cluster CRM WordPress dominé", [
      p(""),
      bul("14 articles publiés (pilier + 13 satellites)"),
      bul("Pilier Top 5 sur « crm wordpress » en FR"),
      bul("3 à 5 satellites Top 10 sur leurs mots-clés respectifs"),
      bul("Affiliation FluentCRM : 300 à 600 €/mois récurrents"),
      bul("4 à 8 leads Audit WBS générés depuis le cluster"),
      bul("1 à 2 clients WBS directement attribuables au cluster"),
      bul("Cluster LMS WordPress en cours de démarrage (articles de pont actifs)"),
      p(""),
      p(rt("Valeur estimée du cluster à M12 : 8 000 à 20 000 € de CA générés (affiliation + missions WBS)", { bold: true })),
    ]),
    p(""),
    cal(
      "Un cluster bien construit vaut 3 ans de contenu généraliste. Tu ne fais pas du volume — tu prends un territoire.",
      "⚡", "yellow_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Cluster Domination — CRM WordPress & Automatisation...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  const totalSatellites = SATELLITES.reduce((s, g) => s + g.articles.length, 0);
  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);
  console.log(`   1 pilier + ${totalSatellites} satellites · 4 groupes`);

  // Batch 1 — Création de la page
  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎯" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🎯 Cluster Domination — CRM WordPress & Automatisation" } },
        ],
      },
    },
    children: batches[0],
  });

  const pageId = page.id;
  console.log(`  ✅ Page créée : ${page.url}`);

  // Batches suivants
  for (let i = 1; i < batches.length; i++) {
    await sleep(600);
    console.log(`\n📦 Ajout batch ${i + 1}/${batches.length}...`);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, {
      children: batches[i],
    });
    console.log(`  ✅ Batch ${i + 1} ajouté`);
  }

  console.log("\n✅  Page créée avec succès !");
  console.log(`   URL : ${page.url}`);
  console.log("\n   Contenu :");
  console.log("   🧠  Pourquoi ce cluster — 6 raisons stratégiques");
  console.log("   1️⃣  Positionnement — territoire vs outil");
  console.log(`   2️⃣  Pilier — structure H2 détaillée (${PILIER.structure_h2.length} sections)`);
  console.log(`   3️⃣  ${totalSatellites} Satellites — 4 groupes, intent + angle + commande production`);
  console.log("   4️⃣  Plan 6 mois — M1-M2 / M3-M4 / M5-M6 avec KPIs");
  console.log("   5️⃣  Signaux Autorité — Google + LLM + 3 blocs à intégrer");
  console.log("   6️⃣  Schéma de maillage interne complet");
  console.log("   7️⃣  Impact Business — 4 sources de revenus chiffrées");
  console.log("   8️⃣  Boule de neige — 4 clusters suivants");
  console.log("   📋  Plan d'action (checkboxes démarrage)");
  console.log("   🧩  Vision M12 — valeur estimée du cluster");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

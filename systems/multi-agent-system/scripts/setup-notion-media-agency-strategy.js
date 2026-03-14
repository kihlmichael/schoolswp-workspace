#!/usr/bin/env node
/**
 * setup-notion-media-agency-strategy.js
 * Crée la page "Stratégie Mix Média + Agency — schoolsWP × SASU" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-media-agency-strategy.js
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

const h1 = (text) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(text)] } });
const h2 = (text) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(text)] } });
const h3 = (text) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(text)] } });
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (text) => ({
  object: "block", type: "numbered_list_item",
  numbered_list_item: { rich_text: [rt(text)] },
});
const tod = (text, checked = false) => ({
  object: "block", type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (text) => ({
  object: "block", type: "quote",
  quote: { rich_text: [rt(text)] },
});
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  return [
    // EN-TÊTE
    cal(
      "schoolsWP = machine d'autorité · SASU = machine de cash premium → sans cannibalisation, sans confusion, sans dilution de positionnement.",
      "🧠", "purple_background"
    ),
    p(rt("Mis à jour : mars 2026", { color: "gray" })),
    div(),

    // ───────────────────────────────────────────
    // 1 — RÔLE DE CHAQUE ENTITÉ
    // ───────────────────────────────────────────
    h1("1️⃣ Rôle clair de chaque entité"),
    p("Deux entités. Une mission unifiée. Zéro confusion entre les deux."),
    p(""),

    h2("🟢 schoolsWP — Autorité · Audience · Confiance"),
    cal("Pédagogue expert WordPress orienté systèmes.", "🟢", "green_background"),
    p(""),

    h3("Mission"),
    bul("Éduquer — expliquer WordPress sans jargon inutile"),
    bul("Comparer — analyses objectives, sans bullshit"),
    bul("Structurer — donner de la méthode, pas juste de l'info"),
    bul("Construire l'expertise publique de Michaël KIHL"),
    p(""),

    h3("Monétisation schoolsWP"),
    bul(rt("Affiliation", { bold: true }), rt(" — plugins, hébergeurs, outils testés et recommandés")),
    bul(rt("Produits digitaux", { bold: true }), rt(" — formations, templates, guides premium")),
    bul(rt("Newsletter", { bold: true }), rt(" — base qualifiée, monétisation directe ou sponsoring")),
    bul(rt("Sponsoring", { bold: true }), rt(" — partenariats ciblés, non intrusifs")),
    p(""),

    h2("🔵 SASU — Transformation · Implémentation · Premium"),
    cal("Architecte de systèmes WordPress rentables.", "🔵", "blue_background"),
    p(""),

    h3("Mission"),
    bul("Implémenter — construire les systèmes concrets"),
    bul("Structurer — architecture WordPress orientée performance et business"),
    bul("Optimiser — transformer un site existant en levier de CA"),
    bul("Automatiser — CRM, emails, LMS, flux de vente"),
    bul("Accompagner — suivi stratégique long terme"),
    p(""),

    h3("Monétisation SASU"),
    bul(rt("Audit stratégique", { bold: true }), rt(" — 1 000 à 2 000 € · porte d'entrée qualifiante")),
    bul(rt("Systèmes WordPress structurés", { bold: true }), rt(" — 4 000 à 15 000 € · implémentation complète")),
    bul(rt("Maintenance stratégique", { bold: true }), rt(" — 300 à 900 €/mois · revenus récurrents")),
    bul(rt("Accompagnement", { bold: true }), rt(" — suivi mensuel, optimisation continue")),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 2 — PONT STRATÉGIQUE
    // ───────────────────────────────────────────
    h1("2️⃣ Le Pont Stratégique"),
    cal(
      "schoolsWP ne vend pas directement des prestations. Il vend de la clarté, de la méthode, de la vision — puis oriente naturellement vers la SASU.",
      "🎯", "yellow_background"
    ),
    p(""),

    h2("Le tunnel naturel schoolsWP → SASU"),
    num("L'audience lit un article décisionnel sur schoolsWP"),
    num("Elle gagne en clarté — mais réalise la complexité de son propre système"),
    num("Le CTA l'invite à un audit stratégique (pas à un devis)"),
    num("L'audit qualifie le prospect et révèle la valeur du projet"),
    num("La mission SASU se justifie seule — zéro vente forcée"),
    p(""),

    h2("Les 3 CTAs stratégiques schoolsWP"),
    bul(rt("→ ", { bold: true }), rt("Audit Stratégique WordPress — 1h, avec livrables (1 000–2 000 €)")),
    bul(rt("→ ", { bold: true }), rt("Diagnostic WordPress Business — formulaire qualifiant (gratuit)")),
    bul(rt("→ ", { bold: true }), rt("Appel Architecture Système — pour projets structurés (30 min)")),
    p(""),
    qot("C'est subtil. Pas agressif. Le prospect se qualifie lui-même avant d'arriver."),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 3 — FUNNEL
    // ───────────────────────────────────────────
    h1("3️⃣ Architecture Funnel Idéale"),
    p(""),

    h2("Étape 1 — Article SEO décisionnel (schoolsWP)"),
    p("Des articles qui répondent aux vraies questions business :"),
    bul('"CRM WordPress : lequel choisir selon votre activité ?"'),
    bul('"Tutor LMS vs Systeme.io : pour qui ?"'),
    bul('"Comment structurer un site WordPress rentable ?"'),
    bul('"FluentCRM vs ActiveCampaign : que choisir en 2026 ?"'),
    p(""),

    h2("Étape 2 — CTA intelligent (en bas d'article)"),
    cal(
      "Si tu veux structurer ton système WordPress correctement, je propose un audit stratégique personnalisé. → [Voir l'Audit Stratégique]",
      "💬", "gray_background"
    ),
    p(""),

    h2("Étape 3 — Formulaire qualifiant (4 questions)"),
    bul("Chiffre d'affaires actuel ?"),
    bul("Outils WordPress utilisés (CRM, LMS, hébergeur) ?"),
    bul("Objectif principal : CA, leads, formations, automatisation ?"),
    bul("Budget envisagé pour structurer ton système ?"),
    p(""),

    h2("Étape 4 — Appel Architecture Système"),
    p("Pas « création de site ». Mais :"),
    bul(rt("Architecture", { bold: true }), rt(" — pages, flux, connexions entre les outils")),
    bul(rt("Optimisation", { bold: true }), rt(" — vitesse, conversion, maillage interne")),
    bul(rt("Automatisation", { bold: true }), rt(" — CRM, LMS, emails transactionnels, tunnels")),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 4 — RATIO CONTENU
    // ───────────────────────────────────────────
    h1("4️⃣ Ratio Contenu Stratégique"),
    cal("À partir de maintenant : 40 % informationnel · 40 % décisionnel · 20 % architecture système", "📈", "orange_background"),
    p(""),

    h2("40 % — Contenu Informationnel"),
    p("Éduquer, expliquer, comparer. Base SEO longue traîne."),
    bul("Tutoriels pas-à-pas (plugin, config, optimisation WordPress)"),
    bul("Comparatifs objectifs (Yoast vs Rank Math, FluentCRM vs WP Fusion…)"),
    bul("Guides de démarrage (LMS, CRM, hébergement, performance)"),
    p(""),

    h2("40 % — Contenu Décisionnel"),
    p("Aider à choisir. Identifier les bons contextes. Réduire l'hésitation."),
    bul('"Lequel choisir selon votre activité ?"'),
    bul('"Pour qui c'est adapté — et pour qui ce n'est pas fait"'),
    bul('"Ce que j'aurais fait différemment si je recommençais"'),
    bul("Comparatifs avec recommandation business claire en conclusion"),
    p(""),

    h2("20 % — Contenu Orienté Architecture Système"),
    p("Démontrer l'expertise systémique. Générer les leads premium."),
    bul('"Comment j'ai structuré le système WordPress d'un formateur LMS"'),
    bul('"Automatisation CRM → LMS → Email : mon architecture complète"'),
    bul('"Pourquoi 80 % des sites WordPress ne génèrent pas de CA"'),
    bul('"Le stack WordPress que j'utilise pour mes clients en 2026"'),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 5 — MONÉTISATION CROISÉE
    // ───────────────────────────────────────────
    h1("5️⃣ Logique de Monétisation Croisée"),
    cal(
      "Un article peut générer : 100 € affiliation + 1 lead + 1 client à 3 000 € + 1 témoignage + 1 étude de cas. Ce n'est plus du SEO. C'est du capital actif.",
      "💰", "green_background"
    ),
    p(""),

    h2("La pyramide de valeur d'un article décisionnel"),
    tog("📊 Revenus potentiels d'un seul article — détail", [
      p(""),
      bul(rt("Affiliation : ", { bold: true }), rt("50 à 300 €/an — recommandation plugin ou hébergeur")),
      bul(rt("Newsletter : ", { bold: true }), rt("1 à 3 abonnés qualifiés par mois")),
      bul(rt("Lead SASU : ", { bold: true }), rt("1 prospect qualifié tous les 2-3 mois")),
      bul(rt("Client SASU : ", { bold: true }), rt("1 client/an = 3 000 à 10 000 €")),
      bul(rt("Étude de cas : ", { bold: true }), rt("crédibilité + contenu futur")),
      bul(rt("Notoriété : ", { bold: true }), rt("backlinks, mentions, opportunités")),
      p(""),
      qot("Un bon article peut valoir 5 000 à 15 000 € de valeur cumulée sur 2 ans."),
    ]),
    p(""),

    h2("La règle des 3 actifs par article"),
    num("1 actif SEO — ranking longue durée (trafic passif)"),
    num("1 actif affiliation — recommandation prouvée (revenu passif)"),
    num("1 actif lead — CTA vers audit ou formulaire (CA actif)"),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 6 — DIFFÉRENCIATION
    // ───────────────────────────────────────────
    h1("6️⃣ Différenciation Forte"),
    p(""),

    h2("Ce que tu n'es pas"),
    bul(rt("✗  ", { bold: true }), rt('"Encore un freelance WordPress"')),
    bul(rt("✗  ", { bold: true }), rt("Le prestataire qui fait des sites pas chers")),
    bul(rt("✗  ", { bold: true }), rt("Le blogueur qui liste des plugins sans angle business")),
    bul(rt("✗  ", { bold: true }), rt("L'agence digitale généraliste sans positionnement clair")),
    p(""),

    h2("Ce que tu es"),
    cal(
      "L'expert qui pense WordPress comme un système business complet. Très peu le font. C'est ton avantage structurel.",
      "🎯", "purple_background"
    ),
    p(""),
    bul(rt("✓  ", { bold: true }), rt("Tu maîtrises le contenu SEO de longue traîne")),
    bul(rt("✓  ", { bold: true }), rt("Tu maîtrises l'automatisation (n8n, FluentCRM, LMS)")),
    bul(rt("✓  ", { bold: true }), rt("Tu maîtrises les systèmes WordPress rentables")),
    bul(rt("✓  ", { bold: true }), rt("Tu maîtrises le positionnement et la communication premium")),
    p(""),

    h2("Les 2 messages de positionnement"),
    qot("schoolsWP — WordPress. Clair. Structuré. Utile."),
    p(""),
    qot("SASU — Architecte de systèmes WordPress rentables, pour freelances, formateurs et entrepreneurs qui veulent un WordPress qui travaille pour eux."),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 7 — PLAN 12 MOIS
    // ───────────────────────────────────────────
    h1("7️⃣ Plan 12 Mois Recommandé"),
    p(""),

    tog("📅 Mois 1–3 — Fondations & Premier Cluster", [
      p(""),
      h3("Objectif : Dominer 1 cluster fort"),
      bul("Choisir le cluster prioritaire : CRM WordPress ou LMS WordPress"),
      bul("Produire 5 articles décisionnels (brain-lite ou Workflow W1)"),
      bul("Créer la Page Audit Stratégique SASU avec formulaire qualifiant"),
      bul("Intégrer les 3 CTAs dans chaque article du cluster"),
      bul("Ouvrir la newsletter et collecter les premiers abonnés"),
      p(""),
      h3("KPIs Mois 1–3"),
      bul("5 articles publiés dans le cluster"),
      bul("1 page Audit en ligne avec formulaire opérationnel"),
      bul("1 premier client audit (objectif : 1 000 €)"),
      bul("50 abonnés newsletter qualifiés"),
      bul("1 premier revenu affiliation (même symbolique)"),
    ]),
    p(""),

    tog("📅 Mois 4–6 — Preuve Sociale & Offre Signature", [
      p(""),
      h3("Objectif : Asseoir la crédibilité"),
      bul("Publier 2 études de cas clients (avec permission)"),
      bul("Collecter 3 témoignages structurés (résultat avant/après)"),
      bul("Finaliser l'offre signature SASU (Audit + Système + Maintenance)"),
      bul("Lancer le 2ème cluster (LMS si CRM d'abord, et inversement)"),
      bul("Tester 1 produit digital simple (template ou guide à 29–49 €)"),
      bul("Publier 1 article Architecture Système par mois"),
      p(""),
      h3("KPIs Mois 4–6"),
      bul("2 études de cas publiées sur schoolsWP"),
      bul("1 offre Système WordPress Structuré vendue (4 000–8 000 €)"),
      bul("150 abonnés newsletter"),
      bul("Revenu affiliation cumulé : 500 €+"),
    ]),
    p(""),

    tog("📅 Mois 7–12 — Domination & Positionnement Premium", [
      p(""),
      h3("Objectif : Scaler sans diluer"),
      bul("Optimiser les CTAs (A/B test sur les articles à fort trafic)"),
      bul("SEO : viser Top 3 sur les 5 articles clés du cluster dominant"),
      bul("Assumer le positionnement premium (tarifs, page offre, communication)"),
      bul("Structurer le MRR maintenance (objectif 3 clients récurrents)"),
      bul("Lancer 1 newsletter payante ou produit digital > 99 €"),
      bul("Préparer 1 webinaire ou atelier live pour l'audience schoolsWP"),
      p(""),
      h3("KPIs Mois 7–12"),
      bul("Top 3 sur au moins 3 mots-clés du cluster principal"),
      bul("MRR maintenance : 900 à 2 700 €/mois (3 à 9 clients)"),
      bul("CA SASU cumulé Année 1 : objectif 40 000 à 60 000 €"),
      bul("Newsletter : 500+ abonnés qualifiés"),
      bul("Revenu affiliation cumulé : 2 000 à 5 000 €"),
    ]),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // 8 — AVANTAGE STRATÉGIQUE
    // ───────────────────────────────────────────
    h1("8️⃣ Avantage Stratégique — L'Agency Invisible"),
    cal(
      "Tu peux créer une agency invisible mais ultra qualitative. Personne ne voit le business — tout le monde voit l'expertise.",
      "🔥", "red_background"
    ),
    p(""),

    h2("Comment fonctionne l'Agency Invisible"),
    bul(rt("schoolsWP attire l'audience", { bold: true }), rt(" → jamais de cold outreach, zéro démarchage")),
    bul(rt("Le contenu filtre les prospects", { bold: true }), rt(" → seuls les bons profils arrivent")),
    bul(rt("L'audit qualifie", { bold: true }), rt(" → zéro mauvais client, zéro négociation inutile")),
    bul(rt("Le projet se justifie seul", { bold: true }), rt(" → l'audit révèle le potentiel, le client se convainc")),
    bul(rt("Le témoignage alimente le contenu", { bold: true }), rt(" → boucle vertueuse media → client → preuve → media")),
    p(""),

    h2("Pourquoi c'est rare"),
    bul("La plupart des freelances WordPress font du démarchage ou des plateformes (Malt, ComeUp)"),
    bul("Très peu construisent un actif médiatique qui génère des leads premium en passif"),
    bul("Encore moins combinent : contenu SEO + automatisation + positionnement systémique"),
    bul(rt("→ Tu as les 3. C'est une combinaison que 99 % des freelances n'ont pas.", { bold: true })),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // DASHBOARD ACTIONS
    // ───────────────────────────────────────────
    h1("📋 Tableau de Bord Actions"),
    p(""),

    h2("🟢 Actions schoolsWP — Contenu & Audience"),
    tod("Définir le cluster prioritaire (CRM ou LMS WordPress)"),
    tod("Lancer 5 articles décisionnels via brain-lite ou Workflow W1"),
    tod("Intégrer les CTAs Audit dans chaque article du cluster"),
    tod("Mettre en place le formulaire de qualification (Gravity Forms ou Tally)"),
    tod("Planifier le calendrier éditorial 3 mois (ratio 40/40/20)"),
    tod("Ouvrir et structurer la newsletter (Brevo ou MailPoet)"),
    tod("Configurer le tracking affiliation sur les articles clés"),
    p(""),

    h2("🔵 Actions SASU — Offre & Clients"),
    tod("Finaliser la page Audit Stratégique (1 000–2 000 €)"),
    tod("Rédiger la page Système WordPress Structuré (4 000–8 000 €)"),
    tod("Préparer le template d'audit livrable (PDF ou page Notion partagée)"),
    tod("Définir la grille de qualification prospect (4 questions)"),
    tod("Créer le process onboarding client (Notion ou ClickUp)"),
    tod("Configurer Cal.com ou Calendly pour les appels découverte"),
    tod("Préparer le contrat SASU type et les CGV"),
    p(""),

    h2("🎯 Actions Stratégiques Croisées"),
    tod("Publier 1 article Architecture Système par mois dès M1"),
    tod("Créer 1 étude de cas (projet test ou bénévole si besoin pour démarrer)"),
    tod("Suivre chaque semaine : trafic / leads / CA / abonnés newsletter"),
    tod("Revue stratégique planifiée à M3, M6, M9, M12"),
    tod("Tester 1 produit digital simple entre M4 et M6"),
    p(""),
    div(),

    // ───────────────────────────────────────────
    // RÉCAP VISUEL
    // ───────────────────────────────────────────
    h1("🧩 Récapitulatif Stratégique"),
    p(""),

    tog("📌 Vue d'ensemble en un coup d'œil", [
      p(""),
      p(rt("schoolsWP — Média d'autorité", { bold: true })),
      bul("Mission : Éduquer · Comparer · Structurer"),
      bul("Monétisation : Affiliation + Produits digitaux + Newsletter + Sponsoring"),
      bul("Positionnement : Pédagogue expert WordPress orienté systèmes"),
      p(""),
      p(rt("SASU — Agency premium", { bold: true })),
      bul("Mission : Implémenter · Optimiser · Automatiser · Accompagner"),
      bul("Monétisation : Audit (1–2k) + Systèmes (4–15k) + Maintenance (300–900 €/m)"),
      bul("Positionnement : Architecte de systèmes WordPress rentables"),
      p(""),
      p(rt("Le Pont stratégique", { bold: true })),
      bul("Contenu décisionnel → CTA Audit → Formulaire → Appel → Mission SASU"),
      bul("Ratio : 40 % info · 40 % décisionnel · 20 % architecture système"),
      p(""),
      p(rt("L'équation gagnante", { bold: true })),
      bul("1 article bien positionné = capital actif de 5 000 à 15 000 € sur 2 ans"),
      bul("Agency invisible = zéro démarchage + prospects qui se pré-qualifient"),
      bul("3 actifs par article : SEO + Affiliation + Lead"),
    ]),
    p(""),

    cal(
      "Ta force unique : tu maîtrises contenu + automatisation + SEO + systèmes. Cette combinaison, 99 % des freelances ne l'ont pas. C'est ton avantage structurel.",
      "⚡", "yellow_background"
    ),
  ];
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Stratégie Mix Média + Agency...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);

  // Batch 1 — Création de la page
  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🧠" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🧠 Stratégie Mix Média + Agency — schoolsWP × SASU" } },
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
  console.log("\n   Sections :");
  console.log("   1️⃣  Rôle de chaque entité — schoolsWP vs SASU");
  console.log("   2️⃣  Le Pont Stratégique — tunnel naturel en 5 étapes");
  console.log("   3️⃣  Architecture Funnel Idéale — 4 étapes");
  console.log("   4️⃣  Ratio Contenu 40/40/20");
  console.log("   5️⃣  Logique de Monétisation Croisée");
  console.log("   6️⃣  Différenciation Forte — l'Agency Invisible");
  console.log("   7️⃣  Plan 12 Mois — M1-M3 · M4-M6 · M7-M12");
  console.log("   8️⃣  Avantage Stratégique");
  console.log("   📋  Tableau de Bord Actions (checkboxes)");
  console.log("   🧩  Récapitulatif Stratégique");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

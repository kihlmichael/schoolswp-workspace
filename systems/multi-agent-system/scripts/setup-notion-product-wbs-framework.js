#!/usr/bin/env node
/**
 * setup-notion-product-wbs-framework.js
 * Crée la page "🎓 WordPress Business System™ — Le Framework Complet" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-product-wbs-framework.js
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
// Données — modules, pricing, roadmap
// ---------------------------------------------------------------------------

const MODULES = [
  {
    num: "1",
    emoji: "🎯",
    titre: "Vision Stratégique",
    accroche: "Pourquoi 90 % des sites WordPress ne convertissent pas",
    duree: "~35 min",
    videos: [
      { num: "1.1", titre: "Le mythe du site vitrine", duree: "8 min", contenu: "Ce que les agences vendent vs ce dont tu as besoin. La différence entre 'présence web' et 'système business'." },
      { num: "1.2", titre: "Anatomie d'un site WordPress qui convertit", duree: "12 min", contenu: "Les 3 flows essentiels : trafic → lead → client. Ce qui bloque à chaque étape." },
      { num: "1.3", titre: "Les 4 piliers d'un WordPress rentable", duree: "15 min", contenu: "SEO, CRM, Automatisation, Performance — comment ils se renforcent mutuellement." },
    ],
    ressources: [
      "Schéma : Les 4 piliers et leurs connexions",
      "Checklist : Audit rapide de ton site actuel (10 questions)",
      "Tableau : Site vitrine vs Système business (comparatif visuel)",
    ],
    objectif: "Tu identifies exactement pourquoi ton site ne travaille pas pour toi, et tu comprends ce qu'est un système business WordPress.",
  },
  {
    num: "2",
    emoji: "🏗️",
    titre: "Architecture Système",
    accroche: "Structurer l'infrastructure qui convertit en automatique",
    duree: "~40 min",
    videos: [
      { num: "2.1", titre: "Structure de pages essentielles", duree: "10 min", contenu: "Home → Problème → Solution → Preuve → CTA. Les 7 pages qu'un système business WordPress doit avoir." },
      { num: "2.2", titre: "CRM natif vs SaaS : le bon choix", duree: "12 min", contenu: "FluentCRM vs ActiveCampaign vs Brevo. Quand garder nativement, quand connecter une API externe." },
      { num: "2.3", titre: "Tunnel simple qui fonctionne", duree: "10 min", contenu: "Lead magnet → séquence email → page offre. Le minimum viable pour commencer à convertir." },
      { num: "2.4", titre: "Intégrations essentielles", duree: "8 min", contenu: "Stripe/Mollie, Calendly/Cal.com, ConvertPro/FluentForms. Ce qu'il faut connecter, et dans quel ordre." },
    ],
    ressources: [
      "Template : Architecture de site (Figma/PDF exportable)",
      "Checklist : Les 7 pages essentielles avec contenu minimum par page",
      "Tableau comparatif : CRM natif vs SaaS (10 critères)",
      "Schéma : Tunnel simple annoté",
    ],
    objectif: "Tu as un plan d'architecture clair. Tu sais exactement quelles pages créer, quel CRM utiliser et comment structurer ton premier tunnel.",
  },
  {
    num: "3",
    emoji: "⚙️",
    titre: "Automatisation Intelligente",
    accroche: "Faire travailler WordPress pendant que tu dors",
    duree: "~45 min",
    videos: [
      { num: "3.1", titre: "Email stratégique : la séquence qui vend", duree: "12 min", contenu: "Séquence bienvenue 5 emails. Structure : utilité → crédibilité → problème → solution → CTA." },
      { num: "3.2", titre: "Segmentation qui change tout", duree: "10 min", contenu: "Tagger par comportement (clic, téléchargement, visite page prix). Les segments à créer en priorité." },
      { num: "3.3", titre: "3 scénarios automatisés à mettre en place", duree: "13 min", contenu: "1) Abandon page offre. 2) Client inactif 30j. 3) Upsell post-achat. Configuration dans FluentCRM." },
      { num: "3.4", titre: "Stack minimaliste recommandé", duree: "10 min", contenu: "FluentCRM + FluentForms + n8n (ou Zapier). Ce que ça coûte, ce que ça rapporte." },
    ],
    ressources: [
      "Template : Séquence bienvenue 5 emails (textes adaptables)",
      "Schéma : Les 3 scénarios automatisés annotés",
      "Checklist : Configuration FluentCRM étape par étape",
      "Tableau : Stack outils avec prix et alternatives",
    ],
    objectif: "Tu as une séquence email qui travaille, 3 automatisations actives, et un stack d'outils clair pour les 12 prochains mois.",
  },
  {
    num: "4",
    emoji: "🔍",
    titre: "SEO Intelligent",
    accroche: "Attirer du trafic qualifié sans dépenser en pub",
    duree: "~40 min",
    videos: [
      { num: "4.1", titre: "La stratégie cluster : 1 pilier, 8-12 satellites", duree: "12 min", contenu: "Ce qu'est un pilier d'autorité. Comment les satellites alimentent le pilier. Pourquoi ça surpasse les articles indépendants." },
      { num: "4.2", titre: "Articles décisionnels : les seuls qui convertissent", duree: "10 min", contenu: "Différence informationnelle / comparative / décisionnelle. Pourquoi écrire pour l'intention décisionnelle en premier." },
      { num: "4.3", titre: "Maillage interne : le levier sous-estimé", duree: "8 min", contenu: "Règles d'ancre, structure de liens, hiérarchie de pages. Comment 10 liens bien placés valent 50 backlinks." },
      { num: "4.4", titre: "Optimisation LLM : écrire pour 2026", duree: "10 min", contenu: "Ce que ChatGPT/Gemini citent et pourquoi. Format réponse directe, FAQ AIO, entités nommées. Adapter son contenu sans tout réécrire." },
    ],
    ressources: [
      "Template : Structure d'article décisionnel (squelette H2/H3)",
      "Checklist : Audit maillage interne (8 critères)",
      "Schéma : Architecture cluster pour ton site",
      "Template : FAQ AIO optimisée (format question/réponse + JSON-LD)",
    ],
    objectif: "Tu as une stratégie de contenu actionnable. Tu sais quoi écrire, dans quel ordre, avec quelle structure pour attirer et convertir.",
  },
  {
    num: "5",
    emoji: "📈",
    titre: "Optimisation & Passage à l'Échelle",
    accroche: "Mesurer, corriger, accélérer — le système complet",
    duree: "~30 min",
    videos: [
      { num: "5.1", titre: "Les 5 KPIs qui comptent vraiment", duree: "8 min", contenu: "Taux de conversion lead, taux d'ouverture email, coût d'acquisition client, LTV, temps de chargement. Où les trouver, comment les améliorer." },
      { num: "5.2", titre: "Les 7 erreurs qui tuent la croissance", duree: "10 min", contenu: "Trop de plugins, pas de tracking, tunnel complexe, email sans segmentation, SEO sans cluster, pas de CRM, dépendance Google Ads." },
      { num: "5.3", titre: "Plan 90 jours : de zéro à système opérationnel", duree: "12 min", contenu: "Semaines 1-2 : architecture + CRM. Semaines 3-4 : tunnel + email. Mois 2 : SEO + contenu. Mois 3 : automatisations + mesure. Avec jalons concrets." },
    ],
    ressources: [
      "Template : Dashboard KPI (Google Sheets exportable)",
      "Checklist : Les 7 erreurs à éviter (auto-diagnostic)",
      "Plan 90 jours : tableau de bord avec cases à cocher",
      "Guide : Quand passer à une mission agency (signaux à surveiller)",
    ],
    objectif: "Tu sais mesurer la performance de ton système, identifier les blocages, et tu as un plan 90 jours précis pour mettre en place tout ce que tu as appris.",
  },
];

const FORMAT = {
  total_videos: MODULES.reduce((acc, m) => acc + m.videos.length, 0),
  duree_totale: "2h30 à 3h",
  format_video: "Screencast + slides animés, format 1080p",
  hebergement: "Plateforme LMS (SureCart + Tutor LMS ou Lemon Squeezy + Vimeo)",
  acces: "Accès à vie — accès immédiat après paiement",
  updates: "Mises à jour incluses (au moins 1/an)",
  bonus: [
    "Templates Google Sheets (Dashboard KPI + plan 90 jours)",
    "Pack 5 schémas PDF haute résolution",
    "Checklist complète imprimable (50 points de contrôle)",
    "Accès au groupe de suivi schoolsWP (Discord ou cercle privé)",
  ],
};

const PRICING = [
  {
    version: "Lancement — Fondateurs",
    fourchette: "97 à 147 €",
    objectif: "Valider le marché, obtenir les premiers retours, créer la preuve sociale",
    acces: "Accès complet à vie + bonus fondateurs",
    bonus_extra: "Session Q&A live 60 min (groupe, 10 à 20 personnes max)",
    limite: "50 places maximum",
    signal: "Candidat type : indépendant/créateur qui a déjà un site WordPress mais ne convertit pas",
    note: "Le prix de lancement est réservé aux inscrits newsletter — jamais en public direct.",
  },
  {
    version: "Prix Stable",
    fourchette: "197 à 297 €",
    objectif: "Positionnement premium confirmé, filtrage naturel des touristes",
    acces: "Accès complet à vie + toutes les mises à jour futures",
    bonus_extra: "Audit express 30 min (pour les formules à 297 €)",
    limite: "Ouvert en continu après la phase de lancement",
    signal: "Candidat type : formateur/consultant/freelance qui veut autonomiser son acquisition",
    note: "À 297 €, on commence à qualifier des futurs clients agency naturellement.",
  },
];

// Calculs financiers transparents
const calc = () => {
  const lancement_mini = 50 * 97;   // 50 places × 97 €
  const lancement_cible = 50 * 147; // 50 places × 147 €
  const stable_mensuel_mini = 5 * 197;  // 5 ventes/mois × 197 €
  const stable_mensuel_cible = 10 * 297; // 10 ventes/mois × 297 €
  const stable_annuel_mini = stable_mensuel_mini * 12;
  const stable_annuel_cible = stable_mensuel_cible * 12;
  return { lancement_mini, lancement_cible, stable_mensuel_mini, stable_mensuel_cible, stable_annuel_mini, stable_annuel_cible };
};
const FIN = calc();

const ROADMAP_PRODUCTION = [
  {
    semaine: "S1",
    focus: "Outline + Slides",
    objectif: "Tout le contenu est structuré avant d'enregistrer",
    taches: [
      "Valider l'outline final de chaque module (utiliser ce document)",
      "Créer les slides Keynote/Figma pour chaque vidéo",
      "Préparer les schémas et templates (Figma ou Canva)",
      "Rédiger les scripts des vidéos (pas nécessaire de tout mémoriser — bullet points suffisent)",
      "Configurer la plateforme de vente (SureCart ou Lemon Squeezy)",
    ],
  },
  {
    semaine: "S2",
    focus: "Enregistrement",
    objectif: "Toutes les vidéos enregistrées en brut",
    taches: [
      "Setup enregistrement : OBS ou Screenflow, micro correct, fond sobre",
      "Enregistrer Module 1 (3 vidéos) — objectif : 1 module/jour",
      "Enregistrer Module 2 (4 vidéos)",
      "Enregistrer Modules 3, 4, 5 — batch de 2 par session",
      "Enregistrer intro + outro génériques (1 × chacun)",
      "Export brut : 1080p, H.264, fichiers nommés 01-01, 01-02, etc.",
    ],
  },
  {
    semaine: "S3",
    focus: "Montage + Landing Page",
    objectif: "Formation publiée et page de vente en ligne",
    taches: [
      "Montage vidéos : couper silence, ajouter intro/outro, sous-titres si possible",
      "Upload Vimeo (ou hébergeur choisi) — organiser en dossiers par module",
      "Configurer LMS : créer les leçons, uploader les vidéos, ajouter les ressources",
      "Créer la landing page : problem → solution → programme → bonus → prix → CTA",
      "Configurer le checkout SureCart/Lemon Squeezy avec accès automatique post-paiement",
      "Tester le parcours complet (achat → accès → première vidéo)",
    ],
  },
  {
    semaine: "S4",
    focus: "Lancement Newsletter",
    objectif: "50 premiers inscrits — validation marché",
    taches: [
      "Email 1 : annonce teaser — 'Je prépare quelque chose' (sans lien)",
      "Email 2 : lancement officiel — prix fondateurs + lien landing page",
      "Email 3 : J+3 — rappel + témoignage si déjà reçu",
      "Email 4 : J+5 — clôture prix fondateurs (deadline réelle)",
      "Post LinkedIn : lancement avec angle 'ce que j'aurais voulu avoir'",
      "Débriefing post-lancement : ventes, retours, améliorations à noter",
    ],
  },
];

const SYNERGIE_SCHOOLSWP = [
  {
    type: "CTA article → Produit",
    description: "Chaque article schoolsWP sur un sujet couvert par le framework inclut un encadré discret de renvoi.",
    exemple: "Si tu veux structurer tout ça proprement dans ton WordPress, le framework complet explique exactement comment faire — de l'architecture au SEO.",
    articles_cibles: [
      "Comparatif CRM WordPress (FluentCRM vs MailerLite, etc.)",
      "Guide LMS WordPress (Tutor LMS, LearnDash, etc.)",
      "Optimisation WordPress (vitesse, Core Web Vitals)",
      "SEO cluster WordPress",
    ],
  },
  {
    type: "Lead magnet → Produit",
    description: "Le framework devient le 'prochain step' naturel après tout contenu gratuit de schoolsWP.",
    exemple: "Séquence email post-téléchargement : après le lead magnet, email J+3 mentionne le framework.",
    lead_magnets_alimente: [
      "Checklist audit WordPress gratuite",
      "Template architecture CRM",
      "Guide démarrage FluentCRM",
    ],
  },
  {
    type: "Produit → Mission Agency",
    description: "Le framework qualifie naturellement les futurs clients agency. Ceux qui ont besoin d'aide pour implémenter = prospect chaud.",
    tunnel: "Article → Framework (147/297 €) → Email séquence → 'Besoin qu'on le fasse pour vous ?' → Mission agency (3 000 à 12 000 €)",
    taux_conversion_estime: "2 à 5 % des acheteurs deviennent prospects agency dans les 6 mois",
  },
  {
    type: "Contenu → Autorité → Confiance",
    description: "Chaque vente du framework renforce la crédibilité schoolsWP. Les témoignages alimentent les articles, le profil LinkedIn, les futurs produits.",
    actif_généré: "Preuve sociale, cas clients anonymisés, insights marché (pour futurs articles)",
  },
];

const OBJECTIF_CACHE = {
  titre: "Machine à leads qualifiés — le vrai ROI du framework",
  explication: "Le framework ne génère pas que du CA direct. Son rôle stratégique est de filtrer et éduquer les futurs clients agency.",
  profil_acheteur_cible: "Indépendant / formateur / consultant qui a déjà un site WordPress et une activité existante, mais stagne sur l'acquisition ou la conversion.",
  signal_prospect_agency: [
    "Achète et revient avec des questions spécifiques à son cas",
    "Répond aux emails avec 'je n'arrive pas à mettre ça en place'",
    "Pose une question sur la landing page avant d'acheter",
    "Mentionne un CA existant > 30 000 €/an dans sa demande",
  ],
  valeur_indirecte: `Un acheteur à 197 € qui devient client agency à 6 000 € = ROI × 30 sur la vente initiale.`,
  règle: "Ne jamais vendre le framework comme 'entrée de gamme'. Le vendre comme le outil que les pros utilisent pour structurer leur WordPress.",
};

const KPIS = [
  { kpi: "Ventes phase lancement", cible: "30 à 50 unités", outil: "SureCart / Lemon Squeezy dashboard" },
  { kpi: "Taux de conversion landing page", cible: "> 3 % (visiteurs → acheteurs)", outil: "Google Analytics 4" },
  { kpi: "Taux de complétion formation", cible: "> 40 % (terminent Module 5)", outil: "LMS dashboard" },
  { kpi: "Net Promoter Score (NPS)", cible: "> 8/10 en moyenne", outil: "Email de suivi J+7 post-achat" },
  { kpi: "CA mensuel stable (mois 3+)", cible: "1 000 à 3 000 €/mois", outil: "Tableau de bord financier" },
  { kpi: "Leads agency qualifiés générés", cible: "1 à 2 prospects/mois dès M3", outil: "CRM FluentCRM (tag: prospect-agency)" },
  { kpi: "Taux d'ouverture email lancement", cible: "> 35 %", outil: "FluentCRM / Brevo analytics" },
];

// ---------------------------------------------------------------------------
// Template de page
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Mini-programme stratégique — 5 modules, 2h30–3h, ressources actionnables.", "🎓", "green_background"));
  blocks.push(p(rt("Comment structurer un site WordPress rentable, automatisé et scalable.", { italic: true })));
  blocks.push(p(
    rt("Format : ", { bold: true }),
    rt(`${FORMAT.total_videos} vidéos — ${FORMAT.duree_totale} — Accès à vie — Mises à jour incluses`)
  ));
  blocks.push(div());

  // Section 1 — Positionnement
  blocks.push(h1("🎯 Positionnement Produit"));
  blocks.push(cal("Tu ne vends pas 'WordPress pour débutants'. Tu vends : Structurer un système WordPress rentable et automatisé.", "🔥", "orange_background"));
  blocks.push(p(""));
  blocks.push(h3("Promesse principale"));
  blocks.push(qot("Après ce framework, tu sais exactement comment structurer un WordPress qui travaille pour toi — trafic qualifié, leads automatisés, conversions mesurables."));
  blocks.push(p(""));
  blocks.push(h3("Différenciation"));
  blocks.push(bul(rt("Pas de théorie générique"), rt(" — tout est ancré dans des cas WordPress réels et documentés sur schoolsWP")));
  blocks.push(bul(rt("Pas de 40 heures de cours"), rt(" — chaque minute de vidéo = une action concrète à mettre en place")));
  blocks.push(bul(rt("Pas de 'il suffit de'"), rt(" — les vrais blocages sont nommés et des solutions précises sont données")));
  blocks.push(bul(rt("Orienté business"), rt(" — chaque module répond à 'ça rapporte combien ?' et 'ça coûte combien à mettre en place ?'")));
  blocks.push(p(""));
  blocks.push(h3("Audience cible"));
  blocks.push(bul("Freelance WordPress qui veut arrêter de faire 'des sites' et commencer à construire des systèmes"));
  blocks.push(bul("Formateur / consultant avec un site WordPress existant qui ne convertit pas"));
  blocks.push(bul("Indépendant avec une activité en ligne qui stagne sur l'acquisition ou la conversion"));
  blocks.push(bul("Créateur de contenu qui veut monétiser son audience sans dépendre des plateformes"));
  blocks.push(p(""));
  blocks.push(h3("Ce que le framework n'est PAS"));
  blocks.push(bul("Pas un guide de création de site from scratch"));
  blocks.push(bul("Pas un tuto plugin spécifique (Divi, Elementor, etc.)"));
  blocks.push(bul("Pas une promesse de revenus passifs ou de résultats garantis"));
  blocks.push(bul("Pas conçu pour les débutants absolus (HTML/WP déjà connu prérequis)"));
  blocks.push(div());

  // Section 2 — Format
  blocks.push(h1("📦 Format & Structure"));
  blocks.push(p(
    rt("Vidéos : ", { bold: true }),
    rt(`${FORMAT.total_videos} vidéos — Screencast + slides — Format 1080p`)
  ));
  blocks.push(p(
    rt("Durée totale : ", { bold: true }),
    rt(FORMAT.duree_totale)
  ));
  blocks.push(p(
    rt("Hébergement : ", { bold: true }),
    rt(FORMAT.hebergement)
  ));
  blocks.push(p(
    rt("Accès : ", { bold: true }),
    rt(FORMAT.acces)
  ));
  blocks.push(p(""));
  blocks.push(h3("Bonus inclus"));
  FORMAT.bonus.forEach((b) => blocks.push(bul(b)));
  blocks.push(div());

  // Section 3 — Modules
  blocks.push(h1("📚 Programme — 5 Modules Détaillés"));
  blocks.push(p("Chaque module est autonome mais s'enchaîne logiquement. Un apprenant peut commencer par le module qui correspond à son blocage actuel."));
  blocks.push(p(""));

  MODULES.forEach((mod) => {
    blocks.push(h2(`Module ${mod.num} — ${mod.emoji} ${mod.titre}`));
    blocks.push(p(
      rt("Accroche : ", { bold: true }),
      rt(mod.accroche, { italic: true })
    ));
    blocks.push(p(
      rt("Durée estimée : ", { bold: true }),
      rt(mod.duree)
    ));
    blocks.push(p(""));

    // Vidéos en toggle
    const videoChildren = mod.videos.flatMap((v) => [
      p(rt(`${v.num} — ${v.titre}`, { bold: true }), rt(` (${v.duree})`)),
      p(v.contenu),
    ]);
    blocks.push(tog(`▶ Vidéos (${mod.videos.length})`, videoChildren));

    // Ressources
    const ressourceChildren = mod.ressources.map((r) => bul(r));
    blocks.push(tog(`📎 Ressources incluses (${mod.ressources.length})`, ressourceChildren));

    // Objectif module
    blocks.push(cal(mod.objectif, "✅", "green_background"));
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 4 — Pricing
  blocks.push(h1("💰 Stratégie de Prix"));
  blocks.push(cal("Ne pas sous-vendre. Le prix filtre les touristes et qualifie les futurs clients agency.", "⚠️", "yellow_background"));
  blocks.push(p(""));

  PRICING.forEach((tier, i) => {
    blocks.push(h2(`${i === 0 ? "🚀" : "💎"} ${tier.version} — ${tier.fourchette}`));
    blocks.push(p(rt("Objectif : ", { bold: true }), rt(tier.objectif)));
    blocks.push(p(rt("Accès : ", { bold: true }), rt(tier.acces)));
    blocks.push(p(rt("Bonus extra : ", { bold: true }), rt(tier.bonus_extra)));
    if (tier.limite) blocks.push(p(rt("Limite : ", { bold: true }), rt(tier.limite)));
    blocks.push(p(rt("Profil acheteur : ", { bold: true }), rt(tier.signal)));
    blocks.push(qot(tier.note));
    blocks.push(p(""));
  });

  // Projections financières
  blocks.push(h3("📊 Projections financières"));
  blocks.push(tog("Voir les projections détaillées", [
    p(rt("Phase lancement (50 places) :", { bold: true })),
    bul(`Scénario conservateur : ${FIN.lancement_mini.toLocaleString("fr-FR")} € (50 × 97 €)`),
    bul(`Scénario cible : ${FIN.lancement_cible.toLocaleString("fr-FR")} € (50 × 147 €)`),
    p(""),
    p(rt("Phase stable (mensuel) :", { bold: true })),
    bul(`Mini : ${FIN.stable_mensuel_mini.toLocaleString("fr-FR")} €/mois (5 ventes × 197 €)`),
    bul(`Cible : ${FIN.stable_mensuel_cible.toLocaleString("fr-FR")} €/mois (10 ventes × 297 €)`),
    p(""),
    p(rt("Phase stable (annuel) :", { bold: true })),
    bul(`Mini : ${FIN.stable_annuel_mini.toLocaleString("fr-FR")} €/an`),
    bul(`Cible : ${FIN.stable_annuel_cible.toLocaleString("fr-FR")} €/an`),
    p(""),
    cal("Ces projections excluent les revenus agency qualifiés par le produit. Un acheteur converti en mission = ×30 ROI.", "🔑", "purple_background"),
  ]));
  blocks.push(div());

  // Section 5 — Roadmap production
  blocks.push(h1("🗓️ Roadmap de Production — 4 Semaines"));
  blocks.push(cal("Pas besoin de perfection. Un produit à 80 % lancé bat un produit parfait jamais sorti.", "⚡", "orange_background"));
  blocks.push(p(""));

  ROADMAP_PRODUCTION.forEach((sem) => {
    blocks.push(h2(`${sem.semaine} — ${sem.focus}`));
    blocks.push(p(rt("Objectif : ", { bold: true }), rt(sem.objectif)));
    sem.taches.forEach((t) => blocks.push(tod(t)));
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 6 — Synergie schoolsWP
  blocks.push(h1("🔗 Synergie schoolsWP × Framework"));
  blocks.push(p("Le framework ne vit pas en isolation. Il s'intègre dans l'écosystème schoolsWP pour maximiser l'impact à chaque point de contact."));
  blocks.push(p(""));

  SYNERGIE_SCHOOLSWP.forEach((syn) => {
    blocks.push(h3(`${syn.type}`));
    blocks.push(p(syn.description));
    if (syn.exemple) blocks.push(qot(`Exemple : "${syn.exemple}"`));
    if (syn.articles_cibles) {
      blocks.push(p(rt("Articles schoolsWP ciblés :", { bold: true })));
      syn.articles_cibles.forEach((a) => blocks.push(bul(a)));
    }
    if (syn.lead_magnets_alimente) {
      blocks.push(p(rt("Lead magnets alimentés :", { bold: true })));
      syn.lead_magnets_alimente.forEach((l) => blocks.push(bul(l)));
    }
    if (syn.tunnel) blocks.push(p(rt("Tunnel : ", { bold: true }), rt(syn.tunnel)));
    if (syn.taux_conversion_estime) blocks.push(p(rt("Taux estimé : ", { bold: true }), rt(syn.taux_conversion_estime)));
    if (syn.actif_généré) blocks.push(p(rt("Actif généré : ", { bold: true }), rt(syn.actif_généré)));
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 7 — Objectif caché
  blocks.push(h1("🧲 Objectif Caché — Machine à Leads Qualifiés"));
  blocks.push(cal(OBJECTIF_CACHE.titre, "🎯", "purple_background"));
  blocks.push(p(""));
  blocks.push(p(OBJECTIF_CACHE.explication));
  blocks.push(p(""));
  blocks.push(h3("Profil acheteur cible"));
  blocks.push(qot(OBJECTIF_CACHE.profil_acheteur_cible));
  blocks.push(p(""));
  blocks.push(h3("Signaux prospect agency dans les acheteurs"));
  OBJECTIF_CACHE.signal_prospect_agency.forEach((s) => blocks.push(bul(s)));
  blocks.push(p(""));
  blocks.push(cal(OBJECTIF_CACHE.valeur_indirecte, "💡", "green_background"));
  blocks.push(p(""));
  blocks.push(qot(`Règle : ${OBJECTIF_CACHE.règle}`));
  blocks.push(div());

  // Section 8 — KPIs
  blocks.push(h1("📊 KPIs à Suivre"));
  blocks.push(p("Suivre chaque semaine pendant le lancement, puis chaque mois en phase stable."));
  blocks.push(p(""));

  blocks.push(tog("Voir le tableau KPIs complet", [
    ...KPIS.map((k) =>
      p(
        rt(`${k.kpi} : `, { bold: true }),
        rt(`Cible ${k.cible} — Outil : ${k.outil}`)
      )
    ),
  ]));
  blocks.push(p(""));
  blocks.push(div());

  // Section 9 — Checklist de lancement
  blocks.push(h1("✅ Checklist Lancement Complète"));
  blocks.push(p(""));

  blocks.push(h3("Semaine 1 — Contenu"));
  blocks.push(tod("Outline validé pour chaque module"));
  blocks.push(tod("Slides créés (1 deck par module)"));
  blocks.push(tod("Schémas et templates produits (PDF + Figma)"));
  blocks.push(tod("Scripts bullet points écrits pour chaque vidéo"));
  blocks.push(tod("Plateforme de vente configurée (SureCart ou Lemon Squeezy)"));

  blocks.push(p(""));
  blocks.push(h3("Semaine 2 — Enregistrement"));
  blocks.push(tod("Setup enregistrement testé (OBS, micro, fond)"));
  blocks.push(tod("Modules 1 et 2 enregistrés (7 vidéos)"));
  blocks.push(tod("Modules 3, 4 et 5 enregistrés (11 vidéos)"));
  blocks.push(tod("Intro et outro génériques enregistrés"));
  blocks.push(tod("Fichiers exportés et nommés correctement (01-01, 01-02...)"));

  blocks.push(p(""));
  blocks.push(h3("Semaine 3 — Production & Technique"));
  blocks.push(tod("Montage vidéos terminé (coupes, intro/outro, sous-titres)"));
  blocks.push(tod("Vidéos uploadées sur Vimeo ou hébergeur choisi"));
  blocks.push(tod("LMS configuré (leçons, vidéos, ressources)"));
  blocks.push(tod("Landing page publiée (problem → solution → programme → prix → CTA)"));
  blocks.push(tod("Checkout configuré avec accès automatique post-paiement"));
  blocks.push(tod("Parcours complet testé (achat → accès → vidéo 1)"));

  blocks.push(p(""));
  blocks.push(h3("Semaine 4 — Lancement"));
  blocks.push(tod("Email 1 envoyé : annonce teaser (sans lien)"));
  blocks.push(tod("Email 2 envoyé : lancement + prix fondateurs + lien"));
  blocks.push(tod("Email 3 envoyé : J+3 rappel + premier témoignage si disponible"));
  blocks.push(tod("Email 4 envoyé : J+5 clôture prix fondateurs (deadline réelle)"));
  blocks.push(tod("Post LinkedIn publié"));
  blocks.push(tod("Débriefing post-lancement documenté (ventes, retours, améliorations)"));

  blocks.push(p(""));
  blocks.push(div());

  // Footer
  blocks.push(cal("Ce framework est le pont entre schoolsWP et l'Agency. Chaque vente = un lead éduqué, qualifié, prêt pour la mission suivante.", "🏁", "green_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'WordPress Business System™ — Le Framework Complet'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎓" },
    properties: {
      title: { title: [{ text: { content: "WordPress Business System™ — Le Framework Complet" } }] },
    },
    children: batch1,
  });

  const pageId = pageRes.id;
  console.log(`✅ Page créée : ${pageId}`);

  for (let i = 1; i < totalBatches; i++) {
    const start = i * CHUNK;
    const end = Math.min(start + CHUNK, totalBlocks);
    const batch = template.slice(start, end);
    console.log(`⏳ Batch ${i + 1}/${totalBatches} (blocs ${start + 1}–${end})...`);
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, { children: batch });
    console.log(`✅ Batch ${i + 1} ajouté.`);
  }

  console.log("");
  console.log("🎉 Page créée avec succès !");
  console.log(`🔗 https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📋 Récapitulatif :");
  console.log(`   • ${MODULES.length} modules détaillés`);
  console.log(`   • ${FORMAT.total_videos} vidéos documentées`);
  console.log(`   • ${PRICING.length} niveaux de prix avec projections`);
  console.log(`   • ${ROADMAP_PRODUCTION.length} semaines de roadmap production`);
  console.log(`   • ${SYNERGIE_SCHOOLSWP.length} synergies schoolsWP documentées`);
  console.log(`   • ${KPIS.length} KPIs de suivi`);
  console.log(`   • Checklist lancement complète`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

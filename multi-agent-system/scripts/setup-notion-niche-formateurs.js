#!/usr/bin/env node
/**
 * setup-notion-niche-formateurs.js
 * Crée la page "🎓 Niche Formateurs — Architecte WordPress des Formateurs Ambitieux" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-niche-formateurs.js
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
// Données
// ---------------------------------------------------------------------------

const PROBLEMES_NICHE = [
  {
    emoji: "🔴",
    probleme: "LMS mal structuré",
    symptomes: [
      "Formation créée sans réfléchir à l'arborescence (module > section > leçon)",
      "Pas de prérequis, pas de progression logique, apprenants perdus",
      "Taux de complétion < 30 % — preuve que l'expérience apprenant est cassée",
    ],
    cout_estime: "30 à 50 % d'avis négatifs liés à l'UX, pas au contenu.",
    solution: "Architecture LMS : structure de progression, prérequis, jalons, certificats.",
  },
  {
    emoji: "🔴",
    probleme: "Pas de CRM segmenté",
    symptomes: [
      "Toute la liste reçoit le même email — taux d'ouverture < 15 %",
      "Impossible de relancer les leads selon leur comportement",
      "Acheteurs et prospects reçoivent les mêmes messages",
    ],
    cout_estime: "Jusqu'à 40 % de ventes perdues faute de relance comportementale.",
    solution: "FluentCRM : tags comportementaux (visite page prix, téléchargement, achat), séquences différenciées.",
  },
  {
    emoji: "🔴",
    probleme: "Tunnel de vente bricolé",
    symptomes: [
      "Page de vente sans structure éprouvée (AIDA ou PAS)",
      "Checkout non optimisé (trop d'étapes, pas de garantie visible)",
      "Pas d'upsell ni d'order bump — vente unique sans maximisation du panier",
    ],
    cout_estime: "Passer de 1 % à 2,5 % de taux de conversion = CA ×2,5 avec le même trafic.",
    solution: "Tunnel en 3 pages : page de vente + checkout optimisé + confirmation avec upsell.",
  },
  {
    emoji: "🟠",
    probleme: "Empilement de plugins non cohérent",
    symptomes: [
      "10+ plugins actifs dont la moitié se chevauchent fonctionnellement",
      "Conflits, lenteurs, mises à jour qui cassent quelque chose à chaque fois",
      "Le formateur a peur de toucher à son WordPress",
    ],
    cout_estime: "TTFB > 4s = -70 % de conversions mobiles (source Google).",
    solution: "Stack minimaliste documenté : LMS + CRM + checkout + cache + CDN. Rien de plus.",
  },
  {
    emoji: "🟠",
    probleme: "Automatisation absente ou basique",
    symptomes: [
      "Onboarding apprenant 100 % manuel (email bienvenue envoyé à la main)",
      "Pas de relance abandons panier, pas de suivi post-achat",
      "Le formateur passe 2 à 3h/semaine sur des tâches répétitives",
    ],
    cout_estime: "2h/semaine = 100h/an = 1 mission Agency perdue.",
    solution: "3 automatisations prioritaires : bienvenue apprenant, abandon checkout, relance inactif 30j.",
  },
  {
    emoji: "🟡",
    probleme: "Performance ignorée",
    symptomes: [
      "Score PageSpeed < 60 sur mobile",
      "Vidéos de cours chargées directement depuis WordPress (pas de CDN dédié)",
      "Pas de cache configuré — tout requête la base de données à chaque visite",
    ],
    cout_estime: "Chaque seconde de chargement supplémentaire = -7 % de conversions (source Google).",
    solution: "Core Web Vitals + cache (FlyingPress) + CDN vidéo (Bunny.net ou Vimeo) + images WebP.",
  },
];

const OFFRE_SIGNATURE = {
  nom: "WordPress Formation System™",
  pitch_court: "Je transforme ton WordPress en système de vente et de formation autonome — LMS structuré, CRM segmenté, tunnel qui convertit, automatisations actives.",
  pitch_long: "La majorité des formateurs ont un WordPress qui ressemble à un chantier ouvert : 15 plugins, un LMS mal configuré, des emails qui partent en masse sans segmentation, et un tunnel qui perd 70 % des prospects. Je construis l'infrastructure qui fait travailler ton expertise pour toi — même quand tu n'es pas là.",
  composantes: [
    { num: "1", nom: "Audit Stratégique Formation", description: "Diagnostic des 6 dimensions : LMS, CRM, tunnel, performance, automatisation, cohérence business. Rapport + plan d'action priorisé par ROI." },
    { num: "2", nom: "Architecture LMS", description: "Structure de progression, prérequis, jalons, certificats. Choix et configuration du LMS adapté (Tutor LMS, LearnDash, ou LifterLMS selon le profil)." },
    { num: "3", nom: "CRM Segmenté (FluentCRM)", description: "Tags comportementaux, listes segmentées, séquences différenciées (prospect / apprenant actif / inactif / upsell). Synchronisation LMS → CRM." },
    { num: "4", nom: "Tunnel Simplifié", description: "3 pages optimisées : page de vente (structure AIDA) + checkout (SureCart ou WooCommerce optimisé) + confirmation + upsell. Tests A/B intégrés." },
    { num: "5", nom: "Automatisations Prioritaires", description: "5 scénarios : bienvenue apprenant, abandon checkout, module complété, inactif 30j, upsell post-formation. Configuration FluentCRM + n8n si besoin." },
    { num: "6", nom: "Optimisation Conversion", description: "Audit page de vente (heatmap, scroll depth), A/B test sur CTA et garantie, optimisation checkout (réduction friction)." },
    { num: "7", nom: "Formation Interne Client", description: "Le formateur prend en main son système : 2h de formation + documentation complète + support async 30j. Il ne dépend plus de toi pour les mises à jour courantes." },
  ],
  deliverables: [
    "Rapport d'audit (20–30 pages) avec plan d'action priorisé",
    "Architecture LMS documentée (schéma + configuration)",
    "CRM configuré avec tags, listes et 5 automatisations actives",
    "Tunnel de vente optimisé (3 pages + checkout + upsell)",
    "Dashboard de performance (GA4 + FluentCRM analytics)",
    "Documentation technique complète du système",
    "2h de formation client avec enregistrement",
  ],
  promesse: "À l'issue de la mission, ton WordPress génère des ventes et accompagne tes apprenants en automatique. Tu te concentres sur la création de contenu — le système fait le reste.",
};

const PRICING_NICHE = [
  {
    emoji: "🔍",
    nom: "Audit Formation System",
    fourchette: "600 – 1 200 €",
    duree: "2 à 3 jours ouvrés",
    inclus: [
      "Audit LMS : structure, progression, taux de complétion",
      "Audit CRM : segmentation, séquences, taux d'ouverture",
      "Audit tunnel : page de vente, checkout, taux de conversion",
      "Audit performance : Core Web Vitals, vitesse, mobile",
      "Rapport + plan d'action priorisé (Quick Wins + 90j + 6 mois)",
      "Session de restitution 60 min",
    ],
    pour_qui: "Formateur avec une formation déjà en ligne, un WordPress existant, et des ventes qui stagnent.",
    upsell: "80 % des audits débouchent sur une mission Architecture.",
    note_vente: "L'audit est un investissement à ROI immédiat : identifier 1 fuite de conversion à 2 % = +40 % de CA avec le même trafic.",
  },
  {
    emoji: "🏗️",
    nom: "Architecture WordPress Formation System™",
    fourchette: "4 000 – 8 000 €",
    duree: "4 à 8 semaines",
    inclus: [
      "Audit complet inclus (ou déduit si déjà réalisé)",
      "Mise en place ou refonte LMS (architecture + configuration + test parcours)",
      "CRM FluentCRM : installation, configuration, 5 automatisations",
      "Tunnel simplifié : 3 pages optimisées + checkout + upsell",
      "Stack technique rationalisé (plugins nettoyés, dépendances documentées)",
      "Optimisation performance (cache, CDN, Core Web Vitals)",
      "Formation client 2h + documentation complète",
      "Support async 30j post-livraison",
    ],
    pour_qui: "Formateur avec CA existant > 30 000 €/an, prêt à investir dans un système durable.",
    upsell: "Naturellement suivi par l'Accompagnement Mensuel.",
    note_vente: "À 5 000 €, si la mission améliore le taux de conversion de 1 %, un formateur à 100k€/an récupère l'investissement en 2 mois.",
  },
  {
    emoji: "⚙️",
    nom: "Optimisation & Accompagnement Mensuel",
    fourchette: "800 – 1 500 € / mois",
    duree: "Engagement minimum 3 mois",
    inclus: [
      "1 session stratégique mensuelle (60 min)",
      "Suivi KPIs : taux de conversion, complétion, email, performance",
      "Optimisation continue tunnel et emails",
      "Ajout et test de nouvelles automatisations",
      "SEO stratégique formation (cluster + articles décisionnels)",
      "Réponse async 24h (jours ouvrés)",
    ],
    pour_qui: "Client Architecture qui veut maintenir et améliorer son système sur la durée.",
    upsell: "Peut intégrer des modules supplémentaires facturés en extra (nouvelle formation, nouveau produit).",
    note_vente: "À 1 000 €/mois, 4 clients = 4 000 € de MRR stable. La prospection baisse, la profondeur de relation augmente.",
  },
];

const CLUSTERS_SEO = [
  {
    nom: "LMS WordPress — Guide Stratégique",
    kw_pilier: "lms wordpress",
    intention_pilier: "informationnelle / comparative",
    satellites: [
      { kw: "tutor lms vs learndash 2026", intent: "comparative", angle: "Comparatif brutal avec critères pour formateurs pro (pas blog)", priorite: "🔴 M1" },
      { kw: "tutor lms avis formateur", intent: "décisionnelle", angle: "Mon avis après 12 mois sur une plateforme 10k€/an", priorite: "🔴 M1" },
      { kw: "lms wordpress gratuit vs payant", intent: "comparative", angle: "Ce que le gratuit ne te dira jamais — les limitations cachées", priorite: "🟠 M2" },
      { kw: "lifterLMS avis", intent: "décisionnelle", angle: "LifterLMS : pour qui, quel budget, quelle formation", priorite: "🟠 M2" },
      { kw: "lms wordpress taux completion", intent: "informationnelle", angle: "Pourquoi ton taux de complétion est < 40 % (et comment le doubler)", priorite: "🟡 M3" },
      { kw: "wordpress certification formation", intent: "informationnelle", angle: "Mettre en place des certificats automatiques — 3 méthodes testées", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "CRM pour Formateurs WordPress",
    kw_pilier: "crm formateurs wordpress",
    intention_pilier: "informationnelle / comparative",
    satellites: [
      { kw: "fluentcrm pour formateurs en ligne", intent: "décisionnelle", angle: "FluentCRM spécifiquement configuré pour vendre des formations", priorite: "🔴 M1" },
      { kw: "segmentation email formateur wordpress", intent: "informationnelle", angle: "5 segments que tout formateur doit créer avant de relancer", priorite: "🔴 M1" },
      { kw: "fluentcrm vs activecampaign formateur", intent: "comparative", angle: "Conserver nativement ou passer à SaaS : le bon choix selon ton CA", priorite: "🟠 M2" },
      { kw: "automatisation email formation wordpress", intent: "informationnelle", angle: "Les 5 automatisations qui récupèrent des ventes perdues", priorite: "🟠 M2" },
      { kw: "email onboarding apprenant wordpress", intent: "informationnelle", angle: "La séquence bienvenue qui réduit l'abandon dès J+1", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Tunnel de Vente Formation WordPress",
    kw_pilier: "tunnel de vente formation wordpress",
    intention_pilier: "informationnelle",
    satellites: [
      { kw: "page de vente formation wordpress", intent: "informationnelle", angle: "Anatomie d'une page de vente à 3 %+ — exemple réel annoté", priorite: "🔴 M1" },
      { kw: "woocommerce formation en ligne", intent: "informationnelle", angle: "WooCommerce pour vendre des formations : configuration pas à pas", priorite: "🟠 M2" },
      { kw: "surecart vs woocommerce formation", intent: "comparative", angle: "SureCart gagne sur WooCommerce pour les formations — voilà pourquoi", priorite: "🟠 M2" },
      { kw: "order bump upsell wordpress formation", intent: "informationnelle", angle: "Ajouter un order bump : +20 % de panier moyen sans convaincre plus", priorite: "🟡 M3" },
      { kw: "taux de conversion formation wordpress", intent: "informationnelle", angle: "Benchmark et 7 leviers pour améliorer ton taux de conversion", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Automatisation WordPress Formateur",
    kw_pilier: "automatisation wordpress formateur",
    intention_pilier: "informationnelle",
    satellites: [
      { kw: "fluentcrm automatisation formateur", intent: "informationnelle", angle: "Les 5 scénarios FluentCRM à configurer avant tout", priorite: "🔴 M1" },
      { kw: "n8n wordpress formation automatisation", intent: "informationnelle", angle: "n8n + WordPress : 3 workflows qui libèrent 3h/semaine", priorite: "🟠 M2" },
      { kw: "onboarding apprenant automatique wordpress", intent: "informationnelle", angle: "Onboarding automatique de A à Z — plus aucun email manuel", priorite: "🟠 M2" },
      { kw: "abandon panier formation récupérer", intent: "informationnelle", angle: "Comment récupérer 15 à 25 % des paniers abandonnés", priorite: "🟠 M2" },
    ],
  },
  {
    nom: "Performance WordPress LMS",
    kw_pilier: "performance wordpress lms",
    intention_pilier: "informationnelle",
    satellites: [
      { kw: "héberger vidéos formation wordpress", intent: "décisionnelle", angle: "Vimeo vs Bunny.net vs YouTube privé — le bon choix pour ta formation", priorite: "🟠 M2" },
      { kw: "wordpress lms lent solution", intent: "décisionnelle", angle: "Pourquoi ton LMS est lent — et comment diviser le temps de chargement par 3", priorite: "🟡 M3" },
      { kw: "cache wordpress formation", intent: "informationnelle", angle: "Cache et LMS : les 3 règles à ne pas violer (sinon les vidéos cassent)", priorite: "🟡 M3" },
      { kw: "core web vitals wordpress elearning", intent: "informationnelle", angle: "Optimiser les Core Web Vitals sur un site LMS — guide technique", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Monétisation WordPress Formateur",
    kw_pilier: "monétisation wordpress formateur",
    intention_pilier: "informationnelle",
    satellites: [
      { kw: "upsell formation wordpress", intent: "informationnelle", angle: "3 upsells simples qui augmentent le CA de 25 % sans plus de trafic", priorite: "🟠 M2" },
      { kw: "abonnement formation wordpress", intent: "informationnelle", angle: "Créer un accès membres récurrent — MRR stable pour formateur", priorite: "🟠 M2" },
      { kw: "pricing formation en ligne wordpress", intent: "informationnelle", angle: "Comment fixer le prix de sa formation — méthodes testées", priorite: "🟡 M3" },
      { kw: "affiliation programme formation wordpress", intent: "informationnelle", angle: "Mettre en place un programme d'affiliation pour sa formation WordPress", priorite: "🟡 M3" },
    ],
  },
];

const DIFFERENCIATEURS = [
  {
    competence: "SEO cluster ultra-ciblé formateurs",
    niveau: "Expert",
    impact_niche: "Aucun concurrent de la niche formateurs ne publie de contenu SEO décisionnel de qualité sur le LMS/CRM WordPress. Le terrain est libre.",
    action: "3 articles décisionnels par cluster = positionnement dominant en 6 mois.",
  },
  {
    competence: "CRM natif WordPress (FluentCRM)",
    niveau: "Avancé",
    impact_niche: "Les formateurs ont l'outil et n'utilisent que 10 % de ses capacités. Pas de segmentation, pas de séquences comportementales.",
    action: "Cas clients documentés : 'Avant/après segmentation' avec métriques email réels.",
  },
  {
    competence: "Architecture LMS",
    niveau: "Avancé",
    impact_niche: "La structure d'une formation est aussi importante que son contenu. Taux de complétion, progression logique, certificats — peu de prestataires pensent à ce niveau.",
    action: "Créer un guide 'Architecture LMS pour formateurs ambitieux' — lead magnet de référence.",
  },
  {
    competence: "Automatisation (n8n + FluentCRM)",
    niveau: "Expert",
    impact_niche: "Les formateurs perdent des heures sur des tâches répétitives. Aucun autre prestataire WP ne propose ce niveau d'automatisation native.",
    action: "Publier 1 workflow automatisation par mois sur schoolsWP — montrer, pas juste expliquer.",
  },
  {
    competence: "Vision business (pas juste technique)",
    niveau: "Différenciant absolu",
    impact_niche: "Tu parles ROI, tunnel, conversion, LTV — pas juste 'installer Tutor LMS'. Cette posture change la relation client et justifie les prix premium.",
    action: "Chaque devis commence par 'Votre objectif est d'augmenter votre CA de X % — voici comment l'architecture WordPress y contribue.'",
  },
];

const PLAN_90_JOURS = [
  {
    mois: "Mois 1",
    focus: "Poser les fondations visibles",
    objectif: "Être visible et crédible sur la niche formateurs WordPress avant de prospecter.",
    actions: [
      { cat: "Agency", items: [
        "Rédiger et publier la page 'WordPress Formation System™' (landing dédiée sur schoolsWP ou SASU)",
        "Créer le devis type pour l'Audit Formation System (600–1 200 €)",
        "Identifier 10 formateurs WordPress avec > 1 000 abonnés et un site existant",
        "Préparer le pitch email de prospection (3 variantes)",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier l'article pilier 'LMS WordPress : Guide Stratégique 2026' (brain-lite.bat)",
        "Publier 'Tutor LMS vs LearnDash 2026 — comparatif formateurs' (brain-lite.bat)",
        "Publier 'FluentCRM pour formateurs en ligne' (brain-lite.bat)",
        "Intégrer les CTA 'Demander un audit' dans chaque article",
      ]},
      { cat: "Autorité", items: [
        "Rédiger et publier 1 post LinkedIn de positionnement formateurs WordPress",
        "Rejoindre 2 communautés de formateurs en ligne (Discord, Facebook, Slack)",
        "Commenter 10 posts LinkedIn de formateurs avec valeur ajoutée réelle (pas de pitch)",
      ]},
    ],
  },
  {
    mois: "Mois 2",
    focus: "Générer les premières preuves",
    objectif: "Avoir au moins 1 mission Audit signée et commencer à construire la preuve sociale.",
    actions: [
      { cat: "Agency", items: [
        "Réaliser et livrer l'Audit Formation System (premier client, même à tarif réduit pour la preuve)",
        "Collecter un témoignage structuré (avant/après avec 1 métrique chiffrée minimum)",
        "Mettre à jour la landing page avec le témoignage et les chiffres",
        "Relancer les 10 prospects M1 avec l'article pilier comme accroche",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier 'Segmentation email formateur WordPress — 5 segments essentiels'",
        "Publier 'CRM pour formateurs : FluentCRM vs ActiveCampaign' (comparatif)",
        "Publier 'Héberger vidéos formation WordPress : Vimeo vs Bunny.net'",
        "Optimiser les 3 articles du M1 (workflow W1 : V1 → Audit → V2)",
      ]},
      { cat: "Lead magnet", items: [
        "Créer le lead magnet niche : 'Checklist — Les 12 points d'un WordPress Formation System™ rentable'",
        "Configurer la séquence email post-téléchargement (5 emails niche formateurs)",
        "Intégrer le lead magnet dans chaque article publié (CTA inline + popup exit-intent)",
      ]},
    ],
  },
  {
    mois: "Mois 3",
    focus: "Amplifier et systématiser",
    objectif: "Avoir un pipeline commercial autonome (leads entrants) et un mini-produit en ligne.",
    actions: [
      { cat: "Agency", items: [
        "Viser la signature de la première mission Architecture complète (4 000–8 000 €)",
        "Documenter la méthodologie 'WordPress Formation System™' (PDF interne + présentation client)",
        "Créer le template d'onboarding client (Notion partagé + accueil automatisé)",
        "Configurer l'automatisation du funnel Audit (formulaire → cal auto → devis email)",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier l'article pilier cluster 2 : 'Tunnel de vente formation WordPress' (brain-lite.bat)",
        "Publier 'Page de vente formation WordPress — anatomie d'une page à 3 % de conversion'",
        "Mettre en place la stratégie AI Overviews : FAQ AIO sur les 3 articles les plus lus",
        "Démarrer le cluster 3 'Automatisation WordPress formateur'",
      ]},
      { cat: "Mini-produit", items: [
        "Lancer le 'Formation System Audit Kit' : checklist + template rapport + guide (47–97 €)",
        "Page de vente dédiée + intégration dans la séquence email",
        "Post LinkedIn de lancement du mini-produit",
        "Objectif M3 : 10 ventes minimum du mini-produit",
      ]},
    ],
  },
];

const SYNERGIE_SCHOOLSWP = {
  media: "schoolsWP reste le média général WordPress — pédagogique, clair, structuré, utile. Il construit l'audience large et l'autorité SEO.",
  sous_positionnement: "Dans cet écosystème, une catégorie dédiée 'Formateurs WordPress' ou un hub de ressources ciblé positionne le sous-niche sans fragmenter l'identité principale.",
  agency: "La SASU récupère les leads les plus qualifiés de schoolsWP — ceux qui ont lu les articles LMS/CRM/tunnel et savent déjà de quoi tu parles au premier call.",
  tunnel_editorial: "Article schoolsWP → Lead magnet niche → Séquence email → Audit Formation System → Architecture → Accompagnement Mensuel",
  articles_double_usage: [
    "Chaque article LMS/CRM/tunnel sert à la fois l'audience schoolsWP et les prospects Agency",
    "Les études de cas Agency alimentent schoolsWP (avec autorisation client, anonymisées si besoin)",
    "Les témoignages Agency renforcent la crédibilité éditoriale de schoolsWP",
  ],
};

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Objectif : devenir la référence WordPress des formateurs ambitieux — média schoolsWP + Agency SASU ultra-spécialisée.", "🎓", "green_background"));
  blocks.push(p(""));
  blocks.push(qot("\"Je n'aide pas à créer des sites. J'architecture des systèmes WordPress rentables pour formateurs en ligne.\""));
  blocks.push(div());

  // Section 1 — Positionnement
  blocks.push(h1("🎯 Positionnement Clair et Tranché"));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu ne dis PLUS"));
  blocks.push(bul(rt("✗ ", { color: "red" }), rt("J'aide à créer un site WordPress.", { italic: true })));
  blocks.push(bul(rt("✗ ", { color: "red" }), rt("Je fais de la refonte WordPress.", { italic: true })));
  blocks.push(bul(rt("✗ ", { color: "red" }), rt("Je gère votre WordPress.", { italic: true })));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu dis MAINTENANT"));
  blocks.push(bul(rt("✓ ", { color: "green" }), rt("J'architecture des systèmes WordPress rentables pour formateurs en ligne.", { bold: true })));
  blocks.push(bul(rt("✓ ", { color: "green" }), rt("Je transforme ton WordPress en machine à ventes et à rétention d'apprenants.")));
  blocks.push(bul(rt("✓ ", { color: "green" }), rt("Je construis l'infrastructure technique qui soutient ta croissance — LMS, CRM, tunnel, automatisation.")));
  blocks.push(p(""));
  blocks.push(cal("La différence : la première formulation vend du temps. La seconde vend une transformation. Ce n'est pas juste sémantique — ça change le prix que le client accepte de payer.", "⚡", "yellow_background"));
  blocks.push(div());

  // Section 2 — Problèmes niche
  blocks.push(h1("🧠 Les 6 Problèmes Réels des Formateurs WordPress"));
  blocks.push(p("Les connaître par cœur te permet de les nommer avant que le client les formule — signal de crédibilité immédiate lors du premier call."));
  blocks.push(p(""));
  PROBLEMES_NICHE.forEach((prob) => {
    blocks.push(tog(`${prob.emoji} ${prob.probleme}`, [
      p(rt("Symptômes observés :", { bold: true })),
      ...prob.symptomes.map((s) => bul(s)),
      p(""),
      p(rt("Coût estimé : ", { bold: true }), rt(prob.cout_estime, { italic: true })),
      p(rt("Solution apportée : ", { bold: true }), rt(prob.solution)),
    ]));
  });
  blocks.push(p(""));
  blocks.push(cal("En résumé : tu résous le chaos technique, le manque de structure, et la perte de revenus. Pour le client : 'Ton WordPress travaille contre toi. Je le retourne.'", "🔑", "orange_background"));
  blocks.push(div());

  // Section 3 — Offre signature
  blocks.push(h1("🏗️ Offre Signature — WordPress Formation System™"));
  blocks.push(qot(OFFRE_SIGNATURE.pitch_long));
  blocks.push(p(""));
  blocks.push(h3("Les 7 composantes"));
  OFFRE_SIGNATURE.composantes.forEach((comp) => {
    blocks.push(bul(
      rt(`${comp.num}. ${comp.nom} — `, { bold: true }),
      rt(comp.description)
    ));
  });
  blocks.push(p(""));
  blocks.push(tog(`📋 Livrables complets (${OFFRE_SIGNATURE.deliverables.length})`,
    OFFRE_SIGNATURE.deliverables.map((d) => tod(d))
  ));
  blocks.push(p(""));
  blocks.push(cal(OFFRE_SIGNATURE.promesse, "✅", "green_background"));
  blocks.push(div());

  // Section 4 — Pricing niche
  blocks.push(h1("💰 Pricing Niche Formateurs"));
  blocks.push(p("Entrée (Audit) → Offre phare (Architecture) → Continuité (Accompagnement). Pas de confusion."));
  blocks.push(p(""));
  PRICING_NICHE.forEach((tier) => {
    blocks.push(h2(`${tier.emoji} ${tier.nom} — ${tier.fourchette}`));
    blocks.push(p(rt("Durée : ", { bold: true }), rt(tier.duree)));
    blocks.push(p(rt("Pour qui : ", { bold: true }), rt(tier.pour_qui)));
    blocks.push(p(""));
    blocks.push(tog(`📋 Inclus (${tier.inclus.length} éléments)`,
      tier.inclus.map((item) => bul(item))
    ));
    blocks.push(p(""));
    blocks.push(qot(`Note de vente : ${tier.note_vente}`));
    blocks.push(p(rt("Upsell naturel : ", { bold: true }), rt(tier.upsell)));
    blocks.push(p(""));
  });
  blocks.push(div());

  // Section 5 — Clusters SEO
  blocks.push(h1("🔍 Stratégie SEO — 6 Clusters Niche Formateurs"));
  blocks.push(cal("Chaque cluster cible les formateurs, pas 'tout le monde'. 1 article ultra-ciblé 'formateur WordPress' vaut 10 articles génériques.", "🎯", "purple_background"));
  blocks.push(p(""));

  const totalSat = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  CLUSTERS_SEO.forEach((cluster, ci) => {
    blocks.push(h2(`Cluster ${ci + 1} — ${cluster.nom}`));
    blocks.push(p(rt("Mot-clé pilier : ", { bold: true }), rt(cluster.kw_pilier, { code: true })));
    blocks.push(p(rt("Intention : ", { bold: true }), rt(cluster.intention_pilier)));
    blocks.push(p(""));
    blocks.push(tog(`📰 Satellites (${cluster.satellites.length} articles)`,
      cluster.satellites.map((sat) =>
        p(
          rt(`${sat.priorite} `, {}),
          rt(`"${sat.kw}" `, { bold: true }),
          rt(`[${sat.intent}] — `),
          rt(sat.angle, { italic: true })
        )
      )
    ));
    blocks.push(p(""));
  });

  blocks.push(cal(`${CLUSTERS_SEO.length} clusters × ${totalSat} articles au total. 🔴 = M1 (priorité absolue) — 🟠 = M2 — 🟡 = M3+`, "📊", "blue_background"));
  blocks.push(div());

  // Section 6 — Différenciateurs
  blocks.push(h1("🧠 Tes 5 Différenciateurs"));
  blocks.push(p("Très peu de prestataires WordPress maîtrisent l'ensemble de ces compétences. C'est ton avantage concurrentiel durable sur cette niche."));
  blocks.push(p(""));
  DIFFERENCIATEURS.forEach((diff, i) => {
    blocks.push(tog(`${i + 1}. ${diff.competence} — ${diff.niveau}`, [
      p(rt("Impact sur la niche : ", { bold: true }), rt(diff.impact_niche)),
      p(rt("Action : ", { bold: true }), rt(diff.action, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 7 — Plan 90 jours
  blocks.push(h1("🗓️ Plan 90 Jours — Actions Concrètes"));
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);
  blocks.push(cal(`Objectif 90 jours : offre visible, 1 Audit signé, 6 articles publiés, lead magnet actif. ${totalActions} actions concrètes.`, "🚀", "orange_background"));
  blocks.push(p(""));

  PLAN_90_JOURS.forEach((mois) => {
    blocks.push(h2(`${mois.mois} — ${mois.focus}`));
    blocks.push(p(rt("Objectif : ", { bold: true }), rt(mois.objectif)));
    blocks.push(p(""));
    mois.actions.forEach((cat) => {
      blocks.push(tog(`📌 ${cat.cat}`, cat.items.map((item) => tod(item))));
    });
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 8 — Synergie schoolsWP
  blocks.push(h1("🔗 Synergie schoolsWP × Niche Formateurs"));
  blocks.push(p(""));
  blocks.push(h3("schoolsWP — Média général"));
  blocks.push(p(SYNERGIE_SCHOOLSWP.media));
  blocks.push(p(""));
  blocks.push(h3("Sous-positionnement formateurs"));
  blocks.push(p(SYNERGIE_SCHOOLSWP.sous_positionnement));
  blocks.push(p(""));
  blocks.push(h3("La SASU Agency"));
  blocks.push(p(SYNERGIE_SCHOOLSWP.agency));
  blocks.push(p(""));
  blocks.push(h3("Tunnel éditorial complet"));
  blocks.push(qot(SYNERGIE_SCHOOLSWP.tunnel_editorial));
  blocks.push(p(""));
  blocks.push(h3("Double usage du contenu"));
  SYNERGIE_SCHOOLSWP.articles_double_usage.forEach((item) => blocks.push(bul(item)));
  blocks.push(div());

  // Footer
  blocks.push(cal("Peu de freelances pensent à ce niveau. Tu construis en parallèle : autorité SEO, audience qualifiée, système automatisé, offre premium. C'est un actif qui s'apprécie chaque mois.", "🏁", "green_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Niche Formateurs — Architecte WordPress des Formateurs Ambitieux'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  const totalSatellites = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);

  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎓" },
    properties: {
      title: { title: [{ text: { content: "🎓 Niche Formateurs — Architecte WordPress des Formateurs Ambitieux" } }] },
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
  console.log(`   • ${PROBLEMES_NICHE.length} problèmes niche avec coût estimé + solution`);
  console.log(`   • ${OFFRE_SIGNATURE.composantes.length} composantes WordPress Formation System™`);
  console.log(`   • ${PRICING_NICHE.length} niveaux de prix avec inclus, note de vente et upsell`);
  console.log(`   • ${CLUSTERS_SEO.length} clusters SEO — ${totalSatellites} articles identifiés`);
  console.log(`   • ${DIFFERENCIATEURS.length} différenciateurs documentés`);
  console.log(`   • Plan 90 jours — ${totalActions} actions concrètes (cases à cocher)`);
  console.log(`   • Synergie schoolsWP × Agency documentée`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

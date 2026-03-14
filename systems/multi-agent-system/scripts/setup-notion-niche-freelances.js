#!/usr/bin/env node
/**
 * setup-notion-niche-freelances.js
 * Crée la page "💼 Niche Freelances — WordPress Business System™ Freelance Edition" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-niche-freelances.js
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

const ICP_PROFILS = [
  {
    emoji: "🔍",
    label: "Consultant SEO indépendant",
    ca_typique: "40 000 – 80 000 €/an",
    situation: "Génère ses leads via LinkedIn et le bouche-à-oreille. Site WordPress basique, pas de CRM, pas de séquence email. Perd des leads faute de relance.",
    pain_points: [
      "Tout le pipeline commercial est dans sa tête ou dans une feuille Excel",
      "Les prospects qui ne signent pas immédiatement disparaissent sans relance",
      "Son site ne génère aucun lead entrant — 100 % de son CA vient du réseau",
    ],
    gain_cible: "Un WordPress qui capture les leads inbound, un CRM qui relance automatiquement, un tunnel qui présente ses offres sans qu'il soit là.",
    signal_prospect: "Parle de 'se structurer' et de 'ne plus dépendre uniquement du bouche-à-oreille'.",
  },
  {
    emoji: "🎨",
    label: "Webdesigner / Intégrateur WordPress",
    ca_typique: "30 000 – 60 000 €/an",
    situation: "Construit des sites WordPress pour ses clients mais pas pour lui-même. Site portfolio statique, pas de tunnel, pas de lead magnet.",
    pain_points: [
      "Son site montre du travail mais ne vend pas activement ses offres",
      "Pas de séquence email post-devis — il relance manuellement ou oublie",
      "Dépend d'une plateforme (Malt, Comet) pour 60 % de ses revenus",
    ],
    gain_cible: "Un site portfolio qui convertit, un tunnel de devis automatisé, une présence indépendante des plateformes.",
    signal_prospect: "Cherche à 'sortir de Malt' et à 'avoir ses propres clients'.",
  },
  {
    emoji: "✍️",
    label: "Copywriter / Consultant marketing",
    ca_typique: "35 000 – 70 000 €/an",
    situation: "Expertise forte en contenu et conversion, mais son propre site ne reflète pas ses compétences. Outils éparpillés (Notion, Google Docs, MailChimp, Stripe séparés).",
    pain_points: [
      "Incongruence visible : vend la conversion mais son site ne convertit pas",
      "Pipeline = DMs LinkedIn + email manuel — aucune automatisation",
      "Pas de lead magnet structuré pour capturer les contacts froids",
    ],
    gain_cible: "Un WordPress qui intègre son expertise en conversion — page de vente maîtrisée, tunnel lead magnet, CRM unifié.",
    signal_prospect: "Parle de 'tout centraliser' et de 'construire un actif qui travaille pour moi'.",
  },
  {
    emoji: "📊",
    label: "Consultant B2B (stratégie, ops, data)",
    ca_typique: "60 000 – 120 000 €/an",
    situation: "TJM élevé, peu de clients mais haute valeur. Site minimal ou inexistant. Toute l'acquisition passe par le réseau. Veut construire une présence qui attire sans démarcher.",
    pain_points: [
      "Son expertise n'est pas visible en dehors de ses clients actuels",
      "Pas de contenu SEO, pas de lead magnet — acquisition = zéro en dehors du réseau",
      "Si 1 client part, le CA chute de 40 % ou plus",
    ],
    gain_cible: "Un WordPress d'autorité qui attire les mandats premium, un lead magnet à forte valeur, un positionnement visible en dehors du réseau direct.",
    signal_prospect: "Parle de 'diversifier l'acquisition' et de 'construire une présence durable'.",
  },
  {
    emoji: "💡",
    label: "Solopreneur / Créateur de contenu monétisé",
    ca_typique: "20 000 – 50 000 €/an",
    situation: "Newsletter, YouTube ou podcast avec une audience existante. Monétise partiellement via des produits digitaux ou services. WordPress fragile, outils non connectés.",
    pain_points: [
      "Son audience est captive d'une plateforme (YouTube, Substack) qu'il ne contrôle pas",
      "Ventes de produits incohérentes — pas de tunnel clair",
      "Email list sous-exploitée : envoie des newsletters mais pas de séquences de vente",
    ],
    gain_cible: "Un WordPress qui porte sa marque personnelle, centralise son audience et automatise ses ventes de produits digitaux.",
    signal_prospect: "Parle de 'reprendre le contrôle' et de 'ne plus dépendre de l'algorithme'.",
  },
];

const PROBLEMES_COMMUNS = [
  {
    emoji: "🔴",
    probleme: "Site vitrine mort",
    description: "Le site existe mais ne fait rien. Pas de lead magnet, pas de CTA clair, pas de tracking. 100 % du CA vient d'ailleurs.",
    cout: "Entre 50 et 100 % des leads potentiels perdus faute de capture.",
    solution: "Transformer chaque page en étape d'un funnel : home → offre → lead magnet → CTA.",
  },
  {
    emoji: "🔴",
    probleme: "Pas de CRM — pipeline dans la tête",
    description: "Les prospects sont dans Gmail, Excel ou Notion. Pas de tags, pas de relance automatique, pas de visibilité sur le pipeline.",
    cout: "En moyenne 20 à 30 % des devis perdus faute de suivi systématique.",
    solution: "FluentCRM : pipeline commercial, tags par statut, séquence de relance post-devis automatisée.",
  },
  {
    emoji: "🔴",
    probleme: "Tunnel bricolé ou inexistant",
    description: "Pas de parcours clair du prospect à l'acheteur. La page de vente des offres n'a pas de structure éprouvée. Le checkout est une friction.",
    cout: "Taux de conversion typique sans tunnel : 0,5 à 1 %. Avec tunnel optimisé : 2 à 4 %.",
    solution: "3 pages minimalistes : page offre (AIDA) + page de contact/devis (friction zéro) + confirmation.",
  },
  {
    emoji: "🟠",
    probleme: "Outils éparpillés non connectés",
    description: "MailChimp + Notion + Stripe + Calendly + Google Analytics séparés. Aucun n'est synchronisé. Le formateur jongle manuellement.",
    cout: "2 à 3h/semaine de travail manuel = 100h+/an perdues.",
    solution: "Stack WordPress intégré : FluentCRM + FluentForms + SureCart + cal.com. Tout dans 1 tableau de bord.",
  },
  {
    emoji: "🟠",
    probleme: "SEO absent — 100 % dépendant du réseau",
    description: "Aucun contenu SEO, pas de stratégie cluster, pas d'articles décisionnels. Si le réseau tarit, l'acquisition s'arrête.",
    cout: "Risque business critique : 1 départ de client important peut mettre en danger la trésorerie.",
    solution: "1 cluster SEO décisionnel sur son expertise principale. 8 à 12 articles = leads entrants en 6 mois.",
  },
  {
    emoji: "🟡",
    probleme: "Automatisation = zéro",
    description: "Chaque prospect est traité manuellement. Pas de séquence bienvenue, pas de nurturing, pas de relance post-devis automatisée.",
    cout: "Le freelance échange son temps contre des leads. Sans automatisation, la croissance plafonne.",
    solution: "3 workflows prioritaires : bienvenue lead magnet, relance devis 48h, réactivation contact inactif 60j.",
  },
];

const OFFRE_SIGNATURE = {
  nom: "WordPress Business System™ — Freelance Edition",
  pitch_court: "Je transforme le WordPress de ton activité freelance en système d'acquisition et de conversion autonome.",
  pitch_long: "La plupart des freelances digitaux ont un WordPress qui ne travaille pas pour eux. Il existe, il est là, mais il ne génère aucun lead entrant, aucune relance automatique, aucune structure commerciale. Je construis le système qui fait tourner ton acquisition pendant que tu es en mission.",
  promesse: "En 4 à 6 semaines, ton WordPress capte des leads, les nurture, présente tes offres et automatise ton pipeline — sans que tu deviennes développeur.",
  composantes: [
    { num: "1", nom: "Audit Stratégique Freelance", description: "Diagnostic site + offres + acquisition + outils. Rapport avec plan d'action priorisé par ROI." },
    { num: "2", nom: "Clarification Offre & Tunnel", description: "Structurer la page offre principale (AIDA), définir l'offre d'entrée et le parcours prospect → client." },
    { num: "3", nom: "CRM Freelance (FluentCRM)", description: "Pipeline commercial, tags statut (prospect / devis envoyé / en négociation / client), séquences automatisées." },
    { num: "4", nom: "Lead Magnet & Capture", description: "1 lead magnet à forte valeur (checklist, template, guide), formulaire optimisé, séquence email 5 messages." },
    { num: "5", nom: "Automatisation Acquisition", description: "3 workflows : bienvenue lead, relance devis 48h, réactivation contact inactif 60j." },
    { num: "6", nom: "SEO de Base — 1 Cluster Décisionnel", description: "Identification du cluster principal, 3 articles décisionnels, maillage interne optimisé." },
    { num: "7", nom: "Stack Technique Rationalisé", description: "Audit et nettoyage des plugins inutiles. Stack recommandé documenté. Performance optimisée (cache + images)." },
  ],
  deliverables: [
    "Rapport d'audit avec plan d'action priorisé (Quick Wins + 30j + 90j)",
    "Page offre principale optimisée (structure AIDA + CTA)",
    "CRM configuré avec pipeline + 3 automatisations actives",
    "Lead magnet produit ou optimisé + séquence 5 emails",
    "3 articles SEO décisionnels publiés",
    "Stack technique documenté (plugins, rôle, alternative)",
    "Dashboard GA4 + FluentCRM analytics paramétré",
    "Documentation complète + formation 1h30",
  ],
};

const PRICING_NICHE = [
  {
    emoji: "🔍",
    nom: "Audit Freelance System",
    fourchette: "500 – 900 €",
    duree: "2 jours ouvrés",
    inclus: [
      "Audit site (tunnel, offre, CTA, SEO de base)",
      "Audit acquisition (sources, pipeline, outils)",
      "Rapport 15–20 pages avec plan d'action priorisé",
      "Session restitution 60 min",
    ],
    pour_qui: "Freelance avec activité existante (CA > 20 000 €/an), site en ligne depuis > 6 mois.",
    note_vente: "Le prix de l'audit = 1 heure de mission perdue. Le plan d'action vaut 10× le prix si 1 seule action améliore le taux de conversion.",
    upsell: "90 % des audits identifient des axes qui justifient la mission Architecture.",
  },
  {
    emoji: "🏗️",
    nom: "Architecture WordPress Business System™ — Freelance",
    fourchette: "3 000 – 6 000 €",
    duree: "4 à 6 semaines",
    inclus: [
      "Audit inclus ou déduit si déjà réalisé",
      "Page offre principale reconstruite",
      "CRM + pipeline commercial + 3 automatisations",
      "Lead magnet + séquence email 5 messages",
      "3 articles SEO décisionnels (avec brain-lite)",
      "Stack rationalisé + performance optimisée",
      "Dashboard de pilotage paramétré",
      "Formation client 1h30 + documentation complète",
    ],
    pour_qui: "Freelance qui veut ne plus dépendre uniquement du bouche-à-oreille, prêt à investir dans un actif durable.",
    note_vente: "À 4 000 €, si la mission génère 1 lead qualifié/mois supplémentaire sur 12 mois = 4 000 € de CA minimum récupéré.",
    upsell: "Débouche naturellement sur un accompagnement mensuel SEO + optimisation conversion.",
  },
  {
    emoji: "⚙️",
    nom: "Accompagnement Mensuel — Croissance Freelance",
    fourchette: "500 – 1 000 € / mois",
    duree: "Engagement minimum 3 mois",
    inclus: [
      "1 session stratégique mensuelle (45 min)",
      "Suivi KPIs : leads entrants, taux de conversion, pipeline",
      "1 article SEO supplémentaire par mois (avec brain-lite)",
      "Optimisation continue landing page + séquences email",
      "Réponse async 48h (jours ouvrés)",
    ],
    pour_qui: "Client Architecture qui veut maintenir la dynamique et renforcer le SEO mois après mois.",
    note_vente: "3 clients à 700 €/mois = 2 100 € de MRR. Stable, prévisible, peu chronophage.",
    upsell: "Peut évoluer vers une mission plus profonde si le CA du client augmente significativement.",
  },
];

const CLUSTERS_SEO = [
  {
    nom: "CRM WordPress pour Freelances",
    kw_pilier: "crm wordpress freelance",
    intention: "informationnelle / comparative",
    satellites: [
      { kw: "fluentcrm pour freelance", intent: "décisionnelle", angle: "FluentCRM pour freelances : configuration spécifique — pas pour e-commerce", priorite: "🔴 M1" },
      { kw: "gérer prospects wordpress freelance", intent: "informationnelle", angle: "Remplacer Excel par un CRM natif WordPress — migration pas à pas", priorite: "🔴 M1" },
      { kw: "relance automatique devis wordpress", intent: "informationnelle", angle: "Automatiser la relance devis : récupérer 20 % de prospects perdus", priorite: "🟠 M2" },
      { kw: "pipeline commercial wordpress freelance", intent: "informationnelle", angle: "Construire un pipeline commercial visuel dans FluentCRM", priorite: "🟠 M2" },
      { kw: "crm gratuit vs payant freelance wordpress", intent: "comparative", angle: "CRM gratuit ou FluentCRM payant : le bon choix selon ton CA", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Tunnel Simple WordPress Freelance",
    kw_pilier: "tunnel wordpress freelance",
    intention: "informationnelle",
    satellites: [
      { kw: "page offre freelance wordpress", intent: "informationnelle", angle: "Anatomie d'une page d'offre freelance qui convertit — exemple réel", priorite: "🔴 M1" },
      { kw: "lead magnet freelance wordpress", intent: "informationnelle", angle: "5 lead magnets adaptés aux freelances digitaux (pas des ebooks génériques)", priorite: "🔴 M1" },
      { kw: "formulaire contact optimisé wordpress freelance", intent: "informationnelle", angle: "Réduire la friction du contact : 3 champs, 1 CTA, +40 % de demandes", priorite: "🟠 M2" },
      { kw: "landing page freelance wordpress conversion", intent: "informationnelle", angle: "La landing page freelance qui convertit à 5 %+ — structure testée", priorite: "🟠 M2" },
      { kw: "calendly wordpress freelance", intent: "informationnelle", angle: "Intégrer Cal.com dans WordPress pour les découvertes — sans friction", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Automatisation Client WordPress",
    kw_pilier: "automatisation client wordpress",
    intention: "informationnelle",
    satellites: [
      { kw: "onboarding client automatique wordpress", intent: "informationnelle", angle: "Onboarding client automatisé de A à Z — plus d'email manuel", priorite: "🔴 M1" },
      { kw: "séquence email freelance wordpress", intent: "informationnelle", angle: "La séquence email bienvenue qui transforme un lead froid en prospect chaud", priorite: "🟠 M2" },
      { kw: "n8n freelance wordpress automatisation", intent: "informationnelle", angle: "n8n + FluentCRM pour freelances : 3 workflows qui libèrent 2h/semaine", priorite: "🟠 M2" },
      { kw: "nurturing prospect freelance email", intent: "informationnelle", angle: "Nurturer ses prospects sans spammer — la méthode en 3 emails", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "WordPress pour Consultant SEO",
    kw_pilier: "wordpress consultant seo",
    intention: "informationnelle",
    satellites: [
      { kw: "site wordpress consultant seo", intent: "informationnelle", angle: "Le site WordPress d'un consultant SEO qui convertit — anatomie complète", priorite: "🔴 M1" },
      { kw: "personal branding seo wordpress", intent: "informationnelle", angle: "Construire son autorité SEO personnelle sur WordPress — stratégie cluster", priorite: "🟠 M2" },
      { kw: "blog consultant seo wordpress", intent: "informationnelle", angle: "Écrire pour son propre SEO quand on est consultant SEO : les règles", priorite: "🟠 M2" },
      { kw: "portfolio consultant seo wordpress", intent: "informationnelle", angle: "Structurer un portfolio SEO qui rassure et attire — exemples réels", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Structurer Son Site Freelance WordPress",
    kw_pilier: "site freelance wordpress structuré",
    intention: "informationnelle",
    satellites: [
      { kw: "site wordpress freelance digital", intent: "informationnelle", angle: "Les 7 pages qu'un freelance digital doit avoir sur WordPress en 2026", priorite: "🔴 M1" },
      { kw: "sortir de malt wordpress", intent: "décisionnelle", angle: "Sortir de Malt : comment construire son acquisition WordPress indépendante", priorite: "🔴 M1" },
      { kw: "vitesse wordpress freelance", intent: "informationnelle", angle: "Optimiser la vitesse de son site WordPress freelance — guide sans dév", priorite: "🟠 M2" },
      { kw: "portfolio wordpress freelance 2026", intent: "informationnelle", angle: "Créer un portfolio WordPress qui travaille comme un commercial", priorite: "🟠 M2" },
      { kw: "personal branding wordpress freelance", intent: "informationnelle", angle: "Construire sa marque personnelle sur WordPress — au-delà du portfolio", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Système WordPress pour Solopreneur",
    kw_pilier: "système wordpress solopreneur",
    intention: "informationnelle",
    satellites: [
      { kw: "solopreneur wordpress système business", intent: "informationnelle", angle: "De freelance à solopreneur : ce que ton WordPress doit changer", priorite: "🔴 M1" },
      { kw: "wordpress indépendant revenus passifs", intent: "informationnelle", angle: "Créer des revenus récurrents avec WordPress — méthodes réalistes", priorite: "🟠 M2" },
      { kw: "stack outils solopreneur wordpress", intent: "comparative", angle: "Le stack parfait pour solopreneur WordPress en 2026 — 7 outils, 0 abonnement superflu", priorite: "🟠 M2" },
      { kw: "newsletter wordpress solopreneur", intent: "informationnelle", angle: "Construire sa newsletter sur WordPress sans quitter Substack brutalement", priorite: "🟡 M3" },
    ],
  },
];

const DIFFERENCIATEURS = [
  {
    competence: "Stack WordPress intégré (pas juste 'un site')",
    impact: "Les freelances qui voient la démo CRM + automatisation + tunnel en 1 seul WordPress ont un déclic immédiat. Aucun concurrent ne le présente ainsi.",
    action: "Créer 1 vidéo courte (3 min) montrant le tableau de bord FluentCRM en live — lien depuis la landing page.",
  },
  {
    competence: "Connaissance des douleurs spécifiques freelance",
    impact: "Tu sais que la peur principale est 'perdre son indépendance vis-à-vis des plateformes'. Tu la nommes avant qu'ils la formulent.",
    action: "Dans chaque article, utiliser l'intro : 'Si tu dépends encore à 60 % de Malt pour tes revenus, ce que je vais te montrer change la donne.'",
  },
  {
    competence: "SEO décisionnel ciblé freelances",
    impact: "Zéro concurrent positionné sur 'CRM WordPress pour freelance' ou 'sortir de Malt WordPress'. Le terrain SEO est vierge.",
    action: "Publier les 2 articles 🔴 M1 de chaque cluster en priorité — positionnement rapide possible sous 3 à 4 mois.",
  },
  {
    competence: "Vision ROI (pas juste technique)",
    impact: "Les freelances comprennent le ROI. Parler 'taux de conversion', 'coût d'acquisition', 'LTV' les connecte immédiatement.",
    action: "Inclure 1 calcul ROI dans chaque présentation : 'Si ce système vous génère 2 leads supplémentaires par mois à 2 000 €, il est remboursé en 30 jours.'",
  },
  {
    competence: "schoolsWP comme preuve d'autorité",
    impact: "Avoir un média référence sur WordPress rassure. Le prospect peut vérifier l'expertise avant même le premier contact.",
    action: "Mentionner schoolsWP explicitement dans le pitch Agency : 'Je publie sur schoolsWP — vous pouvez voir ma méthode avant de travailler avec moi.'",
  },
];

const PLAN_90_JOURS = [
  {
    mois: "Mois 1",
    focus: "Visibilité et crédibilité niche B",
    objectif: "3 articles décisionnels publiés, page Audit Freelance en ligne, CTA intégrés dans 10 articles existants.",
    actions: [
      { cat: "Contenu SEO", items: [
        "Publier 'Site WordPress freelance digital : les 7 pages essentielles 2026' (brain-lite.bat)",
        "Publier 'FluentCRM pour freelance : configuration spécifique' (brain-lite.bat)",
        "Publier 'Sortir de Malt : construire son acquisition WordPress indépendante' (brain-lite.bat)",
        "Intégrer CTA 'Audit gratuit 30 min' dans les 10 articles schoolsWP les plus lus",
      ]},
      { cat: "Agency", items: [
        "Créer la landing page 'Audit Freelance System — 500 à 900 €'",
        "Rédiger le devis type Freelance (avec les 3 niveaux d'offre)",
        "Identifier 15 freelances digitaux sur LinkedIn (CA visible, site WordPress, actif)",
        "Préparer le message d'approche LinkedIn (3 variantes, non-commercial, valeur d'abord)",
      ]},
      { cat: "Autorité", items: [
        "Publier 1 post LinkedIn : 'Pourquoi 80 % des freelances digitaux ont un WordPress qui ne travaille pas pour eux'",
        "Rejoindre 2 communautés freelance (Slack, Discord, ou groupe Facebook actif)",
        "Répondre à 10 posts LinkedIn de freelances avec des conseils WordPress concrets",
      ]},
    ],
  },
  {
    mois: "Mois 2",
    focus: "Preuve sociale et profondeur de niche",
    objectif: "1 étude de cas publiée, 3 articles supplémentaires, lead magnet actif.",
    actions: [
      { cat: "Agency", items: [
        "Réaliser le premier Audit Freelance System (beta client si nécessaire)",
        "Documenter les résultats : avant/après avec métriques (trafic, leads, pipeline)",
        "Publier l'étude de cas sur schoolsWP (anonymisée si besoin)",
        "Relancer les 15 prospects identifiés en M1 avec l'étude de cas en accroche",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier 'CRM WordPress pour freelance : comparatif FluentCRM vs HubSpot gratuit'",
        "Publier 'Onboarding client automatique WordPress — guide complet'",
        "Publier 'Lead magnet freelance WordPress — 5 idées testées'",
        "Optimiser les 3 articles du M1 avec le workflow W1 (V1 → Audit → V2)",
      ]},
      { cat: "Lead magnet", items: [
        "Créer le lead magnet : 'Checklist — Les 10 signes que ton WordPress freelance te coûte des clients'",
        "Configurer la séquence email post-téléchargement (5 emails niche freelances)",
        "Intégrer le CTA lead magnet dans tous les articles freelance + les 5 articles les plus lus",
      ]},
    ],
  },
  {
    mois: "Mois 3",
    focus: "Systématisation et premier MRR",
    objectif: "Pipeline commercial qui tourne, 1ère mission Architecture signée, outreach LinkedIn actif.",
    actions: [
      { cat: "Agency", items: [
        "Viser la signature de la première mission Architecture complète (3 000–6 000 €)",
        "Automatiser le funnel Audit : formulaire → cal auto → email devis → relance J+3",
        "Créer le template Notion d'onboarding client Freelance",
        "Lancer l'outreach soft LinkedIn : commenter + DM à J+3 si interaction",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier l'article pilier cluster 2 : 'Tunnel simple WordPress pour freelance' (brain-lite.bat)",
        "Publier 'Landing page freelance WordPress : structure qui convertit à 5 %'",
        "Mettre en place les FAQ AIO sur les 3 articles les plus lus (AI Overviews)",
        "Démarrer le cluster 3 : 'Automatisation client WordPress'",
      ]},
      { cat: "Positionnement", items: [
        "Publier 1 post LinkedIn résultats : chiffres du M1–M2 (articles, trafic, leads)",
        "Mettre à jour la bio LinkedIn avec le positionnement niche B explicite",
        "Demander 1 recommandation LinkedIn au premier client de l'Audit",
        "Créer 1 carrousel LinkedIn : 'Les 5 erreurs WordPress des freelances digitaux'",
      ]},
    ],
  },
];

const SYNERGIE_SCHOOLSWP = {
  audience_naturelle: "schoolsWP attire naturellement les freelances digitaux : consultants SEO, webdesigners, créateurs de contenus. Ils lisent les articles WordPress, suivent les comparatifs de plugins, cherchent des solutions techniques.",
  conversion_agency: "La SASU Agency capte ceux qui ont compris qu'ils ont besoin d'aide pour passer de 'savoir faire' à 'faire faire travailler son système'. Pas les débutants — les freelances qui ont déjà une activité et veulent se structurer.",
  tunnel: "Article schoolsWP → Lead magnet niche freelance → Séquence email 5 messages → CTA Audit → Découverte call → Architecture → Accompagnement",
  articles_double_usage: [
    "Chaque article niche freelance alimente à la fois l'audience schoolsWP (SEO) et le pipeline Agency (leads qualifiés)",
    "Les études de cas Agency publiées sur schoolsWP renforcent la crédibilité éditoriale ET commerciale",
    "Le lead magnet niche freelance peut être promu dans la newsletter générale schoolsWP",
  ],
  avantage_concurrentiel: "schoolsWP couvre le haut du funnel (articles informationnels). La landing Agency couvre le bas (décision). Le lead magnet fait le pont. Aucun autre prestataire WordPress freelance n'a cette architecture.",
};

// Projections niche B
const PROJECTIONS = {
  m3: { audits: 2, prix_audit: 700, archi: 0, mrr: 0 },
  m6: { audits: 2, prix_audit: 800, archi: 1, prix_archi: 4000, mrr: 0 },
  m9: { audits: 2, prix_audit: 800, archi: 2, prix_archi: 4500, mrr: 1500 },
  m12: { audits: 3, prix_audit: 900, archi: 2, prix_archi: 5000, mrr: 3000 },
};

const calcMois = (m) => m.audits * (m.prix_audit || 0) + (m.archi || 0) * (m.prix_archi || 0) + (m.mrr || 0);

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Niche B — Pas 'tous les freelances'. Freelances et consultants digitaux qui veulent structurer un système WordPress rentable, automatisé et scalable.", "💼", "blue_background"));
  blocks.push(p(""));
  blocks.push(qot("\"J'aide les freelances digitaux à transformer WordPress en un système business structuré, automatisé et rentable — pour ne plus dépendre uniquement du bouche-à-oreille.\""));
  blocks.push(div());

  // Section 1 — 5 profils ICP
  blocks.push(h1("👥 Les 5 Profils ICP Ciblés"));
  blocks.push(p("Pas 'tous les freelances' — 5 profils précis avec des douleurs spécifiques et des signaux de qualification clairs."));
  blocks.push(p(""));

  ICP_PROFILS.forEach((icp) => {
    blocks.push(tog(`${icp.emoji} ${icp.label} — CA typique : ${icp.ca_typique}`, [
      p(rt("Situation actuelle : ", { bold: true }), rt(icp.situation)),
      p(""),
      p(rt("Pain points :", { bold: true })),
      ...icp.pain_points.map((pp) => bul(rt("✗ ", { color: "red" }), rt(pp))),
      p(""),
      p(rt("Ce qu'il cherche vraiment : ", { bold: true }), rt(icp.gain_cible, { italic: true })),
      p(rt("Signal de qualification : ", { bold: true }), rt(icp.signal_prospect, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 2 — Problèmes communs
  blocks.push(h1("🧠 Les 6 Problèmes Communs des Freelances WordPress"));
  blocks.push(p(""));
  PROBLEMES_COMMUNS.forEach((prob) => {
    blocks.push(tog(`${prob.emoji} ${prob.probleme}`, [
      p(prob.description),
      p(rt("Coût estimé : ", { bold: true }), rt(prob.cout, { italic: true })),
      p(rt("Solution : ", { bold: true }), rt(prob.solution)),
    ]));
  });
  blocks.push(p(""));
  blocks.push(cal("Résumé en 3 mots : architecture, automatisation, acquisition. C'est exactement ce que tu apportes.", "🔑", "orange_background"));
  blocks.push(div());

  // Section 3 — Offre signature
  blocks.push(h1("🏗️ Offre Signature — WordPress Business System™ Freelance Edition"));
  blocks.push(qot(OFFRE_SIGNATURE.pitch_long));
  blocks.push(p(""));
  blocks.push(cal(OFFRE_SIGNATURE.promesse, "✅", "green_background"));
  blocks.push(p(""));
  blocks.push(h3("Les 7 composantes"));
  OFFRE_SIGNATURE.composantes.forEach((c) => {
    blocks.push(bul(rt(`${c.num}. ${c.nom} — `, { bold: true }), rt(c.description)));
  });
  blocks.push(p(""));
  blocks.push(tog(`📋 Livrables complets (${OFFRE_SIGNATURE.deliverables.length})`,
    OFFRE_SIGNATURE.deliverables.map((d) => tod(d))
  ));
  blocks.push(div());

  // Section 4 — Pricing
  blocks.push(h1("💰 Pricing Niche Freelances"));
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

  // Projections
  blocks.push(h3("📊 Projections niche B (réalistes)"));
  blocks.push(tog("Voir les projections par étape", [
    p(rt("M3 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m3).toLocaleString("fr-FR")} € (${PROJECTIONS.m3.audits} audits)`)),
    p(rt("M6 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m6).toLocaleString("fr-FR")} € (${PROJECTIONS.m6.audits} audits + 1 architecture)`)),
    p(rt("M9 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m9).toLocaleString("fr-FR")} € (audits + architectures + ${PROJECTIONS.m9.mrr.toLocaleString("fr-FR")} € MRR)`)),
    p(rt("M12 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m12).toLocaleString("fr-FR")} € (${PROJECTIONS.m12.mrr.toLocaleString("fr-FR")} € MRR inclus)`)),
    p(""),
    cal("Ces projections s'ajoutent aux revenus niche A (formateurs) et affiliation schoolsWP — le modèle hybride est cumulatif.", "💡", "yellow_background"),
  ]));
  blocks.push(div());

  // Section 5 — Clusters SEO
  blocks.push(h1("🔍 Stratégie SEO — 6 Clusters Niche Freelances"));
  blocks.push(cal("Terrain SEO quasi vierge. Aucun concurrent positionné sur 'CRM WordPress freelance' ou 'sortir de Malt WordPress'. Fenêtre d'opportunité à saisir maintenant.", "🎯", "green_background"));
  blocks.push(p(""));

  const totalSat = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  CLUSTERS_SEO.forEach((cluster, ci) => {
    blocks.push(h2(`Cluster ${ci + 1} — ${cluster.nom}`));
    blocks.push(p(rt("Mot-clé pilier : ", { bold: true }), rt(cluster.kw_pilier, { code: true })));
    blocks.push(p(rt("Intention : ", { bold: true }), rt(cluster.intention)));
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

  blocks.push(cal(`${CLUSTERS_SEO.length} clusters — ${totalSat} articles identifiés. 🔴 = M1 (production immédiate) — 🟠 = M2 — 🟡 = M3+`, "📊", "blue_background"));
  blocks.push(div());

  // Section 6 — Différenciateurs
  blocks.push(h1("🧠 Tes 5 Différenciateurs sur cette Niche"));
  blocks.push(p(""));
  DIFFERENCIATEURS.forEach((diff, i) => {
    blocks.push(tog(`${i + 1}. ${diff.competence}`, [
      p(rt("Impact sur la niche : ", { bold: true }), rt(diff.impact)),
      p(rt("Action concrète : ", { bold: true }), rt(diff.action, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 7 — Plan 90 jours
  blocks.push(h1("🗓️ Plan 90 Jours — Activer Niche B"));
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);
  blocks.push(cal(`Objectif 90 jours : 6 articles publiés, page Audit en ligne, lead magnet actif, 1 mission signée. ${totalActions} actions concrètes.`, "🚀", "orange_background"));
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
  blocks.push(h1("🔗 Synergie schoolsWP × Niche Freelances"));
  blocks.push(p(""));
  blocks.push(h3("Audience naturelle"));
  blocks.push(p(SYNERGIE_SCHOOLSWP.audience_naturelle));
  blocks.push(p(""));
  blocks.push(h3("Conversion Agency"));
  blocks.push(p(SYNERGIE_SCHOOLSWP.conversion_agency));
  blocks.push(p(""));
  blocks.push(h3("Tunnel éditorial complet"));
  blocks.push(qot(SYNERGIE_SCHOOLSWP.tunnel));
  blocks.push(p(""));
  blocks.push(h3("Double usage du contenu"));
  SYNERGIE_SCHOOLSWP.articles_double_usage.forEach((item) => blocks.push(bul(item)));
  blocks.push(p(""));
  blocks.push(cal(SYNERGIE_SCHOOLSWP.avantage_concurrentiel, "⚡", "purple_background"));
  blocks.push(div());

  // Footer
  blocks.push(cal("Avantage clé niche B : les freelances digitaux comprennent la valeur du système, ont un budget disponible, et sont sensibles au ROI. Le marché est large, structurable, et le terrain SEO est vierge.", "🏁", "green_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Niche Freelances — WordPress Business System™ Freelance Edition'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  const totalSatellites = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);

  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💼" },
    properties: {
      title: { title: [{ text: { content: "💼 Niche Freelances — WordPress Business System™ Freelance Edition" } }] },
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

  const m12 = calcMois(PROJECTIONS.m12);

  console.log("");
  console.log("🎉 Page créée avec succès !");
  console.log(`🔗 https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📋 Récapitulatif :");
  console.log(`   • ${ICP_PROFILS.length} profils ICP avec pain points, gain cible et signal de qualification`);
  console.log(`   • ${PROBLEMES_COMMUNS.length} problèmes communs avec coût estimé + solution`);
  console.log(`   • ${OFFRE_SIGNATURE.composantes.length} composantes + ${OFFRE_SIGNATURE.deliverables.length} livrables`);
  console.log(`   • ${PRICING_NICHE.length} niveaux de prix avec projections jusqu'à M12`);
  console.log(`   • ${CLUSTERS_SEO.length} clusters SEO — ${totalSatellites} articles identifiés`);
  console.log(`   • ${DIFFERENCIATEURS.length} différenciateurs avec action concrète`);
  console.log(`   • Plan 90 jours — ${totalActions} actions (cases à cocher)`);
  console.log(`   • Projection CA niche B à M12 : ${m12.toLocaleString("fr-FR")} €/mois`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

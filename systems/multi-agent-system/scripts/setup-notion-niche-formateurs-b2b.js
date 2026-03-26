#!/usr/bin/env node
/**
 * setup-notion-niche-formateurs-b2b.js
 * Crée la page "🎓 Niche Formateurs B2B — B2B WordPress System™" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-niche-formateurs-b2b.js
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

const B2C_VS_B2B = {
  b2c: {
    label: "Formateur B2C",
    prix_offre: "97 € – 1 500 €",
    cible: "Particuliers",
    volume: "Élevé (50 à 500+ apprenants)",
    cycle_vente: "24 à 72h",
    budget_technique: "Limité (100–300 €/mois max)",
    problematique_wp: "Tunnel optimisé, checkout rapide, LMS simple",
    valeur_mission: "1 500 – 4 000 €",
  },
  b2b: {
    label: "Formateur B2B",
    prix_offre: "1 500 € – 15 000 € par groupe / entreprise",
    cible: "Entreprises (RH, managers, équipes)",
    volume: "Faible (5 à 50 apprenants par cohorte)",
    cycle_vente: "2 à 8 semaines",
    budget_technique: "Élevé (500–2 000 €/mois possible)",
    problematique_wp: "Multi-comptes, reporting, conformité, onboarding corporate",
    valeur_mission: "6 000 – 15 000 €",
  },
};

const ICP_B2B = [
  {
    emoji: "🏢",
    label: "Organisme de Formation (OF) Indépendant",
    ca_typique: "80 000 – 300 000 €/an",
    certifications: "QUALIOPI, Datadock — dossiers de suivi exigés",
    taille: "1 à 5 formateurs, 20 à 100 entreprises clientes/an",
    situation: "WordPress existant avec un LMS bricolé. Gère les inscriptions par email et Excel. Reporting apprenant fait à la main pour chaque client entreprise.",
    pain_points: [
      "Impossible de créer des espaces formation distincts par entreprise cliente — tout est mélangé",
      "Reporting QUALIOPI généré manuellement : feuilles de présence, évaluations, bilans — 2 à 4h par session",
      "Facturation à chaque nouveau groupe : processus 100 % manuel (devis → bon de commande → facture)",
      "Pas de portail client entreprise : les RH ne voient pas l'avancement de leurs collaborateurs",
    ],
    gain_cible: "Un LMS WordPress avec espaces multi-entreprises, reporting automatique, portail RH, facturation semi-automatisée et traçabilité QUALIOPI.",
    signal_prospect: "Parle de 'professionnaliser' et de 'ne plus passer des heures sur l'administratif de chaque session'.",
    ticket_mission: "8 000 – 15 000 €",
  },
  {
    emoji: "💡",
    label: "Expert Consultant / Formateur Freelance B2B",
    ca_typique: "60 000 – 180 000 €/an",
    certifications: "QUALIOPI en cours ou à venir",
    taille: "Solo ou micro-équipe, 10 à 40 entreprises clientes/an",
    situation: "Vend des programmes intra-entreprise (leadership, vente, digital). Site WordPress vitrine sans LMS. Livraison en présentiel ou Zoom. Veut digitaliser et scaler.",
    pain_points: [
      "Offre de formation non digitalisée — chaque session = intervention physique, impossible de scaler",
      "Pas de plateforme pour les ressources post-formation (replays, ressources complémentaires, suivi)",
      "Tunnel de vente B2B inexistant : page de contact générique, pas de page offre corporate structurée",
      "Devis B2B manuel — word/PDF envoyé par email, suivi par WhatsApp. Aucune automatisation.",
    ],
    gain_cible: "Un WordPress qui digitalise l'offre formation B2B : LMS cohorte, tunnel corporate, devis semi-automatisé et espace ressources post-formation.",
    signal_prospect: "Veut 'créer un programme digital' pour 'arrêter de vendre uniquement du temps'.",
    ticket_mission: "6 000 – 10 000 €",
  },
  {
    emoji: "📊",
    label: "Entrepreneur Académique — Formation B2B Niche",
    ca_typique: "120 000 – 500 000 €/an",
    certifications: "QUALIOPI + potentiellement CPF",
    taille: "Équipe 3 à 10 personnes, 50 à 200 entreprises clientes",
    situation: "A outgrown son LMS actuel (Teachable, Thinkific ou LMS WordPress basique). Gère plusieurs marques ou programmes. A besoin d'une architecture multi-programme scalable.",
    pain_points: [
      "LMS actuel ne supporte pas la segmentation par entreprise + cohorte + programme simultanément",
      "Reporting agrégé impossible : doit exporter depuis 3 outils différents pour produire un bilan client",
      "Onboarding corporate décousu : les RH reçoivent un email avec un lien d'accès — pas de portail dédié",
      "Renouvellement contrat difficile à anticiper : pas de tracking fin de programme + relance automatisée",
    ],
    gain_cible: "Un WordPress B2B Grade — multi-programme, multi-cohorte, reporting RH automatique, pipeline renouvellement, portail client entreprise.",
    signal_prospect: "Cherche une 'vraie plateforme' qui ressemble à ce que les grandes entreprises utilisent, mais sur WordPress.",
    ticket_mission: "10 000 – 15 000 €",
  },
  {
    emoji: "🎓",
    label: "Cabinet de Conseil avec Volet Formation",
    ca_typique: "200 000 – 1 000 000 €/an",
    certifications: "QUALIOPI obligatoire, parfois ISO",
    taille: "5 à 20 consultants-formateurs, projets récurrents grands comptes",
    situation: "Formation est une ligne de service parmi d'autres (conseil, audit, coaching). Utilise un site institutionnel WordPress + outils formation séparés (Moodle, 360Learning). Veut tout centraliser.",
    pain_points: [
      "2 systèmes distincts : site institutionnel (WordPress) + plateforme formation (Moodle ou SaaS) — synchronisation zéro",
      "Clients grands comptes exigent SSO, rapports personnalisés et accès RH dédiés — impossible à offrir avec l'existant",
      "Budget formation CPF non exploité — la plateforme actuelle n'est pas compatible avec les exigences QUALIOPI/CPF",
      "Onboarding de chaque nouveau projet : contrat, accès, kick-off, livraison — tout est manuel et non standardisé",
    ],
    gain_cible: "Un WordPress institutionnel + LMS B2B unifié, avec portail client RH, reporting conforme QUALIOPI, et onboarding standardisé.",
    signal_prospect: "Parle de 'tout centraliser' et de 'se doter d'une plateforme à la hauteur de nos clients'.",
    ticket_mission: "12 000 – 20 000 €",
  },
];

const PROBLEMES_B2B = [
  {
    emoji: "🔴",
    probleme: "LMS WordPress non adapté au B2B",
    description: "Les LMS WordPress standards (Tutor LMS, LearnDash) ne gèrent pas nativement les espaces multi-entreprises, les cohortes datées, et les accès segmentés par RH.",
    specificite_b2b: "Un client entreprise doit voir uniquement SES apprenants, SES statistiques, SES certifications — pas celles des autres clients.",
    solution: "Architecture LMS avancée : groupes WordPress + cohortes datées + portail RH dédié + certificats automatiques par session.",
    valeur: "Économise 3 à 5h de reporting manuel par entreprise cliente par mois.",
  },
  {
    emoji: "🔴",
    probleme: "Onboarding corporate 100 % manuel",
    description: "Chaque nouveau client entreprise reçoit ses accès, son planning et ses ressources manuellement. La coordination se fait par email ou WhatsApp.",
    specificite_b2b: "En B2B, l'onboarding implique souvent plusieurs interlocuteurs : RH, managers, apprenants — chacun avec des accès différents.",
    solution: "Workflow automatisé post-signature : création de comptes apprenants en masse, email de bienvenue RH + apprenant, accès planifié à la cohorte, rappels automatiques.",
    valeur: "De 4 à 6h d'onboarding manuel → 20 min de configuration → automatisation totale.",
  },
  {
    emoji: "🔴",
    probleme: "Reporting QUALIOPI et bilan apprenant manuel",
    description: "Feuilles de présence, évaluations à chaud/froid, bilans de formation — tout est produit manuellement après chaque session.",
    specificite_b2b: "QUALIOPI exige la traçabilité des actions : preuves d'assiduité, évaluations, satisfaction, résultats. Sans automatisation, c'est 2 à 4h de travail par session.",
    solution: "LMS configuré avec tracking automatique (connexion, modules vus, quiz, temps passé) + génération de rapport PDF par apprenant + tableau de bord RH en temps réel.",
    valeur: "Conformité QUALIOPI automatisée. Avantage concurrentiel sur les formateurs B2C qui ne peuvent pas offrir ça.",
  },
  {
    emoji: "🟠",
    probleme: "Tunnel de vente B2B non structuré",
    description: "La page de vente des offres B2B ne parle pas au bon interlocuteur (RH, DAF, DRH). Le formulaire de contact est générique. Pas de page d'offre corporate dédiée.",
    specificite_b2b: "En B2B, le décideur d'achat n'est pas l'apprenant. La page doit convaincre un RH ou un DAF — avec des arguments de ROI, de conformité et de reporting.",
    solution: "Page offre corporate (ROI + conformité + références clients) + formulaire de qualification B2B + devis automatisé + signature électronique (HelloSign ou Yousign).",
    valeur: "Réduire le cycle de vente de 6 semaines à 3 semaines avec un tunnel qui répond aux objections B2B avant le call.",
  },
  {
    emoji: "🟠",
    probleme: "CRM non adapté au cycle long B2B",
    description: "FluentCRM ou les outils standards sont configurés pour des cycles courts (B2C 24-72h). Un prospect B2B peut prendre 2 à 8 semaines avant de signer.",
    specificite_b2b: "Les séquences email B2B doivent être plus longues, plus informatives, moins promotionnelles. Les tags doivent refléter le secteur d'activité du client.",
    solution: "CRM configuré pour le cycle long : séquence 8 emails sur 6 semaines, segmentation par secteur (santé, finance, retail), pipeline commercial visible avec jalons.",
    valeur: "Multiplier par 2 le taux de signature sur les devis avec un nurturing adapté au cycle d'achat B2B.",
  },
  {
    emoji: "🟡",
    probleme: "Facturation et renouvellement non automatisés",
    description: "Chaque groupe = un devis + un bon de commande + une facture envoyés manuellement. Le renouvellement de contrat annuel n'est pas anticipé.",
    specificite_b2b: "Les clients entreprises ont souvent des budgets formation annuels. Le renouvellement est prévisible mais rarement exploité faute de suivi.",
    solution: "SureCart + WooCommerce B2B : facturation automatique, échéancier de paiement, séquence de renouvellement J-60 / J-30 / J-15 avant fin de contrat.",
    valeur: "Taux de renouvellement moyen B2B avec suivi automatisé : 65 à 80 % vs 30 à 40 % sans suivi.",
  },
];

const OFFRE_SIGNATURE = {
  nom: "B2B WordPress System™",
  tagline: "Architecture WordPress B2B Grade pour formateurs ambitieux.",
  pitch_court: "Je construis l'infrastructure WordPress qui permet aux formateurs B2B de gérer plusieurs entreprises clientes, d'automatiser l'onboarding, de produire des reportings conformes et de renouveler leurs contrats sans effort manuel.",
  pitch_long: "La plupart des formateurs B2B gèrent 20 à 50 clients entreprises avec des outils conçus pour le B2C. Résultat : 5 à 10h par semaine perdues en administratif, des reportings QUALIOPI faits à la main, et des renouvellements oubliés. Je construis l'infrastructure WordPress qui traite ça en automatique — et qui donne à vos clients RH un portail à la hauteur de votre expertise.",
  promesse: "En 6 à 10 semaines, votre WordPress gère vos cohortes entreprises, automatise l'onboarding, génère les reportings QUALIOPI, et anticipe les renouvellements. Vous passez de l'administratif à la valeur ajoutée.",
  composantes: [
    { num: "1", nom: "Audit B2B Stratégique", description: "Diagnostic : LMS, CRM, tunnel, facturation, conformité QUALIOPI. Identification des 5 plus grandes pertes de temps et de revenus." },
    { num: "2", nom: "Architecture LMS Multi-Entreprises", description: "Espaces segmentés par client entreprise, cohortes datées, gestion des accès (RH / manager / apprenant), certificats automatiques par session." },
    { num: "3", nom: "Portail RH Entreprise", description: "Dashboard dédié par client entreprise : vue progression apprenants, statistiques de complétion, téléchargement bilans. Accès sécurisé indépendant." },
    { num: "4", nom: "Reporting Automatisé (QUALIOPI-ready)", description: "Tracking assiduité + modules vus + quiz + satisfaction. Génération PDF de bilan par apprenant. Tableau de bord conformité." },
    { num: "5", nom: "CRM Cycle Long B2B (FluentCRM)", description: "Segmentation par secteur, séquence nurturing 8 semaines, pipeline commercial avec jalons, tags comportementaux B2B." },
    { num: "6", nom: "Tunnel Corporate", description: "Page offre B2B (ROI + conformité + références) + formulaire de qualification + devis semi-automatisé + signature électronique intégrée." },
    { num: "7", nom: "Onboarding Automatisé", description: "5 workflows : création comptes apprenants en masse, accès cohorte planifié, email bienvenue RH + apprenant, rappels sessions, accès ressources post-formation." },
    { num: "8", nom: "Renouvellement & Fidélisation", description: "Séquence de renouvellement J-60/J-30/J-15. Rapport de fin de programme automatisé. Proposition de renouvellement pré-remplie." },
    { num: "9", nom: "Formation & Autonomie Client", description: "3h de formation équipe + documentation complète. L'OF gère son système sans intervention externe." },
  ],
  deliverables: [
    "Rapport d'audit B2B (30–40 pages) avec plan d'action ROI",
    "LMS multi-entreprises configuré (espaces + cohortes + accès + certificats)",
    "Portail RH entreprise déployé (1 template utilisé pour tous les clients)",
    "Système de reporting QUALIOPI automatisé (PDF + dashboard)",
    "CRM FluentCRM B2B (segmentation + 5 automatisations cycle long)",
    "Tunnel corporate optimisé (page offre + formulaire qualif + devis)",
    "5 workflows d'automatisation actifs",
    "Système de renouvellement automatisé",
    "Documentation complète + formation équipe 3h enregistrée",
  ],
};

const PRICING_B2B = [
  {
    emoji: "🔍",
    nom: "Audit B2B WordPress System",
    fourchette: "1 200 – 2 000 €",
    duree: "3 à 5 jours ouvrés",
    inclus: [
      "Audit LMS : gestion multi-entreprises, cohortes, reporting actuel",
      "Audit CRM : cycle de vente B2B, séquences, segmentation",
      "Audit tunnel corporate : page offre, qualification, devis",
      "Audit conformité : traçabilité QUALIOPI, preuves actuelles",
      "Audit facturation : processus devis-facture-renouvellement",
      "Rapport 30–35 pages avec plan d'action ROI et estimation temps économisé",
      "Session de restitution 90 min",
    ],
    pour_qui: "OF ou formateur B2B avec CA > 60 000 €/an, au moins 10 clients entreprises actifs.",
    note_vente: "Un audit à 1 500 € qui identifie 5h/semaine d'administratif à automatiser = 250h/an libérées. À votre TJM, c'est bien plus que le prix de l'audit.",
    upsell: "90 % des audits B2B débouchent sur une mission Architecture — la complexité du sujet rend le besoin d'accompagnement évident.",
  },
  {
    emoji: "🏗️",
    nom: "B2B WordPress System™ — Architecture Complète",
    fourchette: "6 000 – 15 000 €",
    duree: "6 à 10 semaines",
    inclus: [
      "Audit inclus ou déduit",
      "LMS multi-entreprises complet (espaces + cohortes + certificats)",
      "Portail RH entreprise (template déployable sur tous les clients)",
      "Reporting QUALIOPI automatisé (PDF + dashboard temps réel)",
      "CRM FluentCRM B2B (segmentation + pipeline + 5 automatisations)",
      "Tunnel corporate optimisé",
      "5 workflows d'onboarding et de renouvellement",
      "Facturation semi-automatisée (SureCart ou WooCommerce B2B)",
      "Formation équipe 3h + documentation complète",
      "Support async 45j post-livraison",
    ],
    pour_qui: "OF ou formateur B2B prêt à investir dans une infrastructure durable. Minimum 20 clients entreprises actifs ou objectif de croissance documenté.",
    note_vente: "À 8 000 €, si le système économise 6h/semaine d'administratif × 48 semaines = 288h. À 500 €/h de TJM équivalent, c'est 144 000 € de valeur libérée sur 1 an.",
    upsell: "Débouche sur un Accompagnement Stratégique Mensuel pour maintenir la conformité et optimiser le renouvellement.",
  },
  {
    emoji: "⚙️",
    nom: "Accompagnement Stratégique Mensuel — B2B",
    fourchette: "1 500 – 3 000 € / mois",
    duree: "Engagement minimum 3 mois",
    inclus: [
      "1 session stratégique mensuelle (90 min)",
      "Suivi KPIs : renouvellements, taux de complétion, satisfaction RH",
      "Mise à jour conformité QUALIOPI si évolution des exigences",
      "Nouveaux workflows selon évolution de l'activité",
      "SEO B2B : 1 article décisionnel niche formateurs B2B/mois",
      "Réponse async 24h (jours ouvrés)",
    ],
    pour_qui: "Client Architecture qui veut maintenir la conformité, optimiser le renouvellement et construire sa visibilité SEO B2B.",
    note_vente: "À 2 000 €/mois, 2 clients = 4 000 € de MRR ultra stable. Les OF signent des engagements longs — la relation B2B est naturellement durable.",
    upsell: "Peut intégrer une migration QUALIOPI complète ou un nouveau programme/cohorte comme module supplémentaire.",
  },
];

const CLUSTERS_SEO = [
  {
    nom: "LMS WordPress B2B — Formation Entreprise",
    kw_pilier: "lms wordpress b2b entreprise",
    intention: "informationnelle",
    note_concurrence: "Concurrence quasi nulle. Personne ne publie sur ce sujet en français avec une approche WordPress native.",
    satellites: [
      { kw: "lms wordpress multi-entreprises formateur", intent: "informationnelle", angle: "Gérer plusieurs clients entreprises sur un seul LMS WordPress — architecture complète", priorite: "🔴 M1" },
      { kw: "cohorte wordpress formation entreprise", intent: "informationnelle", angle: "Créer des cohortes datées sur WordPress : configuration pas à pas", priorite: "🔴 M1" },
      { kw: "portail rh formation wordpress", intent: "informationnelle", angle: "Créer un portail RH sur WordPress : les collaborateurs suivent leur progression en autonomie", priorite: "🔴 M1" },
      { kw: "tutor lms entreprise b2b configuration", intent: "informationnelle", angle: "Tutor LMS pour formation B2B : configuration multi-comptes et cohortes", priorite: "🟠 M2" },
      { kw: "learndash entreprise wordpress", intent: "comparative", angle: "LearnDash vs Tutor LMS pour formation B2B — lequel choisit l'OF sérieux", priorite: "🟠 M2" },
      { kw: "certificat automatique formation wordpress", intent: "informationnelle", angle: "Générer des certificats automatiques par session de formation sur WordPress", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Reporting Formation WordPress QUALIOPI",
    kw_pilier: "reporting formation wordpress qualiopi",
    intention: "informationnelle / décisionnelle",
    note_concurrence: "Zéro article SEO sur le reporting QUALIOPI automatisé avec WordPress. Terrain 100 % vierge.",
    satellites: [
      { kw: "qualiopi wordpress automatisation reporting", intent: "informationnelle", angle: "Automatiser son reporting QUALIOPI sur WordPress — fini les Excel manuels", priorite: "🔴 M1" },
      { kw: "bilan formation wordpress pdf automatique", intent: "informationnelle", angle: "Générer des bilans de formation PDF automatiques depuis WordPress", priorite: "🔴 M1" },
      { kw: "traçabilité formation wordpress lms", intent: "informationnelle", angle: "Traçabilité QUALIOPI sur WordPress : connexion, assiduité, évaluations — tout en automatique", priorite: "🟠 M2" },
      { kw: "satisfaction formation wordpress questionnaire", intent: "informationnelle", angle: "Évaluation à chaud et à froid intégrée sur WordPress — sans outil externe", priorite: "🟠 M2" },
      { kw: "tableau de bord kpi formation wordpress", intent: "informationnelle", angle: "Dashboard KPI formation sur WordPress : ce que votre client RH voit en temps réel", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "CRM WordPress pour Formateurs B2B",
    kw_pilier: "crm wordpress formateur b2b",
    intention: "informationnelle / comparative",
    note_concurrence: "Les articles existants sur FluentCRM ciblent le B2C. Le B2B est totalement absent — avantage SEO immédiat.",
    satellites: [
      { kw: "crm cycle long vente formation b2b wordpress", intent: "informationnelle", angle: "Configurer FluentCRM pour un cycle de vente B2B long (2 à 8 semaines)", priorite: "🔴 M1" },
      { kw: "pipeline commercial formateur wordpress b2b", intent: "informationnelle", angle: "Pipeline commercial Formation B2B dans FluentCRM — de la prise de contact à la signature", priorite: "🔴 M1" },
      { kw: "segmentation entreprise fluentcrm formateur", intent: "informationnelle", angle: "Segmenter ses prospects B2B par secteur d'activité dans FluentCRM", priorite: "🟠 M2" },
      { kw: "nurturing email b2b formation wordpress", intent: "informationnelle", angle: "La séquence email nurturing B2B pour formateurs — 8 emails sur 6 semaines", priorite: "🟠 M2" },
      { kw: "relance devis formation b2b automatique", intent: "informationnelle", angle: "Automatiser la relance de devis formation B2B sans paraître lourd", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Tunnel de Vente WordPress Corporate",
    kw_pilier: "tunnel vente corporate formation wordpress",
    intention: "informationnelle",
    note_concurrence: "Aucun article en français sur les tunnels B2B spécifiques à la formation avec WordPress.",
    satellites: [
      { kw: "page offre formation entreprise wordpress", intent: "informationnelle", angle: "La page d'offre formation B2B qui convainc un RH en 3 minutes — anatomie complète", priorite: "🔴 M1" },
      { kw: "formulaire qualification prospect b2b wordpress", intent: "informationnelle", angle: "Créer un formulaire de qualification B2B sur WordPress — 6 questions qui filtrent", priorite: "🔴 M1" },
      { kw: "devis automatisé formation b2b wordpress", intent: "informationnelle", angle: "Générer des devis formation B2B semi-automatiques depuis WordPress", priorite: "🟠 M2" },
      { kw: "signature electronique wordpress devis formation", intent: "informationnelle", angle: "Intégrer la signature électronique dans WordPress pour les contrats de formation", priorite: "🟠 M2" },
      { kw: "onboarding formation b2b wordpress automatisation", intent: "informationnelle", angle: "Onboarding d'un nouveau client entreprise en formation — automatisation complète", priorite: "🟠 M2" },
      { kw: "renouvellement contrat formation wordpress", intent: "informationnelle", angle: "Automatiser le renouvellement de contrat formation B2B — relance J-60 à J-15", priorite: "🟡 M3" },
    ],
  },
];

const PRODUITS_DIGITAUX = [
  {
    nom: "Template 'Système B2B WordPress' — Kit de démarrage",
    type: "Template + configuration",
    prix: "197 – 497 €",
    contenu: [
      "Template LMS WordPress B2B (structure + pages + cohortes préconfigurées)",
      "Template portail RH (pages client entreprise préconfigurées)",
      "Template devis formation B2B (Google Docs ou PDF exportable)",
      "5 templates d'email onboarding corporate (bienvenue RH + apprenant)",
      "Checklist QUALIOPI WordPress (50 points de traçabilité)",
      "Guide de configuration FluentCRM B2B (15 pages)",
    ],
    pour_qui: "Formateur B2B DIY qui veut implémenter lui-même avec un guide clair.",
    upsell: "Idéal pré-qualification pour la mission Architecture : 'Tu veux que je le configure pour toi ?'",
  },
  {
    nom: "Formation 'Structurer son Offre Formation Entreprise sur WordPress'",
    type: "Mini-formation vidéo (3 modules)",
    prix: "297 – 497 €",
    contenu: [
      "Module 1 — Architecture LMS B2B (espaces multi-entreprises, cohortes, reporting)",
      "Module 2 — CRM et pipeline commercial B2B (FluentCRM cycle long, segmentation secteur)",
      "Module 3 — Tunnel et onboarding corporate (page offre RH, devis, signature, onboarding auto)",
      "Ressources : templates, checklists, exemples de configuration réels",
      "Bonus : FAQ QUALIOPI WordPress — les 10 questions les plus fréquentes",
    ],
    pour_qui: "Formateur B2B qui veut comprendre l'architecture avant de déléguer ou d'implémenter.",
    upsell: "CTA final : 'Vous préférez qu'on le fasse ensemble ? → Demander un audit'.",
  },
  {
    nom: "Checklist 'Architecture LMS Corporate WordPress'",
    type: "Lead magnet premium (PDF téléchargeable)",
    prix: "Gratuit — lead magnet niche B2B",
    contenu: [
      "30 points de contrôle pour un LMS WordPress B2B professionnel",
      "Section LMS : espaces, cohortes, accès, certificats (10 points)",
      "Section CRM : segmentation, pipeline, relances (8 points)",
      "Section Conformité : QUALIOPI, traçabilité, évaluations (7 points)",
      "Section Onboarding : workflow, emails, accès planifiés (5 points)",
    ],
    pour_qui: "Tout formateur B2B qui veut évaluer son WordPress actuel.",
    upsell: "Séquence email post-téléchargement → proposition audit → mission Architecture.",
  },
];

const DIFFERENCIATEURS_ABSOLUS = [
  {
    competence: "Maîtrise de l'environnement réglementaire QUALIOPI",
    rarity: "Extrêmement rare — aucun autre prestataire WordPress ne parle de QUALIOPI",
    impact: "C'est le point de douleur n°1 des OF. Le nommer = crédibilité immédiate, sans concurrence.",
    action: "Publier 'QUALIOPI et WordPress : les 10 exigences que votre LMS doit satisfaire'. Aucun concurrent ne l'a fait.",
  },
  {
    competence: "Architecture multi-entreprises sur WordPress",
    rarity: "Compétence technique avancée — demande 2 à 3 ans d'expérience LMS",
    impact: "C'est le problème que personne ne résout sur le marché. Les OF paient des plateformes SaaS à 500 €/mois faute d'alternative WordPress viable.",
    action: "Créer un blueprint 'LMS WordPress multi-entreprises' — schéma annoté à publier sur schoolsWP.",
  },
  {
    competence: "Connaissance du cycle de vente B2B long",
    rarity: "Les freelances WordPress configurent pour le B2C. Le B2B (2–8 semaines) est ignoré.",
    impact: "Parler de 'nurturing 6 semaines', 'jalons de pipeline', 'qualification RH' résonne immédiatement avec un OF qui perd des deals faute de suivi.",
    action: "Créer le template de pipeline commercial formateur B2B dans FluentCRM — à montrer lors des calls de découverte.",
  },
  {
    competence: "Vision économique de la formation B2B (renouvellement, LTV, CPF)",
    rarity: "Aucun prestataire WordPress ne parle de LTV client B2B, de taux de renouvellement ou d'exploitation du CPF",
    impact: "Parler le langage business de l'OF (CA par client entreprise, coût d'acquisition B2B, LTV) = passer de 'technicien' à 'partenaire stratégique'.",
    action: "Préparer 1 slide 'ROI Business' à présenter lors du call de découverte : économies SaaS + temps libéré + renouvellements anticipés = ROI total de la mission.",
  },
];

const PLAN_90_JOURS = [
  {
    mois: "Mois 1",
    focus: "Fondations et signal d'existence sur la niche B2B",
    actions: [
      { cat: "Contenu SEO prioritaire", items: [
        "Publier 'LMS WordPress multi-entreprises pour formateur B2B' — article pilier (brain-lite.bat)",
        "Publier 'Portail RH formation WordPress : comment vos clients voient l'avancement de leurs équipes'",
        "Publier 'Reporting QUALIOPI automatisé sur WordPress — fini les Excel manuels'",
        "Ajouter les CTA niche B2B dans les articles LMS schoolsWP existants",
      ]},
      { cat: "Agency", items: [
        "Créer la landing page 'Audit B2B WordPress System' (1 200–2 000 €)",
        "Identifier 10 OF sur DATADOCK / QUALIOPI.fr avec un site WordPress",
        "Identifier 5 formateurs freelance B2B sur LinkedIn (> 50k€/an visible)",
        "Préparer le pitch B2B : 1 page ROI avec économies SaaS + temps libéré",
      ]},
      { cat: "Produit digital", items: [
        "Créer la checklist 'Architecture LMS Corporate WordPress' (PDF 30 points)",
        "Configurer la séquence email post-téléchargement (5 emails B2B spécifiques)",
        "Intégrer le lead magnet dans les 3 articles publiés",
      ]},
    ],
  },
  {
    mois: "Mois 2",
    focus: "Preuves et profondeur de niche",
    actions: [
      { cat: "Contenu SEO", items: [
        "Publier 'CRM WordPress cycle long pour formateur B2B — FluentCRM B2B pipeline'",
        "Publier 'Page d'offre formation entreprise WordPress : convaincre un RH en 3 min'",
        "Publier 'Onboarding corporate automatisé sur WordPress — de 4h à 20 min'",
        "Optimiser les 3 articles M1 avec le workflow W1 (V1 → Audit → V2)",
      ]},
      { cat: "Agency", items: [
        "Réaliser le premier Audit B2B (même à tarif réduit 800 € pour avoir la première référence)",
        "Documenter les résultats : temps économisé + problème QUALIOPI résolu",
        "Publier l'étude de cas sur schoolsWP",
        "Approcher 5 OF sur LinkedIn avec l'article QUALIOPI en accroche",
      ]},
      { cat: "Produit", items: [
        "Lancer la formation 'Structurer son Offre Formation Entreprise sur WordPress' (297 €)",
        "Enregistrer les 3 modules (objectif : 2h30 total)",
        "Créer la landing page dédiée + intégration dans la séquence email",
      ]},
    ],
  },
  {
    mois: "Mois 3",
    focus: "Systématisation et première mission Architecture complète",
    actions: [
      { cat: "Agency", items: [
        "Viser la signature de la première mission Architecture B2B (6 000–10 000 €)",
        "Automatiser le funnel Audit B2B : formulaire qualif → cal auto → email pré-brief → devis",
        "Créer le template Notion d'onboarding client B2B (spécifique OF / formateur freelance)",
        "Publier 1 post LinkedIn : 'Comment un OF gère 30 clients entreprises sur un seul WordPress'",
      ]},
      { cat: "Contenu SEO", items: [
        "Publier 'Devis automatisé formation B2B sur WordPress — de Word à SureCart'",
        "Publier 'Renouvellement contrat formation B2B — la séquence qui évite les pertes'",
        "Démarrer le cluster 'Reporting Formation WordPress QUALIOPI' (article pilier)",
        "Mettre en place FAQ AIO sur les 3 articles les plus lus",
      ]},
      { cat: "Positionnement", items: [
        "Mettre à jour le profil LinkedIn : 'Architecte WordPress pour Formateurs B2B'",
        "Demander 1 recommandation LinkedIn au client de l'Audit",
        "Créer 1 carrousel LinkedIn : 'Les 5 signes que votre WordPress OF vous fait perdre 5h/semaine'",
        "Intégrer la section 'Formateurs B2B' dans la page Agency schoolsWP",
      ]},
    ],
  },
];

// Projections financières niche B2B
const PROJECTIONS = {
  m3: { audits: 1, prix_audit: 1500, archi: 0, mrr: 0, produits: 500 },
  m6: { audits: 1, prix_audit: 1800, archi: 1, prix_archi: 8000, mrr: 0, produits: 1000 },
  m9: { audits: 2, prix_audit: 1800, archi: 1, prix_archi: 9000, mrr: 2500, produits: 1500 },
  m12: { audits: 2, prix_audit: 2000, archi: 2, prix_archi: 10000, mrr: 5000, produits: 2000 },
};
const calcMois = (m) =>
  m.audits * (m.prix_audit || 0) +
  (m.archi || 0) * (m.prix_archi || 0) +
  (m.mrr || 0) +
  (m.produits || 0);

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Niche chirurgicale — pas 'les formateurs'. Les formateurs B2B premium qui vendent 1 500 à 15 000 € par entreprise et ont besoin d'une vraie infrastructure WordPress.", "🎓", "purple_background"));
  blocks.push(p(""));
  blocks.push(qot("\"Je construis l'infrastructure WordPress qui permet aux formateurs B2B de gérer plusieurs entreprises clientes, d'automatiser la conformité QUALIOPI, et de renouveler leurs contrats sans effort manuel.\""));
  blocks.push(div());

  // Section 1 — B2C vs B2B
  blocks.push(h1("⚖️ Formateur B2C vs Formateur B2B — Pourquoi C'est Un Autre Marché"));
  blocks.push(p(""));
  blocks.push(cal("Un formateur B2B ne cherche pas 'un LMS'. Il cherche une infrastructure qui lui permet de gérer 20 à 50 clients entreprises sans s'épuiser en administratif.", "🎯", "orange_background"));
  blocks.push(p(""));

  blocks.push(tog("Voir le tableau comparatif B2C vs B2B", [
    p(rt("Prix de l'offre formation :", { bold: true })),
    bul(rt("B2C : ", { bold: true }), rt(`${B2C_VS_B2B.b2c.prix_offre} — vente volume`)),
    bul(rt("B2B : ", { bold: true }), rt(`${B2C_VS_B2B.b2b.prix_offre} — vente valeur par groupe`)),
    p(""),
    p(rt("Cycle de vente :", { bold: true })),
    bul(rt("B2C : ", { bold: true }), rt(B2C_VS_B2B.b2c.cycle_vente)),
    bul(rt("B2B : ", { bold: true }), rt(B2C_VS_B2B.b2b.cycle_vente)),
    p(""),
    p(rt("Problématique WordPress spécifique :", { bold: true })),
    bul(rt("B2C : ", { bold: true }), rt(B2C_VS_B2B.b2c.problematique_wp)),
    bul(rt("B2B : ", { bold: true }), rt(B2C_VS_B2B.b2b.problematique_wp)),
    p(""),
    p(rt("Valeur de mission Agency :", { bold: true })),
    bul(rt("B2C : ", { bold: true }), rt(B2C_VS_B2B.b2c.valeur_mission)),
    bul(rt("B2B : ", { bold: true }), rt(`${B2C_VS_B2B.b2b.valeur_mission} — le ticket le plus élevé de toutes les niches`)),
  ]));
  blocks.push(div());

  // Section 2 — 4 profils ICP
  blocks.push(h1("👥 Les 4 Profils ICP Formateurs B2B"));
  blocks.push(p(""));
  ICP_B2B.forEach((icp) => {
    blocks.push(tog(
      `${icp.emoji} ${icp.label} — Ticket mission : ${icp.ticket_mission}`,
      [
        p(rt("CA typique : ", { bold: true }), rt(icp.ca_typique)),
        p(rt("Certifications : ", { bold: true }), rt(icp.certifications)),
        p(rt("Taille structure : ", { bold: true }), rt(icp.taille)),
        p(rt("Situation actuelle : ", { bold: true }), rt(icp.situation)),
        p(""),
        p(rt("Pain points B2B :", { bold: true })),
        ...icp.pain_points.map((pp) => bul(rt("✗ ", { color: "red" }), rt(pp))),
        p(""),
        p(rt("Ce qu'il cherche vraiment : ", { bold: true }), rt(icp.gain_cible, { italic: true })),
        p(rt("Signal de qualification : ", { bold: true }), rt(icp.signal_prospect, { italic: true })),
      ]
    ));
  });
  blocks.push(p(""));
  blocks.push(cal(`Ticket moyen pondéré : ~10 000 €. C'est la niche avec le ticket le plus élevé de tout le portfolio. 1 mission Architecture B2B = CA mensuel complet.`, "💰", "green_background"));
  blocks.push(div());

  // Section 3 — Problèmes B2B
  blocks.push(h1("🧠 Les 6 Problèmes Spécifiques au B2B"));
  blocks.push(p("Ce qui différencie cette niche : les problèmes sont tous liés à la gestion multi-clients, à la conformité réglementaire et aux cycles longs. Les solutions B2C ne fonctionnent pas."));
  blocks.push(p(""));
  PROBLEMES_B2B.forEach((prob) => {
    blocks.push(tog(`${prob.emoji} ${prob.probleme}`, [
      p(prob.description),
      p(rt("Spécificité B2B : ", { bold: true }), rt(prob.specificite_b2b, { italic: true })),
      p(rt("Solution : ", { bold: true }), rt(prob.solution)),
      p(rt("Valeur : ", { bold: true }), rt(prob.valeur)),
    ]));
  });
  blocks.push(div());

  // Section 4 — Offre signature
  blocks.push(h1("🏗️ Offre Signature — B2B WordPress System™"));
  blocks.push(qot(OFFRE_SIGNATURE.pitch_long));
  blocks.push(p(""));
  blocks.push(cal(OFFRE_SIGNATURE.promesse, "✅", "green_background"));
  blocks.push(p(""));
  blocks.push(h3(`Les ${OFFRE_SIGNATURE.composantes.length} composantes`));
  OFFRE_SIGNATURE.composantes.forEach((c) => {
    blocks.push(bul(rt(`${c.num}. ${c.nom} — `, { bold: true }), rt(c.description)));
  });
  blocks.push(p(""));
  blocks.push(tog(`📋 Livrables complets (${OFFRE_SIGNATURE.deliverables.length})`,
    OFFRE_SIGNATURE.deliverables.map((d) => tod(d))
  ));
  blocks.push(div());

  // Section 5 — Pricing
  blocks.push(h1("💰 Pricing Premium B2B"));
  blocks.push(cal("Le B2B justifie les tickets les plus élevés. Un OF qui signe 20 clients entreprises à 3 000 €/groupe fait 60 000 €/an. Il peut investir 8 000 € dans son infrastructure.", "💎", "purple_background"));
  blocks.push(p(""));
  PRICING_B2B.forEach((tier) => {
    blocks.push(h2(`${tier.emoji} ${tier.nom} — ${tier.fourchette}`));
    blocks.push(p(rt("Durée : ", { bold: true }), rt(tier.duree)));
    blocks.push(p(rt("Pour qui : ", { bold: true }), rt(tier.pour_qui)));
    blocks.push(p(""));
    blocks.push(tog(`📋 Inclus (${tier.inclus.length} éléments)`,
      tier.inclus.map((item) => bul(item))
    ));
    blocks.push(p(""));
    blocks.push(qot(`Note de vente : ${tier.note_vente}`));
    blocks.push(p(rt("Upsell : ", { bold: true }), rt(tier.upsell)));
    blocks.push(p(""));
  });

  blocks.push(h3("📊 Projections niche B2B"));
  blocks.push(tog("Voir les projections par étape", [
    ...Object.entries(PROJECTIONS).map(([k, v]) =>
      p(rt(`${k.toUpperCase()} : `, { bold: true }), rt(`${calcMois(v).toLocaleString("fr-FR")} €/mois`))
    ),
    p(""),
    cal("1 mission Architecture B2B à 10 000 € = objectif mensuel atteint. Le M12 inclut 5 000 € de MRR Agency + 2 000 € de produits.", "🎯", "green_background"),
  ]));
  blocks.push(div());

  // Section 6 — Clusters SEO
  blocks.push(h1("🔍 Stratégie SEO — 4 Clusters Ultra-Ciblés B2B"));
  const totalSat = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  blocks.push(cal(`Terrain 100 % vierge. Aucun concurrent ne publie sur 'LMS WordPress B2B' ou 'QUALIOPI WordPress' en français. ${totalSat} articles identifiés sur ${CLUSTERS_SEO.length} clusters.`, "🎯", "green_background"));
  blocks.push(p(""));

  CLUSTERS_SEO.forEach((cluster, ci) => {
    blocks.push(h2(`Cluster ${ci + 1} — ${cluster.nom}`));
    blocks.push(p(rt("Mot-clé pilier : ", { bold: true }), rt(cluster.kw_pilier, { code: true })));
    blocks.push(p(rt("Concurrence : ", { bold: true }), rt(cluster.note_concurrence, { italic: true })));
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

  blocks.push(cal("🔴 M1 = production immédiate. 🟠 M2. 🟡 M3+", "📊", "blue_background"));
  blocks.push(div());

  // Section 7 — Produits digitaux
  blocks.push(h1("📦 Produits Digitaux Alignés Niche B2B"));
  blocks.push(p("3 produits qui créent un continuum : lead magnet gratuit → formation → template → mission Agency."));
  blocks.push(p(""));
  PRODUITS_DIGITAUX.forEach((prod, i) => {
    blocks.push(tog(`${i + 1}. ${prod.nom} — ${prod.prix}`, [
      p(rt("Type : ", { bold: true }), rt(prod.type)),
      p(rt("Pour qui : ", { bold: true }), rt(prod.pour_qui)),
      p(rt("Upsell : ", { bold: true }), rt(prod.upsell)),
      p(""),
      p(rt("Contenu :", { bold: true })),
      ...prod.contenu.map((c) => bul(c)),
    ]));
  });
  blocks.push(div());

  // Section 8 — Différenciateurs
  blocks.push(h1("🧠 Tes 4 Différenciateurs Absolus sur cette Niche"));
  blocks.push(cal("Ce sont des compétences que quasiment aucun autre prestataire WordPress ne combine. C'est une fenêtre d'opportunité rare — à saisir avant que la niche soit saturée.", "⚡", "yellow_background"));
  blocks.push(p(""));
  DIFFERENCIATEURS_ABSOLUS.forEach((diff, i) => {
    blocks.push(tog(`${i + 1}. ${diff.competence}`, [
      p(rt("Rareté : ", { bold: true }), rt(diff.rarity)),
      p(rt("Impact : ", { bold: true }), rt(diff.impact)),
      p(rt("Action : ", { bold: true }), rt(diff.action, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 9 — Plan 90 jours
  blocks.push(h1("🗓️ Plan 90 Jours — Activer la Niche B2B"));
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);
  blocks.push(cal(`Objectif 90 jours : 3 clusters SEO amorcés, checklist B2B en lead magnet, 1 Audit signé, 1 formation digitale lancée. ${totalActions} actions concrètes.`, "🚀", "orange_background"));
  blocks.push(p(""));

  PLAN_90_JOURS.forEach((mois) => {
    blocks.push(h2(`${mois.mois} — ${mois.focus}`));
    blocks.push(p(""));
    mois.actions.forEach((cat) => {
      blocks.push(tog(`📌 ${cat.cat}`, cat.items.map((item) => tod(item))));
    });
    blocks.push(p(""));
  });

  blocks.push(div());

  // Footer
  blocks.push(cal(`Tu passes de 'Expert WordPress avancé' à 'Spécialiste des architectures WordPress B2B'. C'est rare. C'est premium. C'est crédible. Projection M12 : ${calcMois(PROJECTIONS.m12).toLocaleString("fr-FR")} €/mois.`, "🏁", "purple_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Niche Formateurs B2B — B2B WordPress System™'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  const totalSatellites = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  const totalActions = PLAN_90_JOURS.reduce((a, m) => a + m.actions.reduce((b, c) => b + c.items.length, 0), 0);
  const m12 = calcMois(PROJECTIONS.m12);

  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🎓" },
    properties: {
      title: { title: [{ text: { content: "🎓 Niche Formateurs B2B — B2B WordPress System™" } }] },
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
  console.log(`   • Tableau B2C vs B2B (6 critères comparés)`);
  console.log(`   • ${ICP_B2B.length} profils ICP avec ticket mission (jusqu'à 20 000 €)`);
  console.log(`   • ${PROBLEMES_B2B.length} problèmes B2B avec spécificité + valeur chiffrée`);
  console.log(`   • ${OFFRE_SIGNATURE.composantes.length} composantes + ${OFFRE_SIGNATURE.deliverables.length} livrables`);
  console.log(`   • ${PRICING_B2B.length} niveaux de prix (Audit 1 200–2 000 € / Architecture 6 000–15 000 €)`);
  console.log(`   • ${CLUSTERS_SEO.length} clusters SEO — ${totalSatellites} articles (terrain 100 % vierge)`);
  console.log(`   • ${PRODUITS_DIGITAUX.length} produits digitaux alignés (lead magnet + formation + template)`);
  console.log(`   • ${DIFFERENCIATEURS_ABSOLUS.length} différenciateurs absolus`);
  console.log(`   • Plan 90 jours — ${totalActions} actions concrètes`);
  console.log(`   • Projection CA M12 : ${m12.toLocaleString("fr-FR")} €/mois`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

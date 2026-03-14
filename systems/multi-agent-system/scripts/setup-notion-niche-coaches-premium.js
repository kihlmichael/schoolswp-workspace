#!/usr/bin/env node
/**
 * setup-notion-niche-coaches-premium.js
 * Crée la page "🏆 Niche Coaches Premium — WordPress Growth System™" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-niche-coaches-premium.js
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
    emoji: "💼",
    label: "Coach Business / Entrepreneur",
    ca_typique: "80 000 – 200 000 €/an",
    offre_type: "Accompagnement individuel 3–6 mois (3 000–8 000 €), mastermind (5 000–15 000 €)",
    situation: "Audience LinkedIn ou email existante, programme premium en place, mais WordPress bricolé au fil des ans. Utilise Kajabi ou Systeme.io en parallèle sans cohérence.",
    pain_points: [
      "Site WordPress + Kajabi + ActiveCampaign + Stripe séparés — aucune synchronisation",
      "Tunnel de vente programme premium non optimisé : trop d'étapes, pas de preuve sociale au bon endroit",
      "Pas de segmentation entre prospects froids, leads chauds et clients actifs",
      "Onboarding nouveau client 100 % manuel — 4 à 5 heures par nouveau client",
    ],
    gain_cible: "Un écosystème WordPress unifié qui remplace 3 outils SaaS, segmente automatiquement, et onboarde les clients sans intervention manuelle.",
    signal_prospect: "Parle de 'simplifier' et de 'tout avoir au même endroit' — souvent frustré par la multiplication des abonnements SaaS.",
    ticket_moyen_mission: "6 000 – 8 000 €",
  },
  {
    emoji: "🧘",
    label: "Coach Développement Personnel / Life Coach",
    ca_typique: "40 000 – 100 000 €/an",
    offre_type: "Séances individuelles (200–400 €/h), programme groupe en ligne (1 500–4 000 €)",
    situation: "Forte présence réseaux sociaux (Instagram, YouTube), audience engagée. Site WordPress comme blog. Monétise partiellement — ventes incohérentes, pas de tunnel clair.",
    pain_points: [
      "Dépend de l'algorithme Instagram pour 80 % de ses leads — risque majeur",
      "Pas de liste email structurée — envois irréguliers sans segmentation",
      "Programme groupe ouvert 2 fois par an : pas de liste d'attente automatisée, pas de nurturing entre les sessions",
      "Checkout mal configuré — abandons de panier non récupérés",
    ],
    gain_cible: "Un WordPress qui capte l'audience sociale, la nourrit par email, et automatise les ouvertures de programme avec liste d'attente et nurturing.",
    signal_prospect: "Veut 'arrêter de tout faire manuellement' lors des ouvertures de programme.",
    ticket_moyen_mission: "4 000 – 6 000 €",
  },
  {
    emoji: "🏋️",
    label: "Coach Sportif / Santé Premium",
    ca_typique: "50 000 – 120 000 €/an",
    offre_type: "Coaching en ligne individuel (500–2 000 €/mois), programme groupe (1 200–3 000 €)",
    situation: "Clientèle fidèle, résultats prouvés, mais acquisition 100 % bouche-à-oreille. Site WordPress basique ou Wix. Pas de présence SEO, pas de contenu décisionnel.",
    pain_points: [
      "Zéro acquisition inbound — si les recommandations tarissent, le CA s'effondre",
      "Pas de lead magnet niche (nutrition, training plan, assessment) — perd des contacts froids",
      "Suivi client 100 % manuel (WhatsApp, email) — pas de CRM, pas d'automatisation post-programme",
      "Upsell inexistant — chaque client repart sans offre de continuation",
    ],
    gain_cible: "Un WordPress avec SEO décisionnel niche santé, lead magnet expert, et système de suivi client automatisé.",
    signal_prospect: "Cherche à 'ne plus dépendre uniquement du réseau' et à 'créer une présence en ligne professionnelle'.",
    ticket_moyen_mission: "4 000 – 5 500 €",
  },
  {
    emoji: "📈",
    label: "Coach Carrière / Leadership B2B",
    ca_typique: "60 000 – 150 000 €/an",
    offre_type: "Coaching cadre (300–600 €/h), programme leadership (5 000–12 000 €), interventions entreprises",
    situation: "Positionnement premium assumé, CV impressionnant. Mais numérique quasi absent — LinkedIn fort, site inexistant ou daté. Acquiert par le réseau exclusivement.",
    pain_points: [
      "Visibilité numérique ne correspond pas à l'expertise réelle — décalage crédibilité",
      "Pas de contenu de référence (articles, white papers, études de cas) pour la décision B2B",
      "Le site n'est pas pensé pour la décision B2B (pas de témoignages structurés, pas de cas clients)",
      "Aucune automatisation — chaque devis, relance et contrat est traité à la main",
    ],
    gain_cible: "Un WordPress d'autorité B2B : page de vente premium, proof wall structuré, lead magnet expert (assessment ou guide), et pipeline commercial semi-automatisé.",
    signal_prospect: "Parle de 'se donner une présence digitale à la hauteur de son expertise'.",
    ticket_moyen_mission: "5 000 – 8 000 €",
  },
  {
    emoji: "🎯",
    label: "Coach / Mentor sur une expertise métier spécifique",
    ca_typique: "60 000 – 180 000 €/an",
    offre_type: "Programmes high-ticket (3 000–10 000 €), membership mensuel (200–500 €/mois), mastermind (8 000–20 000 €)",
    situation: "Forte expertise sectorielle (marketing, finance, immobilier, copywriting). A déjà vendu des programmes. WordPress existant avec LMS partiel — mais parcours client décousu.",
    pain_points: [
      "LMS mal structuré — apprenants perdus, taux de complétion < 25 %, avis négatifs sur l'UX",
      "Membership pas rentable — churn élevé faute de valeur ajoutée régulière automatisée",
      "Mastermind : onboarding et coordination 100 % manuels (Notion + WhatsApp + email)",
      "Pas de stratégie d'upsell intelligente — chaque montée en gamme est une conversation à relancer manuellement",
    ],
    gain_cible: "Un WordPress qui orchestre le parcours complet : entrée par lead magnet → programme → membership → mastermind. Chaque étape automatisée.",
    signal_prospect: "Parle de 'construire un vrai écosystème' et de 'scaler sans embaucher'.",
    ticket_moyen_mission: "6 000 – 10 000 €",
  },
];

const PROBLEMES_COMMUNS = [
  {
    emoji: "🔴",
    probleme: "Stack SaaS dispersé et coûteux",
    description: "Le coach utilise Kajabi (150–200 €/mois) + ActiveCampaign (100–200 €/mois) + Stripe + Calendly + Zoom + une solution de cours. Rien n'est synchronisé. Les données clients sont éparpillées.",
    cout: "400 à 600 €/mois d'abonnements SaaS + 5 à 8h/mois de synchronisation manuelle.",
    solution: "Stack WordPress natif unifié : LMS + FluentCRM + SureCart + cal.com. Moins de 100 €/mois d'abonnements, tout dans 1 tableau de bord.",
  },
  {
    emoji: "🔴",
    probleme: "Tunnel premium non optimisé",
    description: "La page de vente du programme high-ticket ne suit pas de structure éprouvée. La preuve sociale est absente ou mal placée. Le checkout a trop d'étapes. Le taux de conversion est < 1 %.",
    cout: "Passer de 0,5 % à 2 % sur un programme à 5 000 € = multiplier le CA par 4 avec le même trafic.",
    solution: "Page de vente AIDA avec preuve sociale au-dessus du fold + checkout SureCart 2 étapes + order bump + page confirmation avec upsell.",
  },
  {
    emoji: "🔴",
    probleme: "Pas de CRM segmenté",
    description: "Toute la liste email est traitée identiquement. Prospects froids, leads chauds, clients actifs et anciens clients reçoivent les mêmes emails. Taux d'ouverture < 15 %.",
    cout: "40 % de leads perdus faute de relance comportementale. Chaque 'batch email' irrite une partie de la liste.",
    solution: "FluentCRM : 5 segments minimum (froid / nurturing / découverte planifiée / client actif / alumni). Séquences adaptées à chaque statut.",
  },
  {
    emoji: "🟠",
    probleme: "Onboarding client 100 % manuel",
    description: "Chaque nouveau client reçoit les accès, les ressources, le planning et les premières instructions manuellement. 4 à 6 heures perdues par nouveau client.",
    cout: "À 10 nouveaux clients/an = 40 à 60 heures perdues. À TJM équivalent = 8 000 à 12 000 € de temps non facturé.",
    solution: "Workflow automatisé post-achat : email bienvenue + accès LMS auto + ressources semaine 1 + rappel call J+3.",
  },
  {
    emoji: "🟠",
    probleme: "Pas d'upsell structuré",
    description: "À la fin d'un programme, le client repart sans offre de continuation. Pas d'upsell vers le niveau supérieur (ex : individuel → mastermind), pas de membership, pas de relance à 6 mois.",
    cout: "La LTV (lifetime value) d'un client coaching pourrait être 2 à 3× plus élevée avec un upsell structuré.",
    solution: "Séquence post-programme automatisée : J+30 assessment + offre continuation + J+90 invitation mastermind ou membership.",
  },
  {
    emoji: "🟡",
    probleme: "Absence de SEO décisionnel",
    description: "Le site du coach n'apparaît jamais sur des requêtes de type 'meilleur coach [niche]' ou 'programme [niche] WordPress'. L'acquisition est 100 % réseaux sociaux ou bouche-à-oreille.",
    cout: "Risque d'acquisition critique : 1 changement d'algorithme peut réduire le CA de 30 à 50 %.",
    solution: "1 cluster SEO décisionnel sur la niche du coach : 8 à 12 articles, 1 pilier d'autorité, maillage optimisé.",
  },
];

const OFFRE_SIGNATURE = {
  nom: "WordPress Growth System™ pour Coaches Premium",
  tagline: "Transformation stratégique, pas technique.",
  pitch_court: "Je structure l'écosystème WordPress de coaches premium pour transformer leur expertise en système d'acquisition et de rétention autonome.",
  pitch_long: "Les coaches premium font confiance à des SaaS à 600 €/mois qui ne se parlent pas, des tunnels qui convertissent à 0,5 %, et un onboarding client qui leur prend 5 heures par mois. Je remplace tout ça par un WordPress unifié — un seul tableau de bord, une segmentation qui travaille, un tunnel optimisé, et des automatisations qui font tourner la machine pendant qu'ils coachent.",
  promesse: "En 5 à 8 semaines, l'écosystème WordPress du coach génère des leads qualifiés, les convertit, les onboarde et les fidélise — sans dépendre d'une plateforme externe.",
  composantes: [
    { num: "1", nom: "Audit Stratégique Coach", description: "6 dimensions : stack outils, tunnel, CRM, LMS si applicable, performance, cohérence business. Rapport + plan d'action ROI." },
    { num: "2", nom: "Refonte Architecture WordPress", description: "Structure de pages, hiérarchie, stack rationalisé. Remplacement des SaaS inutiles par des équivalents natifs WordPress." },
    { num: "3", nom: "Tunnel Premium Optimisé", description: "Page de vente haute valeur (AIDA + preuve sociale + FAQ objections) + checkout SureCart 2 étapes + upsell post-achat. Tests A/B intégrés." },
    { num: "4", nom: "CRM Segmenté (FluentCRM)", description: "5 segments minimum, tags comportementaux, séquences automatisées (nurturing / post-découverte / post-achat / upsell / alumni)." },
    { num: "5", nom: "Automatisation Complète", description: "5 workflows : bienvenue lead, relance découverte, onboarding client, post-programme (upsell), réactivation alumni 6 mois." },
    { num: "6", nom: "LMS si Applicable", description: "Architecture programme : structure de progression, prérequis, certificats. Configuration Tutor LMS ou LearnDash selon le profil." },
    { num: "7", nom: "Optimisation Conversion", description: "Audit et A/B test page de vente (CTA, preuve sociale, garantie), réduction friction checkout, optimisation page confirmation." },
    { num: "8", nom: "Formation & Autonomie Client", description: "2h de formation + documentation complète + support async 30j. Le coach gère son système sans toi." },
  ],
  deliverables: [
    "Rapport d'audit stratégique (25–35 pages) + plan d'action priorisé ROI",
    "Architecture WordPress reconstruite (stack rationalisé documenté)",
    "Tunnel premium 3 pages optimisé (page de vente + checkout + confirmation + upsell)",
    "CRM FluentCRM configuré (5 segments + 5 automatisations actives)",
    "Dashboard de pilotage (GA4 + FluentCRM analytics + KPIs business)",
    "LMS configuré si applicable (structure + progression + certificats)",
    "Documentation complète du système + formation 2h enregistrée",
    "Support async 30j post-livraison",
  ],
};

const PRICING_NICHE = [
  {
    emoji: "🔍",
    nom: "Audit Growth System Coach",
    fourchette: "800 – 1 500 €",
    duree: "3 à 4 jours ouvrés",
    inclus: [
      "Audit stack outils + coût mensuel réel vs alternatives WordPress",
      "Audit tunnel : page de vente, checkout, taux de conversion estimé",
      "Audit CRM : segmentation, séquences actives, taux d'ouverture",
      "Audit acquisition : sources, cohérence avec positionnement premium",
      "Rapport 25–30 pages + plan d'action priorisé ROI",
      "Session de restitution 90 min",
    ],
    pour_qui: "Coach avec CA > 50 000 €/an, programme premium existant, WordPress en ligne depuis > 1 an.",
    note_vente: "Un audit à 1 200 € qui identifie 600 €/mois d'abonnements SaaS inutiles = ROI en 60 jours. Et ça, c'est avant la mission.",
    upsell: "85 % des audits débouchent sur une mission Architecture. L'audit crédibilise le besoin — il ne crée pas la vente, il la légitime.",
  },
  {
    emoji: "🏗️",
    nom: "WordPress Growth System™ — Architecture Complète",
    fourchette: "4 000 – 8 000 €",
    duree: "5 à 8 semaines",
    inclus: [
      "Audit inclus ou déduit si déjà réalisé",
      "Refonte architecture complète (stack, pages, hiérarchie)",
      "Tunnel premium 3 pages + checkout + upsell",
      "CRM FluentCRM : 5 segments + 5 automatisations",
      "LMS si applicable (configuration complète)",
      "Optimisation performance (cache, CDN, Core Web Vitals)",
      "Dashboard de pilotage + GA4 paramétré",
      "Formation 2h + documentation complète",
      "Support async 30j",
    ],
    pour_qui: "Coach premium prêt à investir dans un système durable. CA > 50 000 €/an, stack SaaS coûteux, tunnel sous-performant.",
    note_vente: "À 5 000 €, si le tunnel passe de 0,5 % à 2 % de conversion sur un programme à 5 000 € avec 200 visites/mois : +7 500 € de CA mensuel supplémentaire.",
    upsell: "Débouche sur l'Accompagnement Mensuel Stratégique pour maintenir et optimiser.",
  },
  {
    emoji: "⚙️",
    nom: "Accompagnement Stratégique Mensuel — Coach Premium",
    fourchette: "1 000 – 2 000 € / mois",
    duree: "Engagement minimum 3 mois",
    inclus: [
      "1 session stratégique mensuelle (60–90 min)",
      "Suivi KPIs : leads, taux de conversion, complétion, LTV",
      "Optimisation continue tunnel + séquences email",
      "SEO stratégique : 1 article décisionnel niche coach/mois",
      "Nouvelles automatisations selon évolution de l'offre",
      "Réponse async 24h (jours ouvrés)",
    ],
    pour_qui: "Client Architecture qui lance un nouveau programme ou veut maintenir la dynamique de croissance.",
    note_vente: "À 1 500 €/mois, 3 clients = 4 500 € de MRR. Le ticket élevé justifie moins de clients — qualité avant volume.",
    upsell: "Peut intégrer des modules supplémentaires (nouveau tunnel, nouveau LMS) facturés en extra.",
  },
];

const CLUSTERS_SEO = [
  {
    nom: "CRM WordPress pour Coach",
    kw_pilier: "crm wordpress coach",
    intention: "informationnelle / comparative",
    satellites: [
      { kw: "fluentcrm pour coach", intent: "décisionnelle", angle: "FluentCRM pour coaches : configuration spécifique high-ticket (pas e-commerce)", priorite: "🔴 M1" },
      { kw: "remplacer kajabi par wordpress", intent: "décisionnelle", angle: "Quitter Kajabi : ce que WordPress fait mieux et moins cher", priorite: "🔴 M1" },
      { kw: "segmentation email coach wordpress", intent: "informationnelle", angle: "5 segments email que tout coach premium doit configurer", priorite: "🔴 M1" },
      { kw: "crm coach en ligne wordpress", intent: "informationnelle", angle: "Gérer ses prospects coaching dans WordPress — du CRM à l'onboarding", priorite: "🟠 M2" },
      { kw: "activecampaign vs fluentcrm coach", intent: "comparative", angle: "ActiveCampaign vs FluentCRM pour coach : lequel choisir selon ton CA", priorite: "🟠 M2" },
    ],
  },
  {
    nom: "Tunnel WordPress pour Coach Premium",
    kw_pilier: "tunnel wordpress coach",
    intention: "informationnelle",
    satellites: [
      { kw: "page de vente programme coaching wordpress", intent: "informationnelle", angle: "Anatomie d'une page de vente coaching high-ticket qui convertit à 2 %+", priorite: "🔴 M1" },
      { kw: "tunnel high-ticket wordpress coach", intent: "informationnelle", angle: "Le tunnel high-ticket WordPress : 3 pages, 1 logique, 0 complication", priorite: "🔴 M1" },
      { kw: "checkout coaching wordpress optimisé", intent: "informationnelle", angle: "Réduire l'abandon checkout sur un programme à 3 000 €+ — 5 ajustements", priorite: "🟠 M2" },
      { kw: "upsell coaching wordpress", intent: "informationnelle", angle: "3 upsells logiques post-achat pour augmenter la LTV client coaching", priorite: "🟠 M2" },
      { kw: "page découverte coaching wordpress", intent: "informationnelle", angle: "La page de prise de RDV découverte qui pré-qualifie avant le call", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Automatisation Email Coaching",
    kw_pilier: "automatisation email coaching wordpress",
    intention: "informationnelle",
    satellites: [
      { kw: "onboarding client coaching automatique", intent: "informationnelle", angle: "Onboarding automatique d'un nouveau client coaching — 5h libérées", priorite: "🔴 M1" },
      { kw: "séquence nurturing coach wordpress", intent: "informationnelle", angle: "La séquence nurturing qui transforme un lead froid en client high-ticket", priorite: "🟠 M2" },
      { kw: "relance prospect coaching wordpress", intent: "informationnelle", angle: "Relancer un prospect après un call découverte sans être lourd — automatisation", priorite: "🟠 M2" },
      { kw: "email post programme coaching wordpress", intent: "informationnelle", angle: "La séquence post-programme qui génère des upsells 6 mois après", priorite: "🟡 M3" },
      { kw: "alumni coaching wordpress fidélisation", intent: "informationnelle", angle: "Fidéliser ses alumni coaching : le système qui transforme 1 client en 3", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "LMS WordPress Programme Premium",
    kw_pilier: "lms wordpress programme coaching",
    intention: "informationnelle / comparative",
    satellites: [
      { kw: "lms wordpress coach programme high-ticket", intent: "informationnelle", angle: "Structurer un programme de coaching en ligne sur WordPress — architecture complète", priorite: "🔴 M1" },
      { kw: "alternatives kajabi wordpress lms", intent: "comparative", angle: "Les 3 meilleures alternatives à Kajabi sur WordPress en 2026", priorite: "🔴 M1" },
      { kw: "tutor lms programme coaching", intent: "décisionnelle", angle: "Tutor LMS pour un programme coaching : configuration pas à pas", priorite: "🟠 M2" },
      { kw: "membership wordpress coach", intent: "informationnelle", angle: "Créer un membership coaching sur WordPress — MRR stable pour coach", priorite: "🟠 M2" },
      { kw: "mastermind wordpress plateforme", intent: "informationnelle", angle: "Gérer un mastermind sur WordPress — outils et workflow complet", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Alternatives Kajabi pour Coach",
    kw_pilier: "alternative kajabi wordpress",
    intention: "comparative / décisionnelle",
    satellites: [
      { kw: "kajabi vs wordpress coach 2026", intent: "comparative", angle: "Kajabi vs WordPress pour coach : comparaison honnête sur 8 critères", priorite: "🔴 M1" },
      { kw: "migrer kajabi wordpress", intent: "décisionnelle", angle: "Migrer de Kajabi vers WordPress : guide complet sans perdre ses données", priorite: "🔴 M1" },
      { kw: "systeme io vs wordpress coach", intent: "comparative", angle: "Systeme.io vs WordPress pour coach : avantages et limites de chaque", priorite: "🟠 M2" },
      { kw: "podia teachable alternatives wordpress", intent: "comparative", angle: "Podia, Teachable, WordPress : lequel choisir pour son programme coaching", priorite: "🟠 M2" },
      { kw: "coût kajabi vs wordpress hébergé", intent: "informationnelle", angle: "Calcul réel : Kajabi 150 €/mois vs WordPress 30 €/mois — ce qu'on ne te dit pas", priorite: "🟡 M3" },
    ],
  },
  {
    nom: "Segmenter ses Clients WordPress — Coach",
    kw_pilier: "segmentation client wordpress coaching",
    intention: "informationnelle",
    satellites: [
      { kw: "segmenter liste email coach wordpress", intent: "informationnelle", angle: "Segmenter sa liste coaching en 5 groupes — et ce que ça change sur le CA", priorite: "🟠 M2" },
      { kw: "tag comportemental fluentcrm coach", intent: "informationnelle", angle: "Les 8 tags comportementaux essentiels pour un coach avec FluentCRM", priorite: "🟠 M2" },
      { kw: "lead scoring coach wordpress", intent: "informationnelle", angle: "Lead scoring pour coaches : qualifier automatiquement avant le call découverte", priorite: "🟡 M3" },
      { kw: "lifecycle client coaching wordpress", intent: "informationnelle", angle: "Cartographier le lifecycle client coaching sur WordPress — de la découverte à l'alumni", priorite: "🟡 M3" },
    ],
  },
];

const STRATEGIE_CONTENU = [
  {
    type: "Comparatifs orientés coach",
    description: "Comparatifs qui positionnent WordPress face aux SaaS que les coaches utilisent — avec un angle ROI et contrôle.",
    exemples: [
      "Kajabi vs WordPress pour coach — comparaison honnête sur 8 critères",
      "ActiveCampaign vs FluentCRM pour coach high-ticket",
      "Teachable vs Tutor LMS pour programme premium",
    ],
    angle_differentiant: "Toujours conclure par : 'sur schoolsWP, voici comment on résout ça nativement'. Pas de réponse générique.",
  },
  {
    type: "Architectures type pour coaching",
    description: "Schémas et blueprints WordPress pour les offres coaches classiques. Montrer l'architecture avant de la vendre.",
    exemples: [
      "Blueprint WordPress pour coach individuel (5 pages essentielles)",
      "Architecture LMS pour programme coaching groupe 12 semaines",
      "Schéma tunnel high-ticket WordPress annoté",
    ],
    angle_differentiant: "Publier le schéma réel utilisé en mission — montrer, pas juste expliquer. Ce que les concurrents ne font pas.",
  },
  {
    type: "Études de cas pédagogiques",
    description: "Avant/après anonymisés ou fictifs bien construits. Montrer les chiffres réels quand possible.",
    exemples: [
      "Comment un coach business a multiplié ses leads par 3 en 4 mois avec WordPress",
      "Migration Kajabi → WordPress : résultats à 6 mois (coûts, conversions, autonomie)",
      "Onboarding client automatisé : de 5h à 45 min par nouveau client",
    ],
    angle_differentiant: "Format : situation → problème → solution → résultats chiffrés. Pas de vague 'amélioration'. Des chiffres.",
  },
  {
    type: "Guides CRM pour offre high-ticket",
    description: "Guides pratiques spécifiques à la gestion CRM d'une offre premium — segmentation, nurturing long cycle, LTV.",
    exemples: [
      "Guide complet : FluentCRM pour coach high-ticket (de l'installation à l'automatisation)",
      "Les 5 séquences email indispensables pour un coach avec une offre > 3 000 €",
      "Lead scoring pour coaches : qualifier avant le call découverte",
    ],
    angle_differentiant: "Tout est spécifique au coaching premium. Pas de généralités e-commerce.",
  },
  {
    type: "Structuration funnel WordPress coaching",
    description: "Guides pas à pas pour construire ou optimiser chaque étape du funnel.",
    exemples: [
      "Créer une page de vente coaching qui convertit à 2 %+ — guide étape par étape",
      "Optimiser le checkout d'un programme à 5 000 € — 7 ajustements testés",
      "La page de prise de RDV découverte qui pré-qualifie automatiquement",
    ],
    angle_differentiant: "Inclure des benchmarks réels. 'La moyenne du secteur est X. Voici comment dépasser ça.'",
  },
];

const VISION_12_MOIS = [
  {
    periode: "Mois 1–3",
    label: "Fondations & Visibilité",
    objectif: "Être visible sur la niche coaches premium, avoir une offre claire, générer les premières opportunités.",
    kpis: ["3 articles décisionnels niche coach publiés", "Page offre WordPress Growth System™ Coach en ligne", "1 Audit Coach signé", "CTA niche coach intégrés dans 10 articles schoolsWP"],
    actions: [
      "Publier article pilier 'CRM WordPress pour coach' (brain-lite.bat)",
      "Publier 'Remplacer Kajabi par WordPress — guide complet 2026'",
      "Publier 'Tunnel high-ticket WordPress coach : 3 pages qui convertissent'",
      "Créer la landing page 'Audit Growth System Coach' (800–1 500 €)",
      "Identifier 15 coaches premium sur LinkedIn (CA visible, site WordPress, programme existant)",
      "Publier 1 post LinkedIn : 'Pourquoi votre WordPress vous coûte 600 €/mois de trop'",
    ],
  },
  {
    periode: "Mois 4–6",
    label: "Preuve Sociale & Accélération",
    objectif: "2 missions Architecture livrées, 3 articles supplémentaires, témoignages publiés.",
    kpis: ["2 missions Architecture signées", "3 témoignages collectés avec métriques", "5 articles total publiés niche coach", "Lead magnet niche coach actif"],
    actions: [
      "Réaliser et documenter les 2 premières missions Architecture (études de cas)",
      "Collecter les témoignages (avant/après chiffrés : coûts SaaS économisés, conversion, leads)",
      "Publier les études de cas sur schoolsWP",
      "Lancer le lead magnet : 'Checklist — Les 8 signes que votre WordPress coach perd des revenus'",
      "Automatiser le funnel Audit : formulaire → cal → email devis → relance J+3",
      "Publier 2 comparatifs supplémentaires (Kajabi vs WP, ActiveCampaign vs FluentCRM)",
    ],
  },
  {
    periode: "Mois 7–12",
    label: "Autorité & Scalabilité",
    objectif: "Référence niche coaches WordPress, pricing revu à la hausse, produit digital lancé, MRR > 3 000 €.",
    kpis: ["5 missions Agency signées au total", "MRR Accompagnement ≥ 3 000 €/mois", "Trafic organique articles niche coach : ≥ 1 000 sessions/mois", "Pricing Architecture : ≥ 6 000 €"],
    actions: [
      "Revoir le pricing Architecture à la hausse (6 000–8 000 €) — nouveaux devis seulement",
      "Lancer le produit digital niche coach : 'WordPress Coach System™ — le framework' (97–197 €)",
      "Compléter les 6 clusters SEO (tous les articles 🔴 + 🟠)",
      "Démarrer la stratégie AI Overviews sur les articles les plus lus",
      "Publier 1 blueprint ou guide complet > 3 000 mots par mois",
      "Lancer les Accompagnements Mensuels (1 000–2 000 €/mois) — viser 3 clients",
    ],
  },
];

// Projections financières niche C
const PROJECTIONS = {
  m3: { audits: 1, prix_audit: 1200, archi: 0, mrr: 0 },
  m6: { audits: 2, prix_audit: 1300, archi: 1, prix_archi: 5500, mrr: 0 },
  m9: { audits: 2, prix_audit: 1400, archi: 2, prix_archi: 6000, mrr: 2000 },
  m12: { audits: 2, prix_audit: 1500, archi: 2, prix_archi: 6500, mrr: 4000 },
};
const calcMois = (m) => m.audits * (m.prix_audit || 0) + (m.archi || 0) * (m.prix_archi || 0) + (m.mrr || 0);

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Niche C — Coaches premium : budget fort, besoin business fort, terrain SEO quasi vierge. Ticket moyen Agency : 5 000 à 8 000 €.", "🏆", "purple_background"));
  blocks.push(p(""));
  blocks.push(qot("\"Je structure l'écosystème WordPress de coaches premium pour transformer leur expertise en système d'acquisition et de rétention autonome.\""));
  blocks.push(div());

  // Section 1 — Pourquoi cette niche
  blocks.push(h1("🎯 Pourquoi la Niche Coaches Premium est Stratégique"));
  blocks.push(p(""));
  blocks.push(cal("Un coach premium vend entre 2 000 € et 10 000 €+. Son WordPress doit être à la hauteur de son positionnement. Et il ne l'est presque jamais.", "💡", "yellow_background"));
  blocks.push(p(""));
  blocks.push(h3("Arguments économiques"));
  blocks.push(bul(rt("Budget disponible : ", { bold: true }), rt("CA > 50 000 €/an pour les cibles prioritaires — l'investissement WordPress est marginal")));
  blocks.push(bul(rt("Sensibilité ROI : ", { bold: true }), rt("Un coach comprend la valeur d'un système qui travaille sans lui")));
  blocks.push(bul(rt("Ticket mission élevé : ", { bold: true }), rt("4 000–8 000 € par mission — 2 missions/mois = objectif atteint")));
  blocks.push(bul(rt("LTV forte : ", { bold: true }), rt("Audit → Architecture → Accompagnement mensuel → nouveau tunnel — relation longue durée possible")));
  blocks.push(p(""));
  blocks.push(h3("Arguments de terrain"));
  blocks.push(bul(rt("Stack SaaS coûteux : ", { bold: true }), rt("Kajabi, ActiveCampaign, Teachable — 400 à 600 €/mois qu'on peut réduire à 80 €/mois en WordPress natif")));
  blocks.push(bul(rt("Terrain SEO vierge : ", { bold: true }), rt("Aucun concurrent positionné sur 'tunnel WordPress coach' ou 'remplacer Kajabi WordPress'")));
  blocks.push(bul(rt("Peu de spécialistes : ", { bold: true }), rt("Les freelances WordPress génériques ne parlent pas LTV, onboarding, segmentation, upsell")));
  blocks.push(div());

  // Section 2 — 5 profils ICP
  blocks.push(h1("👥 Les 5 Profils ICP Coaches Premium"));
  blocks.push(p(""));
  ICP_PROFILS.forEach((icp) => {
    blocks.push(tog(
      `${icp.emoji} ${icp.label} — CA typique : ${icp.ca_typique} — Ticket mission : ${icp.ticket_moyen_mission}`,
      [
        p(rt("Offre type : ", { bold: true }), rt(icp.offre_type)),
        p(rt("Situation actuelle : ", { bold: true }), rt(icp.situation)),
        p(""),
        p(rt("Pain points :", { bold: true })),
        ...icp.pain_points.map((pp) => bul(rt("✗ ", { color: "red" }), rt(pp))),
        p(""),
        p(rt("Ce qu'il cherche vraiment : ", { bold: true }), rt(icp.gain_cible, { italic: true })),
        p(rt("Signal de qualification : ", { bold: true }), rt(icp.signal_prospect, { italic: true })),
      ]
    ));
  });

  // Ticket moyen calculé
  const ticketsMoyens = ICP_PROFILS.map((icp) => {
    const parts = icp.ticket_moyen_mission.replace(/[^0-9–-]/g, "").split(/[–-]/);
    return (parseInt(parts[0]) + parseInt(parts[1])) / 2;
  });
  const ticketMoyen = Math.round(ticketsMoyens.reduce((a, b) => a + b, 0) / ticketsMoyens.length);
  blocks.push(p(""));
  blocks.push(cal(`Ticket moyen pondéré sur les 5 profils : ${ticketMoyen.toLocaleString("fr-FR")} €. C'est la niche au ticket le plus élevé des 3 niches cibles.`, "💰", "green_background"));
  blocks.push(div());

  // Section 3 — Problèmes communs
  blocks.push(h1("🧠 Les 6 Problèmes Communs des Coaches Premium"));
  blocks.push(p(""));
  PROBLEMES_COMMUNS.forEach((prob) => {
    blocks.push(tog(`${prob.emoji} ${prob.probleme}`, [
      p(prob.description),
      p(rt("Coût estimé : ", { bold: true }), rt(prob.cout, { italic: true })),
      p(rt("Solution : ", { bold: true }), rt(prob.solution)),
    ]));
  });
  blocks.push(p(""));
  blocks.push(cal("Formule synthétique : tu remets de la structure, de la cohérence et de la performance là où il y a du chaos, des outils éparpillés et des conversions perdues.", "🔑", "orange_background"));
  blocks.push(div());

  // Section 4 — Offre signature
  blocks.push(h1("🏗️ Offre Signature — WordPress Growth System™ pour Coaches Premium"));
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
  blocks.push(h1("💰 Pricing Niche Coaches Premium"));
  blocks.push(p("Le ticket élevé de cette niche justifie des prix plus hauts que les niches A et B. Un coach à 100k€/an ne regarde pas un devis à 5 000 € de la même façon qu'un freelance."));
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

  blocks.push(h3("📊 Projections niche C (coaches premium)"));
  blocks.push(tog("Voir les projections par étape", [
    p(rt("M3 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m3).toLocaleString("fr-FR")} € (${PROJECTIONS.m3.audits} audit)`)),
    p(rt("M6 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m6).toLocaleString("fr-FR")} € (audits + 1 architecture)`)),
    p(rt("M9 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m9).toLocaleString("fr-FR")} € (audits + architectures + ${PROJECTIONS.m9.mrr.toLocaleString("fr-FR")} € MRR)`)),
    p(rt("M12 : ", { bold: true }), rt(`${calcMois(PROJECTIONS.m12).toLocaleString("fr-FR")} € (${PROJECTIONS.m12.mrr.toLocaleString("fr-FR")} € MRR inclus)`)),
    p(""),
    cal("Niche C = tickets les plus élevés. 2 missions Architecture/mois suffisent pour atteindre 12 000 € en phase stable.", "💎", "purple_background"),
  ]));
  blocks.push(div());

  // Section 6 — Clusters SEO
  blocks.push(h1("🔍 Stratégie SEO — 6 Clusters Niche Coaches Premium"));
  const totalSat = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  blocks.push(cal(`Terrain quasi vierge — aucun concurrent spécialisé. ${CLUSTERS_SEO.length} clusters, ${totalSat} articles identifiés. Fenêtre à saisir maintenant.`, "🎯", "green_background"));
  blocks.push(p(""));

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

  blocks.push(cal(`🔴 = M1 (production immédiate) — 🟠 = M2 — 🟡 = M3+`, "📊", "blue_background"));
  blocks.push(div());

  // Section 7 — Stratégie contenu
  blocks.push(h1("📝 Stratégie Contenu Différenciante"));
  blocks.push(p("5 types de contenus à publier sur schoolsWP pour dominer la niche coaches premium."));
  blocks.push(p(""));
  STRATEGIE_CONTENU.forEach((type, i) => {
    blocks.push(tog(`${i + 1}. ${type.type}`, [
      p(type.description),
      p(rt("Exemples d'articles : ", { bold: true })),
      ...type.exemples.map((ex) => bul(rt(`"${ex}"`))  ),
      p(rt("Angle différenciant : ", { bold: true }), rt(type.angle_differentiant, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 8 — Vision 12 mois
  blocks.push(h1("🗓️ Vision 12 Mois — Domination Niche Coaches"));
  blocks.push(p(""));
  VISION_12_MOIS.forEach((phase) => {
    blocks.push(h2(`${phase.periode} — ${phase.label}`));
    blocks.push(p(rt("Objectif : ", { bold: true }), rt(phase.objectif)));
    blocks.push(p(""));

    blocks.push(h3("KPIs cibles"));
    phase.kpis.forEach((kpi) => blocks.push(bul(kpi)));
    blocks.push(p(""));

    blocks.push(tog(`✅ Actions (${phase.actions.length})`,
      phase.actions.map((a) => tod(a))
    ));
    blocks.push(p(""));
  });
  blocks.push(div());

  // Footer
  blocks.push(cal("Niche C en synthèse : ticket le plus élevé des 3 niches, terrain SEO vierge, audience schoolsWP naturellement présente. 2 missions Architecture/mois = 12 000 € de CA. Sans MRR.", "🏁", "purple_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Niche Coaches Premium — WordPress Growth System™'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  const totalSatellites = CLUSTERS_SEO.reduce((a, c) => a + c.satellites.length, 0);
  const totalActions = VISION_12_MOIS.reduce((a, p) => a + p.actions.length, 0);

  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🏆" },
    properties: {
      title: { title: [{ text: { content: "🏆 Niche Coaches Premium — WordPress Growth System™" } }] },
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
  console.log(`   • ${ICP_PROFILS.length} profils ICP avec CA typique, pain points et ticket mission`);
  console.log(`   • ${PROBLEMES_COMMUNS.length} problèmes communs avec coût chiffré + solution`);
  console.log(`   • ${OFFRE_SIGNATURE.composantes.length} composantes + ${OFFRE_SIGNATURE.deliverables.length} livrables`);
  console.log(`   • ${PRICING_NICHE.length} niveaux de prix avec projections M3→M12`);
  console.log(`   • ${CLUSTERS_SEO.length} clusters SEO — ${totalSatellites} articles identifiés`);
  console.log(`   • ${STRATEGIE_CONTENU.length} types de contenus différenciants`);
  console.log(`   • Vision 12 mois — ${totalActions} actions documentées`);
  console.log(`   • Projection CA niche C à M12 : ${m12.toLocaleString("fr-FR")} €/mois`);
  console.log(`   • Ticket moyen ICP : ~6 100 €`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});

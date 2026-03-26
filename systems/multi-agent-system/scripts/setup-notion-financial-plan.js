#!/usr/bin/env node
/**
 * setup-notion-financial-plan.js — Plan financier prévisionnel 24 mois
 *
 * Crée dans Notion la page :
 *   "📊 Plan Financier 24 mois — SASU WordPress"
 *
 * Contenu :
 *   Hypothèses de base
 *   Scénario prudent — Année 1 avec projection mensuelle M1-M12
 *   Scénario ambitieux — Année 2 avec projection mensuelle M13-M24
 *   Structure de charges (fixes vs variables)
 *   Point mort (break-even)
 *   Structure de rémunération intelligente
 *   KPI à surveiller
 *   Lecture stratégique
 *   Tracker mensuel (à remplir en temps réel)
 *
 * Variables :
 *   NOTION_API_KEY         — obligatoire
 *   NOTION_PARENT_PAGE_ID  — page parente (obligatoire)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   node scripts/setup-notion-financial-plan.js
 *
 * Pré-requis : Node 18+
 */

const API_KEY   = process.env.NOTION_API_KEY;
const PARENT_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || !PARENT_ID) {
  console.error('❌  Variables manquantes : NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

// ─── API ──────────────────────────────────────────────────────────────────────

async function notion(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1/${endpoint}`, {
    method,
    headers: {
      Authorization:    `Bearer ${API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type':   'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`${method} ${endpoint} → ${resp.status}: ${err.message || JSON.stringify(err)}`);
  }
  return resp.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ─── Blocks ───────────────────────────────────────────────────────────────────

const rt  = (txt, opts = {}) => ({ type: 'text', text: { content: txt }, annotations: opts });
const rtb = (txt) => rt(txt, { bold: true });

const h1 = (txt) => ({ object: 'block', type: 'heading_1', heading_1: { rich_text: [rt(txt)] } });
const h2 = (txt) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: [rt(txt)] } });
const h3 = (txt) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: [rt(txt)] } });

const p   = (txt = '') => ({ object: 'block', type: 'paragraph',           paragraph:           { rich_text: txt ? [rt(txt)] : [] } });
const bul = (txt)      => ({ object: 'block', type: 'bulleted_list_item',  bulleted_list_item:  { rich_text: [rt(txt)] } });
const bulb = (txt)     => ({ object: 'block', type: 'bulleted_list_item',  bulleted_list_item:  { rich_text: [rtb(txt)] } });
const num = (txt)      => ({ object: 'block', type: 'numbered_list_item',  numbered_list_item:  { rich_text: [rt(txt)] } });

const tod = (txt, checked = false) => ({
  object: 'block', type: 'to_do',
  to_do: { rich_text: [rt(txt)], checked },
});

const div = () => ({ object: 'block', type: 'divider', divider: {} });

const cal = (emoji, txt, color = 'gray_background') => ({
  object: 'block', type: 'callout',
  callout: { icon: { type: 'emoji', emoji }, rich_text: [rt(txt)], color },
});

const qot = (txt) => ({
  object: 'block', type: 'quote',
  quote: { rich_text: [rt(txt)] },
});

const tog = (title, children = []) => ({
  object: 'block', type: 'toggle',
  toggle: { rich_text: [rtb(title)], children },
});

// ─── Données financières ──────────────────────────────────────────────────────

// Projection mensuelle — scénario prudent (Année 1)
const MOIS_AN1 = [
  { m: 'M1', phase: '🔧 Création SASU',      clients: 0, ca_presta: 0,    ca_aff: 0,   total: 0,    charges: 1500, solde: -1500 },
  { m: 'M2', phase: '🔎 Prospection active', clients: 0, ca_presta: 0,    ca_aff: 200, total: 200,  charges: 1500, solde: -1300 },
  { m: 'M3', phase: '🚀 1er client',         clients: 1, ca_presta: 3000, ca_aff: 300, total: 3300, charges: 1700, solde: 1600  },
  { m: 'M4', phase: '📈 Régime 2 clients',   clients: 2, ca_presta: 6000, ca_aff: 500, total: 6500, charges: 1800, solde: 4700  },
  { m: 'M5', phase: '📈 Consolidation',      clients: 2, ca_presta: 6000, ca_aff: 500, total: 6500, charges: 1800, solde: 4700  },
  { m: 'M6', phase: '📈 Consolidation',      clients: 2, ca_presta: 6000, ca_aff: 600, total: 6600, charges: 1800, solde: 4800  },
  { m: 'M7', phase: '💰 1er cas d\'étude',   clients: 2, ca_presta: 6000, ca_aff: 600, total: 6600, charges: 1800, solde: 4800  },
  { m: 'M8', phase: '📈 Stabilité',          clients: 2, ca_presta: 6000, ca_aff: 700, total: 6700, charges: 1800, solde: 4900  },
  { m: 'M9', phase: '📈 Stabilité',          clients: 2, ca_presta: 6000, ca_aff: 700, total: 6700, charges: 1800, solde: 4900  },
  { m: 'M10', phase: '🔄 Récurrences',       clients: 2, ca_presta: 6000, ca_aff: 800, total: 6800, charges: 1800, solde: 5000  },
  { m: 'M11', phase: '🔄 Récurrences',       clients: 2, ca_presta: 6000, ca_aff: 800, total: 6800, charges: 1800, solde: 5000  },
  { m: 'M12', phase: '📊 Bilan',             clients: 2, ca_presta: 6000, ca_aff: 900, total: 6900, charges: 1900, solde: 5000  },
];

const CA_AN1_PRESTA = MOIS_AN1.reduce((s, m) => s + m.ca_presta, 0);  // 57 000
const CA_AN1_AFF    = MOIS_AN1.reduce((s, m) => s + m.ca_aff, 0);     // ~6 600
const CA_AN1_TOTAL  = MOIS_AN1.reduce((s, m) => s + m.total, 0);
const CHARGES_AN1   = MOIS_AN1.reduce((s, m) => s + m.charges, 0);

// Projection mensuelle — scénario ambitieux (Année 2, M13-M24)
const MOIS_AN2 = [
  { m: 'M13', phase: '🚀 Accélération',      clients: 2, ca_presta: 7000,  ca_aff: 1000, total: 8000,  charges: 2200, solde: 5800  },
  { m: 'M14', phase: '🚀 Accélération',      clients: 3, ca_presta: 9000,  ca_aff: 1000, total: 10000, charges: 2500, solde: 7500  },
  { m: 'M15', phase: '📈 Régime 3 clients',  clients: 3, ca_presta: 10500, ca_aff: 1200, total: 11700, charges: 2600, solde: 9100  },
  { m: 'M16', phase: '📈 Régime 3 clients',  clients: 3, ca_presta: 10500, ca_aff: 1200, total: 11700, charges: 2600, solde: 9100  },
  { m: 'M17', phase: '💎 1er PREMIUM',       clients: 3, ca_presta: 10500, ca_aff: 1300, total: 11800, charges: 2700, solde: 9100  },
  { m: 'M18', phase: '📊 Bilan S1 An2',      clients: 3, ca_presta: 10500, ca_aff: 1300, total: 11800, charges: 2700, solde: 9100  },
  { m: 'M19', phase: '🔄 MRR solide',        clients: 3, ca_presta: 10500, ca_aff: 1400, total: 11900, charges: 2800, solde: 9100  },
  { m: 'M20', phase: '🔄 MRR solide',        clients: 3, ca_presta: 10500, ca_aff: 1400, total: 11900, charges: 2800, solde: 9100  },
  { m: 'M21', phase: '📈 Optimisation',      clients: 3, ca_presta: 10500, ca_aff: 1500, total: 12000, charges: 2800, solde: 9200  },
  { m: 'M22', phase: '📈 Optimisation',      clients: 3, ca_presta: 10500, ca_aff: 1500, total: 12000, charges: 2800, solde: 9200  },
  { m: 'M23', phase: '💰 Dividendes envisageables', clients: 3, ca_presta: 10500, ca_aff: 1600, total: 12100, charges: 2900, solde: 9200 },
  { m: 'M24', phase: '📊 Bilan An2',         clients: 3, ca_presta: 10500, ca_aff: 1600, total: 12100, charges: 2900, solde: 9200  },
];

const CA_AN2_PRESTA = MOIS_AN2.reduce((s, m) => s + m.ca_presta, 0);
const CA_AN2_AFF    = MOIS_AN2.reduce((s, m) => s + m.ca_aff, 0);
const CA_AN2_TOTAL  = MOIS_AN2.reduce((s, m) => s + m.total, 0);
const CHARGES_AN2   = MOIS_AN2.reduce((s, m) => s + m.charges, 0);

const fmt = (n) => n.toLocaleString('fr-FR') + ' €';

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('📊', 'Plan financier réaliste — orienté cash et sérénité, pas croissance à tout prix.', 'blue_background'),
    p(),
    qot('Tu n\'as pas besoin de 10 clients par mois. Tu as besoin de 2 à 3 clients premium réguliers, d\'un SEO décisionnel fort et d\'un système propre.'),
    p(),
  );

  // ── Vue consolidée ────────────────────────────────────────────────────────
  add(
    h2('🔭 Vue 24 mois — Synthèse'),
    p(),
    bul(`Année 1 (scénario prudent)  →  CA total estimé : ${fmt(CA_AN1_TOTAL)}`),
    bul(`Année 2 (scénario ambitieux)  →  CA total estimé : ${fmt(CA_AN2_TOTAL)}`),
    bul('Charges fixes mensuelles : ~1 500 – 2 900 € (selon rémunération)'),
    bul('Point mort : 1 client par mois suffit à couvrir les charges fixes'),
    bul('MRR Maintenance cible M12 : 1 500 €  ·  M24 : 3 000 €+'),
    p(),
    div(),
  );

  // ── 1. Hypothèses ─────────────────────────────────────────────────────────
  add(
    h1('1️⃣ Hypothèses de base'),
    p(),
    h3('Offre principale — WordPress Learning System™'),
    p(),
    bul('Prix d\'entrée CORE : 3 000 – 6 000 €  (prix moyen retenu : 3 500 €)'),
    bul('Prix PREMIUM : 6 000 – 10 000 €  (rare en An1, viser 1 projet en An2)'),
    bul('Durée projet : 3 à 6 semaines par client'),
    bul('Capacité max solo : 2 à 3 projets simultanément (jamais plus)'),
    p(),
    h3('Revenus secondaires (schoolsWP)'),
    p(),
    bul('Affiliation plugins : montée progressive M1 → M24 (0 → 1 600 €/mois)'),
    bul('Maintenance clients : 300 €/mois par client récurrent'),
    bul('Formations digitales : non incluses dans ce prévisionnel (upside)'),
    p(),
    h3('Hypothèses de capacité'),
    p(),
    bul('Ramp-up réaliste : 3 mois avant le 1er client payant (prospection + setup SASU)'),
    bul('M4-M12 : 2 clients/mois en régime de croisière'),
    bul('M13-M14 : transition vers 3 clients/mois (légère hausse prix)'),
    bul('M15-M24 : 3 clients à 3 500 € + affiliation 1 200-1 600 €/mois'),
    p(),
    cal('⚠️', 'Ces chiffres excluent les charges sociales sur la rémunération du président — voir Section 5 pour l\'impact.', 'yellow_background'),
    p(),
    div(),
  );

  // ── 2. Scénario prudent — Année 1 ────────────────────────────────────────
  add(
    h1('2️⃣ Scénario Prudent — Année 1'),
    p(),
    cal('💰', `CA total estimé An1 : ${fmt(CA_AN1_TOTAL)}  (prestations ${fmt(CA_AN1_PRESTA)} + affiliation ${fmt(CA_AN1_AFF)})`, 'green_background'),
    p(),
  );

  // Tableau mensuel An1
  add(
    tog('📅 Projection mensuelle M1 → M12 (détail)', [
      ...MOIS_AN1.map((m) => p(
        `${m.m}  [${m.phase}]` +
        `  Clients: ${m.clients}` +
        `  CA: ${fmt(m.total).padStart(8)}` +
        `  (presta ${fmt(m.ca_presta)} + aff ${fmt(m.ca_aff)})` +
        `  Charges: ${fmt(m.charges)}` +
        `  Solde: ${m.solde >= 0 ? '+' : ''}${fmt(m.solde)}`
      )),
      p(),
      p(`  Total  →  CA: ${fmt(CA_AN1_TOTAL)}  ·  Charges: ${fmt(CHARGES_AN1)}  ·  Résultat brut: ${fmt(CA_AN1_TOTAL - CHARGES_AN1)}`),
    ]),
    p(),
  );

  add(
    h2('Résultat Année 1'),
    p(),
    bul(`CA Prestations : ${fmt(CA_AN1_PRESTA)}`),
    bul(`CA Affiliation : ${fmt(CA_AN1_AFF)}`),
    bul(`CA Total HT : ${fmt(CA_AN1_TOTAL)}`),
    bul(`Charges opérationnelles (hors rémunération) : ${fmt(CHARGES_AN1)}`),
    p(),
    bul(`Résultat avant rémunération et IS : ~${fmt(CA_AN1_TOTAL - CHARGES_AN1)}`),
    bul('IS 15% estimé (sur bénéfice après rémunération) : ~4 000 – 6 000 €'),
    bul('Résultat net disponible : ~25 000 – 35 000 €'),
    p(),
    cal('📌', 'Année 1 = structuration et validation. Pas d\'extraction maximale. Capitaliser la trésorerie SASU.', 'blue_background'),
    p(),
    div(),
  );

  // ── 3. Scénario ambitieux — Année 2 ──────────────────────────────────────
  add(
    h1('3️⃣ Scénario Ambitieux — Année 2'),
    p(),
    cal('💰', `CA total estimé An2 : ${fmt(CA_AN2_TOTAL)}  (prestations ${fmt(CA_AN2_PRESTA)} + affiliation ${fmt(CA_AN2_AFF)})`, 'green_background'),
    p(),
  );

  add(
    tog('📅 Projection mensuelle M13 → M24 (détail)', [
      ...MOIS_AN2.map((m) => p(
        `${m.m}  [${m.phase}]` +
        `  Clients: ${m.clients}` +
        `  CA: ${fmt(m.total).padStart(9)}` +
        `  (presta ${fmt(m.ca_presta)} + aff ${fmt(m.ca_aff)})` +
        `  Charges: ${fmt(m.charges)}` +
        `  Solde: +${fmt(m.solde)}`
      )),
      p(),
      p(`  Total  →  CA: ${fmt(CA_AN2_TOTAL)}  ·  Charges: ${fmt(CHARGES_AN2)}  ·  Résultat brut: ${fmt(CA_AN2_TOTAL - CHARGES_AN2)}`),
    ]),
    p(),
  );

  add(
    h2('Résultat Année 2'),
    p(),
    bul(`CA Prestations : ${fmt(CA_AN2_PRESTA)}`),
    bul(`CA Affiliation : ${fmt(CA_AN2_AFF)}`),
    bul(`CA Total HT : ${fmt(CA_AN2_TOTAL)}`),
    bul(`Charges opérationnelles (hors rémunération) : ${fmt(CHARGES_AN2)}`),
    p(),
    bul(`Résultat avant rémunération et IS : ~${fmt(CA_AN2_TOTAL - CHARGES_AN2)}`),
    bul('IS 15% estimé : ~8 000 – 12 000 € (sur bénéfice résiduel)'),
    bul('Résultat net disponible (avant dividendes) : ~60 000 – 75 000 €'),
    p(),
    cal('📌', 'Année 2 = premiers dividendes envisageables. Décision salaire vs dividendes avec l\'EC en M18.', 'blue_background'),
    p(),
    div(),
  );

  // ── 4. Structure de charges ────────────────────────────────────────────────
  add(
    h1('4️⃣ Structure de charges'),
    p(),
    h2('Charges fixes mensuelles (hors rémunération)'),
    p(),
    bul('Expert-comptable : 80 – 120 €/mois (1 000 – 1 500 €/an)'),
    bul('RC Pro : 35 – 50 €/mois (420 – 600 €/an)'),
    bul('Compte bancaire pro : 10 – 20 €/mois'),
    bul('Hébergement + domaines : 50 – 80 €/mois'),
    bul('Outils SEO (Ahrefs ou DataForSEO) : 80 – 150 €/mois'),
    bul('Outils IA (OpenAI API, Claude) : 30 – 80 €/mois'),
    bul('n8n + SaaS automatisation : 20 – 50 €/mois'),
    bul('Notion + outils divers : 20 – 30 €/mois'),
    bul('Logiciel facturation : 0 – 20 €/mois'),
    p(),
    bulb('TOTAL CHARGES FIXES (hors rémunération) : ~400 – 600 €/mois'),
    p(),
    h2('Charges variables'),
    p(),
    bul('Plugins & licences ponctuels : 500 – 1 000 €/an'),
    bul('Matériel informatique (amortissement) : 300 – 600 €/an'),
    bul('Formations & certifications : 500 – 1 500 €/an'),
    bul('Déplacements clients : variable'),
    p(),
    h2('Charges sociales — À NE PAS OUBLIER'),
    p(),
    cal('⚠️', 'Les charges sociales sur salaire président SASU sont ~80% du brut (régime général). Elles s\'ajoutent aux charges opérationnelles.', 'red_background'),
    p(),
    bul('Salaire brut 1 500 €  →  ~1 200 € charges  →  ~300 € net  (non optimisé)'),
    bul('Salaire brut 2 500 €  →  ~2 000 € charges  →  ~1 900 € net'),
    bul('Salaire brut 3 500 €  →  ~2 800 € charges  →  ~2 600 € net'),
    p(),
    cal('💡', 'Stratégie recommandée An1 : salaire 0 ou minimum (réduire les charges sociales). Compenser avec les économies accumulées.', 'green_background'),
    p(),
    div(),
  );

  // ── 5. Point mort ─────────────────────────────────────────────────────────
  add(
    h1('5️⃣ Point Mort — Break-even'),
    p(),
    h2('Calcul simple'),
    p(),
    bul('Charges fixes opérationnelles mensuelles : ~500 €'),
    bul('Charges sociales (si salaire 2 000 € brut) : ~1 600 €'),
    bul('Provisions IS et TVA : ~500 – 800 €'),
    bul('TOTAL charges mensuelles à couvrir : ~2 200 – 2 900 €'),
    p(),
    cal('✅', 'Avec panier moyen 3 500 € → 1 client par mois couvre largement le point mort. Ton seuil critique est faible.', 'green_background'),
    p(),
    h2('Interprétation stratégique'),
    p(),
    bul('1 client/mois = seuil de survie (charges couvertes, pas de salaire)'),
    bul('1,5 client/mois = point d\'équilibre avec salaire minimal'),
    bul('2 clients/mois = confort + capitalisation trésorerie'),
    bul('3 clients/mois = accélération + dividendes possibles en fin d\'année'),
    p(),
    cal('💡', 'Tu n\'es qu\'à 1 client par mois du point mort. C\'est rassurant et réaliste dès le 3e mois.', 'blue_background'),
    p(),
  );

  add(
    h2('MRR Maintenance — L\'accélérateur caché'),
    p(),
    bul('Chaque client CORE = potentiel 300 €/mois de Maintenance récurrente'),
    bul('Chaque client PREMIUM = potentiel 600 €/mois'),
    p(),
    bul('5 clients Maintenance Starter  →  1 500 €/mois MRR'),
    bul('5 clients Maintenance Starter + 2 Maintenance Expert  →  2 700 €/mois MRR'),
    p(),
    cal('📈', 'MRR 1 500 €/mois = point mort entièrement couvert sans nouveau projet ce mois-là. Objectif M12.', 'green_background'),
    p(),
    div(),
  );

  // ── 6. Rémunération ────────────────────────────────────────────────────────
  add(
    h1('6️⃣ Structure de rémunération intelligente'),
    p(),
  );

  add(
    tog('Année 1 — Mode capitalisation', [
      bul('Salaire président : 0 € ou salaire symbolique (économiser les charges sociales)'),
      bul('Vivre sur les économies constituées avant la sortie du salariat'),
      bul('Laisser la trésorerie SASU grossir (objectif : 3 mois de charges à fin M12)'),
      bul('Provisions : 40% de chaque encaissement HT → sous-compte fiscal'),
      p(),
      cal('💡', 'Si besoin perso urgent : virement "avance en compte courant d\'associé" (remboursé plus tard, pas de charges sociales immédiates). Valider avec l\'EC.', 'blue_background'),
    ]),
    p(),
    tog('Année 2 — Mode optimisation', [
      bul('Salaire cible : 2 000 – 3 000 € net/mois (selon CA stable)'),
      bul('Dividendes : bénéfice après IS × 70% → flat tax 30% (PFU)'),
      bul('Arbitrage avec l\'EC à M18 : quand les dividendes deviennent plus efficaces'),
      bul('Épargne salariale (intéressement SASU depuis 2019) si pertinent'),
      p(),
      cal('💡', 'À CA 10 000 €/mois : dividendes deviennent clairement plus efficaces que d\'augmenter le salaire.', 'green_background'),
    ]),
    p(),
    div(),
  );

  // ── 7. KPI à surveiller ────────────────────────────────────────────────────
  add(
    h1('7️⃣ Indicateurs clés à surveiller chaque mois'),
    p(),
    bul('Cash disponible compte pro (pas de surprise URSSAF)'),
    bul('Marge nette par projet (CA projet – temps réel × coût horaire implicite)'),
    bul('Temps réel par projet (objectif < 40h/projet CORE)'),
    bul('Taux de closing (devis envoyés vs signés — objectif > 25%)'),
    bul('Délai de paiement moyen (objectif < 30j, alerte à 45j)'),
    bul('MRR Maintenance (croissance mensuelle — objectif +300 €/mois)'),
    bul('CA Affiliation schoolsWP (croissance organique)'),
    bul('Coût d\'acquisition client (objectif : quasi nul via SEO)'),
    p(),
    cal('💡', 'Coût d\'acquisition via SEO = principal avantage concurrentiel. Un article bien positionné travaille 24h/24 sans coût marginal.', 'green_background'),
    p(),
    div(),
  );

  // ── 8. Moments de décision ─────────────────────────────────────────────────
  add(
    h1('8️⃣ Moments de décision stratégiques'),
    p(),
  );

  const decisions = [
    ['M3 — 1er client signé', 'Valider le pricing. Ajuster si > 50% de taux de closing (sous-facturation).'],
    ['M6 — 2 clients/mois stable', 'Formaliser l\'onboarding. Créer le premier cas d\'étude. Commencer le contenu formateurs WordPress.'],
    ['M9 — 3 mois stables', 'Décision : augmenter les prix (4 000 €+) ou volume ? Salaire modeste activable.'],
    ['M12 — 1er bilan', 'Revue complète avec l\'EC. Optimisation rémunération. Vérifier MRR Maintenance.'],
    ['M18 — Dividendes possibles', 'Calcul arbitrage salaire vs dividendes. Décision outsourcing partiel ou rester solo ?'],
    ['M24 — Vision 3 ans', 'Option holding si bénéfice > 60 000 €. Décision : agrandir l\'offre ou rester ultra-niche ?'],
  ];

  decisions.forEach(([moment, action]) => {
    add(tog(moment, [p(action)]));
    add(p());
  });

  add(div());

  // ── 9. Lecture stratégique ─────────────────────────────────────────────────
  add(
    h1('9️⃣ Lecture stratégique — Froide et honnête'),
    p(),
    h2('Ce dont tu n\'as PAS besoin'),
    p(),
    bul('❌  10 clients par mois — 2 à 3 bien choisis suffisent'),
    bul('❌  Une grosse équipe — rester solo jusqu\'à MRR > 5 000 €'),
    bul('❌  Un volume massif de contenu — 20 articles ultra-ciblés beats 200 articles génériques'),
    bul('❌  Une levée de fonds — aucun besoin de capital externe'),
    bul('❌  De la publicité payante — SEO décisionnel suffit à remplir le pipeline'),
    p(),
    h2('Ce dont tu AS besoin'),
    p(),
    bulb('2 à 3 clients premium réguliers  →  3 500 € × 3 = 10 500 €/mois'),
    bulb('SEO décisionnel fort  →  leads entrants qualifiés sans coût d\'acquisition'),
    bulb('Système propre  →  onboarding, contrats, livrables, maintenance'),
    bulb('MRR Maintenance  →  revenu prévisible qui couvre le point mort'),
    p(),
    cal('🎯', 'La combinaison schoolsWP (levier SEO/LLM) + SASU (structure) + Formateurs WordPress (niche) = business solide, scalable et aligné avec ce que tu construis déjà.', 'green_background'),
    p(),
    div(),
  );

  // ── Tracker mensuel ────────────────────────────────────────────────────────
  add(
    h1('📋 Tracker mensuel — À remplir en temps réel'),
    p('Dupliquer cette section chaque mois. Comparer avec le prévisionnel.'),
    p(),
  );

  // Générer les 12 premiers mois comme toggles
  ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'].forEach((m, i) => {
    const prev = MOIS_AN1[i];
    add(
      tog(`${m} — Réalisé vs Prévisionnel`, [
        p('CA Réel Prestations :  _____ €  (prévu : ' + fmt(prev.ca_presta) + ')'),
        p('CA Réel Affiliation :  _____ €  (prévu : ' + fmt(prev.ca_aff) + ')'),
        p('CA Total Réel :        _____ €  (prévu : ' + fmt(prev.total) + ')'),
        p('Charges Réelles :      _____ €  (prévu : ' + fmt(prev.charges) + ')'),
        p('Trésorerie Compte Pro :_____ €'),
        p('MRR Maintenance :      _____ €/mois'),
        p('Nombre de devis envoyés :  _____  ·  Signés :  _____  ·  Taux closing : ____%'),
        p(''),
        p('Notes / Écarts :'),
        p('_______________________'),
        tod('Factures émises et enregistrées'),
        tod('Provisions fiscales virées (40%)'),
        tod('Export comptable envoyé à l\'EC'),
        tod('Revue trésorerie réalisée'),
      ]),
      p(),
    );
  });

  add(
    cal('💡', 'Tracker An2 (M13-M24) : dupliquer ce tracker avec les prévisions Scénario Ambitieux comme référence.', 'gray_background'),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Plan Financier Prévisionnel 24 mois\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs — ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '📊' },
    properties: {
      title: { title: [{ text: { content: '📊 Plan Financier 24 mois — SASU WordPress' } }] },
    },
    children: batches[0],
  });

  console.log(`        ✅  Batch 1 créé (${batches[0].length} blocs)`);

  for (let i = 1; i < batches.length; i++) {
    await sleep(600);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batches[i] });
    console.log(`        ✅  Batch ${i + 1} ajouté (${batches[i].length} blocs)`);
  }

  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Plan financier 24 mois créé !\n');
  console.log('  📊  Page : "📊 Plan Financier 24 mois — SASU WordPress"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Chiffres clés du prévisionnel :');
  console.log(`    Année 1 CA total  : ${fmt(CA_AN1_TOTAL)}`);
  console.log(`    Année 1 Presta    : ${fmt(CA_AN1_PRESTA)}`);
  console.log(`    Année 1 Affiliation : ${fmt(CA_AN1_AFF)}`);
  console.log('');
  console.log(`    Année 2 CA total  : ${fmt(CA_AN2_TOTAL)}`);
  console.log(`    Année 2 Presta    : ${fmt(CA_AN2_PRESTA)}`);
  console.log(`    Année 2 Affiliation : ${fmt(CA_AN2_AFF)}`);
  console.log('');
  console.log('  Contenu de la page :');
  console.log('    📅  Projection mensuelle M1-M12 (détail)');
  console.log('    📅  Projection mensuelle M13-M24 (détail)');
  console.log('    📊  Structure charges fixes vs variables');
  console.log('    ⚖️   Point mort — 1 client/mois suffit');
  console.log('    💰  Rémunération intelligente An1 vs An2');
  console.log('    🎯  6 moments de décision stratégiques');
  console.log('    📋  Tracker mensuel M1-M12 (à remplir en temps réel)');
  console.log('');
  console.log('  Point mort calculé :');
  console.log('    Charges fixes : ~2 200 – 2 900 €/mois');
  console.log('    1 client à 3 500 € → point mort largement couvert');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});

#!/usr/bin/env node
/**
 * setup-notion-remuneration-sasu.js — Simulation rémunération optimisée SASU
 *
 * Crée dans Notion la page :
 *   "💰 Simulation Rémunération SASU — schoolsWP + Agence"
 *
 * Contenu :
 *   Rappel fondamental SASU à l'IS
 *   3 scénarios complets (CA 80k) avec calculs détaillés
 *   Tableau comparatif des 3 scénarios
 *   Impact protection sociale par niveau de salaire
 *   PER — Plan Épargne Retraite (défiscalisation additionnelle)
 *   Simulation Année 2 (CA 120k)
 *   Logique stratégique An1 → An2 → An3
 *   Décisions mensuelles concrètes
 *
 * Variables :
 *   NOTION_API_KEY         — obligatoire
 *   NOTION_PARENT_PAGE_ID  — page parente (obligatoire)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   node scripts/setup-notion-remuneration-sasu.js
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

const h1 = (t) => ({ object: 'block', type: 'heading_1', heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: [rt(t)] } });

const p   = (t = '') => ({ object: 'block', type: 'paragraph',          paragraph:         { rich_text: t ? [rt(t)] : [] } });
const bul = (t)      => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rt(t)] } });
const bulb = (t)     => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rtb(t)] } });
const num = (t)      => ({ object: 'block', type: 'numbered_list_item', numbered_list_item: { rich_text: [rt(t)] } });

const div = () => ({ object: 'block', type: 'divider', divider: {} });

const cal = (emoji, t, color = 'gray_background') => ({
  object: 'block', type: 'callout',
  callout: { icon: { type: 'emoji', emoji }, rich_text: [rt(t)], color },
});

const qot = (t) => ({ object: 'block', type: 'quote', quote: { rich_text: [rt(t)] } });

const tog = (title, children = []) => ({
  object: 'block', type: 'toggle',
  toggle: { rich_text: [rtb(title)], children },
});

// ─── Calculs financiers ───────────────────────────────────────────────────────

const fmt  = (n, suf = ' €') => Math.round(n).toLocaleString('fr-FR') + suf;
const pct  = (n) => Math.round(n) + ' %';

// Paramètres communs An1
const CA_AN1        = 80_000;
const CHARGES_OPE   = 14_000;
const RESULTAT_BRUT = CA_AN1 - CHARGES_OPE;  // 66 000

// Taux charges sociales assimilé salarié SASU (approximations 2025)
const TAUX_PAT   = 0.45;   // charges patronales ~45% du brut
const TAUX_SAL   = 0.23;   // charges salariales ~23% du brut
const TAUX_NET   = 1 - TAUX_SAL;        // net/brut ~0.77
const TAUX_COCO  = 1 + TAUX_PAT;        // coût total/brut ~1.45
const IS_REDUIT  = 0.15;
const IS_NORMAL  = 0.25;
const PFU        = 0.30;

function calcScenario(brut_annuel, resultat_avant_rem) {
  const cout_total   = brut_annuel * TAUX_COCO;
  const salaire_net  = brut_annuel * TAUX_NET;
  const resultat_is  = Math.max(0, resultat_avant_rem - cout_total);
  const is           = resultat_is <= 42_500 ? resultat_is * IS_REDUIT : 42_500 * IS_REDUIT + (resultat_is - 42_500) * IS_NORMAL;
  const beni_distrib = resultat_is - is;
  const div_net      = beni_distrib * (1 - PFU);
  const total_net    = salaire_net + div_net;
  const tx_effectif  = total_net > 0 ? ((CA_AN1 - total_net) / CA_AN1 * 100) : 0;
  return { brut_annuel, cout_total, salaire_net, resultat_is, is, beni_distrib, div_net, total_net, tx_effectif };
}

// 3 scénarios An1 (CA 80k, résultat brut 66k)
const S = {
  A: calcScenario(12_000, RESULTAT_BRUT),   // Minimal — 1 000 €/mois brut
  B: calcScenario(24_000, RESULTAT_BRUT),   // Équilibre — 2 000 €/mois brut
  C: calcScenario(36_000, RESULTAT_BRUT),   // Modéré — 3 000 €/mois brut
};

// An2 scénarios
const CA_AN2          = 120_000;
const CHARGES_OPE_AN2 = 20_000;
const RES_AN2         = CA_AN2 - CHARGES_OPE_AN2;  // 100 000

const S2 = {
  rec:  calcScenario(30_000, RES_AN2),   // Recommandé An2
  max:  calcScenario(48_000, RES_AN2),   // Salaire élevé
};

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('💰', 'Simulation réaliste — pas d\'optimisation borderline. L\'objectif : te rémunérer correctement tout en capitalisant.', 'blue_background'),
    p(),
    qot('La bonne question n\'est pas "comment payer le moins d\'impôts ?" mais "comment structurer pour être serein sur 3 ans ?"'),
    p(),
    div(),
  );

  // ── 1. Rappel SASU à l'IS ─────────────────────────────────────────────────
  add(
    h1('1️⃣ Rappel fondamental — SASU à l\'IS'),
    p(),
    bul('Président assimilé salarié → régime général (pas TNS comme micro)'),
    bul('Charges sociales élevées sur le salaire : ~68% du brut (patronales + salariales)'),
    bul('Dividendes soumis à PFU 30% uniquement (flat tax — pas de charges sociales)'),
    bul('IS 15% jusqu\'à 42 500 € de bénéfice · 25% au-delà'),
    bul('Résultat = levier d\'optimisation entre salaire et dividendes'),
    p(),
    cal('⚠️', 'Salaire élevé = plus de protection sociale (retraite, arrêts maladie) mais moins d\'argent en poche. Dividendes = moins de protection sociale mais net plus élevé.', 'yellow_background'),
    p(),
    div(),
  );

  // ── 2. Hypothèses An1 ─────────────────────────────────────────────────────
  add(
    h1('2️⃣ Hypothèses — Année 1 (CA 80 000 €)'),
    p(),
    bul(`Chiffre d\'affaires total HT : ${fmt(CA_AN1)}`),
    bul('  dont Prestations agence : 50 000 €'),
    bul('  dont Affiliation schoolsWP + digital : 30 000 €'),
    p(),
    bul('Charges opérationnelles :'),
    bul('  Outils / SaaS / hébergement : 6 000 €'),
    bul('  Comptable / banque / RC Pro : 3 000 €'),
    bul('  Divers / formation / matériel : 5 000 €'),
    bulb(`  Total charges : ${fmt(CHARGES_OPE)}`),
    p(),
    bulb(`Résultat avant rémunération : ${fmt(RESULTAT_BRUT)}`),
    p(),
    cal('📌', 'C\'est sur ces 66 000 € que s\'appliquent les charges sociales du salaire + l\'IS. L\'enjeu : les répartir intelligemment.', 'blue_background'),
    p(),
    div(),
  );

  // ── 3. Scénarios ──────────────────────────────────────────────────────────
  add(
    h1('3️⃣ Simulations — 3 scénarios (CA 80k)'),
    p(),
  );

  // Scénario A
  add(
    h2('Scénario A — Salaire minimal (1 000 €/mois brut)'),
    cal('🎯', 'Recommandé si tu as une épargne de transition et veux capitaliser la trésorerie SASU.', 'green_background'),
    p(),
  );
  add(
    tog('Calcul détaillé Scénario A', [
      p(`Salaire brut annuel             : ${fmt(S.A.brut_annuel)}`),
      p(`Charges sociales (~68% du brut) : + ${fmt(S.A.brut_annuel * TAUX_PAT)}`),
      p(`Coût total salarial entreprise  : ${fmt(S.A.cout_total)}`),
      p(`Salaire net perçu               : ${fmt(S.A.salaire_net)} / an  (${fmt(S.A.salaire_net / 12)} / mois)`),
      p(''),
      p(`Résultat avant IS               : ${fmt(RESULTAT_BRUT)} – ${fmt(S.A.cout_total)} = ${fmt(S.A.resultat_is)}`),
      p(`IS 15%                          : ${fmt(S.A.is)}`),
      p(`Bénéfice distribuable           : ${fmt(S.A.beni_distrib)}`),
      p(''),
      p(`Dividendes bruts versés         : ${fmt(S.A.beni_distrib)}`),
      p(`Flat tax PFU 30%                : – ${fmt(S.A.beni_distrib * PFU)}`),
      p(`Dividendes nets perçus          : ${fmt(S.A.div_net)}`),
      p(''),
      p(`▶  Salaire net                  : ${fmt(S.A.salaire_net)}`),
      p(`▶  Dividendes nets              : ${fmt(S.A.div_net)}`),
      p(`▶  TOTAL NET PERÇU              : ${fmt(S.A.total_net)}`),
    ]),
    p(),
    bul('✅  Avantages : IS minimal, dividendes maximisés, trésorerie SASU préservée'),
    bul('⚠️  Risques : protection sociale réduite (retraite, arrêts maladie basés sur salaire)'),
    bul(`📊  Taux de prélèvement global : ${pct(S.A.tx_effectif)} du CA`),
    p(),
  );

  // Scénario B
  add(
    h2('Scénario B — Salaire équilibré (2 000 €/mois brut)'),
    cal('🎯', 'Recommandé si tu veux un équilibre protection sociale / optimisation fiscale.', 'blue_background'),
    p(),
  );
  add(
    tog('Calcul détaillé Scénario B', [
      p(`Salaire brut annuel             : ${fmt(S.B.brut_annuel)}`),
      p(`Charges sociales (~68% du brut) : + ${fmt(S.B.brut_annuel * TAUX_PAT)}`),
      p(`Coût total salarial entreprise  : ${fmt(S.B.cout_total)}`),
      p(`Salaire net perçu               : ${fmt(S.B.salaire_net)} / an  (${fmt(S.B.salaire_net / 12)} / mois)`),
      p(''),
      p(`Résultat avant IS               : ${fmt(RESULTAT_BRUT)} – ${fmt(S.B.cout_total)} = ${fmt(S.B.resultat_is)}`),
      p(`IS 15%                          : ${fmt(S.B.is)}`),
      p(`Bénéfice distribuable           : ${fmt(S.B.beni_distrib)}`),
      p(''),
      p(`Dividendes bruts versés         : ${fmt(S.B.beni_distrib)}`),
      p(`Flat tax PFU 30%                : – ${fmt(S.B.beni_distrib * PFU)}`),
      p(`Dividendes nets perçus          : ${fmt(S.B.div_net)}`),
      p(''),
      p(`▶  Salaire net                  : ${fmt(S.B.salaire_net)}`),
      p(`▶  Dividendes nets              : ${fmt(S.B.div_net)}`),
      p(`▶  TOTAL NET PERÇU              : ${fmt(S.B.total_net)}`),
    ]),
    p(),
    bul('✅  Avantages : meilleure protection sociale, flexibilité dividendes, IS réduit'),
    bul('⚠️  Risques : charges sociales significatives sur le salaire'),
    bul(`📊  Taux de prélèvement global : ${pct(S.B.tx_effectif)} du CA`),
    p(),
  );

  // Scénario C
  add(
    h2('Scénario C — Salaire modéré (3 000 €/mois brut)'),
    cal('📌', 'Pour ceux qui veulent vivre uniquement du salaire et peu/pas de dividendes.', 'gray_background'),
    p(),
  );
  add(
    tog('Calcul détaillé Scénario C', [
      p(`Salaire brut annuel             : ${fmt(S.C.brut_annuel)}`),
      p(`Charges sociales (~68% du brut) : + ${fmt(S.C.brut_annuel * TAUX_PAT)}`),
      p(`Coût total salarial entreprise  : ${fmt(S.C.cout_total)}`),
      p(`Salaire net perçu               : ${fmt(S.C.salaire_net)} / an  (${fmt(S.C.salaire_net / 12)} / mois)`),
      p(''),
      p(`Résultat avant IS               : ${fmt(RESULTAT_BRUT)} – ${fmt(S.C.cout_total)} = ${fmt(S.C.resultat_is)}`),
      p(`IS 15%                          : ${fmt(S.C.is)}`),
      p(`Bénéfice distribuable           : ${fmt(S.C.beni_distrib)}`),
      p(''),
      p(`Dividendes bruts versés         : ${fmt(S.C.beni_distrib)}`),
      p(`Flat tax PFU 30%                : – ${fmt(S.C.beni_distrib * PFU)}`),
      p(`Dividendes nets perçus          : ${fmt(S.C.div_net)}`),
      p(''),
      p(`▶  Salaire net                  : ${fmt(S.C.salaire_net)}`),
      p(`▶  Dividendes nets              : ${fmt(S.C.div_net)}`),
      p(`▶  TOTAL NET PERÇU              : ${fmt(S.C.total_net)}`),
    ]),
    p(),
    bul('✅  Avantages : protection sociale correcte, revenu stable prévisible'),
    bul('⚠️  Inconvénients : charges sociales très élevées, peu de bénéfice résiduel, faibles dividendes'),
    bul(`📊  Taux de prélèvement global : ${pct(S.C.tx_effectif)} du CA`),
    p(),
    div(),
  );

  // ── Tableau comparatif ────────────────────────────────────────────────────
  add(
    h1('4️⃣ Comparaison des 3 scénarios (CA 80k)'),
    p(),
  );

  const rows = [
    ['Salaire brut/mois',    fmt(S.A.brut_annuel/12), fmt(S.B.brut_annuel/12), fmt(S.C.brut_annuel/12)],
    ['Salaire net/mois',     fmt(S.A.salaire_net/12), fmt(S.B.salaire_net/12), fmt(S.C.salaire_net/12)],
    ['Dividendes nets/an',   fmt(S.A.div_net),        fmt(S.B.div_net),        fmt(S.C.div_net)],
    ['IS payé',              fmt(S.A.is),             fmt(S.B.is),             fmt(S.C.is)],
    ['TOTAL NET ANNUEL',     fmt(S.A.total_net),      fmt(S.B.total_net),      fmt(S.C.total_net)],
    ['Tréso SASU conservée', fmt(S.A.beni_distrib - S.A.div_net + S.A.div_net*0), fmt(0), fmt(0)],
  ];

  rows.forEach(([label, a, b, c]) => {
    add(bul(`${label.padEnd(28)}  A: ${a.padStart(10)}  B: ${b.padStart(10)}  C: ${c.padStart(10)}`));
  });

  add(p());
  add(cal('🥇', `Scénario recommandé An1 : B (${fmt(S.B.total_net)} net) — équilibre protection / trésorerie / optimisation.`, 'green_background'));
  add(p());

  // Protection sociale
  add(
    tog('Protection sociale par scénario — Impact concret', [
      p('Les droits sociaux sont calculés sur le salaire brut, pas sur les dividendes.'),
      p(''),
      p('Scénario A (12k brut/an) :'),
      bul('Retraite : droits très limités (base minimum cotisée)'),
      bul('Arrêt maladie : indemnisation partielle seulement si salaire ≥ SMIC'),
      bul('Chômage : aucun (pas d\'assurance chômage pour président SASU)'),
      bul('Mutuelle : obligatoire via contrat perso (non prise en charge employeur si salaire < seuil)'),
      p(''),
      p('Scénario B (24k brut/an) :'),
      bul('Retraite : cotisations correctes (trimestres complets validés)'),
      bul('Arrêt maladie : IJSS (Indemnités Journalières) activées si arrêt > 3j'),
      bul('Prévoyance : possible via contrat Madelin ou contrat collectif'),
      p(''),
      p('Scénario C (36k brut/an) :'),
      bul('Retraite : trimestres pleins + retraite complémentaire AGIRC-ARRCO correcte'),
      bul('Arrêt maladie : IJSS complètes'),
      bul('Prévoyance : bien couverte'),
      p(''),
      cal('💡', 'Alternative An1 : salaire B (24k) + contrat prévoyance perso (~50-100 €/mois) pour compléter la couverture.', 'blue_background'),
    ]),
    p(),
    div(),
  );

  // ── PER ───────────────────────────────────────────────────────────────────
  add(
    h1('5️⃣ PER — Plan Épargne Retraite (levier fiscal additionnel)'),
    p(),
    p('Le PER permet de déduire les versements du résultat imposable de la SASU (ou de ton revenu imposable perso selon le type de PER).'),
    p(),
    h3('PER Individuel (déduction sur revenu imposable perso)'),
    p(),
    bul('Plafond : 10% de tes revenus N-1 (plafonnés à 8 × PASS)'),
    bul('Pour un salaire 24 000 € brut : déduction max ~4 640 € / an'),
    bul('Versement 4 640 € → économie IR en fonction de ta TMI (0% à 41%)'),
    bul('Attention : bloqué jusqu\'à la retraite (sauf cas exceptionnels)'),
    p(),
    h3('PER d\'Entreprise — Madelin équivalent pour SASU'),
    p(),
    bul('Contrat Madelin TNS : adaptable pour assimilé salarié avec accord EC'),
    bul('Prévoyance Madelin déductible du résultat SASU (charges déductibles)'),
    bul('Conseil : valider avec l\'expert-comptable avant de souscrire'),
    p(),
    cal('💡', 'PER = bonne stratégie An2+ quand le bénéfice devient significatif. An1 : se concentrer sur la trésorerie opérationnelle.', 'blue_background'),
    p(),
    div(),
  );

  // ── Année 2 ───────────────────────────────────────────────────────────────
  add(
    h1('6️⃣ Simulation Année 2 (CA 120 000 €)'),
    p(),
    bul(`CA total HT : ${fmt(CA_AN2)}`),
    bul(`Charges opérationnelles (plus d\'outils, sous-traitance partielle) : ${fmt(CHARGES_OPE_AN2)}`),
    bul(`Résultat avant rémunération : ${fmt(RES_AN2)}`),
    p(),
  );

  add(
    tog('Scénario recommandé An2 — Salaire 2 500 €/mois brut (30k/an)', [
      p(`Salaire brut annuel             : ${fmt(S2.rec.brut_annuel)}`),
      p(`Coût total salarial entreprise  : ${fmt(S2.rec.cout_total)}`),
      p(`Salaire net perçu               : ${fmt(S2.rec.salaire_net)} / an  (${fmt(S2.rec.salaire_net/12)} / mois)`),
      p(''),
      p(`Résultat avant IS               : ${fmt(RES_AN2)} – ${fmt(S2.rec.cout_total)} = ${fmt(S2.rec.resultat_is)}`),
      p(`IS 15% (jusqu\'à 42 500 €) + 25% au-delà  : ${fmt(S2.rec.is)}`),
      p(`Bénéfice distribuable           : ${fmt(S2.rec.beni_distrib)}`),
      p(''),
      p('Option 1 — Distribuer 100% en dividendes :'),
      p(`Dividendes nets (après PFU 30%) : ${fmt(S2.rec.div_net)}`),
      p(`TOTAL NET PERÇU                 : ${fmt(S2.rec.total_net)}`),
      p(''),
      p('Option 2 — Distribuer 50% · Conserver 50% dans la SASU :'),
      p(`Dividendes nets (50%)           : ${fmt(S2.rec.beni_distrib * 0.5 * 0.70)}`),
      p(`Conservé SASU (investissement)  : ${fmt(S2.rec.beni_distrib * 0.5)}`),
      p(`TOTAL NET PERÇU (salaire + 50%) : ${fmt(S2.rec.salaire_net + S2.rec.beni_distrib * 0.5 * 0.70)}`),
    ]),
    p(),
    bul(`✅  Total net An2 Option 1 (100% dividendes) : ${fmt(S2.rec.total_net)}`),
    bul(`✅  Total net An2 Option 2 (50% conservé)    : ${fmt(S2.rec.salaire_net + S2.rec.beni_distrib * 0.5 * 0.70)}`),
    bul(`📈  IS payé : ${fmt(S2.rec.is)}  (IS taux mixte 15%/25% — plafond 42 500 € dépassé)`),
    p(),
    cal('💡', 'An2 : Option 2 (conserver 50% dans la SASU) est stratégique — constitue la réserve pour holding ou investissement futur.', 'green_background'),
    p(),
    div(),
  );

  // ── Logique stratégique ────────────────────────────────────────────────────
  add(
    h1('7️⃣ Logique stratégique An1 → An2 → An3'),
    p(),
  );

  add(
    tog('Année 1 — Capitalisation', [
      p('Objectif : structurer sans se fragiliser.'),
      bul('Salaire : 0 – 24 000 € brut/an selon épargne perso disponible'),
      bul('Dividendes : 0 (pas de bénéfice à distribuer avant clôture du 1er exercice)'),
      bul('Priorité : trésorerie SASU ≥ 3 mois de charges avant M12'),
      bul('Action : verser un acompte sur dividendes en décembre si bénéfice visible'),
      bul('Avec EC : ajuster en janvier de l\'année suivante selon le bilan réel'),
    ]),
    p(),
    tog('Année 2 — Optimisation', [
      p('Objectif : rémunération correcte + premiers vrais dividendes.'),
      bul('Salaire : 24 000 – 36 000 € brut/an (selon CA stabilisé)'),
      bul('Dividendes : distribuer 50 – 100% du bénéfice net IS'),
      bul('PER : envisager premiers versements déductibles'),
      bul('Prévoyance : souscrire si pas encore fait (contrat complémentaire santé + prévoyance)'),
      bul('Revue avec EC : optimisation exacte salaire/dividendes au 1er trimestre An2'),
    ]),
    p(),
    tog('Année 3 — Structuration', [
      p('Objectif : architecture fiscale longue durée.'),
      bul('Holding : envisager si bénéfice > 60 000 € non distribué'),
      bul('Investissement : loger les bénéfices non distribués dans des actifs'),
      bul('PER : maximiser les versements annuels'),
      bul('Décision : rester solo ou premier prestataire régulier ?'),
      bul('Revue holding avec EC : calcul du montage optimal'),
    ]),
    p(),
    div(),
  );

  // ── SASU vs Micro ─────────────────────────────────────────────────────────
  add(
    h1('8️⃣ SASU vs Micro — Quand la SASU s\'impose'),
    p(),
    bul('SASU pertinente si CA > 50 000 – 60 000 € : IS + dividendes plus avantageux que cotisations micro'),
    bul('SASU pertinente si tu vises la crédibilité B2B (contrats > 5 000 €)'),
    bul('SASU pertinente si tu penses croissance (outsourcing, holding, revente)'),
    bul('SASU pertinente si tu veux déduire les charges (outils, formation, matériel)'),
    p(),
    bul('Micro encore pertinente si CA < 40 000 €/an et aucune intention de croissance'),
    bul('Micro si tu veux simplicité administrative totale (pas d\'EC, pas de bilan)'),
    p(),
    cal('⚖️', 'Avec un CA cible de 80 000 € An1 → 120 000 € An2 : la SASU est clairement le bon choix.', 'green_background'),
    p(),
    div(),
  );

  // ── Actions concrètes ─────────────────────────────────────────────────────
  add(
    h1('9️⃣ Décisions concrètes — Action par action'),
    p(),
    h2('Décision 1 — Quel salaire choisir au lancement ?'),
    p(),
    num('Si tu as 6 mois de charges perso en épargne → Scénario A (12k brut) · Maximise la trésorerie'),
    num('Si tu as 3 mois en épargne → Scénario B (24k brut) · Équilibre recommandé'),
    num('Si pas d\'épargne → Scénario C (36k brut) · Mais attention : rentre moins net'),
    p(),
    h2('Décision 2 — Comment se verser les dividendes ?'),
    p(),
    bul('Pas avant le 1er bilan annuel (impossible légalement avant la 1ère clôture)'),
    bul('Acompte possible en cours d\'exercice si bénéfice visible et EC validé'),
    bul('Vote en Assemblée Générale Unique (AGU) = toi seul, sur procès-verbal'),
    bul('Virement compte SASU → compte perso dans les 9 mois suivant la clôture'),
    p(),
    h2('Décision 3 — Combien provisionner chaque mois ?'),
    p(),
    bul('Règle simple : 40% de chaque encaissement HT → sous-compte "Fiscal"'),
    bul('Détail : ~20% IS estimé + ~15% TVA + ~5% tampon'),
    bul('Charges sociales : provisionnées séparément si tu verses un salaire'),
    bul('Révision trimestrielle avec l\'EC pour ajuster si CA très différent du prévisionnel'),
    p(),
    cal('💡', 'Règle ultime : ne JAMAIS toucher au sous-compte Fiscal. Traiter cet argent comme s\'il n\'existait pas.', 'red_background'),
    p(),
    div(),
  );

  // ── Résumé exécutif ────────────────────────────────────────────────────────
  add(
    h2('📌 Résumé exécutif'),
    p(),
    bul(`An1 — CA 80k — Scénario B recommandé → ${fmt(S.B.total_net)} net/an`),
    bul(`An2 — CA 120k — Scénario 2 500 €/mois → ${fmt(S2.rec.total_net)} net/an (100% dividendes)`),
    bul('Protection : souscrire une prévoyance complémentaire (~80 €/mois)'),
    bul('PER : démarrer les versements en An2 quand le bénéfice est stable'),
    bul('Holding : évaluer en An3 si bénéfice non distribué > 60 000 €'),
    p(),
    qot(`Avec ${fmt(S.B.total_net)} net An1 et ${fmt(S2.rec.total_net)} net An2, ton modèle est solide, scalable et aligné avec ta trajectoire long terme.`),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Simulation Rémunération Optimisée SASU\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs — ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '💰' },
    properties: {
      title: { title: [{ text: { content: '💰 Simulation Rémunération SASU — schoolsWP + Agence' } }] },
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
  console.log('✅  Simulation rémunération créée !\n');
  console.log('  💰  Page : "💰 Simulation Rémunération SASU — schoolsWP + Agence"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Résultats des simulations (CA 80 000 €) :');
  console.log(`    Scénario A — 1 000 €/mois brut  : ${fmt(S.A.total_net)} net/an`);
  console.log(`    Scénario B — 2 000 €/mois brut  : ${fmt(S.B.total_net)} net/an  ← Recommandé An1`);
  console.log(`    Scénario C — 3 000 €/mois brut  : ${fmt(S.C.total_net)} net/an`);
  console.log('');
  console.log(`  Année 2 (CA 120 000 €) :`)
  console.log(`    2 500 €/mois brut → dividendes 100% : ${fmt(S2.rec.total_net)} net/an`);
  console.log('');
  console.log('  Contenu de la page :');
  console.log('    3 scénarios avec calculs détaillés (toggles)');
  console.log('    Tableau comparatif côte à côte');
  console.log('    Impact protection sociale par scénario');
  console.log('    PER — défiscalisation additionnelle An2+');
  console.log('    Simulation An2 complète');
  console.log('    3 décisions concrètes (salaire, dividendes, provisions)');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});

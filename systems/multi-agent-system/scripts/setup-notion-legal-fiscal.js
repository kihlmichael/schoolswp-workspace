#!/usr/bin/env node
/**
 * setup-notion-legal-fiscal.js — Architecture légale & fiscale SASU
 *
 * Crée dans Notion la page stratégique :
 *   "⚖️ Architecture Légale & Fiscale — SASU WordPress"
 *
 * Contenu :
 *   1. Architecture globale SASU à l'IS
 *   2. Répartition activités (Média vs Agence)
 *   3. Optimisation fiscale + simulation rémunération
 *   4. Dépenses déductibles (exhaustif + catégorisé)
 *   5. Structure comptable propre + calendrier fiscal
 *   6. Protection stratégique (RC Pro, CGV, contrats)
 *   7. Vision 3 ans + option holding
 *   8. Pièges à éviter
 *   9. Dashboard actions légales (checkboxes)
 *
 * Variables :
 *   NOTION_API_KEY         — obligatoire
 *   NOTION_PARENT_PAGE_ID  — page parente (obligatoire)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   node scripts/setup-notion-legal-fiscal.js
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
const rtc = (txt) => rt(txt, { code: true });

const h1  = (txt) => ({ object: 'block', type: 'heading_1',  heading_1:  { rich_text: [rt(txt)] } });
const h2  = (txt) => ({ object: 'block', type: 'heading_2',  heading_2:  { rich_text: [rt(txt)] } });
const h3  = (txt) => ({ object: 'block', type: 'heading_3',  heading_3:  { rich_text: [rt(txt)] } });

const p   = (txt = '') => ({ object: 'block', type: 'paragraph', paragraph: { rich_text: txt ? [rt(txt)] : [] } });
const pb  = (txt)      => ({ object: 'block', type: 'paragraph', paragraph: { rich_text: [rtb(txt)] } });

const bul  = (txt) => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rt(txt)] } });
const bulb = (txt) => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rtb(txt)] } });
const num  = (txt) => ({ object: 'block', type: 'numbered_list_item', numbered_list_item: { rich_text: [rt(txt)] } });

const tod = (txt, checked = false) => ({
  object: 'block', type: 'to_do',
  to_do: { rich_text: [rt(txt)], checked },
});

const div = () => ({ object: 'block', type: 'divider', divider: {} });

const cal = (emoji, txt, color = 'gray_background') => ({
  object: 'block', type: 'callout',
  callout: { icon: { type: 'emoji', emoji }, rich_text: [rt(txt)], color },
});

const qot = (txt) => ({ object: 'block', type: 'quote', quote: { rich_text: [rt(txt)] } });

const tog = (title, children = []) => ({
  object: 'block', type: 'toggle',
  toggle: { rich_text: [rtb(title)], children },
});

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('⚖️', 'La SASU est un véhicule stratégique d\'actifs WordPress — pas juste une agence.', 'blue_background'),
    p(),
    qot('Une structure fiscale propre au départ = des décisions libres toute la vie. Une structure bancale = des contraintes permanentes.'),
    p(),
    div(),
  );

  // ── 1. Architecture globale ────────────────────────────────────────────────
  add(
    h1('1️⃣ Architecture globale recommandée'),
    p(),
    cal('🎯', 'SASU à l\'IS (Impôt sur les Sociétés) — seule option cohérente avec ta trajectoire.', 'green_background'),
    p(),
    h3('Pourquoi SASU à l\'IS et pas autre chose ?'),
    p(),
    bul('vs Auto-Entrepreneur  →  Plafond AE bloquant (77 700 €/an), IR direct, zéro optimisation'),
    bul('vs EURL à l\'IR        →  Résultat intégré au revenu perso même non distribué — piège fiscal'),
    bul('vs EURL à l\'IS        →  Possible, mais SASU plus souple pour évoluer (associés, holding)'),
    bul('vs SAS                →  Identique fiscalement, mais SASU = 1 associé = moins de contraintes'),
    p(),
    h3('Ce que la SASU à l\'IS te permet'),
    p(),
    bul('Séparer patrimoine perso et professionnel (responsabilité limitée au capital)'),
    bul('Fixer ta rémunération librement (salaire + dividendes)'),
    bul('Déduire toutes les charges professionnelles avant IS'),
    bul('Taux IS réduit à 15% jusqu\'à 42 500 € de bénéfice (puis 25%)'),
    bul('Capitaliser les bénéfices dans la SASU sans les distribuer'),
    bul('Option holding ultérieure sans tout reconstruire'),
    p(),
    div(),
  );

  // ── 2. Répartition activités ───────────────────────────────────────────────
  add(
    h1('2️⃣ Répartition stratégique des activités'),
    p(),
    h2('Les 2 flux de revenus'),
    p(),
  );

  add(
    tog('A) Revenus Média & Affiliation — schoolsWP', [
      bul('Commissions affiliation plugins (FluentCRM, Tutor LMS, Rank Math…)'),
      bul('Sponsoring articles ou newsletters'),
      bul('Formations digitales vendues sur schoolsWP.com'),
      bul('Produits digitaux (guides, checklists, templates)'),
      bul('Revenus publicité display si trafic significatif'),
      p(),
      cal('💡', 'Tous ces revenus passent dans la SASU — schoolsWP est une marque commerciale, pas une entité séparée.', 'blue_background'),
    ]),
    p(),
    tog('B) Revenus Prestations — Agency Branch', [
      bul('Audits WordPress (Audit & Blueprint 1 200 – 2 000 €)'),
      bul('Projets CORE WordPress Learning System™ (3 000 – 6 000 €)'),
      bul('Projets PREMIUM (6 000 – 10 000 €)'),
      bul('Maintenance mensuelle (300 – 600 €/mois par client)'),
      bul('SEO Mensuel (500 – 900 €/mois)'),
      p(),
      cal('💡', 'Les prestations sont facturées par la SASU avec TVA (régime réel normal recommandé).', 'blue_background'),
    ]),
    p(),
  );

  add(
    h2('Stratégie de centralisation'),
    p(),
    cal('✅', 'Tout dans la SASU. schoolsWP = marque commerciale de la SASU. 1 seule structure, 1 seule comptabilité.', 'green_background'),
    p(),
    bul('Simplification comptable (1 seul bilan, 1 seul EC)'),
    bul('Image professionnelle unifiée (même SIRET pour affiliation et agence)'),
    bul('Pas de conflits micro-entreprise / société (deux statuts ne coexistent pas proprement)'),
    bul('Déduction intégrale des outils communs (SEO, IA, hébergement)'),
    bul('Revenus affiliation traités comme CA ordinaire → déductible des charges'),
    p(),
    div(),
  );

  // ── 3. Optimisation fiscale ────────────────────────────────────────────────
  add(
    h1('3️⃣ Optimisation fiscale intelligente'),
    p(),
    h2('Schéma de rémunération optimal'),
    p(),
  );

  add(
    tog('Année 1 — Mode consolidation', [
      p('Priorité : trésorerie SASU > rémunération perso.'),
      p(),
      bul('Salaire président : 0 à 1 500 €/mois NET (selon besoin perso et trésorerie)'),
      bul('Pas de dividendes année 1 — pas de bénéfice distribuable avant clôture'),
      bul('Objectif : maximiser les charges déductibles, minimiser le bénéfice imposable'),
      bul('Provision URSSAF mensuelle (si salaire > 0) : ~45-50% du brut en charges sociales'),
      p(),
      cal('⚠️', 'Charges sociales président SASU : ~80% du brut (régime général = cotisations élevées). Budget à provisionner impérativement.', 'red_background'),
    ]),
    p(),
    tog('Année 2 — Mode stabilisation', [
      p('CA stable → optimisation du mix salaire/dividendes.'),
      p(),
      bul('Salaire cible : 2 000 – 3 000 €/mois NET (selon CA)'),
      bul('Dividendes : bénéfice après IS × 30% (flat tax PFU) ou TMI si plus favorable'),
      bul('Arbitrage avec l\'EC : quand les dividendes deviennent plus efficaces que le salaire'),
      bul('Épargne salariale si applicable (intéressement SASU depuis 2019)'),
    ]),
    p(),
    tog('Simulation rémunération — CA 8 000 €/mois HT', [
      p('─ Hypothèse de base ─────────────────────────────'),
      p('CA mensuel HT : 8 000 €'),
      p('Charges pro déductibles (outils, EC, RC Pro, abonnements) : ~1 200 €/mois'),
      p(),
      p('─ Salaire brut choisi : 2 500 €/mois ────────────'),
      p('Charges patronales + salariales (~80% brut) : ~2 000 €'),
      p('Net perçu : ~1 950 €/mois'),
      p(),
      p('─ Résultat avant IS ──────────────────────────────'),
      p('8 000 – 1 200 (charges) – 4 500 (salaire brut + charges sociales) = 2 300 €/mois'),
      p('IS 15% sur 2 300 × 12 = 27 600 € → IS annuel ~4 140 €'),
      p('Bénéfice net distribuable : ~23 460 €/an → dividendes flat tax 30% → ~16 422 € net'),
      p(),
      p('─ Revenu total perçu ─────────────────────────────'),
      p('Net salaire : 1 950 × 12 = 23 400 €'),
      p('Net dividendes : 16 422 €'),
      p('Total : 39 822 € net/an  (contre ~96 000 € CA brut)'),
      p(),
      cal('💡', 'Le ratio améliore fortement à CA 10 000 €+/mois. Objectif M6 : atteindre ce seuil.', 'green_background'),
    ]),
    p(),
    div(),
  );

  // ── 4. Déductibles ────────────────────────────────────────────────────────
  add(
    h1('4️⃣ Dépenses stratégiques déductibles'),
    p('Toutes ces dépenses réduisent le bénéfice imposable avant IS.'),
    cal('💡', 'Règle : toute dépense engagée dans l\'intérêt de la SASU est déductible. Conserver les factures.', 'green_background'),
    p(),
  );

  const deductibles = [
    ['Infrastructure WordPress', [
      'Hébergement (o2switch, WP Rocket, Cloudways…)',
      'Noms de domaine (schoolswp.com + variantes)',
      'CDN et services performance',
      'Certificats SSL si payants',
    ]],
    ['Plugins & Licences', [
      'Plugins premium (Rank Math Pro, FluentCRM, Tutor LMS…)',
      'Thèmes premium',
      'Licences développeur (accès multi-sites)',
      'WooCommerce extensions',
    ]],
    ['Outils SEO & IA', [
      'Ahrefs / Semrush / DataForSEO',
      'Thruuu, SurferSEO, ou équivalent',
      'OpenAI API (GPT-4, API Claude)',
      'Outils de monitoring et analytics',
    ]],
    ['Automatisation & SaaS', [
      'n8n (auto-hébergé ou cloud)',
      'Notion (workspace)',
      'Make / Zapier si utilisé',
      'Outils emailing (si hors FluentCRM)',
      'Outils de facturation (Zervant, Facture.net…)',
    ]],
    ['Matériel informatique', [
      'Ordinateur (amortissement sur 3 ans)',
      'Écran(s), clavier, souris',
      'Disques durs externes',
      'Casque audio, caméra (si contenu vidéo)',
      'Tablette graphique si pertinent',
    ]],
    ['Formation & Documentation', [
      'Formations en ligne (MSc, certifications)',
      'Abonnements livres / cours spécialisés',
      'Conférences et événements pros',
      'Documentation technique payante',
    ]],
    ['Expert-comptable & Juridique', [
      'Honoraires expert-comptable (~600-1 200 €/an)',
      'Frais de création SASU (greffe)',
      'Assurance RC Pro (~300-600 €/an)',
      'Avocat si besoin CGV / contrats',
    ]],
    ['Déplacements & Représentation', [
      'Déplacements clients (train, carburant avec barème kilométrique)',
      'Repas prospects / partenaires (dans la limite du raisonnable)',
      'Espace de coworking si utilisé',
      'Frais de bureau à domicile (quote-part proratisée)',
    ]],
  ];

  deductibles.forEach(([cat, items]) => {
    add(tog(cat, items.map((i) => bul(i))), p());
  });

  add(
    cal('⚠️', 'Dépenses mixtes (téléphone, internet) : ne déduire que la quote-part professionnelle (généralement 70-80% justifié).', 'yellow_background'),
    p(),
    div(),
  );

  // ── 5. Structure comptable ─────────────────────────────────────────────────
  add(
    h1('5️⃣ Structure comptable propre dès le départ'),
    p(),
    h2('Outils recommandés'),
    p(),
    bul('Compte bancaire pro : Qonto (19 €/mois) ou Shine (8 €/mois) ou Société Générale Pro'),
    bul('Expert-comptable en ligne : Indy (~50 €/mois) ou Dougs (~80 €/mois) ou Comptastart'),
    bul('Facturation : module de l\'EC ou Zervant (gratuit jusqu\'à 10 factures/mois)'),
    bul('Tableau de bord mensuel : Notion (ce workspace) + export CSV mensuel de la banque'),
    p(),
  );

  add(
    h2('Calendrier fiscal — À connaître absolument'),
    p(),
    tog('Mensuel / Trimestriel', [
      bul('TVA : déclaration mensuelle (régime réel normal) ou trimestrielle si CA < 800k€'),
      bul('Salaire président : DSIJ mensuelle si salaire versé'),
      bul('URSSAF : acomptes mensuels ou trimestriels selon effectif'),
      p(),
      cal('💡', 'Dès le 1er mois : ouvrir un sous-compte "provisions fiscal" et y virer 40% de chaque encaissement HT.', 'blue_background'),
    ]),
    p(),
    tog('Annuel', [
      bul('IS : acomptes en mars, juin, septembre, décembre (si IS > 3 000 €)'),
      bul('Liasse fiscale : dépôt au plus tard 7 mois après la clôture'),
      bul('Clôture exercice : 31 décembre (ou autre date choisie à la création)'),
      bul('Approbation des comptes : dans les 6 mois suivant la clôture'),
      bul('CFE (Cotisation Foncière des Entreprises) : décembre chaque année'),
    ]),
    p(),
  );

  add(
    h2('Règle de provision mensuelle'),
    p(),
    bul('Sur chaque encaissement HT : virer 20% → provision IS (sur le bénéfice estimé)'),
    bul('Sur chaque encaissement HT : virer 20% → provision TVA (si assujetti)'),
    bul('Sur chaque salaire brut : virer 45-50% → provision charges sociales URSSAF'),
    p(),
    cal('💡', 'Méthode simple : 40% de chaque virement client HT va dans le sous-compte "Fiscal". Le reste c\'est ta trésorerie opérationnelle.', 'green_background'),
    p(),
    div(),
  );

  // ── 6. Protection ─────────────────────────────────────────────────────────
  add(
    h1('6️⃣ Protection stratégique'),
    p(),
    h2('RC Pro — Responsabilité Civile Professionnelle'),
    p(),
    bul('Obligatoire avant la 1ère mission — aucune exception'),
    bul('Couvre les dommages causés au client (bug, perte de données, conseil erroné)'),
    bul('Budget : 300 – 600 €/an pour prestataire IT'),
    bul('Fournisseurs recommandés : Hiscox, AXA Pro, Allianz Pro, Simplis'),
    p(),
    h2('CGV — Conditions Générales de Vente'),
    p(),
    bul('Obligatoires en B2B dès la première facture'),
    bul('Mentions minimales : délais de paiement (30j max), pénalités de retard, clause propriété intellectuelle, clause de résiliation'),
    bul('Valider avec un avocat ou utiliser un modèle professionnel (LegalStart, Captain Contrat)'),
    bul('Affiliation : ajouter obligatoirement les mentions légales d\'affiliation sur chaque article sponsorisé'),
    p(),
  );

  add(
    h2('Contrat prestation type — Mentions obligatoires'),
    p(),
    tog('Voir le template minimum', [
      bul('Identification des parties (SASU + SIRET + client)'),
      bul('Objet précis de la mission (périmètre limité = moins de litiges)'),
      bul('Livrables définis clairement (pas de "et tout ce qui va avec")'),
      bul('Planning et jalons'),
      bul('Prix HT + TVA + modalités de paiement (acompte 30-50% à la signature)'),
      bul('Clause de propriété intellectuelle (IP reste à la SASU jusqu\'au solde)'),
      bul('Clause de confidentialité'),
      bul('Clause de résiliation (conditions + délais + pénalités)'),
      bul('Loi applicable et juridiction compétente'),
      p(),
      cal('🎯', 'Acompte 40% à la signature = filtre les mauvais payeurs + couvre les coûts initiaux.', 'green_background'),
    ]),
    p(),
    h2('Propriété intellectuelle — Affiliation'),
    p(),
    bul('Mention légale obligatoire : "Cet article contient des liens affiliés. En achetant via ces liens, je perçois une commission sans surcoût pour toi."'),
    bul('RGPD : politique de confidentialité à jour sur schoolsWP.com'),
    bul('Cookies : consentement conforme (CMP configuré sur le site)'),
    bul('Revenus affiliation : déclarer dans les revenus de la SASU → facturation si plateforme l\'exige'),
    p(),
    div(),
  );

  // ── 7. Vision 3 ans ────────────────────────────────────────────────────────
  add(
    h1('7️⃣ Vision 3 ans — Roadmap structure'),
    p(),
  );

  add(
    tog('Année 1 — Structuration (J0 → J365)', [
      bul('Immatriculer la SASU, ouvrir compte pro, RC Pro, EC'),
      bul('Centraliser schoolsWP + Agency dans la SASU'),
      bul('Salaire minimal, capitaliser la trésorerie'),
      bul('Objectif CA : 50 000 – 80 000 € HT'),
      bul('Constituer réserves (3 mois de charges au minimum)'),
      bul('Clôturer le 1er bilan proprement avec l\'EC'),
    ]),
    p(),
    tog('Année 2 — Stabilisation (J365 → J730)', [
      bul('CA stable ≥ 8 000 €/mois HT → ajuster salaire'),
      bul('Premiers dividendes si bénéfice significatif'),
      bul('MRR Maintenance ≥ 1 500 €/mois (5 clients récurrents)'),
      bul('Affiliation schoolsWP ≥ 500 €/mois'),
      bul('Objectif CA : 100 000 – 150 000 € HT'),
      bul('Décision : rester solo ou 1er prestataire régulier ?'),
    ]),
    p(),
    tog('Année 3 — Option Holding (si croissance forte)', [
      p('La holding devient pertinente quand :'),
      bul('Multiples sources de revenus stables (Agency + Média + Formations)'),
      bul('Bénéfices à réinvestir (pas tout distribuer en dividendes)'),
      bul('Envisage investissements (immobilier, actions, autres projets)'),
      bul('Revente potentielle de schoolsWP ou de l\'agence'),
      bul('CA > 200 000 € HT/an'),
      p(),
      cal('💡', 'Structure holding : SAS Holding → 100% SASU opérationnelle. Dividendes remontent dans la holding (quasi sans IS via régime mère-fille). Décision à prendre avec l\'EC en année 2.', 'blue_background'),
      p(),
      cal('⚠️', 'La holding complexifie la gestion (+500 €/an minimum). Ne pas créer avant d\'en avoir vraiment besoin.', 'yellow_background'),
    ]),
    p(),
    div(),
  );

  // ── 8. Pièges à éviter ─────────────────────────────────────────────────────
  add(
    h1('8️⃣ Pièges à éviter'),
    p(),
    bul('❌  Mélanger micro-entreprise + SASU — impossible légalement si même activité. Il faut choisir.'),
    bul('❌  Se payer trop tôt — les charges sociales URSSAF sont prélevées dès le 1er euro de salaire'),
    bul('❌  Sous-estimer les charges sociales — prévoir 80% du brut en charges patronales + salariales'),
    bul('❌  Négliger la trésorerie — 1 gros impayé sans trésorerie = problème immédiat'),
    bul('❌  Facturer sans contrat signé — oral ≠ opposable juridiquement'),
    bul('❌  Oublier la TVA — si régime réel, collecter et reverser la TVA à l\'État chaque mois/trimestre'),
    bul('❌  Pas d\'acompte à la signature — augmente drastiquement le risque d\'impayé'),
    bul('❌  Confondre CA et bénéfice — payer ses charges sociales sur le CA brut est une erreur courante'),
    bul('❌  Multiplier les offres dans les 6 premiers mois — 1 offre principale, 2 niveaux, puis stabiliser'),
    bul('❌  Dépenser le compte pro comme un compte perso — les virements perso = salaire = charges sociales'),
    p(),
    div(),
  );

  // ── 9. Dashboard actions légales ────────────────────────────────────────────
  add(
    h1('9️⃣ Dashboard — Actions légales & fiscales'),
    p('Master checklist — cocher au fur et à mesure.'),
    p(),
    h2('Création SASU'),
    p(),
    tod('Choisir le nom commercial et vérifier disponibilité (INPI)'),
    tod('Rédiger les statuts SASU (LegalStart, Captain Contrat ou avocat)'),
    tod('Déposer capital social (min 1 €, recommandé 1 000 €)'),
    tod('Immatriculer au RCS → obtenir SIRET'),
    tod('Ouvrir compte bancaire pro'),
    tod('Choisir et mandater l\'expert-comptable'),
    tod('Souscrire RC Pro'),
    tod('Configurer outil facturation'),
    p(),
    h2('Protection & documents'),
    p(),
    tod('Rédiger CGV (valider avec EC ou avocat)'),
    tod('Créer le template contrat prestation'),
    tod('Ajouter clause propriété intellectuelle aux contrats'),
    tod('Mettre à jour mentions légales schoolsWP.com'),
    tod('Ajouter disclaimer affiliation sur tous les articles concernés'),
    tod('Vérifier conformité RGPD (politique de confidentialité + cookies)'),
    p(),
    h2('Structure fiscale'),
    p(),
    tod('Choisir date de clôture exercice (31 décembre recommandé)'),
    tod('Ouvrir sous-compte "Provisions fiscal" dans le compte pro'),
    tod('Paramétrer provision automatique 40% sur chaque encaissement'),
    tod('Paramétrer rappels calendrier fiscal (TVA, IS, CFE)'),
    tod('Définir salaire initial avec l\'EC'),
    tod('Premier bilan prévisionnel (avec EC)'),
    p(),
    h2('Opérationnel'),
    p(),
    tod('Configurer numéro de facture séquentiel (SASU2026-001…)'),
    tod('Créer template devis PDF avec toutes les mentions légales'),
    tod('Paramétrer relance automatique impayés (J+30, J+45, J+60)'),
    tod('Configurer export comptable mensuel (CSV banque → EC)'),
    tod('Calendrier mensuel : 1er du mois = revue trésorerie + provisions'),
    p(),
    div(),
  );

  // ── Message final ──────────────────────────────────────────────────────────
  add(
    cal('🧭', 'La structure juridique n\'est pas une contrainte — c\'est le cadre qui te libère. Chaque euro bien structuré est un euro que tu contrôles.', 'blue_background'),
    p(),
    qot('"Véhicule stratégique d\'actifs WordPress" — SASU = l\'outil. schoolsWP = l\'actif. Formateurs WordPress = la cible. Tout est cohérent.'),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Architecture Légale & Fiscale SASU\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs — ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '⚖️' },
    properties: {
      title: { title: [{ text: { content: '⚖️ Architecture Légale & Fiscale — SASU WordPress' } }] },
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
  console.log('✅  Architecture légale & fiscale documentée !\n');
  console.log('  ⚖️   Page : "⚖️ Architecture Légale & Fiscale — SASU WordPress"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Structure :');
  console.log('    1️⃣   SASU à l\'IS — pourquoi vs AE / EURL / SAS');
  console.log('    2️⃣   Répartition Média (schoolsWP) vs Agence — tout dans la SASU');
  console.log('    3️⃣   Optimisation fiscale + simulation CA 8k€/mois');
  console.log('    4️⃣   Déductibles catégorisés (8 catégories, exhaustif)');
  console.log('    5️⃣   Structure comptable + calendrier fiscal + règle 40%');
  console.log('    6️⃣   RC Pro + CGV + contrat type + mentions affiliation');
  console.log('    7️⃣   Vision 3 ans (structuration → stabilisation → holding)');
  console.log('    8️⃣   10 pièges à éviter');
  console.log('    9️⃣   Dashboard 25 actions légales cochables');
  console.log('');
  console.log('  Règle clé documentée :');
  console.log('    40% de chaque encaissement HT → sous-compte "Provisions fiscal"');
  console.log('    (IS + TVA + URSSAF — pas toucher à cet argent)');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});

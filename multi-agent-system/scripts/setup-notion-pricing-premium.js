#!/usr/bin/env node
/**
 * setup-notion-pricing-premium.js — Pricing Premium Structuré SASU WordPress
 *
 * Crée dans Notion la page :
 *   "💎 Pricing Premium — WordPress Business System"
 *
 * Contenu :
 *   Principe fondamental (valeur, pas temps)
 *   3 offres structurées avec livrables + pricing + pitch
 *   Logique psychologique des 3 niveaux
 *   Grille de routing prospect → offre
 *   Calculateur de valeur client (template call découverte)
 *   Modèle économique (50/50, maintenance, upsell)
 *   5 mots interdits dans le pitch
 *   Objections + réponses
 *   Process de vente (découverte → signature)
 *   Projection financière
 *   Erreurs à éviter
 *
 * Variables :
 *   NOTION_API_KEY         — obligatoire
 *   NOTION_PARENT_PAGE_ID  — page parente (obligatoire)
 *
 * Pré-requis : Node 18+
 */

const API_KEY   = process.env.NOTION_API_KEY;
const PARENT_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || !PARENT_ID) {
  console.error('❌  Variables manquantes : NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

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

const rt  = (t, opts = {}) => ({ type: 'text', text: { content: t }, annotations: opts });
const rtb = (t) => rt(t, { bold: true });

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

// ─── Offres ───────────────────────────────────────────────────────────────────

const OFFRES = [
  {
    num:     '1',
    emoji:   '🟢',
    nom:     'Audit & Stratégie WordPress',
    role:    'Porte d\'entrée',
    cible:   'Entrepreneur déjà en ligne, mal structuré, besoin de clarté avant d\'investir',
    mini:    1000,
    maxi:    2000,
    duree:   '3 à 5 jours',
    livrables: [
      'Audit technique WordPress (performance, sécurité, structure)',
      'Audit SEO (maillage, intentions, opportunités)',
      'Audit automatisation (ce qui manque, ce qui est redondant)',
      'Diagnostic business (tunnel, CRM, conversion)',
      'Roadmap 90 jours priorisée',
      'Document stratégique livré en PDF + Notion',
    ],
    pitch: 'Avant d\'investir dans un système, comprends exactement ce qui bloque. Cet audit te donne la clarté pour décider — et une roadmap actionnelle pour agir.',
    upsell: 'Présenter naturellement l\'Offre 2 dans la roadmap. 70% des clients Audit deviennent clients Système.',
    vendre: 'Clarté stratégique, pas "mini audit technique". Le client repart avec une décision, pas juste un rapport.',
    color: 'green_background',
  },
  {
    num:     '2',
    emoji:   '🟠',
    nom:     'Système WordPress Structuré',
    role:    'Offre Standard — cœur du business',
    cible:   'Formateur / freelance sérieux qui veut un vrai système opérationnel',
    mini:    4000,
    maxi:    8000,
    duree:   '3 à 5 semaines',
    livrables: [
      'Refonte architecture WordPress (structure pages + navigation)',
      'CRM intégré et configuré (FluentCRM + séquences de base)',
      'Automatisation de base (inscription, relances, confirmation)',
      'Tunnel simple et fonctionnel (Lead → Offre → Remerciement)',
      'SEO technique propre (Core Web Vitals, balises, maillage)',
      'Formation client enregistrée (autonomie garantie)',
    ],
    pitch: 'Ton WordPress travaille pour toi ou contre toi. Ce système transforme ton site en outil qui vend, automatise et te libère.',
    upsell: 'Maintenance mensuelle systématiquement proposée à la livraison (300 – 500 €/mois). Accès facilité Offre 3 si scope évolue.',
    vendre: 'Système opérationnel, pas "site joli". Le client sort avec quelque chose qui fonctionne.',
    color: 'orange_background',
  },
  {
    num:     '3',
    emoji:   '🔴',
    nom:     'WordPress Business Engine',
    role:    'Offre Transformation — haut de gamme',
    cible:   'Entrepreneur avec ambition de croissance, CA existant, prêt à structurer sérieusement',
    mini:    8000,
    maxi:    15000,
    duree:   '6 à 10 semaines',
    livrables: [
      'Architecture complète WordPress (LMS, CRM, tunnel avancé)',
      'CRM avancé (FluentCRM + segmentation + scoring leads)',
      'Séquences automatisées complètes (nurturing, upsell, récurrence)',
      'Optimisation conversion (CTA, A/B, tracking GA4 + Meta)',
      'Structure cluster SEO (pilier + satellites + maillage)',
      'Intégration LMS ou booking (Tutor LMS, Calendly, ThriveCart)',
      'Formation client complète + documentation Notion',
      'Suivi post-livraison 4 semaines inclus',
    ],
    pitch: 'Tu as le contenu, l\'audience et le produit. Ce moteur transforme tout ça en machine à générer des revenus — sans dépendre d\'une plateforme externe.',
    upsell: 'Maintenance Expert (600 – 800 €/mois) + SEO Mensuel (500 – 900 €/mois) en suites naturelles.',
    vendre: 'Un moteur business, pas un site. On parle ROI : x€ de CA actuel, objectif y€ dans 12 mois.',
    color: 'red_background',
  },
];

// Packages maintenance
const MAINTENANCES = [
  { nom: 'Maintenance Starter', prix: 300, pour: 'Clients Offre 1 ou Offre 2 simple', inclus: ['Mises à jour WordPress + plugins (mensuel)', 'Backup sécurisé (hebdo)', '1h d\'intervention correctrice/mois', 'Rapport mensuel bref'] },
  { nom: 'Maintenance Expert',  prix: 600, pour: 'Clients Offre 2 ou 3',              inclus: ['Tout Starter +', '2h d\'interventions/mois', 'Monitoring performance 24/7', 'Suivi SEO mensuel (2 pages)', 'Priorité support'] },
  { nom: 'Maintenance Premium', prix: 900, pour: 'Clients Offre 3',                   inclus: ['Tout Expert +', 'Audit mensuel conversion', '4h d\'interventions/mois', 'Revue stratégique trimestrielle', 'Accès WhatsApp direct'] },
];

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  const fmt = (n) => n.toLocaleString('fr-FR') + ' €';

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('💎', 'Tu ne vends pas du temps. Tu vends une transformation mesurable et un système qui continue à travailler après ta livraison.', 'blue_background'),
    p(),
    qot('"Ce n\'est pas ce que tu fais qui justifie le prix. C\'est ce que le client gagne après."'),
    p(),
    div(),
  );

  // ── 1. Principe fondamental ────────────────────────────────────────────────
  add(
    h1('1️⃣ Principe fondamental'),
    p(),
    h3('Ce que tu ne vends PAS'),
    bul('❌  "Création de site WordPress"'),
    bul('❌  "Développement WordPress"'),
    bul('❌  "Refonte de votre site"'),
    bul('❌  "Pack 10h WordPress"'),
    p(),
    h3('Ce que tu vends'),
    bulb('✅  Structuration d\'un système WordPress rentable et automatisé'),
    bulb('✅  Transformation business mesurable (avant / après)'),
    bulb('✅  Gain de temps chiffré (automatisations)'),
    bulb('✅  Augmentation de conversion (tunnel + CRM)'),
    bulb('✅  Autonomie du client (formation + documentation)'),
    p(),
    h3('Le pricing doit refléter'),
    bul('Impact business — pas le nombre d\'heures'),
    bul('Expertise stratégique — pas l\'exécution technique'),
    bul('Effet long terme — pas le livrable ponctuel'),
    p(),
    cal('💡', 'Règle de base : ne jamais mentionner le temps passé dans le pitch ou le devis. Toujours parler en termes de résultat attendu.', 'green_background'),
    p(),
    div(),
  );

  // ── 2. Les 3 offres ────────────────────────────────────────────────────────
  add(
    h1('2️⃣ Structure — 3 offres claires'),
    p(),
    cal('📌', '3 niveaux. Pas 12 options. La clarté de l\'offre est un signal de confiance pour le client.', 'blue_background'),
    p(),
  );

  OFFRES.forEach((o) => {
    add(
      h2(`${o.emoji} Offre ${o.num} — ${o.nom}`),
      cal('💶', `${fmt(o.mini)} – ${fmt(o.maxi)}   ·   ${o.duree}   ·   Rôle : ${o.role}`, o.color),
      p(),
      h3('Pour qui ?'),
      p(o.cible),
      p(),
      h3('Livrables inclus'),
    );
    o.livrables.forEach((l) => add(bul(l)));
    add(
      p(),
      h3('Comment le pitcher'),
      qot(o.pitch),
      p(),
    );
    add(
      tog(`Vendre cette offre — Tips concrets`, [
        p(`Angle : ${o.vendre}`),
        p(),
        p(`Upsell naturel : ${o.upsell}`),
        p(),
        p('Ce qu\'il ne faut pas dire :'),
        bul('"Je vais passer X heures dessus"'),
        bul('"C\'est un site clé en main"'),
        bul('"C\'est ce que font tous mes clients"'),
        p(),
        p('Ce qu\'il faut dire :'),
        bulb('"Qu\'est-ce qui te coûte du temps chaque semaine ?"'),
        bulb('"C\'est quoi l\'impact si tu n\'as toujours pas de CRM dans 6 mois ?"'),
        bulb('"Ce qu\'on livre ici, c\'est X semaines de travail en moins pour toi chaque mois."'),
      ]),
      p(),
    );
  });

  add(div());

  // ── 3. Logique psychologique ──────────────────────────────────────────────
  add(
    h1('3️⃣ Logique psychologique des 3 niveaux'),
    p(),
    bul('🟢 Offre 1 (Audit)        →  Porte d\'entrée. Pas de résistance au prix. Commence la relation.'),
    bul('🟠 Offre 2 (Système)      →  Standard. La référence. Le prospect compare tout le reste à elle.'),
    bul('🔴 Offre 3 (Business Engine)  →  Ancre haute. Rend l\'Offre 2 plus raisonnable par contraste.'),
    p(),
    cal('💡', 'Présenter toujours les 3 offres en même temps. Le prospect choisit lui-même son niveau d\'engagement. Ne pas décider à sa place.', 'green_background'),
    p(),
    tog('Pourquoi présenter les 3 en même temps ?', [
      p('1. L\'Offre 3 ancre la valeur perçue → l\'Offre 2 semble raisonnable par contraste'),
      p('2. L\'Offre 1 réduit la résistance → "je peux toujours commencer par l\'audit"'),
      p('3. Le choix du niveau révèle l\'ambition du client → aide à qualifier le bon prospect'),
      p('4. L\'Offre 3 filtre les mauvais clients → ceux qui refusent même de l\'entendre ne sont pas ta cible'),
    ]),
    p(),
    div(),
  );

  // ── 4. Grille de routing ──────────────────────────────────────────────────
  add(
    h1('4️⃣ Grille de routing — Quel prospect → Quelle offre'),
    p(),
  );

  const routing = [
    ['Profil prospect',                        'Offre recommandée'],
    ['Budget signalé < 2 000 €',              '🟢 Offre 1 (Audit) — porte d\'entrée'],
    ['Budget signalé 2 000 – 6 000 €',        '🟠 Offre 2 (Système) — standard'],
    ['Budget signalé > 6 000 €',              '🔴 Offre 3 (Engine) — ou Offre 2 Premium'],
    ['Site existant → besoin clarté',          '🟢 Offre 1 → upsell Offre 2 dans la roadmap'],
    ['Formateur avec audience existante',      '🟠 Offre 2 ou 🔴 Offre 3'],
    ['Formateur sans site / nouveau départ',   '🟠 Offre 2'],
    ['OF / structure avec ambition forte',     '🔴 Offre 3'],
    ['Score fit ≤ 2 → hors cible',            '❌ Refuser poliment'],
  ];

  routing.slice(1).forEach(([profil, offre]) => {
    add(bul(`${profil.padEnd(42)} →  ${offre}`));
  });

  add(p(), div());

  // ── 5. Calculateur de valeur ──────────────────────────────────────────────
  add(
    h1('5️⃣ Calculateur de valeur — Template call découverte'),
    p('Remplir pendant ou juste après le call. Permet de justifier le prix avec les chiffres du client.'),
    p(),
    cal('💡', 'La valeur que tu apportes = la somme des gains du client. Toujours chiffrer avec ses propres données.', 'blue_background'),
    p(),
  );

  add(
    tog('Template — À remplir pendant le call', [
      p('─── Situation actuelle ──────────────────────────────'),
      p('CA actuel du client           : _____ €/mois'),
      p('Temps perdu en tâches manuelles : _____ h/semaine'),
      p('Coût heure estimé client      : _____ €/h'),
      p('Taux de conversion actuel     : _____ %'),
      p('CA manqué estimé/mois         : _____ €'),
      p(''),
      p('─── Calcul valeur apportée ──────────────────────────'),
      p('Gain temps automatisation     : _____ h/semaine × _____ semaines × _____ €/h = _____ €'),
      p('Gain conversion estimé        : _____ CA actuel × _____ % augmentation = _____ €/mois'),
      p('Gain temps client post-formation : _____ h/semaine × 12 mois × _____ €/h = _____ €/an'),
      p(''),
      p('─── Résultat ────────────────────────────────────────'),
      p('Valeur totale estimée sur 12 mois : _____ €'),
      p('Prix de l\'offre proposée      : _____ €'),
      p('Ratio valeur/prix              : _____×  (objectif : > 5×)'),
      p(''),
      cal('🎯', 'Si le ratio valeur/prix est > 5× : le prix est justifié. Présenter ce calcul au client directement.', 'green_background'),
    ]),
    p(),
    tog('Exemple rempli — Formateur FluentCRM', [
      p('CA actuel : 3 000 €/mois'),
      p('Temps perdu relances manuelles : 6h/semaine × 50 semaines × 80 €/h = 24 000 €/an'),
      p('Gain conversion tunnel + CRM : 3 000 × 15% = 450 €/mois × 12 = 5 400 €/an'),
      p('Formation client : 3h/semaine économisées × 50 × 80 € = 12 000 €/an'),
      p(''),
      p('Valeur totale : 24 000 + 5 400 + 12 000 = 41 400 € sur 12 mois'),
      p('Offre 2 proposée : 6 000 €'),
      p('Ratio : 41 400 / 6 000 = 6,9×  ✅'),
      p(''),
      p('Pitch : "Tu investis 6 000 € pour un retour estimé de 41 000 € sur 12 mois. C\'est un ratio de 7."'),
    ]),
    p(),
    div(),
  );

  // ── 6. Modèle économique ──────────────────────────────────────────────────
  add(
    h1('6️⃣ Modèle économique intelligent'),
    p(),
    h2('Modalités de paiement'),
    p(),
    bul('50% à la signature (acompte) — filtre les prospects non sérieux'),
    bul('50% à la livraison (ou jalons intermédiaires pour Offre 3)'),
    bul('Offre 3 : 40% signature · 30% à M3 · 30% à la livraison'),
    p(),
    cal('⚠️', 'Sans acompte = pas de démarrage. C\'est une règle, pas une option. L\'acompte qualifie l\'engagement.', 'red_background'),
    p(),
  );

  add(h2('Packages Maintenance Mensuelle'), p());

  MAINTENANCES.forEach((m) => {
    add(
      tog(`${m.nom} — ${m.prix} €/mois (pour : ${m.pour})`, [
        ...m.inclus.map((i) => bul(i)),
      ]),
      p(),
    );
  });

  add(
    cal('💡', 'Règle : proposer la Maintenance lors de CHAQUE livraison. Ne jamais attendre que le client demande.', 'green_background'),
    p(),
    h2('Upsell trimestriel'),
    p(),
    bul('À M3 post-livraison : revue stratégique (2h, 300 – 500 €)'),
    bul('À M6 : optimisation conversion ou SEO (projet 500 – 1 500 €)'),
    bul('À M12 : évolution système (nouveau cluster SEO, LMS additionnel)'),
    bul('Maintenance Expert → SEO Mensuel (bundle 900 – 1 200 €/mois)'),
    p(),
    div(),
  );

  // ── 7. Mots interdits ─────────────────────────────────────────────────────
  add(
    h1('7️⃣ Les 5 mots interdits dans le pitch'),
    p(),
    bul('❌  "Site"         → Remplacer par "système"'),
    bul('❌  "Heures"       → Remplacer par "résultat", "transformation"'),
    bul('❌  "Refonte"      → Remplacer par "structuration", "architecture"'),
    bul('❌  "Template"     → Remplacer par "architecture sur-mesure"'),
    bul('❌  "Je vais faire" → Remplacer par "tu vas obtenir", "le système va faire"'),
    p(),
    qot('Chaque fois que tu dis "heures", le client pense "coût". Chaque fois que tu dis "résultat", le client pense "investissement".'),
    p(),
    div(),
  );

  // ── 8. Objections ─────────────────────────────────────────────────────────
  add(
    h1('8️⃣ Objections + Réponses'),
    p(),
  );

  const objections = [
    ['"C\'est cher pour un site WordPress."',
     '"Ce n\'est pas un site. C\'est un système qui automatise tes relances, structure ton CRM et te génère des ventes en continu. Un site, tu peux en avoir un pour 500 €. Ce que je livre, ça te rapporte."'],
    ['"Je vais réfléchir."',
     '"C\'est normal. Qu\'est-ce qui te manque pour décider ? Si c\'est le budget : on peut commencer par l\'Audit (1 000 €) pour valider la direction avant d\'engager le reste."'],
    ['"J\'ai un ami qui fait ça moins cher."',
     '"Sûrement. La question n\'est pas le prix de départ, c\'est ce que ça rapporte. Si ce système te génère 5 000 € de CA en plus par mois, combien coûte-t-il vraiment ?"'],
    ['"Je peux pas me permettre maintenant."',
     '"Quand est-ce que tu te le permets ? Si tu attends d\'avoir plus de CA pour structurer, tu risques de bricoler encore 2 ans. L\'Audit à 1 000 € te donne la clarté pour décider quand."'],
    ['"J\'ai besoin de faire ça moi-même."',
     '"Bien sûr — c\'est pour ça qu\'une formation client est incluse. Le but n\'est pas que tu dépenses de moi. C\'est que tu sois autonome à la livraison."'],
  ];

  objections.forEach(([obj, rep]) => {
    add(
      tog(obj, [
        p('Réponse :'),
        qot(rep),
      ]),
      p(),
    );
  });

  add(div());

  // ── 9. Process de vente ───────────────────────────────────────────────────
  add(
    h1('9️⃣ Process de vente — De la découverte à la signature'),
    p(),
  );

  const process_steps = [
    ['Étape 1 — Prise de contact (J0)',        'Formulaire qualifiant (3 questions). Score fit immédiat. Si fit ≤ 2 → réponse polie mais non.'],
    ['Étape 2 — Call découverte (J1-J3)',       '30 min max. 7 questions de qualification. Calculateur de valeur rempli. Présentation des 3 offres.'],
    ['Étape 3 — Devis sous 24h (J2-J4)',       'PDF professionnel. Offre recommandée mise en avant. Deux autres en comparaison. CTA clair.'],
    ['Étape 4 — Relance à J+5 (si silence)',   'Un seul message : "Tu as eu le temps de regarder ? Des questions sur le devis ?". Pas de pression.'],
    ['Étape 5 — Signature + Acompte (J3-J7)',  'Contrat + facture acompte 50%. Démarrage uniquement après réception de l\'acompte.'],
    ['Étape 6 — Onboarding (J0 projet)',        'Envoi template onboarding Notion. Accès partagés. Réunion kick-off 1h.'],
  ];

  process_steps.forEach(([step, detail]) => {
    add(
      tog(step, [p(detail)]),
      p(),
    );
  });

  add(div());

  // ── 10. Projection ────────────────────────────────────────────────────────
  add(
    h1('📈 Projection financière'),
    p(),
    h2('Tu n\'as pas besoin de volume. Tu as besoin de cohérence.'),
    p(),
    bul('2 projets Offre 2 / mois  →  2 × 6 000 € = 12 000 € HT/mois'),
    bul('1 projet Offre 3 / mois   →  1 × 10 000 € = 10 000 € HT/mois'),
    bul('3 clients Maintenance      →  3 × 500 € = 1 500 € MRR/mois'),
    p(),
    bulb('Scénario cible M12 : 1 Offre 2 + 1 Offre 3 + 5 Maintenances  →  ~18 000 € HT/mois'),
    p(),
    cal('💡', 'À 18 000 €/mois HT → 216 000 €/an HT → IS 15% jusqu\'à 42 500 € puis 25%. Niveau holding pertinent.', 'green_background'),
    p(),
    div(),
  );

  // ── 11. Erreurs à éviter ──────────────────────────────────────────────────
  add(
    h1('⚠️ Erreurs à éviter'),
    p(),
    bul('❌  Tarifs bas "pour rassurer" → ça rassure pas, ça inquiète (perception qualité)'),
    bul('❌  Offre floue → le prospect ne sait pas ce qu\'il achète = il achète rien'),
    bul('❌  Trop de personnalisation → chaque exception crée un précédent dangereux'),
    bul('❌  Argumentaire technique au lieu business → parler plugins ennuie, parler résultats convainc'),
    bul('❌  Baisser le prix sans contrepartie → toujours retirer quelque chose si on réduit le prix'),
    bul('❌  Démarrer sans acompte → la date de livraison glisse toujours sans acompte'),
    bul('❌  Tout faire soi-même → facturer l\'expertise, pas l\'exécution manuelle'),
    bul('❌  Oublier la Maintenance → c\'est proposé à CHAQUE livraison, pas en option oubliée'),
    p(),
    div(),
  );

  // ── Résumé exécutif ────────────────────────────────────────────────────────
  add(
    h2('📌 Résumé exécutif'),
    p(),
    bul('🟢 Offre 1 — Audit & Stratégie  :  1 000 – 2 000 €  ·  Porte d\'entrée · 3-5 jours'),
    bul('🟠 Offre 2 — Système Structuré  :  4 000 – 8 000 €  ·  Standard · 3-5 semaines'),
    bul('🔴 Offre 3 — Business Engine    :  8 000 – 15 000 € ·  Transformation · 6-10 semaines'),
    p(),
    bul('Maintenance : 300 – 900 €/mois · proposée à chaque livraison'),
    bul('Paiement : 50% acompte · 50% livraison (Offre 3 : 40/30/30)'),
    bul('Mots interdits : site, heures, refonte, template, "je vais faire"'),
    p(),
    qot('Le bon prix est celui que le client paie sans négocier parce qu\'il comprend exactement ce qu\'il gagne.'),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Pricing Premium Structuré SASU\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs — ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '💎' },
    properties: {
      title: { title: [{ text: { content: '💎 Pricing Premium — WordPress Business System' } }] },
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
  console.log('✅  Pricing Premium documenté !\n');
  console.log('  💎  Page : "💎 Pricing Premium — WordPress Business System"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Structure :');
  console.log('    1️⃣   Principe fondamental (valeur, pas temps)');
  console.log('    2️⃣   3 offres détaillées avec livrables + pitch + tips de vente');
  console.log('    3️⃣   Logique psychologique des 3 niveaux');
  console.log('    4️⃣   Grille de routing prospect → offre');
  console.log('    5️⃣   Calculateur de valeur (template + exemple chiffré)');
  console.log('    6️⃣   Modèle économique (50/50 + 3 packages Maintenance)');
  console.log('    7️⃣   5 mots interdits dans le pitch');
  console.log('    8️⃣   5 objections + réponses complètes');
  console.log('    9️⃣   Process de vente 6 étapes (découverte → signature)');
  console.log('    📈  Projection financière (scénario cible M12)');
  console.log('    ⚠️   8 erreurs à éviter');
  console.log('');
  console.log('  Grille tarifaire :');
  console.log('    🟢 Offre 1 — Audit & Stratégie      :  1 000 – 2 000 €');
  console.log('    🟠 Offre 2 — Système Structuré      :  4 000 – 8 000 €');
  console.log('    🔴 Offre 3 — Business Engine        :  8 000 – 15 000 €');
  console.log('    🔄 Maintenance Starter/Expert/Premium:  300 / 600 / 900 €/mois');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});

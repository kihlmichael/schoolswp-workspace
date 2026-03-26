#!/usr/bin/env node
/**
 * setup-notion-exit-strategy.js — Stratégie de sortie salarié → SASU
 *
 * Crée dans Notion la page :
 *   "🚪 Stratégie de Sortie — Salarié → SASU"
 *
 * Contenu :
 *   Audit de situation actuelle (checkboxes)
 *   Phase 1 — Pré-sortie intelligente (0-6 mois)
 *     · Rupture conventionnelle / ARE / ARCE
 *     · Construire la machine AVANT le départ
 *   Phase 2 — Création SASU au bon timing (Option A vs B)
 *   Phase 3 — Optimisation pendant ARE (cumul ARE + SASU)
 *     · Maintien ARE vs ARCE — comparaison calculée
 *     · Simulation cumul revenus SASU + ARE
 *   Phase 4 — Accélération maîtrisée (6-18 mois)
 *   KPI Transition
 *   Stratégie mentale
 *   Master checklist (50+ actions)
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

const rt  = (txt, opts = {}) => ({ type: 'text', text: { content: txt }, annotations: opts });
const rtb = (txt) => rt(txt, { bold: true });

const h1 = (t) => ({ object: 'block', type: 'heading_1', heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: [rt(t)] } });

const p   = (t = '') => ({ object: 'block', type: 'paragraph',          paragraph:         { rich_text: t ? [rt(t)] : [] } });
const bul = (t)      => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rt(t)] } });
const bulb = (t)     => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rtb(t)] } });
const num = (t)      => ({ object: 'block', type: 'numbered_list_item', numbered_list_item: { rich_text: [rt(t)] } });

const tod = (t, checked = false) => ({
  object: 'block', type: 'to_do',
  to_do: { rich_text: [rt(t)], checked },
});

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

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('🧭', 'Tu n\'es pas dans une logique "je démissionne". Tu es dans une logique de transition stratégique optimisée.', 'blue_background'),
    p(),
    qot('Stabilité > vitesse. Quitter intelligemment, c\'est quitter avec tous les filets de sécurité activés.'),
    p(),
  );

  // ── Vue d'ensemble ────────────────────────────────────────────────────────
  add(
    h2('🗺 Vue d\'ensemble — 4 phases'),
    p(),
    bul('Phase 1 — Pré-sortie intelligente   (0-6 mois avant départ)   : Maximiser le cadre de sortie'),
    bul('Phase 2 — Création SASU              (au bon timing)           : Option A ou B selon ta situation'),
    bul('Phase 3 — Optimisation pendant ARE   (J0 → J540 max)          : Maintien ARE + SASU en parallèle'),
    bul('Phase 4 — Accélération maîtrisée    (6-18 mois)               : De la transition à l\'indépendance stable'),
    p(),
    div(),
  );

  // ── Audit de situation ─────────────────────────────────────────────────────
  add(
    h1('🔍 Audit de ta situation actuelle'),
    p('Cocher ce qui s\'applique pour calibrer ta stratégie.'),
    p(),
    h3('Type de départ envisagé'),
    tod('Rupture conventionnelle (accord employeur + employé → ARE automatique)'),
    tod('Démission avec projet (reconversion — accès ARE sous conditions depuis 2019)'),
    tod('Fin de CDD (ARE automatique si ancienneté suffisante)'),
    tod('Licenciement économique / Plan de restructuration (ARE + reclassement)'),
    tod('Congé de reclassement ou congé de mobilité (salaire maintenu + formation)'),
    p(),
    h3('Situation actuelle'),
    tod('J\'ai calculé mes droits ARE estimés (durée + montant mensuel)'),
    tod('J\'ai calculé mes indemnités de rupture conventionnelle estimées'),
    tod('J\'ai ≥ 6 mois de charges perso en épargne personnelle'),
    tod('J\'ai ≥ 1 client potentiel identifié (ou prospect chaud)'),
    tod('Mon offre signature est définie et documentée'),
    p(),
    cal('💡', 'Si tu cloches sur 3+ cases → tu n\'es pas encore prêt à déclencher la Phase 2. Rester en Phase 1 jusqu\'à avoir tout coché.', 'yellow_background'),
    p(),
    div(),
  );

  // ── PHASE 1 ───────────────────────────────────────────────────────────────
  add(
    h1('🧱 PHASE 1 — Pré-sortie intelligente (0 à 6 mois avant)'),
    p(),
    cal('🎯', 'Objectif : sécuriser le maximum AVANT de partir. Chaque mois de préparation = un mois de sérénité en moins post-départ.', 'green_background'),
    p(),
  );

  // 1.1 Maximiser le cadre de sortie
  add(
    h2('1.1 Maximiser le cadre de départ'),
    p(),
  );

  add(
    tog('Rupture conventionnelle — Ce qu\'il faut savoir', [
      p('La rupture conventionnelle est la modalité de sortie la plus favorable dans ton cas.'),
      p(),
      bul('Accord mutuel : toi + employeur doivent signer'),
      bul('Délai de rétractation : 15 jours calendaires après signature'),
      bul('Homologation DREETS : 15 jours ouvrables (validation automatique si pas de refus)'),
      bul('Indemnité minimale : 1/4 de mois de salaire brut par année d\'ancienneté (0-10 ans)'),
      bul('Accès ARE : automatique dès J+1 de la rupture (après délai d\'attente légal)'),
      p(),
      cal('💡', 'Conseil : ne jamais démissionner si une rupture conventionnelle est possible. La démission supprime les droits ARE sauf cas de démission légitime reconnu par France Travail.', 'red_background'),
      p(),
      bul('Délai de carence ARE : 7 jours + délai différé lié aux indemnités de départ'),
      bul('Délai différé : indemnités ÷ 90.6 = nombre de jours de carence additionnels (max 75j)'),
    ]),
    p(),
    tog('Démission avec projet (reconversion) — Conditions 2025', [
      p('Possible depuis 2019 pour les salariés voulant créer une entreprise.'),
      p(),
      bul('Condition 1 : au moins 5 ans d\'ancienneté dans le secteur privé'),
      bul('Condition 2 : projet validé par la Commission Paritaire Interprofessionnelle Régionale (CPIR)'),
      bul('Condition 3 : dossier solide (business plan, offre définie, prévisionnel)'),
      bul('Délai instruction : 2-4 mois → prévoir large'),
      bul('Si validé : accès ARE comme une rupture conventionnelle'),
      p(),
      cal('⚠️', 'Si tu remplis les conditions de la rupture conventionnelle → ne pas passer par la démission avec projet. La RC est plus simple et plus rapide.', 'yellow_background'),
    ]),
    p(),
    tog('Congé de reclassement / mobilité — Le jackpot', [
      p('Réservé aux entreprises de plus de 1 000 salariés en cas de licenciement économique.'),
      p(),
      bul('Maintien du salaire pendant 4 à 12 mois'),
      bul('Accompagnement formation financé à 100%'),
      bul('Temps libre pour créer ton entreprise pendant que tu es encore payé'),
      bul('Accès ARE à l\'issue du congé'),
      p(),
      cal('🔥', 'Si cette option est disponible dans ta situation : c\'est le scénario optimal. Utiliser 100% du temps pour préparer la SASU et schoolsWP.', 'green_background'),
    ]),
    p(),
    h3('ARE — Estimer tes droits avant de partir'),
    p(),
    bul('Durée minimale travaillée pour ouvrir des droits : 6 mois dans les 24 derniers mois'),
    bul('Durée d\'indemnisation : 1 jour travaillé = 1 jour d\'ARE (plafonné selon âge)'),
    bul('Montant : 57% du salaire journalier de référence (SJR) + partie fixe'),
    bul('SJR = total salaires 12 derniers mois ÷ nombre de jours travaillés'),
    p(),
    tog('Simulation ARE — Exemple type', [
      p('Hypothèse : salaire brut 3 000 €/mois · ancienneté 4 ans'),
      p(''),
      p('SJR = 36 000 € ÷ 365 × (jours travaillés / 365) ≈ 98 €/jour'),
      p('Allocation journalière = 57% × 98 = 55,86 €/jour'),
      p('ARE mensuelle ≈ 55,86 × 30 = 1 675 €/mois net'),
      p(''),
      p('Durée droits : 4 ans ancienneté → 24 mois max (plafonné à 24 mois < 53 ans)'),
      p('→ Total droits = 1 675 € × 24 mois = 40 200 €'),
      p(''),
      cal('💡', 'Ton simulateur exact : France Travail → simulation.pole-emploi.fr. Utiliser avant de négocier la rupture.', 'blue_background'),
    ]),
    p(),
    div(),
  );

  // 1.2 Construire la machine
  add(
    h2('1.2 Construire la machine AVANT le départ'),
    p('Chaque heure de préparation pendant le salariat vaut 10 heures après la sortie.'),
    p(),
  );

  const actions_presortie = [
    ['Mois 1 — Offre et positionnement', [
      'Définir l\'offre signature (WordPress Learning System™ — CORE + PREMIUM)',
      'Documenter le positionnement formateurs WordPress dans Notion',
      'Créer la page "Offre Signature" sur schoolsWP.com (draft)',
      'Rédiger les CGV + template contrat prestation (avec LegalStart ou avocat)',
    ]],
    ['Mois 2 — Contenu décisionnel', [
      '5 articles décisionnels forts sur le cluster formateurs WordPress',
      'Page "Diagnostic WordPress Business" avec formulaire qualifiant',
      'CTA Audit sur les 10 articles à plus fort trafic',
      'Créer la lead magnet : "Checklist WordPress Learning System™"',
    ]],
    ['Mois 3 — Pipeline et prospection douce', [
      '2 posts LinkedIn / semaine sur l\'angle formateurs WordPress',
      'Entrer en contact avec 5 formateurs en ligne (entretiens de découverte gratuits)',
      'Rejoindre 3 communautés de formateurs en ligne (Facebook, LinkedIn, Slack)',
      '1 premier devis envoyé à un prospect (même sans SASU — facturable en micro ou perso)',
    ]],
    ['Mois 4-6 — Validation et sécurisation', [
      '1 mission vendue et livrée (validation prix + temps réel)',
      'Estimation définitive des droits ARE avec simulation France Travail',
      'Rendez-vous avec expert-comptable pour préparer la SASU',
      'Déclencher la rupture conventionnelle quand les signaux GO sont verts',
    ]],
  ];

  actions_presortie.forEach(([titre, actions]) => {
    add(
      tog(titre, [
        ...actions.map((a) => tod(a)),
      ]),
      p(),
    );
  });

  add(
    cal('⚠️', 'Zéro dispersion. Pas de 10 offres. Pas de 5 projets parallèles. 1 offre. 1 niche. 1 tunnel. Tout le reste attend.', 'red_background'),
    p(),
    div(),
  );

  // ── PHASE 2 ───────────────────────────────────────────────────────────────
  add(
    h1('🏗 PHASE 2 — Création SASU au bon timing'),
    p(),
    h2('Option A — Créer APRÈS validation des droits ARE'),
    p(),
    bul('Scénario : sortie → ouverture droits France Travail → puis création SASU'),
    bul('Avantage : droits ARE 100% sécurisés avant toute action'),
    bul('Délai : 3-6 semaines entre la rupture et la création SASU'),
    bul('Recommandé si : pas encore de client signé, trésorerie perso < 6 mois'),
    p(),
    h2('Option B — Créer JUSTE AVANT la sortie'),
    p(),
    bul('Scénario : SASU créée pendant le préavis (si préavis > 0) ou avant signature rupture'),
    bul('Avantage : démarrer les activités immédiatement sans interruption'),
    bul('Condition : avoir un contrat signé ou une visibilité forte sur le pipeline'),
    bul('Risque : si les droits ARE sont refusés ou réduits, la SASU n\'a pas encore de CA'),
    p(),
    cal('🎯', 'Pour un profil prudent et structuré : Option A recommandée. Sécuriser les droits, puis créer la SASU dans la foulée.', 'green_background'),
    p(),
    tog('Chronologie Option A — Détail semaine par semaine', [
      bul('S1-S2  : Signature de la rupture conventionnelle'),
      bul('S3-S4  : Délai de rétractation (15 jours cal.)'),
      bul('S5-S8  : Instruction DREETS (15 jours ouvr. + marge)'),
      bul('S9     : Homologation → fin du contrat de travail'),
      bul('S10    : Inscription France Travail (dans les 12j)'),
      bul('S11-S12: Délai de carence (7j + différé indemnités)'),
      bul('S13    : Premiers versements ARE'),
      bul('S14-S16: Création SASU (statuts → RCS → SIRET)'),
      bul('S17    : Déclaration d\'activité à France Travail → ARE maintenu partiellement'),
    ]),
    p(),
    div(),
  );

  // ── PHASE 3 ───────────────────────────────────────────────────────────────
  add(
    h1('💰 PHASE 3 — Optimisation revenus pendant ARE'),
    p(),
    cal('🎯', 'Objectif : utiliser l\'ARE comme filet de sécurité sans le couper prématurément.', 'green_background'),
    p(),
  );

  add(
    h2('Cumul ARE + Revenus SASU — Comment ça fonctionne'),
    p(),
    bul('Obligatoire : déclarer à France Travail tout revenu tiré de la SASU (salaire ou dividendes)'),
    bul('Le cumul est autorisé mais partiel : plus tu gagnes, moins France Travail verse'),
    bul('Résultat : tes droits ne sont pas perdus, juste étalés dans le temps'),
    bul('Avantage majeur : si CA SASU faible un mois → ARE complète ce mois-là'),
    p(),
    tog('Simulation cumul ARE + revenus SASU', [
      p('Hypothèse : ARE mensuelle = 1 675 € · Revenus SASU mois = 3 500 €'),
      p(''),
      p('Formule simplifiée de réduction :'),
      p('Jours indemnisés = 30 – (revenus SASU / allocation journalière)'),
      p('= 30 – (3 500 / 55,86) = 30 – 62,6 = ... → 0 jours indemnisés ce mois-là'),
      p(''),
      p('Si revenus SASU = 1 000 € (mois calme) :'),
      p('Jours indemnisés = 30 – (1 000 / 55,86) = 30 – 17,9 = ~12 jours'),
      p('ARE perçue = 12 × 55,86 = 670 €  →  Revenu total = 1 000 + 670 = 1 670 €'),
      p(''),
      p('Si revenus SASU = 0 € (mois de lancement) :'),
      p('Jours indemnisés = 30  →  ARE complète = 1 675 €'),
      p(''),
      cal('💡', 'Les jours non indemnisés s\'ajoutent à tes droits restants → la durée d\'ARE s\'étend automatiquement. Tu ne "perds" pas ces jours.', 'green_background'),
    ]),
    p(),
  );

  add(
    h2('ARCE vs Maintien ARE — Comparaison'),
    p(),
  );

  add(
    tog('ARCE — Capital immédiat (60% des droits en 2 fois)', [
      p('L\'ARCE verse 60% de tes droits ARE restants en capital.'),
      p(''),
      p('Exemple : droits restants = 40 200 €'),
      p('ARCE = 40 200 × 60% = 24 120 €'),
      p('  · 1er versement à la création : 12 060 €'),
      p('  · 2e versement à M6 : 12 060 €'),
      p(''),
      bul('✅  Avantages : capital immédiat disponible, pas de déclaration mensuelle, visibilité financière'),
      bul('⚠️  Inconvénients : pas de filet si CA s\'effondre, capital consommé sans retour'),
      bul('⚠️  Pour qui : profils avec pipeline solide et trésorerie déjà constituée'),
    ]),
    p(),
    tog('Maintien ARE partiel — Le filet intelligent', [
      p('Tu gardes les droits ARE mais ils sont réduits selon tes revenus SASU.'),
      p(''),
      bul('✅  Avantages : filet de sécurité variable selon CA, droits prolongés'),
      bul('✅  Si mois calme → ARE complète, si mois fort → zéro ARE mais droits conservés'),
      bul('✅  Durée totale des droits étendue (idéal si ramp-up progressif)'),
      bul('⚠️  Inconvénients : obligation de déclarer chaque mois, règles complexes'),
      bul('⚠️  Attention : salaire SASU = déclaré. Dividendes = non déclarés à France Travail (A CONFIRMER avec l\'EC)'),
    ]),
    p(),
    cal('🎯', 'Pour ton profil (prudent, construction progressive, CA en ramp-up) : Maintien ARE souvent plus intelligent que l\'ARCE.', 'green_background'),
    p(),
  );

  add(
    h2('Règles ARE + SASU — Points critiques'),
    p(),
    bul('Déclarer la création de la SASU à France Travail dès l\'immatriculation'),
    bul('Déclarer les revenus SASU mensuellement (salaire président = revenu à déclarer)'),
    bul('Ne pas verser de salaire les mois où tu veux toucher l\'ARE complète (légal si planifié)'),
    bul('Les dividendes : non soumis à déclaration ARE selon jurisprudence actuelle (valider avec EC)'),
    bul('ARE + Salaire SASU : le cumul peut être fait proprement si salaire < 70% du SJR'),
    p(),
    cal('⚠️', 'Cette section décrit des principes généraux. Valider obligatoirement avec un expert-comptable et/ou un conseiller France Travail avant de prendre toute décision.', 'red_background'),
    p(),
    div(),
  );

  // ── PHASE 4 ───────────────────────────────────────────────────────────────
  add(
    h1('🚀 PHASE 4 — Accélération maîtrisée (6 à 18 mois)'),
    p(),
    cal('🎯', 'Objectif : passer de "en transition" à "indépendant stable". Progressivement, pas d\'un coup.', 'green_background'),
    p(),
  );

  add(
    h2('Mois 1-3 — Structurer'),
    p(),
    num('Signer 2 à 3 premiers clients (CORE ou Audit → CORE)'),
    num('Créer le template onboarding client (Notion ou PDF)'),
    num('Formaliser la méthode 4 phases documentée'),
    num('Mesurer le temps réel sur chaque projet'),
    num('Installer la récurrence Maintenance sur chaque livraison'),
    p(),
    h2('Mois 4-6 — Capitaliser'),
    p(),
    num('Transformer client 1 en cas d\'étude anonymisé → publier'),
    num('Ajuster le pricing si taux closing > 50% (sous-facturation probable)'),
    num('Augmenter le volume contenu schoolsWP (20 articles cluster formateurs)'),
    num('MRR Maintenance cible : 600 – 900 €/mois'),
    num('Réduire progressivement la dépendance à l\'ARE à mesure que le CA monte'),
    p(),
    h2('Mois 7-12 — Stabiliser'),
    p(),
    num('CA mensuel stable ≥ 8 000 € → ajuster salaire SASU'),
    num('1er bilan SASU avec EC → optimisation fiscale réelle'),
    num('Viser 1 client PREMIUM (6 000 – 10 000 €)'),
    num('Pipeline autonome : ≥ 3 prospects qualifiés en permanence via schoolsWP'),
    num('Décision : rester solo ou 1er partenaire régulier ?'),
    p(),
    h2('Mois 13-18 — Accélérer'),
    p(),
    num('Positionnement renforcé : citations LLM, position SERP formateurs WordPress'),
    num('MRR total (Maintenance + SEO) : 1 500 – 3 000 €/mois'),
    num('Décision structurelle : holding envisageable si bénéfice > 60 000 €'),
    num('Offre signature consolidée, testimonials clients publiés'),
    num('schoolsWP = machine d\'autorité autonome (leads entrants sans prospection active)'),
    p(),
    div(),
  );

  // ── KPI ───────────────────────────────────────────────────────────────────
  add(
    h1('📊 KPI Transition — Indicateurs à surveiller'),
    p(),
    bul('Trésorerie SASU       →  ≥ 6 mois de charges fixes à M12'),
    bul('Clients actifs        →  ≥ 3 clients simultanément à M6'),
    bul('CA mensuel stable     →  Atteindre le seuil de sécurité (≥ point mort sans ARE)'),
    bul('Dépendance ARE        →  Réduite progressivement (0% à M18)'),
    bul('MRR Maintenance       →  ≥ 1 500 €/mois à M12'),
    bul('Leads entrants SEO    →  ≥ 3/mois via schoolsWP à M9'),
    bul('Taux closing devis    →  > 25% (si > 50% → prix trop bas)'),
    bul('Temps réel/projet     →  < 40h/projet CORE (rentabilité horaire > 80 €/h)'),
    p(),
    div(),
  );

  // ── Stratégie mentale ─────────────────────────────────────────────────────
  add(
    h1('🧠 Stratégie mentale — Les pièges psychologiques'),
    p(),
    h2('Ce qu\'il faut éviter'),
    p(),
    bul('❌  L\'excitation du lancement → prendre n\'importe quel client pour "démarrer"'),
    bul('❌  La sur-expansion rapide → multiplier les offres, les niches, les canaux'),
    bul('❌  Le syndrome "je prends tout client" → 1 mauvais client = 6 semaines perdues'),
    bul('❌  Comparer sa progression à des entrepreneurs en année 3+ (biais de survie)'),
    bul('❌  Regarder son compte bancaire quotidiennement les 3 premiers mois'),
    bul('❌  Confondre activité (tâches) et productivité (résultats qui comptent)'),
    p(),
    h2('Ce qu\'il faut cultiver'),
    p(),
    bulb('Stabilité > vitesse — 1 client premium vaut mieux que 3 clients médiocres'),
    bulb('Système > effort — schoolsWP travaille quand tu livres les projets'),
    bulb('Patience > panic — les droits ARE sont là pour financer la montée en puissance'),
    bulb('Décision froide — chaque client passe les 7 questions de qualification'),
    bulb('Revue hebdo — 30 min chaque lundi pour ajuster, pas pour paniquer'),
    p(),
    qot('"Je n\'ai pas besoin de 10 clients. J\'ai besoin d\'un système qui me ramène 2-3 clients premium réguliers. Tout le reste est du bruit."'),
    p(),
    div(),
  );

  // ── Position à 18 mois ───────────────────────────────────────────────────
  add(
    h1('🏢 Position idéale à 18 mois'),
    p(),
    bul('SASU rentable : CA ≥ 10 000 €/mois · MRR ≥ 1 500 €'),
    bul('schoolsWP : autorité reconnue sur le segment formateurs WordPress'),
    bul('Offre claire : 1 offre signature (CORE + PREMIUM), 0 dispersion'),
    bul('Clients qualifiés : 3-5 actifs ou récurrents, tous dans la niche formateurs'),
    bul('Système automatisé : pipeline SEO → qualification → onboarding → livraison'),
    bul('Liberté décisionnelle : refuser un client sans stress financier'),
    p(),
    cal('🎯', '18 mois d\'exécution rigoureuse = indépendance durable. Pas 18 mois d\'enthousiasme. 18 mois de système.', 'green_background'),
    p(),
    div(),
  );

  // ── Master checklist ──────────────────────────────────────────────────────
  add(
    h1('✅ Master Checklist — Transition complète'),
    p('Cocher au fur et à mesure. La progression se lit ici.'),
    p(),
    h2('Phase 1 — Pré-sortie'),
    p(),
    h3('Droits et cadre juridique'),
    tod('Estimation droits ARE réalisée (simulation France Travail)'),
    tod('Estimation indemnités rupture conventionnelle calculée'),
    tod('Type de sortie déterminé (rupture / démission avec projet / licenciement)'),
    tod('Rendez-vous prévu avec RH ou conseiller France Travail'),
    p(),
    h3('Offre et positionnement'),
    tod('Offre signature documentée (WordPress Learning System™)'),
    tod('Positionnement formateurs défini et écrit'),
    tod('Page offre en draft sur schoolsWP.com'),
    tod('CGV rédigées et validées'),
    tod('Template contrat prestation prêt'),
    p(),
    h3('Contenu et pipeline'),
    tod('5 articles décisionnels formateurs publiés'),
    tod('CTA Audit sur les 10 articles stratégiques'),
    tod('Page "Diagnostic WordPress Business" créée'),
    tod('Lead magnet créée (checklist ou guide)'),
    tod('Formulaire qualifiant installé (3 questions minimum)'),
    tod('2 posts LinkedIn / semaine activés'),
    p(),
    h3('Validation marché'),
    tod('3 entretiens de découverte réalisés'),
    tod('1 devis envoyé à prix cible'),
    tod('1 mission signée et livrée'),
    tod('Temps réel mesuré sur premier projet'),
    tod('Pricing validé (pas bradé)'),
    p(),
    h2('Phase 2 — Création SASU'),
    p(),
    tod('Expert-comptable choisi et briefé'),
    tod('Option A ou B décidée (après/avant validation ARE)'),
    tod('SASU immatriculée (SIRET obtenu)'),
    tod('Compte bancaire pro ouvert'),
    tod('RC Pro souscrite'),
    tod('Logiciel facturation configuré'),
    tod('Déclaration à France Travail faite'),
    p(),
    h2('Phase 3 — Pendant ARE'),
    p(),
    tod('Stratégie cumul ARE choisie (maintien partiel ou ARCE)'),
    tod('Calendrier déclarations France Travail configuré (mensuel)'),
    tod('Salaire SASU ajusté pour optimiser le cumul'),
    tod('EC informé de la stratégie de cumul'),
    tod('Sous-compte "Fiscal" créé et alimenté (40% règle)'),
    p(),
    h2('Phase 4 — Accélération'),
    p(),
    tod('2 premiers clients CORE signés'),
    tod('Template onboarding créé'),
    tod('MRR Maintenance ≥ 300 €/mois (1er client récurrent)'),
    tod('1er cas d\'étude anonymisé publié'),
    tod('CA mensuel ≥ point mort sans dépendre de l\'ARE'),
    tod('MRR ≥ 1 500 €/mois (M12)'),
    tod('1 client PREMIUM signé'),
    tod('Dépendance ARE = 0% (M18 max)'),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Stratégie de Sortie Salarié → SASU\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs — ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '🚪' },
    properties: {
      title: { title: [{ text: { content: '🚪 Stratégie de Sortie — Salarié → SASU' } }] },
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
  console.log('✅  Stratégie de sortie documentée !\n');
  console.log('  🚪  Page : "🚪 Stratégie de Sortie — Salarié → SASU"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Structure :');
  console.log('    🔍  Audit de situation actuelle (checkboxes)');
  console.log('    🧱  Phase 1 — Pré-sortie (0-6 mois) + plan mois par mois');
  console.log('          · Rupture conventionnelle vs démission avec projet vs congé reclassement');
  console.log('          · Simulation ARE (exemple chiffré)');
  console.log('          · Actions par mois (M1 à M6)');
  console.log('    🏗   Phase 2 — Création SASU (Option A vs B + chronologie semaine/semaine)');
  console.log('    💰  Phase 3 — Cumul ARE + SASU (simulation + ARCE vs maintien)');
  console.log('    🚀  Phase 4 — Accélération 6-18 mois (actions par trimestre)');
  console.log('    📊  KPI Transition (8 indicateurs)');
  console.log('    🧠  Stratégie mentale (pièges + posture)');
  console.log('    🏢  Position idéale à 18 mois');
  console.log('    ✅  Master checklist 50+ actions cochables');
  console.log('');
  console.log('  Point clé de la stratégie :');
  console.log('    Option A recommandée : sécuriser l\'ARE AVANT de créer la SASU');
  console.log('    Maintien ARE > ARCE pour un profil prudent et progressif');
  console.log('    Phase 1 active pendant le salariat = 6 mois de préparation');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});

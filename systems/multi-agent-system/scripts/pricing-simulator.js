#!/usr/bin/env node
/**
 * pricing-simulator.js — Simulateur de prix SASU WordPress schoolsWP
 *
 * 1 offre signature · 2 niveaux.
 * Calcule le prix optimal pour un prospect en 2 minutes.
 * Aucune dépendance npm — Node 18+.
 *
 * ┌──────────────────────────────────────────────────────────────┐
 * │  🥇 CORE     WordPress Business System   3 000 – 6 000 €    │
 * │  🥈 PREMIUM  WordPress Business System   6 000 – 10 000 €   │
 * └──────────────────────────────────────────────────────────────┘
 *
 * Usage :
 *   node scripts/pricing-simulator.js
 *   node scripts/pricing-simulator.js --export     JSON pour Notion
 *   node scripts/pricing-simulator.js --silent     Sans bannière
 */

import * as readline from 'node:readline';

const args   = process.argv.slice(2);
const EXPORT = args.includes('--export');
const SILENT = args.includes('--silent');

// ─── ANSI ─────────────────────────────────────────────────────────────────────

const bold  = (s) => `\x1b[1m${s}\x1b[0m`;
const dim   = (s) => `\x1b[2m${s}\x1b[0m`;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const blue  = (s) => `\x1b[34m${s}\x1b[0m`;
const red   = (s) => `\x1b[31m${s}\x1b[0m`;
const yel   = (s) => `\x1b[33m${s}\x1b[0m`;
const cya   = (s) => `\x1b[36m${s}\x1b[0m`;
const mag   = (s) => `\x1b[35m${s}\x1b[0m`;

const sep = (ch = '─', n = 58) => ch.repeat(n);

// ─── Offres ────────────────────────────────────────────────────────────────────

const OFFRES = {
  CORE: {
    emoji:    '🥇',
    label:    'WordPress Business System — CORE',
    mini:     3000,
    maxi:     6000,
    duree:    '3 à 5 semaines',
    phases: [
      'Phase 1 · Audit stratégique (architecture, tunnel, SEO, plugins, automatisation)',
      'Phase 2 · Structuration (stack, CRM, tunnel, automatisations clés)',
      'Phase 3 · Optimisation (CTA, performance, SEO structure, email auto)',
      'Phase 4 · Transmission (formation enregistrée, documentation, autonomie)',
    ],
    rec_label:  'Maintenance Starter — 300 €/mois (optionnel)',
    rec_amount: 300,
  },
  PREMIUM: {
    emoji:    '🥈',
    label:    'WordPress Business System — PREMIUM',
    mini:     6000,
    maxi:     10000,
    duree:    '6 à 10 semaines',
    phases: [
      'CORE complet (4 phases incluses)',
      'Optimisation SEO avancée + stratégie contenu cluster',
      'Intégration booking ou LMS (Tutor LMS, Calendly, ThriveCart…)',
      '3 mois de suivi mensuel (audit + ajustements)',
    ],
    rec_label:  'Maintenance Expert — 600 €/mois (conseillé)',
    rec_amount: 600,
  },
};

// ─── Questions ─────────────────────────────────────────────────────────────────

const QUESTIONS = [

  // Q1 — Profil client
  {
    id:   'profil',
    text: 'Profil du prospect ?',
    info: 'Choisir ce qui correspond le mieux à la situation.',
    options: [
      { key: '1', label: 'Freelance / solopreneur — site existant, besoin de clarté',
        value: { premium_pts: 0 } },
      { key: '2', label: 'Formateur / créateur de cours en ligne — veut automatiser',
        value: { premium_pts: 1 } },
      { key: '3', label: 'Consultant / coach — tunnel + CRM + autorité SEO',
        value: { premium_pts: 1 } },
      { key: '4', label: 'Entrepreneur ambitieux — LMS + booking + SEO cluster',
        value: { premium_pts: 3 } },
    ],
  },

  // Q2 — Situation actuelle
  {
    id:   'situation',
    text: 'Situation du site actuel ?',
    options: [
      { key: '1', label: 'Site existant mal structuré — besoin de restructuration',
        value: { premium_pts: 0, complexity_base: 1.00 } },
      { key: '2', label: 'Site existant + SEO faible — besoin d\'autorité contenu',
        value: { premium_pts: 1, complexity_base: 1.10 } },
      { key: '3', label: 'Site existant + veut ajouter LMS ou booking',
        value: { premium_pts: 2, complexity_base: 1.15 } },
      { key: '4', label: 'Refonte complète — nouveau système de A à Z',
        value: { premium_pts: 2, complexity_base: 1.20 } },
    ],
  },

  // Q3 — Modules PREMIUM inclus (multi)
  {
    id:    'modules',
    text:  'Modules additionnels à inclure ? (sélection multiple, 0 si aucun)',
    info:  'Ces modules font basculer vers le PREMIUM.',
    multi: true,
    options: [
      { key: '0', label: 'Aucun — CORE suffit',                  value: { premium_pts: 0 } },
      { key: '1', label: 'SEO avancé + stratégie cluster',       value: { premium_pts: 2 } },
      { key: '2', label: 'LMS (formation en ligne)',              value: { premium_pts: 2 } },
      { key: '3', label: 'Booking / réservation (Calendly…)',     value: { premium_pts: 1 } },
      { key: '4', label: 'Suivi mensuel 3 mois post-livraison',  value: { premium_pts: 1 } },
    ],
  },

  // Q4 — Budget signalé
  {
    id:   'budget',
    text: 'Budget mentionné par le prospect ?',
    options: [
      { key: '1', label: 'Non évoqué / inconnu',
        value: { budget_ok: true, budget_signal: 'unknown' } },
      { key: '2', label: 'Moins de 3 000 € — sous le seuil CORE',
        value: { budget_ok: false, budget_signal: 'low' } },
      { key: '3', label: '3 000 – 6 000 €',
        value: { budget_ok: true, budget_signal: 'core' } },
      { key: '4', label: '6 000 – 10 000 €',
        value: { budget_ok: true, budget_signal: 'premium', premium_pts: 2 } },
      { key: '5', label: 'Plus de 10 000 €',
        value: { budget_ok: true, budget_signal: 'premium', premium_pts: 3 } },
    ],
  },

  // Q5 — Urgence
  {
    id:   'urgence',
    text: 'Niveau d\'urgence ?',
    options: [
      { key: '1', label: 'Aucune urgence — démarrage flexible',    value: { urg_mult: 1.00 } },
      { key: '2', label: 'Modérée — démarrage dans 4-8 semaines', value: { urg_mult: 1.00 } },
      { key: '3', label: 'Urgente — démarrage dans 2-3 semaines', value: { urg_mult: 1.15 } },
      { key: '4', label: 'Immédiate — cette semaine',             value: { urg_mult: 1.20 } },
    ],
  },

  // Q6 — Complexité
  {
    id:   'complexite',
    text: 'Complexité technique estimée ?',
    options: [
      { key: '1', label: 'Légère — stack standard, peu de custom',          value: { cplx_mult: 1.00 } },
      { key: '2', label: 'Moyenne — quelques intégrations API / CRM',       value: { cplx_mult: 1.15 } },
      { key: '3', label: 'Élevée — automatisations + intégrations multiples', value: { cplx_mult: 1.25 } },
      { key: '4', label: 'Très élevée — migrations, sur-mesure, n8n avancé', value: { cplx_mult: 1.35 } },
    ],
  },

  // Q7 — Récurrence
  {
    id:   'recurrence',
    text: 'Récurrence mensuelle à proposer ?',
    options: [
      { key: '1', label: 'Aucune',                               value: { rec_amount: 0,   rec_label: null } },
      { key: '2', label: 'Maintenance Starter — 300 €/mois',    value: { rec_amount: 300,  rec_label: 'Maintenance Starter' } },
      { key: '3', label: 'Maintenance Expert — 600 €/mois',     value: { rec_amount: 600,  rec_label: 'Maintenance Expert' } },
      { key: '4', label: 'Maintenance + SEO Solo — 800 €/mois', value: { rec_amount: 800,  rec_label: 'Maintenance + SEO Solo' } },
    ],
  },

  // Q8 — Score fit
  {
    id:   'fit',
    text: 'Score fit client (1-5) ?',
    info: '5 = prospect idéal · 1 = mauvais fit',
    options: [
      { key: '1', label: '1 — Faible fit (hors cible)',       value: { score_fit: 1 } },
      { key: '2', label: '2 — Fit moyen',                     value: { score_fit: 2 } },
      { key: '3', label: '3 — Bon fit',                       value: { score_fit: 3 } },
      { key: '4', label: '4 — Top fit',                       value: { score_fit: 4 } },
      { key: '5', label: '5 — Parfait (cible idéale)',        value: { score_fit: 5 } },
    ],
  },

];

// ─── readline ──────────────────────────────────────────────────────────────────

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (p) => new Promise((r) => rl.question(p, r));

async function askQ(q, idx, total) {
  console.log('');
  console.log(dim(`  Question ${idx}/${total}`));
  if (q.info) console.log(dim(`  ${q.info}`));
  console.log(bold(`\n  ${q.text}`));
  console.log('');

  q.options.forEach((o) => console.log(`  ${cya(o.key + '.')} ${o.label}`));

  if (q.multi) console.log(dim('\n  (plusieurs choix, ex : 1 3  ou  0 pour aucun)'));

  console.log('');
  const input = await ask('  → ');
  const keys  = input.trim().split(/\s+/);

  if (q.multi) {
    const chosen = q.options.filter((o) => keys.includes(o.key));
    return chosen.length ? chosen : [q.options[0]];
  }
  return [q.options.find((o) => o.key === keys[0]) || q.options[0]];
}

// ─── Calcul ────────────────────────────────────────────────────────────────────

function compute(answers) {
  let premium_pts   = 0;
  let urg_mult      = 1.00;
  let cplx_base     = 1.00;  // from situation
  let cplx_mult     = 1.00;  // from complexite question
  let rec_amount    = 0;
  let rec_label     = null;
  let score_fit     = 3;
  let budget_ok     = true;
  let budget_signal = 'unknown';

  for (const chosen of Object.values(answers)) {
    for (const opt of chosen) {
      const v = opt.value;
      if (v.premium_pts)   premium_pts   += v.premium_pts;
      if (v.urg_mult)      urg_mult       = v.urg_mult;
      if (v.cplx_mult)     cplx_mult      = v.cplx_mult;
      if (v.complexity_base) cplx_base    = v.complexity_base;
      if (v.rec_amount !== undefined) rec_amount = v.rec_amount;
      if (v.rec_label !== undefined)  rec_label  = v.rec_label;
      if (v.score_fit !== undefined)  score_fit  = v.score_fit;
      if (v.budget_ok !== undefined)  budget_ok  = v.budget_ok;
      if (v.budget_signal)            budget_signal = v.budget_signal;
    }
  }

  // Décision niveau : ≥ 4 pts → PREMIUM
  const level  = premium_pts >= 4 ? 'PREMIUM' : 'CORE';
  const offre  = OFFRES[level];

  // Prix ajusté
  const mult  = urg_mult * cplx_mult * cplx_base;
  const mini  = Math.round(offre.mini * mult / 100) * 100;
  const maxi  = Math.round(offre.maxi * mult / 100) * 100;

  // Valeur 12 mois
  const val12_mini = mini + rec_amount * 12;
  const val12_maxi = maxi + rec_amount * 12;

  return {
    level, offre,
    mini_base: offre.mini,
    maxi_base: offre.maxi,
    mini, maxi,
    urg_mult, cplx_mult, cplx_base, mult,
    premium_pts,
    rec_amount, rec_label,
    val12_mini, val12_maxi,
    score_fit,
    budget_ok, budget_signal,
  };
}

// ─── Affichage ─────────────────────────────────────────────────────────────────

function printResult(r) {
  const { offre, level, mini, maxi, urg_mult, cplx_mult, cplx_base,
          mult, premium_pts, rec_amount, rec_label,
          val12_mini, val12_maxi, score_fit, budget_ok, budget_signal } = r;

  const color = level === 'PREMIUM' ? blue : green;

  console.log('');
  console.log(bold(sep('━')));
  console.log(bold(`  RÉSULTAT — ${offre.emoji} ${offre.label}`));
  console.log(bold(sep('━')));
  console.log('');

  // Budget warning
  if (!budget_ok) {
    console.log(yel(`  ⚠️  Budget signalé sous le seuil CORE (< 3 000 €).`));
    console.log(yel(`     Commencer par l'Audit seul (1 200 €) pour créer la confiance.`));
    console.log('');
  }

  // Prix
  const range = `${mini.toLocaleString('fr-FR')} – ${maxi.toLocaleString('fr-FR')} €`;
  console.log(`  ${bold('💶 Prix recommandé :')}  ${color(bold(range))}`);
  console.log(`  ${bold('⏱  Durée :')}            ${offre.duree}`);
  console.log('');

  // Modificateurs
  const mods = [];
  if (cplx_base > 1.00) mods.push(`situation ×${cplx_base.toFixed(2)}`);
  if (urg_mult > 1.00)  mods.push(`urgence ×${urg_mult.toFixed(2)}`);
  if (cplx_mult > 1.00) mods.push(`complexité ×${cplx_mult.toFixed(2)}`);

  if (mods.length > 0) {
    console.log(`  ${dim('Modificateurs :')} ${yel(mods.join(' · '))}  ${dim('(total ×' + mult.toFixed(2) + ')')}`);
    console.log(`  ${dim('Prix base :')} ${r.mini_base.toLocaleString('fr-FR')} – ${r.maxi_base.toLocaleString('fr-FR')} €`);
    console.log('');
  }

  // Score premium
  console.log(`  ${dim('Score PREMIUM :')} ${premium_pts} pts ${premium_pts >= 4 ? '→ ' + mag('PREMIUM déclenché') : '→ ' + green('CORE recommandé')}`);
  console.log('');

  // Phases incluses
  console.log(`  ${bold('📦 Phases incluses :')}`);
  offre.phases.forEach((ph) => console.log(`     • ${ph}`));
  console.log('');

  // Récurrence
  if (rec_amount > 0 && rec_label) {
    console.log(`  ${bold('🔄 Récurrence :')} ${cya(rec_label)}`);
    console.log(`  ${bold('📈 Valeur 12 mois :')} ${cya(val12_mini.toLocaleString('fr-FR') + ' – ' + val12_maxi.toLocaleString('fr-FR') + ' €')}`);
  } else {
    console.log(`  ${dim('Récurrence : aucune (possibilité d\'ajouter ' + offre.rec_label + ')')}`);
  }
  console.log('');

  // Notion copy
  const fitLabel = score_fit >= 5 ? '🔥 Parfait'
    : score_fit >= 4 ? '🟢 Top Fit'
    : score_fit >= 3 ? '🟡 Bon Fit'
    : score_fit >= 2 ? '🟠 Moyen'
    : '⚫ Faible';

  const prix_moyen = Math.round((mini + maxi) / 2 / 100) * 100;

  console.log(sep());
  console.log(bold('  📋 NOTION — À copier dans la fiche Prospect'));
  console.log(sep());
  console.log('');
  console.log(`  Offre cible     : ${level}`);
  console.log(`  Prix proposé    : ${prix_moyen.toLocaleString('fr-FR')} €`);
  console.log(`  Prix mini       : ${mini.toLocaleString('fr-FR')} €`);
  console.log(`  Prix maxi       : ${maxi.toLocaleString('fr-FR')} €`);
  console.log(`  Récurrence      : ${rec_amount > 0 ? 'Oui' : 'Non'}`);
  console.log(`  Montant rép.    : ${rec_amount > 0 ? rec_amount + ' €/mois' : '—'}`);
  console.log(`  Score fit       : ${score_fit} — ${fitLabel}`);
  console.log('');

  // Conseils
  console.log(sep());
  console.log(bold('  💡 Conseils'));
  console.log(sep());
  console.log('');

  if (budget_signal === 'low') {
    console.log(`  ${yel('→')} Proposer l'Audit seul (1 200 €) comme porte d'entrée.`);
    console.log(`  ${yel('→')} Présenter l'Audit comme "étape 0" — pas un coût, une décision éclairée.`);
    console.log(`  ${yel('→')} Upsell naturel : Audit → CORE si le rapport convainc.`);
  } else if (level === 'CORE') {
    console.log(`  ${green('→')} Mentionner l'option PREMIUM dès le devis — "si le scope grandit".`);
    console.log(`  ${green('→')} Inclure 1 session onboarding (2h) dans le prix — réduit le SAV.`);
    console.log(`  ${green('→')} Proposer Maintenance Starter à la signature — MRR dès le premier jour.`);
  } else {
    console.log(`  ${blue('→')} Décomposer en jalons facturés : CORE puis modules PREMIUM.`);
    console.log(`  ${blue('→')} Acompte 40% à la signature — filtre les prospects non sérieux.`);
    console.log(`  ${blue('→')} Présenter la valeur 12 mois (${val12_mini.toLocaleString('fr-FR')} – ${val12_maxi.toLocaleString('fr-FR')} €) pas juste le projet.`);
    console.log(`  ${blue('→')} Inclure Maintenance Expert post-livraison — MRR qualifié.`);
  }

  if (urg_mult > 1.10) {
    console.log(`  ${yel('→')} Urgence élevée — le majorer : "planning dédié disponible cette semaine".`);
  }

  if (score_fit <= 2) {
    console.log('');
    console.log(`  ${red('⚠️  Score fit faible — reconsidérer avant de proposer l\'offre.')}`);
    console.log(`  ${red('   Ce prospect n\'est peut-être pas dans la cible WordPress Business System.')}`);
  }

  console.log('');
  console.log(bold(sep('━')));
  console.log('');

  // Export JSON
  if (EXPORT) {
    const json = {
      offre_cible:          level,
      prix_propose:         prix_moyen,
      prix_mini:            mini,
      prix_maxi:            maxi,
      recurrence:           rec_amount > 0,
      montant_recurrence:   rec_amount,
      label_recurrence:     rec_label,
      valeur_12_mois_mini:  val12_mini,
      valeur_12_mois_maxi:  val12_maxi,
      score_fit,
      label_fit:            fitLabel,
      score_premium_pts:    premium_pts,
    };
    console.log(sep());
    console.log(bold('  📤 JSON'));
    console.log(sep());
    console.log('');
    console.log(JSON.stringify(json, null, 2).split('\n').map((l) => '  ' + l).join('\n'));
    console.log('');
  }
}

// ─── Bannière ──────────────────────────────────────────────────────────────────

function banner() {
  if (SILENT) return;
  console.clear();
  console.log('');
  console.log(bold(green('  ┌─────────────────────────────────────────────────────┐')));
  console.log(bold(green('  │   💶 schoolsWP · Simulateur prix SASU               │')));
  console.log(bold(green('  │   1 offre signature · 2 niveaux · 2 minutes         │')));
  console.log(bold(green('  └─────────────────────────────────────────────────────┘')));
  console.log('');
  console.log(dim('  Je ne crée pas des sites.'));
  console.log(dim('  Je structure des systèmes WordPress rentables et automatisés.'));
  console.log('');
  console.log(`  ${green('🥇 CORE    ')}  ${dim('3 000 – 6 000 €')}    4 phases · 3-5 semaines`);
  console.log(`  ${blue('🥈 PREMIUM ')}  ${dim('6 000 – 10 000 €')}   CORE + SEO cluster + LMS + suivi`);
  console.log('');
  console.log(sep());
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  banner();

  const answers = {};
  for (let i = 0; i < QUESTIONS.length; i++) {
    const q = QUESTIONS[i];
    answers[q.id] = await askQ(q, i + 1, QUESTIONS.length);
  }

  rl.close();

  const result = compute(answers);
  printResult(result);
}

main().catch((err) => {
  rl.close();
  console.error('\n❌  Erreur :', err.message);
  process.exit(1);
});

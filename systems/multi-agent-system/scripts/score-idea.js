#!/usr/bin/env node
/**
 * score-idea.js — Scoreur interactif d'idées d'articles schoolsWP
 *
 * Guide pas à pas sur les 5 critères → Score Opportunité /100 → recommandation.
 * Aucune clé API requise — 100% local, 100% gratuit.
 *
 * Usage :
 *   node scripts/score-idea.js
 *   node scripts/score-idea.js --topic "FluentCRM vs MailerLite"
 *   node scripts/score-idea.js --batch  (mode multi-sujets)
 *
 * Output : scores + label + recommandations + valeurs à copier dans Notion
 */

const readline = require('readline');

const args    = process.argv.slice(2);
const getArg  = (flag, def) => { const i = args.indexOf(flag); return i !== -1 && args[i + 1] ? args[i + 1] : def; };
const BATCH   = args.includes('--batch');
const TOPIC   = getArg('--topic', '');

// ─── Critères de scoring ──────────────────────────────────────────────────────

const CRITERIA = [
  {
    key: 'seo',
    label: 'SEO',
    max: 25,
    header: '📊 POTENTIEL SEO (0–25)',
    hint: 'Est-ce que ce sujet peut ranker sur Google dans un horizon réaliste ?',
    sub: [
      { label: 'Volume estimé',        range: '0-6',  guide: '0: <100/mois · 3: 100-1k · 6: >1k' },
      { label: 'Difficulté relative',  range: '0-6',  guide: '0: KD>70 (GAFA) · 3: KD 40-70 · 6: KD<40 (atteignable)' },
      { label: 'Intent claire',        range: '0-7',  guide: '0: vague · 4: informationnelle · 7: décisionnelle/transactionnelle' },
      { label: 'Concurrents faibles',  range: '0-6',  guide: '0: GAFA/marques fortes · 3: blogs moyens · 6: faible/niche' }
    ]
  },
  {
    key: 'business',
    label: 'Business',
    max: 25,
    header: '💰 INTENT BUSINESS (0–25)',
    hint: 'Ce sujet mène-t-il vers une action monétisable pour schoolsWP ?',
    sub: [
      { label: 'Lien affilié naturel', range: '0-8',  guide: '0: aucun · 4: indirect (bouton en bas) · 8: direct (comparatif CTA)' },
      { label: 'Lead magnet possible', range: '0-7',  guide: '0: aucun · 3: possible (checklist) · 7: évident (template, guide)' },
      { label: 'Intent achat/décision',range: '0-10', guide: '0: aucune · 5: partielle (comparatif info) · 10: forte (vs/choisir/meilleur)' }
    ]
  },
  {
    key: 'autorite',
    label: 'Autorité',
    max: 20,
    header: '🧠 POTENTIEL AUTORITÉ THÉMATIQUE (0–20)',
    hint: 'Ce sujet renforce-t-il l\'écosystème WordPress/LMS/CRM/Automatisation de schoolsWP ?',
    sub: [
      { label: 'Renforce un cluster',       range: '0-8', guide: '0: hors cluster · 4: satellite · 8: pilier de cluster' },
      { label: 'Satellites futurs',         range: '0-6', guide: '0: aucun · 3: 1-2 articles possibles · 6: 3+ articles naturels' },
      { label: 'Cohérence positionnement',  range: '0-6', guide: '0: hors sujet · 3: tangent WP · 6: cœur schoolsWP (LMS/CRM/SEO/Auto/Perf)' }
    ]
  },
  {
    key: 'llm',
    label: 'LLM',
    max: 15,
    header: '🤖 POTENTIEL LLM / AI VISIBILITY (0–15)',
    hint: 'Ce sujet peut-il générer des citations dans Perplexity, ChatGPT, Gemini ?',
    sub: [
      { label: 'FAQ-friendly',          range: '0-5', guide: '0: non structurable · 3: quelques questions · 5: bloc FAQ naturel' },
      { label: 'Réponse extractible',   range: '0-5', guide: '0: subjective/contextuelle · 3: partielle · 5: réponse directe en 2 phrases' },
      { label: 'Définitions/comparatif',range: '0-5', guide: '0: aucun · 3: un aspect structurable · 5: tableau / liste / définition claire' }
    ]
  },
  {
    key: 'effort',
    label: 'Effort',
    max: 15,
    header: '⚡ EFFORT VS IMPACT (0–15) — score INVERSÉ',
    hint: 'Plus le sujet est rapide à traiter pour un fort impact, plus le score est élevé.',
    sub: [
      { label: 'Temps rédaction',      range: '0-5', guide: '0: >2 jours · 3: 1 jour · 5: <4h (sujet déjà maîtrisé)' },
      { label: 'Complexité technique', range: '0-5', guide: '0: très haute (code, config avancée) · 3: moyenne · 5: faible (concept clair)' },
      { label: 'Recherche nécessaire', range: '0-5', guide: '0: exhaustive (tester 5 plugins) · 3: modérée · 5: connue (vécu direct)' }
    ]
  }
];

// ─── Interprétation ───────────────────────────────────────────────────────────

function getLabel(score) {
  if (score >= 85) return { emoji: '🔥', text: 'Priorité absolue',  action: 'Planifier ce trimestre — sujet stratégique' };
  if (score >= 70) return { emoji: '🟢', text: 'Planifier',         action: 'Backlog Q suivant — bon levier' };
  if (score >= 50) return { emoji: '🟡', text: 'À challenger',      action: 'Requalifier l\'angle ou attendre meilleure fenêtre' };
  return              { emoji: '⚫', text: 'Éviter',             action: 'Levier trop faible pour schoolsWP à ce stade' };
}

function getRecommendations(scores) {
  const recs = [];
  if (scores.seo      <= 10) recs.push('SEO faible      → travailler l\'angle long tail ou requalifier l\'intent');
  if (scores.business <= 10) recs.push('Business faible → identifier un affilié ou lead magnet naturel sur ce sujet');
  if (scores.autorite <=  8) recs.push('Autorité faible → rattacher à un cluster existant avant d\'écrire');
  if (scores.llm      <=  6) recs.push('LLM faible      → prévoir blocs FAQ + "Réponse rapide" pour la visibilité IA');
  if (scores.effort   <=  6) recs.push('Effort élevé    → découper en sous-article ou planifier avec plus de temps');
  return recs;
}

// ─── Affichage ────────────────────────────────────────────────────────────────

function bar(score, max, width = 18) {
  const filled = Math.round((score / max) * width);
  return `[${'█'.repeat(filled)}${'░'.repeat(width - filled)}]`;
}

function printResult(topic, scores) {
  const total = Object.values(scores).reduce((a, b) => a + b, 0);
  const lbl   = getLabel(total);
  const recs  = getRecommendations(scores);

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log(`  📊  Résultat — "${topic}"\n`);
  console.log('  Critère      Score   /Max   Barre');
  console.log('  ─────────────────────────────────────────────────────');

  for (const crit of CRITERIA) {
    const s = scores[crit.key];
    console.log(
      `  ${crit.label.padEnd(12)} ${String(s).padStart(3)}     ${crit.max}    ${bar(s, crit.max)}`
    );
  }

  console.log('  ─────────────────────────────────────────────────────');
  console.log(`  TOTAL        ${String(total).padStart(3)}     100   ${bar(total, 100)}`);
  console.log('');
  console.log(`  ${lbl.emoji}  Score Opportunité : ${total}/100`);
  console.log(`      ${lbl.text} — ${lbl.action}`);

  if (recs.length > 0 && total >= 50) {
    console.log('\n  📌  Points d\'amélioration :');
    recs.forEach(r => console.log(`      → ${r}`));
  }

  console.log('\n  📋  À copier dans Notion :');
  console.log(`      SEO      : ${scores.seo}`);
  console.log(`      Business : ${scores.business}`);
  console.log(`      Autorité : ${scores.autorite}`);
  console.log(`      LLM      : ${scores.llm}`);
  console.log(`      Effort   : ${scores.effort}`);
  console.log(`      → Score Opportunité calculé automatiquement : ${total}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');

  return total;
}

// ─── Session interactive ──────────────────────────────────────────────────────

const rl  = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (q) => new Promise(res => rl.question(q, ans => res(ans.trim())));

async function scoreTopic(topic) {
  const scores = {};

  for (const crit of CRITERIA) {
    console.log(`\n  ┌─ ${crit.header}`);
    console.log(`  │  ${crit.hint}`);
    console.log('  │');
    crit.sub.forEach(s => {
      console.log(`  │  ${s.label.padEnd(24)} [${s.range}]   ${s.guide}`);
    });
    console.log('  │');

    let score;
    while (true) {
      const raw = await ask(`  └─ Score ${crit.label} [0-${crit.max}] : `);
      const val = parseInt(raw, 10);
      if (!isNaN(val) && val >= 0 && val <= crit.max) {
        score = val;
        break;
      }
      console.log(`     ⚠️  Entrer un nombre entre 0 et ${crit.max}`);
    }

    scores[crit.key] = score;
    const pct = Math.round((score / crit.max) * 100);
    console.log(`     ${bar(score, crit.max)} ${score}/${crit.max} (${pct}%)`);
  }

  return scores;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  🧠  schoolsWP — Scoreur d\'Opportunité Éditoriale');
  console.log('  5 critères · Score /100 · Décision en 5 minutes');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');

  const results = [];

  do {
    let topic = TOPIC;
    if (!topic || results.length > 0) {
      topic = await ask('  📝  Sujet / idée d\'article : ');
    }
    if (!topic) break;

    console.log(`\n  Évaluation : "${topic}"\n`);
    const scores = await scoreTopic(topic);
    const total  = printResult(topic, scores);
    results.push({ topic, scores, total });

    if (BATCH) {
      const again = await ask('\n  Scorer un autre sujet ? [o/N] : ');
      if (again.toLowerCase() !== 'o' && again.toLowerCase() !== 'oui') break;
    }
  } while (BATCH);

  // Récapitulatif batch
  if (results.length > 1) {
    console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    console.log(`  📊  Récapitulatif — ${results.length} sujets évalués\n`);
    results
      .sort((a, b) => b.total - a.total)
      .forEach((r, i) => {
        const lbl = getLabel(r.total);
        console.log(`  ${String(i + 1).padStart(2)}.  ${lbl.emoji} ${String(r.total).padStart(3)}/100  ${r.topic}`);
      });
    console.log('\n  → Écrire dans cet ordre de priorité.\n');
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
  } else {
    console.log('');
  }

  rl.close();
}

main().catch(e => {
  if (e.code === 'ERR_USE_AFTER_CLOSE') process.exit(0);
  console.error('\n❌  Erreur :', e.message);
  rl.close();
  process.exit(1);
});

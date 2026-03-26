#!/usr/bin/env node
/**
 * auto-scorer.js — Scoring automatique d'articles schoolsWP via OpenAI
 *
 * Usage :
 *   node scripts/auto-scorer.js --file article.md [--keyword "plugin SEO WordPress"]
 *   node scripts/auto-scorer.js --file article.md --fix         (score + auto-correction)
 *   node scripts/auto-scorer.js --file article.md --save        (sauvegarde JSON résultat)
 *   node scripts/auto-scorer.js --file article.md --model gpt-4o-mini  (modèle moins coûteux)
 *   cat article.md | node scripts/auto-scorer.js --stdin         (lecture depuis stdin)
 *
 * Env : OPENAI_API_KEY (requis)
 *
 * Pas de dépendances npm — utilise fetch natif Node.js 18+.
 * Équivalent SDK : import OpenAI from "openai"; openai.responses.create(payload)
 */

const OPENAI_KEY = process.env.OPENAI_API_KEY;

if (!OPENAI_KEY) {
  console.error('❌  OPENAI_API_KEY manquant');
  process.exit(1);
}

// ─── Prompts ─────────────────────────────────────────────────────────────────

const SYSTEM_SCORING = `Tu es schoolsWP Brain en mode Audit Scoring strict.

Contexte : schoolsWP (schoolswp.com) — WordPress pédagogique francophone.
Public : freelances et indépendants WordPress, débutants à intermédiaires.
Ton attendu dans les articles : direct, tutoiement, pédagogique, sans jargon.
Mots interdits à pénaliser : disruptif, game changer, scalable, révolutionnaire, incroyable, en un clic, sans effort.

Analyse l'article fourni et retourne UNIQUEMENT un JSON valide — aucun texte avant ni après.

=== CRITÈRES D'ÉVALUATION ===

SEO (0-100) :
- H1/H2/H3 structurés et cohérents avec le mot-clé
- Mot-clé principal dans : titre, intro, au moins 2 H2
- Champs sémantiques exploités (synonymes, entités nommées liées)
- FAQ ou bloc Q/R structuré présent
- Intro < 3 phrases, répond à l'intention de recherche immédiatement
- Densité naturelle, pas de sur-optimisation

LLM (0-100) — AI Visibility :
- Bloc "Réponse rapide" ou définition directe en 2-3 phrases (AI Overview-ready)
- Format question/réponse explicite dans au moins une section
- Entités nommées claires (plugins nommés, versions, URLs, chiffres)
- Phrases courtes et factuelles dans les blocs clés
- Pas d'ambiguïté sur les recommandations

Conversion (0-100) :
- 1 CTA principal visible et ciblé (pas générique)
- Lien vers offre / formation / outil affilié ou lead magnet
- Argumentation business présente (gain de temps, économie, ROI chiffré)
- Tunnel logique : problème → solution → bénéfice → action
- Au moins une objection traitée

Autorité (0-100) :
- Expérience terrain mentionnée ("dans mon cas", "sur schoolsWP", "j'ai testé")
- Données chiffrées ou sources citées (au moins 1)
- Positionnement expert — pas de contenu générique applicable partout
- Comparaisons objectives si article comparatif
- Zéro promesse non prouvée

=== FORMAT DE RETOUR (JSON strict) ===
{
  "keyword": "mot-clé principal détecté",
  "seo": {
    "score": 0,
    "justification": "max 200 caractères",
    "improvements": ["amélioration 1", "amélioration 2"]
  },
  "llm": {
    "score": 0,
    "justification": "max 200 caractères",
    "improvements": ["amélioration 1", "amélioration 2"]
  },
  "conversion": {
    "score": 0,
    "justification": "max 200 caractères",
    "improvements": ["amélioration 1", "amélioration 2"]
  },
  "autorite": {
    "score": 0,
    "justification": "max 200 caractères",
    "improvements": ["amélioration 1", "amélioration 2"]
  },
  "score_global": 0,
  "diagnostic": "max 300 caractères — diagnostic global",
  "priority": "A|B|C",
  "action": "✅ Actif Premium|🟢 Actif Performant|🟡 Optimiser|🔴 Révision Stratégique"
}`;

const SYSTEM_FIX = `Tu es schoolsWP Brain en mode Correction Chirurgicale.

Consigne : améliore UNIQUEMENT les sections responsables des scores inférieurs à 85.
Ne touche pas aux parties ayant un score ≥ 85.
Conserve le style, le ton, le tutoiement, la structure générale.
Intègre les améliorations listées dans l'audit fourni.

Retourne UNIQUEMENT le contenu markdown corrigé — aucun commentaire ni explication.`;

// ─── API helper ───────────────────────────────────────────────────────────────

async function callOpenAI(systemPrompt, userContent, model = 'gpt-4o', jsonMode = true) {
  const body = {
    model,
    input: [
      { role: 'system', content: systemPrompt },
      { role: 'user',   content: userContent  }
    ],
    temperature: 0.2
  };

  if (jsonMode) {
    body.text = { format: { type: 'json_object' } };
  }

  const resp = await fetch('https://api.openai.com/v1/responses', {
    method: 'POST',
    headers: {
      Authorization:  `Bearer ${OPENAI_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });

  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`OpenAI API ${resp.status}: ${err.error?.message || JSON.stringify(err)}`);
  }

  const data = await resp.json();
  // output_text est le raccourci Responses API (équivalent choices[0].message.content)
  return data.output_text
    || (data.output?.[0]?.content?.[0]?.text)
    || '';
}

// ─── Scoring ──────────────────────────────────────────────────────────────────

async function scoreArticle(content, keyword, model) {
  const userMsg = keyword
    ? `Mot-clé cible : "${keyword}"\n\n---\n\n${content}`
    : content;

  const raw = await callOpenAI(SYSTEM_SCORING, userMsg, model, true);

  let scores;
  try {
    scores = JSON.parse(raw);
  } catch {
    // Fallback : extraire le JSON si entouré de texte parasite
    const match = raw.match(/\{[\s\S]*\}/);
    if (!match) throw new Error('Réponse OpenAI non-JSON : ' + raw.slice(0, 200));
    scores = JSON.parse(match[0]);
  }

  // Recalcul Score Global (vérification cohérence)
  const sg = Math.round(
    (scores.seo.score        * 0.25) +
    (scores.llm.score        * 0.15) +
    (scores.conversion.score * 0.30) +
    (scores.autorite.score   * 0.30)
  );
  scores.score_global = sg;

  // Action label
  scores.action = sg >= 95 ? '✅ Actif Premium'
    : sg >= 85 ? '🟢 Actif Performant'
    : sg >= 70 ? '🟡 Optimiser'
    : '🔴 Révision Stratégique';

  scores.priority = sg >= 85 ? 'A' : sg >= 70 ? 'B' : 'C';

  return scores;
}

// ─── Auto-correction ──────────────────────────────────────────────────────────

async function fixArticle(content, scores, model) {
  const weakDims = ['seo', 'llm', 'conversion', 'autorite']
    .filter(d => scores[d].score < 85)
    .map(d => `${d.toUpperCase()} (${scores[d].score}/100) :\n${scores[d].improvements.map(i => `  - ${i}`).join('\n')}`)
    .join('\n\n');

  if (!weakDims) {
    return { fixed: content, note: 'Aucune correction nécessaire (tous les scores ≥ 85)' };
  }

  const userMsg = `Scores à corriger :\n${weakDims}\n\n---\n\n${content}`;
  const fixed = await callOpenAI(SYSTEM_FIX, userMsg, model, false);
  return { fixed, note: 'Corrections appliquées sur : ' + weakDims.slice(0, 100) };
}

// ─── CLI ──────────────────────────────────────────────────────────────────────

function parseArgs() {
  const args = process.argv.slice(2);
  const get = (flag) => {
    const i = args.indexOf(flag);
    return i !== -1 ? args[i + 1] : null;
  };
  return {
    file:    get('--file'),
    keyword: get('--keyword'),
    model:   get('--model') || 'gpt-4o',
    fix:     args.includes('--fix'),
    save:    args.includes('--save'),
    stdin:   args.includes('--stdin')
  };
}

function printScores(scores) {
  const bar = (n) => '█'.repeat(Math.round(n / 5)).padEnd(20) + ` ${n}/100`;
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log(`  schoolsWP Brain — Audit Scoring\n`);
  if (scores.keyword) console.log(`  Mot-clé détecté : ${scores.keyword}\n`);
  console.log(`  SEO        ${bar(scores.seo.score)}`);
  console.log(`  LLM        ${bar(scores.llm.score)}`);
  console.log(`  Conversion ${bar(scores.conversion.score)}`);
  console.log(`  Autorité   ${bar(scores.autorite.score)}`);
  console.log(`\n  ──────────────────────────────────`);
  console.log(`  SCORE GLOBAL  ${bar(scores.score_global)}`);
  console.log(`  ${scores.action}  |  Priorité ${scores.priority}`);
  if (scores.diagnostic) console.log(`\n  ${scores.diagnostic}`);
  console.log('\n  Top améliorations :');
  ['seo', 'llm', 'conversion', 'autorite'].forEach(d => {
    if (scores[d].score < 85) {
      console.log(`\n  [${d.toUpperCase()}]`);
      scores[d].improvements.forEach(i => console.log(`    → ${i}`));
    }
  });
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

async function main() {
  const { file, keyword, model, fix, save, stdin } = parseArgs();

  let content = '';
  if (stdin) {
    content = await new Promise(res => {
      let d = '';
      process.stdin.on('data', c => { d += c; });
      process.stdin.on('end', () => res(d));
    });
  } else if (file) {
    const { readFileSync } = await import('fs');
    content = readFileSync(file, 'utf8');
  } else {
    console.error('❌  Fournir --file <path> ou --stdin');
    process.exit(1);
  }

  console.log(`🔍  Scoring en cours... (modèle: ${model})`);
  const scores = await scoreArticle(content, keyword, model);
  printScores(scores);

  let result = { scores };

  if (fix) {
    console.log('🔧  Auto-correction des sections < 85...');
    const { fixed, note } = await fixArticle(content, scores, model);
    result.fixed_content = fixed;
    result.fix_note = note;
    console.log(`  ✅  ${note}`);

    if (fixed !== content) {
      console.log('\n  Re-scoring du contenu corrigé...');
      const scores2 = await scoreArticle(fixed, keyword, model);
      result.scores_after_fix = scores2;
      printScores(scores2);
    }
  }

  if (save) {
    const { writeFileSync } = await import('fs');
    const outFile = (file || 'stdin').replace(/\.md$/, '') + '-scores.json';
    writeFileSync(outFile, JSON.stringify(result, null, 2));
    console.log(`  💾  Sauvegardé → ${outFile}`);
  } else {
    // JSON brut en stdout pour piping
    console.log(JSON.stringify(result.scores, null, 2));
  }
}

main().catch(e => {
  console.error('\n❌  Erreur :', e.message);
  process.exit(1);
});

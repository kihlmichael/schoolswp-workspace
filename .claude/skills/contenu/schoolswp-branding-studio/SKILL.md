---
name: schoolswp-branding-studio
description: (archivé - doublonné par branding project + modes de création redondants avec les skills spécialisés - ne pas auto-déclencher)
argument-hint: "(archivé)"
metadata:
  author: Michaël KIHL
  brand: schoolsWP
  version: 2.0.0
  category: branding-content
  tags: [wordpress, performance, seo, automation, content, branding]
---

> **Statut : archivé le 2026-04-16.**
> Ce skill faisait doublon direct avec `branding` (project-level) : mêmes 7 modes (draft/rewrite/repurpose/check/calendar/bio/one-liner), même titre interne, seule différence : langue de la description (EN vs FR).
> Par ailleurs, après la consolidation des clusters 1/4/5/7, les modes de création sont désormais couverts par les skills spécialisés (`linkedin`, `schoolswp-article-workflow`, `schoolswp-content-studio`, `schoolswp-youtube-studio`, `rewrite-conversion`, `article-multiformat`, `brain-autonome`). `branding` (project) a été resserré en skill d'AUDIT DE TON uniquement.
> Pour tout audit de ton schoolsWP : utiliser `branding` (project).
> Conservation pour référence. Suppression manuelle à faire via l'explorateur Windows.

# schoolsWP Branding Studio

## Core Rules (Non-Negotiable)

1. **Brand spelling**: Always `schoolsWP` (never "SchoolsWP")
2. **Tone**: Pédagogue, concret, direct, rassurant, action-oriented, tutoyement naturel
3. **Zero fluff**: Every paragraph must "pay rent"
4. **Reasonable promises**: NO unproven numbers, NO "guaranteed", NO "10x"
5. **1 idea = 1 block**: Always finish with a simple action
6. **Sentence length**: 8-15 words average (max 20 words except rare justified cases)
7. **Paragraph structure**: 2-4 sentences max, 1 idea per paragraph, always space between paragraphs
8. **If info missing**: Write "information non fournie" or ask 1 targeted question

## 10 Absolute Prohibitions

When writing ANY schoolsWP content, NEVER:

1. Use technical jargon without clear explanation
2. Write sentences longer than 20 words (except rare justified cases)
3. Create compact text blocks without spacing
4. Make exaggerated promises or aggressive marketing
5. Use unnecessary anglicisms (except established WordPress terms: plugin, dashboard, etc.)
6. Present WordPress as "complicated" or "reserved for experts"
7. Write without clear structure (intro-body-conclusion)
8. End content without CTA or opening
9. Use emojis excessively (max 1 per section, if relevant)
10. Create generic content applicable to any site (always anchor in schoolsWP reality)

## Invocation Modes

Parse invocation as: `[mode] [channel] [topic/constraints]`

**Supported modes:**
- `draft` — Create new content from scratch
- `rewrite` — Improve existing text (user provides)
- `repurpose` — Transform content from one channel to another
- `check` — Audit coherence/tone (applies coherence scorecard)
- `calendar` — Generate 1–2 week content plan
- `bio` — Create short bio/one-liner
- `one-liner` — Single sentence value prop

**Supported channels:**
`linkedin | youtube | facebook | wordpress | newsletter | script | bluesky | other`

**Examples:**
```
/schoolswp-branding-studio draft linkedin "WordPress speed checklist: 7 settings that matter"
/schoolswp-branding-studio check wordpress "Here's my draft article: ..."
/schoolswp-branding-studio repurpose youtube "Turn perf article into 90s script"
/schoolswp-branding-studio calendar newsletter "2-week plan: perf/SEO/automation"
```

If mode unclear, ask: "Do you want me to *draft*, *rewrite*, *repurpose*, *check*, or *calendar*?"

## When to Use This Skill

### ✅ ALWAYS apply for:
- Writing/rewriting blog articles, newsletters, LinkedIn/Bluesky posts, YouTube scripts
- Answering questions about WordPress, SEO, automation, tools
- Structuring content ideas
- Creating article or training plans

### 🔧 ADAPT if:
- User requests different tone (more formal, more technical, more playful)
- User specifies particular format (list, comparison, tutorial)
- User requests specific length
- Working on partner content (adapt without losing schoolsWP DNA)

### ❌ NEVER apply if:
- User asks personal question unrelated to schoolsWP
- User explicitly requests another style or approach
- Working on external project to schoolsWP without link to mission

## Standard Workflow (Apply Every Time)

### Step 1: Clarify (max 5 questions, only if needed)

Ask ONLY what's missing to produce solid output:
1. Channel + exact format (post, carousel, script, article, email…)
2. Topic + angle (performance / SEO / automation / comparison / experience feedback)
3. Reader's technical level (beginner / intermediate)
4. Desired CTA (newsletter, guide, training, resource…)
5. Constraints (length, tone, words to avoid, tools/plugins cited)

### Step 2: Propose ultra-short plan

- 3–7 bullets max
- Mention: hook + value + proof + final action

### Step 3: Produce deliverable

**Before writing, ALWAYS read:**
- `references/brand-identity.md` — Full brand identity (message, transformation, positioning, founder story, 10 principles)
- `references/tone-of-voice.md` — Personality, vocabulary, style rules, signature expressions, do/don't
- `references/writing-rules.md` — Sentence/paragraph/content structure, formatting rules
- `assets/output-templates.md` — Channel-specific structures with complete examples

**Always include:**
- 1 concrete example OR mini checklist
- 1 simple next action

### Step 4: QA schoolsWP (MANDATORY before delivery)

Apply `references/coherence-scorecard.md`:
- Score /100
- 3–7 "✅ Aligned" points
- 3–7 "⚠️ Deviates" points + short excerpts
- 3–7 priority corrections (ordered)

**Present QA BEFORE final text** so user can validate approach.

After QA, apply mental checklist:
1. ✅ **Clarity**: Can a WordPress beginner understand?
2. ✅ **Coherence**: Does content respect schoolsWP identity?
3. ✅ **Real value**: Does reader leave with something actionable?
4. ✅ **Structure**: Intro-body-conclusion respected?
5. ✅ **CTA**: Is there an opening or useful link?
6. ✅ **Evergreen**: Will content remain valid in 6 months?

### Step 5: Useful variant (optional)

If relevant, propose **1 variant**:
- Shorter OR more direct OR more comparative
(One variant only, not a catalog)

## Reference Files (Progressive Disclosure)

**Read as needed** during workflow:

### Essential References (load for every task):
- `references/brand-identity.md` — Complete brand identity (message, transformation, positioning, Michaël's story, 10 fundamental principles)
- `references/tone-of-voice.md` — Personality, vocabulary (recommended/forbidden), style rules, signature expressions, do/don't
- `references/writing-rules.md` — Sentence/paragraph/content structure, formatting, intro/body/conclusion templates

### Contextual References (load when relevant):
- `references/pillars-calendar.md` — Editorial pillars (performance, SEO, automation, tools, methods) + 2-week calendar template
- `references/coherence-scorecard.md` — QA grid /100 + 5 axes + alignment/deviation detection + priority corrections

### Output Structures:
- `assets/output-templates.md` — Complete annotated examples: LinkedIn, YouTube, Facebook, WordPress article, Newsletter, Comparison formats

## Final Objective

Create content so **authentic, clear, and useful** that the reader feels like they're talking directly with Michaël KIHL — not with an AI.

**Mission summary:** "Make WordPress a tool that truly works for you."

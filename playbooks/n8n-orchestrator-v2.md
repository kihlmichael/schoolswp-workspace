# schoolsWP OS — n8n Orchestrator V2 (JSON strict)

Objectif V2
- Router JSON strict
- Outputs agents agreges (seo_output, wp_output, etc.)
- Synthese + QA en JSON
- Boucle auto si QA = FAIL (max 2 iterations)

Architecture V2
Webhook -> Normalize Input -> Router (LLM JSON)
-> Parse Router JSON -> Spawn Agents -> Agents LLM JSON
-> Parse Agent JSON -> Merge -> Aggregator
-> Synthesizer LLM JSON -> QA LLM JSON
-> IF QA PASS -> Outputs
-> IF QA FAIL -> Append fixes -> Re-synth -> QA

1) Router V2 prompt (JSON strict)
Tu es ROUTER du schoolsWP OS.
Decide quels agents lancer.

Entree:
- Mission: {{$json.mission}}
- Contexte: {{$json.context}}
- Data: {{$json.data}}

Contraintes:
- Reponds UNIQUEMENT en JSON valide.
- Pas de texte hors JSON.
- Agents possibles: "seo", "wp", "automation", "monetization"
- Toujours inclure "qa".
- Max 4 agents metier + qa.

Sortie JSON exacte:
{
  "agents": ["seo","monetization","qa"],
  "priority": "low|medium|high",
  "expected_outputs": ["plan","deliverables","verification_checklist"],
  "notes": "hypotheses de routing en 1 phrase"
}

Reglages
- Temp: 0.1-0.2
- Max tokens: 600-1200

2) Parse Router JSON (Function)
const raw = $json.text ?? $json.content ?? $json.message ?? $json;
const s = typeof raw === "string" ? raw : JSON.stringify(raw);

function extractJson(str) {
  const first = str.indexOf("{");
  const last = str.lastIndexOf("}");
  if (first === -1 || last === -1) throw new Error("No JSON object found");
  return str.slice(first, last + 1);
}

let parsed;
try { parsed = JSON.parse(s); }
catch (e) { parsed = JSON.parse(extractJson(s)); }

const allowed = new Set(["seo","wp","automation","monetization","qa"]);
let agents = Array.isArray(parsed.agents) ? parsed.agents.filter(a => allowed.has(a)) : [];
if (!agents.includes("qa")) agents.push("qa");
agents = agents.slice(0, 5);

return [{
  json: {
    ...$json,
    router: {
      agents,
      priority: parsed.priority || "medium",
      expected_outputs: parsed.expected_outputs || ["plan","deliverables","verification_checklist"],
      notes: parsed.notes || ""
    },
    iteration: $json.iteration ?? 0
  }
}];

3) Agents V2 prompts (JSON strict)
SEO-ANALYST JSON
{
  "agent": "seo",
  "findings": ["..."],
  "recommendation": ["..."],
  "internal_linking": { "parent": "...", "children": ["..."], "peers": ["..."] },
  "ia_citable_blocks": { "definitions": ["..."], "checklists": ["..."] },
  "risks": ["..."],
  "next_actions": ["..."]
}

WP-ARCHITECT JSON
{
  "agent": "wp",
  "stack_choices": ["..."],
  "risks_mitigations": ["..."],
  "minimal_change_plan": ["..."],
  "verification_checklist": ["..."]
}

AUTOMATION-ENGINEER JSON
{
  "agent": "automation",
  "trigger_map": ["..."],
  "tags_namespace": ["..."],
  "sequence_steps": ["..."],
  "guardrails": ["..."],
  "tracking_kpis": ["..."],
  "test_plan": ["..."]
}

MONETIZATION JSON
{
  "agent": "monetization",
  "primary_offer_cta": ["..."],
  "secondary_offers": ["..."],
  "placement_plan": ["..."],
  "objections_answers": ["..."],
  "kpi": ["..."]
}

Reglages agents
- Temp: 0.2-0.4
- Max tokens: 2000-4000

4) Parse Agent JSON (Function)
const raw = $json.text ?? $json.content ?? $json.message ?? $json;
const s = typeof raw === "string" ? raw : JSON.stringify(raw);

function extractJson(str) {
  const first = str.indexOf("{");
  const last = str.lastIndexOf("}");
  if (first === -1 || last === -1) throw new Error("No JSON object found");
  return str.slice(first, last + 1);
}

let parsed;
try { parsed = JSON.parse(s); }
catch { parsed = JSON.parse(extractJson(s)); }

return [{ json: { ...$json, agent_output: parsed } }];

5) Aggregator (Function)
const outputs = {
  seo_output: null,
  wp_output: null,
  automation_output: null,
  monetization_output: null
};

for (const item of $input.all()) {
  const o = item.json.agent_output;
  if (!o || !o.agent) continue;
  if (o.agent === "seo") outputs.seo_output = o;
  if (o.agent === "wp") outputs.wp_output = o;
  if (o.agent === "automation") outputs.automation_output = o;
  if (o.agent === "monetization") outputs.monetization_output = o;
}

const base = $input.first().json;

return [{
  json: {
    mission: base.mission,
    context: base.context,
    data: base.data,
    router: base.router,
    iteration: base.iteration ?? 0,
    ...outputs,
    qa_fixes_required: base.qa_fixes_required ?? []
  }
}];

6) Synthesizer V2 prompt (JSON strict)
Tu es le schoolsWP OS (SYNTHESIZER).
Style: francais, phrases courtes, concret.

Entree:
- Mission: {{$json.mission}}
- Contexte: {{$json.context}}
- Data: {{$json.data}}
- Routing: {{$json.router}}
- Fixes QA: {{$json.qa_fixes_required}}

Agents:
- SEO: {{$json.seo_output}}
- WP: {{$json.wp_output}}
- Automation: {{$json.automation_output}}
- Monetization: {{$json.monetization_output}}

Contraintes:
- Reponds UNIQUEMENT en JSON valide.
- Toujours inclure: plan, execution_steps, verification_proofs, deliverables, assumptions.

Sortie JSON exacte:
{
  "module": "schoolsWP OS",
  "plan": ["..."],
  "execution_steps": ["..."],
  "verification_proofs": ["..."],
  "deliverables": ["..."],
  "assumptions": ["..."],
  "notes": ["..."]
}

Reglages synthese
- Temp: 0.2-0.3
- Max tokens: 2500-6000

7) QA V2 prompt (JSON strict)
Tu es QA-VERIFIER.
Tu refuses toute conclusion si manque de preuves/tests, incoherences, ou plan non actionnable.

Entree synthese:
{{$json.synth_output}}

Sortie JSON exacte:
{
  "verdict": "PASS|FAIL",
  "issues": ["..."],
  "required_fixes": ["..."],
  "proof_checklist": ["..."]
}

Reglages QA
- Temp: 0.1-0.2
- Max tokens: 1200-2500

8) Boucle FAIL -> Fixes -> Re-synth (max 2 iterations)
Parse QA JSON (Function)
const raw = $json.text ?? $json.content ?? $json.message ?? $json;
const s = typeof raw === "string" ? raw : JSON.stringify(raw);

function extractJson(str){
  const a = str.indexOf("{");
  const b = str.lastIndexOf("}");
  if(a === -1 || b === -1) throw new Error("No JSON found");
  return str.slice(a, b+1);
}

let qa;
try { qa = JSON.parse(s); } catch { qa = JSON.parse(extractJson(s)); }

const verdict = (qa.verdict || "").toUpperCase();
const required_fixes = Array.isArray(qa.required_fixes) ? qa.required_fixes : [];

return [{
  json: {
    ...$json,
    qa: {
      verdict: verdict === "PASS" ? "PASS" : "FAIL",
      issues: qa.issues || [],
      required_fixes,
      proof_checklist: qa.proof_checklist || []
    }
  }
}];

IF QA PASS
Condition: {{ $json.qa.verdict === "PASS" }}

IF FAIL -> Append Fixes + Increment iteration (Function)
const iteration = ($json.iteration ?? 0) + 1;
if (iteration > 2) {
  return [{
    json: {
      ...$json,
      iteration,
      loop_stopped: true,
      loop_reason: "Max iterations reached",
      qa_fixes_required: $json.qa.required_fixes || []
    }
  }];
}

return [{
  json: {
    ...$json,
    iteration,
    qa_fixes_required: $json.qa.required_fixes || []
  }
}];

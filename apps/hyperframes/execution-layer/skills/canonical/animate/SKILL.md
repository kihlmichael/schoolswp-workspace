---
name: animate
description: Orchestrate the schoolsWP Video Production System without bypassing evidence, brand or human review gates.
---

# /animate — schoolsWP video orchestrator

Use this skill as a facade, not as a monolithic video editor.

## Order

1. Inspect the source and preserve the original.
2. Normalize a word-level transcript when speech exists.
3. Run silence planning.
4. Run mistake/retake candidate review when useful.
5. Freeze the canonical EDL and canonical transcript.
6. Hand off to schoolsWP evidence/story/design contracts.
7. Build or update the visual plan.
8. Route each scene to the correct production mode.
9. Compose with HyperFrames when HyperFrames is the selected renderer.
10. Run execution-layer preflight.
11. Produce a draft.
12. Stop at the applicable human gate.

## Hard rules

- Never publish from this skill.
- Never use stale pre-edit timestamps after the media timeline changes.
- Never auto-approve an ambiguous speech cut.
- Never fabricate a WordPress interface where UI_CAPTURE is required.
- The schoolsWP Brand Kit and Evidence Ledger outrank generic HyperFrames defaults.
- Existing approved project decisions outrank this generic skill.

Execution commands live in:

apps/hyperframes/execution-layer/

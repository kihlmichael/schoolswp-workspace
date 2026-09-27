---
name: swp-video-preflight
description: Run machine-verifiable schoolsWP video execution checks before preview, render or human review.
---

# schoolsWP video preflight

Run:

    node apps/hyperframes/execution-layer/scripts/preflight.mjs <project-root>

Current P0 checks:
- canonical transcript structure
- canonical EDL continuity and source mapping
- plan duration sanity
- footage-ledger identity and SHA256 integrity

Status vocabulary:
- PASS
- PASS_WITH_WARNINGS
- FAIL

A technical PASS does not certify:
- factual accuracy
- visual quality
- a compelling hook
- brand approval
- editorial approval
- publication readiness

Those remain separate schoolsWP gates.

---
name: swp-cut-silences
description: Deterministically remove dead air from schoolsWP talking-head media while preserving natural breath and generating an EDL plus retimed transcript.
---

# schoolsWP cut silences

Use only for silence/dead-air tightening.

Do not remove:
- words
- retakes
- stutters
- repeated ideas
- editorial content

Those belong to review-gated mistake editing.

Default profile:

apps/hyperframes/execution-layer/profiles/educational.json

Plan first:

    node apps/hyperframes/execution-layer/scripts/cut-silences.mjs <transcript.json> --out-dir <assets>

Render only when editing is authorized:

    node apps/hyperframes/execution-layer/scripts/cut-silences.mjs <transcript.json> --video <raw.mp4> --out-dir <assets> --apply

Outputs:
- silence-edl.json
- transcript-silenced.json
- silence-decisions.md
- optional silenced.mp4

Never overwrite the source media.

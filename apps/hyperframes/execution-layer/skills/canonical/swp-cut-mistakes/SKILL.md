---
name: swp-cut-mistakes
description: Propose and apply reviewed speech edits for schoolsWP videos after silence removal, preserving canonical source-time provenance.
---

# schoolsWP cut mistakes

This stage is review-gated.

Candidate detection may identify:
- immediate duplicate words
- short repeated phrases / retakes

Detection is not approval.

Generate candidates:

    node apps/hyperframes/execution-layer/scripts/find-cut-candidates.mjs <transcript-silenced.json> <assets-dir>

A human or authorized editorial agent reviews candidates in context and writes:

    { "cuts": [{ "start": 1.2, "end": 1.5, "type": "mistake", "reason": "false start", "approved": true }] }

Then apply:

    node apps/hyperframes/execution-layer/scripts/apply-cuts.mjs <transcript-silenced.json> --previous-edl <silence-edl.json> --cuts <approved-cuts.json> --out-dir <assets>

The resulting edit-decisions.json is the canonical EDL and transcript.json is the canonical edited transcript.

Never cut intentional emphasis merely because a detector flags repetition.

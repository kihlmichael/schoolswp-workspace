# schoolsWP Video Production System v1.1 — HyperFrames Execution Layer

This directory is the **execution plane** for the schoolsWP video system.

It does not replace the schoolsWP control plane. Editorial strategy, factual evidence,
brand rules, human gates, publication, analytics and the LEARNED loop remain upstream.

## P0 scope

- canonical edit decision ledger (EDL)
- transcript normalization and deterministic retiming
- silence-cut planning
- mistake/retake candidate review
- footage provenance ledger validation
- portable canonical skills for Claude Code and Codex
- synthetic fixture and tests
- preflight aggregation
- multi-OS CI

## Rules

1. Never modify the original media in place.
2. After an edit, downstream timing uses the retimed transcript only.
3. Every retained word keeps sourceStart/sourceEnd provenance.
4. Ambiguous speech edits are review-gated.
5. Real UI requirements from schoolsWP remain authoritative.
6. No validator may claim subjective quality it cannot prove.
7. No publication action is performed by this layer.
8. Upstream HyperFrames Student Kit ideas are adapted and pinned, not pulled blindly at runtime.

## Quick start

From this directory:

    npm test
    npm run preflight
    npm run skills:check

Optional media smoke test (requires FFmpeg):

    npm run fixture:generate
    npm run smoke

## Status

v1.1 P0 is intentionally minimal and extensible. P1 will add the richer plan schema,
short-form hook/open-loop contracts, caption/beat validators and Style Registry.

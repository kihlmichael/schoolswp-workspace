# Playbooks index

This folder contains the operating playbooks and n8n orchestrator workflows.

## Runbooks
- `runbook-idea-to-publish.md` — Flux principal : idee → qualification → generation → audit → publication

## Core playbooks
- `seo-system.md`
- `wordpress-stack.md`
- `automation-flows.md`

## Strategy playbooks
- `anti-competitors-strategy.md`
- `15-pages-execution-pack.md`
- `pitch-and-positioning.md`
- `category-design-wordpress-growth-systems.md`
- `category-design-one-pager.md`

## n8n orchestrator docs
- `n8n-orchestrator.md` (v1)
- `n8n-orchestrator-v2.md` (JSON strict, router + QA)

## n8n workflow exports
- `n8n-orchestrator-workflow.json`
- `n8n-orchestrator-v2-workflow.json`
- `n8n-orchestrator-v2-pro-anthropic.json`
- `n8n-orchestrator-v2-pro-openai.json`

## Import notes
1) Import the JSON in n8n.
2) Select credentials in each LLM node.
3) Set model + temperature per node.
4) Keep Router and QA on low temperature.
5) Run a test POST to the webhook.

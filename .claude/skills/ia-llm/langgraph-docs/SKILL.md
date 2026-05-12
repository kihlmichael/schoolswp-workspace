---
name: langgraph-docs
description: |
  Récupère la doc LangGraph officielle (llms.txt + how-to + concepts + tutorials + reference) pour répondre précisément aux questions d'implémentation : StateGraph, nœuds, edges conditionnels, persistence, human-in-the-loop, multi-agent.
  Utilise ce skill quand l'utilisateur dit : "LangGraph", "graph d'agents Python", "StateGraph", "LangChain graph", "checkpointer LangGraph", "human-in-the-loop LangGraph", ou implémente un workflow d'agents en Python avec LangChain.
  NE PAS utiliser pour : agents simples sans graph (utiliser `claude-api` ou `gemini-api-dev`), architecture multi-agents conceptuelle (utiliser `tri-agent-architecture` ou `agents-architect`), ou agents Claude Code internes (utiliser le système `.claude/agents/`).

---

# langgraph-docs

## Overview

This skill explains how to access LangGraph Python documentation to help answer questions and guide implementation.

## Instructions

### 1. Fetch the Documentation Index

Use the fetch_url tool to read the following URL:
https://docs.langchain.com/llms.txt

This provides a structured list of all available documentation with descriptions.

### 2. Select Relevant Documentation

Based on the question, identify 2-4 most relevant documentation URLs from the index. Prioritize:
- Specific how-to guides for implementation questions
- Core concept pages for understanding questions
- Tutorials for end-to-end examples
- Reference docs for API details

### 3. Fetch Selected Documentation

Use the fetch_url tool to read the selected documentation URLs.

### 4. Provide Accurate Guidance

After reading the documentation, complete the users request.

---
name: langgraph-docs
description: |
  Récupère la documentation LangGraph pertinente pour fournir des conseils précis et à jour. Utilise ce
  skill pour toute demande liée à LangGraph.
  Déclenche pour "LangGraph", "graph d'agents", "StateGraph", "LangChain graph".

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

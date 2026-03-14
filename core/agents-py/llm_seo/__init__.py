"""
Module LLM-SEO schoolsWP.

Audit de citabilité IA + optimisation AI Overviews.
Score /100 sur 5 signaux + probabilités par plateforme (Google AI Overview,
Perplexity, ChatGPT Browse, Bing Copilot).
"""
from agents.llm_seo.agent import CitationSignalResult, LlmSeoAgent

__all__ = ["LlmSeoAgent", "CitationSignalResult"]

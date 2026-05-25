---
name: agents-py-error-handling
description: "Patterns FR d'error handling pour les 28 agents Python schoolsWP : typed exceptions, retry exponential backoff, circuit breaker, logging structure, pour calls LLM, MCP et IO. Adapte de ECC error-handling avec scope Python uniquement et integration BaseContentAgent."
origin: ECC error-handling (ADAPT, Python only)
ecc-version: 2.0.0-rc.1
imported: 2026-05-25
scope: core/agents-py
---

# Error handling pour les agents Python schoolsWP

> Patterns d'error handling robustes pour les 28 agents Python heritant de BaseContentAgent. Couvre les calls LLM multi-provider, les calls MCP, l'IO fichier, le parsing LLM, et les pipelines multi-etapes.
>
> Adapte de l'EC ECC error-handling, restreint au scope Python schoolsWP, et enrichi de retry exponential backoff et circuit breaker absents du skill source.

## Quand activer

- Tu ajoutes un nouveau provider LLM dans core/agents-py/providers : besoin d'exception hierarchy plus retry pour les transients.
- Tu ecris un agent qui appelle un MCP externe (Novamira, n8n, DataForSEO, FluentCRM) : besoin de retry plus circuit breaker pour les downtimes.
- Tu construis un pipeline multi-etapes (article_pipeline, content_factory) : besoin d'errors typees pour distinguer fail recuperable vs fatal.
- Tu fais le code review d'un agent et tu remarques des except generiques ou des try sans log : signal pour ce skill.
- Tu debugges un silent failure (sortie vide, JSON malforme, timeout cache) : ce skill liste les patterns qui evitent ce cas.

## Principes directeurs

1. Echouer vite et fort : surfacer les erreurs a la frontiere ou elles se produisent, ne pas les enterrer dans des wrappers vides.
2. Exceptions typees plutot que strings : chaque erreur est une valeur structuree avec code, contexte et severite.
3. Messages utilisateur vs developpeur : le markdown de sortie ne contient pas de stack trace, le log fichier contient le contexte complet.
4. Jamais swallow silencieusement : tout except doit handle, re-raise ou log. Le pattern except sans action est interdit.
5. Les erreurs font partie du contrat : la docstring du run() documente quelles exceptions peuvent etre levees et dans quel cas.

## Hierarchie d'exceptions schoolsWP

Voir le fichier d'exemple examples/errors.py de ce skill : il contient les classes AgentError (base), LLMProviderError, LLMRateLimitError, MCPCallError, LLMParseError, PipelineError, ConfigurationError. Toutes derivent d'AgentError qui porte un code, une flag retryable, et un dict context pour les details (provider name, operation, excerpt LLM).

A copier dans core/agents-py/errors.py (a creer si absent), puis importer dans les agents qui en ont besoin.

La flag retryable distingue les erreurs transientes (rate limit, timeout reseau, 5xx) des erreurs permanentes (auth invalide, parse echec, config manquante). Le retry helper (section suivante) lit cette flag pour decider de retry ou pas.

## Retry avec exponential backoff

Voir le fichier d'exemple examples/retry.py : helper with_retry(fn, max_attempts, base_delay_seconds, max_delay_seconds, retry_if) qui retry une coroutine en exponential backoff plus jitter. Par defaut, retry uniquement si l'exception est une AgentError avec retryable=True. Cas particulier : LLMRateLimitError fournit son propre retry_after_seconds, qui est respecte au lieu du backoff calcule.

A placer dans core/agents-py/retry.py, importable par tous les agents.

Usage type dans un agent : envelopper l'appel self.call_llm() dans with_retry pour les transients (rate limit, 5xx provider). Voir examples/agent_with_retry.py pour le pattern complet.

Important : les calls LLM via self.call_llm() doivent lever LLMProviderError ou LLMRateLimitError depuis le provider concret (core/agents-py/providers/anthropic.py et autres) pour que retry_if puisse decider. Si les providers actuels levent juste des Exception generiques, c'est la premiere chose a refactorer.

## Circuit breaker pour MCP externes

Voir le fichier d'exemple examples/circuit_breaker.py : classe CircuitBreaker avec 3 etats (CLOSED, OPEN, HALF_OPEN), failure_threshold et cooldown_seconds parametrables. Apres N echecs consecutifs, le circuit s'ouvre et refuse les requetes pendant le cooldown. Apres ce delai, passe en HALF_OPEN : un seul appel autorise. Si OK, retour CLOSED. Si KO, retour OPEN.

A placer dans core/agents-py/circuit_breaker.py.

Une instance par MCP cible : un breaker pour Novamira, un pour n8n, un pour DataForSEO, etc. Les threshold et cooldown peuvent etre differents selon la criticite et la latence de chaque service.

Combiner avec with_retry : le retry gere les transients dans un meme call, le circuit breaker protege contre les downtimes prolonges du service. Les deux sont complementaires.

ECC mentionne circuit breaker dans la description du skill source mais ne l'implemente pas. Cette adaptation comble ce trou.

## Logging structure

Tous les agents heritent de self._log via BaseContentAgent (logger nomme agents plus self.name). Le logger schoolsWP ecrit dans logs/agents.log avec rotation 10 MB par 5 fichiers, et envoie WARNING plus a la console.

Pattern recommande pour logger une exception sans la perdre : capturer l'exception typee, logger le contexte (provider, operation, excerpt), puis re-raise une PipelineError pour que l'orchestrateur decide de la suite. Voir examples/agent_with_retry.py.

Anti-pattern a eviter : except suivi de return string vide. C'est exactement le silent failure que le sub-agent silent-failure-hunter cherche a traquer.

## Integration BaseContentAgent

Le BaseContentAgent ne fait pas de retry ni de circuit breaker par defaut. C'est le role de chaque agent fils de decider, parce que :

- Un agent simple (SeoWriterAgent, ContentSummarizer) n'a probablement pas besoin de retry : si le LLM echoue, on remonte.
- Un agent pipeline (article_pipeline, content_factory) doit retry les transients sur chaque etape ET arreter sur les permanents.
- Un agent qui appelle des MCP externes doit utiliser le circuit breaker en plus du retry.

Voir examples/agent_with_retry.py pour le pattern type d'un agent qui combine retry plus parsing strict plus PipelineError en cas d'echec definitif.

## Checklist pre-commit

A passer mentalement avant de commiter un agent ou un pipeline :

- [ ] Aucun except sans action ou return vide dans le code (verif via grep).
- [ ] Toute exception typee derive d'AgentError avec un code et une flag retryable explicite.
- [ ] Les calls LLM dans une boucle ou un pipeline utilisent with_retry pour les transients.
- [ ] Les calls MCP externes utilisent un CircuitBreaker dedie (une instance par serveur).
- [ ] Le logger self._log enregistre le contexte de l'exception (provider, operation, excerpt) avant de raise.
- [ ] Le markdown de sortie ne contient JAMAIS de stack trace ou de message d'erreur brut visible par l'utilisateur final.
- [ ] La docstring de run() documente les exceptions levees (AgentError, sous-classes).
- [ ] Les tests pytest existants couvrent au moins un cas d'erreur (LLM rate limit, MCP down, parse echec).

## Renvois

- Skill source : projects/everything-claude-code/skills/error-handling (couvre aussi TS et Go, hors-scope schoolsWP).
- BaseContentAgent : core/agents-py/base.py (call_llm, self._log, providers).
- silent-failure-hunter agent : .claude/agents/silent-failure-hunter.md (audit complementaire pour traquer les swallow silencieux).
- agent-architecture-audit skill : .claude/skills/external-ecc/agent-architecture-audit (diagnostic 12-layer dont error handling, a invoquer avant chaque release pipeline).
- harness-optimizer agent : .claude/agents/harness-optimizer.md (tuning reliability au niveau harness).

## Limites de ce skill

- Pas de retry pour les writes (file IO, sauvegarde markdown) : par convention schoolsWP, les writes sont idempotents et n'ont pas besoin de retry.
- Pas de gestion des deadlocks Python : le pattern asyncio.Lock dans CircuitBreaker est volontairement simple, le scope n'est pas un threading robuste.
- Pas de telemetry plus metrics export : les logs fichier suffisent au scope actuel. Si besoin futur, brancher Prometheus ou OpenTelemetry sur logging handlers.
- Pas d'integration FastAPI : les agents schoolsWP ne servent pas d'API REST, c'est le scope du skill ECC source ignore ici.
- Le circuit breaker n'a pas de mode reset manuel : il attend toujours le cooldown. Si besoin de reset force, ajouter une methode reset() sur l'instance.

import asyncio
from typing import Optional

from packages.agents.back import BackAgent
from packages.agents.front import FrontAgent
from packages.agents.security import SecurityAgent
from packages.agents.seo import SeoAgent
from packages.memory.store import complete_run, save_decision, save_run
from packages.orchestrator.guardrails import Guardrails
from packages.orchestrator.router import route
from packages.orchestrator.synthesis import synthesize

# Pool d'agents partagés (stateless — safe pour concurrence asyncio)
_AGENTS = {
    "front": FrontAgent(),
    "back": BackAgent(),
    "seo": SeoAgent(),
    "security": SecurityAgent(),
}


class Orchestrator:
    """
    Orchestrateur principal.
    Flux : routing → dispatch parallèle → guardrails → synthesis → persist.
    """

    def __init__(self, event_bus=None):
        self._bus = event_bus

    async def _emit(self, run_id: str, event: dict):
        """Publie un événement SSE si un event_bus est connecté."""
        if self._bus:
            await self._bus.publish(run_id, event)

    async def run(
        self,
        run_id: str,
        task: str,
        forced_agents: Optional[list[str]] = None,
        context: dict | None = None,
    ) -> dict:
        guards = Guardrails()
        context = context or {}

        await save_run(run_id, task)
        await self._emit(run_id, {"type": "status", "status": "routing", "run_id": run_id})

        # ── 1. ROUTING ─────────────────────────────────────────────────────────
        ok, reason = guards.check()
        if not ok:
            return self._error(run_id, reason)

        if forced_agents:
            agents_to_call = [a for a in forced_agents if a in _AGENTS]
            subtasks = {a: task for a in agents_to_call}
        else:
            agents_to_call, subtasks = await route(task)
            guards.tick(tokens=300)  # Haiku routing ~300 tokens

        await self._emit(run_id, {
            "type": "routing_done",
            "agents": agents_to_call,
            "run_id": run_id,
        })

        # ── 2. DISPATCH PARALLÈLE ──────────────────────────────────────────────
        ok, reason = guards.check()
        if not ok:
            return self._error(run_id, reason)

        await self._emit(run_id, {"type": "status", "status": "running", "run_id": run_id})

        agent_tasks = {
            name: _AGENTS[name].run(
                task=subtasks.get(name, task),
                run_id=run_id,
                context=context,
            )
            for name in agents_to_call
            if name in _AGENTS
        }

        raw_results = await asyncio.gather(*agent_tasks.values(), return_exceptions=True)
        agent_outputs: dict = {}

        for name, result in zip(agent_tasks.keys(), raw_results):
            if isinstance(result, Exception):
                agent_outputs[name] = {
                    "domain": name,
                    "confidence": 0.0,
                    "recommendations": [],
                    "warnings": [f"Agent exception: {result!s}"],
                    "depends_on": [],
                    "tool_calls_made": [],
                }
            else:
                agent_outputs[name] = result
                # Persiste les décisions haute confiance automatiquement
                if result.get("confidence", 0) >= 0.8:
                    for rec in result.get("recommendations", [])[:2]:
                        await save_decision(run_id, name, rec, "auto-persist high confidence", result["confidence"])

            await self._emit(run_id, {
                "type": "agent_done",
                "agent": name,
                "output": agent_outputs[name],
                "run_id": run_id,
            })

        guards.tick(tokens=len(agent_tasks) * 700)

        # ── 3. GUARDRAILS ──────────────────────────────────────────────────────
        low_conf = guards.low_confidence_agents(agent_outputs)
        conflicts_detected = guards.detect_conflicts(agent_outputs)

        if low_conf:
            await self._emit(run_id, {
                "type": "warning",
                "warning": "low_confidence",
                "agents": low_conf,
                "run_id": run_id,
            })

        # ── 4. SYNTHESIS ───────────────────────────────────────────────────────
        ok, reason = guards.check()
        if not ok:
            # Synthèse dégradée sans appel LLM supplémentaire
            synthesis = {
                "summary": f"Synthèse partielle — {reason}",
                "priority_actions": [],
                "conflicts": [reason],
                "cross_domain_insights": [],
                "next_steps": [],
            }
        else:
            await self._emit(run_id, {
                "type": "status", "status": "synthesizing", "run_id": run_id
            })
            synthesis = await synthesize(agent_outputs)
            guards.tick(tokens=1200)

        # ── 5. RÉSULTAT FINAL ──────────────────────────────────────────────────
        result = {
            "run_id": run_id,
            "task": task,
            "agent_outputs": agent_outputs,
            "synthesis": synthesis,
            "meta": {
                **guards.summary,
                "low_confidence_agents": low_conf,
                "conflicts_detected": conflicts_detected,
                "agents_called": agents_to_call,
            },
        }

        await complete_run(run_id, result)
        await self._emit(run_id, {
            "type": "status",
            "status": "done",
            "result": result,
            "run_id": run_id,
        })

        return result

    @staticmethod
    def _error(run_id: str, reason: str) -> dict:
        return {
            "run_id": run_id,
            "error": reason,
            "agent_outputs": {},
            "synthesis": {},
            "meta": {"error": reason},
        }

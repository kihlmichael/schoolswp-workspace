import asyncio

from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from api.queue_manager import event_bus

router = APIRouter()


@router.get("/stream/{run_id}")
async def stream_run(run_id: str):
    """
    SSE stream pour suivre un run en temps réel.
    Chaque event a un champ 'data' en JSON avec 'type' parmi :
      status | routing_done | agent_done | warning | ping
    Le stream se ferme quand type=status et status=done|error.

    Usage Claude Code CLI :
      curl -N http://localhost:8000/api/stream/{run_id}
    """

    async def generator():
        q = event_bus.subscribe(run_id)
        try:
            while True:
                try:
                    data = await asyncio.wait_for(q.get(), timeout=60.0)
                    yield {"data": data}
                    # Fermeture propre quand terminé
                    if '"done"' in data or '"error"' in data:
                        break
                except asyncio.TimeoutError:
                    yield {"data": '{"type":"ping"}'}
        finally:
            event_bus.unsubscribe(run_id, q)

    return EventSourceResponse(generator())

import uuid
from datetime import datetime

from fastapi import APIRouter

from api.models import RunRequest, RunResponse, RunStatus
from api.queue_manager import job_queue

router = APIRouter()


@router.post("/run", response_model=RunResponse)
async def run_async(req: RunRequest):
    """
    Mode async : retourne run_id immédiatement.
    Le résultat est accessible via GET /api/status/{run_id}
    ou SSE GET /api/stream/{run_id}.
    Si callback_url est fourni (n8n webhook), l'API appelle ce webhook quand c'est fini.
    """
    run_id = str(uuid.uuid4())[:8]
    await job_queue.enqueue(run_id, {
        "task": req.task,
        "callback_url": req.callback_url,
        "agents": req.agents,
        "context": req.context or {},
        "created_at": datetime.utcnow().isoformat(),
    })
    return RunResponse(
        run_id=run_id,
        status=RunStatus.QUEUED,
        stream_url=f"/api/stream/{run_id}",
    )


@router.post("/run-sync")
async def run_sync(req: RunRequest):
    """
    Mode sync : attend la fin de l'exécution et retourne le résultat directement.
    Utiliser pour n8n (HTTP Request node avec timeout 60s+).
    """
    from packages.orchestrator.orchestrator import Orchestrator

    run_id = str(uuid.uuid4())[:8]
    try:
        orchestrator = Orchestrator()
        result = await orchestrator.run(
            run_id=run_id,
            task=req.task,
            forced_agents=req.agents,
            context=req.context or {},
        )
        return result
    except Exception as e:
        return {"run_id": run_id, "error": str(e), "status": "error"}


@router.get("/status/{run_id}")
async def get_status(run_id: str):
    """Polling endpoint. Retourne status + result si done."""
    status = job_queue.get_status(run_id)
    if status is None:
        return {"error": "run_id not found"}
    return status

import asyncio
import os
from contextlib import asynccontextmanager

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from api.queue_manager import event_bus, job_queue
from api.routes import run, stream
from packages.memory.store import init_db
from packages.orchestrator.orchestrator import Orchestrator


async def worker():
    """
    Worker background unique.
    Dépile les jobs de job_queue et les exécute en tâches asyncio parallèles.
    Gère le callback n8n si callback_url est fourni.
    """
    orchestrator = Orchestrator(event_bus=event_bus)

    while True:
        job = await job_queue.dequeue()
        run_id = job["run_id"]

        async def process(j=job, rid=run_id):
            try:
                result = await orchestrator.run(
                    run_id=rid,
                    task=j["task"],
                    forced_agents=j.get("agents"),
                    context=j.get("context", {}),
                )
                job_queue.update(rid, "done", result)

                # Callback n8n si fourni
                if callback := j.get("callback_url"):
                    async with httpx.AsyncClient(timeout=30) as client:
                        await client.post(callback, json=result)

            except Exception as e:
                error_payload = {"error": str(e), "run_id": rid}
                job_queue.update(rid, "error", error_payload)
                await event_bus.publish(rid, {"type": "status", "status": "error", "error": str(e)})

        asyncio.create_task(process())


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    asyncio.create_task(worker())
    yield


app = FastAPI(
    title="Multi-Agent Orchestration API",
    description="Orchestrateur multi-agents : Front / Back / SEO. Piloté par n8n.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(run.router, prefix="/api", tags=["runs"])
app.include_router(stream.router, prefix="/api", tags=["streaming"])


@app.get("/health", tags=["infra"])
async def health():
    return {"status": "ok", "model": os.getenv("MODEL_ORCHESTRATOR", "claude-sonnet-4-6")}


def start():
    """Entrypoint pour pyproject.toml [project.scripts]"""
    import uvicorn
    uvicorn.run(
        "api.main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
        reload=True,
    )

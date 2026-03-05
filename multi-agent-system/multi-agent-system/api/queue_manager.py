import asyncio
import json
from collections import defaultdict


class EventBus:
    """SSE pub/sub par run_id. Chaque subscriber reçoit un asyncio.Queue."""

    def __init__(self):
        self._subscribers: dict[str, list[asyncio.Queue]] = defaultdict(list)

    def subscribe(self, run_id: str) -> asyncio.Queue:
        q: asyncio.Queue = asyncio.Queue()
        self._subscribers[run_id].append(q)
        return q

    def unsubscribe(self, run_id: str, q: asyncio.Queue):
        if run_id in self._subscribers:
            try:
                self._subscribers[run_id].remove(q)
            except ValueError:
                pass

    async def publish(self, run_id: str, event: dict):
        data = json.dumps(event, ensure_ascii=False)
        for q in list(self._subscribers.get(run_id, [])):
            await q.put(data)


class JobQueue:
    """Queue FIFO des jobs à traiter par le worker background."""

    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()
        self._runs: dict[str, dict] = {}

    async def enqueue(self, run_id: str, job: dict):
        self._runs[run_id] = {**job, "status": "queued"}
        await self._queue.put({"run_id": run_id, **job})

    async def dequeue(self) -> dict:
        return await self._queue.get()

    def get_status(self, run_id: str) -> dict | None:
        return self._runs.get(run_id)

    def update(self, run_id: str, status: str, result: dict | None = None):
        if run_id in self._runs:
            self._runs[run_id]["status"] = status
            if result is not None:
                self._runs[run_id]["result"] = result


# Singletons partagés dans toute l'app
event_bus = EventBus()
job_queue = JobQueue()

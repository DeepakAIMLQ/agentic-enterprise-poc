import asyncio
from core.task_queue import get_next_task, complete_task
from core.dead_letter_queue import add_failed_task
from core.retry import run_with_timeout  # Import the new timeout wrapper
from agents import brd_agent, research_agent  # Add ARCHITECT if exists
from core.task_queue import EXECUTED_TASKS

AGENTS = {
    "BRD": brd_agent.execute,
    "MARKET_RESEARCH": research_agent.execute,
    # "ARCHITECT": architect_agent.execute  # Uncomment when ready
}

async def worker(agent_name):
    while True:
        task = get_next_task(agent_name)
        if not task:
            await asyncio.sleep(1)
            continue

        # ← HERE: Idempotency check before execution
        if task.id in EXECUTED_TASKS:
            complete_task(task.id)  # Auto-complete duplicates
            continue

        handler = AGENTS.get(task.type)
        if not handler:
            continue

        try:
            await run_with_timeout(handler, task, timeout=90)
            complete_task(task.id)  # Adds to EXECUTED_TASKS via task_queue
        except asyncio.TimeoutError:
            task.status = "FAILED"
            add_failed_task(task, "Handler timed out after 90s")
        except Exception as e:
            task.status = "FAILED"
            add_failed_task(task, str(e))

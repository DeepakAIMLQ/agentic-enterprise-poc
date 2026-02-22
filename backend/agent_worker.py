from core.task_queue import get_next_task, complete_task
from agents import brd_agent, research_agent

AGENTS = {
    "BRD": brd_agent.execute,
    "MARKET_RESEARCH": research_agent.execute
}

def agent_loop(agent_name):
    while True:
        task = get_next_task(agent_name)
        if not task:
            break

        handler = AGENTS.get(task.type)
        if handler:
            handler(task)
            complete_task(task.id)
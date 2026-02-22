from agents.brd_agent import run as brd_agent
from agents.research_agent import run as research_agent
from core.state import PipelineState
from core.governance import safety_check
from core.memory import save_memory
from agents.planner_agent import run as planner
from agent_registry import AGENT_MAP
import uuid

from core.tasks import Task
from core.task_queue import add_task
from agent_worker import agent_loop

PIPELINE_DB = {}

def start_pipeline(idea: str):
    add_task(Task(type="BRD", input=idea))

    # run agents
    agent_loop("BRD")
    agent_loop("MARKET_RESEARCH")

    return {"status": "Pipeline executed"}

# def start_pipeline(idea: str):
#     state = PipelineState(idea=idea)

#     plan = planner(idea)
#     state.plan = plan
#     state.status = "PLANNED"

#     PIPELINE_DB[idea] = state
#     return state


def run_next_step(idea: str):
    state = PIPELINE_DB.get(idea)

    if not state:
        return {"error": "Pipeline not found"}

    remaining = [s for s in state.plan if s not in state.completed_steps]

    if not remaining:
        state.status = "COMPLETED"
        return state

    step = remaining[0]
    agent = AGENT_MAP.get(step)

    if not agent:
        state.completed_steps.append(step)
        return state

    result = agent(state.idea if step == "CREATE_BRD" else state.brd)

    if step == "CREATE_BRD":
        state.brd = result
    elif step == "GET_MARKET_RESEARCH":
        state.market_research = result

    state.completed_steps.append(step)
    state.status = f"STEP_{step}_DONE"

    return state

def approve_brd(idea: str, approved: bool, feedback: str = ""):
    state = PIPELINE_DB.get(idea)

    if not state:
        return {"error": "Pipeline not found"}

    if not approved:
        state.status = "BRD_REJECTED"
        state.feedback = feedback
        return state

    # Governance check
    check = safety_check(state.brd)
    if not check["approved"]:
        state.status = "BRD_REJECTED"
        state.feedback = check["reason"]
        return state

    state.status = "BRD_APPROVED"

    # Continue pipeline automatically
    state.market_research = research_agent(state.brd)
    state.status = "COMPLETED"

    return state

##step 3 code
# def start_pipeline(idea: str):
#     state = PipelineState(idea=idea)

#     state.brd = brd_agent(idea)
#     state.status = "WAITING_FOR_BRD_APPROVAL"

#     PIPELINE_DB[idea] = state
#     return state

##Step 2 Code 
#def run_pipeline(idea: str):
#    state = PipelineState(idea=idea)

#    state.brd = brd_agent(state.idea)
#    save_memory(str(uuid.uuid4()), f"BRD completed for idea: {idea}", {"event": "BRD_DONE"})

#    state.market_research = research_agent(state.brd)
#   save_memory(str(uuid.uuid4()), "Market research completed", {"event": "RESEARCH_DONE"})

#    return state.model_dump()

from agents.brd_agent import run as brd_agent
from agents.research_agent import run as research_agent
from core.state import PipelineState
from core.memory import save_memory
import uuid

def run_pipeline(idea: str):
    state = PipelineState(idea=idea)

    state.brd = brd_agent(state.idea)
    save_memory(str(uuid.uuid4()), f"BRD completed for idea: {idea}", {"event": "BRD_DONE"})

    state.market_research = research_agent(state.brd)
    save_memory(str(uuid.uuid4()), "Market research completed", {"event": "RESEARCH_DONE"})

    return state.model_dump()

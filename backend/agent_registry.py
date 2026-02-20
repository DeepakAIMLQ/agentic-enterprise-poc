from agents.brd_agent import run as brd
from agents.research_agent import run as research

AGENT_MAP = {
    "CREATE_BRD": brd,
    "GET_MARKET_RESEARCH": research
}
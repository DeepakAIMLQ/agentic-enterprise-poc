from core.llm import call_llm
import json

AVAILABLE_AGENTS = [
    "CREATE_BRD",
    "GET_MARKET_RESEARCH",
    "DEFINE_TECH_STACK",
    "GENERATE_PRD",
    "DESIGN_ARCHITECTURE"
]

def run(idea:str):
    prompt = f"""
    You are an AI project planner.

    Based on the product idea below, decide which steps are required
    to transform it into a production-ready software system.

    Available steps:
    {AVAILABLE_AGENTS}

    Return ONLY a JSON array of steps in execution order.

    Idea:
    {idea}
    """

    response=call_llm(prompt)

    try:
        return json.laod(response)
    except:
        return ["CREATE_BRD", "GET_MARKET_RESEARCH"]


from core.llm import call_llm

def run(brd: str):
    prompt = f"""
    Based on this BRD, provide a market research summary:
    - Target users
    - Existing solutions / competitors
    - Market trends
    - Risks
    BRD:
    {brd}
    """
    return call_llm(prompt)
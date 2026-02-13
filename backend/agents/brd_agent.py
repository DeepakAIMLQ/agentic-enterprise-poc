from core.llm import call_llm

def run(idea: str):
    prompt = f"""
    Convert the following idea into a structured Business Requirements Document (BRD):
    Idea: {idea}

    Provide:
    - Problem Statement
    - Business Objectives
    - In-Scope
    - Out-of-Scope
    - Stakeholders
    - Success Metrics (KPIs)
    """
    return call_llm(prompt)
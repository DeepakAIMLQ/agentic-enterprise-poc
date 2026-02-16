# backend/agents/brd_agent.py
from core.llm import call_llm
from core.memory import save_memory
import uuid

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
    brd = call_llm(prompt)
    save_memory(id=str(uuid.uuid4()), text=brd, metadata={"type": "BRD"})
    return brd

#from core.memory import save_memory
#import uuid
from core.llm import call_llm
from core.tasks import Task
from core.task_queue import add_task
from core.project_memory import write

def execute(task):
    idea = task.input

    prompt = f"""
    # Convert the following idea into a structured Business Requirements Document (BRD):
    # Idea: {idea}

    # Provide:
    # - Problem Statement
    # - Business Objectives
    # - In-Scope
    # - Out-of-Scope
    # - Stakeholders
    # - Succe
    """
    brd = call_llm(prompt)
    write("BRD", brd)

    # Delegate research automatically
    add_task(Task(type="MARKET_RESEARCH", input=brd))

    return brd

##def run(idea: str):
    # prompt = f"""
    # Convert the following idea into a structured Business Requirements Document (BRD):
    # Idea: {idea}

    # Provide:
    # - Problem Statement
    # - Business Objectives
    # - In-Scope
    # - Out-of-Scope
    # - Stakeholders
    # - Success Metrics (KPIs)
    # """
    # brd = call_llm(prompt)
    # save_memory(id=str(uuid.uuid4()), text=brd, metadata={"type": "BRD"})
    # return brd

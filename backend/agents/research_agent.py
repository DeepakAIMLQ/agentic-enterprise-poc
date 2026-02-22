# from core.memory import save_memory, query_memory
# import uuid
from core.llm import call_llm
from core.tasks import Task
from core.task_queue import add_task
from core.project_memory import write

def execute(task):
    brd = task.input

    prompt = f"Perform market research based on:\n{brd}"
    research = call_llm(prompt)

    write("MARKET_RESEARCH", research)

    # delegate architecture design
    add_task(Task(type="ARCHITECTURE_DESIGN", input=research))

    return research

# def run(brd: str):
#     context = query_memory("business requirements")
    
#     prompt = f"""
#     Using the following BRD and prior context, provide a market research summary:
#     Context: {context}

#     BRD:
#     {brd}

#     Provide:
#     - Target users
#     - Competitors
#     - Market trends
#     - Risks
#     """
#     research = call_llm(prompt)
#     save_memory(id=str(uuid.uuid4()), text=research, metadata={"type": "MARKET_RESEARCH"})
#     return research

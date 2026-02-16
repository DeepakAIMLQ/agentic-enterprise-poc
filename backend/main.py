from fastapi import FastAPI
from orchestrator import run_pipeline

app=FastAPI(title="Agentic Enterprise AI POC")

@app.post("/run")
def run_agents(payload:dict):
    idea=payload.get("idea")
    result=run_pipeline(idea)

    return result

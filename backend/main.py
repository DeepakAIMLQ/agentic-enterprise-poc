from fastapi import FastAPI
from orchestrator import start_pipeline, run_next_step, PIPELINE_DB

app = FastAPI()

@app.post("/start")
def start(payload: dict):
    return start_pipeline(payload["idea"])

@app.post("/next")
def next_step(payload: dict):
    return run_next_step(payload["idea"])

@app.get("/state")
def get_state(idea: str):
    return PIPELINE_DB.get(idea)

##step 3
# @app.post("/start")
# def start(payload: dict):
#     return start_pipeline(payload["idea"])


# @app.post("/approve")
# def approve(payload: dict):
#     return approve_brd(
#         idea=payload["idea"],
#         approved=payload["approved"],
#         feedback=payload.get("feedback", "")
#     )


# @app.get("/status")
# def status(idea: str):
#     return PIPELINE_DB.get(idea)


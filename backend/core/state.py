# backend/core/state.py
from pydantic import BaseModel

class PipelineState(BaseModel):
    idea: str
    brd: str | None = None
    market_research: str | None = None
    strategy: str | None = None

from typing import List, Optional
from pydantic import BaseModel

class PipelineState(BaseModel):
    idea: str

    plan: Optional[List[str]] = None
    completed_steps: List[str] = []

    brd: Optional[str] = None
    market_research: Optional[str] = None

    status: str = "CREATED"


# class PipelineState(BaseModel):
#     idea: str
#     brd: Optional[str] = None
#     market_research: Optional[str] = None

#     status: Literal[
#         "CREATED",
#         "WAITING_FOR_BRD_APPROVAL",
#         "BRD_REJECTED",
#         "BRD_APPROVED",
#         "COMPLETED"
#     ] = "CREATED"

#     feedback: Optional[str] = None


from pydantic import BaseModel
from typing import Optional
import uuid

class Task(BaseModel):
    id: str = str(uuid.uuid4())
    type: str = ""
    input: str = ""
    status: str = "PENDING"
    assigned_agent: Optional[str] = None
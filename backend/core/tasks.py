from pydantic import BaseModel
from typing import Optional
import uuid, time

class Task(BaseModel):
    id: str = str(uuid.uuid4())
    type: str = ""
    input: str = ""

    status: str = "PENDING"  # PENDING | RUNNING | DONE | FAILED
    assigned_agent: Optional[str] = None

    retries: int = 0
    max_retries: int = 3
    created_at: float = time.time()
    updated_at: float = time.time()
from pydantic import BaseModel
from typing import Optional, List
from app.core.types import ToolEvidence


class ChatIn(BaseModel):
    thread_id: str
    message: str


class ChatOut(BaseModel):
    reply: str
    evidence: List[ToolEvidence] = []
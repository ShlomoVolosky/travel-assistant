from pydantic import BaseModel
from typing import Optional


class ChatIn(BaseModel):
    thread_id: str
    message: str


class ChatOut(BaseModel):
    reply: str
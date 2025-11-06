from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel


Role = Literal["system", "user", "assistant"]


class ChatTurn(BaseModel):
    role: Role
    content: str


class Decision(BaseModel):
    intent: Literal["destination_reco", "packing", "local_attractions", "weather", "general"]
    use_weather: bool = False
    use_knowledge: bool = False
    use_search: bool = False
    query: str


class ToolEvidence(BaseModel):
    tool: str
    payload: Dict[str, Any]


class ChatResponseModel(BaseModel):
    reply: str
    evidence: List[ToolEvidence] = []
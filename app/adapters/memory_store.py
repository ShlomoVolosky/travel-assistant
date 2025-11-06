from typing import List, Dict
from app.core.types import ChatTurn
from app.ports.memory_port import MemoryPort


class InMemoryStore(MemoryPort):
    def __init__(self):
        self._db: Dict[str, List[ChatTurn]] = {}

    def get(self, thread_id: str) -> List[ChatTurn]:
        return list(self._db.get(thread_id, []))

    def put(self, thread_id: str, turn: ChatTurn) -> None:
        self._db.setdefault(thread_id, []).append(turn)
from abc import ABC, abstractmethod
from typing import List
from app.core.types import ChatTurn


class MemoryPort(ABC):
    """Port for storing and retrieving conversation turns by thread_id."""

    @abstractmethod
    def get(self, thread_id: str) -> List[ChatTurn]:
        """Return the chronological list of chat turns for a thread.
        Must return an empty list if the thread does not exist.
        """
        raise NotImplementedError(
            "MemoryPort.get must be implemented by an adapter (e.g., InMemoryStore)"
        )

    @abstractmethod
    def put(self, thread_id: str, turn: ChatTurn) -> None:
        """Append a new turn to a thread (creating it if needed)."""
        raise NotImplementedError(
            "MemoryPort.put must be implemented by an adapter (e.g., InMemoryStore)"
        )
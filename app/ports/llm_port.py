from abc import ABC, abstractmethod
from typing import List
from app.core.types import ChatTurn


class LLMPort(ABC):
"""Port defining the interface to any Large Language Model provider."""


@abstractmethod
def chat(self, messages: List[ChatTurn]) -> str:
"""Return the assistant's reply text given a list of chat turns.


Implementations must call an LLM (e.g., Ollama) and return the model's
final response content as a plain string.
"""
raise NotImplementedError(
"LLMPort.chat must be implemented by an adapter (e.g., OllamaLLM)"
)
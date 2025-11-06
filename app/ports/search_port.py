from abc import ABC, abstractmethod
from typing import List


class SearchPort(ABC):
"""Port for general web search."""


@abstractmethod
def search(self, query: str, k: int = 5) -> List[str]:
"""Return up to k concise result lines/URLs/snippets for the query."""
raise NotImplementedError(
"SearchPort.search must be implemented by an adapter (e.g., DuckDuckGoSearch)"
)
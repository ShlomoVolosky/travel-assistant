from abc import ABC, abstractmethod
from typing import List, Dict, Any


class KnowledgePort(ABC):
"""Port for encyclopedic/knowledge retrieval (e.g., Wikipedia)."""


@abstractmethod
def wiki(self, query: str, max_docs: int = 3, lang: str = "en") -> List[Dict[str, Any]]:
"""Return a list of normalized wiki docs for the given query.


Each item should look like:
{
"title": str,
"published": Optional[str],
"summary": str,
"content": str
}
"""
raise NotImplementedError(
"KnowledgePort.wiki must be implemented by an adapter (e.g., WikipediaKnowledge)"
)
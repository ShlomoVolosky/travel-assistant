from typing import List
from langchain.tools import DuckDuckGoSearchRun
from app.ports.search_port import SearchPort


class DuckDuckGoSearch(SearchPort):
    def __init__(self):
        self.tool = DuckDuckGoSearchRun()

    def search(self, query: str, k: int = 5) -> List[str]:
        # Returns a string of results by default; we split lines for simplicity
        text = self.tool.invoke(query)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return lines[:k]
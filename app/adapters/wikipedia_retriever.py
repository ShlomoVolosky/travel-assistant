from typing import List, Dict, Any
from langchain_community.retrievers import WikipediaRetriever
from app.ports.knowledge_port import KnowledgePort


class WikipediaKnowledge(KnowledgePort):
def __init__(self, lang: str = "en", max_docs: int = 5, load_all_meta: bool = False):
self.retriever = WikipediaRetriever(lang=lang, load_max_docs=max_docs, load_all_available_meta=load_all_meta)


def wiki(self, query: str, max_docs: int = 3, lang: str = "en") -> List[Dict[str, Any]]:
# retriever.invoke returns Document objects
docs = self.retriever.invoke(query)
out = []
for d in docs[:max_docs]:
out.append({
"title": d.metadata.get("title"),
"published": d.metadata.get("Published"),
"summary": d.metadata.get("summary") or d.page_content[:500],
"content": d.page_content,
})
return out
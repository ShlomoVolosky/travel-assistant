import pytest
import asyncio
from app.adapters.ollama_llm import OllamaLLM
from app.adapters.openmeteo_weather import OpenMeteoWeather
from app.adapters.wikipedia_retriever import WikipediaKnowledge
from app.adapters.duckduckgo_tool import DuckDuckGoSearch
from app.adapters.memory_store import InMemoryStore
from app.application.conversation import ConversationService


@pytest.mark.asyncio
async def test_chat_smoke():
    llm = OllamaLLM()
    weather = OpenMeteoWeather()
    knowledge = WikipediaKnowledge()
    search = DuckDuckGoSearch()
    memory = InMemoryStore()
    svc = ConversationService(llm, weather, knowledge, search, memory)

    # Use a simpler query that triggers knowledge/weather but not search
    # to avoid DuckDuckGo rate limiting in tests
    out = await svc.handle("thread-1", "What are the must-see attractions in Kyoto?")
    assert isinstance(out.reply, str) and len(out.reply) > 0
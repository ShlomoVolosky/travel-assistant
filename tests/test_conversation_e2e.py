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

    out = await svc.handle("thread-1", "Top attractions in Kyoto and expected weather tomorrow")
    assert isinstance(out.reply, str) and len(out.reply) > 0
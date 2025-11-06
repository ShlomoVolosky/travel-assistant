import asyncio
from fastapi import FastAPI
from app.adapters.ollama_llm import OllamaLLM
from app.adapters.openmeteo_weather import OpenMeteoWeather
from app.adapters.wikipedia_retriever import WikipediaKnowledge
from app.adapters.duckduckgo_tool import DuckDuckGoSearch
from app.adapters.memory_store import InMemoryStore
from app.application.conversation import ConversationService
from .schemas import ChatIn, ChatOut


app = FastAPI(title="Travel Assistant")


# Wire dependencies (ports & adapters)
llm = OllamaLLM()
weather = OpenMeteoWeather()
knowledge = WikipediaKnowledge(lang="en", max_docs=5)
search = DuckDuckGoSearch()
memory = InMemoryStore()
svc = ConversationService(llm, weather, knowledge, search, memory)


@app.post("/chat", response_model=ChatOut)
async def chat(body: ChatIn):
result = await svc.handle(thread_id=body.thread_id, user_input=body.message)
return ChatOut(reply=result.reply)


# Simple liveness
@app.get("/health")
async def health():
return {"status": "ok"}
import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.adapters.ollama_llm import OllamaLLM
from app.adapters.openmeteo_weather import OpenMeteoWeather
from app.adapters.wikipedia_retriever import WikipediaKnowledge
from app.adapters.duckduckgo_tool import DuckDuckGoSearch
from app.adapters.memory_store import InMemoryStore
from app.application.conversation import ConversationService
from .schemas import ChatIn, ChatOut


app = FastAPI(title="Travel Assistant")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return ChatOut(reply=result.reply, evidence=result.evidence)


# Simple liveness
@app.get("/health")
async def health():
    return {"status": "ok"}


# Serve the chat UI
@app.get("/")
async def root():
    static_dir = Path(__file__).parent.parent / "web" / "static"
    return FileResponse(static_dir / "index.html")
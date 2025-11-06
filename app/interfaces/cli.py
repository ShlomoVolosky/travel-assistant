import asyncio
import uuid
from app.adapters.ollama_llm import OllamaLLM
from app.adapters.openmeteo_weather import OpenMeteoWeather
from app.adapters.wikipedia_retriever import WikipediaKnowledge
from app.adapters.duckduckgo_tool import DuckDuckGoSearch
from app.adapters.memory_store import InMemoryStore
from app.application.conversation import ConversationService


async def main():
llm = OllamaLLM()
weather = OpenMeteoWeather()
knowledge = WikipediaKnowledge()
search = DuckDuckGoSearch()
memory = InMemoryStore()
svc = ConversationService(llm, weather, knowledge, search, memory)


thread_id = str(uuid.uuid4())
print("Travel Assistant CLI. Type 'exit' to quit.\n")
while True:
q = input("you> ").strip()
if q.lower() in {"exit", "quit"}: break
resp = await svc.handle(thread_id, q)
print("assistant>", resp.reply)


if __name__ == "__main__":
asyncio.run(main())
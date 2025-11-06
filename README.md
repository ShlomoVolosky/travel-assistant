# travel-assistant

# Travel Assistant (Ollama + LangChain + Hexagonal)


A conversation‑first travel planner showcasing prompt engineering, context management, and data augmentation. Uses **Ollama (gemma3)**, **LangChain Wikipedia Retriever**, **DuckDuckGo Search**, and **Open‑Meteo**.


## Features
- Handles 3+ query types: destination recommendations, packing suggestions, local attractions, weather & timing.
- Conversation‑first: keeps thread history by `thread_id`.
- Prompt engineering: guided reasoning, concise style, uncertainty handling.
- Data augmentation: Wikipedia + DuckDuckGo + Open‑Meteo; simple policy to decide when to call them.
- Hexagonal architecture: core, ports, adapters, application, interfaces.
- Error handling & telemetry.


## Quickstart
```bash
cp .env.example .env
# start Ollama
docker compose up -d ollama
# inside ollama container, pull model
docker exec -it ollama ollama pull gemma3
# start API
docker compose up -d api
# test chat
curl -s -X POST http://localhost:8080/chat \
-H 'content-type: application/json' \
-d '{"thread_id":"demo","message":"3 must-see spots in Kyoto and what to pack in October"}' | jq

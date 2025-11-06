from typing import List


class ConversationService:
def __init__(self, llm: LLMPort, weather: WeatherPort, knowledge: KnowledgePort, search: SearchPort, memory: MemoryPort):
self.llm = llm
self.weather = weather
self.knowledge = knowledge
self.search = search
self.memory = memory


async def handle(self, thread_id: str, user_input: str) -> ChatResponseModel:
# 1) Context & Decision
history: List[ChatTurn] = self.memory.get(thread_id)
decision = decide(user_input)


evidence: List[ToolEvidence] = []


# 2) External data (Data Augmentation) per decision
if decision.use_weather:
# Fallback demo coords: Tokyo if none extracted (simple MVP)
lat, lon = 35.6762, 139.6503
wz = await self.weather.forecast(lat, lon)
evidence.append(ToolEvidence(tool="weather", payload={"lat": lat, "lon": lon, "raw": wz}))


if decision.use_knowledge:
docs = self.knowledge.wiki(decision.query, max_docs=3)
if docs:
evidence.append(ToolEvidence(tool="wikipedia", payload={"docs": [{"title": d["title"], "summary": d["summary"]} for d in docs]}))


if decision.use_search:
hits = self.search.search(decision.query, k=5)
if hits:
evidence.append(ToolEvidence(tool="duckduckgo", payload={"results": hits}))


# 3) Compose messages: system + condensed evidence + history + user
evidence_text_parts = []
for e in evidence:
if e.tool == "weather":
daily = e.payload["raw"].get("daily", {})
tmax = daily.get("temperature_2m_max", [None])[0]
tmin = daily.get("temperature_2m_min", [None])[0]
evidence_text_parts.append(f"Weather: next-day max {tmax}°C / min {tmin}°C near {e.payload['lat']},{e.payload['lon']} (Source: weather)")
elif e.tool == "wikipedia":
titles = ", ".join([d["title"] for d in e.payload["docs"] if d.get("title")])
evidence_text_parts.append(f"Wikipedia summaries for: {titles} (Source: wikipedia)")
elif e.tool == "duckduckgo":
evidence_text_parts.append(f"DuckDuckGo top lines: {' | '.join(e.payload['results'])[:300]} (Source: duckduckgo)")


evidence_text = "\n".join(evidence_text_parts).strip()


messages: List[ChatTurn] = [
ChatTurn(role="system", content=system_prompt()),
]
for h in history[-8:]:
messages.append(h)
if evidence_text:
messages.append(ChatTurn(role="system", content=f"Context data to use if relevant:\n{evidence_text}"))
messages.append(ChatTurn(role="user", content=user_frame(user_input)))


# 4) LLM call
reply = self.llm.chat(messages)


# 5) Memory update & telemetry
self.memory.put(thread_id, ChatTurn(role="user", content=user_input))
self.memory.put(thread_id, ChatTurn(role="assistant", content=reply))
record_event("reply", intent=decision.intent, use_weather=decision.use_weather, use_knowledge=decision.use_knowledge, use_search=decision.use_search)


return ChatResponseModel(reply=reply, evidence=evidence)
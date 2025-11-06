from .types import Decision


WEATHER_KEYWORDS = {"weather", "rain", "temperature", "forecast", "season"}
ATTRACTION_KEYWORDS = {"things to do", "attractions", "must see", "what to visit", "tourism"}
PACKING_KEYWORDS = {"pack", "packing", "what to bring", "luggage"}
DESTINATION_KEYWORDS = {"where to go", "suggest", "recommend", "destination"}


# Very light, transparent decision policy


def decide(query: str) -> Decision:
q = query.lower()
use_weather = any(k in q for k in WEATHER_KEYWORDS)
use_knowledge = any(k in q for k in ATTRACTION_KEYWORDS | DESTINATION_KEYWORDS)
use_search = "best" in q or "top" in q or "visa" in q or "safety" in q


intent = "general"
if any(k in q for k in PACKING_KEYWORDS):
intent = "packing"
elif use_weather:
intent = "weather"
elif any(k in q for k in ATTRACTION_KEYWORDS):
intent = "local_attractions"
elif any(k in q for k in DESTINATION_KEYWORDS):
intent = "destination_reco"


return Decision(intent=intent, use_weather=use_weather, use_knowledge=use_knowledge, use_search=use_search, query=query)
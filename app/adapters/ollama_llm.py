from typing import List
from app.core.types import ChatTurn
from app.ports.llm_port import LLMPort
from config.settings import settings

# CRITICAL: use Ollama exactly as requested
from ollama import chat as ollama_chat
from ollama import ChatResponse

class OllamaLLM(LLMPort):
    def __init__(self):
        self.model = settings.ollama_model

    def chat(self, messages: List[ChatTurn]) -> str:
        payload = [{"role": m.role, "content": m.content} for m in messages]
        # example-compliant call:
        response: ChatResponse = ollama_chat(model=self.model, messages=payload)
        # Access both styles to be future-proof:
        try:
            return response["message"]["content"]
        except TypeError:
            return response.message.content

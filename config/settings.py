from pydantic import BaseModel
import os


class Settings(BaseModel):
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "gemma3")
    weather_base_url: str = os.getenv("WEATHER_BASE_URL", "https://api.open-meteo.com/v1/forecast")
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8080"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
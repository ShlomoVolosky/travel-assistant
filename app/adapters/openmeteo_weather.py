import httpx
from typing import Dict, Any
from app.ports.weather_port import WeatherPort
from config.settings import settings


class OpenMeteoWeather(WeatherPort):
    async def forecast(self, lat: float, lon: float) -> Dict[str, Any]:
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,precipitation,cloudcover",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
            "forecast_days": 3,
            "timezone": "auto",
        }
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(settings.weather_base_url, params=params)
            r.raise_for_status()
            return r.json()
from abc import ABC, abstractmethod
from typing import Dict, Any


class WeatherPort(ABC):
    """Port for weather forecasting services."""

    @abstractmethod
    async def forecast(self, lat: float, lon: float) -> Dict[str, Any]:
        """Return a minimal normalized weather payload for given coordinates.

        Expected keys (adapter may include more):
        {
            "daily": {
                "temperature_2m_max": [float, ...],
                "temperature_2m_min": [float, ...],
                "precipitation_sum": [float, ...]
            },
            "hourly": { ... },
            "timezone": str
        }
        """
        raise NotImplementedError(
            "WeatherPort.forecast must be implemented by an adapter (e.g., OpenMeteoWeather)"
        )
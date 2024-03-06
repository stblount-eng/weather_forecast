from pydantic import BaseModel
from typing import List, Tuple


class WeatherRequest(BaseModel):
    location: Tuple[float, float]


class WeatherResponse(BaseModel):
    location: str
    date: str
    temperature: float
    humidity: float


class HourlyData(BaseModel):
    time: List[str]
    temperature_2m: List[float]


class HourlyUnits(BaseModel):
    temperature_2m: str


class MeteoWeatherResponse(BaseModel):
    latitude: float
    longitude: float
    elevation: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    hourly: HourlyData
    hourly_units: HourlyUnits

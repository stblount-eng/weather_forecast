from fastapi import FastAPI
from model import WeatherResponse
from geopy import geocoders, Point
import requests
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

def get_weather_from_point(coord: Point | None) -> WeatherResponse | None:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coord.latitude}&longitude={coord.longitude}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data:", response.text)
        return None

def get_point_from_location(address: str) -> Point | None:
    geolocator = geocoders.Nominatim(user_agent="Weather App")
    location = geolocator.geocode(address)
    if location == None:
        return location
    return Point(location.latitude, location.longitude)

@app.get("/weather")
async def get_weather(address: str) -> WeatherResponse | None:
    location = (get_point_from_location(address))
    return get_weather_from_point(location)

# coord = Point(52.52, 13.419)
# print(get_point_from_location('London'))
# print(get_weather_from_point(coord))
print(asyncio.run(get_weather("London")))
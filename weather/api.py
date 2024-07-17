from pydantic import BaseModel
from models import Location
import openmeteo_requests
from dataclasses import dataclass

om = openmeteo_requests.Client()
@dataclass(frozen=True)
class OM_API_ENDPOINTS:

    forecast = "https://api.open-meteo.com/v1/forecast"

def get_current_weather(weather_params):
    responses = om.weather_api(url=OM_API_ENDPOINTS.forecast, params=weather_params)
    response = responses[0]
    current = response.Current()
    print(f'Current Temp: {current.Variables(0).Value()}')
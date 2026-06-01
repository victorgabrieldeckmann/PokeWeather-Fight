url = "http://api.weatherapi.com/v1"
from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

class WeatherApi:
    def __init__(self, weather_endpoint, city):
        self.weather_endpoint = weather_endpoint
        self.city = city

    def get_current_weather(self):
        response = requests.get(f"{url}/{self.weather_endpoint}.json?key={api_key}&q={self.city}").json()

        data = response["current"]["condition"]["text"]
        return self.normalize_weather(data.lower())

    def normalize_weather(self,data):
        match data:

            case "sunny" | "clear":
                return "sun"

            case "partly cloudy" | "cloudy" | "overcast":
                return "cloud"

            case "light rain" | "moderate rain" | "heavy rain" | "patchy rain nearby":
                return "rain"

            case "thundery outbreaks nearby" | "moderate or heavy rain with thunder":
                return "storm"

            case "light snow" | "moderate snow" | "heavy snow" | "blizzard":
                return "snow"

            case "mist" | "fog" | "freezing fog":
                return "fog"

            case _:
                return "unknown"
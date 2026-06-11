url = "http://api.weatherapi.com/v1"
from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

class WeatherApi:
    def get_current_weather(self, city):
        response = requests.get(f"{url}/current.json?key={api_key}&q={city}").json()

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
            
    def get_weather_multiplier(self, move_type, weather):
        weather_effects = {
            "sun": {
                "buff": ["Fire"],
                "debuff": ["Water"]
            },
            "rain": {
                "buff": ["Water"],
                "debuff": ["Fire"]
            },
            "storm": {
                "buff": ["Electric"],
                "debuff": ["Flying"]
            },
            "snow": {
                "buff": ["Ice"],
                "debuff": ["Grass"]
            },
            "fog": {
                "buff": ["Ghost", "Dark"],
                "debuff": ["Normal"]
            },
            "cloud": {
                "buff": ["Flying"],
                "debuff": ["Fire"]
            }
        }

        if weather not in weather_effects:
            return 1

        if move_type in weather_effects[weather]["buff"]:
            return 1.2

        if move_type in weather_effects[weather]["debuff"]:
            return 0.8

        return 1
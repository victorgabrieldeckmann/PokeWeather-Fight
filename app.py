from flask import Flask, render_template
from services.pokemon_api import PokemonAPI
from services.weather_api import WeatherApi
from models.pokemon import Pokemon
from models.battle import Battle
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

pokemon_api = PokemonAPI('Pikachu')
weather_api = WeatherApi('current', 'Mexico')
pokemon_selected = pokemon_api.get_pokemon()
pikachu = Pokemon(pokemon_selected["name"], pokemon_selected["type"], pokemon_selected["level"] ,pokemon_selected["weight"], pokemon_selected["height"], pokemon_selected["base_health"], pokemon_selected["base_attack"], pokemon_selected["base_defense"], pokemon_selected["moves"], pokemon_selected["base_speed"])

pokemon_api = PokemonAPI('Charmander')
pokemon_selected = pokemon_api.get_pokemon()
charmander = Pokemon(pokemon_selected["name"], pokemon_selected["type"], pokemon_selected["level"] ,pokemon_selected["weight"], pokemon_selected["height"], pokemon_selected["base_health"], pokemon_selected["base_attack"], pokemon_selected["base_defense"], pokemon_selected["moves"], pokemon_selected["base_speed"])

batalha = Battle()
batalha.decide_action(pikachu, charmander, )

if __name__ == "__main__":

    app.run(debug=True)
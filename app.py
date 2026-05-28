from flask import Flask, render_template
from services.pokemon_api import PokemonAPI
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

pokemon_api = PokemonAPI('Pikachu')
pokemon = pokemon_api.get_pokemon('pikachu')

print(pokemon)

if __name__ == "__main__":

    app.run(debug=True)
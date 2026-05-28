from flask import Flask, render_template
from services.pokemon_api import PokemonAPI
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

pokemon_api = PokemonAPI('Pikachu')

print(pokemon_api.get_pokemon('pikachu'))

if __name__ == "__main__":

    app.run(debug=True)
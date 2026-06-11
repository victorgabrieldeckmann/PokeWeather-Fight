from flask import Flask, render_template
from services.pokemon_api import PokemonAPI
from services.weather_api import WeatherApi
from services.pokemon_type_api import TypePokemon
from models.pokemon import Pokemon
from models.battle import Battle
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

pokemon_api = PokemonAPI('Pikachu')
pokemon_selected = pokemon_api.get_pokemon()
pikachu = Pokemon(pokemon_selected["name"], pokemon_selected["type"], pokemon_selected["level"] ,pokemon_selected["weight"], pokemon_selected["height"], pokemon_selected["base_health"], pokemon_selected["base_attack"], pokemon_selected["base_defense"], pokemon_selected["moves"], pokemon_selected["base_speed"])

pokemon_api = PokemonAPI('Charmander')
pokemon_selected = pokemon_api.get_pokemon()
charmander = Pokemon(pokemon_selected["name"], pokemon_selected["type"], pokemon_selected["level"] ,pokemon_selected["weight"], pokemon_selected["height"], pokemon_selected["base_health"], pokemon_selected["base_attack"], pokemon_selected["base_defense"], pokemon_selected["moves"], pokemon_selected["base_speed"])


batalha = Battle("Porto Alegre")

first_pokemon = (
    pikachu
    if pikachu.speed > charmander.speed
    else charmander
)

second_pokemon = (
    charmander
    if first_pokemon == pikachu
    else pikachu
)

while batalha.check_battle_status(
    first_pokemon,
    second_pokemon
) == "continue":

    print("\n------------------")
    print(f"Turn: {batalha.count_turn}")
    print(f"{pikachu.name}: {pikachu.health} HP")
    print(f"{charmander.name}: {charmander.health} HP")
    print("------------------")

    batalha.handle_turn(
        first_pokemon,
        second_pokemon
    )

    current_attacker = batalha.order_to_play[0]
    current_defender = batalha.order_to_play[1]

    print(f"{current_attacker.name}'s turn")
    batalha.print_moves(current_attacker.moves)
    move_id = int(input("Choose a move: "))

    if move_id == 0:
        batalha.decide_action(
            current_attacker,
            current_defender,
            "heal"
        )
    else:
        move = current_attacker.choose_move(move_id)

        if move:
            batalha.decide_action(
                current_attacker,
                current_defender,
                move
            )
        else:
            print("Invalid move!")
if __name__ == "__main__":

    app.run(debug=True)
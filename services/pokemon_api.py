import requests
poke_url = "https://pokeapi.co/api/v2/pokemon/"

class PokemonAPI:
    def __init__(self, name):
        self.name = name
    
    def get_pokemon(self, name):
        response = requests.get(f"{poke_url}{name}").json()
        
        moves = self.get_moves(name)

        data = {
            "name": response["name"],
            "type": response["types"][0]["type"]["name"],
            "weight": response["weight"],
            "height": response["height"],
            "health": response["stats"][0]["base_stat"],
            "attack": response["stats"][1]["base_stat"],
            "defense": response["stats"][2]["base_stat"],
            "moves": moves
        }
        
        return data

    def get_moves(self, name):

        response = requests.get(
            f"{poke_url}{name}"
        ).json()

        data = []

        for move in response["moves"][:5]:

            move_name = move["move"]["name"]

            move_data = requests.get(
                f"https://pokeapi.co/api/v2/move/{move_name}"
            ).json()

            data.append({
                "name": move_name,
                "power": move_data["power"] or 0
            })

        return data
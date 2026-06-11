import requests
from models.move import Move, StatusMove, DamageMove
poke_url = "https://pokeapi.co/api/v2/pokemon/"

class PokemonAPI:
    def __init__(self, name):
        self.name = name
    
    def get_pokemon(self):
        response = requests.get(f"{poke_url}{self.name}").json()
        level = 50        
        moves = self.get_moves(self.name)

        data = {
            "name": response["name"],
            "type": response["types"][0]["type"]["name"],
            "level": level,
            "weight": response["weight"],
            "height": response["height"],
            "base_health": int(response["stats"][0]["base_stat"]),
            "base_attack": int(response["stats"][1]["base_stat"]),
            "base_defense": int(response["stats"][2]["base_stat"]),
            "base_speed": int(response["stats"][5]["base_stat"]),
            "moves": self.create_moves(moves)
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
                "power": move_data["power"] or 0,
                "type": move_data["type"]["name"],
                "category": move_data["damage_class"]["name"],
                "target": move_data["target"]["name"],
                "stat_changes": move_data["stat_changes"]
            })

        return data
    
    def create_moves(self, moves_api):
        moves = []
        for index, move_data in enumerate(moves_api, start = 1):
            if move_data["category"] == "status":
                move = StatusMove(
                    index,
                    move_data["name"],
                    move_data["power"],
                    move_data["type"].capitalize(),
                    move_data["category"],
                    move_data["target"],
                    move_data["stat_changes"]
                )
            else:
                move = DamageMove(
                    index,
                    move_data["name"],
                    move_data["power"],
                    move_data["type"].capitalize(),
                    move_data["category"],
                    move_data["target"],
                    move_data["stat_changes"]
                )
            moves.append(move)
        return moves
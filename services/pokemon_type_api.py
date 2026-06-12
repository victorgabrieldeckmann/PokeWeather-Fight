import requests
poke_url = "https://pokeapi.co/api/v2/type"
class PokemonTypeApi:
    def get_type_effectiveness(self, attack_type, defender_type):
        response = requests.get(f"{poke_url}/{attack_type}").json()
        
        response_double_damage_to = []
        response_half_damage_to = []
        response_no_damage_to = []

        for d_damage_to in response["damage_relations"]["double_damage_to"]:
            response_double_damage_to.append(d_damage_to["name"])

        for h_damage_to in response["damage_relations"]["half_damage_to"]:
            response_half_damage_to.append(h_damage_to["name"])

        for no_damage_to in response["damage_relations"]["no_damage_to"]:
            response_no_damage_to.append(no_damage_to["name"])

        defender_type = defender_type.lower()

        if defender_type in response_no_damage_to:
            return 0

        if defender_type in response_double_damage_to:
            return 2

        if defender_type in response_half_damage_to:
            return 0.5

        return 1

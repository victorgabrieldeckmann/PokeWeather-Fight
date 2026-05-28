import requests
url = "https://pokeapi.co/api/v2/pokemon/"

class PokemonAPI:
    def __init__(self, name):
        self.name = name

    def get_pokemon(self, name):
        response = requests.get(f"{url}{name}").json()
        data = {
            "name" : response["name"],
            "weight" : response["weight"],
            "height" : response["height"],
            "abilities" : response["abilities"]
        }
        
        return data

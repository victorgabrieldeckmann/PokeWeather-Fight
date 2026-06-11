from services.weather_api import WeatherApi
from services.pokemon_type_api import TypePokemon
class Move:
    def __init__(self, name, power, type, category, target, stat_changes):
        self.name = name
        self.power = power
        self.type = type
        self.category = category
        self.target = target
        self.stat_changes = stat_changes

    def execute(self, attacker, defender):
        pass

class DamageMove(Move):
    def execute(self, attacker, defender, weather):
        type_multiplier = TypePokemon().get_type_effectiveness(self.type, defender.type)
        
        weather_multiplier = (WeatherApi().get_weather_multiplier(self.type, weather))
        
        damage = self.calculate_damage(attacker, defender) * type_multiplier * weather_multiplier

        defender.take_damage(damage)

        if weather_multiplier > 1:
            print(
                f"{self.type} moves are empowered by "
                f"the {weather} weather!"
            )

        elif weather_multiplier < 1:
            print(
                f"{self.type} moves are weakened by "
                f"the {weather} weather!"
            )

        if type_multiplier == 2:
            print("It's super effective!")
            print(f"{defender.name} received {damage} damage!")

        elif type_multiplier == 0.5:
            print("It's not very effective...")
            print(f"{defender.name} received {damage} damage!")

        elif type_multiplier == 0:
            print("It doesn't affect the opponent!")

        else:
            print(f"{defender.name} received {damage} damage!")

        print(
            f"{defender.name} HP: "
            f"{defender.health}/{defender.max_health}"
        )

    def calculate_damage(self, attacker, defender):
        return round(( 22 * self.power * attacker.attack / defender.defense ) / 50 + 2)

class StatusMove(Move):
    def execute(self, attacker, defender, weather):
        if self.target == "user":
            target_pokemon = attacker
        else:
            target_pokemon = defender

        for effect in self.stat_changes:

            stat_name = effect["stat"]["name"]

            if stat_name not in ["attack", "defense", "speed"]:
                continue

            change = effect["change"]

            old_value, new_value = target_pokemon.change_stat(
                stat_name,
                change * 10
            )

            print(
                f"{target_pokemon.name}'s "
                f"{stat_name} changed from "
                f"{old_value} to {new_value}"
            )
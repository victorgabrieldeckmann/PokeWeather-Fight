class Battle:
    def __init__(self):
        self.count_turn = 1
        self.order_to_play = []

    def decide_action(self, pokemon1, pokemon2, action):
        if action == "heal":
            self.heal_pokemon(pokemon1)
        else:
            self.start_battle(pokemon1, pokemon2, action)
    
    def start_battle(self, attacker, defender, action):
        checking_pokemons_state = self.check_battle_status(
            attacker,
            defender
        )

        if checking_pokemons_state == "continue":

            print(
                f"{attacker.name} used "
                f"{action.name.capitalize()}"
            )

            action.execute(
                attacker,
                defender
            )

            self.count_turn += 1

    def handle_turn(self, pokemon1, pokemon2):
        if not self.order_to_play:
            self.order_to_play = [pokemon1, pokemon2]

        if self.count_turn > 1:
            self.switch_turn()

        return self.order_to_play

    def switch_turn(self):
        self.order_to_play.reverse()
        return self.order_to_play

    def check_battle_status(self, pokemon1, pokemon2):
        if pokemon1.health > 0 and pokemon2.health > 0:
            return "continue"
        elif pokemon1.health > 0 and pokemon2.health == 0:
            return {"winner" : pokemon1}
        else:
            return {"winner" : pokemon2}

    def heal_pokemon(self, pokemon_to_heal):
        pokemon_to_heal.heal_pokemon()
        self.count_turn += 1
    
    def print_moves(self, moves):
        print("\n------------------")
        print("List of moves:")
        for m in moves:
            print(f"{m.name.capitalize()} - Power: {m.power} Type: {m.type}")

        print("------------------")
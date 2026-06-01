class Battle:
    def __init__(self):
        self.count_turn = 1
        self.order_to_play = []

    def decide_action(self, pokemon1, action, pokemon2 = None):
        if action == "heal":
            self.heal_pokemon(pokemon1)
        else:
            self.start_battle(pokemon1, pokemon2, action)

    def start_battle(self, pokemon1, pokemon2, action):
        checking_pokemons_state = self.check_battle_status(pokemon1, pokemon2)
        if checking_pokemons_state == "continue":
            pokemons_organized_to_play = self.handle_turn(pokemon1, pokemon2)
            self.attack_pokemon(pokemons_organized_to_play[0], pokemons_organized_to_play[1], action)
        else:
            print(f"O vencedor é {checking_pokemons_state["winner"]}!!")

    def handle_turn(self, pokemon1, pokemon2):
      if self.count_turn == 1:
        first_to_play = self.define_first_turn(pokemon1, pokemon2)
        second_to_play = pokemon1 if first_to_play == pokemon2 else pokemon2
        self.order_to_play = [first_to_play, second_to_play]
        return self.order_to_play
      else:
        return  self.switch_turn()

    def switch_turn(self):
        self.order_to_play.reverse()
        return self.order_to_play
    
    def define_first_turn(self, pokemon1, pokemon2):
        if pokemon1.speed > pokemon2.speed:
            return pokemon1
        else:
            return pokemon2

    def check_battle_status(self, pokemon1, pokemon2):
        if pokemon1.health > 0 and pokemon2.health > 0:
            return "continue"
        elif pokemon1.health > 0 and pokemon2.health == 0:
            return {"winner" : pokemon1}
        else:
            return {"winner" : pokemon2}

    def attack_pokemon(self, pokemon_attacker, pokemon_defender, move_to_use):
        damage = self.calc_damage(
            pokemon_attacker,
            pokemon_defender,
            move_to_use
        )
    
        pokemon_defender.take_damage(damage)
        self.count_turn += 1

    def heal_pokemon(self, pokemon_to_heal):
        pokemon_to_heal.heal_pokemon()
        self.count_turn += 1

    def calc_damage(self, pokemon_attacker, pokemon_defender, move_to_use):
        damage = round((22 * self.get_move_power(move_to_use) * pokemon_attacker.attack / pokemon_defender.defense) / 50 + 2)
        return damage

    def get_move_power(self, move_to_use):
        return int(move_to_use["power"])
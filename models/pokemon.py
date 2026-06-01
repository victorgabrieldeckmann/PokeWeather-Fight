class Pokemon:
    def __init__(self, name, type, level, weight, height, base_health, base_attack, base_defense, moves, base_speed):
        self.name = name
        self.type = type
        self.weight = weight
        self.height = height
        self.health = base_health + (level * 2)
        self.max_health = base_health + (level * 2)
        self.attack = base_attack + level
        self.defense = base_defense + level
        self.moves = moves
        self.speed = base_speed + level
        self.heal_potions = {"qnt": 2, "heal_points": 40}

    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
            print(f"{self.name} fainted!")
        else:
            self.health -= damage
        
    def heal_pokemon(self):
        if self.health > 0 and self.heal_potions["qnt"] > 0 and (self.health + self.heal_potions["heal_points"]) > self.max_health:
            self.health = self.max_health
            self.heal_potions["qnt"] -= 1
            print(f"{self.name} is with full health!")
        elif self.health > 0 and self.heal_potions["qnt"] > 0 and self.health < self.max_health:
            self.health += self.heal_potions["heal_points"]
            self.heal_potions["qnt"] -= 1
            print(f"{self.name} healed 8 points of health!")
        elif self.health > 0 and self.heal_potions["qnt"] == 0:
            print("You don't have more healing potions!")
        else:
            print("This pokemon is fainted!")
    
    def choose_move(self, move_to_use):
        move = next(
            (m for m in self.moves if m["name"] == move_to_use), None)
        return move
    


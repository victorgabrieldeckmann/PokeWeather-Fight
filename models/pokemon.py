class Pokemon:
    def __init__(self, name, type, weight, height, health, attack, defense, moves):
        self.name = name
        self.type = type
        self.weight = weight
        self.height = height
        self.health = health
        self.attack = attack
        self.defense = defense
        self.moves = moves

    def get_heath(self, health):
        if health >= 1:
            return self.health
        else:
            return print("Your pokemon is dead!!!")
    
    def get_type(self, type):
        return self.type 

    def get_speed(self, speed):
        return self.speed 
    
    def get_attack(self, attack):
        return self.attack 
    
    def get_defense(self, defense):
        return self.defense

    def get_moves(self, moves):
        return self.moves 

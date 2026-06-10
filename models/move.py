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
    def execute(self, attacker, defender):
        damage = self.calculate_damage(
            attacker,
            defender
        )

        defender.take_damage(damage)

        print(
            f"{defender.name} received {damage} damage!"
        )

        print(
            f"{defender.name} HP: "
            f"{defender.health}/{defender.max_health}"
        )

    def calculate_damage(self, attacker, defender):
        return round(( 22 * self.power * attacker.attack / defender.defense ) / 50 + 2)

class StatusMove(Move):
    def execute(self, attacker, defender):
        if self.target == "user":
            target_pokemon = attacker
        else:
            target_pokemon = defender

        for effect in self.stat_changes:

            stat_name = effect["stat"]["name"]

            if stat_name not in ["attack", "defense", "speed"]:
                continue

            change = effect["change"]

            target_pokemon.change_stat(
                stat_name,
                change * 10
            )

            print(
                f"{target_pokemon.name}'s "
                f"{stat_name} changed by "
                f"{change}"
            )
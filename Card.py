class Card:
    def __init__(self, name, attack=0, defense=0, healing=0, special_ability=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.healing = healing
        self.special_ability = special_ability

    def apply_effect(self, target_player, current_player=None):
        if self.attack > 0:
            target_player["health"] -= max(0, self.attack - target_player["defense"])
        if self.healing > 0 and current_player:
            current_player["health"] = min(current_player["max_health"], current_player["health"] + self.healing)
        if self.special_ability:
            self.special_ability(target_player, current_player)

    def __str__(self):

        ability_text = f"Special: {self.special_ability}" if self.special_ability else "No special ability"

        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense}, Healing: {self.healing}) - {ability_text}"


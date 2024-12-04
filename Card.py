class Card:
    def __init__(self, name, attack=0, defense=0, healing=0, special_ability=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.healing = healing
        self.special_ability = special_ability

    def apply_effect(self, target_player, current_player=None):
        # Apply attack with overflow logic
        if self.attack > 0:
            if target_player["defense"] > 0:
                # Reduce defense first
                remaining_damage = self.attack - target_player["defense"]
                target_player["defense"] = max(0, target_player["defense"] - self.attack)
                # Overflow to health if damage exceeds defense
                if remaining_damage > 0:
                    target_player["health"] -= remaining_damage
            else:
                # If no defense, apply full damage to health
                target_player["health"] -= self.attack

        # Apply healing to the current player
        if self.healing > 0 and current_player:
            current_player["health"] = min(
                current_player["max_health"], current_player["health"] + self.healing
            )

        # Apply defense boost to the current player
        if self.defense > 0 and current_player:
            current_player["defense"] += self.defense

        # Apply special ability if present
        if self.special_ability:
            self.special_ability(target_player, current_player)

    def __str__(self):
        ability_text = f"Special: {self.special_ability}" if self.special_ability else "No special ability"
        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense}, Healing: {self.healing}) - {ability_text}"

class Card:
    def __init__(self, name, attack=0, defense=0, healing=0):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.healing = healing

    def apply_effect(self, target_player, current_player):
        # If the card has attack value
        if self.attack > 0:
            if target_player.defense > 0:
                if target_player.defense >= self.attack:
                    target_player.defense -= self.attack
                else:
                    remaining_damage = self.attack - target_player.defense
                    target_player.defense = 0
                    target_player.health -= remaining_damage
            else:
                target_player.health -= self.attack

        # If the card has defense value
        if self.defense > 0:
            current_player.defense += self.defense

        # If the card has healing value
        if self.healing > 0:
            current_player.health = min(current_player.max_health, current_player.health + self.healing)

class Card:
    def __init__(self, name, attack=0, defense=0, healing=0):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.healing = healing

    def apply_effect(self, target_player, current_player):
        if self.attack > 0:
            target_player.take_damage(self.attack)

        if self.defense > 0:
            current_player.defense += self.defense

        if self.healing > 0:
            current_player.heal(self.healing)

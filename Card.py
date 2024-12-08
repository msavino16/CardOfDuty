#Author: Jake Gebeline and Michael Savino
#Date: 12/08/2024
#Description: This class deals with how card stats are broken down and how the deal damge, apply armor, and heal the user.

class Card:
    
    def __init__(self, name, attack=0, defense=0, healing=0):
        
        self.name = name
        self.attack = attack
        self.defense = defense
        self.healing = healing

    def apply_effect(self, target_player, current_player):
        """
        Function to deal damage, increase defense, or Heal
        
        :param target_player: The player to be affected
        :type target_player: Player
        
        :param target_player: The player using the card
        :type target_player: Player
        
        """

        if self.attack > 0:
            target_player.take_damage(self.attack)

        if self.defense > 0:
            current_player.defense += self.defense

        if self.healing > 0:
            current_player.heal(self.healing)

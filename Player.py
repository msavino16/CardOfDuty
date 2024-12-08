import random

class Player:
    def __init__(self, name, max_health=100):
        self.name = name
        self.health = max_health
        self.defense = 0
        self.max_health = max_health
        self.hand = []

    def draw_card(self, deck, discard_pile):
        
        """
        Function to deal damage, increase defense, or Heal
        
        :param deck: The current deck of cards
        :type deck: list 
        
        :param discard_pile: The discard pile that contains used cards
        :type discard_pile: list
        
        """
        if not deck:
            deck.extend(discard_pile)
            random.shuffle(deck)
            discard_pile.clear()
        self.hand.append(deck.pop())

    def take_damage(self, damage):
        
        """
        Function to take damage
        
        :param damage: The amount of damage to be done
        :type damage: int 
        
        """        

        if self.defense >= damage:
            self.defense -= damage
        else:
            remaining_damage = damage - self.defense
            self.defense = 0
            self.health = max(0, self.health - remaining_damage)

    def heal(self, amount):
        """
        Function to take heal
        
        :param amount: The amount of healing to be done
        :type amount: int 
        
        """      
        self.health = min(self.max_health, self.health + amount)

    def play_card(self, card_index, opponent, discard_pile):
        """
        This function takes the card from their hand, apply its effect, and moves it to the discard pile.
        
        :param card_index: The index of the card in the players hand
        :type card_index: int
        
        :param opponent: The opponent to be affected by the card
        :type opponent: Player
        
        :param discard_pile: The discard pile of cards
        :type discard_pile: list
        
        """      
        if 0 <= card_index < len(self.hand):
            card = self.hand.pop(card_index)
            card.apply_effect(opponent, self)
            discard_pile.append(card)

    def is_defeated(self):
        """
        This function checks whether the players health is at or below 0
        """      
        return self.health <= 0

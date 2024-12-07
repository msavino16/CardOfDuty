import random

class Player:
    def __init__(self, name, max_health=100):
        self.name = name
        self.health = max_health
        self.defense = 0
        self.max_health = max_health
        self.hand = []

    def draw_card(self, deck, discard_pile):
        if not deck:
            deck.extend(discard_pile)
            random.shuffle(deck)
            discard_pile.clear()
        self.hand.append(deck.pop())

    def play_card(self, card_index, opponent, discard_pile):
        if 0 <= card_index < len(self.hand):
            card = self.hand.pop(card_index)
            card.apply_effect(opponent, self)
            discard_pile.append(card)

    def is_defeated(self):
        return self.health <= 0
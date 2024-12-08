#Author: Jake Gebeline and Michael Savino
#Date: 12/08/2024
#Description: This file holds our test cases to test specific parts of the code to help limit the amount of time we have to use for bug fixes.

import pytest
from Player import Player
from Card import Card

@pytest.fixture
def sample_deck():
    return [
        Card("Fireball", attack=10),
        Card("Shield", defense=5),
        Card("Healing Potion", healing=15),
    ]

@pytest.fixture
def players():
    return Player(name="Player 1"), Player(name="Player 2")

def test_draw_card(sample_deck, players):
    player1, _ = players
    discard_pile = []
    
    player1.draw_card(sample_deck, discard_pile)
    
    assert len(player1.hand) == 1
    assert len(sample_deck) == 2

def test_play_card_attack(sample_deck, players):
    player1, player2 = players
    player1.hand = [Card("Fireball", attack=10)]
    discard_pile = []

    player1.play_card(0, player2, discard_pile)

    assert player2.health == 90  
    assert len(player1.hand) == 0
    assert len(discard_pile) == 1

def test_play_card_defense(sample_deck, players):
    player1, _ = players
    player1.hand = [Card("Shield", defense=5)]
    discard_pile = []

    player1.play_card(0, None, discard_pile)

    assert player1.defense == 5
    assert len(player1.hand) == 0
    assert len(discard_pile) == 1

def test_play_card_healing(sample_deck, players):
    player1, _ = players
    player1.health = 80
    player1.hand = [Card("Healing Potion", healing=15)]
    discard_pile = []

    player1.play_card(0, None, discard_pile)

    assert player1.health == 95
    assert len(player1.hand) == 0
    assert len(discard_pile) == 1

def test_health_does_not_exceed_max(players):
    player1, _ = players
    player1.health = 95
    player1.hand = [Card("Healing Potion", healing=15)]
    discard_pile = []

    player1.play_card(0, None, discard_pile)

    assert player1.health == player1.max_health
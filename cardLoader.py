#Author: Jake Gebeline and Michael Savino
#Date: 12/08/2024
#Description: This file loads the cards from an excel/csv file we have that holds the name, damage, defense, and healing.

import pandas as pd
from Card import Card

def cardLoader():
    """
    Function to load in the cards into the deck used into the game from a CSV
    """
    file_path = "cards.csv"
    df = pd.read_csv(file_path)
    deck = []
    for _, row in df.iterrows():
        name = row['name']
        attack = row.get('attack', 0)
        defense = row.get('defense', 0)
        healing = row.get('healing', 0)
        deck.append(Card(name, attack=attack, defense=defense, healing=healing))
    return deck


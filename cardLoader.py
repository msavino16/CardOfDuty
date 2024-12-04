import pandas as pd
from Card import Card

def cardLoader():
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


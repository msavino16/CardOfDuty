import pygame as py
import random
from Card import Card
from cardLoader import cardLoader

def main():
    py.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
    screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py.display.set_caption("Card Game")

    font = py.font.SysFont(None, 36)

    # Load the table image
    table = py.image.load("Table.png").convert()

    # Player stats
    player1 = {"health": 100, "defense": 0, "max_health": 100}
    player2 = {"health": 100, "defense": 0, "max_health": 100}

    # Card deck
    deck = cardLoader()

    random.shuffle(deck)
    discard_pile = []

    def draw_random_card():
        if not deck:
            deck.extend(discard_pile)
            random.shuffle(deck)
            discard_pile.clear()
        return deck.pop()

    player1_hand = [draw_random_card() for _ in range(3)]
    player2_hand = [draw_random_card() for _ in range(3)]

    turn = 1
    run = True

    def draw_text(text, x, y):
        rendered = font.render(text, True, (0, 0, 0))
        screen.blit(rendered, (x, y))

    def display_final_health():
        screen.blit(table, (0, 0)) 
        draw_text(f"Player 1 Health: {max(0, player1['health'])}", 20, 20)
        draw_text(f"Player 2 Health: {max(0, player2['health'])}", 515, 20)
        draw_text(f"Player 1 Defense: {max(0, player1['defense'])}", 20, 60)
        draw_text(f"Player 2 Defense: {max(0, player2['defense'])}", 515, 60)
        py.display.update()
        py.time.delay(1000)

    while run:

        screen.blit(table, (0, 0))

        # Display player stats
        draw_text(f"Player 1 Health: {max(0, player1['health'])}", 20, 20)
        draw_text(f"Player 2 Health: {max(0, player2['health'])}", 515, 20)

        draw_text(f"Player 1 Defense: {max(0, player1['defense'])}", 20, 60)
        draw_text(f"Player 2 Defense: {max(0, player2['defense'])}", 515, 60)

        # Display current turn
        draw_text(f"Player {turn}'s Turn", 300, 60)

        # Display player 1 hand on the left
        for i, card in enumerate(player1_hand):
            draw_text(f"{i+1}. {card.name}", 20, 150 + i * 40)

        # Display player 2 hand on the right
        for i, card in enumerate(player2_hand):
            draw_text(f"{i+1}. {card.name}", 600, 150 + i * 40)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                if turn == 1:
                    if event.key in [py.K_1, py.K_2, py.K_3]:
                        index = event.key - py.K_1
                        if 0 <= index < len(player1_hand):
                            selected_card = player1_hand.pop(index)
                            selected_card.apply_effect(player2, player1)
                            discard_pile.append(selected_card)
                            player1_hand.append(draw_random_card())
                            turn = 2
                elif turn == 2:
                    if event.key in [py.K_1, py.K_2, py.K_3]:
                        index = event.key - py.K_1
                        if 0 <= index < len(player2_hand):
                            selected_card = player2_hand.pop(index)
                            selected_card.apply_effect(player1, player2)
                            discard_pile.append(selected_card)
                            player2_hand.append(draw_random_card())
                            turn = 1

        # Check for win condition
        if player1["health"] <= 0:
            display_final_health()
            draw_text("Player 2 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False
        elif player2["health"] <= 0:
            display_final_health()
            draw_text("Player 1 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False

        py.display.update()

    py.quit()


if __name__ == "__main__":
    main()

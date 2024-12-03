import pygame as py
import random

from Card import Card

def main():
    py.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * .8)
    screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py.display.set_caption("Card Game")

    font = py.font.SysFont(None, 36)

    # player stats
    player1 = {"health": 100, "defense": 0, "max_health": 100}
    player2 = {"health": 100, "defense": 0, "max_health": 100}

    # TBD CARDS NEED EXCEL
    deck = [
        Card("Fireball", attack=100),
        Card("Shield", defense=5),
        Card("Healing Potion", healing=15),
        Card("Lightning Strike", attack=15),
        Card("Armor Up", defense=10),
    ]
    random.shuffle(deck)

    # gives player cards
    player1_hand = deck[:3]
    player2_hand = deck[3:6]

    turn = 1
    run = True

    def draw_text(text, x, y):
        rendered = font.render(text, True, (255, 255, 255))
        screen.blit(rendered, (x, y))

    while run:
        screen.fill((0, 0, 0))

        # display player stats
        draw_text(f"Player 1 Health: {player1['health']}", 20, 20)
        draw_text(f"Player 2 Health: {player2['health']}", 20, 60)

        # display current turn
        draw_text(f"Player {turn}'s Turn", 300, 20)

        # display player hands
        for i, card in enumerate(player1_hand if turn == 1 else player2_hand):
            draw_text(f"{i+1}. {card.name}", 20, 150 + i * 40)

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
                            turn = 2
                elif turn == 2:
                    if event.key in [py.K_1, py.K_2, py.K_3]:
                        index = event.key - py.K_1
                        if 0 <= index < len(player2_hand):
                            selected_card = player2_hand.pop(index)
                            selected_card.apply_effect(player1, player2)
                            turn = 1

        # check for win condition
        if player1["health"] <= 0:
            draw_text("Player 2 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False
        elif player2["health"] <= 0:
            draw_text("Player 1 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False

        py.display.update()

    py.quit()


if __name__ == "__main__":
    main()

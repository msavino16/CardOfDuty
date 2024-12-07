import pygame as py
import random
from Player import Player
from cardLoader import cardLoader

def main():
    py.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
    screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py.display.set_caption("Card Game")

    font = py.font.SysFont(None, 36)

    # load the table image
    table = py.image.load("Table.png").convert()

    # Initialize players
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")

    # Card deck
    deck = cardLoader()

    random.shuffle(deck)
    discard_pile = []

    # Initial hand setup
    for _ in range(3):
        player1.draw_card(deck, discard_pile)
        player2.draw_card(deck, discard_pile)

    turn = 1
    run = True

    def draw_text(text, x, y):
        rendered = font.render(text, True, (0, 0, 0))
        screen.blit(rendered, (x, y))

    def draw_health_bar(player, x, y, width=200, height=20):
        py.draw.rect(screen, (255, 0, 0), (x, y, width, height))  
        health_ratio = player.health / player.max_health
        current_width = int(width * health_ratio)
        py.draw.rect(screen, (0, 255, 0), (x, y, current_width, height))  

    def display_final_health():
        screen.blit(table, (0, 0))
        draw_text(f"Player 1 Health: {max(0, player1.health)}", 20, 20)
        draw_text(f"Player 2 Health: {max(0, player2.health)}", 515, 20)
        draw_text(f"Player 1 Defense: {max(0, player1.defense)}", 20, 60)
        draw_text(f"Player 2 Defense: {max(0, player2.defense)}", 515, 60)
        py.display.update()
        py.time.delay(1000)

    while run:

        screen.blit(table, (0, 0))

        # Display player stats
        draw_text(f" {max(0, player1.health)}", 210, 20)
        draw_text(f" {max(0, player2.health)}", 710, 20)

        draw_text(f"Player 1 Defense: {max(0, player1.defense)}", 20, 60)
        draw_text(f"Player 2 Defense: {max(0, player2.defense)}", 515, 60)

        draw_health_bar(player1, 12, 22)
        draw_health_bar(player2, SCREEN_WIDTH - 292, 22)

        # Display current turn
        draw_text(f"{player1.name if turn == 1 else player2.name}'s Turn", 300, 60)

        # Display player hands
        for i, card in enumerate(player1.hand):
            draw_text(f"{i+1}. {card.name}", 20, 150 + i * 40)
        for i, card in enumerate(player2.hand):
            draw_text(f"{i+1}. {card.name}", 600, 150 + i * 40)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                current_player = player1 if turn == 1 else player2
                opponent = player2 if turn == 1 else player1
                if event.key in [py.K_1, py.K_2, py.K_3]:
                    index = event.key - py.K_1
                    current_player.play_card(index, opponent, discard_pile)
                    current_player.draw_card(deck, discard_pile)
                    turn = 2 if turn == 1 else 1

        # Check for win condition
        if player1.is_defeated():
            display_final_health()
            draw_text("Player 2 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False
        elif player2.is_defeated():
            display_final_health()
            draw_text("Player 1 Wins!", 300, 300)
            py.display.update()
            py.time.delay(3000)
            run = False

        py.display.update()

    py.quit()


if __name__ == "__main__":
    main()

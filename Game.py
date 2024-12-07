import pygame as py
import random
from Player import Player
from cardLoader import cardLoader

def main():
    py.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
    screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py.display.set_caption("Card of Duty")

    font = py.font.SysFont(None, 24)
    table = py.image.load("Table.png").convert()
    
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")

    deck = cardLoader()
    random.shuffle(deck)
    discard_pile = []

    for _ in range(3):
        player1.draw_card(deck, discard_pile)
        player2.draw_card(deck, discard_pile)

    turn = 1
    run = True

    def draw_text(text, x, y, size=24, color=(0, 0, 0)):
        font = py.font.SysFont(None, size)
        rendered = font.render(text, True, color)
        screen.blit(rendered, (x, y))

    def draw_health_bar(player, x, y, width=200, height=20):
        py.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        health_ratio = player.health / player.max_health
        current_width = int(width * health_ratio)
        py.draw.rect(screen, (0, 255, 0), (x, y, current_width, height))

    def draw_card(card, x, y, card_number, width=150, height=100):
        py.draw.rect(screen, (255, 255, 255), (x, y, width, height))
        py.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)
        draw_text(f"{card_number}. {card.name}", x + 10, y + 10, size=20)
        draw_text(f"Attack: {card.attack}", x + 10, y + 40)
        draw_text(f"Defense: {card.defense}", x + 10, y + 60)
        draw_text(f"Healing: {card.healing}", x + 10, y + 80)

    def draw_player_cards(player, x_start, y_start, card_spacing=120):
        for i, card in enumerate(player.hand):
            card_y = y_start + (i * card_spacing)
            draw_card(card, x_start, card_y, card_number=i + 1)
    
    def display_final_health():
        screen.blit(table, (0, 0))
        draw_text("Player 1", 20, 10, size=28, color=(0, 0, 0))
        draw_health_bar(player1, 20, 40)
        draw_text(f"{player1.health}", 230, 40)
        draw_text(f"Player 1 Defense: {player1.defense}", 20, 70)
        draw_text("Player 2", 515, 10, size=28, color=(0, 0, 0))
        draw_health_bar(player2, 515, 40)
        draw_text(f"{player2.health}", 725, 40)
        draw_text(f"Player 2 Defense: {player2.defense}", 515, 70)
        py.display.update()
        py.time.delay(1000)

    while run:
        screen.blit(table, (0, 0))

        draw_text("Player 1", 20, 10, size=28, color=(0, 0, 0))
        draw_health_bar(player1, 20, 40)
        draw_text(f"{player1.health}", 230, 40)
        draw_text(f"Player 1 Defense: {player1.defense}", 20, 70)
        draw_text("Player 2", 515, 10, size=28, color=(0, 0, 0))
        draw_health_bar(player2, 515, 40)
        draw_text(f"{player2.health}", 725, 40)
        draw_text(f"Player 2 Defense: {player2.defense}", 515, 70)

        draw_text(f"Player {turn}'s Turn", 330, 10, size=28, color=(0, 0, 0))

        draw_player_cards(player1, 100, 200, card_spacing=120)
        draw_player_cards(player2, 500, 200, card_spacing=120)

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
            draw_text("Player 2 Wins!", 300, 300, size=36, color=(0, 0, 0))
            py.display.update()
            py.time.delay(3000)
            run = False
        elif player2.is_defeated():
            display_final_health()
            draw_text("Player 1 Wins!", 300, 300, size=36, color=(0, 0, 0))
            py.display.update()
            py.time.delay(3000)
            run = False

        py.display.update()

    py.quit()


if __name__ == "__main__":
    main()

import pygame as py

py.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Card Of Duty")

screen.fill((255, 255, 255))

player1 = py.Rect(300, 250, 50, 50)
player2 = py.Rect(400, 250, 50, 50)
selected_player = None

run = True
while run:
    screen.fill((255, 255, 255))
    py.draw.rect(screen, (255, 0, 0), player1)
    py.draw.rect(screen, (0, 255, 0), player2)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.MOUSEBUTTONDOWN:
            if player1.collidepoint(event.pos):
                selected_player = player1
            elif player2.collidepoint(event.pos):
                selected_player = player2
    
    key = py.key.get_pressed()
    if selected_player:
        if key[py.K_a] and selected_player.left > 0:
            selected_player.move_ip(-1, 0)
        if key[py.K_d] and selected_player.right < SCREEN_WIDTH:
            selected_player.move_ip(1, 0)
        if key[py.K_w] and selected_player.top > 0:
            selected_player.move_ip(0, -1)
        if key[py.K_s] and selected_player.bottom < SCREEN_HEIGHT:
            selected_player.move_ip(0, 1)
    
    py.display.update()

py.quit()

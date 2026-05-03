import pygame
import sys
from classes import Clock, Player
import time

import primitives as pr
from transforms import create_transform

# --- Exemplo de como chamar no seu módulo principal ---
# pontos_poligono = [(200, 100), (400, 100), (300, 300)]
# imagem_carregada = pygame.image.load("sua_imagem.png")
# aplicar_imagem_no_poligono(screen, pontos_poligono, imagem_carregada)

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

losango = [(300, 300), (300, 500), (100, 500), (100, 300)]
losango2 = [(600, 600), (600, 700), (500, 700), (500, 600)]

uvs = [
    (0.5, 0.0),
    (1.0, 0.5),
    (0.5, 1.0),
    (0.0, 0.5)
]

uvs2 = [
    (1.0, 0.0), 
    (1.0, 1.0), 
    (0.0, 1.0), 
    (0.0, 0.0)
]

textura = pygame.image.load('sprites/test-img.jpg').convert_alpha()
textura2 = pygame.image.load('sprites/test-img2.png').convert_alpha()

"""fix_point = (300, 300)
pointer1 = [fix_point, (300,400)]
pointer2 = [fix_point, (400,475)]
radius = 200

theta1 = 0.5
theta2 = 0.3

clock = Clock(screen,pointer2, pointer1, fix_point, radius)"""

player1 = Player(screen, losango, [textura], uvs)
player2 = Player(screen, losango2, [textura2], uvs2)

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.go_left()
            if event.key == pygame.K_d:
                player1.go_right()
            if event.key == pygame.K_LEFT:
                player2.go_left()
            if event.key == pygame.K_RIGHT:
                player2.go_right()


    #losango = create_transform(losango, theta=theta)

    #theta += 1

    #clock.run_clock(0.0, theta2)

    player1.draw_player()
    player2.draw_player()

    #pr.polygon(screen, losango, (250,0,0,250))
    
    pygame.display.flip()
    
    #time.sleep(1)
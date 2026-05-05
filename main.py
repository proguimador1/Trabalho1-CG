import pygame
import sys
import mapa as mp
width = 1000
height = 700
fullscreen = False
from classes import *

#####################
def get_mouse_pos():
    return pygame.mouse.get_pos()

#####################

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Duelo Salgado")

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

textura = pygame.image.load('coxinha.jpeg').convert_alpha()
textura2 = pygame.image.load('coxinha.jpeg').convert_alpha()

player1 = Player(screen, losango, [textura], uvs)
player2 = Player(screen, losango2, [textura2], uvs2)


while player1.dead_or_alive() and player2.dead_or_alive():
    for event in pygame.event.get():
        # TEMPORÁRIA##############
        #x, y = get_mouse_pos()
        #print(x, y)
        ##########################

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:

                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width,height))

            if event.key == pygame.K_a:
                player1.go_left()
            if event.key == pygame.K_d:
                player1.go_right()
            if event.key == pygame.K_r:
                player1.punch()
                player2.lose_life()
            if event.key == pygame.K_LEFT:
                player2.go_left()
            if event.key == pygame.K_RIGHT:
                player2.go_right()
            if event.key == pygame.K_m:
                player2.punch()
                player1.lose_life()
            

    screen.fill((200, 140, 30))

    mp.desenhar_mapa(screen, player1, player2)



    pygame.display.flip()

winner = player1 if player1.dead_or_alive() else player2

#tela de vitória vem aqui
print(f'Player {winner} venceu!')

pygame.quit()
sys.exit()
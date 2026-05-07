import pygame
import sys
import mapa as mp
width = 1000
height = 700
fullscreen = False
from classes import *
import menu2 as mn

#####################
def get_mouse_pos():
    return pygame.mouse.get_pos()

#####################

pygame.init()

mn.desenhar_menu()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Duelo Salgado")

losango1 = [(300, 600), (300, 700), (400, 700), (400, 600)]
losango2 = [(600, 600), (600, 700), (700, 700), (700, 600)]

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

sprites_player1 = [r'sprites\sprite1-guarda.jpeg', r'sprites\sprite2-corrida.jpeg', r'sprites\sprite3-soco.jpeg']

textura = [pygame.image.load(sprite).convert_alpha() for sprite in sprites_player1]
textura2 = [pygame.transform.flip(sprite, True, False) for sprite in textura]

player1 = Player(1,screen, losango1, textura, uvs)
player2 = Player(2,screen, losango2, textura2, uvs2)


while player1.dead_or_alive() and player2.dead_or_alive():
    for event in pygame.event.get():
        # TEMPORÁRIA##############
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = get_mouse_pos()
            print(x, y)
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
                player1.go_left(player2)
            if event.key == pygame.K_d:
                player1.go_right(player2)
            if event.key == pygame.K_r:
                player1.punch(player2)
            if event.key == pygame.K_LEFT:
                player2.go_left(player1)
            if event.key == pygame.K_RIGHT:
                player2.go_right(player1)
            if event.key == pygame.K_m:
                player2.punch(player1)
            

    screen.fill((200, 140, 30))

    mp.desenhar_mapa(screen, player1, player2)
    
    player1.update_sprite()
    player2.update_sprite()

    pygame.display.flip()

winner = player1 if player1.dead_or_alive() else player2

#tela de vitória vem aqui
print(f'Player {winner.get_id()} venceu!')

pygame.quit()
sys.exit()
import primitives as pr
from primitives import *
import pygame
import sys
import transforms as tr
from transforms import *
import math
import menu2 as mn
import mapa as mp
import vitoria as vt

running = True
width = 1000
height = 700
fullscreen = False
pygame.init()
vt.desenhar_tela_vitoria()
tela = pygame.display.set_mode((width, height))

def get_mouse_pos():
    return pygame.mouse.get_pos()
#mn.desenhar_menu()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # TEMPORÁRIA##############
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = get_mouse_pos()
            print(x, y)
        ##########################
    #mp.desenhar_mapa(screen, player1, player2)
    
    pygame.display.flip()

pygame.quit()
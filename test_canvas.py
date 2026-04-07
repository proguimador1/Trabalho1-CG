import pygame
import sys
from classes import Clock

import primitives as pr
from transforms import create_transform

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

fix_point = (400,400)
other_point = (500, 600)
radius = 250
relogio = Clock(screen, (250,250,250), fix_point, other_point, radius)

relogio.draw_clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detecta o pressionar da tecla Espaço
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                relogio.run_clock()
    
    pygame.display.update()
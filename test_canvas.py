import pygame
import sys
from classes import Clock

import primitives as pr
from transforms import create_transform

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))
circulo = {'center': (400, 400), 'radius': 300}
linha = [(400, 400), (500, 600)]

relogio = Clock(circulo, linha)

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detecta o pressionar da tecla Espaço
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #relogio.run_clock(screen, (250,250,250))
                ...

        #relogio.draw_clock(screen, (250,250,250))
    
    pygame.display.update()
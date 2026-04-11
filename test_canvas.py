import pygame
import sys
from classes import Clock
import time

import primitives as pr
from transforms import create_transform

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

#fix_point = (400,400)
#other_point = (500, 600)
#radius = 250
#relogio = Clock(screen, (250,250,250), fix_point, other_point, radius)

#relogio.draw_clock()

linha = [(400, 400), (500, 500)]

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detecta o pressionar da tecla Espaço
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE:
        
    pr.line(screen, linha[0], linha[1], (40, 70, 120))

    linha = create_transform(linha, theta=10)

    #print(linha)

    pygame.display.update()

    time.sleep(1)
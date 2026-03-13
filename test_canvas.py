import pygame
import sys

import primitives as pr

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    triangulo = [(400, 400), (200,600), (500,600)]
    pr.polygon(screen, triangulo, (250,250,250))
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

    retangulo = [(300, 300), (500,300), (500,400), (300,400)]
    pr.polygon(screen, retangulo, (250,250,250))

    pr.circle(screen, 50, (200, 200), (250,250,250))
import pygame
import sys

import primitives as pr

width = 800
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update( )

    
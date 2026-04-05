import pygame
import sys

import primitives as pr
import transforms as trs

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))
losango = [(300, 300), (500,500), (300,700), (100,500)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill((0,0,0))
            trs.create_transform(screen, losango, theta=45)
        
        if event.type == pygame.KEYUP:
            screen.fill((0,0,0))

    pygame.display.flip()

    pr.polygon(screen, losango, (250,250,250))
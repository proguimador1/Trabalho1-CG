import pygame
import sys

import primitives as pr
import transforms as trs

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))
losango = [(300, 300), (500,500), (300,700), (100,500)]

rotating = translating = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detecta o pressionar da tecla Espaço
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rotating = True
            
            if event.key == pygame.K_t:
                translating = True
            
        # Detecta o soltar da tecla Espaço
        if event.type == pygame.KEYUP:
            screen.fill((0,0,0))
            rotating = False
            translating = False

    if rotating:
        screen.fill((0,0,0))
        trs.create_transform(screen, losango, theta=90)
    elif translating:
        screen.fill((0,0,0))
        trs.create_transform(screen, losango, delta=(50, 50))
    else:
        pr.polygon(screen, losango, (250,250,250))
    
    pygame.display.flip()
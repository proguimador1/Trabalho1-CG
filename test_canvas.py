import pygame
import sys

import primitives as pr
from transforms import create_transform

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))
losango0 = losango =  [(300, 300), (500,500), (300,700), (100,500)]

rotating = translating = False

while True:
    screen.fill((0,0,0))
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
            rotating = False
            translating = False

    if rotating:
        losango = create_transform(losango0, theta=45)
    elif translating:
        losango = create_transform(losango0, delta=(80, -20))
    else:
        losango = losango0

    pr.polygon(screen, losango, (250,250,250))
    pr.scan_line_polygon(screen, losango, (250,250,250))
    
    pygame.display.update()
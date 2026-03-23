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

    retangulo1 = [(300, 300), (800,300), (800,750), (300,750)]
    retangulo2 = [(400, 300), (900,300), (900,650), (400,650)]
    retangulo3 = [(500, 500), (400,500), (400,100), (500,100)]
    pr.polygon(screen, retangulo1, (250,250,250))
    pr.polygon(screen, retangulo2, (250,250,250))
    pr.polygon(screen, retangulo3, (250,250,250))

    pr.scan_line_polygon(screen, retangulo1, (250,250,250))
    pr.scan_line_polygon(screen, retangulo2, (250,250,250))
    pr.scan_line_polygon(screen, retangulo3, (250,250,250))

    pr.ellipisis(screen, 50, 90, (200, 200), (250,250,250))
    pr.scan_line_ellipsis(screen, 50, 90, (200, 200), (250,250,250))


import pygame
import sys
from classes import Clock
import time

import primitives as pr
from transforms import create_transform

# --- Exemplo de como chamar no seu módulo principal ---
# pontos_poligono = [(200, 100), (400, 100), (300, 300)]
# imagem_carregada = pygame.image.load("sua_imagem.png")
# aplicar_imagem_no_poligono(screen, pontos_poligono, imagem_carregada)

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

losango = [(300, 300), (300, 500), (100, 500), (100, 300)]

uvs = [
    (0.5, 0.0),
    (1.0, 0.5),
    (0.5, 1.0),
    (0.0, 0.5)
]

textura = pygame.image.load('sprites/test-img.jpg').convert_alpha()

"""fix_point = (300, 300)
pointer1 = [fix_point, (300,400)]
pointer2 = [fix_point, (400,475)]
radius = 200

theta1 = 0.5
theta2 = 0.3

clock = Clock(screen,pointer2, pointer1, fix_point, radius)"""

while True:
    #screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pr.polygon(screen, losango, (40,120,120))

    #losango = create_transform(losango, theta=theta)

    #theta += 1

    #clock.run_clock(0.0, theta2)


    pr.scanline_texture(screen, losango, uvs, textura)

    pr.polygon(screen, losango, (30, 80, 40))

    pygame.display.flip()
    
    time.sleep(1)
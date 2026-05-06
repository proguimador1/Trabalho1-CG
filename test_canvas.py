import pygame
import sys
from classes import Clock, Player
import time

import primitives as pr
from transforms import *
from mapa import janela_viewport

# --- Exemplo de como chamar no seu módulo principal ---
# pontos_poligono = [(200, 100), (400, 100), (300, 300)]
# imagem_carregada = pygame.image.load("sua_imagem.png")
# aplicar_imagem_no_poligono(screen, pontos_poligono, imagem_carregada)

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

losango = [(300, 300), (300, 600), (200, 600), (200, 300)]
sprite_sheet = pygame.image.load('sprites/sprite1.png').convert_alpha()
uvs = [
    (0.5, 0.0),
    (1.0, 0.5),
    (0.5, 1.0),
    (0.0, 0.5)
]
"""losango2 = [(600, 600), (600, 700), (500, 700), (500, 600)]

uvs = [
    (0.5, 0.0),
    (1.0, 0.5),
    (0.5, 1.0),
    (0.0, 0.5)
]

uvs2 = [
    (1.0, 0.0), 
    (1.0, 1.0), 
    (0.0, 1.0), 
    (0.0, 0.0)
]

textura = pygame.image.load('sprites/test-img.jpg').convert_alpha()
textura2 = pygame.image.load('sprites/test-img2.png').convert_alpha()"""

"""fix_point = (300, 300)
pointer1 = [fix_point, (300,400)]
pointer2 = [fix_point, (400,475)]
radius = 200

theta1 = 0.5
theta2 = 0.3

clock = Clock(screen,pointer2, pointer1, fix_point, radius)"""

"""janela_mundo = (0, 0, 1000, 700)
viewport_tv = (500, 290, 700, 390)

player1 = Player(screen, losango, [textura], uvs)
player2 = Player(screen, losango2, [textura2], uvs2)

minipol1 = janela_viewport(janela_mundo, viewport_tv, player1.get_polygon())
minipol2 = janela_viewport(janela_mundo, viewport_tv, player2.get_polygon())

uv1 = calculate_uvs(minipol1)
uv2 = calculate_uvs(minipol2)

print(uv1)"""
#print(uv2)

while True:
    screen.fill((250, 250, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
    pr.scanline_texture(screen, losango, uvs, sprite_sheet)

    #pr.polygon(screen, losango, (250,0,0,250))
    
    pygame.display.flip()
    
    #time.sleep(1)
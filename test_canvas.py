import pygame
import sys
from classes import Clock
import time

import primitives as pr
from transforms import create_transform

def aplicar_imagem_no_poligono(screen, pontos, imagem):
    """
    Mapeia a imagem para dentro do polígono usando o algoritmo scanline.
    Cada ponto do polígono recebe a cor da imagem na coordenada correspondente.
    """
    # 1. Mapeia cada vértice do polígono para uma cor extraída da imagem
    # Usamos o bounding box do polígono para calcular as coordenadas UV (0 a 1)
    min_x = min(p[0] for p in pontos)
    max_x = max(p[0] for p in pontos)
    min_y = min(p[1] for p in pontos)
    max_y = max(p[1] for p in pontos)
    
    img_w, img_h = imagem.get_size()
    cores_nos_vertices = []
    
    for x, y in pontos:
        # Calcula a posição relativa do vértice na caixa delimitadora
        u = (x - min_x) / (max_x - min_x) if max_x != min_x else 0
        v = (y - min_y) / (max_y - min_y) if max_y != min_y else 0
        
        # Pega a cor correspondente na imagem
        img_px_x = int(u * (img_w - 1))
        img_px_y = int(v * (img_h - 1))
        
        cor = imagem.get_at((img_px_x, img_px_y))
        cores_nos_vertices.append(cor)
    
    # 2. Chama o seu algoritmo original com as cores extraídas
    pr.scanline_fill_gradiente(screen, pontos, cores_nos_vertices)

# --- Exemplo de como chamar no seu módulo principal ---
# pontos_poligono = [(200, 100), (400, 100), (300, 300)]
# imagem_carregada = pygame.image.load("sua_imagem.png")
# aplicar_imagem_no_poligono(screen, pontos_poligono, imagem_carregada)

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

losango = [(300, 300), (300, 600), (600,600), (300, 600)]

imagem = pygame.image.load('sprites/test-img.jpg').convert_alpha()

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

    pr.polygon(screen, losango, (30, 80, 40))

    aplicar_imagem_no_poligono(screen, losango, imagem)

    pygame.display.flip()
    
    time.sleep(1)
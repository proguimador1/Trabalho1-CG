from classes import Player
import primitives as pr
from primitives import *
import pygame
import sys
import transforms as tr
from transforms import *
import math

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("menu")


def centro_botao(vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[2]
    return (x1 + x2) // 2, (y1 + y2) // 2


text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()
largura = text_cox.get_width()
altura = text_cox.get_height()
for x in range(largura):
    for y in range(altura):
        r, g, b, a = text_cox.get_at((x, y))
        if r > 170 and g > 170 and b > 170:
            text_cox.set_at((x, y), (192, 192, 192, 255))

angulo = 0.02
base = [(375, 200), (375, 250), (425, 250), (425, 200)]

titulo_font = pygame.font.SysFont("ROG Fonts", 50)
font = pygame.font.SysFont("ROG Fonts", 30)
tempo = 0
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONUP:
            x, y = evento.pos
            if 250 <= x <= 550 and 250 <= y <= 300:
                print("Opção 1 selecionada")
            elif 270 <= x <= 530 and 430 <= y <= 470:
                rodando = False
    tela.fill((255, 165, 0))

    vertices = [(250, 200), (550, 200), (550, 250), (250, 250)]

    pr.ellipisis(tela, 150, 25, (400, 325), (0, 0, 0))
    pr.flood_fill(tela, (410, 335), (128, 128, 128))

    t1 = font.render("Opção 1", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t1.get_width()
    altura = t1.get_height()
    tela.blit(t1, (400 - largura / 2, 325 - altura / 2))

    vertices = [(250, 430), (550, 430), (550, 470), (250, 470)]

    pr.ellipisis(tela, 150, 25, (400, 500), (0, 0, 0))
    pr.flood_fill(tela, (410, 510), (128, 128, 128))

    t2 = font.render("Sair", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t2.get_width()
    altura = t2.get_height()
    tela.blit(t2, (400 - largura // 2, 500 - altura // 2))

    text_surface = titulo_font.render("DUELO SALGADO", True, (0, 0, 0))
    largura = text_surface.get_width()
    altura = text_surface.get_height()
    tela.blit(text_surface, (400 - largura / 2, 100))

    vertices = [
        (100, 100),
        (700, 100),
        (700, 170),
        (100, 170),
    ]
    pr.polygon(tela, vertices, (0, 0, 0))
    pr.flood_fill(tela, (110, 110), (255, 0, 0))

    vertices = [
        (330, 375),
        (370, 375),
        (400, 405),
        (430, 375),
        (470, 375),
        (410, 415),
        (470, 455),
        (430, 455),
        (400, 425),
        (370, 455),
        (330, 455),
        (390, 415),
    ]
    pr.polygon(tela, vertices, (255, 0, 0))
    pr.flood_fill(tela, (340, 377), (0, 0, 0))

    escala = 1 + 0.5 * math.sin(tempo)

    points = tr.create_transform(
        base, theta=angulo, pivot=(400, 225), scale=(escala, escala)
    )
    pr.scanline_texture(
        tela,
        points,
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        text_cox,
    )
    angulo += 0.04
    tempo += 0.1
    pygame.display.flip()


pygame.quit()
sys.exit()

from classes import Player
import primitives as pr
from primitives import *
import pygame
import sys
import transforms as tr
from transforms import *
import math

pygame.init()
pygame.mixer.init()
largura, altura = 1000, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("menu")


def centro_botao(vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[2]
    return (x1 + x2) // 2, (y1 + y2) // 2


pygame.mixer.init()

som_click = pygame.mixer.Sound("click.mp3")
som_click.set_volume(0.7)
pygame.mixer.music.load("Final Boss Battle - Rod Kim.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()
largura = text_cox.get_width()
altura = text_cox.get_height()
for x in range(largura):
    for y in range(altura):
        r, g, b, a = text_cox.get_at((x, y))
        if r > 170 and g > 170 and b > 170:
            text_cox.set_at((x, y), (60, 60, 60, 255))

angulo = 0.02
base = [(475, 260), (475, 310), (525, 310), (525, 260)]

titulo_font = pygame.font.SysFont("Arial", 50)
font = pygame.font.SysFont("Arial", 30)
tempo = 0
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONUP:
            x, y = evento.pos
            if 350 <= x <= 650 and 350 <= y <= 400:
                som_click.play()
                print("Opção 1 selecionada")
            elif 350 <= x <= 650 and 525 <= y <= 575:
                som_click.play()
                rodando = False
    tela.fill((255, 120, 0))

    # BOTAO INICIAR
    vertices = [(350, 250), (650, 250), (650, 300), (350, 300)]

    pr.ellipisis(tela, 150, 25, (500, 375), (0, 0, 0))
    pr.flood_fill(tela, (510, 385), (170, 170, 170))

    t1 = font.render("INICIAR", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t1.get_width()
    altura = t1.get_height()
    tela.blit(t1, (500 - largura / 2, 375 - altura / 2))

    # BOTAO SAIR
    vertices = [(350, 480), (650, 480), (650, 520), (350, 520)]

    pr.ellipisis(tela, 150, 25, (500, 550), (0, 0, 0))
    pr.flood_fill(tela, (510, 560), (60, 60, 60))

    t2 = font.render("SAIR", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t2.get_width()
    altura = t2.get_height()
    tela.blit(t2, (500 - largura // 2, 550 - altura // 2))

    # TITULO
    text_surface = titulo_font.render("DUELO SALGADO", True, (0, 0, 0))
    largura = text_surface.get_width()
    altura = text_surface.get_height()
    tela.blit(text_surface, (500 - largura / 2, 150))

    vertices = [
        (200, 150),
        (800, 150),
        (800, 220),
        (200, 220),
    ]
    pr.polygon(tela, vertices, (0, 0, 0))
    pr.flood_fill(tela, (210, 160), (255, 0, 0))

    # X ENTRE OS BOTOES
    vertices = [
        (430, 425),
        (470, 425),
        (500, 455),
        (530, 425),
        (570, 425),
        (510, 465),
        (570, 505),
        (530, 505),
        (500, 475),
        (470, 505),
        (430, 505),
        (490, 465),
    ]
    pr.polygon(tela, vertices, (255, 0, 0))
    pr.flood_fill(tela, (440, 427), (0, 0, 0))

    escala = 1 + 0.5 * math.sin(tempo)

    CX, CY = 500, 285
    points = base

    points = tr.create_transform(points, delta=(-CX, -CY))

    points = [(x * escala, y * escala) for x, y in points]

    points = tr.create_transform(points, theta=angulo)

    points = tr.create_transform(points, delta=(CX, CY))

    pr.circle(tela, 52, (500, 285), (0, 0, 0))
    pr.flood_fill(tela, (510, 285), (60, 60, 60))

    pr.scanline_texture(
        tela,
        points,
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        text_cox,
    )

    angulo += 0.2
    tempo += 0.5

    pygame.display.flip()


pygame.quit()
sys.exit()

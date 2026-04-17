import primitives as pr
from primitives import *
import pygame
import sys

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("menu")


def centro_botao(vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[2]
    return (x1 + x2) // 2, (y1 + y2) // 2


titulo_font = pygame.font.SysFont("ROG Fonts", 50)
font = pygame.font.SysFont("ROG Fonts", 30)
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONUP:
            x, y = evento.pos
            if 250 <= x <= 550 and 300 <= y <= 350:
                print("Opção 1 selecionada")
            elif 270 <= x <= 530 and 430 <= y <= 470:
                rodando = False
    tela.fill((255, 165, 0))

    vertices = [(250, 300), (550, 300), (550, 350), (250, 350)]
    polygon(tela, vertices, (0, 0, 0))
    t1 = font.render("Opção 1", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t1.get_width()
    altura = t1.get_height()
    tela.blit(t1, (cx - largura // 2, cy - altura // 2))

    vertices = [(270, 430), (530, 430), (530, 470), (270, 470)]
    polygon(tela, vertices, (0, 0, 0))
    t2 = font.render("Sair", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t2.get_width()
    altura = t2.get_height()
    tela.blit(t2, (cx - largura // 2, cy - altura // 2))

    text_surface = titulo_font.render("LUTA NA CANTINA", True, (0, 0, 0))
    largura = text_surface.get_width()
    altura = text_surface.get_height()
    tela.blit(text_surface, (400 - largura / 2, 100))
    pygame.display.flip()

pygame.quit()
sys.exit()

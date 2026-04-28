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
            if 250 <= x <= 550 and 250 <= y <= 300:
                print("Opção 1 selecionada")
            elif 270 <= x <= 530 and 430 <= y <= 470:
                rodando = False
    tela.fill((255, 165, 0))

    vertices = [(250, 250), (550, 250), (550, 300), (250, 300)]

    ellipisis(tela, 150, 25, (400, 275), (0, 0, 0))
    flood_fill(tela, (410, 285), (128, 128, 128))

    t1 = font.render("Opção 1", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t1.get_width()
    altura = t1.get_height()
    tela.blit(t1, (400 - largura // 2, 325 - altura // 2))

    vertices = [(250, 430), (550, 430), (550, 470), (250, 470)]

    ellipisis(tela, 150, 25, (400, 450), (0, 0, 0))
    flood_fill(tela, (410, 460), (128, 128, 128))

    t2 = font.render("Sair", True, (0, 0, 0))
    cx, cy = centro_botao(vertices)
    largura = t2.get_width()
    altura = t2.get_height()
    tela.blit(t2, (400 - largura // 2, 500 - altura // 2))

    text_surface = titulo_font.render("LUTA NA CANTINA", True, (0, 0, 0))
    largura = text_surface.get_width()
    altura = text_surface.get_height()
    tela.blit(text_surface, (400 - largura / 2, 100))

    vertices = [
        (100, 100),
        (700, 100),
        (700, 170),
        (100, 170),
    ]
    polygon(tela, vertices, (0, 0, 0))
    flood_fill(tela, (110, 110), (255, 0, 0))

    vertices = [
        (330, 325),
        (370, 325),
        (400, 355),
        (430, 325),
        (470, 325),
        (410, 365),
        (470, 405),
        (430, 405),
        (400, 375),
        (370, 405),
        (330, 405),
        (390, 365),
    ]
    pr.polygon(tela, vertices, (0, 0, 0))
    pr.flood_fill(tela, (110, 110), (128, 128, 128))

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

    pr.scan_line_ellipsis(tela, 12, 17, (400, 251), (230, 140, 40))  # 8, 12, (670,566)
    pr.scan_line_ellipsis(tela, 15, 15, (400, 255), (230, 140, 40))  # 10,10,(670,570)
    pr.scan_line_ellipsis(tela, 7, 7, (400, 240), (230, 140, 40))  # 2,2,(670,554)
    pygame.display.flip()


pygame.quit()
sys.exit()

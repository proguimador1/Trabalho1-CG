import primitives as pr
from primitives import *
import pygame
from transforms import *
import transforms as tr
import sys
width = 1000
height = 700

screen = pygame.display.set_mode((width, height))

def get_mouse_pos():
    return pygame.mouse.get_pos()
def desenhar_menu():
    
    angulo = 0.02
    tempo = 0
    text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()

    largura = text_cox.get_width()
    altura = text_cox.get_height()

    for x in range(largura):
        for y in range(altura):
            r, g, b, a = text_cox.get_at((x, y))

            if r > 170 and g > 170 and b > 170:
                text_cox.set_at((x, y), (100, 100, 100, 255))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # TEMPORÁRIA##############
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = get_mouse_pos()
            print(x, y)
        ##########################
        

        pygame.display.flip()

        # Pintando screen toda
        pr.flood_fill(screen, (25,25), (255, 120, 0))

        #pr.flood_fill(screen, (25,25), (23, 62, 101))

        # Variáveis para as fontes
        # Fonte do título
        titulo_fonte = pygame.font.SysFont("Arial", 50)
        texto_titulo = titulo_fonte.render("DUELO SALGADO", True, (255,255,255))

        # Fonte do botão
        botoes_fonte = pygame.font.SysFont("Arial", 30)

        screen.blit(texto_titulo, (320, 110))

        # Poligono do título
        pr.polygon(screen, [(250,95),(750,95),(750,175),(250,175)], (255,255,255))
        pr.flood_fill(screen, (282,133), (0,0,0)) # Azul petróleo (0,0,0)
        pr.flood_fill(screen, (335, 146), (0,0,0))

        # Aplicações do floodfill em áreas que não estavam sendo pintadas
        pr.flood_fill(screen, (443 ,150), (0,0,0))
        pr.flood_fill(screen, (513, 137), (0,0,0))
        pr.flood_fill(screen, (595, 137), (0,0,0))
        pr.flood_fill(screen, (624, 143), (0,0,0))
        pr.flood_fill(screen, (653, 144), (0,0,0))

        # Botão de Iniciar
        texto_iniciar = botoes_fonte.render("INICIAR", True, (255,255,255))
        screen.blit(texto_iniciar, (460,335))
        pr.ellipisis(screen, 150, 35, (500,350), (0,0,0))
        pr.flood_fill(screen, (370,355), (100,100,100))

        # Coreeção do que não foi pintado direito pelo floodfill entre as letras
        pr.flood_fill(screen, (540,348), (100,100,100))
        pr.flood_fill(screen, (525, 352), (100,100,100))

        # Símbolo do X entre os botões
        pr.polygon(
            screen,
            [(430, 419), (470, 419), (500, 449), (530, 419),
             (570, 419), (510, 459), (570, 499), (530, 499),
             (500, 469), (470, 499), (430, 499), (490, 459)],
            (255,255,255)
        )
        pr.flood_fill(screen, (500,460), (0,0,0))

        # Botão de sair
        texto_sair = botoes_fonte.render("SAIR", True, (255,255,255))
        screen.blit(texto_sair, (475, 555))

        pr.ellipisis(screen, 150, 35, (500, 570), (0,0,0))

        pr.flood_fill(screen, (390, 571), (100,100,100))

        # Correção de falhas do floodfill no botão sair
        pr.flood_fill(screen, (498,571), (100,100,100))
        pr.flood_fill(screen, (521,567), (100,100,100))

        # Bordas de scanline
        # pr.scan_line_polygon(
        #     screen,
        #     [(0,0),(999,0),(999,80),(0,80)],
        #     [(0, 0, 20), (0, 0, 50), (0, 0, 80),
        #      (0, 20, 110), (0, 35, 130), (5, 45, 145),
        #      (12, 52, 155), (18, 58, 165), (23, 62, 101)]
        # )

        # Círculo
        pr.circle(screen, 55, (500,240), (100,100,100))
        pr.flood_fill(screen, (500,240), (100,100,100))



        
        escala = 1 + 0.5 * math.sin(tempo)
        base = [
    (535, 240),
    (500, 275),
    (465, 240),
    (500, 205)
]

        CX, CY = 500, 240
        points = base

        points = tr.create_transform(points, delta=(-CX, -CY))

        points = [(x * escala, y * escala) for x, y in points]

        points = tr.create_transform(points, theta=angulo)

        points = tr.create_transform(points, delta=(CX, CY))

        pr.circle(screen, 55, (500, 240), (0, 0, 0))
        pr.flood_fill(screen, (510, 240), (100, 100, 100))

        pr.scanline_texture(screen, points,[(0, 0), (0, 1), (1, 1), (1, 0)],text_cox,)

        angulo += 0.05
        tempo += 0.01
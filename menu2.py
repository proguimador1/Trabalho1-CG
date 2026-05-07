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
    # Nomeação do canva como Menu
    pygame.display.set_caption("Menu")

    # Inicialização das variáveis para a rotação dentro do looping
    angulo = 0.02
    tempo = 0

    # Leitura da textura da coxinha
    text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()

    # Captura das dimensões da textura da coxinha
    largura = text_cox.get_width()
    altura = text_cox.get_height()
    
    # Aplicação para limpar bordas desnecessárias da textura
    for x in range(largura):
        for y in range(altura):
            r, g, b, a = text_cox.get_at((x, y))

            if r > 170 and g > 170 and b > 170:
                text_cox.set_at((x, y), (115, 85, 41, 255))

    # Leitura da textura do player normal
    textura_player = pygame.image.load(r"sprites\sprite3_soco.jpeg").convert_alpha()

    # Captura das dimensões da textura do stickman normal
    largura_player = textura_player.get_width()
    altura_player = textura_player.get_height()

    # Aplicação para limpar bordas desnecessárias da textura
    for x in range(largura_player):
        for y in range(altura_player):
            r, g, b, a = textura_player.get_at((x, y))

            if r > 210 and g > 210 and b > 210:
                textura_player.set_at((x, y), (210, 155, 54, 255))  

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
        pr.flood_fill(screen, (25,25), (210, 155, 54))

        # Scanline gradiente aplicado ao topo do menu
        pr.scanline_fill_gradiente(screen, [(0,0),(1000,0),(1000,75),(900,65),(100,65),(0,75)], [
        (25, 15, 5),
        (35, 21, 8),
        (45, 28, 10),
        (55, 34, 12),
        (62, 38, 14),
        (78, 50, 20),
        (96, 63, 28),
        (118, 79, 40),
        (142, 98, 55)
        ])

        # Scanline gradiente aplicado à base do menu
        pr.scanline_fill_gradiente(screen, [(0,625),(100,635),(900,635),(1000,625),(1000,700),(0,700)], [
        (25, 15, 5),
        (35, 21, 8),
        (45, 28, 10),
        (55, 34, 12),
        (62, 38, 14),
        (78, 50, 20),
        (96, 63, 28),
        (118, 79, 40),
        (142, 98, 55)
        ])
        
        # Variáveis para as fontes
        # Fonte do título
        titulo_fonte = pygame.font.SysFont("Arial", 50)
        texto_titulo = titulo_fonte.render("DUELO SALGADO", True, (62, 38, 14))

        # Fonte do botão
        botoes_fonte = pygame.font.SysFont("Arial", 30)

        screen.blit(texto_titulo, (320, 110))

        # Poligono do título
        pr.polygon(screen, [(250,95),(750,95),(750,175),(250,175)], (62, 38, 14))
        pr.flood_fill(screen, (282,133), (216, 196, 160)) # Azul petróleo (0,0,0)
        pr.flood_fill(screen, (335, 146), (216, 196, 160))

        # Aplicações do floodfill em áreas que não estavam sendo pintadas
        pr.flood_fill(screen, (443 ,150), (216, 196, 160))
        pr.flood_fill(screen, (513, 137), (216, 196, 160))
        pr.flood_fill(screen, (595, 137), (216, 196, 160))
        pr.flood_fill(screen, (624, 143), (216, 196, 160))
        pr.flood_fill(screen, (653, 144), (216, 196, 160))

        # Botão de Iniciar
        texto_iniciar = botoes_fonte.render("INICIAR", True, (255,255,255))
        screen.blit(texto_iniciar, (460,335))
        pr.ellipisis(screen, 150, 35, (500,350), (245, 185, 78))
        pr.flood_fill(screen, (370,355), (62, 38, 14))

        # Coreeção do que não foi pintado direito pelo floodfill entre as letras
        pr.flood_fill(screen, (540,348), (62, 38, 14))
        pr.flood_fill(screen, (525, 352), (62, 38, 14))

        # Símbolo do X entre os botões
        pr.polygon(
            screen,
            [(430, 419), (470, 419), (500, 449), (530, 419),
             (570, 419), (510, 459), (570, 499), (530, 499),
             (500, 469), (470, 499), (430, 499), (490, 459)],
            (62, 38, 14)
        )
        pr.flood_fill(screen, (500,460), (62, 38, 14))

        # Botão de sair
        texto_sair = botoes_fonte.render("SAIR", True, (62, 38, 14))
        screen.blit(texto_sair, (475, 555))

        pr.ellipisis(screen, 150, 35, (500, 570), (62, 38, 14))

        pr.flood_fill(screen, (390, 571), (216, 196, 160))

        # Correção de falhas do floodfill no botão sair
        pr.flood_fill(screen, (498,571), (216, 196, 160))
        pr.flood_fill(screen, (521,567), (216, 196, 160))

        # Círculo
        pr.circle(screen, 55, (500,240), (216, 196, 160))
        pr.flood_fill(screen, (500,240), (216, 196, 160))



        # Rotação da coxinha
        # Definindo a variável da escala
        escala = 1 + 0.5 * math.sin(tempo)
        # Definindo a base em que a textura da coxinha está sobre
        base = [(535, 240), (500, 275), (465, 240),(500, 205)]

        # Variáveis para a rotação
        CX, CY = 500, 240

        # Rotação e Escala
        points = base

        points = tr.create_transform(points, delta=(-CX, -CY))

        points = [(x * escala, y * escala) for x, y in points]

        points = tr.create_transform(points, theta=angulo)

        points = tr.create_transform(points, delta=(CX, CY))

        pr.circle(screen, 55, (500, 240), (62, 38, 14))
        pr.flood_fill(screen, (510, 240), (115, 85, 41))

        pr.scanline_texture(screen, points,[(0, 0), (0, 1), (1, 1), (1, 0)],text_cox)

        angulo += 0.3 # padrão: 0.1
        tempo += 0.15 # padrão: 0.05

        
        # Sprites do jogador na tela
        base_text_player1 = [(100,240),(215,240),(215,500),(100,500)]
        pr.scanline_texture(screen, base_text_player1, [(0, 0), (1, 0), (1, 1), (0,1)], textura_player)

        base_text_player2 = [(785,240),(900,240),(900,500),(785,500)]
        pr.scanline_texture(screen, base_text_player2, [(1, 0), (0, 0), (0, 1), (1,1)], textura_player)

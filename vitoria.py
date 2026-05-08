import primitives as pr
from primitives import *
import pygame
from transforms import *
import transforms as tr
import sys
width = 1000
height = 700

screen = pygame.display.set_mode((width, height))


def desenhar_tela_vitoria(id_player):
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
    textura_player = pygame.image.load(r"sprites\sprite3-soco.png").convert_alpha()

    # Captura das dimensões da textura do stickman normal
    largura_player = textura_player.get_width()
    altura_player = textura_player.get_height()

    # Aplicação para limpar bordas desnecessárias da textura
    for x in range(largura_player):
        for y in range(altura_player):
            r, g, b, a = textura_player.get_at((x, y))

            if r > 210 and g > 210 and b > 210:
                textura_player.set_at((x, y), (210, 155, 54, 255))  

    rodando = True

    while rodando:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if 350 <= x <= 650 and 315 <= y <= 385:
                rodando = False

            if 350 <= x <= 650 and 535 <= y <= 605:
                pygame.quit()
                sys.exit()
        ##########################
        

        pygame.display.flip()

        # Pintando screen toda
        pr.flood_fill(screen, (25,25), (210, 155, 54))

        # Variáveis para as fontes
        # Fonte do título
        titulo_fonte = pygame.font.SysFont("Arial", 70)
        texto_titulo = titulo_fonte.render("Vitória", True, (62, 38, 14))

        # Fonte do botão
        botoes_fonte = pygame.font.SysFont("Arial", 30)

        screen.blit(texto_titulo, (315, 110))

        # Poligono do título
        pr.polygon(screen, [(250,95),(750,95),(750,300),(250,300)], (62, 38, 14))
        pr.flood_fill(screen, (282,133), (216, 196, 160)) # Azul petróleo (0,0,0)
        pr.flood_fill(screen, (335, 146), (216, 196, 160))

        texto_player_vitorioso = titulo_fonte.render(f"Player {id_player}", True, (62,38,14))
        screen.blit(texto_player_vitorioso, (510,110))

        # Aplicações do floodfill em áreas que não estavam sendo pintadas
        pr.flood_fill(screen, (400 ,160), (216, 196, 160))
        pr.flood_fill(screen, (458 ,166), (216, 196, 160))

        # Botão de sair
        texto_sair = botoes_fonte.render("SAIR", True, (255,255,255))
        screen.blit(texto_sair, (475, 385))

        pr.ellipisis(screen, 150, 35, (500, 400), (62, 38, 14))

        pr.flood_fill(screen, (390, 401), (62, 38, 14))

        # Correção de falhas do floodfill no botão sair
        pr.flood_fill(screen, (498,401), (62, 38, 14))
        pr.flood_fill(screen, (521,397), (62, 38, 14))
        
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

if __name__ == 'main':
    desenhar_tela_vitoria()
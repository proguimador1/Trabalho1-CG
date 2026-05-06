import primitives as pr
from primitives import *
import pygame
from transforms import *


width = 1000
height = 700

screen = pygame.display.set_mode((width, height))



def desenhar_menu():
    # Pintando tela toda
    pr.flood_fill(screen, (25,25), (255, 120, 0))

    #pr.flood_fill(screen, (25,25), (23, 62, 101))
   


    # Variáveis para as fontes
    #Fonte do título
    titulo_fonte= pygame.font.SysFont("Arial", 50)
    texto_titulo = titulo_fonte.render("DUELO SALGADO", True, (255,255,255))

    # Fonte do botão
    botoes_fonte = pygame.font.SysFont("Arial", 30)
    
    screen.blit(texto_titulo, (320, 115))

    # Poligono do título
    pr.polygon(screen, [(250,100),(750,100),(750,180),(250,180)], (255,255,255))
    pr.flood_fill(screen, (370,150), (12, 38, 51))
    pr.flood_fill(screen, (335, 146), (12, 38, 51))

    # Aplicações do floodfill em áreas que não estavam sendo pintadas
    pr.flood_fill(screen, (443 ,155), (12, 38, 51))
    pr.flood_fill(screen, (513, 142), (12, 38, 51))
    pr.flood_fill(screen, (595, 142), (12, 38, 51))
    pr.flood_fill(screen, (624, 148), (12, 38, 51))
    pr.flood_fill(screen, (653, 149), (12, 38, 51))


    # Botão de Iniciar
    texto_iniciar = botoes_fonte.render("INICAR",True, (255,255,255))
    screen.blit(texto_iniciar, (460,335))
    pr.ellipisis(screen, 150,35,(500,350), (0,0,0))
    pr.flood_fill(screen, (370,355), (170,170,170))

    # Coreeção do que não foi pintado direito pelo floodfill entre as letras
    pr.flood_fill(screen, (518,352), (170,170,170))
    pr.flood_fill(screen, (533, 350), (170,170,170))


    # Símbolo do X entre os botões
    pr.polygon(screen,  [(430, 419), (470, 419), (500, 449), (530, 419), (570, 419), (510, 459), (570, 499), (530, 499), (500, 469), (470, 499), (430, 499), (490, 459)], (255,255,255))
    pr.flood_fill(screen, (500,460),(0,0,0))

    # Botão de sair
    texto_sair = botoes_fonte.render("SAIR", True, (255,255,255))
    screen.blit(texto_sair, (475, 555))

    pr.ellipisis(screen, 150, 35, (500, 570), (0,0,0))

    pr.flood_fill(screen, (390, 571), (60,60,60))

    # Correção de falhas do floodfill no botão sair
    pr.flood_fill(screen, (498,571),(60,60,60))
    pr.flood_fill(screen, (521,567),(60,60,60))

    # Bordas de scanline
    #pr.scan_line_polygon(screen, [(0,0),(999,0),(999,80),(0,80)],[(0, 0, 20), (0, 0, 50), (0, 0, 80), (0, 20, 110), (0, 35, 130), (5, 45, 145), (12, 52, 155), (18, 58, 165), (23, 62, 101)])
    
    # Círculo
    pr.circle(screen, 50, (500,240), (120,120,120))
    pr.flood_fill(screen, (500,240), (120,120,120))
    
    text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()
    width_cox = text_cox.get_width()
    height_cox = text_cox.get_height()
    for x in range(width_cox):
        for y in range(height_cox):
            r, g, b, a = text_cox.get_at((x, y))
            if r > 170 and g > 170 and b > 170:
                text_cox.set_at((x, y), (23, 62, 101, 255))
    
    



    

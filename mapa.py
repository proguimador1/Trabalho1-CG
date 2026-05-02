import primitives as pr
from primitives import *
import pygame
from classes import *

losango = [(300, 300), (300, 500), (100, 500), (100, 300)]
losango2 = [(600, 600), (600, 700), (500, 700), (500, 600)]

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


def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):
    pygame.init()

    textura = pygame.image.load('coxinha.jpeg').convert_alpha()
    textura2 = pygame.image.load('coxinha.jpeg').convert_alpha()

    player1 = Player(screen, losango, [textura], uvs)
    player2 = Player(screen, losango2, [textura2], uvs2)

    #Balcão 1
    balcao1 = [(0,530),(250,530),(250,700),(0,700)]
    pr.scan_line_polygon(screen, balcao1, (90, 50, 15))
    pr.polygon(screen, balcao1, (0,0,0))
    """textura1 = pygame.image.load("text_mad_escura.jpg")
    pr.scanline_texture(screen,[(0,530),(250,530),(250,700),(0,700)],[(0,0), (1,0), (1,1), (0,1)], textura1)
    """
    # TEXTURA COXINHA
    
    
    
    #Balcão 2
    balcao2 = [(400,530),(1000,530),(1000,700),(400,700)] 
    pr.scan_line_polygon(screen, balcao2, (192, 192, 192))
    pr.polygon(screen, balcao2, (0,0,0))

    # Coxinha
    text_cox = pygame.image.load("coxinha.jpeg").convert_alpha()

    largura = text_cox.get_width()
    altura = text_cox.get_height()

    for x in range(largura):
        for y in range(altura):
            r, g, b, a = text_cox.get_at((x, y))
            if r > 170 and g > 170 and b > 170:
                text_cox.set_at((x, y), (192, 192, 192, 255))
    pr.scanline_texture(screen,[(655,549),(690,549),(690,579),(655,579)],[(0,0), (1,0), (1,1), (0,1)],text_cox)
    
    
    #Primeira sequência
    pr.line(screen, (430,580), (570,580), (255,255,255))
    pr.line(screen, (600,580), (740,580), (255,255,255))
    pr.line(screen, (770,580), (910, 580), (255,255,255))
    
    #Segunda sequência
    pr.line(screen, (430,620), (570,620), (255,255,255))
    pr.line(screen, (600,620), (740,620), (255,255,255))
    pr.line(screen, (770,620), (910, 620), (255,255,255))
    
    #Terceira sequência
    pr.line(screen, (430,660), (570,660), (255,255,255))
    pr.line(screen, (600,660), (740,660), (255,255,255))
    pr.line(screen, (770,660), (910, 660), (255,255,255))
    
    #Caixa
    caixa = [(45,430),(160,430),(160,530),(45,530)]
    pr.scan_line_polygon(screen, caixa, (200, 220, 230))
    pr.polygon(screen, caixa, (0,0,0))

    fonte1 = pygame.font.SysFont("Arial", 32)
    texto_caixa = fonte1.render("CAIXA", True, (255,255,255))
    screen.blit(texto_caixa, (62, 540))

    fonte3 = pygame.font.SysFont("Arial", 50)
    texto_dinheiro = fonte3.render("$", True, (0,240,0))
    screen.blit(texto_dinheiro, (90, 580))
    

    #Boca do caixa
    pr.scan_line_ellipsis(screen, 17,17, (102,510), (178, 116, 0))
    pr.circle(screen, 17, (102,510), (0, 0, 0))

    # TV
    tv =  [(500,290),(700,290),(700, 390),(500, 390)]
    pr.scan_line_polygon(screen, tv, (0,0,0))
    pr.polygon(screen, tv, (0,0,0))
    
    # Suporte da TV
    suporte_tv = [(597,390),(605,390),(605,400),(665,400),(665,407),(535,407),(535,400),(597,400),(597,390)]
    pr.scan_line_polygon(screen, suporte_tv, (0,0,0))
    pr.polygon(screen, suporte_tv, (0,0,0))

    # Linha para luzes da TV
    line(screen, (500,385),(700, 385), (255,255,255))

    # Luzes TV
    pr.set_pixel(screen, 598, 387, (255,0,0))
    pr.set_pixel(screen, 604, 387, (0,255,0))

    # Prateleira TV
    prateleira_tv = [(500,408),(700,408),(700,422),(680,422),(680,434),(665,434),(665,422),(520,422),(520,434),(535,434),(535,422),(500,422),(500,408)]
    pr.polygon(screen, prateleira_tv, (0,0,0))
    pr.scan_line_polygon(screen, prateleira_tv, (181, 101, 29))


    #Porta
    porta = [(325,315),(470,315),(470,530),(400,530), (400,700), (325, 700), (325,530)]
    pr.polygon(screen, porta, (0,0,0))
    pr.scan_line_polygon(screen, porta, (0,0,0))
    '''
    #Vitrine
    vitrine = [(0,430),(45,430),(45,530),(0,530)]
    pr.scan_line_polygon(screen, vitrine, (245, 245, 220))
    pr.polygon(screen, vitrine, (0,0,0))
    '''
    #Geladeira
    geladeira = [(800,345),(950,345),(950,530),(800,530)]
    pr.scan_line_polygon(screen, geladeira, (240, 80, 80))
    pr.polygon(screen, geladeira, (0,0,0))

    #Maçanetas 1 e 2
    macaneta1 = [(810,415),(830,415),(830,423),(810,423)]
    macaneta2 = [(810,464),(830,464),(830,472),(810,472)]
    pr.scan_line_polygon(screen, macaneta1, (128, 128, 128))
    pr.scan_line_polygon(screen, macaneta2, (128, 128, 128))
    pr.polygon(screen, macaneta1, (0,0,0))
    pr.polygon(screen, macaneta2, (0,0,0))

    #Prateleira
    pateleira_micro = [(550,490),(720,490),(720,505),(550,505)]
    pr.polygon(screen, pateleira_micro, (0,0,0))
    pr.scan_line_polygon(screen, pateleira_micro, (181, 101, 29))

    #Suportes 1 e 2
    suporte1_prateleira =[(580,505),(590,505),(590,515), (580,515)]
    suporte2_prateleira = [(680,505), (690, 505), (690, 515), (680, 515)]
    pr.polygon(screen, suporte1_prateleira, (0,0,0))
    pr.polygon(screen, suporte2_prateleira, (0,0,0))
    pr.scan_line_polygon(screen, suporte1_prateleira, (181, 101, 29))
    pr.scan_line_polygon(screen, suporte2_prateleira, (181, 101, 29))


    #Micro-ondas
    microondas = [(565,445), (665,445), (665,490), (565,490)]
    pr.scan_line_polygon(screen, microondas, (245, 245, 220))
    pr.polygon(screen, microondas, (0,0,0))

    
    #Vidro micro-ondas
    vidro_microondas = [(575,455),(630,455),(630,480),(575,480)]
    pr.scan_line_polygon(screen, vidro_microondas, (200, 220, 230))
    pr.polygon(screen, vidro_microondas, (0,0,0))

    #Suporte micro-ondas
    suporte_microondas = [(634,460),(637,460),(637,475),(634,475)]
    pr.scan_line_polygon(screen, suporte_microondas, (0,0,0))
    pr.scan_line_polygon(screen, suporte_microondas, (0,0,0))


    #Teto
    teto = [(0,0),(1000,0),(1000,125),(0,125)]
    pr.polygon(screen, teto, (0,0,0))
    pr.scan_line_polygon(screen, teto, (120, 70, 20))

    fonte2 = pygame.font.SysFont("Arial", 80)
    texto_teto = fonte2.render("C   A   N   T   I   N   A", True, (255, 200, 100))
    screen.blit(texto_teto, (180, 20))

    #Linha da geladeira
    linha_geladeira =[(800,435), (950,435),(950,440),(800,440)]
    pr.polygon(screen, linha_geladeira, (0,0,0))
    pr.scan_line_polygon(screen, linha_geladeira, (0,0,0))    
    '''
    #Linhas da vitrine
    pr.line(screen, (0,455), (45,455), (0,0,0))
    pr.line(screen, (0, 480),(45,480), (0,0,0))
    pr.line(screen, (0,505), (45,505), (0,0,0))
    '''
    #Boca do caixa
    pr.scan_line_ellipsis(screen, 17,17, (102,510), (200, 140, 30))
    pr.circle(screen, 17, (102,510), (0, 0, 0))

    # Relógio de parede
    pr.circle(screen, 30, (240,360), (0,0,0))
    pr.circle(screen, 25, (240,360), (255,255,255))
    pr.scan_line_ellipsis(screen, 30,30, (240,360), (0,0,0))
    pr.scan_line_ellipsis(screen, 25,25, (240,360), (255,255,255))

    # Ponteiro maior
    pr.line(screen, (240,360), (240, 340), (0,0,0))

    # Ponteiro menor
    pr.line(screen, (240, 360), (252,360), (0,0,0))

    #Salgado
    """
    pr.scan_line_ellipsis(screen, 7,12, (670,566), (230,140,40)) # 8, 12, (670,566)
    pr.scan_line_ellipsis(screen,10,10,(670,570), (230, 140, 40)) # 10,10,(670,570)
    pr.scan_line_ellipsis(screen, 2,2, (670,555), (230,140,40)) # 2,2,(670,554)
    """

    # Papel do salgado
    #papel = [(662,570),(679,570),(676,581),(665,581)]
    #pr.scan_line_polygon(screen,papel, (245, 222, 179))


    #Painel micro-ondas
    painel = [(645,455),(660,455),(660,480),(645,480)]
    pr.scan_line_polygon(screen, painel, (60, 60, 65))
    pr.polygon(screen, painel, (0,0,0))

    #Linhas dos painéis
    #X
    pr.line(screen, (645,465), (660,465), (0,0,0))
    pr.line(screen, (645,470),(660,470),(0,0,0))
    pr.line(screen,(645,475), (660,475),(0,0,0))
    #Y
    pr.line(screen, (650,465),(650,480),(0,0,0))
    pr.line(screen, (655,465),(655,480), (0,0,0))

    # Espelho
    pr.scan_line_polygon(screen, [(715,395), (780,395), (780,480), (715,480)], (101, 67, 33))

    pr.scanline_fill_gradiente(screen,[(720,400), (775,400), (775,475), (720,475)],
    [(248,248,248),(228,235,245),(205,215,228),(182,192,208),(238,242,248),(198,208,222)])

    
    # Lâmpada 1
    base_lamp1 = [(125,125),(141,125),(141,145),(125,145)]
    pr.scan_line_polygon(screen, base_lamp1, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (133,145),(255, 223, 120))
    tr_base1 = [(115,145),(133,133),(152,145)]
    pr.scan_line_polygon(screen, tr_base1, (128, 128, 128))


# Lâmpada 2
    base_lamp2 = [(325,125),(341,125),(341,145),(325,145)]
    pr.scan_line_polygon(screen, base_lamp2, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (333,145),(255, 223, 120))
    tr_base2 = [(315,145),(333,133),(352,145)]
    pr.scan_line_polygon(screen, tr_base2, (128, 128, 128))

# Lâmpada 3
    base_lamp3 = [(491,125),(507,125),(507,145),(491,145)]
    pr.scan_line_polygon(screen, base_lamp3, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (499,145),(255, 223, 120))
    tr_base3 = [(481,145),(499,133),(517,145)]
    pr.scan_line_polygon(screen, tr_base3, (128, 128, 128))

# Lâmpada 4
    base_lamp4 = [(658,125),(674,125),(674,145),(658,145)]
    pr.scan_line_polygon(screen, base_lamp4, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (666,145),(255, 223, 120))
    tr_base4 = [(648,145),(666,133),(685,145)]
    pr.scan_line_polygon(screen, tr_base4, (128, 128, 128))    

# Lâmpada 5
    base_lamp5 = [(858,125),(874,125),(874,145),(858,145)]
    pr.scan_line_polygon(screen, base_lamp5, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (866,145),(255, 223, 120))
    tr_base5 = [(848,145),(866,133),(885,145)]
    pr.scan_line_polygon(screen, tr_base5, (128, 128, 128))

    player1.draw_player()    
    player2.draw_player()    


    #COLORAÇÃO
    """ TABELA DE CORES:
        Prata (silver): RGB(192, 192, 192)
        Marrom claro: RGB(181, 101, 29)
        Branco creme: RGB(245, 245, 220)
        Vidro (translúcido claro): RGB(200, 220, 230)
        Vermelho claro: RGB(255, 102, 102)
        Laranja: RGB(255, 165, 0)     
        Cinza (gray padrão): RGB(128, 128, 128)"""
    
    

    #LINHAS DO BALCÃO 2 (BALCÃO DE SALGADOS)
    #Primeira sequência
    
    # BALCÃO 2
   #  pr.polygon(screen, [(400,530),(1000,530),(1000,700),(400,700)], (255,255,255), False)


    #SUBSTITUIR AS LINHAS POR POLIGONOS, REDESENHAR O MAPA À MÃO E FAZER A MODELAGEM DE CADA DESENHO


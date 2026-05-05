import primitives as pr
from primitives import *
import pygame
from classes import *
from transforms import *

objetos_cenario = [
    {
        "nome": "Balcão 1", ###
        "pontos": [(0, 530), (250, 530), (250, 700), (0, 700)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (90, 50, 15)
    },
    {
        "nome": "Balcão 2", ###
        "pontos": [(400, 530), (1000, 530), (1000, 700), (400, 700)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (192, 192, 192)
    },
    {
        "nome": "Caixa", ###
        "pontos": [(45, 430), (160, 430), (160, 530), (45, 530)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (200, 220, 230)
    },
    {
        "nome": "TV", ###
        "pontos": [(500, 290), (700, 290), (700, 390), (500, 390)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (0, 0, 0)
    },
    {
        "nome": "Suporte da TV", ###
        "pontos": [(597, 390), (605, 390), (605, 400), (665, 400), (665, 407), (535, 407), (535, 400), (597, 400), (597, 390)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (0, 0, 0)
    },
    {
        "nome": "Prateleira TV", ###
        "pontos": [(500, 408), (700, 408), (700, 422), (680, 422), (680, 434), (665, 434), (665, 422), (520, 422), (520, 434), (535, 434), (535, 422), (500, 422), (500, 408)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (181, 101, 29)
    },
    {
        "nome": "Porta", ###
        "pontos": [(325, 315), (470, 315), (470, 530), (400, 530), (400, 700), (325, 700), (325, 530)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (0, 0, 0)
    },
    {
        "nome": "Geladeira", ###
        "pontos": [(800, 345), (950, 345), (950, 530), (800, 530)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (240, 80, 80)
    },
    {
        "nome": "Maçaneta 1", ###
        "pontos": [(810, 415), (830, 415), (830, 423), (810, 423)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (128, 128, 128)
    },
    {
        "nome": "Maçaneta 2", ###
        "pontos": [(810, 464), (830, 464), (830, 472), (810, 472)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (128, 128, 128)
    },
    {
        "nome": "Prateleira", ###
        "pontos": [(550, 490), (720, 490), (720, 505), (550, 505)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (181, 101, 29)
    },
    {
        "nome": "Suporte 1 Prateleira", ###
        "pontos": [(580, 505), (590, 505), (590, 515), (580, 515)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (181, 101, 29)
    },
    {
        "nome": "Suporte 2 Prateleira", ###
        "pontos": [(680, 505), (690, 505), (690, 515), (680, 515)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (181, 101, 29)
    },
    {
        "nome": "Micro-ondas", ###
        "pontos": [(565, 445), (665, 445), (665, 490), (565, 490)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (245, 245, 220)
    },
    {
        "nome": "Vidro micro-ondas", ###
        "pontos": [(575, 455), (630, 455), (630, 480), (575, 480)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (200, 220, 230)
    },
    {
        "nome": "Suporte micro-ondas", ###
        "pontos": [(634, 460), (637, 460), (637, 475), (634, 475)],
        "cor_contorno": None,
        "cor_scanline": (0, 0, 0)
    },
    {
        "nome": "Painel micro-ondas", ###
        "pontos": [(645, 455), (660, 455), (660, 480), (645, 480)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (60, 60, 65)
    },
    {
        "nome": "Teto", ###
        "pontos": [(0, 0), (1000, 0), (1000, 125), (0, 125)],
        "cor_contorno": (0, 0, 0),
        "cor_scanline": (120, 70, 20)
    }
]

miniuv1 = [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]
miniuv2 = [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]

# Controladore de tempo
counter_time = 0

def clock_animation(clock: Clock):
    # 1. Obtém o tempo total em segundos (float para precisão)
    total_seconds = pygame.time.get_ticks() / 1000.0
    
    # 2. Calcula os ângulos absolutos (0 a 360)
    # Ponteiro menor (segundos): dá uma volta (360°) a cada 60 segundos
    # Usamos o operador % 360 para manter o valor limpo, embora math.cos/sin aceitem valores altos
    angle_small = (total_seconds * 0.6) % 360
    
    # Ponteiro maior (minutos): dá uma volta (360°) a cada 3600 segundos (60 min)
    # Dividimos o total_seconds por 60 e multiplicamos por 6 (ou simplesmente total / 10)
    angle_big = (total_seconds * 0.1) % 360

    # 3. Atualiza os ponteiros
    # Importante: Como run_clock usa o ponteiro original para criar o novo, 
    # se você chamar run_clock sucessivamente, ele vai girar cada vez mais rápido.
    # O IDEAL é que o Clock guarde os pontos ORIGINAIS (estáticos) e run_clock
    # aplique a rotação sempre sobre o estado inicial.
    
    clock.run_clock(angle_big, angle_small)

    # 4. Desenha
    clock.draw_clock()

def janela_viewport(janela, viewport, primitive):
    Wxmin, Wymin, Wxmax, Wymax = janela
    Vxmin, Vymin, Vxmax, Vymax = viewport

    # 1. Escala sempre POSITIVA (mantém a orientação da tela do Pygame)
    sx = (Vxmax - Vxmin) / (Wxmax - Wxmin)
    sy = (Vymax - Vymin) / (Wymax - Wymin) 

    # 2. Leva para a origem, escala, e move para a posição da TV
    # Usamos o delta para "ancorar" o desenho no canto (Vxmin, Vymin) da TV
    primitive = create_transform(primitive, 
                                 delta=(Vxmin - Wxmin * sx, Vymin - Wymin * sy), 
                                 scale=(sx, sy))

    return primitive

def minimap(screen, player1:Player, player2:Player):
    janela_mundo = (0, 0, 1000, 700)
    viewport_tv = (500, 290, 700, 390)

    tv = objetos_cenario[3]

    polygon(screen, tv['pontos'], (0,0,0))
    scan_line_polygon(screen, tv['pontos'], (255, 165, 0))

    for obj in objetos_cenario:
        zoom_points = janela_viewport(janela_mundo, viewport_tv, obj['pontos'])
        scan_line_polygon(screen, zoom_points, obj['cor_scanline'])

        if obj['cor_contorno']:
            polygon(screen, zoom_points, obj['cor_contorno'])

    minipol1 = janela_viewport(janela_mundo, viewport_tv, player1.get_polygon())
    minipol2 = janela_viewport(janela_mundo, viewport_tv, player2.get_polygon())

    miniplayer1 = Player(screen, minipol1, [pygame.image.load('coxinha.jpeg')], miniuv1)
    miniplayer2 = Player(screen, minipol2, [pygame.image.load('coxinha.jpeg')], miniuv2)

    miniplayer1.draw_player()
    miniplayer2.draw_player()

def desenhar_mapa(screen, player1:Player, player2:Player):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):
    pygame.init()

    for obj in objetos_cenario:
        scan_line_polygon(screen, obj['pontos'], obj['cor_scanline'])

        if obj['cor_contorno']:
            polygon(screen, obj['pontos'], obj['cor_contorno'])

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
    fonte1 = pygame.font.SysFont("Arial", 32)
    texto_caixa = fonte1.render("CAIXA", True, (255,255,255))
    screen.blit(texto_caixa, (62, 540))

    fonte3 = pygame.font.SysFont("Arial", 50)
    texto_dinheiro = fonte3.render("$", True, (0,240,0))
    screen.blit(texto_dinheiro, (90, 580))
    

    #Boca do caixa
    pr.scan_line_ellipsis(screen, 17,17, (102,510), (178, 116, 0))
    pr.circle(screen, 17, (102,510), (0, 0, 0))

    # Linha para luzes da TV
    line(screen, (500,385),(700, 385), (255,255,255))

    # Luzes TV
    pr.set_pixel(screen, 598, 387, (255,0,0))
    pr.set_pixel(screen, 604, 387, (0,255,0))

    '''
    #Vitrine
    vitrine = [(0,430),(45,430),(45,530),(0,530)]
    pr.scan_line_polygon(screen, vitrine, (245, 245, 220))
    pr.polygon(screen, vitrine, (0,0,0))
    '''

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
    clock = Clock(screen, [(240,360), (240, 340)], [(240, 360), (252,360)], (240, 360))
    clock_animation(clock)

    #Salgado
    """
    pr.scan_line_ellipsis(screen, 7,12, (670,566), (230,140,40)) # 8, 12, (670,566)
    pr.scan_line_ellipsis(screen,10,10,(670,570), (230, 140, 40)) # 10,10,(670,570)
    pr.scan_line_ellipsis(screen, 2,2, (670,555), (230,140,40)) # 2,2,(670,554)
    """

    # Papel do salgado
    #papel = [(662,570),(679,570),(676,581),(665,581)]
    #pr.scan_line_polygon(screen,papel, (245, 222, 179))

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

    #Mini mapa
    minimap(screen, player1, player2)

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


import primitives as pr
from primitives import *
 
def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):

    #Balcão 1
    balcao1 = [(0,530),(250,530),(250,700),(0,700)]
    pr.scan_line_polygon(screen, balcao1, (90, 50, 15))
    pr.polygon(screen, balcao1, (0,0,0))

    #Balcão 2
    balcao2 = [(400,530),(1000,530),(1000,700),(400,700)] 
    pr.scan_line_polygon(screen, balcao2, (192, 192, 192))
    pr.polygon(screen, balcao2, (0,0,0))

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

    #Vitrine
    vitrine = [(0,430),(45,430),(45,530),(0,530)]
    pr.scan_line_polygon(screen, vitrine, (245, 245, 220))
    pr.polygon(screen, vitrine, (0,0,0))

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

    #Linha da geladeira
    linha_geladeira =[(800,435), (950,435),(950,440),(800,440)]
    pr.polygon(screen, linha_geladeira, (0,0,0))
    pr.scan_line_polygon(screen, linha_geladeira, (0,0,0))    
    
    #Linhas da vitrine
    pr.line(screen, (0,455), (45,455), (0,0,0))
    pr.line(screen, (0, 480),(45,480), (0,0,0))
    pr.line(screen, (0,505), (45,505), (0,0,0))
    
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
    pr.scan_line_ellipsis(screen, 7,12, (670,566), (230,140,40)) # 8, 12, (670,566)
    pr.scan_line_ellipsis(screen,10,10,(670,570), (230, 140, 40)) # 10,10,(670,570)
    pr.scan_line_ellipsis(screen, 2,2, (670,555), (230,140,40)) # 2,2,(670,554)


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

    # Lâmpada 1
    base_lamp1 = [(125,125),(141,125),(141,165),(125,165)]
    pr.scan_line_polygon(screen, base_lamp1, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (133,165),(255, 223, 120))
    tr_base1 = [(115,165),(133,152),(152,165)]
    pr.scan_line_polygon(screen, tr_base1, (128, 128, 128))


    # Lâmpada 2
    base_lamp2 = [(325,125),(341,125),(341,165),(325,165)]
    pr.scan_line_polygon(screen, base_lamp2, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (333,165),(255, 223, 120))
    tr_base2 = [(315,165),(333,152),(352,165)]
    pr.scan_line_polygon(screen, tr_base2, (128, 128, 128))
    
    # Lâmpada 3
    base_lamp3 = [(491,125),(507,125),(507,165),(491,165)]
    pr.scan_line_polygon(screen, base_lamp3, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (499,165),(255, 223, 120))
    tr_base3 = [(481,165),(499,152),(517,165)]
    pr.scan_line_polygon(screen, tr_base3, (128, 128, 128))

    # Lâmpada 4
    base_lamp4 = [(658,125),(674,125),(674,165),(658,165)]
    pr.scan_line_polygon(screen, base_lamp4, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (666,165),(255, 223, 120))
    tr_base4 = [(648,165),(666,152),(685,165)]
    pr.scan_line_polygon(screen, tr_base4, (128, 128, 128))    

    # Lâmpada 5
    base_lamp5 = [(858,125),(874,125),(874,165),(858,165)]
    pr.scan_line_polygon(screen, base_lamp5, (128, 128, 128))
    pr.scan_line_ellipsis(screen, 8,8, (866,165),(255, 223, 120))
    tr_base5 = [(848,165),(866,152),(885,165)]
    pr.scan_line_polygon(screen, tr_base5, (128, 128, 128)) 

    # Efeito da Luz (Aplicação do Gradiente)
    """pr.scanline_fill_gradiente(screen, [(0,125),(999,125),(999,240),(0,240)],[
        (245,235,150), 
        (245,235,150),
        (210,160,55),  
        (210,160,55)
    ])"""


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